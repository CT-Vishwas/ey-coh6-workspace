'''
Module to handle email related common functionalities
'''
def is_valid_email(email: str)-> bool:
    '''
    Returns Ture if the email id is VALID
    '''
    if email.find("@") != -1 and email.count("@") == 1:
        return True
    else:
        return False