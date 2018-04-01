# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午5:43
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : __init__.py
# @Software: 自动写诗
# @Descript: __init__

from keras import models
from keras import layers
from keras import optimizers
class Model():
    def __init__(self):
        pass

    def build_model(shape,learning_rate):
        input = layers.Input(shape=shape)
        lstm = layers.LSTM(512,return_sequences=True)(input)
        dropout = layers.Dropout(0.6)(lstm)
        lstm = layers.LSTM(256)(dropout)
        dropout = layers.Dropout(0.6)(lstm)
        dense = layers.Dense(shape[1], activation='softmax')(dropout)
        model = models.Model(inputs=input, outputs=dense)
        optimizer = optimizers.Adam(lr=learning_rate)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return model

