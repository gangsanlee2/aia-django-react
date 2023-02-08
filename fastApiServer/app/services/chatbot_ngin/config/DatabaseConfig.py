'''DB_HOST = "127.0.0.1"
DB_USER = "homestead"
DB_PASSWORD = "secret"
DB_NAME = "homestead"'''
DB_HOST = "host.docker.internal"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "mydb"

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
