from collections import Counter
import math
import os
"""f1 is the file number one"""
"""f2 is the second file we will compare f1 and f2 for plagirism"""
f1 = open("text2_plagrism.txt")
f2 = open("text_plagrism.txt")
x = f1.readlines()
y = f2.readlines()
print("file1 content with delimeter",x,"file2 content with delimeter",y)
d1 = []
d2 = []
""" remove_delimeters is a function to delete delimeters from file f1 and f2"""
# way_to_files = os.getcwd()
# files = os.listdir(way_to_files)
# filesText = [i for i in files if i.endswith(".txt")]
# print(filesText)
# for x in range(len)
def remove_delimiters (delimiters, s):
    for d in delimiters:
        ind = s.find(d)
        while ind != -1:
            s = s[:ind] + s[ind+1:]
            ind = s.find(d)
    return ' '.join(s.split())


delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]
d_list1= []
d_list2= []
for j in x:
    d_list1.append(remove_delimiters(delimiters,j))
print(d_list1)
string = " ".join(map(str,d_list1))
for i in string.split():
	d1.append(i)
print (d1)
"""counts1 and counts2 are dictionaries containing frequencies for both the files"""
counts1 = dict(Counter(d1))
print(counts1)
for k in y:
    d_list2.append(remove_delimiters(delimiters,k))
string = " ".join(map(str,d_list2))
for n in string.split():
	d2.append(n)
# print (d2)
counts2 =dict(Counter(d2))
print(counts2)
dotproduct = 0
for d in counts1:
	if d in counts2:
		dotproduct = dotproduct + counts1.get(d)*counts2.get(d)
"""values1 and values2 are frequency of the words in file f1 and file f2"""
values1 =list(counts1.values())
values2= list(counts2.values())
print(values1)
print(values2)
i,j = 0,0
square1 = 0
square2 = 0
for i in range (len(values1)):
	square1 =square1 + values1[i]**2
for j in range (len(values2)):
	square2 = square2 + values2[j]**2
modefrequency1 = math.sqrt(square1)
modefrequency2 = math.sqrt(square2)
print(modefrequency1)
print(modefrequency2)
i = 0
print("dotproduct",dotproduct)
dis =((dotproduct)/(modefrequency1*modefrequency2))*100
print("plagirism percentage",dis)
