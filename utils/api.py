import json
from utils.http_metod import Http_methods
from utils.json import *

"""Методы для тестирования Google_maps_api"""

base_url = "https://rahulshettyacademy.com"              # Базовая URL
key = "?key=qaclick123"                                  # Параметр для всех запросов
post_resource = "/maps/api/place/add/json"               # Ресурс метода POST
get_resourse = "/maps/api/place/get/json"                # Ресурс метода GET
put_resourse = "/maps/api/place/update/json"             # Ресурс метода PUT
delete_resourecese = "/maps/api/place/delete/json"       # Ресурс метода DELETE

class Google_maps_api():

    @staticmethod
    def create_new_place():
        """Метод для созданияя новой локации"""

        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""

        get_url = base_url + get_resourse + key + "&place_id={}".format(place_id)
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get


    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения локации"""

        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_place["place_id"] = place_id
        result_put = Http_methods.put(put_url, json_for_update_place)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_new_place(place_id):
        """Метод удаления локации"""

        delete_url = base_url + delete_resourecese + key
        print(delete_url)
        json_for_delete_place["place_id"] = place_id
        result_delete = Http_methods.delete(delete_url, json_for_delete_place)
        print(result_delete.text)
        return result_delete
