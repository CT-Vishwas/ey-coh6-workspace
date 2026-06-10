from  dataclasses import dataclass
# Read the files
# data classes
# dict of login counts
# mark 


@dataclass
class Event:
    date: str
    time: str
    success: bool
    email: str
    ipaddress: str

count_dict = dict()

def data_reader(file_path):

    try:
        with open(file_path,"rt") as fh:
            while True:
                line = fh.readline()
                if not line:
                    break
                data = line.split()
                is_success = True if data[2] == "[SUCCESS]" else False
                event = Event(date=data[0], time=data[1], success=is_success,email=data[4],ipaddress=data[7])
                yield event
    
    except FileNotFoundError:
        print(f"{file_path} does not exist")



def main():
    file_path = r"C:\Users\VishwasKSingh\Workspace\ey-coh6-workspace\data\susp_log"
    for event in data_reader(file_path):
        if not event.success:
            count_dict[event.email] = count_dict.get(event.email,0) + 1
    # print(count_dict)
    print("Suspicious Emails:")

    print(f"|{'Email':<30}|{'Failed Logins':<20}|{'Marked Suspicious':<20}|")
    print("|" + "-" * 30 + "|"+"" + "-" * 20 + "|" + "-" * 20 + "|")

    for email, count in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
        is_suspicious = "YES" if count >= 2 else "NO"
        if is_suspicious == "YES":
            print(f"|{email:<30}|{count:<20}|{is_suspicious:>20}|")
        else:
            print(f"|{email:<30}|{count:<20}|{is_suspicious:<20}|")

if __name__ == '__main__':
    main()


