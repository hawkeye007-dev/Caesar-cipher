import string

alphabets = string.ascii_lowercase
direction = input("Type 'decode' to decode the script and 'encode' to code a script : \n").lower()
text = input("Type the text you want to direct : \n").lower()
shift = int(input("The shift number is : \n"))
