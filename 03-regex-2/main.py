import re

def extract_mmddyyyy(txt):
    """Extracts month, day, and year of the first matched mm/dd/yyyy format date"""
    response = { 'ok': False }
    format = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
    result = format.search(txt)
    if result:
        response['ok'] = True
        response['full_date'] = result.group(0)
        response['month'] = int(result.group(1))
        response['day'] = int(result.group(2))
        response['year'] = int(result.group(3))
    return response

print("This program will take a string, look for the first date in mm/dd/yyyy format, and")
print("return the full date, month, day, and year as part of a dictionary.")
txt = input("Please enter input to check:\n~> ")

result = extract_mmddyyyy(txt)

if result['ok']:
    print("\nDate: ", result['full_date'], "\n")
    print("Month: ", result['month'])
    print("Day:   ", result['day'])
    print("Year:  ", result['year'])
else:
    print("\nDid not find a valid date within the provided input")