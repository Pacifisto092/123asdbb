
from utils.api import Google_maps_api
from utils.cheking import Cheking

""""Создание, изменение и удаление локации"""
class TestCreatePlace():

    def test_create_new_place(self):

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        # token = json.loads(result_post.text)     #Получение полей в ответе
        # print(list(token))
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

    def test_update_new_place(self):

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '100 Lenina street, RU')

    def test_delete_new_place(self):

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        Cheking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")  #Проверка всего текста
        Cheking.check_json_search_word_in_value(result_get,'msg','failed')                                          # Проверка слова или части текста

print("Тестирование позитивных сценариев создания, изменения и удаления локации прошло успешно")



