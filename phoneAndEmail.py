# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard. 
import pyperclip, re
text = str(pyperclip.paste())
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (optional)
    (\s|-|\.)?                      # separator (optional)      
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional)
    )''', re.VERBOSE)
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)
matches = []
for phoneMatch in phoneRegex.findall(text):
    matches.append(phoneMatch[0])
    for emailMatch in emailRegex.findall(text):
        matches.append(emailMatch[0])
        print(f'Phone number: {phoneMatch[0]}, Email address: {emailMatch[0]}')
        pyperclip.copy(emailMatch[0])
        print('Copied email address to clipboard.')
        pyperclip.copy(phoneMatch[0])
        print('Copied phone number to clipboard.')
        print('Copied phone number and email address to clipboard.')
if len(matches) > 0:
    print(f'Total matches found: {len(matches)}')
else:
    print('No phone numbers or email addresses found.')
cvc