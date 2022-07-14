#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()

number_guests = len(names_list)

for name in range(number_guests):
    names_list[name] = names_list[name].strip()

with open("input/Letters/starting_letter.txt", "r") as letter:
    invite_list = letter.readlines()

invite_list[0].replace("[name]", f"{names_list[0]}")
##########
for name in range(number_guests):

    with open(f"Output/ReadyToSend/letter_to_{names_list[name]}.txt", "w") as letter_to:
        letter_to.write(invite_list[0].replace("[name]", f"{names_list[name]}"))
    with open(f"Output/ReadyToSend/letter_to_{names_list[name]}.txt", "a") as letter_to:
        letter_to.writelines(invite_list[1:])



