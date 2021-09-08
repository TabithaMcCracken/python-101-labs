# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("Please give me your honest opinion: ")
sarcasm = ""
for idx in range(len(opinion)):
    if not idx % 2:
        sarcasm = sarcasm + opinion[idx].lower()
    else:
        sarcasm = sarcasm + opinion[idx].upper()

print(sarcasm)