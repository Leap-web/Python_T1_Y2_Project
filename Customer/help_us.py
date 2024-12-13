import os
def help_us():
    os.system('cls')
    while True:
        print("\n**********HELP US*********")
        print("1. Provide feedback.")
        print("2. User also as questions.")
        print("3. Contect information.")
        print("4. Back to main menu.")
        option = input("Enter your choice (1, 2, 3 and 4): ")
        if option == "1":
            provide_feedback()
        elif option == "2":
            user_question()
        elif option == "3":
            contect_information()
        elif option == "4":
            back_menu()
            break
        else:
            print("Invalid option. Please try again!")

def provide_feedback():
    
    print("\n---------------Provide_feedback---------------")
    try:
        username = input("Enter your username: ").strip()
        if not username:
            raise ValueError("User name cannot empty")
        feedback = input("Enter your feedback: ").strip()
        if not feedback:
            raise ValueError("Feedback connot empty.")
        with open('Customer/feedback.txt', 'a') as file:
            file.write(f"Username: {username}, Feedback: {feedback}\n")
        print("Thank you for your feedback!")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

def user_question():
  
    print("\n---------------User FAQs---------------")
    print("Q: How can I reset my password?")
    print("A: Use the 'Forgot Password' opption from the main menu.")
    print("\nQ: Can I update my profile details?")
    print("A: YES, go to 'Manage Profile' in the menu.")
    print("\nQ: How do I contact customer service?")
    print("A: Check the 'Contact Information' section for detail.")

def contect_information():

    print("\n---------------Contect Information---------------")
    print("Customer Support Email: support@gmail.iec.com")
    print("Contact Number: +855 123456789")
    print("Website: www.iec.com.kh")

def back_menu():
    
    print("Returning to the main menu!")

help_us()