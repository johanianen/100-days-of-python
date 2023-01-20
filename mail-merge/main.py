#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = open("Input/Letters/starting_letter.txt", "r")
letter_text = starting_letter.read()
invited_names = open("Input/Names/invited_names.txt")
import os
 
#remove existing letters
old_letters = "Output/ReadyToSend"
for old_letter in os.listdir(old_letters):
    os.remove(os.path.join(old_letters, old_letter))

#create new letters
for name in invited_names.readlines():
    new_letter = open(f"Output/ReadyToSend/letter for {name}.txt", "w")
    new_letter.write(letter_text.replace("[name]", name.strip()))