import interact
import messages  

def main():
    try:
        messages_ = messages.Messages("messages.txt")
    except FileNotFoundError:
        print("Error: Unable to open 'messages.txt'. Make sure the file exists.")
        return
    
    done = False
    while not done:
        interact.session(messages_)
        done = input("Will another user be logging in? (y/n) ").upper() != "Y"

if __name__ == "__main__":
    main()

def session(messages):
    open_session()
    print("Users:")
    interact.display_users()
    username = input("\nWhat is your username? ")
    password = input("What is your password? ")
    interact_ = interact.Interact(username, password, messages)
    print(f"\nWelcome, {username}. Please select an option:\n")
    interact_.display_options()
    options = {
        "o": "print('Options:'); interact_.display_options();",
        "d": "interact_.display();",
        "s": "interact_.show();",
        "a": "interact_.add();",
        "u": "interact_.update();",
        "r": "interact_.remove();",
        "l": "print(f'Goodbye, {username}{chr(10)}'); close_session();"
    }
    while session_open:
        option = input(f"{username}> ")
        exec(options.get(option, "print(f\"Unknown option: \'{option}\'\");"))

def close_session():
    global session_open
    session_open = False

def open_session():
    global session_open
    session_open = True

session_open = True  # Added global variable initialization

if __name__ == "__main__":
    main()
