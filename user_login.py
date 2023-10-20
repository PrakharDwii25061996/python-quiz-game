import bcrypt


if __name__ == '__main__':

	user = input("Enter name: ")
	password = input("Enter password: ")

	password_in_bytes = password.encode('utf-8')

	user_password = b'Myaddiddie'

	if bcrypt.checkpw(password_in_bytes, user_hashed_password):
		print("Login Successfull! ")
	else:
		print("Login UnSuccessfull! ")
