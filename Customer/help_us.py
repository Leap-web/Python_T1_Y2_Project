import os
def help_us():
    while True:
        print("\n**********HELP US*********")
        print("1. Store Policies.")
        print("2. Product Repair.")
        print("3. Shipping and Delivery.")
        print("4. Privacy Policy.")
        print("5. User also as questions.")
        print("6. Contect information.")
        print("7. Back to main menu.")
        option = input("Enter your choice option: ")
        os.system('cls')
        if option == "1":
            store_policies()
        elif option == "2":
            product_repair()
        elif option == "3":
            shipping_delivery()
        elif option == "4":
            privacy_policy()
        elif option == "5":
            user_question()
        elif option == "6":
            contect_information()
        elif option == "7":
            back_menu()
            break
        else:
            print("Invalid option. Please try again!")
def store_policies():
    print("\n---------------Store_Policies---------------")
    print("1. Return & Exchange: You can return or exchange items within 14 days of purchase.")
    print("2. Warrabty: All Apple products come with a 1_year warranty.")

def product_repair():
    print("\n---------------Product Repair---------------")
    print("You can request repair for your Apple products by visiting an Apple Store or contacting Apple Support online.")
    print("Make sure your product in covered under warranty or AppleCare.")

def shipping_delivery():
    print("\n---------------Shipping & Delivery---------------")
    print("We offer free shipping for orders over 1500$.")
    print("\nStandard delivery takes 1-2 days befor order.")
    print("For expedited shipping, additional fees apply.")
    print("You can select your preferred shipping method at checkout.")

def privacy_policy():
    print("\n---------------Privacy Policy---------------")
    print("Your privacy is important for us. We need only use your personal data for processing orders.")
    print("Read our full privacy policy on our wenbsite for more detail.")

def user_question():
    print("\n---------------User FAQs---------------")
    print("Q: How can I reset my password?")
    print("A: Use the 'Forgot Password' opption from the main menu.")
    print("\nQ: How can I update my profile details?")
    print("A: YES, go to 'Manage Profile' in the menu.")
    print("\nQ: How do I contact customer service?")
    print("A: Check the 'Contact Information' section for detail.")

def contect_information():

    print("\n---------------Contect Information---------------")
    print("Customer Support Email: apple.store@gmail.iec.com")
    print("Contact Number: +855 123456789")
    print("Website: www.iec.com.kh")

def back_menu():
    print("Returning to the main menu!")

help_us()