"""
	This module contains functions for user login and authentication.

"""

import bcrypt
import shelve
import getpass
import os


def retreive_user(user_email, entered_password):
	"""
	This function returns the user information for the user.txt
	file using shelve module.

	Arguments:
	1. user_email: str
	 -  User email for retreiving it.

	2. entered_password: str
	 -  User password for retreiving it.

	Returns:
	tuple containing user data and user hashed password.

	"""
	with shelve.open(f'{os.getcwd()}/user.txt', 'r') as user_file:
		try:
			user = user_file[user_email]
			user_hashed_password = user.get('password')
		except Exception as e:
			user, user_hashed_password = None, b''
		user_file.close()

	return (user, user_hashed_password)


def get_user_password_in_bytes(entered_password):
	"""
	This coverts the user password in bytes and returns it.

	Arguments:
	entered_password: str
	 - User entered password for login.

	"""
	if not entered_password:
		print("Please enter valid password")
		return None
	else:
		return entered_password.encode('utf-8')


def check_login_password(user, user_hashed_password, password_in_bytes):
	"""
	This checks the user login password corrects or not by taking the entered password
	and user registered password.

	Arguments:
	user: dict
	 -  Registered user information

	user_hashed_password: byte 
	 -  Registered user password in hashed format.

	password_in_bytes: byte
	 -  Entered user password for login in hashed format.

	"""
	if user and bcrypt.checkpw(password_in_bytes, user_hashed_password):
		print("Login Successfull! ")
	else:
		print("Please enter correct email or password. ")


if __name__ == '__main__':

	# The user enters the email and password
	user_email = input("Enter Email: ")
	entered_password = getpass.getpass("Enter password: ")

	# Retreives user information
	user, user_hashed_password = retreive_user(
		user_email,
		entered_password
	)

	password_in_bytes = get_user_password_in_bytes(entered_password)

	if not password_in_bytes: # check whether the password in bytes is none or not.
		print("Please Enter Password. ")
	else:
		check_login_password(user, user_hashed_password, password_in_bytes)
