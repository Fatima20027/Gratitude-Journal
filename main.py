
print("###WELCOME TO YOUR JOURNAL")
print("Please choose the things you want to write about.")
print("""1. Write about what you are grateful for today.
         2. Write about how you define happiness.
    """)

while True:
    choice = input("<><><>: ")
    i = 2
    while choice != 'exit':
        if choice == '1':
            write = input(" ")
            print(f"{i}. {write}", end = "\n")
            choice = input('')
        i += 1