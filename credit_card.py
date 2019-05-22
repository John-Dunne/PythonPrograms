# John Dunne (Jd5an)

def check(creditcardnumber):
    onetotendict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    creditlength = len(str(creditcardnumber))
    creditcardnumberstr = str(creditcardnumber)
    c = 0
    i = 0
    deck = list()
    tempdeck = list()
    if creditlength%2 == 1 and creditlength != 2 and creditlength != 3:
        while c != 1:
            c = creditlength - i
            deck.append(onetotendict.get(creditcardnumberstr[i]))
            i += 1
        deck.reverse()
            # This while loop makes a list of the numbers in the credit card number given
        remainingdeck = deck[0:len(deck):2]
        deck2 = deck[0:len(deck):2]
        sumdeck2 = sum(deck2)
        for number in remainingdeck:
            doublednum = number*2
            doublednumstr = str(doublednum)
            doublenumlen = len(doublednumstr)
            n = 0
            e = 0
            while n != 1:
                n = doublenumlen - e
                tempdeck.append(onetotendict.get(doublednumstr[e]))
                e += 1
        totaldouble = sum(tempdeck)
        validcreditcardnum = (totaldouble + sumdeck2)%10
        if validcreditcardnum == 0:
            return True
        else:
            return False
    if creditlength%2 == 0 and creditlength != 2 and creditlength != 3:
        while c != 1:
            c = creditlength - i
            deck.append(onetotendict.get(creditcardnumberstr[i]))
            i += 1
            # This while loop makes a list of the numbers in the credit card number given
        remainingdeck = deck[0:len(deck):2]
        deck2 = deck[0:len(deck):2]
        sumdeck2 = sum(deck2)
        for number in remainingdeck:
            doublednum = number*2
            doublednumstr = str(doublednum)
            doublenumlen = len(doublednumstr)
            n = 0
            e = 0
            while n != 1:
                n = doublenumlen - e
                tempdeck.append(onetotendict.get(doublednumstr[e]))
                e += 1
        totaldouble = sum(tempdeck)
        validcreditcardnum = (totaldouble + sumdeck2) % 10
        if validcreditcardnum == 0:
            return True
        else:
            return False
    if creditlength == 2:
        while c != 1:
            c = creditlength - i
            deck.append(onetotendict.get(creditcardnumberstr[i]))
            i += 1
        sumofdecks = deck[0]*2 + deck[1]
        if sumofdecks%10 == 0:
            return True
        else:
            return False
    if creditlength == 3:
        e = 0
        n = 0
        while i<=2:
            deck.append(onetotendict.get(creditcardnumberstr[i]))
            i += 1
        sumtwoofdeck = deck[0] + deck[2]
        print(sumtwoofdeck)
        finalsum = (deck[1]*2)
        print(finalsum)
        strfinalsum = str(finalsum)
        for n in range(len(strfinalsum)):
            tempdeck.append(onetotendict.get(strfinalsum[n]))
            n += 1
        print(tempdeck)
        sumfinal = (sum(tempdeck) + sumtwoofdeck) % 10
        if sumfinal == 0:
            return True
        else:
            return False