class decimalnumber():
    def first_nine_convertions(self, number):
        if number < 4:
            number = number*"I"
            return number
        elif number == 4:
            number = "IV"
            return number
        elif number < 9:
            number = "V"+(number-5)*"I"
            return number
        elif number == 9:
            number = "IX"
            return number
    def decimal_to_roman(self, number):
        number2 = number%100
        if number2<40:
            number ="C"*(number//100)+"X"*(number2//10)+decimalnumber.first_nine_convertions(self, number2%10)
            return number
        elif number2<50:
            number ="C"*(number//100)+"XL"+decimalnumber.first_nine_convertions(self, number2%10)
            return number
        elif number2<90:
            number ="C"*(number//100)+"L"+"X"*((number2-50)//10)+decimalnumber.first_nine_convertions(self, number2%10)
            return number
        elif number2<100:
            number ="C"*(number//100)+"XC"+decimalnumber.first_nine_convertions(self, number2%10)
            return number
        elif number>399:
            return "We can't convert that number"
        
        