#shut down computer
def shutdown():
    user_input = input("Do you want to shut down? (Yes/No): ")
    if user_input == "Yes":
        print("Shutting down...")
    elif user_input == "No":
        print("Abort shut down.")
    else:
        print("Sorry, invalid input.")
