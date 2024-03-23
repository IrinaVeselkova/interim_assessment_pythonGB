# Проверка данных
def is_correct_input(data):
    try:
        if data.isdigit() == False:
            raise TypeError(
                'Неверно введен номер меню. Введите число от 1 до 6')
        if int(data) < 1 or int(data) > 6:
            raise ValueError(
                'Неверно введен номер меню. Введите число от 1 до 6')
        return True
    except TypeError as err:
        print(err)
        return False
    except ValueError as e:
        print(e)
        return False
