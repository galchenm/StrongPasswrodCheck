from getpass import getpass

password = getpass("Enter your password: ")
result = {}

if len(password) >= 8:
  result['length'] = True
else:
  result['length'] = False

if any(char.isdigit() for char in password):
  result['digit'] = True
else:
  result['digit'] = False

if any(char.isupper() for char in password):
  result['upper-case'] = True
else:
  result['upper-case'] = False

if any(char.islower() for char in password):
  result['lower-case'] = True
else:
  result['lower-case'] = False

if any(char in "!@#$%^&*()_+-=" for char in password):
  result['special-symbol'] = True
else:
  result['special-symbol'] = False

if all(result.values()):
  print("Strong password")
else:
  print("Weak password")
  print("The problem is withe the following:")
  for key, value in result.items():
    if not value:
      print(key)
