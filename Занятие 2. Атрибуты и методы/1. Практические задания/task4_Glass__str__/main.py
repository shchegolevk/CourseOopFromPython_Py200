from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def __str__(self) -> str:
        # return # TODO метод должен возвращать строку, которая содержит человеко-читаемую информацию
        return "Стакан объёмом " + str(self.capacity_volume) + '. Объём жидкости = ' + str(self.occupied_volume)

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса

    print(glass)  # Стакан объёмом 200. Объём жидкости = 100
