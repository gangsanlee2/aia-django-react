from django.http import JsonResponse
from rest_framework.response import Response
from security.z_users.models import User
from security.z_users.serializers import UserSerializer


class UserRepository(object):
    def __init__(self):
        print("UserRepository 객체 생성")

    def login(self, login_info):
        loginUser = User.objects.get(user_email=login_info['user_email'])
        print(f"해당 email 을 가진  User ID: *** \n {loginUser.id}")
        if loginUser.password == login_info['password']:
            dbUser = self.find_by_id(loginUser.id)
            print(f" DBUser is {dbUser}")
            serializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        # dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
        else:
            return JsonResponse({"data": "WRONG_PASSWORD"})

    def get_all(self):
        return User.objects.all()

    def find_by_id(self, id):
        return User.objects.all().filter(id=id).values()[0]

    def find_user_by_email(self, param):
        return User.objects.all().filter(user_email=param).values()[0]

    def find_users_by_name(self, param):
        return User.objects.all().filter(user_name=param).values()