# John Dunne (Jd5an)

def instructors(department):
    departmenturladdition = department
    import urllib.request
    requestedurl = "http://cs1110.cs.virginia.edu/files/louslist/" + str(departmenturladdition)
    stream = urllib.request.urlopen(requestedurl)
    classlist = list()
    instructorlist = list()
    sortedfinalinstructorlist = list()
    for line in stream:
        line_in_document = line.strip().decode("UTF-8")
        Classcatagories = line_in_document.split("|")
        # This is where class catagories are broken up and most functions start to differ
        classlist.append(line_in_document)
        Strippedinstructor = Classcatagories[4].strip("+123456789")
        instructorlist.append(Strippedinstructor)
        instructorset = set(instructorlist)
        finalinstructorlist = list(instructorset)
        sortedfinalinstructorlist = sorted(finalinstructorlist)
    return sortedfinalinstructorlist
            # Classlist is the list of all the classes, they are seen as string right now

def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    departmenturladdition = dept_name
    seats = True
    correct_list = list()
    level_requirement = None
    import urllib.request
    requestedurl = "http://cs1110.cs.virginia.edu/files/louslist/" + str(departmenturladdition)
    stream = urllib.request.urlopen(requestedurl)
    for line in stream:
        line_in_document = line.strip().decode("UTF-8")
        Classcatagories = line_in_document.split("|")
        #print(Classcatagories[0])
        # Checks to see if seats are available
        if has_seats_available is not False:
            if int(Classcatagories[15]) >= int(Classcatagories[16]):
                seats = False
            else:
                seats = True
        else:
            seats = True
        # This is the level check
        if level is not None:
            if len(Classcatagories[1]) < len(str(level)):
                level_requirement = False
            elif len(Classcatagories[1]) > len(str(level)):
                level_requirement = False
            elif len(Classcatagories[1]) == len(str(level)):
                if Classcatagories[1].startswith("1") and str(level).startswith("1"):
                    level_requirement = True
                elif Classcatagories[1].startswith("2") and str(level).startswith("2"):
                    level_requirement = True
                elif Classcatagories[1].startswith("3") and str(level).startswith("3"):
                    level_requirement = True
                elif Classcatagories[1].startswith("4") and str(level).startswith("4"):
                    level_requirement = True
                elif Classcatagories[1].startswith("5") and str(level).startswith("5"):
                    level_requirement = True
                elif Classcatagories[1].startswith("6") and str(level).startswith("6"):
                    level_requirement = True
                elif Classcatagories[1].startswith("7") and str(level).startswith("7"):
                    level_requirement = True
                elif Classcatagories[1].startswith("8") and str(level).startswith("8"):
                    level_requirement = True
                elif Classcatagories[1].startswith("9") and str(level).startswith("9"):
                    level_requirement = True
                elif Classcatagories[1].startswith("1") and str(level).startswith("1"):
                    level_requirement = True
                else:
                    level_requirement = False
        else:
            level_requirement = True
        # This is the not_before check
        if not_before is not None:
            classstart1 = False
            if int(Classcatagories[12]) < int(not_before):
                classstart1 = False
            else:
                classstart1 = True
        else:
            classstart1 = True
        # This is the not_after check
        if not_after is not None:
            classstart2 = False
            if int(Classcatagories[12]) > int(not_after):
                classstart2 = False
            else:
                classstart2 = True
        else:
            classstart2 = True
        if seats is not False and level_requirement is not False and classstart1 is not False and classstart2 is not False:
            if Classcatagories is not None:
                correct_list.append(Classcatagories)
    return correct_list