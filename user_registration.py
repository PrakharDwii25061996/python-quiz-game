import os
import pprint
import bcrypt


def get_hashed_password(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password.encode(), salt)


if __name__ == '__main__':

	try:
		user_file = open(f'{os.getcwd()}/user.py', 'w+')
		user_file.close()
	except FileExistsError as e:
		print(e)

	user_name = input("Enter name: ")
	user_email = input("Enter email: ")
	password = input("Enter Password: ")


	user = {
		'user_name': user_name,
		'user_email': user_email,
		'password': get_hashed_password(password),
		'quizes': 0,
		'maximum_score': 0
	}

	user_data_file = open(f'{os.getcwd()}/user.py', 'w')
	user_data_file.write(pprint.pformat(user))
