__author__ = 'ze'
import os
import plistlib
import csv
import sys


for item in os.listdir('.'):
    g_date = ""
    if os.path.isfile(item) and item.endswith('.plist'):
        content = plistlib.readPlist(item)
        content = content[0]
        mutaArray = []
        for dict in content:
            for key in dict:
                s = dict[key]
                s = "".join(s.split())

                s1 = s.split(",")
                mutaArray.append(s1)

                records = [("date", "time", "heart", "sport")]
            for item in mutaArray:
                date = item[0]+'/'+ item[1] + '/' + item[2]
                time = item[3] + ':'+ item[4]
                heart = item[5]
                sport = int(item[6]) * 256 + int(item[7])

                date1 = item[8]+'/'+ item[9] + '/' + item[10]
                time1 = item[11] + ':'+ item[12]
                heart1 = item[13]
                sport1 = int(item[14]) * 256 + int(item[15])
                record = (date, time, heart, sport)
                record1 = (date1, time1, heart1, sport1)

                records.append(record)
                records.append(record1)

            itt = mutaArray[0]
            itt = item[0]+ '-'+item[1] +'-' +item[2] + '.csv'


            with open(itt,"wb") as f:
                 writer = csv.writer(f)
                 writer.writerows(records)





# content = plistlib.readPlist("/Users/ze/Desktop/2015-05-09/05.plist")
# content = content[0]
#
# mutaArray = []
# for key in content:
#     s = key['History Heart 2']
#     s = "".join(s.split())
#
#     s1 = s.split(",")
#     mutaArray.append(s1)
#
#
# print mutaArray
#
# records = []
# for item in mutaArray:
#     date = item[0]+'/'+ item[1] + '/' + item[2]
#     time = item[3] + ':'+ item[4]
#     heart = item[5]
#     record = date+','+time+','+heart
#     records.append(record)
#
# print records
#
# records.insert(0,'date, time, heart')
#
# a = '\n'
# x = a.join(records)
# print(x)



