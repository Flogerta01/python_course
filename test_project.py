import pytest
from unittest.mock import patch
import requests
from io import StringIO
from project import  get_questions,get_valid_difficulty,get_valid_amount,quiz


def main():
    test_get_questions_api_error()
    test_get_valid_amount_valid_input()
    test_get_valid_difficulty_valid_input()
    test_quiz()


def test_get_questions_api_error():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        questions = get_questions(2)
        assert questions is None

def test_get_valid_amount_valid_input():
    # Mocking input to return a valid number
    with patch('builtins.input', side_effect=['5']):
        result = get_valid_amount()
        assert result == 5

def test_get_valid_difficulty_valid_input():
    with patch('builtins.input', side_effect=['easy']):
        result = get_valid_difficulty()
        assert result == 'easy'

    with patch('builtins.input', side_effect=['medium']):
        result = get_valid_difficulty()
        assert result == 'medium'

    with patch('builtins.input', side_effect=['hard']):
        result = get_valid_difficulty()
        assert result == 'hard'

def test_quiz():
    questions = [
        {"question": "Is Python a programming language?", "correct_answer": "True"},
        {"question": "Is the Earth flat?", "correct_answer": "False"},
    ]
    with patch('builtins.input', side_effect=['True', 'False']):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            quiz(questions)
            output = fake_stdout.getvalue()


if __name__ == "__main__":
    main()
