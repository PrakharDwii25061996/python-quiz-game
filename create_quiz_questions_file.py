import random
import pprint
import shelve
import os


def save_quiz_questions(quiz, quiz_questions):
	with shelve.open(f'{os.getcwd()}/quizes/quiz.txt', 'c') as quiz_file:
		quiz_file[f'quiz_{quiz}'] = quiz_questions
		quiz_file.close()


def get_question():

	while True:
		question = input("Enter Question: ")

		if not question:
			print("Please Enter valid question. ")
		else:
			break

	return question


def get_answer():

	while True:
		answer = input("Enter Answer: ")

		if not answer:
			print("Please Enter valid Answer")
		else:
			break

	return answer


def get_questions_and_answers(number_of_questions):

	quiz_questions = {}
	for ques in range(1, number_of_questions + 1):
		question, answer = get_question(), get_answer()
		quiz_questions[question] = answer

	return quiz_questions


def get_number_of_questions():
	return int(input("Number of questions for this quiz: "))


def creating_files_for_quiz_questions(quiz):

	number_of_questions = get_number_of_questions()

	quiz_questions = get_questions_and_answers(number_of_questions)

	save_quiz_questions(quiz, quiz_questions)


if __name__ == '__main__':

	number_of_quiz = int(input("Enter number of quizes: "))

	creating_files_for_quiz_questions(number_of_quiz)
