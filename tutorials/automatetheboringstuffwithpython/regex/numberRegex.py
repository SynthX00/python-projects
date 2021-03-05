import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 415-555-4242.") #mo is a generic name for "Match Object"
print("Phone number found: " + mo.group())