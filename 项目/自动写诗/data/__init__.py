# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午5:41
# @Author  : ZZZ
# @Email   : zuxinxing531@pingan.com.cn
# @File    : _init_.py
# @Software: 自动写诗
# @Descript: _init_

import numpy as np
class Data():
    ## 1. 读取文件
    ## 1. 构建poems,保存每首诗
    ## 1. 构建dict,使用one-hot进行编码
    def __init__(self,filename,batch_size,seq_len,pickleFile="./data/poem_list.pickle"):
        self.filename = filename
        self.batch_size = batch_size
        self.max_seq_len = seq_len
        self.pickleFile = pickleFile

    def prepare_data(self):
        import os
        import pickle
        if os.path.exists(self.pickleFile):
            print("import data...")
            with open(self.pickleFile, 'rb') as f:
                self.poems_list = pickle.load(f)
        else:
            print("processing data...")
            import codecs
            with codecs.open(self.filename, 'r', 'utf-8') as f:
                self.poems_list = []
                for line in f:
                    if len(line.strip())>5:
                        self.poems_list.append(line.strip())
            with open(self.pickleFile,'wb') as f:
                pickle.dump(self.poems_list,f)

        print "poems:",len(self.poems_list)

        self.words = set(''.join(self.poems_list)+' ')

        self.word2code = {w: i for i, w in enumerate(self.words)}
        self.code2word = {i: w for i, w in enumerate(self.words)}
        self.to_code = lambda w: self.word2code.get(w, self.word2code[" "])

        self.word2vec = {}
        for i,w in enumerate(self.words):
            self.word2vec[w] = np.zeros(shape=(len(self.words)),dtype=np.int32)
            self.word2vec[w][self.to_code(w)] = 1.0
        self.to_vec = lambda w: self.word2vec.get(w, self.word2vec[" "])

    def data_generator(self):
        import random
        from keras.preprocessing.sequence import pad_sequences
        from keras.utils import np_utils

        is_poem_ending = 1

        while (True):
            # 当遍历完所有诗之后,将顺序随机打乱
            if is_poem_ending == 1:
                is_poem_ending = 0
                random.shuffle(self.poems_list)

                poem_index = 0
                start = 0
                # 挑选一首诗
                c_poem = self.poems_list[poem_index]

            x_input = []
            y_label = []

            for k in range(self.batch_size):
                # 从诗中挑出一段随机长度的连续内容
                end = max(start+np.random.randint(self.max_seq_len),start+1)
                end = min(end,len(c_poem)-1)
                x_input.append([self.to_code(item) for item in c_poem[start:end]])
                # y_label.append([self.to_code(c_poem[end])])
                try:
                    y = c_poem[end]
                except:
                    print len(c_poem),":",end,":",c_poem

                y_label.append(self.to_vec(y))

                if end >= len(c_poem)-1:
                    poem_index += 1
                    start = 0
                    end = 0
                    c_poem = self.poems_list[poem_index]

                    if poem_index>len(self.poems_list)-self.batch_size-1:
                        is_poem_ending = 1

                start = end
            x_input = pad_sequences(x_input,maxlen=self.max_seq_len,value=self.to_code(' '))
            x_input = x_input.reshape(self.batch_size,self.max_seq_len,1)
            x_input = x_input/float(len(self.words))
            y_label = np.array(y_label)
            yield x_input,y_label#,np_utils.to_categorical(y_label)

    def get_data(self,data_size):
        data_input = []
        data_label = []
        i = 0
        for x,y in self.data_generator():
            data_input.append(x)
            data_label.append(y)
            i += 1
            if i>=data_size:break;
        data_input = np.array(data_input)
        data_input = data_input.reshape((data_size,self.max_seq_len,1))
        data_label = np.array(data_label)
        data_label = data_label.reshape((data_size,len(self.words)))
        print "training data: ",data_input.shape,"---",data_label.shape
        return data_input,data_label

if __name__ == "__main__":
    data = Data(filename="poetry_little.txt",
                batch_size=1,
                seq_len=6,
                pickleFile="poem_list.pickle")
    a = list("asdfghjkl")
    data.prepare_data()
    i = 1
    # data.get_data(50000)
    for x,z in data.data_generator():
        i+=1
        print x.shape,":",z.shape
        result = ""
        for j in range(x.shape[1]):
            result += data.code2word[int(x[0,j,0]*len(data.words))]

        index = np.argmax(z)
        print result,":",data.code2word[index]
    #
    #     # for
    #     # for j,c in enumerate(x):
    #     #     print j,":",c,":",z[j]
    #         # print str(j)+":"+''.join(c)+":"+''.join(y[j])
        if i>10:break;