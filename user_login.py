import bcrypt
import shelve
import getpass
import os


def retreive_user(user_email, entered_password):
	with shelve.open(f'{os.getcwd()}/user.txt', 'r') as user_file:
		try:
			user = user_file[user_email]
			user_hashed_password = user.get('password')
		except Exception as e:
			user, user_hashed_password = None, b''
		user_file.close()

	return (user, user_hashed_password)


def get_user_password_in_bytes(entered_password):
	if not entered_password:
		print("Please enter password")
		return None
	else:
		return entered_password.encode('utf-8')


def check_login_password(user, user_hashed_password, password_in_bytes):
	if user and bcrypt.checkpw(password_in_bytes, user_hashed_password):
		print("Login Successfull! ")
	else:
		print("Please enter correct email or password. ")


if __name__ == '__main__':

	user_email = input("Enter Email: ")
	entered_password = getpass.getpass("Enter password: ")

	user, user_hashed_password = retreive_user(
		user_email,
		entered_password
	)

	password_in_bytes = get_user_password_in_bytes(entered_password)

	if not password_in_bytes:
		print("Please Enter Password. ")
	else:
		check_login_password(user, user_hashed_password, password_in_bytes)
