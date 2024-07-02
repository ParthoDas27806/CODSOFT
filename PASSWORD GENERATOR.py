import random
import string

def generate_password(length):
  """Generates a random password with the specified length and includes numbers.

  Args:
      length: The desired length of the password.

  Returns:
      A randomly generated password string.
  """

  # Define the character set including lowercase letters, uppercase letters, and digits
  characters = string.ascii_letters + string.digits

  # Generate the password
  password = ''.join(random.choices(characters, k=length))

  return password

# Get user input for password length
while True:
  try:
    length = int(input("Enter desired password length (minimum 5 characters): "))
    if length < 5:
      print("Password length must be at least 5 characters. Please try again.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")

# Generate and print the password
password = generate_password(length)
print("Your generated password is:", password)