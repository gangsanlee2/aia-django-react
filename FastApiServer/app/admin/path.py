import os
import platform
myos = platform.system()
root_window = r"C:\Users\bitcamp\aia-django-react\FastApiServer\app"
root_docker = "/usr/src/app/app"
root = root_docker

def dir_path(param):
    if (param == "config")\
            or (param == "models")\
            or (param == "test")\
            or (param == "train_tools")\
            or (param == "utils")\
            :
        return os.path.join(root, "services", 'chatbot_ngin', param)

if __name__ == '__main__':
    print(">> "+dir_path("carts"))