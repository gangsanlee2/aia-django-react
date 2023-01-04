import os.path
import warnings

import pandas as pd
from prophet import Prophet
from tensorflow import keras

from admin.path import dir_path
from basic.dlearn.aitrader.models import DnnModel, LstmModel, DnnEnsemble, LstmEnsemble

warnings.filterwarnings("ignore")
from pandas_datareader import data
import yfinance as yf
yf.pdr_override()   # TypeError: string indices must be integers 해결법

path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc, pyplot as plt

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
plt.rcParams['axes.unicode_minus'] = False

'''
Date    Open     High      Low    Close     Adj Close   Volume                                                                 
'''

class AiTraderService(object):

    def __init__(self):
        global start_date, end_date, item_code
        start_date = "2019-1-4"
        end_date = "2022-12-30"
        item_code = "000270.KS" # kia 종목코드 (KS:코스피)

    def hook(self):
        item = data.get_data_yahoo(item_code, start=start_date, end=end_date)
        print(type(item))
        print(f"KIA head:\n {item.head(3)}")
        print(f"KIA tail:\n {item.tail(3)}")
        item['Close'].plot(figsize=(12,6), grid=True)
        item_trunc = item[:"2023-12-31"]
        df = pd.DataFrame({"ds": item_trunc.index, "y": item_trunc["Close"]})
        df.reset_index(inplace=True)
        del df["Date"]
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(df)
        future = prophet.make_future_dataframe(periods=61)
        forecast = prophet.predict(future)
        prophet.plot(forecast)
        plt.figure(figsize=(12,6))
        plt.plot(item.index, item["Close"], label="real")
        plt.plot(forecast["ds"], forecast["yhat"], label="forecast")
        plt.grid()
        plt.legend()
        plt.savefig(os.path.join(dir_path("aitrader"), "kia_close.png"))
        plt.show()

    def pred_dnn(self, param):
        ai = DnnModel()
        x_train_scaled, x_test_scaled, y_train, y_test = ai.data_scaling(ai.load_numpy()[0])
        model = keras.models.load_model(os.path.join(dir_path('aitrader'), "save", "dnn.h5"))
        predict = model.predict(x_test_scaled)
        return str(predict[int(param)][0])

    def pred_lstm(self, param):
        ai = LstmModel()
        x_train_scaled, x_test_scaled, y_train, y_test = ai.data_scaling(ai.load_numpy()[0])
        model = keras.models.load_model(os.path.join(dir_path('aitrader'), "save", "lstm.h5"))
        predict = model.predict(x_test_scaled)
        return str(predict[int(param)][0])

    def pred_dnn_ensemble(self, param):
        ai = DnnEnsemble()
        x1_train_scaled, x1_test_scaled, y1_train, y1_test = ai.data_scaling(ai.load_numpy()[0])
        x2_train_scaled, x2_test_scaled, y2_train, y2_test = ai.data_scaling(ai.load_numpy()[1])
        x1_train_scaled, x1_test_scaled = ai.back_to_3d(x1_train_scaled, x1_test_scaled)
        x2_train_scaled, x2_test_scaled = ai.back_to_3d(x2_train_scaled, x2_test_scaled)
        model = keras.models.load_model(os.path.join(dir_path('aitrader'), "save", "dnn_ensemble.h5"))
        predict = model.predict([x1_test_scaled, x2_test_scaled])
        return str(predict[int(param)][0])

    def pred_lstm_ensemble(self, param):
        ai = LstmEnsemble()
        x1_train_scaled, x1_test_scaled, y1_train, y1_test = ai.data_scaling(ai.load_numpy()[0])
        x2_train_scaled, x2_test_scaled, y2_train, y2_test = ai.data_scaling(ai.load_numpy()[1])
        x1_train_scaled, x1_test_scaled = ai.back_to_3d(x1_train_scaled, x1_test_scaled)
        x2_train_scaled, x2_test_scaled = ai.back_to_3d(x2_train_scaled, x2_test_scaled)
        model = keras.models.load_model(os.path.join(dir_path('aitrader'), "save", "lstm_ensemble.h5"))
        #pred = model.predict([x1_test_scaled[[int(param)].reshape(1, 5, 5), x2_test_scaled[[int(param)].reshape(1, 5, 5)])
        predict = model.predict([x1_test_scaled, x2_test_scaled])
        return str(predict[int(param)][0])

