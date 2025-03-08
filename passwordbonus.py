# password = input('Enter the password:')

# result = []

# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)

# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True

# result.append(digit)

# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True

# result.append(uppercase)

# if all(result) == True:
#     print('Strong Password')
# else:
#     print('Weak Password')


# Use Dict
password = input('Enter the password:')

result = {}

if len(password) >= 8:
    result['Length'] = True
else:
    result['Length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['Digits'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['Uppercase'] = uppercase

if all(result) == True:
    print('Strong Password')
else:
    print('Weak Password')
            