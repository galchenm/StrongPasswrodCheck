from getpass import getpass

password = getpass("Enter your password: ")
result = []

if len(password) >= 8:
  result.append(True)
else:
  result.append(False)

if any(char.isdigit() for char in password):
  result.append(True)
else:
  result.append(False)

if any(char.isupper() for char in password):
  result.append(True)
else:
  result.append(False)

if any(char.islower() for char in password):
  result.append(True)
else:
  result.append(False)

if any(char in "!@#$%^&*()_+-=" for char in password):
  result.append(True)
else:
  result.append(False)

if all(result):
  print("Strong password")
else: 
  print("Weak password")
  