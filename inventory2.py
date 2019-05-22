# John Dunne (jd5an)

import os, errno

def restock(filename, product, quantity):
    sourcefile = open(filename, "r")
    tempfilename = "temp.csv"
    tempfile = open(tempfilename, "w")
    global restock_found, counter
    counter = 0
    restock_found = False
    for lines in sourcefile:
        linelist = lines.strip("\n").split(",")
        if product == linelist[0]:
            newquantity = int(linelist[1]) + int(quantity)
            restock_found = True
            tempfile.write(linelist[0] + ",")
            tempfile.write(str(newquantity) + ",")
            tempfile.write(linelist[2] + "\n")
        elif product != linelist[0]:
            tempfile.write(linelist[0] + ",")
            tempfile.write(linelist[1] + ",")
            tempfile.write(linelist[2] + "\n")
    if restock_found == False:
        priceinput = -1
        priceinputcondition = False
        while priceinputcondition == False:
            try:
                priceinput = float(input("What is the price of " + str(product)+ "? "))
                if priceinput == float(priceinput) and priceinput > 0:
                    priceinputcondition = True
            except:
                priceinputcondition = False
        tempfile.write(product + ",")
        tempfile.write(str(quantity) + ",")
        tempfile.write(str(priceinput) + "\n")
        tempfile.close()
        sourcefile.close()
        os.remove(filename)
        os.rename(tempfilename, filename)
        return quantity
    elif restock_found == True:
        tempfile.close()
        sourcefile.close()
        os.remove(filename)
        os.rename(tempfilename, filename)
        return newquantity

def sell(filename, product, quantity):
    sourcefile = open(filename, "r")
    tempfilename = "temp.csv"
    tempfile = open(tempfilename, "w")
    global t1, t2, t3
    t1 = False
    t2 = False
    t3 = False
    for lines in sourcefile:
        linelist = lines.strip("\n").split(",")
        if product == linelist[0]:
            newquantity = int(linelist[1]) - int(quantity)
            if int(linelist[1]) > int(quantity):
                tempfile.write(linelist[0] + ",")
                tempfile.write(str(newquantity) + ",")
                tempfile.write(linelist[2] + "\n")
                t1 = True
            elif int(linelist[1]) < int(quantity):
                tempfile.write(linelist[0] + ",")
                tempfile.write(str(linelist[1]) + ",")
                tempfile.write(linelist[2] + "\n")
                t2 = True
            elif int(linelist[1]) - int(quantity) == 0:
                t3 = True
        elif product != linelist[0]:
            tempfile.write(linelist[0] + ",")
            tempfile.write(linelist[1] + ",")
            tempfile.write(linelist[2] + "\n")
    tempfile.close()
    sourcefile.close()
    os.remove(filename)
    os.rename(tempfilename, filename)
    if t1 == True:
        return newquantity
    elif t2 == True:
        return None
    elif t3 == True:
        return 0
