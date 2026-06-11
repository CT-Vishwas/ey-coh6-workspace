'''
Module to handle email related common functionalities
'''
def is_valid_email_basic(email: str)-> bool:
    '''
    Returns True if the email id is VALID
    '''
    if email.find("@") != -1 and email.count("@") == 1:
        return True
    else:
        return False
    
def is_valid_email(email: str) -> bool:
    '''
    Returns True if the email id is VALID
    '''
    import re
    pattern = r'^[a-z][a-z0-9.]+@[a-z]{2,20}.[a-z]+'
    if re.match(pattern, email):
        return True
    else:
        return False
    
if __name__ == "__main__":
    email = input("Enter an email id to validate: ")
    if is_valid_email(email):
        print(f"Email id '{email}' is valid.")
    else:
        print(f"Email id '{email}' is invalid.")