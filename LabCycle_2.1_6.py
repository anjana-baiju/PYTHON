s1="hai, this is that"

d1={}

for word in s1:
    for letter in word:
        s=d1.keys()
        if letter in s:
            d1[letter]=d1[letter]+1
        else:
            d1[letter]=1
print("Char Frequency is : ",d1)
