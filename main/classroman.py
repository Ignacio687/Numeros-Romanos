class romannumber():
    def roman_to_decimal(self,rnumber):
        global number
        number = 0
        global count2
        count2=[]
        for count1 in(rnumber):
            count2.append(count1)
            if len(count2)==2:
                if (count2[0]+count2[1])=="IV":
                    number=number-2
                if (count2[0]+count2[1])=="IX":
                    number=number-2
                if (count2[0]+count2[1])=="XL":
                    number=number-20
                if (count2[0]+count2[1])=="XC":
                    number=number-20
            if len(count2)==2:
                count2.pop(0)
        for count1 in(rnumber):
            if count1=="I":
                number=number+1
            elif count1=="V":
                number=number+5
            elif count1=="X":
                number=number+10
            elif count1=="L":
                number=number+50
            elif count1=="C":
                number=number+100
        return number
