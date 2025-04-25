f = open('myfile'.txt,w)
f.write('hello wold')
f.close()

with open ('myfile.txt','a') as f :
f.write("Hey I am inside with")
#f = open('mfile.txt.'rt')
#print(f)

#text = f.read()
#print(text)
#f.close()