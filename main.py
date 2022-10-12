from questions import answer_questions
from generator import generate_project


if __name__ == '__main__':
    answers = answer_questions()
    generate_project(answers)
