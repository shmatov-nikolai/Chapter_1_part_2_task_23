'''
Напишите функцию котрый будет определять введенный год, высокосный или нет.
'''
def opredelenie_year(year):
    if year % 4 != 0:
        print("Обычный")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Високосный")

opredelenie_year(2020)