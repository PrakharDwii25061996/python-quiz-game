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

		if (len(password) > conf.PASSWORD_MINIMUM_LENGTH) and (len(password) < conf.PASSWORD_MAXIMUM_LENGTH):
			print("Please Enter password having minimum characters 8 and maximum 15. ")
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


def get_user_email():

	while True:
		email = input("Enter email: ")

		if not (email and email.endswith('@gmail.com')):
			print("Please Enter correct email. ")
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

	print(user_name)
	print(user_email)
	print(password)

	# user = get_user_data(user_name, user_email, password)

	# save_user_data(user)
