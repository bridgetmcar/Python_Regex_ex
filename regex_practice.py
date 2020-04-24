import re
x = '3036 many reasons, ranging from making your living to solving 7209'
y = re.findall('[0-9]+', x)
print(y)

x = 'My 5 numbers are 2, 19 and 2025'
y = re.findall('[aeiou]+', x)
print(y)

x = 'My 5 numbers are 2, 19 and 2025'
y = re.findall('[AEIOU]+', x)
print(y)

x = "From: Using the : character"
y = re.findall('^F.+?:', x)
print(y)

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('\S+?@\S+', x)
print(y)
#find the string around the @
y = re.findall('^From (\S+@\S+)', x)
print(y)
#at the @ find nonblank characters
y = re.findall('@([^ ]*)', x)
print(y)
