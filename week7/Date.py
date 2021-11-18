# Date.py
# import 금지

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date
        self.end_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False

    def is_valid_date(self, ):
        if self.year <= 0:
            return self.print_valid(False)
        if self.is_leap_year():
            self.end_date[1] += 1
        if self.month > 12 or self.month < 0:
            return self.print_valid(False)
        if self.date > self.end_date[self.month -1] or self.date < 0:
            return self.print_valid(False)
        return self.print_valid(True)

    def print_valid(self, bool):
        if bool:
            print(f"{self.year}년 {self.month}월 {self.date}일은 존재하는 날짜입니다.")
        else:
            print(f"{self.year}년 {self.month}월 {self.date}일은 존재하지 않는 날짜입니다.")
