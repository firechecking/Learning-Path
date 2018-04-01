# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 下午2:44
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : main.py
# @Software: CartPole
# @Descript: main

import game2048 as game
import time
import thread
from collections import deque

import random
import numpy as np

import json
import keras
from keras import initializers
from keras.initializers import normal, identity
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD , Adam
import tensorflow as tf


GAME = 'bird' # the name of the game being played for log files
CONFIG = 'nothreshold'
ACTIONS = 4 # number of valid actions
GAMMA = 0.9 # decay rate of past observations
OBSERVATION = 33#3200. # timesteps to observe before training
EXPLORE = 3000000. # frames over which to anneal epsilon
FINAL_EPSILON = 0.001 # final value of epsilon
INITIAL_EPSILON = 0.1 # starting value of epsilon
REPLAY_MEMORY = 50000 # number of previous transitions to remember
BATCH = 32 # size of minibatch
FRAME_PER_ACTION = 1
LEARNING_RATE = 1e-4


## score
# 1:最大数+1
# -1:游戏结束
# 0:和上一次举证无变化
# 0.1:移动一次,并且游戏未结束,最大数没变化

def buildmodel():
    print("Now we build the model")
    model = Sequential()
    model.add(Dense(32,input_dim=16))  # 4*4
    model.add(Activation('relu'))

    model.add(Dense(10))
    model.add(Activation('relu'))

    model.add(Dropout(0.25))

    model.add(Dense(30))
    model.add(Activation('relu'))

    # model.add(Dropout(0.5))

    model.add(Dense(4))

    adam = Adam(lr=LEARNING_RATE)
    model.compile(loss='mse', optimizer=adam)
    print("We finish building the model")
    return model

def DQN(model,type="run"):
    import os
    if os.path.exists("model.h5"):
        print ("Now we load weight")
        model = keras.models.load_model("model.h5")
        adam = Adam(lr=LEARNING_RATE)
        model.compile(loss='mse', optimizer=adam)
        print ("Weight load successfully")

    a_t = ("up", "down", "left", "right","none")
    D = deque()
    s_t,score_0,terminal=game.game_update(a_t[4])
    s_t = np.array(s_t)
    s_t[s_t < 2] = 1
    s_t = np.log2(s_t)

    s_t = s_t.reshape(1,s_t.shape[0]*s_t.shape[1])

    if type == "run":
        OBSERVE = 999999999  # We keep observe, never train
        epsilon = FINAL_EPSILON
    else:  # We go to training mode
        OBSERVE = OBSERVATION
        epsilon = INITIAL_EPSILON

    t = 0
    while (True):
        loss = 0
        Q_sa = 0
        a_t_i = 0
        r_t = 0

        # e-greedy:以一定概率进行随机动作,否则进行最优动作
        if random.random() <= epsilon:
            # print("----------Random Action----------")
            a_t_i = random.randrange(len(a_t)-1)
        else:
            q = model.predict(s_t)  # input a stack of 4 images, get the prediction
            a_t_i = np.argmax(q)

        if epsilon > FINAL_EPSILON and t > OBSERVE:
            epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE

        s_t1, score_1, terminal = game.game_update(a_t[a_t_i])

        if type == "run":
            time.sleep(0.1)
            print a_t[a_t_i],":",score_1
        if t % 500 == 0:
            game.restart()

        s_t1 = np.array(s_t1)
        s_t1[s_t1 < 2] = 1
        s_t1 = np.log2(s_t1)

        s_t1 = s_t1.reshape(1, s_t1.shape[0]*s_t1.shape[1])
        if terminal:
            r_t = -1
            game.restart();
        elif score_1>score_0:
            r_t = 0.1
        elif s_t.all() == s_t1.all():
            r_t = -0.5
        else:
            r_t = 0

        score_0 = score_1

        D.append((s_t, a_t_i, r_t, s_t1, terminal))
        if len(D) > REPLAY_MEMORY:
            D.popleft()
        if t > OBSERVE:
            #当t超过观察次数后,进行train
            minibatch = random.sample(D, BATCH)

            inputs = np.zeros((BATCH, s_t.shape[1]))  # 32, 16
            targets = np.zeros((inputs.shape[0], ACTIONS))  # 32, 4

            for i in range(0, len(minibatch)):
                state_t = minibatch[i][0]
                action_t = minibatch[i][1]  # This is action index
                reward_t = minibatch[i][2]
                state_t1 = minibatch[i][3]
                terminal = minibatch[i][4]
                # if terminated, only equals reward

                inputs[i] = state_t  # I saved down s_t

                targets[i] = model.predict(state_t)  # Hitting each buttom probability
                Q_sa = model.predict(state_t1)

                if terminal:
                    targets[i, action_t] = reward_t
                else:
                    targets[i, action_t] = reward_t + GAMMA * np.max(Q_sa)
                    # print(targets[i, action_t], reward_t, GAMMA * np.max(Q_sa))

            # targets2 = normalize(targets)
            loss += model.train_on_batch(inputs, targets)

        s_t = s_t1
        t = t + 1



        # print info
        state = ""
        if t <= OBSERVE:
            state = "observe"
        elif t > OBSERVE and t <= OBSERVE + EXPLORE:
            state = "explore"
        else:
            state = "train"

        # save progress every 10000 iterations
        if t % 1000 == 0:
            print("Now we save model")
            model.save("model.h5")
            # model.save_weights("model.h5", overwrite=True)
            with open("model.json", "w") as outfile:
                json.dump(model.to_json(), outfile)
            print("TIMESTEP", t, "/ STATE", state, \
              "/ EPSILON", epsilon, "/ ACTION", a_t[a_t_i], "/ REWARD", r_t, \
              "/ Q_MAX ", np.max(Q_sa), "/ Loss ", loss,"/ Score ",score_0,"/ Terminal ",terminal)
            oo = np.power(2, s_t)
            oo[oo<2] = 0
            print oo.reshape((4,4))

    print("Episode finished!")
    print("************************")


if __name__ == "__main__":
    import sys
    # type =  sys.argv[1]
    # type = "run"
    type = "train"
    print type
    game.main(type)
    model = buildmodel()
    DQN(model,type)