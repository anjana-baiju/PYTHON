
word=input("Enter the word : ")
letters=list(word)
vowels=[]
print("Vowels in the Word are : ")
for i in 'aeiou':
    if i in letters:
        vowels.append(i)
print(vowels)
