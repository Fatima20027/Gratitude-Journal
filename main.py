
print("               WELCOME TO YOUR JOURNAL!", end="\n\n")
print("Please choose the things you want to write about, or type 'exit' to exit.(select number)", end="\n\n")
print("""1. Write about what you are grateful for today.
2. Write about how you define happiness.
3. Write about the things you love about yourself.
4. Write about the things that you don't like about yourself.
5. write a motivational letter for your future self.
    """)

while True:
    choice = input("<><><>: ")
    if choice == 'exit':
        break
    elif choice == '5':
        write = input("Write a motivational letter for your future self:\n")
        print("Your motivational letter for your future self has been saved.\n")
        continue
    elif choice not in ['1', '2', '3', '4']:
        print("Not valid, try again.\n")
        continue

    i = 1
    while choice != 'exit':
        if choice == '1':
            print(f"{i}.", end = "\n")
            write = input(" ")
        elif choice == '2':
            print(f"{i}.", end = "\n")
            write = input(" ")
        elif choice == '3':
            print(f"{i}.", end = "\n")
            write = input(" ")
        elif choice == '4':
            print(f"{i}.", end = "\n")
            write = input(" ")
     
        i += 1
       
         
    
    
        

        





