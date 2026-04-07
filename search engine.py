print ("✨ WELCOME TO WORD SEARCH AND COUNT ENGINE ✨")
print ("{To test it; a sample file already exists in the repository}")
#a sample file named 'data.txt' exists in the repository "hello-world" 

#This is where it asks to enter the file name to locate the file in the computer
name_file = input("Enter the file name 📁: ").strip()

#This set of code opens,reviews,by-hearts and closes the file 
file = open(name_file, "r")
content = file.read()
file.close()

#This is where it will take the input to search 
query = input("Enter the word you wanna search 🔍: ").strip()

#This is where it finds and counts the word provided in the dedicated file
if query.lower() in content.lower():
    count = content.lower().count(query.lower())
    print ("FOUND IT! ✔️")
    print (f"The word '{query}' appeared '{count} times' in '{name_file}'")

else:
    print ("SORRY!,NOT FOUND ❌")

print ("✨ Thank You! ✨")    
