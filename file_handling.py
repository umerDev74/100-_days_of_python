#  READING A FILE ..........

# f=open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()

#  WRITING A FILE ..........

# f=open('myfile2.txt','w')
# f.write("hello! I am a python developer.")
# f.close()


#  APPEND A FILE ..........

# f=open('myfile2.txt','a')
# f.write('\nmy name is umer nawaz')
# f.close()


#  THE 'WITH' STATEMENT ..........

f=open('myfile2.txt','w')
f.write("hello! I am a python developer.")

# f.close() # agar ham with statement use karte hai
# tu close() ki zarrorat nahi parti agar l;aga le tu bhi koi masla nahi hai 

with open('myfile2.txt','a') as f:
    f.write('\nhey i am already in with')