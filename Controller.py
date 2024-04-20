import Saver
import View
import Note
import datetime

def start ():
    notePad = [];
    id = 1;
    while True:
        View.view_comands()
        choise = View.get_user_choise()

        if (choise == "add"):
            new_note = Note.Notes()
            head = View.get_head();
            text = View.get_text();
            new_note.set_head(head)
            new_note.set_text(text)
            notePad.append(new_note)
            date = datetime.datetime.today().isoformat()
            new_note.set_date(date)
            new_note.set_idd(id)
            id +=1
            print("Запись добавлена")


        elif (choise == "print"):
            for item in notePad:
                View.print_console(item)


        elif (choise == "change"):
            head = View.get_head();
            text = View.get_text()
            for item in notePad:
                if item.get_head() == head: item.set_text(text)
            print("Записи изменены")

        elif (choise == "delete"):
            head = View.get_head();
            for item in notePad:
                if item.get_head() == head:
                    notePad.remove(item)
            print("Запись удалена")

        elif (choise == "save"):
            Saver.save_tofile(notePad)
            print("Сохранено в файл")
        elif (choise == "1"):
            for item in notePad:
                item.view()


        elif (choise == "0"):
            break
    return



