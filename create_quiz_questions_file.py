import random
import pprint
import os

def create_a_quiz_file(quiz):
	file = open(f'{os.getcwd()}/quizes/quiz_{quiz}.py', 'x')
	file.close()

def creating_files_for_quiz_questions(quiz):
	create_a_quiz_file(quiz)

	countries_capital = {}
	number_of_questions = int(input("Number of questions for this quiz: "))

	for ques in range(1, number_of_questions + 1):
		question = input("Question: ")
		answer = input("Answer: ")
		countries_capital[question] = answer

	file = open(f'{os.getcwd()}/quizes/quiz_{quiz}.py', 'a')
	file.write(f'questions = {countries_capital}')
	file.close()


if __name__ == '__main__':

	number_of_quizes = int(input("Enter number of quizes: "))

	for quiz in range(1, number_of_quizes + 1):
		creating_files_for_quiz_questions(quiz)

	# bla bla bla