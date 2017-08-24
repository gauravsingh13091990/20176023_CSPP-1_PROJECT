file1 = open("text_plagrism.txt").readlines()
file2 = open("text2_plagrism.txt").readlines()
"""file1 and file 2 are the files for test of plagrism"""
f = [file1,file2]
print(file1)
def remove_delimiters (delimiters, s):
    for d in delimiters:
        ind = s.find(d)
        while ind != -1:
            s = s[:ind] + s[ind+1:]
            ind = s.find(d)
    return ' '.join(s.split())
deli1 = []
deli2 = []
delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]
for i in range(2):
	for j in (f[i]):
		if i == 0:
			deli1.append(remove_delimiters(delimiters,j))
		else:
			deli2.append(remove_delimiters(delimiters,j))




		

	

