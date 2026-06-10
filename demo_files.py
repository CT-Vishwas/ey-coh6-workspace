# fh = open("first.py")
# data = fh.read()
# print(data)
# fh.close()

# A context manager
# try:
#     with open("first1.py", "rt") as fh:
#         data = fh.read()
#         print(data)
# except FileNotFoundError:
#     print("File you are trying to read does not exist")

try:
    with open("demo_write.txt", "x") as fh:
        fh.write("I am vishwas")
except FileExistsError:
    print("Trying to overwrite the file! NOT ALLOWED")
except Exception:
    print("Unknown error occured")