import json
from django.http import JsonResponse
from rest_framework.decorators import api_view

from basic.dlearn.aitrader.services import AiTraderService


@api_view(['POST'])
def aitrader(request):
    print("### here 1 ###")
    data = json.loads(request.body)
    print("### here 2 ###")
    service = AiTraderService()
    print("### here 3 ###")
    label = service.label(data)
    result_dnn = service.pred_dnn(data)
    result_lstm = service.pred_lstm(data)
    result_dnn_ensemble = service.pred_dnn_ensemble(data)
    result_lstm_ensemble = service.pred_lstm_ensemble(data)
    print("### here 4 ###")
    return JsonResponse({'label': label,
                         'result_dnn': result_dnn,
                         'result_lstm': result_lstm,
                         'result_dnn_ensemble': result_dnn_ensemble,
                         'result_lstm_ensemble': result_lstm_ensemble,
                         })
