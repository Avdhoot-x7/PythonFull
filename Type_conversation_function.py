f = 16.58
s = '123'
b = True
s1 = 0b111
s2 = 0xA
#now we can try to convert them into one type to integer

f = int(16.58)
s = int('123')
b = int(True)
s1 = int(0b111) # these are binary , hexadecimal and octal numbers conversation
s2 = int(0xA)
s3 = int(0o7)

print(f,s,b,s1,s2,s3)

########################################


#we can try with other types of convesations also 
#if you can convert anything into float
#you can convert anything into bool (pass it) and it will return true except = 0 , False and Bool() -> these all will return False

f1 = 3.14
i1 = 3
b1 = True
b2 = False
s = '1+2j'

list = [f1,i1,b1,b2,s]
for i in list: 
    x = complex(i)
    print(x , type(x))
#This is how you convert the all the types into complex number using python

#for string type you pass anything it'll return string like anything -> 'anything'

print(oct(20))