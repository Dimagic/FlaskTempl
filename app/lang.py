# -*- coding: utf-8 -*-

class Lang:
    def __init__(self):
        self.dict_ru = {}
        self.dict_en = {}
        self.dict_ru.update({'login_message': 'Пожалуйста, войдите, чтобы продолжить.'})
        self.dict_en.update({'login_message': 'Please, login for continue.'})

    def get_str(self, val):
        return self.dict_ru.get(val).decode('utf-8')