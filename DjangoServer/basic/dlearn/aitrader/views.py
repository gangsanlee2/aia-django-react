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
    result = service.predict(data)
    print("### here 4 ###")
    return JsonResponse({'result': result})