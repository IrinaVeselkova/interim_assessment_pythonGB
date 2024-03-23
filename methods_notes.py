import random
import sys
from msvcrt import getch
from datetime import datetime
import json
# id заметки
# тема заметки
# тело заметки
# дата/время создания или изменения заметки
# сохранение заметки


def add_note():
    note = {}
    id_note = chr(random.randint(65, 90)) + \
        chr(random.randint(65, 90)) + str(random.randint(0, 1001))
    theme_note = input("Введите краткое описание заметки: => ")
    if len(theme_note) > 20:
        theme_note = theme_note[:21]
    if theme_note == "" or theme_note == None or theme_note == ' ':
        theme_note = "Тема отсутствует"
    print("Текст заметки (после окончания ввода нажмите ESC): => ")
    text_note = ''
    for line in sys.stdin:
        text_note = text_note+line
        key = ord(getch())
        if key == 27:
            break
    note["id_note"] = id_note
    note["theme"] = theme_note
    note["date_time"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note["change_data_time"] = None
    note["text"] = text_note
    with open("notes.json", "a", encoding='utf-8') as notes_file:
        json.dump(note, notes_file, indent=3, separators=(';', ' : '),ensure_ascii=False)


# удаление заметки


def remove_note():
    pass
# очищение файла
def clear():
    print('*'*20)
    answer = input("Вы уверены, что хотите удалить все заметки?(Д/Н) =>")
    if answer.lower() in ["y",'yes',"да","д"]:
        open('notes.json', 'w').close()
        print('*'*20)
        print("Все заметки удалены")
    

# изменение заметки


def change_note():
    pass

# поиск заметки


def search_note():
    pass

# показать все заметки


def show_notes():
    pass


clear()
