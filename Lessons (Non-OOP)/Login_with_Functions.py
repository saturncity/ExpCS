import json
import ast

current_users = []
admin = {'username': 'admin', 'password': 'guess_me'}  # add password hint and user type
                                                    # i.e. 'hint': 'Who should I guess?', 'account type': 'admin'
current_users.append(admin)

# current_users = [admin]


def write_to_file(file_name):
    with open(file_name, 'w') as file_out:
        json.dump(current_users, file_out)
        print("File output done.")


def read_file(file_name):
    with open(file_name, 'r') as file_in:
        new_list = ast.literal_eval(file_in.read())
        global current_users
        current_users = new_list
        print("File input done.")


def registration():
    username = input("Enter a new username: ").lower().strip()
    # **** implement a searching and checking whether or not the username is already exist ****
    #
    pass_verification = False
    while not pass_verification:
        password = input("Enter a password: ")
        count = 0
        for char in password:
            count = count + 1

        if count >= 10:
            confirm_password = input("Reenter the password: ")
            if password == confirm_password:
                create_user(username, password)
                pass_verification = True
            else:
                print("Verification Failed. Please enter the same password twice")
        else:
            print("Please enter a password with at least 10 characters.")


def create_user(username, password):
    new_user = {'username': username, 'password': password}
    current_users.append(new_user)
    write_to_file('accounts.txt')
    print(f"{username.title()} has been added.")


def authentication(user_index):
    correct_pass = False
    count = 0
    while not correct_pass and count < 3:
        user_password = input("Enter your password: ")
        user = current_users[user_index]
        if user['password'] == user_password:
            print(f"Welcome, {user['username'].title()}")
            correct_pass = True
        else:
            count = count + 1
            if count == 3:
                print("Authentication failed. Please try again.")
            else:
                print("Incorrect password. Please try gain.")
                print(f"You have {3 - count} attempt(s) left.")

    return correct_pass


def search_user(username):
    index = -1
    i = 0
    for user in current_users:
        if user['username'].lower() == username.lower():
            index = i
            break

        i = i + 1
    return index


def launch_app():
    print('Launching the application...')
    exit()


def display_menu():
    print('Enter one the followings:')
    print('"1" for Login.')
    print('"2" for Registration.')
    # print('"3" to Search a User.')
    # print('"4" to update Password.')
    # print('"5" to update Username.')
    # print('"6" to Print all Users.')
    # print('"7" to Delete a User.')
    print('"8" to Save all Users.')
    print('"9" to Read all Users.')
    print('"91" to exit.')
    choice = input('What would you like to do? : ')
    return choice


# main program
separator = '--------------------------'
exit_program = False
print('~*~  Welcome to my program ~*~')
read_file('accounts.txt')
while not exit_program:
    print(separator)
    u_choice = display_menu()
    if u_choice == '1':
        account_name = input("Enter your username: ")
        u_index = search_user(account_name)
        if u_index == -1:
            print("User doesn't exit. Please try again.")
        else:
            auth_pass = authentication(u_index)
            if auth_pass:
                launch_app()
    elif u_choice == '2':
        registration()
    elif u_choice == '8':
        write_to_file('accounts.txt')
    elif u_choice == '9':
        read_file('accounts.txt')
    elif u_choice == '91':
        print('Okay. Goodbye. See you next time.')
        exit_program = True
    else:
        print("Invalid option. Please try again.")
