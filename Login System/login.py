# ADMIN USER: admin
# ADMIN PASS: 1234

import ast
import json
import random
import time

spacer = ("\n\n\n\n\n\n\n\n\n\n" + r'''
_|"""""|_|"""""|_|"""""|_| """ |_|"""""|_|"""""|_|"""""|_ 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"
''')


def write_to_file(file_name):
    with open(file_name, 'w') as file_out:
        json.dump(current_users, file_out)
        # print("File Output Done")


def read_file(file_name):
    global current_users
    with open(file_name, 'r') as file_in:
        current_users = ast.literal_eval(file_in.read())


# obtain the saved data. if there is none (error) then it will default and add the admin and make a new file
try:
    read_file('accounts.txt')
except:
    current_users = [{'username': 'admin', 'password': '1234', 'type': 'admin', 'hint': 'One Two Three Four'}]
    write_to_file('accounts.txt')


def starting_animation():
    print(r"""
 ________  ________  ___      ___ ________  ________   ________  _______   ________     
|\   __  \|\   ___ \|\  \    /  /|\   __  \|\   ___  \|\   ____\|\  ___ \ |\   ___ \    
\ \  \|\  \ \  \_|\ \ \  \  /  / | \  \|\  \ \  \\ \  \ \  \___|\ \   __/|\ \  \_|\ \   
 \ \   __  \ \  \ \\ \ \  \/  / / \ \   __  \ \  \\ \  \ \  \    \ \  \_|/_\ \  \ \\ \  
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \ \  \ \  \\ \  \ \  \____\ \  \_|\ \ \  \_\\ \ 
   \ \__\ \__\ \_______\ \__/ /     \ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\
    \|__|\|__|\|_______|\|__|/       \|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|
""")  # ADVANCED
    time.sleep(1)  # WAIT 1 SEC
    print(r"""
 ___       ________  ________  ___  ________      
|\  \     |\   __  \|\   ____\|\  \|\   ___  \    
\ \  \    \ \  \|\  \ \  \___|\ \  \ \  \\ \  \   
 \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \\ \  \  
  \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|__|\|__| \|__|
""")  # LOGIN
    time.sleep(1)
    print(r"""
 ________       ___    ___ ________  _________  _______   _____ ______   ________      
|\   ____\     |\  \  /  /|\   ____\|\___   ___\\  ___ \ |\   _ \  _   \|\   ____\     
\ \  \___|_    \ \  \/  / | \  \___|\|___ \  \_\ \   __/|\ \  \\\__\ \  \ \  \___|_    
 \ \_____  \    \ \    / / \ \_____  \   \ \  \ \ \  \_|/_\ \  \\|__| \  \ \_____  \   
  \|____|\  \    \/  /  /   \|____|\  \   \ \  \ \ \  \_|\ \ \  \    \ \  \|____|\  \  
    ____\_\  \ __/  / /       ____\_\  \   \ \__\ \ \_______\ \__\    \ \__\____\_\  \ 
   |\_________\\___/ /       |\_________\   \|__|  \|_______|\|__|     \|__|\_________\
   \|_________\|___|/        \|_________|                                  \|_________|
""")  # SYSTEMS
    time.sleep(2)  # WAIT 2 SECS
    print(r'''
   _       ___    _   _   _  _     ___    _  _     ___    _  _     ___   
  | |     /   \  | | | | | \| |   / __|  | || |   |_ _|  | \| |   / __|  
  | |__   | - |  | |_| | | .` |  | (__   | __ |    | |   | .` |  | (_ |  
  |____|  |_|_|   \___/  |_|\_|   \___|  |_||_|   |___|  |_|\_|   \___|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'

''')  # LAUNCHING
    time.sleep(5)
    print(r'''
   ___     ___   __  __     ___    _       ___    _____    ___   
  / __|   / _ \ |  \/  |   | _ \  | |     | __|  |_   _|  | __|  
 | (__   | (_) || |\/| |   |  _/  | |__   | _|     | |    | _|   
  \___|   \___/ |_|__|_|  _|_|_   |____|  |___|   _|_|_   |___|  
_|"""""|_|"""""|_|"""""|_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
''')  # COMPLETE
    time.sleep(1)
    print(r'''
      _    ___     ___     ___    _  _   
   _ | |  /   \   / __|   / _ \  | \| |  
  | || |  | - |   \__ \  | (_) | | .` |  
  _\__/   |_|_|   |___/   \___/  |_|\_|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' ''')  # JASON
    time.sleep(2)
    print(r'''
   ___     ___     ___     ___   
  / __|   /   \   | _ \   /   \  
  \__ \   | - |   |   /   | - |  
  |___/   |_|_|   |_|_\   |_|_|  
_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' ''')  # SARA
    time.sleep(2)
    return  # GO BACK TO start()


def start():
    starting_animation()  # START THE ANIMATION

    global spacer, error, hint, logged  # THIS CODE EDITS THESE VARIABLES

    hint = ""
    error = ""
    exit_program = False
    while not exit_program:  # WHILE RUNNING THE PROGRAM
        u_choice = logged_out_menu()
        if u_choice == '1':
            header("sign_in")
            account_name = input("ENTER YOUR USERNAME: ")
            u_index = search_user(account_name)  # CHECK IF USER EXISTS
            if u_index == -1:
                error = 'User does not exist. Please select the "Sign Up" Feature.'
            else:  # IF USER DOES EXIST THEN PROCEED TO PASSWORD TYPING
                auth_pass = authentication(u_index)
                if auth_pass:
                    logged = account_name
                    launch_app()
        elif u_choice == '2':
            registration()
        elif u_choice == '0':
            print(spacer + "THANK YOU FOR USING OUR PROGRAM")
            write_to_file('accounts.txt')
            exit_program = True
        else:
            error = "Invalid Option!"


def header(location):
    # THIS IS THE CODE FOR THE CUSTOM HEADERS
    global error, hint  # THIS CODE EDITS THESE VARIABLES

    print(spacer, end="")
    print(f'LOCATION: {location}')  # THE location VARIABLE IS GIVEN WHEN USING THE FUNCTION I.E header("menu")
    if hint != "":  # IF THERE IS A HINT DISPLAY IT
        print(f'HINT: {hint}')
    else:  # IF NO HINT THEN DO NOTHING
        pass

    if error != "":  # IF THERE IS A ERROR DISPLAY IT AND MAKE NEW LINE
        print(f"ERROR: {error}\n")
    else:  # IF NO ERROR THEN JUST MAKE A NEW LINE
        print()

    error = ""  # RESET ERROR
    hint = ""  # RESET HINT


def registration():
    global error  # THIS CODE EDITS THESE VARIABLES

    user_verification = False
    while not user_verification:  # UNTIL A VALID USERNAME IS GIVEN
        header("create_user")
        username = input("ENTER A NEW USERNAME: ").lower().strip()  # USERNAMES ARE STORED AS LOWERCASES
        for user in current_users:
            if user['username'] != username:  # IF THE USERNAME ISN'T TAKEN THEN PASS THE VERIFICATION
                user_verification = True
            else:  # IF USER TAKEN THEN RETRY AND PRINT ERROR MESSAGE
                error = "Username taken."
    pass_verification = False
    while not pass_verification:  # UNTIL A VALID PASSWORD IS GIVEN
        header(f'{username.lower()}_create_password')
        password = input("ENTER THE PASSWORD: ")  # INPUT PASSWORD FROM USER
        count = 0
        for char in password:  # FOR EVERY CHARACTER IN THE PASSWORD
            count = count + 1  # GET THE TOTAL NUMB OF CHARACTERS
        if count >= 3:  # PROCEED ONLY IF 3 OR MORE CHARACTERS
            if any(ele.isnumeric() for ele in password):  # PROCEED ONLY IF CONTAINS NUMBERS
                if any(ele.isupper() for ele in password):  # PROCEED ONLY IF CONTAINS UPPER CASES
                    if any(ele not in "[@_!#$%^&*()<>?/|}{~:]" for ele in password):  # PROCEED ONLY IF USES SYMBOLS
                        confirm_password = input("CONFIRM THE PASSWORD: ")  # CHECK TO MAKE SURE PASS WAS CORRECT
                        if password == confirm_password:  # IF PASS WAS CORRECT
                            # PROMPT IF THEY WANT TO ADD A HINT
                            valid_int = False
                            while not valid_int:
                                header(f"{username.lower()}_propmt_password_hint")
                                print('Enter one the following:')
                                print('1 : Proceed with no password hint.')
                                print('2 : Create a password hint for my account.')
                                try:
                                    choice = int(input("\nSELECT AN OPTION: "))
                                except:
                                    pass
                                if choice == 1 or choice == 2:
                                    valid_int = True
                                else:
                                    error = "Invalid Option!"
                            if choice == 2:  # IF THEY WANT A HINT THEN CREATE ACCOUNT WITH A HINT, PASS, AND USER
                                header(f"{username.lower()}_create_password_hint")
                                hint = input("PLEASE ENTER YOUR HINT: ")
                                create_user(username, password, hint)
                            elif choice == 1:  # IF THEY DONT WANT A HINT THEN CREATE ACCOUNT WITH PASS AND USER
                                create_user(username, password)
                            pass_verification = True
                        else:
                            error = "Passwords do not match."
        error = "Password must be at least 3 characters. And contain at least one capital letter, symbol and number."


def search_user(username):
    index = -1
    i = 0
    for user in current_users:
        if user['username'].lower() == username.lower():
            index = i
            break
        i = i + 1
    return index


def authentication(user_index):
    global error, hint  # THIS CODE EDITS THESE VARIABLES
    hint = ""

    correct_pass = False
    count = 0
    while not correct_pass and count < 3:  # IF THEY GOT THE PASSWORD WRONG LESS THAN 3 TIMES
        user = current_users[user_index]
        header(f"{user['username'].lower()}_sign_in")
        user_password = input("ENTER YOUR PASSWORD: ")  # INPUT PASSWORD FROM USER
        if user['password'] == user_password:  # IF CORRECT
            correct_pass = True  # EXIT LOOP
        else:  # IF WRONG
            count = count + 1  # ADD TO COUNT
            if count == 3:  # IF TOO MANY FAILS EXIT
                error = "Too many failed attempts!"
            else:  # OTHER WISE SHOW HOW MANY ATTEMPTS LEFT, AND BEGIN TO SHOW HINT
                error = f"Incorrect password. You have {3 - count} attempt(s) left."
                if user.get('hint', "None") != "None":
                    hint = f"{user['hint']}"
    return correct_pass


def create_user(username, password, hint="None", type="default"):  # DEFAULT hint TO NONE IF NOT SPECIFIED
    global error
    new_user = {'username': username, 'password': password, 'type': type,
                "hint": hint}  # ACCOUNTS ARE CREATED AS GUESTS
    current_users.append(new_user)  # ADD THE USER TO LIST
    print(spacer)
    print("USER CREATED! SELECT OPTION '1' WHILE IN THE MAIN MENU\n\n\n")
    write_to_file("accounts.txt")  # SAVE DATA
    time.sleep(5)
    error = ""


def logged_out_menu():  # DISPLAY THE LOGGED OUT MENU
    header("logged_out_main_menu")
    print('Enter one the following:')
    print('1 : Sign In')
    print('2 : Sign Up')
    print('0 : Shut Down')
    choice = input('\nENTER YOUR OPTION: ')
    return choice


def launch_app():
    global error, logged, choice  # THIS CODE EDITS THESE VARIABLES

    logged_out = False
    while not logged_out:  # WHILE LOGGED IN
        choice = ""
        logged_menu()  # SHOW OPTIONS
        if choice == "1":
            launch_game()
        elif choice == "2":  # THEY NEED TO HAVE THE 'type': 'admin' IN THE USER'S DICTIONARY
            check_user = current_users[search_user(logged)]
            if check_user['type'] == "admin":
                admin_access()
            else:
                error = "Invalid Permissions. If this is a mistake, please contact the super administrator to change " \
                        "your account type to 'admin' within the storage."
        elif choice == "0":
            logged_out = True
            logged = ""
        else:
            error = "Invalid Option."


def logged_menu():  # DISPLAY THE USER MENU
    global choice
    header(f'{logged}_main_menu')
    print('Enter one the following:')
    print('1 : Launch Game')
    print('2 : Admin Menu')
    print('0 : Log Out')
    choice = input('\nENTER YOUR OPTION: ')


def print_users():
    for i in range(100):  # LINE SKIPS
        print()
    header("accounts.txt")
    for user in current_users:  # FOR EVERY USER DISPLAY A UNIQUE WIDGET SHOWING ALL DETAILS ABOUT ALL ACCOUNTS
        print(f'''==========
= Username: {user["username"]}
= Password: {user["password"]}
= Rank: {user["type"].upper()}
= Hint: {user["hint"]}''')
    print("==========")
    pause = input(
        "(SCROLLING MAY BE NECESSARY FOR VIEWING USERS) PRESS ENTER WHEN COMPLETE: ")  # THE INPUT FUNCTION PAUSES CODE SO USER CAN READ


def edit_user(modification):
    global error  # THIS CODE EDITS THESE VARIABLES

    header(f"admin_access_edit_user_{modification}")
    account_name = input("ENTER THE USERNAME OF THE ACCOUNT TO EDIT: ").lower()  # GET THE INDEX OF THE ACCOUNT TO EDIT
    u_index = search_user(account_name)
    if u_index == -1:
        error = 'User does not exist.'
    else:
        print(current_users[u_index])
        current_users[u_index][f'{modification}'] = input(
            f"ENTER NEW {modification.upper()}: ")  # EDIT THE SPECIFIED VALUE WITH THE VALUE INPUTTED BY USER
    write_to_file('accounts.txt')  # SAVE DATA
    print_users()  # SHOW ADMIN THE LIST


def del_user():
    global error  # THIS CODE EDITS THESE VARIABLES

    header("admin_access_delete_account")
    username = input("ENTER THE USERNAME OF THE ACCOUNT TO DELETE (PERMANENT): ").lower()  # GET THE USERNAME TO DELETE
    deletion_check = False  # CHECK IF IT HAS BEEN DELETED THIS WILL CHANGE TO TRU WHEN THE MAIN DELETE EVEN HAPPENS
    for i in range(len(current_users)):  # FOR EVERY USER THAT EXISTS
        if current_users[i]['username'] == username:  # IF USER HAS SPECIFIED NAME
            del current_users[i]  # DELETE WHOLE DICTIONARY FOR USER IN LIST
            deletion_check = True
            print_users()
            break  # END EARLY
    username = ""
    write_to_file('accounts.txt')
    if deletion_check == False:
        error = "No Account was Removed."


def admin_register():
    header("admin_access_uct")
    username = input('USERNAME: ').lower()
    password = input('PASSWORD: ')
    type = input('TYPE ("admin" OR "guest"): ').lower()
    hint = input('HINT (DEFAULT: None): ')
    create_user(username, password, hint, type)  # MERGE ALL DATA INTO ONE USER


def admin_access():
    global admin_action, exit_admin

    exit_admin = False
    while not exit_admin:
        admin_menu()
        if admin_action == "1":
            print_users()
        elif admin_action == "2":
            edit_user('password')
        elif admin_action == "3":
            edit_user('username')
        elif admin_action == "4":
            edit_user('hint')
        elif admin_action == "5":
            edit_user('type')
        elif admin_action == "6":
            del_user()
        elif admin_action == "7":
            admin_register()
        elif admin_action == "0":
            exit_admin = True
        else:
            error = "Invalid Option."


def admin_menu():  # DISPLAY THE ADMIN MENU
    global admin_action
    header('admin_access')
    print('Enter one the following: (Index values are required for usage for options 2-6)')
    print('1 : See User Index')
    print("2 : Change a User's Password")
    print("3 : Change a User's Username")
    print("4 : Change a User's Hint")
    print("5 : Change a User's Permissions")
    print('6 : Delete a User')
    print('7 : Advanced User Creation Tool')
    print('0 : Go Back')
    admin_action = input('\nENTER YOUR OPTION: ')


def launch_game():
    print(spacer)

    print("Welcome to words guessing game")
    words_dic = {
        'something that you measure with': 'ruler',
        'something with ink that you write with': 'pen',
        'the species that you are': 'human',
        'pink farm animals': 'pig',
        'something that you drink from': 'cup',
        'most common type of animal living in the sea': 'fish',
        'form of transport that many people own': 'car',
        'white liquid coming from an animal': 'milk',
        'parts of your body you use for walking': 'legs',
        'colour you get when you mix red and white': 'pink'}
    # create a dictionary, key is the definition and value is the word
    Definitions = list(words_dic.keys())
    print("Let's learn some words. 3 rounds. Enter exit to quit the game.")
    point = 0  # this is the score
    for i in range(3):
        definition = random.choice(Definitions)  # randomly select 3 definitions
        word = words_dic[definition]
        user_guess = input('what is the word for %s?' % definition)
        if user_guess.lower() == 'exit':  # if a user type in exit, the game exits
            break
        elif user_guess == word:
            point += 1
            print('Correct! Your score is %d' % point)
        else:
            print('Incorrect. The word for {} is {}.'.format(definition, word))
    print('We are done. Your final score is %d, thank you.' % point)

    time.sleep(5)


start()
