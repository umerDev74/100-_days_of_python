

# -------------- SIMPLE FUNCTION -------------

def double(x):
    return x*2

print(double(5))

# ---------- LAMBDA FUNCTION OF SAME SIMPLE FUNCTION ----------

double = lambda x:x*2
print(double(5))

# ---------- CUBE FUNCTION IN LAMBDA --------------

cube = lambda x:x*x*x
print(cube(5))

# ---------- average FUNCTION IN LAMBDA --------------

avg = lambda x,y:(x+y)/2
print(avg(5,21))

# --------- PASS FUNCTION AS A FUNCTION ARGUMENTS -----------

def apply(fx, value):
    return 8 + fx(value)
print(apply(lambda x: x*x*x, 2))   