# # ------- BREAK STATEMENT -----------

for i in range(0,101,10):
    print(i,end=' ')
    if(i==50):
        break
    else:
        print("Miss is loop i")

print("\nThank You") 

# ------------- CONTINUE STATEMENT -----------

for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)