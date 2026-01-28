# TODO скопириуйте и запустите здесь необходимый код
class MyClass:
    def __init__(self, value):
        self.value = value  # Открытый атрибут
        self._value = value  # Защищённый атрибут

    def my_method(self):  # Открытый метод
        return self._value
if __name__ == "__main__":
    obj = MyClass(42)
    print(obj.value)  # Открытый доступ
    obj.value = 100   # Изменение атрибута
    print(obj._value)  # Можно получить доступ, но это нарушает соглашение
    obj._value = 100  # Возможное изменение, но не рекомендуется
    print(obj.value)  # Открытый доступ
    print(obj._value)  # Открытый доступ