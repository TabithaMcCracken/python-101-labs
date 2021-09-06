# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

for char in range(len(secret)):
    if secret[char].isalpha():
        solution += secret[char]

print(solution)








#hello = "hello World"
#result = ""

#cipher1 = "cake"
#cipher2 = "bear"
#result = ""

#for char in range(len(cipher1)):
#    result = cipher1[char] + cipher2[char]
#    print (result)

# for char in range(len(hello)):
#    if (char%2)==0:
#    #    result = result + hello[char].upper()
#        print (char)

# for n in range(50, 100, 2):
#    if n % 2 == 0:
#        print(n)   

# for char in range(len(hello)):
#    if char % 2 :
#        result = result + hello[char].upper()
#    else:
#        result = result + hello[char].lower()        
#        
#print (result)