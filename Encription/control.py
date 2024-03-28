class User:
    def __init__(self, name, password, security_level):
        self.name = name
        self.password = password
        self.security_level = security_level

userlist = [
   [ "AdmiralAbe",     "password", "Secret" ],  
   [ "CaptainCharlie", "password", "Privileged" ], 
   [ "SeamanSam",      "password", "Confidential" ],
   [ "SeamanSue",      "password", "Confidential" ],
   [ "SeamanSly",      "password", "Confidential" ]
]

users = [User(name, password, security_level) for name, password, security_level in userlist]

def get_usernames():
    return [user.name for user in users]

def authenticate_user(username, password):
    for user in users:
        if user.name == username and user.password == password:
            return True
    return False

def get_user_security_level(username):
    for user in users:
        if user.name == username:
            return user.security_level
    return None

def can_view_message(username, message_classification):
    user_security_level = get_user_security_level(username)
    if user_security_level == "Secret":
        return True
    elif user_security_level == "Privileged" and message_classification != "Secret":
        return True
    elif user_security_level == "Confidential" and message_classification == "Confidential":
        return True
    elif user_security_level == "Public" and message_classification == "Public":
        return True
    return False

def can_add_message(username):
    user_security_level = get_user_security_level(username)
    return user_security_level in ["Privileged", "Secret"]

def can_modify_message(username, message_classification):
    user_security_level = get_user_security_level(username)
    return user_security_level == "Secret" or (user_security_level == "Privileged" and message_classification != "Secret")

def can_delete_message(username, message_classification):
    user_security_level = get_user_security_level(username)
    return user_security_level == "Secret" or (user_security_level == "Privileged" and message_classification != "Secret")
