import json
from collections import Counter
data = json.load(open("D:/blo/data.json")) #to store the racial slurs in json file named data and read it
c=0
with open("D:/blo/hosts" , 'r') as file: #let hosts be the file of tweets
    for line in file:
        str= line.split()
        
        lent = len(str)
        for i in range(lent) :
            l=str[i]
            l=l.lower()
            if str[i] in data:
                c=c+1
    file.seek(0)
if c == 0:
    print("no profanity")
elif 0<c< 5 :
    print("%d no. of profane words resulting low profanity" %c)
elif 5<= c <10:
     print("%d no. of profane words resulting medium profanity" %c)
else:
     print("%d no. of profane words resulting high profanity" %c)



