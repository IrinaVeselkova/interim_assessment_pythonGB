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
    if len(theme_note) > 30:
        theme_note = theme_note[:31]
    if theme_note == "" or theme_note == None or theme_note == ' ':
        theme_note = "Тема отсутствует"
    print("Текст заметки (после окончания ввода нажмите ESC): => ")
    text_note = 'Пустая заметка'
    for line in sys.stdin:
        text_note = text_note+line
        key = ord(getch())
        if key == 27:
            break
    note["id"] = id_note
    note["тема"] = theme_note
    datetime_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note["дата_и_время заметки"] = datetime_note
    note["дата_и_время_изменения_заметки"] = datetime_note
    note["заметка"] = text_note
    with open(file_name, "a", encoding='utf-8') as notes_file:
        json.dump(note, notes_file,ensure_ascii=False)
        notes_file.write('\n')
    print("\nЗаметка сохранена")

# удаление заметки
def add_theme_and_note():
    theme_note = input("Введите краткое описание заметки: => ")
    if len(theme_note) > 30:
        theme_note = theme_note[:31]
    if theme_note == "" or theme_note == None or theme_note == ' ':
        theme_note = "Тема отсутствует"
    print("Текст заметки (после окончания ввода нажмите ESC): => ")
    text_note = ''
    for line in sys.stdin:
        text_note = text_note+line
        key = ord(getch())
        if key == 27:
            break
        
def remove_note():
    id_note = input("Введите id заметки, которую необходимо удалить: => ")
    with open(file_name,"r",encoding="utf-8") as notes_file:
        data=[json.loads(jline) for jline in notes_file]
        data_new=[]
        for v in data:
            if id_note == v["id"]:
                print("Заметка",id_note,"удалена")
            else:
                data_new.append(v)
    if len(data)==len(data_new):
        print("Указанный id не обнаружен. Поробуйте еще раз.")
    else: 
        with open(file_name,'w',encoding='utf-8') as record_file:
            for d in data_new:
                json.dump(d, record_file,ensure_ascii=False)
                record_file.write('\n')
# очищение файла


def clear():
    print('*'*60)
    answer = input("Вы уверены, что хотите удалить все заметки?(Д/Н) =>")
    if answer.lower() in ["y", 'yes', "да", "д"]:
        with open(file_name, 'w') as file:
            file.close()
        print('*'*60)
        print("Все заметки удалены")


# изменение заметки


def change_note():
    id_note = input("Введите id заметки, которую необходимо изменить: => ")
    new_note={}
    with open(file_name,"r",encoding="utf-8") as notes_file:
        data=[json.loads(jline) for jline in notes_file]
        data_new=[]
        for v in data:
            if id_note == v["id"]:
                theme_note = input("Введите краткое описание заметки: => ")
                if len(theme_note) > 30:
                    theme_note = theme_note[:31]
                if theme_note == "" or theme_note is None or theme_note == ' ':
                    theme_note = v["тема"]
                print("Текст заметки (после окончания ввода нажмите ESC): => ")
                text_note =''
                for line in sys.stdin:
                    text_note = text_note+line
                    key = ord(getch())
                    if key == 27:
                        break
                new_note["id"] = v["id"]
                new_note["тема"] = theme_note
                datetime_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                new_note["дата_и_время заметки"] = v["дата_и_время заметки"]
                new_note["дата_и_время_изменения_заметки"] = datetime_note
                new_note["заметка"] = text_note
                data_new.append(new_note)
                print("Заметка",id_note,"изменена")
            else:
                data_new.append(v)
    with open(file_name,'w',encoding='utf-8') as record_file:
        for d in data_new:
            json.dump(d, record_file,ensure_ascii=False)
            record_file.write('\n')

# поиск заметки


def search_note(search_in):
    if search_in in ["None", '', " "]: 
        show_notes()
        return
    with open(file_name,"r",encoding="utf-8") as notes_file:
        data=[json.loads(jline) for jline in notes_file]
        for v in data:
            for val in v.values():
                if search_in.lower() in val.lower() or val.lower() in search_in.lower():
                    for key,value in v.items():
                        if key=="заметка":
                            print("*"*60)
                            print(value.rstrip())
                            
                        else:
                            print(f"{key}{" "*(30-len(key))} : {value.rstrip()}")
                    print()
                    break

# показать все заметки


def show_notes():
    with open(file_name,"r",encoding="utf-8") as notes_file:
        data=[json.loads(jline) for jline in notes_file]
        for v in data:
            for key,value in v.items():
                if key=="заметка":
                    print("*"*60)        
                    print(value.rstrip())        
                else:            
                    print(f"{key}{" "*(30-len(key))} : {value.rstrip()}")    
                           
            print('\n',"*"*60,sep='')             

# add_note()
# search_note("23.03")
#clear()
