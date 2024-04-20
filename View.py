import Note
def view_comands():
    print(f"add - добавить запись \n"
          f"cahnge - заменить записи (заменит все записи с указанным заголовком)\n"
          f"delete - далит записи с указанным заголовком +\n"
          f"print - вывести все записи в консоль \n"
          f"save - сохранить все записи в файл 'notes.csv'\n"
          f"0 - закрыть программу")
def print_txt (text):
    print(text)


def get_user_choise ():
    print("Введитте что вы ходите сделать:")
    choise = input()
    return choise

def get_head():
    head = input("Введит имя заголовка \t")
    return head

def get_text():
    text = input("Введит текст заметки \t")
    return text

def print_console (notes: Note):
    print("head = "+ notes.get_head())

    print("text = "+ notes.get_text())
    print("date = "+ notes.get_date())
    print(f"id = " +str(notes.get_idd()))

    print()

