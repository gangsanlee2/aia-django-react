from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from security.z_users.repositories import UserRepository
from security.z_users.serializers import UserSerializer
from rest_framework.response import Response

@api_view(['Post', 'PUT', 'PATCH', 'DELETE', 'GET'])
def user(request):
    if request.method == 'POST':
        new_user = request.data
        print(f' 리액트에서 등록한 신규 사용자 ')
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result":"SUCCESS"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        repo = UserRepository()
        modify_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(modify_user.id)
        serializer = UserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user, db_user)
            return JsonResponse({"result":"SUCCESS"})
    elif request.method == 'PATCH':
        return None
    elif request.method == 'DELETE':
        repo = UserRepository()
        delete_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(delete_user.id)
        db_user.delete()
        return JsonResponse({"result":"SUCCESS"})
    elif request.method == 'GET':
        return Response(UserRepository().find_user_by_email(request.data["user_email"]))

@api_view(['GET'])
def user_list(request): return Response(UserSerializer(UserRepository().get_all(), many=True).data)

@api_view(['Post'])
def login(request): return UserRepository().login(request.data)

@api_view(['GET'])
def user_list_by_name(request): return UserRepository().find_users_by_name(request.data["user_name"])