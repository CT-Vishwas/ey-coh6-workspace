# # Email Validation
# email = input("Enter the email Id: ")
# if email.find("@") != -1 and email.count("@") == 1:
#     print(f"{email} is VALID")
#     # Username Extraction
#     print(f"Username: {email[:email.find("@")]}")
# else:
#     print(f"{email} is INVALID")

flg = 0
ip_address = input("Enter the IPv4 Address: ")
fields = ip_address.split(".")
if len(fields) != 4:
    print(f"{ip_address} is INVALID")
    flg = 1
else:
    for field in fields:
        if not field.isdigit():
            print(f"{ip_address} is INVALID")
            flg = 1
            break

        val = int(field)
        if not (val >= 0 and val <= 255):
            print(f"{ip_address} is INVALID")
            flg = 1
            break

if flg == 0:
    print(f"{ip_address} is VALID")