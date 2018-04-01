# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午5:39
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : main.py
# @Software: 自动写诗
# @Descript: main

from data import Data
from model import Model
from train import run_train,run_val
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout
import keras

class Config():
    filename = "./data/poetry_little.txt"
    batch_size = 1
    learning_rate = 0.01
    seq_len = 6
    model_weights = "model_weights.h5"

if __name__ == "__main__":
    import sys
    import os
    import numpy as np
    from keras.preprocessing.sequence import pad_sequences
    # type =  sys.argv[1]
    # type = "run"
    type = "train"


    data = Data(filename=Config.filename,
                batch_size=Config.batch_size,
                seq_len=Config.seq_len)

    data.prepare_data()
    x_data,y_data = data.get_data(500)

    for i in range(x_data.shape[0]):
        result = ""
        for j in range(x_data.shape[1]):
            result += data.code2word[int(x_data[i, j, 0] * len(data.words))]
        index = np.argmax(y_data[i])
        print i,":",result, "——", data.code2word[index]

    if os.path.exists(Config.model_weights):
        from keras.models import load_model
        model = load_model(Config.model_weights)
    else:
        model = Sequential()
        # model.add(LSTM(128, return_sequences=True,input_shape=(Config.seq_len, 1)))
        model.add(LSTM(32, return_sequences=True,input_shape=(Config.seq_len, 1)))
        model.add(Dropout(0.4))
        model.add(LSTM(32))
        model.add(Dropout(0.4))
        model.add(Dense(len(data.words), activation='softmax'))
    adam = keras.optimizers.Adam(lr=Config.learning_rate)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    # model.fit_generator(data.data_generator(), epochs=5,steps_per_epoch=100, verbose=2)
    model.fit(x_data,y_data,epochs=50,batch_size=Config.batch_size,verbose=2, callbacks=[
            keras.callbacks.ModelCheckpoint(Config.model_weights, save_weights_only=False),
        ])

    # x_input = [[np.random.randint(len(data.words))]]
    # print data.code2word[x_input[0][0]]
    # for i in range(40):
    #     # x_input = pad_sequences(x_input, maxlen=data.max_seq_len, value=data.to_code(' '))
    #     # x_input = x_input.reshape(1, data.max_seq_len, 1)
    #     # x_input = x_input / float(len(data.words))
    #     x_input = x_data[np.random.randint(500)]
    #     x_input = x_input.reshape(1, data.max_seq_len, 1)
    #     prediction = model.predict(x_input,verbose=0)
    #     index = np.argmax(prediction)
    #
    #     result = data.code2word[index]
    #     x_out = ""
    #     for j in range(x_input.shape[1]):
    #         x_out += data.code2word[int(x_input[0, j, 0] * len(data.words))]
    #     print index,":",x_out,'——',result

    x_input = [[np.random.randint(len(data.words))]]
    result = data.code2word[x_input[0][0]]
    for i in range(80):
        x_pre = pad_sequences([x_input], maxlen=data.max_seq_len, value=data.to_code(' '))
        x_pre = x_pre.reshape(1, data.max_seq_len, 1)
        x_pre = x_pre / float(len(data.words))

        prediction = model.predict(x_pre, verbose=0)
        index = np.argmax(prediction)
        result += data.code2word[index]
        x_input.append([index])
        if len(x_input)>data.max_seq_len:
            x_input = x_input[1:]

    print result




        # model = Model()
    # model.build_model((data.max_length,len(data.word2code)),0.01)
    #
    # run_train(model,data,data.poems_codes,batch_size=batch_size,epochs=100)