import Note

def save_tofile (notes):
    file = open('notes.csv', 'w', encoding='utf-8')
    for item in notes:
        print (item)
        file.writelines("id = "+ str(item.get_idd()) +";\t")
        file.writelines("head = "+ item.get_head() +";\t")
        file.writelines("text = "+ item.get_text() +";\t")
        file.writelines("date = "+ item.get_date() +";\t")
        file.write(f" \n")
    file.close()