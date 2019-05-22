# John Dunne (Jd5an)

import urllib.request, re


def get_info(name):
    holder = name.lstrip('"').rstrip('"').lower()
    Nonelist = {}
    if len(holder) == 0:
        return Nonelist
    if "," in holder:
        extrastripped = holder.split(",")
        firstname = extrastripped[1].strip(" ")
        steve = firstname+"-"+extrastripped[0]
        strippedname = steve.replace(" ", "-")
    else:
        strippedname = holder.replace(" ", "-")
    Breakdowndict = {}
    FinalDictionary = {}
    try:
        requestedurl = "http://cs1110.cs.virginia.edu/files/uva2015/" + str(strippedname)
        stream = urllib.request.urlopen(requestedurl)
        title = re.compile(r'(content="Job title: (.+<))')
        pay = re.compile(r"(\d\d\d\d \w\w\w\w\w \w\w\w\w\w \w\w\w: \$(\d?\d?\d?,?\d?\d?\d?))")
        rank = re.compile(r"([\w\s]+<\/td><td>(\d+) of \d?,?\d+)")
        base_salary = re.compile(r"('([\w\s]+)', 'amount': (\d+))")
        additional_compensation = re.compile(r"(\wdditional\s?\wompensation)', 'amount': (\d+)")
        nonstate = re.compile(r"('(\won-state \walary)', 'amount': (\d+))")
        deferred = re.compile(r"('(\weferred \wompensation)', 'amount': (\d+))")
        for line in stream:
            decoded = line.decode("UTF-8")
            title1 = title.search(decoded)
            if title1 != None:
                title2 = (title1.group(2))
                title3 = title2.strip("<").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                FinalDictionary['title'] = str(title3)
            pay1 = pay.search(decoded)
            if pay1 != None:
                pay2 = str(pay1.group(2))
                pay3 = pay2.replace(",", "")
                FinalDictionary['pay'] = float(pay3)
            rank1 = rank.search(decoded)
            if rank1 != None:
                FinalDictionary['rank'] = int(rank1.group(2))
            base_salary1 = base_salary.search(decoded)
            if base_salary1 != None:
                Breakdowndict[base_salary1.group(2)] = float(base_salary1.group(3))
            additional_compensation1 = additional_compensation.search(decoded)
            if additional_compensation1 != None:
                Breakdowndict[additional_compensation1.group(1)] = float(additional_compensation1.group(2))
            nonstate1 = nonstate.search(decoded)
            if nonstate1 != None:
                Breakdowndict[nonstate1.group(2)] = float(nonstate1.group(3))
            deferred1 = deferred.search(decoded)
            if deferred1 != None:
                Breakdowndict[deferred1.group(2)] = float(deferred1.group(3))
        FinalDictionary['breakdown'] = Breakdowndict
        return FinalDictionary
    except:
        return Nonelist