from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:
    """
    Функция поиска номера телефона пользователя в структуре данных.

    Алгоритм работы следующий:
    1) принимаем на вход структуру content, состоящую из словарей,
    списков и строковых ключей в списке
    2) внутри структуры может быть запись следующего формата:
    {
        'name': 'user_name',
        'phone': 'user_phone',
    }

    3) необходимо пройтись по всей структуре
    4) если встречаем словарь, в котором ключ name совпадает с
    аргументом функции name - берем из этого словаря поле phone
    и возвращаем этот телефон из функции
    5) если поле name с таким значением не найдено - возвращаем из
    функции None

    Может пригодиться:

    1) Чтобы проверить, является ли объект списком используйте функцию:
    isinstance(some_object, list)
    если some_object список - результат будет True
    если some_object не список - False

    2) Чтобы проверить, является ли объект словарем используйте функцию:
    isinstance(some_object, dict)


    :param content: словарь или список, внутрь которого вложены объекты. Внутри
                      может скрываться номер телефона пользователя
    :param name: имя пользователя, у которого будем искать номер телефона
    :return: номер телефона пользователя или None
    """
    ans=""
    if isinstance(content,dict):
        if "name" in content and content["name"]==name:
            ans= content['phone']
        else:
            for each in content.values():
                if search_phone(each,name) !=None:
                    ans=search_phone(each,name)
    elif (isinstance(content,list)):
        for each in content:
            if search_phone(each, name) != None:
                ans = search_phone(each, name)
    if ans !="":
        return ans
    else:
        return None
IVAN_USER_INFO = {
    'name': 'Ivan',
    'phone': '+78005553535',
}
test1={
                'university': 'HSE',
                'groups': [
                    {
                        'group_name': '20pmi-1',
                        'students': [
                            {
                                'name': 'Serg',
                                'phone': '+78001001005',
                            },
                            IVAN_USER_INFO,
                        ],
                    }
                ],
            }
#print(search_phone(test1, 'Ivan'))