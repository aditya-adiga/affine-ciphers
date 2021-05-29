choice=int(input("enter 1 to encode the text and 2 to decode the text using affine cipher:"))
text=input("enter the text:")
print("considering the affine cipher to encrypt the message in the form a*x+b:")
key_a=int(input("enter the 'a' part of key:"))
key_b=int(input("enter 'b' part of the key:"))
key1={}
key2={}
def inverse(a,m):
    for i in range(int(m/a),m):
        if((i*a)%m==1):
            return i
    return -1
alphabet='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    key1[i]=alphabet[i]
    key2[alphabet[i]]=i
resulting_text=''
inv=inverse(key_a,26)
print(inv)
if(inv!=-1):
    if(choice==1):
        for i in text:
            resulting_text+=key1[(key_a*key2[i]+key_b)%26]
    elif(choice==2):
        for i in text:
            resulting_text+=key1[inv*(key2[i]-key_b)%26]
        
else:
    print("the value of a is not relatively prime with the value of modulus i.e. 26")
    
print("resulting text :"+resulting_text)          
        
            
    