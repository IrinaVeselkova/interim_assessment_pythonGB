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
file_name = "notes.jsonl"

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
    datetime_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note["date_time"] = datetime_note
    note["change_data_time"] = datetime_note
    note["text"] = text_note
    with open(file_name, "a", encoding='utf-8') as notes_file:
        json.dump(note, notes_file,ensure_ascii=False)
        notes_file.write('\n')

# удаление заметки


def remove_note():
    pass
# очищение файла


def clear():
    print('*'*20)
    answer = input("Вы уверены, что хотите удалить все заметки?(Д/Н) =>")
    if answer.lower() in ["y", 'yes', "да", "д"]:
        open(file_name, 'w').close()
        print('*'*20)
        print("Все заметки удалены")


# изменение заметки


def change_note():
    pass

# поиск заметки


def search_note(search_in):
    if search_in in ["None", '', " "]: show_notes()
    with open(file_name,"r",encoding="utf-8") as notes_file:
        data=[json.loads(jline) for jline in notes_file]
        for v in data:
            for val in v.values():
                if search_in in val or val in search_in:
                    for key,value in v.items():
                        print(key,":",value)

# показать все заметки


def show_notes():
    pass


# add_note()
search_note()
