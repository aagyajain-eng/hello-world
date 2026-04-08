#mood diary code
print("✨ WELCOME TO MOOD DIARY ✨")

choice = input("Type 'w' to write and 'r' to read: ")

#TAKING INPUTS
if choice == "w":
    date = input("DATE 📅: ")
    mood = input("MOOD (1-10): ")
    note = input("ABOUT YOUR DAY? 🤔: ")
    #OPENING THE FILE TO SAVE DATA ENTERED
    file = open("mood_diary.txt" , "a")
    data = date + "," + mood + "," + note + "\n"
    file.write(data)
    file.close()
    print("Succesfully Saved! ✔️")

#WANT TO VIEW PAST ENTRIES
elif choice == "r":
    file = open("mood_diary.txt" , "r")
    print("\n ALL ENTRIES! 💌")
    print(file.read())
    file.close()

else:
    print ("INVALID! ❌\n(try typing 'w' or 'r')")    
