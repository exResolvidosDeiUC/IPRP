def print_emails(names_file, domain):
    with open(names_file, 'r') as f:
        emails = sorted([line.split(' ')[0][0] + line.split(' ')[1][:-1] + '@' + domain for line in f.readlines()])
    print('\n'.join(emails))

print_emails('names.txt', 'dei.uc.pt')