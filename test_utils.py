# general import
# import utils
# print(utils.is_valid_email("vishwas@cloudthat.com")) #True

# specific functio import
# from utils import is_valid_email
# print(is_valid_email("vishwas@cloudthat.com")) #True

# aliasing



# importing multiple modules
# from utilities.email_utils import is_valid_email
# from utilities.ipv4_utils import is_valid_ip
# print(is_valid_email("vishwas@cloudthat.com")) #True
# print(is_valid_ip("192.168.1.1"))

# importing multiple modules at once using __init__.py
# from utilities import is_valid_email, is_valid_ip 
# print(is_valid_email("vishwas@cloudthat.com")) #True
# print(is_valid_ip("192.168.1.1"))

from utilities import *
print(email_utils.is_valid_email("vishwas@cloudthat.com")) #True
print(ipv4_utils.is_valid_ip("192.168.1.1"))
#print(utils.add()) # This gives not defined error

