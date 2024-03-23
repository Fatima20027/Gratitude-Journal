print("                       WELCOME TO YOUR JOURNAL!", end="\n\n")
print("PLEASE CHOOSE THE THINGS YOU WANT TO WRITE ABOUT, OR TYPE 'exit' TO EXIT.(select number)", end="\n\n")
print("""1. Write About A Gratitude Log.
2. Write your Feelings And Thoughts.
3. Write Things you Need to Get Done.
4. Write The Reasons to be Proud of Yourself.
5. Review Your Progress.
6. You Can Write Whatever.
    """)

while True:
    choice = input("<><><><><><><>: ")
    if choice == 'exit':
        break
        
    x = int(choice)
    choices = {
        1: "What You Are Gratful For?",
        2: "Your Feelings And Thoughts",
        3: "Start Listing the Things you Need to Get Done",
        4: "Reasons To Be Proud Of yourself?",
        5: "Your Progress",
        6: "Whatever In Your Mind.."
    }

    default_choices = "NOT VALID! PLEASE TRY AGAIN."
    print(choices.get(x, default_choices))
    entry = input("Start writing: ")

    while True:
        more_entry = input(" ")
        if more_entry.strip():
            entry += "\n" + more_entry
        else:
            break

    filename = "Your_writing_Journal.txt"
    with open(filename, 'a') as file:
        file.write(entry + '\n\n')

    print("Entry saved/processed.")



     
       
         
    
    
        

        





