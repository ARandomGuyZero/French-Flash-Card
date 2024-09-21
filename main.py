"""
Quiz Game

Author: Alan
Date: August 4th 2024

This script simulates a quiz game.
Questions taken from Open Trivia DB.
The user answer either True or False and they get points for the final score.
This project uses data from the Open Trivia Database API:https://opentdb.com/api_config.php
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_interface import QuizInterface

question_bank = []

# Simple loop to create a question bank using data from question_data
for question in question_data:
    # Storing the question and answer on each item of the list
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Creating a new question that will use the Question
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating a new object QuizBrain which will do the quiz logic
quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface()

# Simple loop that will continue as long as there as unanswered questions
while quiz.still_has_questions():
    quiz.next_question()

# Congratulate user for finishing quest and show them score
print("You finished it!")
print(f"Your final score is {quiz.score}/{quiz.question_number}!")