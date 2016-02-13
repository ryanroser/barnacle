# models.py

def greet_user(user_name):
    """Creates a greeting for a user base off of the user name"""
    if len(user_name) % 2 == 0:
        greeting = "Nice to see you!"
    else:
        greeting = "Thanks for visiting!"
    return greeting
