import string
alphabets = string.ascii_lowercase

direction = input("Type 'decode' to decode the script and 'encode' to code a script : \n").lower()
direc_list = ['decode', 'encode']
while direction not in direc_list :
    print("please enter the value that can be valid for the process ")
    direction = input("Type 'decode' to decode the script and 'encode' to code a script : \n").lower()

shift = input("The shift number is : \n")
while not shift.isnumeric() :
    print("please enter the value that can be valid for the process : ")
    shift = input("The shift number is : \n")

text = input("Type the text you want to direct : \n").lower()


def output(text_0,shift_0,direction_0) :
    cipher = ""
    for letter in text_0 :
        if letter not in alphabets :
            cipher += letter
        else :
            index_0 = alphabets.index(letter)
            if direction_0 == "decode" :
                shift_0 = shift_0 * -1
            new_index = index_0 + int(shift_0)
            new_index %= len(alphabets)
            cipher += alphabets[new_index]
    print(f"This is your {direction}d text : {cipher}")

output(text,shift,direction)
