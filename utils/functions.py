import json

path = "../config.json"

def set_path(new_path):
    global path
    path = new_path

def get_config(property):
    with open(path, 'r') as f:
        config = json.load(f)
        return config[property]

def get_db_name():
    return get_config('dbName')

def get_pass():
    return get_config('pass')

def get_server():
    return get_config('server')

def get_port():
    return get_config('port')

def get_user():
    return get_config('user')

def get_baseApiUrl():
    return get_config('baseApiUrl')

def get_appId():
    return get_config('appId')

def get_apiKey():
    return get_config('apiKey')

def get_listingsUrl():
    return get_config('listingsUrl')

def get_chromeDriver():
    return get_config('chromeDriver')

def get_itemsImagesUrl():
    return get_config('itemsImagesUrl')

def get_db_connString():
    return get_config('connString')


