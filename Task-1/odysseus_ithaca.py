#Odysseus and the Prophecy of Ithaca

letters = input("Enter A letter sequence: ")
print(letters)
letters_list = letters.split()

flag  = False
count=0
freq = {}
for letter in letters_list:
    count+=1
    if letter in freq:
        freq[letter]+=1
    else:
        freq[letter] =1

    if freq.get("I",0)>=1 and freq.get("T",0)>=1 and freq.get("H",0)>=1 and freq.get("A",0) >=2 and freq.get("C",0)>=1:
        print("The earliest step when the collected letters can form `ITHACA`: ", count)
        flag = True
        break
    
if(flag == False):
    print("-1")

