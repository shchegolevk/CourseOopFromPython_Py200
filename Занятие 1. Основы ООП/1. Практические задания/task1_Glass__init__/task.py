from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        self.capacity_volume = self.capacity_volume_chek(capacity_volume)
        self.occupied_volume = self.occupied_volume_check(occupied_volume)
    def capacity_volume_chek(self, capacity_volume):
        if not isinstance(capacity_volume, (int,float)):
            raise TypeError("Объём должен быть типа float или int")
        if capacity_volume < 0.0:
            raise ValueError("Обём должен бытьбольше 0")
        return capacity_volume

    def occupied_volume_check(self,occupied_volume):
        if not (isinstance(occupied_volume, float) or isinstance(occupied_volume, int)):
            raise TypeError("Заполненный объём должен быть типа float или int")
        if occupied_volume < 0.0:
            raise ValueError("Заполненный обём должен быть больше 0")
        if self.capacity_volume < occupied_volume:
            raise ValueError("Заполненный обём должен быть больше 0")
        return occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    cup = Glass(0.2,0.1)
    mug = Glass(1.0,0.2)
    try:
        ...  # TODO инициализировать не корректные объекты
        jar1 = Glass(0,0)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")
    try:
        ...  # TODO инициализировать не корректные объекты
        jar2 = Glass(-1.1,0)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")
    try:
        ...  # TODO инициализировать не корректные объекты
        jar3 = Glass(10,12)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")



