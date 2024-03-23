from correct_value import *
from methods_notes import *

# интерфейс


def interface():
    print('*'*20)
    print("Добро пожаловать в приложение 'Notes'!")
    print('*'*20)
    print("Выберите пункт меню:\n" +
          "1. Добавить новую заметку\n" +
          "2. Найти заметку\n" +
          "3. Изменить заметку\n" +
          "4. Показать все заметки\n" +
          "5. Удалить заметку\n" +
          "6. Удалить все заметки")
    input_menu = 0
    flag = False
    while flag != True:
        input_menu = input("Выберите пункт меню: => ")
        flag = is_correct_input(input_menu,6)

    if input_menu == 1:
        add_note()
    elif input_menu == 2:
        interface_search()
    elif input_menu == 3:
        change_note()
    elif input_menu == 4:
        show_notes()
    elif input_menu == 5:
        remove_note()
    elif input_menu == 6:
        clear()

def interface_search():
    search_in = input("Введите данные для поиска: =>")
    print("Вот что удалось найти: ")
    search_note(search_in)
    
