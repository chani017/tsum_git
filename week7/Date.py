# Date.py
# import 금지

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def is_valid_date(self, year, month, date):
        if  year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
            if (month % 2) == 1: #31일이 있는 달
                if month <= 7:
                    if date <= 0 or date > 31:
                        return False
                else:
                    if date <= 0 or date > 30:
                        return False
        else: #31일이 없는 달
            if month <= 6:
                if month == 2:
                    if date <= 0 or date > 29:
                        return False
                    elif date <= 0 or date > 28:
                        return False
                if date <= 0 or date > 30:
                    return False
            else: 
                if date <= 0 or date > 31:
                    return False
        print(year + "년" + month + "월" + date + "일은 존재하는 날짜입니다.")
