# TODO скопириуйте и запустите здесь необходимый код
class A:
    class_attr = 10  # классовый атрибут

    def __init__(self, param):
        self.param = param  # экземплярный атрибут

    def get_param(self):  # экземплярный метод
        return self.param

class B(A):  # Так происходит наследование, теперь в классе B есть все тоже самое, что и в классе A

if __name__ == "__main__":

    obj_a = A(20)
    obj_b = B(40)  # хотя мы и не писали __init__(self, param) в классе B, но оно полностью скопировалось из класса A
