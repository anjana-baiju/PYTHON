names=["Annie","cucia","dhanya"]
count=0
for name in names:
    for letter in name:
        if letter =='a' or letter=='A':
            count=count+1
print("There are ",count," A in the list")