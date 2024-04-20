import datetime

class Notes:
    def __init__(self):
        self.head = "HEAD"
        self.text = "Some text"
        self.date = datetime.datetime.today().isoformat()
        self.idd = 0


    def get_head(self): return self.head
    def get_text(self): return self.text
    def get_date(self): return self.date
    def get_idd(self): return  self.idd #?????????????????

    def set_head(self, txt): self.head = txt
    def set_text(self, txt): self.text = txt
    def set_date(self, date): self.date = date
    def set_idd(self, idd): self.idd = idd

    def view(self):
        print(self.idd)
    pass