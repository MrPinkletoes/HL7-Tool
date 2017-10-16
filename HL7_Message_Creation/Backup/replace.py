import random
import time
import os
import csv


def get_lines():
    # classes to import random data from .csv files
    # the following classes open and parse the .csv files drawing random individual results
    class Male:
        def __init__(self, name):
            self.name = name

    with open('data/names_m.csv', 'r') as csvfile:
        names_m = list(csv.reader(csvfile))
    lengthofcsv = len(names_m)
    position = random.randrange(0, lengthofcsv)
    namem = Male(*names_m[position])

    class Female:
        def __init__(self, name):
            self.name = name

    with open('data/names_f.csv', 'r') as csvfile:
        names_f = list(csv.reader(csvfile))
    lengthofcsv = len(names_f)
    position = random.randrange(0, lengthofcsv)
    namef = Female(*names_f[position])

    class Surname:
        def __init__(self, name):
            self.name = name

    with open('data/surnames.csv', 'r') as csvfile:
        surnames = list(csv.reader(csvfile))
    lengthofcsv = len(surnames)
    position = random.randrange(0, lengthofcsv)
    sname = Surname(*surnames[position])

    class SampleType:
        def __init__(self, name):
            self.name = name

    with open('data/sampletype.csv', 'r') as csvfile:
        sampletype = list(csv.reader(csvfile))
    lengthofcsv = len(sampletype)
    position = random.randrange(0, lengthofcsv)
    stype = SampleType(*sampletype[position])

    class Locations:
        def __init__(self,name):
            self.name = name

    with open ('data/locations_code.csv','r') as csvfile:
        locations_code = list(csv.reader(csvfile))
    lengthofcsv = len(locations_code)
    position = random.randrange(0, lengthofcsv)
    locations_code = Locations(*locations_code[position])


    # generate random dob
    dobformat = "{Year}{Month}{Day}"
    year_range = [str(i) for i in range(1900, 2014)]
    month_range = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    day_range = [str(i).zfill(2) for i in range(1, 28)]

    argz = {"Year": random.choice(year_range),
            "Month": random.choice(month_range),
            "Day": random.choice(day_range),
            }
    dob = dobformat.format(**argz)


    # getting today's date to put into line 4,5,6
    date = time.strftime("%Y%m%d")
    # string_1 Unique reference number
    string_1 = random.randrange(1000000000, 9999999999)
    # string_2 patient ID number
    hosp_no = 'P%s' % (random.randrange(100000, 999999))
    # string_3 ward selection
    location = locations_code.name
    # date + order number (string_5)
    # string_5
    string_5 = random.randrange(00000000, 99999999)
    # string 6 = Surnames from Surnames.csv
    surname = sname.name
    # string_7 Male first names
    string_7 = namem.name
    # string_9 random choice male female
    sex = random.choice(['M', 'F'])
    priority = random.choice(['R', 'A', 'P', 'S'])
    # string_8 sample type from sampletype.csv
    string_8 = stype.name
    nhs_no = '4444%s' % random.randrange (0000000, 9999999)

    # HL7 Message.
    line1 = "MSH|^~\&|RHM||SAMPLE360|MSOFT|%s1105||ORM^O01|%s|P|2.5||NE|AL||||" % (date,string_1)
    line2 = "\nPID|1||%s^^^^HOSPITALNO~%s^^^^NHSNO||%s^%s||%s0000|%s|||||||||||||| " % (hosp_no,nhs_no, surname, string_7, dob, sex)
    line3 = "\nPV1|1||%s|||||||||||||||||||||||||||||||||||||||||||||||| " % location
    line4 = "\nORC|NW|%s%s||%s|||1^^^%s4500^^%s||^^^%s104500^^^^|||Test001||||REASON||||" % (
    date, string_5, string_5,date,priority,date)
    line5 = "\nOBR|1|%s%s||%s|||%s11045|%s1045||Test001||||||||||" % (date, string_5, string_8,date,date)
    line6 = "\nOBX|1|ST|%s%s||%s%s|||||||||||||||" % (date,string_5, date,string_5)
    line7 = "\nSPM|1|||||||||||||||||||||||||||||"

    return line1 + line2 + line3 + line4 + line5 + line6 + line7

# Creates and writes the first file
i = 1
f = open('messages/S360_%s.xml' % i, "w+")
lines_to_write = get_lines()
f.write(lines_to_write)
i = 1
# Input for the number of files wanted, (currently if only one file is selected then an infinite amount is created)
files = int(input("How many orders would you like?:"))
print(files)

# loop for creating the requested amount of files
while os.path.exists("messages/S360_%s.xml" % i):

    if i == files:
        print("complete")
        i += 1
    else:
        i += 1
        f = open('messages/S360_%s.xml' % i, "w+")
        lines_to_write = get_lines()
        f.write(lines_to_write)
        f.close()