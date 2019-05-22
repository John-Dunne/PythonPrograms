# John Dunne (Jd5an)

import urllib.request
url = "http://cs1110.cs.virginia.edu/files/words.txt"
stream = urllib.request.urlopen(url)
wordlist = list()
for line in stream:
    line_in_document = line.decode("UTF-8").strip()
    wordlist.append(line_in_document)
lensentence = 1
print("Type text; enter a blank line to end.")
while lensentence != 0:
    i = 0
    sentence = str(input(""))
    lensentence = len(sentence)
    freesentence = sentence.replace('"','')
    extrafreesentence = freesentence.replace("!","")
    extraextrafreesentence = extrafreesentence.replace("?","")
    triplefreesentence = extraextrafreesentence.replace("(","")
    quadruplefreesentence = triplefreesentence.replace(")","")
    pentafreesentence = quadruplefreesentence.replace(".","")
    sextafreesentence = pentafreesentence.replace(",","")
    splitsentence = extraextrafreesentence.split()
    for i in range(0, len(splitsentence)-1):
        word = splitsentence[i]
        strippedword = word.strip("+!?',().").strip('"')
        correctness_of_word = strippedword not in wordlist
        lowercase_correctness_of_word = strippedword.lower() not in wordlist
        if correctness_of_word == True and lowercase_correctness_of_word == True:
            print("  MISSPELLED:", str(strippedword))