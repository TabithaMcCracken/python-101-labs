# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

if file_1[-4:] == ".pdf":
    print ("True")
else: print ("False")

if file_2[-4:] == ".pdf":
    print ("True")
else: print("False")

if file_3[-4:] == ".pdf":
    print ("True")
else: print("False")

if file_4[-4:] == ".pdf":
    print ("True")
else: print("False")