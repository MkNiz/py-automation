import re

def extract_dates(text):
    all_dates = []
    formats = [
        re.compile(r'\d{2}/\d{2}/\d{2,4}'),
        re.compile(r'\d{2}\.\d{2}\.\d{2,4}'),
    ]
    
    for format in formats:
        results = format.findall(text)
        for result in results:
            all_dates.append(result)
            
    return all_dates

print("This program strips and displays dates in the supported formats from")
print("the string you provide.\n")
txt = input("Please enter input to check:\n~> ")

dates = extract_dates(txt)

print("Dates found:\n")
for date in dates:
    print(date)
    