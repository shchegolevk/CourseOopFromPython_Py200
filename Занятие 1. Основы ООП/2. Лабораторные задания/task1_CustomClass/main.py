# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Battery:
    def __init__(self, capacity: int):
        """
        Инициализация батареи.

        :param capacity: Ёмкость батареи.
        :param level: Остаточная заряд батареи.
        Новая батарейка всегда заряжена

        Примеры:
        >>> battery = Battery(500)  # инициализация экземпляра класса
        >>> battery = Battery(-500)  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        ValueError: Ёмкость батареи должна быть положительным числом
        >>> battery = Battery('500')  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Ёмкость батареи должна быть типа int или float
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Ёмкость батареи должна быть типа int или float")
        if capacity <= 0:
            raise ValueError("Ёмкость батареи должна быть положительным числом")

        self.capacity = capacity
        self.level = float(capacity)

    def use(self, amount: float):
        """
        Использует определенное количество заряда.

        :param amount: Количество использованного заряда.

        Примеры:
        >>> battery = Battery(200)
        >>> battery.use(100)  # поверка метода
        100.0
        >>> battery = Battery(200)
        >>> battery.use(300)  # поверка метода
        0.0
        >>> battery = Battery(200)
        >>> battery.use(-100)  # поверка метода
        Traceback (most recent call last):
        ...
        ValueError: Использованный заряд должен быть положительным числом
        >>> battery = Battery(200)
        >>> battery.use('100')  # поверка метода
        Traceback (most recent call last):
        ...
        TypeError: Использованный заряд должен быть типа int или float
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Использованный заряд должен быть типа int или float")
        if amount <= 0:
            raise ValueError("Использованный заряд должен быть положительным числом")
        if amount > self.level:
            consumption = self.level
        else:
            consumption = amount
        self.level -= consumption
        return self.level

    def chardge(self):
        """
        Зарядка батарейки.
        """
        self.level = self.capacity
        print("Батарея полностью заряжена")
        return self.level


class Motor:
    def __init__(self, power: int):
        """
        Инициализация двигателя.

        :param power: Мощность двигателя.

        Примеры:
        >>> motor = Motor(500)  # инициализация экземпляра класса
        >>> motor = Motor(-500)   # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        ValueError: Мощность двигателя должна быть положительным числом
        >>> motor = Motor('500')  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Мощность двигателя быть типа int

        """
        if not isinstance(power, int):
            raise TypeError("Мощность двигателя быть типа int")
        if power <= 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self.power = power

    def operate(self, time: int):
        """
        Симулирует процесс работы двигателя.

        :param time: Время работы двигателя в секундах.
        :return : Сколько заряда использовано
        Примеры:
        >>> motor = Motor(500) # инициализация экземпляра класса
        >>> motor.operate(10000) # поверка метода
        115.74074074074073
        >>> motor = Motor(500) # инициализация экземпляра класса
        >>> motor.operate(-1000) # поверка метода
        Traceback (most recent call last):
        ...
        ValueError: Время работы двигателя должно быть положительным числом
        >>> motor = Motor(500)  # инициализация экземпляра класса
        >>> motor.operate('1000')  # поверка метода
        Traceback (most recent call last):
        ...
        TypeError: Время работы двигателя должно быть типа int
        """
        if not isinstance(time, int):
            raise TypeError("Время работы двигателя должно быть типа int")
        if time <= 0:
            raise ValueError("Время работы двигателя должно быть положительным числом")

        consumption = self.power / 12 * (time / 3600)
        return consumption

    def time_operated(self, consumption: float):
        """
        Проверяет сколько проработает двигатель с таким потребление.

        :param consumption: Использованный заряд.
        :return time: Время работы двигателя в секундах.

        Примеры:
        >>> motor = Motor(500) # инициализация экземпляра класса
        >>> motor.time_operated(10000) # поверка метода
        Двигатель проработал  6000.0  секунд.
        6000.0
        >>> motor = Motor(500) # инициализация экземпляра класса
        >>> motor.operate(-1000) # поверка метода
        Traceback (most recent call last):
        ...
        ValueError: Время работы двигателя должно быть положительным числом
        >>> motor = Motor(500)  # инициализация экземпляра класса
        >>> motor.operate('1000')  # поверка метода
        Traceback (most recent call last):
        ...
        TypeError: Время работы двигателя должно быть типа int

        """
        if not isinstance(consumption, (int, float)):
            raise TypeError("Потребление энергии должно быть типа int или float")
        if consumption <= 0:
            raise ValueError("Потребление энергии должно быть положительным числом")

        time = consumption / self.power/12 * 3600
        print('Двигатель проработал ', time, ' секунд.')
        return time


class Toy:
    def __init__(self, model: str, color: str, motor: Motor, battery: Battery):
        """
        Инициализация игрушки.

        :param color: Цвет игрушки.
        :param model: Модель игрушки.
        :param motor: Объект Motor, представляющий моторчик игрушки.
        :param battery: Объект Battery, представляющий батарейку игрушки.

        Примеры:
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy('Автомобиль', 'красный', motor, battery)
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy(100, 'красный', motor, battery)
        Traceback (most recent call last):
        ...
        TypeError: Модель должна быть типа str
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy('Автомобиль', 100, motor, battery)
        Traceback (most recent call last):
        ...
        TypeError: Цвет должен быть типа str
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy('Автомобиль', 'красный', motor, motor)
        Traceback (most recent call last):
        ...
        TypeError: Батарея должна быть типа Battery
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy('Автомобиль', 'красный', battery, battery)
        Traceback (most recent call last):
        ...
        TypeError: Двигатель должен быть типа Motor
        >>> battery = Battery(500)
        >>> motor = Motor(200)
        >>> toy = Toy('Автомобиль', 'красный', motor, battery)
        >>> toy.run(-100)
        Traceback (most recent call last):
        ...
        ValueError: Время включения должно быть положительным числом
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color
        if not isinstance(motor, Motor):
            raise TypeError("Двигатель должен быть типа Motor")
        self.motor = motor
        if not isinstance(battery, Battery):
            raise TypeError("Батарея должна быть типа Battery")
        self.battery = battery

    def run(self, time: int) -> object:
        """
        Симулирует работу игрушки в течение времени time секунд.

        :param time: Время работы игрушки.
        """
        if not isinstance(time, int):
            raise TypeError("Модель должна быть типа int")
        if time <= 0:
            raise ValueError("Время включения должно быть положительным числом")
        print('Включили игрушку на ', time, ' секунд')
        start_level = self.battery.level
        print('Уровень заряда ', round(start_level / self.battery.capacity * 100, 2), 'процентов')

        consumption = self.motor.operate(time)
        level = self.battery.use(consumption)
        if level == 0:
            oper_time = self.motor.time_operated(start_level)
            print("Игрушка работала ", oper_time, " секунд")
            print("Остаточный заряд 0. Требуется зарядка.")
        else:
            print("Игрушка работала ", time, " секунд")
            print("Остаточный заряд ", level, ".")

    def charge_battery(self):
        """
        Заряд батарейки.

        """
        self.battery.chardge()

    def __str__(self):
        # return f"{self.model}, {self.color}, {self.motor.power}, {self.battery.capacity}, {self.battery.level}"
        return '%s, %s, %s, %s, %s' % (self.model, self.color, self.motor.power, self.battery.capacity, self.battery.level)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    # Создаём объект Motor мощностью 500 Вт 12 Вольт
    toy_motor = Motor(power=500)

    # Создаем объект Battery с ёмкостью 500 А*ч
    toy_battery = Battery(capacity=500)

    # Создаем объект Toy с видом и цветом
    chicken_toy = Toy(model='Цыплёнок', color="зелёный", motor=toy_motor, battery=toy_battery)
    print(chicken_toy)

    # Используем ручку для письма
    print(f"Заряд батареи {chicken_toy.battery.level}")

    chicken_toy.run(10000)
    chicken_toy.run(10000)
    # Заряжаем батарею и снова запускаем игрушку
    chicken_toy.battery.chardge()

    chicken_toy.run(10000)


