#message = str.capitalize('my message')
#print(message)
#
#message = 'my message'.capitalize()
#print(message)
#
#message = 'my message'
#print(message.capitalize())

#message = 'hello world'
#print(message.lower())
#print(message.upper())
#
#message = message.title()
#print(message)
#print(message.swapcase())

#location = 'mississipi'
#print(location.count('s'))
#
#print(len('how many characters are in this string'))

message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)