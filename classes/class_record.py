import datetime
class DateCheck:
    def __init__(self, date):
        self.date = date
    
    def date_check(date):
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
            return date
        except:
            i = 1
            for i in range(3):
                print("Incorrect date format, should be dd/mm/yyyy.")
                date = input("Please try again: ")
                if datetime.datetime.strptime(date, "%d/%m/%Y"):
                    return date
                else:
                    i +=1
            return False
