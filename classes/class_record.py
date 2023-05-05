
class Record:
    def __init__(self, fname, lname, phone, company, email, birthday, last_contact, next_contact):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.company = company
        self.email = email
        self.birthday = birthday
        self.last_contact = last_contact
        self.next_contact = next_contact

    def fullname(self):
        return f"{self.fname} {self.lname}"