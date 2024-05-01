import random
import string
def password_generator(lenght):
	character = string.ascii_letters + string.digits + string.punctuation
	password = "".join(random.choice(character)for i in range(lenght))
	return password

password_lenght = 12
generated_password = (password_generator(password_lenght))
print ("Gneratred password", generated_password)