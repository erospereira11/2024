import messages
import control

class Interact:
    def __init__(self, username, password, messages):
        self._authenticate(username, password)
        self._username = username
        self._p_messages = messages

    def show(self):
        id_ = self._prompt_for_id("display")
        if control.can_view_message(self._username, self._p_messages.get_message_classification(id_)):
            self._p_messages.show(id_)
        else:
            print("Access denied: You do not have permission to view this message.")

    def display(self):
        print("Messages:")
        self._p_messages.display()

    def add(self):
        if control.can_add_message(self._username):
            self._p_messages.add(self._prompt_for_line("message"), self._username, self._prompt_for_line("date"))
        else:
            print("Access denied: You do not have permission to add messages.")

    def update(self):
        id_ = self._prompt_for_id("update")
        if control.can_modify_message(self._username, self._p_messages.get_message_classification(id_)):
            self._p_messages.update(id_, self._prompt_for_line("message"))
        else:
            print("Access denied: You do not have permission to update this message.")

    def remove(self):
        id_ = self._prompt_for_id("delete")
        if control.can_delete_message(self._username, self._p_messages.get_message_classification(id_)):
            self._p_messages.remove(id_)
        else:
            print("Access denied: You do not have permission to delete this message.")

    def display_options(self):  # Define display_options function
        print("\td .. Display the list of messages\n" +
              "\ts .. Show one message\n" +
              "\ta .. Add a new message\n" + 
              "\tu .. Update an existing message\n" + 
              "\tr .. Delete an existing message\n" + 
              "\to .. Display this list of options\n" + 
              "\tl .. Log out\n")

    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    def _authenticate(self, username, password):
        return control.authenticate_user(username, password)

def session(messages):
    open_session()

    print("Users:")
    display_users()
    username = input("\nWhat is your username? ")
    password = input("What is your password? ")

    interact_ = Interact(username, password, messages)
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

def display_users():
    users = control.get_usernames()
    for username in users:
        print(f"\t{username}")

def open_session():
    global session_open
    session_open = True

def close_session():
    global session_open
    session_open = False
