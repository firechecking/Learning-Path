# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午5:44
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : __init__.py
# @Software: 自动写诗
# @Descript: __init__

import keras

def run_train(model,data,poems_codes,batch_size,epochs):
    model.fit_generator(generator=data.data_generator(),
                        steps_per_epoch=len(poems_codes)/batch_size-1,
                        verbose=True,
                        epochs=epochs,
                        callbacks=
                        [
                            keras.callbacks.ModelCheckpoint("./model/weight.h5", save_weights_only=False),
                            keras.callbacks.LambdaCallback(on_epoch_end=run_val)
                        ]
                        )

def run_val(epoch,logs):
    print "hello"