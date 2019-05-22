# John Dunne (Jd5an)

def check(creditcardnumber):
    onetotendict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    creditlength = len(str(creditcardnumber))
    creditcardnumberstr = str(creditcardnumber)
    c = "none"
    i = 0
    n = 0
    e = "none"
    deck = list()
    deck3 = list()
    while c != 1:
        c = creditlength - i
        deck.append(onetotendict.get(creditcardnumberstr[i]))
        i += 1
    sumeveryother = sum(list(range(0, creditlength+1, 2)))
    deck2 = (list(range(1, creditlength+1, 2)))
    while e != 1:
        e = len(deck2) - n
        currentnum = deck2[n]
        doublednum = currentnum*2
        if len(str(doublednum)) == 2:
            doublednumstr = str(doublednum)
            rightnum = doublednumstr[-1:]
            leftnum = doublednumstr[0]
            deck3.append(onetotendict.get(rightnum))
            deck3.append(onetotendict.get(leftnum))
        if len(str(doublednum)) == 1:
            deck3.append(doublednum)
        n += 1
    sumofboth = sum(deck3) + sumeveryother
    sumofboth
    validcreditnum = sumofboth%10
    if validcreditnum == 0:
        return True
    else:
        return False