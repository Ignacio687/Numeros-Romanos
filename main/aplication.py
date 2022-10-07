from main.classdecimal import decimalnumber
from main.classroman import romannumber
class Aplication():
    def run(self):
        run = True
        while run == True:
            decimal1 = decimalnumber()
            roman1= romannumber()
            if str(input("What tipe of number would you like to convert? r for roman or d for decimal   ")) == "d":
                number = int(input("What number would you like to convert?   "))
                print(decimal1.decimal_to_roman(number))
            else:
                number = str(input("What number would you like to convert?   "))
                print(roman1.roman_to_decimal(number))
            if str(input("Do you want to convert another number?  y/n   ")) == "y" :
                run = True
            else:
                run = False
