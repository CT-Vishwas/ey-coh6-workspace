data = {
"vishwas@cloudthat.com": 1,
"alice@cloudthat.com":10,
"kiran@cloudthat.com":3,
"Riya@cloudthat.com": 15
}

# data_lst = list(data.items())
# data_lst.sort(reverse=True)
# data_lst.sort(key=lambda x:x[1], reverse=True)
# print(f"|{'Emailid':<30}|{'Attempts':<30}|")
# print('|'+"-"*61+'|')
# for k,v in data_lst:
#     print(f"|{k:<30}|{v:<30}|")

data_dict = {k:v for k,v in data.items() if v == 3}
print(data_dict)