# Replicate one of the oldest known encryption in code.
# Apply a Cesar cipher of 7 to the 'secret' variable.
# P.S.: http://www.montypython.net/scripts/dentist.php ;)
# You can start with the following code:


#secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
secret = str(input("Please enter the text you would like encoded."))
cipher = 7
encrypted_code = ""
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("The original message is: ")
print(secret)

for char in secret:
    if char in lower_alphabet:
        location = lower_alphabet.find(char) #get location of the letter
        new_location = (location - cipher) % 26 #move the location over according to the cipher number
        new_letter = lower_alphabet[new_location] #get the new letter
        encrypted_code += new_letter #add the new letter to the new encryption
    elif char in upper_alphabet:
        location = upper_alphabet.find(char) #get location of the letter
        new_location = (location - cipher) % 26 #move the location over according to the cipher number
        new_letter = upper_alphabet[new_location] #get the new letter
        encrypted_code += new_letter #add the new letter to the new encryption
    else:
        encrypted_code += char #anything not in a the alphabet stays the same

print("Your encrypted message is:")
print(encrypted_code, "\n")
