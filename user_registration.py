"""
This module is used for teacher and student registration.
"""
import os
import pprint
import bcrypt
import shelve
import getpass

import conf


def get_hashed_password(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password.encode(), salt)


def get_password():

	while True:
		password = getpass.getpass("Enter Password: ")
		if not (len(password) >= conf.PASSWORD_MINIMUM_LENGTH) and (len(password) <= conf.PASSWORD_MAXIMUM_LENGTH):
			print("Please Enter password having minimum characters 8 and maximum 15. ")
		elif password.isupper() or password.islower() or password.isdigit():
			print("""
				Please Enter password containing atleast one small letters,
				one capital letters and one numeric letter
			""")
		else:
			break

	return password


def get_user_data(user_name, user_email, password):
	user = {
		'user_email': user_email, 
		'user_name': user_name,
		'password': get_hashed_password(password),
		'quizes': 0,
		'maximum_score': 0
	}
	return user


def get_user_name():

	while True:
		name = input("Enter Name: ")
		if not (name and (len(name.split()) <= 3) and name.istitle()):
			print("Please enter correct username. ")
		else:
			break
	
	return name


def check_email_exists(email):

	with shelve.open(f'{os.getcwd()}/user.txt', 'r') as user_file:
		if email in dict(user_file).keys():
			return True
		user_file.close()	

	return False


def get_user_email():

	while True:
		email = input("Enter email: ")

		if not email.endswith('@gmail.com'):
			print("Please Enter correct email. ")
		elif check_email_exists(email):
			print("User email already exist. ")
		elif not email:
			print("Please enter valid email.")
		else:
			break

	return email


def save_user_data(user):
	with shelve.open(f'{os.getcwd()}/user.txt', 'c') as user_file:
		user_file[user_email] = user
		user_file.close()


if __name__ == '__main__':

	user_name = get_user_name()

	user_email = get_user_email()

	password = get_password()

	user = get_user_data(user_name, user_email, password)

	save_user_data(user)

	print(user_name)
	print(user_email)
	print(password)
