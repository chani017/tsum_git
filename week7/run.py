from Date import Date

year = int(input("년도를 입력하세요 : "))
month = int(input("월을 입력하세요 : "))
date = int(input("일을 입력하세요 : "))

inst_1 = Date(year, month, date)
inst_1.is_valid_date()
