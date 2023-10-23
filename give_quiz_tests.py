import random
# from quizes import quiz_1
import shelve
import os


def get_random_three_values(quiz_questions):
	return random.sample(list(quiz_questions.values()), 3)


def print_options_list(choices):

	for option in choices:
		print(f"""{choices.index(option)}. {option}""")


def print_user_quiz_score_dashboard(score_card):
	print(f"""
		Total Questions: {score_card['total_questions']}
		Wrong Answers: {score_card['wrong_answers']}
		Corrent Answers: {score_card['right_answers']}
		Total Score: {score_card['score']}
	""")


def get_quiz_to_play():

	with shelve.open(f'{os.getcwd()}/quizes/quiz.txt', 'c') as quiz_file:

		for quiz in quiz_file.keys():
			print(quiz)

		quiz = input("Which quiz you want to play? ")

		quiz_questions = quiz_file[quiz]
		quiz_file.close()

	return quiz_questions


def get_score_card_according_to_correct_answers(entered_answer, answer, total_questions):
	score_card = {
		'score': 0,
		'wrong_answers': 0,
		'right_answers': 0,
		'total_questions': total_questions
	}

	if entered_answer.lower() == answer.lower():
		score_card['right_answers'] += 1
		score_card['score'] += 2
	else:
		score_card['wrong_answers'] += 1

	return score_card


def get_choices(quiz_questions, answer):

	three_option_list = get_random_three_values(quiz_questions)
	three_option_list.append(answer)
	three_option_list = list(dict.fromkeys(three_option_list))
	option_list = random.sample(three_option_list, len(three_option_list))

	return option_list


def get_entered_answer(question, choices):
	print(f"""\n{question}""")
	print_options_list(choices)

	while True:
		entered_answer = input("Answer: ")

		if not entered_answer:
			print("Please Enter valid answer. ")
		else:
			break

	return entered_answer


if __name__ == '__main__':

	quiz_questions = get_quiz_to_play()
	total_questions = len(quiz_questions)
	
	print(f"Below are the {total_questions} questions. Each questions consist of 2 marks: ")

	for question, answer in quiz_questions.items():
		
		choices = get_choices(quiz_questions, answer)

		entered_answer = get_entered_answer(question, choices)

		score_card = get_score_card_according_to_correct_answers(
			entered_answer,
			answer,
			total_questions
		)

	print_user_quiz_score_dashboard(score_card)
