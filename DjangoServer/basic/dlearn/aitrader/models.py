import os.path
from enum import Enum

import numpy as np
import pandas as pd
from keras import Sequential, Input, Model
from keras.callbacks import EarlyStopping
from keras.layers import Dense, LSTM, concatenate
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
from admin.path import dir_path
from abc import abstractmethod, ABCMeta

class ModelType(Enum):
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4

class H5FileNames(Enum):
    dnn_model = "samsung_stock_dnn_model.h5"
    dnn_ensemble = "samsung_stock_dnn_ensemble.h5"
    lstm_model = "samsung_stock_lstm_model.h5"
    lstm_ensemble = "samsung_stock_lstm_ensemble.h5"

class Activations(Enum):
    relu = 'relu'

class AiTraderBase(metaclass=ABCMeta):
    @abstractmethod
    def show_csv(self, **kwargs):
        pass
    @abstractmethod
    def create(self):
        pass
    @abstractmethod
    def data_trimming(self):
        pass
    @abstractmethod
    def to_numpy(self):
        pass
    @abstractmethod
    def load_numpy(self):
        pass
    @abstractmethod
    def data_scaling(self, param):
        pass
    @abstractmethod
    def back_to_3d(self, *params):
        pass
    @abstractmethod
    def fit(self,*params):
        pass
    @abstractmethod
    def merge_model(self, *params):
        pass

class AiTraderModel(AiTraderBase):
    def __init__(self):
        global df_samsung, df_kospi, np_samsung, np_kospi
        df_samsung = pd.read_csv(os.path.join(dir_path("aitrader"), "data", "삼성전자.csv"), index_col=0, header=0, sep=',')
        df_kospi = pd.read_csv(os.path.join(dir_path("aitrader"), "data", "코스피200.csv"), index_col=0, header=0, sep=',')
        np_samsung = os.path.join(dir_path('aitrader'), "save", "samsung.npy")
        np_kospi = os.path.join(dir_path('aitrader'), "save", "kospi200.npy")
        self.df_ss = None
        self.df_ko = None

    def show_csv(self):
        print(" ##### kospi ##### ")
        print(df_kospi)
        print(df_kospi.shape)
        print(" ##### samsung ##### ")
        print(df_samsung)
        print(df_samsung.shape)

    def data_trimming(self):
        '''
        DF에서 loc는 키 값으로 검색 하고 iloc는 인덱스 값으로 검색한다. 따라서 loc는 세로 방향을, iloc는 가로 방향으로 검색한다.
        '''
        for i in range(len(df_kospi.index)):
            if "M" in df_kospi.iloc[i,4]:
                df_kospi.iloc[i,4] = df_kospi.iloc[i,4].replace('M','')
                df_kospi.iloc[i,4] = int(float(df_kospi.iloc[i,4]) * 1000000)
            elif "K" in df_kospi.iloc[i,4]:
                df_kospi.iloc[i,4] = df_kospi.iloc[i,4].replace('K','')
                df_kospi.iloc[i,4] = int(float(df_kospi.iloc[i,4]) * 1000)
        df_ss = df_samsung.dropna()
        for i in range(len(df_ss.index)):
            for j in range(len(df_ss.iloc[i])):
                if ',' in df_ss.iloc[i,j]:
                    df_ss.iloc[i,j] = int(df_ss.iloc[i,j].replace(',',''))
                elif "M" in df_ss.iloc[i,j]:
                    df_ss.iloc[i, j] = df_ss.iloc[i, j].replace('M','')
                    df_ss.iloc[i, j] = int(float(df_ss.iloc[i, j]) * 1000000)
                elif "K" in df_ss.iloc[i, j]:
                    df_ss.iloc[i, j] = df_ss.iloc[i, j].replace('K', '')
                    df_ss.iloc[i, j] = int(float(df_ss.iloc[i, j]) * 1000)
        df_ko = df_kospi.sort_values(['날짜'], ascending=[True])
        df_ss = df_ss.sort_values(['날짜'], ascending=[True])
        df_ko.drop(["변동 %"], axis=1, inplace=True)
        df_ss.drop(["변동 %"], axis=1, inplace=True)
        self.df_ko = df_ko
        self.df_ss = df_ss

    def to_numpy(self):
        df_ko = self.df_ko.to_numpy()
        df_ss = self.df_ss.to_numpy()
        np.save(np_kospi, arr=df_ko)
        np.save(np_samsung, arr=df_ss)

    def load_numpy(self):
        samsung = np.load(np_samsung, allow_pickle=True)
        kospi200 = np.load(np_kospi, allow_pickle=True)
        return samsung, kospi200

    def split_xy5(self, **kwargs):
        dataset = kwargs['dataset']
        time_steps = kwargs['time_steps']
        y_column = kwargs['y_column']
        x, y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column
            if y_end_number > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :]
            tmp_y = dataset[x_end_number:y_end_number, 0]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    def data_scaling(self, loaded_numpy):
        x, y = self.split_xy5(dataset=loaded_numpy, time_steps=5, y_column=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        x_train_2d = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test_2d = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        scaler = StandardScaler()
        scaler.fit(x_train_2d)
        x_train_scaled = scaler.transform(x_train_2d)
        x_test_scaled = scaler.transform(x_test_2d)
        x_train_scaled = x_train_scaled.astype(float)
        x_test_scaled = x_test_scaled.astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)
        return x_train_scaled, x_test_scaled, y_train, y_test

    def back_to_3d(self, x_train_scaled, x_test_scaled):
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 5, 5))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 5, 5))
        return x_train_scaled, x_test_scaled

    def fit(self, model, x_train_scaled, y_train, x_test_scaled, y_test, h5_fname):
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print(f"loss : {loss}")
        print(f"mse : {mse}")
        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print(f'종가 : {y_test[i]} / 예측가 : {y_pred[i]}')
        model.save(os.path.join(dir_path('aitrader'), "save", h5_fname))

    def merge_model(self, input1, input2, output1, output2):
        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)
        return model

class DnnModel(AiTraderModel):
    def create(self):
        x_train_scaled, x_test_scaled, y_train, y_test = self.data_scaling(self.load_numpy()[0])

        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))

        self.fit(model, x_train_scaled, y_train, x_test_scaled, y_test, H5FileNames.dnn_model.value)

class LstmModel(AiTraderModel):
    def create(self):
        x_train_scaled, x_test_scaled, y_train, y_test = self.data_scaling(self.load_numpy()[0])
        x_train_scaled, x_test_scaled = self.back_to_3d(x_train_scaled, x_test_scaled)

        model = Sequential()
        model.add(LSTM(64, input_shape=(5,5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))

        self.fit(model, x_train_scaled, y_train, x_test_scaled, y_test, H5FileNames.lstm_model.value)

class DnnEnsemble(AiTraderModel):
    def create(self):
        x1_train_scaled, x1_test_scaled, y1_train, y1_test = self.data_scaling(self.load_numpy()[0])
        x2_train_scaled, x2_test_scaled, y2_train, y2_test = self.data_scaling(self.load_numpy()[1])

        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        model = self.merge_model(input1, input2, output1, output2)
        self.fit(model, [x1_train_scaled, x2_train_scaled], y1_train, [x1_test_scaled, x2_test_scaled], y1_test, H5FileNames.dnn_ensemble.value)

class LstmEnsemble(AiTraderModel):
    def create(self):
        x1_train_scaled, x1_test_scaled, y1_train, y1_test = self.data_scaling(self.load_numpy()[0])
        x2_train_scaled, x2_test_scaled, y2_train, y2_test = self.data_scaling(self.load_numpy()[1])
        x1_train_scaled, x1_test_scaled = self.back_to_3d(x1_train_scaled, x1_test_scaled)
        x2_train_scaled, x2_test_scaled = self.back_to_3d(x2_train_scaled, x2_test_scaled)

        input1 = Input(shape=(5,5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(5,5))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        model = self.merge_model(input1, input2, output1, output2)
        self.fit(model, [x1_train_scaled, x2_train_scaled], y1_train, [x1_test_scaled, x2_test_scaled], y1_test, H5FileNames.lstm_ensemble.value)
