# John Dunne (Jd5an)

arabicnum = (str(int(input("Enter an integer: "))))
lenarabicnum = len(arabicnum)
onesdigit = {"0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9":"IX"}
seconddigit = {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX","9": "XC"}
thirddigit = {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM"}
fourthdigit = {"0": "", "1": "M", "2": "MM", "3": "MMM"}
i = 0
fourth = ""
second = ""
ones = ""
third = ""
while i != lenarabicnum:
    c = lenarabicnum - i
    if c == 1:
        ones = onesdigit.get(arabicnum[i])
    if c == 2:
        second = seconddigit.get(arabicnum[i])
    if c == 3:
        third = thirddigit.get(arabicnum[i])
    if c == 4:
        fourth = fourthdigit.get(arabicnum[i])
    i += 1
print(fourth+third+second+ones)