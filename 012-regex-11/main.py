import re

rx = re.compile(r'<div(.*)>(.*)</div>')

faux_html = "<div class='menu-item'>Home</div>"

print("Assuming the string:\n\t", faux_html)

result = rx.search(faux_html)

if result:
    print("Full match:\n\t", result.group(0))
    print("Div attributes:\n\t", result.group(1))
    print("Contents of div:\n\t", result.group(2))