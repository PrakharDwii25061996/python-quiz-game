import random
from quizes import quiz_1


def get_random_three_values(asking_questions):
	return random.sample(list(asking_questions.values()), 3)


def print_options_list(option_list):
	for option in option_list:
		print(f"""{option_list.index(option)}. {option}""")


def print_user_quiz_score_dashboard(score, wrong_answers, right_answers, total_questions):
	print(f"""
		Total Questions: {total_questions}
		Wrong Answers: {wrong_answers}
		Corrent Answers: {right_answers}
		Total Score: {score}
	""")


if __name__ == '__main__':
	asking_questions = quiz_1.questions
	score, wrong_answers, right_answers, total_questions = 0, 0, 0, len(asking_questions)
	print(f"Below are the {total_questions} questions. Each questions consist of 2 marks: ")

	for key, value in asking_questions.items():
		three_option_list = get_random_three_values(asking_questions)
		three_option_list.append(value)
		three_option_list = list(dict.fromkeys(three_option_list))
		option_list = random.sample(three_option_list, len(three_option_list))

		print(f"""\nQuestion : What is the capital of {key}?""")

		print_options_list(option_list)

		answer_index_value = input("Answer: ")

		if answer_index_value.lower() == value.lower():
			right_answers += 1
			score += 2
		else:
			wrong_answers += 1

	print_user_quiz_score_dashboard(score, wrong_answers, right_answers, total_questions)
