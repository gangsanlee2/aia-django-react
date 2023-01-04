from basic.dlearn.aitrader.services import AiTraderService

if __name__ == '__main__':
    ai = AiTraderService()
    print(f'type(ai.pred_dnn(0)) is {type(ai.pred_dnn(0))}')
    print(ai.pred_dnn(0))
    print(f'type(ai.pred_lstm(0)) is {type(ai.pred_lstm(0))}')
    print(ai.pred_lstm(0))
    print(f'type(ai.pred_dnn_ensemble(0)) is {type(ai.pred_dnn_ensemble(0))}')
    print(ai.pred_dnn_ensemble(0))
    print(f'type(ai.pred_lstm_ensemble(0)) is {type(ai.pred_lstm_ensemble(0))}')
    print(ai.pred_lstm_ensemble(0))