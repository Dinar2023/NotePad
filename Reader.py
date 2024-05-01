import Note

def read_file ():
    list_notes = [];
    with open('notes.csv') as file:
        str_list = file.read().splitlines()
        new_note = Note.Notes()
        for item in str_list:
            pars_list = item.split(";\t")
            # print(pars_list)

            if pars_list[0].__contains__("id = "): pars_list[0].replace("id = ", "")
            else: raise SyntaxWarning ("Некорректный формат данных")
            new_note.set_idd(pars_list[0])

            if pars_list[1].__contains__("head = "): pars_list[1].replace("head = ", "")
            else: raise SyntaxWarning ("Некорректный формат данных")
            new_note.set_text(pars_list[1])

            if pars_list[2].__contains__("text = "): pars_list[2].replace("text = ", "")
            else: raise SyntaxWarning ("Некорректный формат данных")
            new_note.set_text(pars_list[2])

            if pars_list[3].__contains__("date = "): pars_list[3].replace("date = ", "")
            else: raise SyntaxWarning ("Некорректный формат данных")
            new_note.set_date(pars_list[3])
            list_notes.append(new_note);
    # print(str_list)
    file.close()
    return list_notes