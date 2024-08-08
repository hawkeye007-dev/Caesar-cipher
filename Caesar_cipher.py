import string

alphabets = string.ascii_lowercase
direction = input("Type 'decode' to decode the script and 'encode' to code a script : \n").lower()
text = input("Type the text you want to direct : \n").lower()
shift = int(input("The shift number is : \n"))

def output(text_0,shift_0,direction_0) :
    cipher = ""
    for letter in text_0 :
        if letter not in alphabets :
            cipher += letter
        else :
            index_0 = alphabets.index(letter)
            if direction_0 == "decode" :
                shift_0 = shift_0 * -1
            new_index = index_0 + shift_0
            new_index %= len(alphabets)
            cipher += alphabets[new_index]
    print(cipher)

output(text,shift,direction)
