
def read_mbox_file(file_path: str):
    '''
    Reads the mbox file and prints the email ids of the senders
    '''
    try:
        with open(file_path, 'r') as fh:
            while True:
                line = fh.readline()
                if not line:
                    break

                yield line.strip()

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    file_path = r"C:\Users\VishwasKSingh\Workspace\ey-coh6-workspace\data\mbox.txt"
    emails = []
    for line in read_mbox_file(file_path):
        if line.startswith("From:"):
            email = line.split()[1]
            emails.append(email)

    emails = list(set(emails))
    print("Email ids of the senders:")
    for email in emails:
        print(email)