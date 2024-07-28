import random
import string
#Get user input for password length

length=int(input("Enter the length of Password(Minimum length of 4):"))
if length<4:
    print("Password will be less strong")

#Generate the password
def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Display the password

password = generate_password(length)
print("Generated Password:", password)


