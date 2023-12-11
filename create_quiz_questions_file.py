"""
	This modules contains functions to get quiz questions
	and saves it in quiz.txt file using shelve module.

"""

import random
import pprint
import shelve
import os


def save_quiz_questions(number_of_quizes, quiz_questions_and_answers):
	"""
		Saves quiz questions and answers in quiz.txt file using shelve module

		Arguments:
		number_of_quizes: int
		- number of quize

		quiz_questions_and_answers: dict
		- quiz questions and answers

	"""
	with shelve.open(f'{os.getcwd()}/quizes/quiz.txt', 'c') as quiz_file:
		quiz_file[f'quiz_{number_of_quizes}'] = quiz_questions_and_answers
		quiz_file.close()


def get_question():
	"""
	Returns entered question
	"""

	while True:
		question = input("Enter Question: ")

		if not question:
			print("Please Enter valid question. ")
		else:
			break

	return question


def get_answer():
	"""
	Returns entered answer.
	"""

	while True:
		answer = input("Enter Answer: ")

		if not answer:
			print("Please Enter valid Answer")
		else:
			break

	return answer


def get_questions_and_answers(number_of_questions):
	"""
	Return quiz questions after retreiving question and answer

	Arguments:
	number_of_questions: int

	Returns:
	quiz_questions: dict
	-  quiz questions and answers.

	"""

	quiz_questions = {}
	for _ in range(1, number_of_questions + 1):
		question, answer = get_question(), get_answer()
		quiz_questions[question] = answer

	return quiz_questions


def get_number_of_questions():
	"""
	Return number of quiz questions.

	"""
	return int(input("Number of questions for this quiz: "))


def creating_files_for_quiz_questions(number_of_quizes):
	"""
	This function get number of questions then get questions and answers after
	that it saves quiz questions in the specified file.

	Arguments:
	number_of_quizes: int
	 - Number of quizes

	"""

	number_of_questions = get_number_of_questions()

	quiz_questions_and_answers = get_questions_and_answers(number_of_questions)

	save_quiz_questions(number_of_quizes, quiz_questions_and_answers)


if __name__ == '__main__':

	# Number of quizes
	number_of_quizes = int(input("Enter number of quizes: "))

	creating_files_for_quiz_questions(number_of_quizes)
