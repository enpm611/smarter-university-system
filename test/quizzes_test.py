import unittest
from app.controllers.quizzes_controller import QuizzesController
from datetime import datetime
from unittest.mock import patch
from app.model.assignments import Quiz
from datetime import datetime, timedelta
import os 

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Point to a test file to avoid using production data.
        self.ctrl = QuizzesController('test_assignments.json')

    def test_expose_failure_01(self):
        """
        This test checks whether the system can handle text encoding issues gracefully.
        It attempts to create a new quiz and add a question with a title that has
        characters not supported by the standard UTF-8 encoding.
        An encoding error is expected to originate from utils.py and surface in quizzes_controller.py, line 78
        """
        # Define a title with characters outside the typical UTF-8 range
        problematic_title = '\ud861\udd37'

        # Ensure the quizzes list is empty before starting the test
        self.ctrl.clear_data()

        # Add a new quiz and verify that it has been added
        new_quiz_id = self.ctrl.add_quiz("Introduction to Encoding", "Exploring edge cases with encodings.", "2023-11-07T00:00:00Z", "2023-11-14T00:00:00Z")
        self.assertEqual(1, len(self.ctrl.get_quizzes()), "A single quiz should be present after addition.")

        # Attempt to add a question with a problematic title and check for successful addition
        new_question_id = self.ctrl.add_question(new_quiz_id, problematic_title, "What is the standard encoding for web content?")
        self.assertIsNotNone(new_question_id, "Question addition should fail due to encoding issue.")


    def test_expose_failure_02(self):
        """
        Tests if the application fails to handle an addition of a question correctly, which should not occur.
        A failure is expected due to the code at line 63 in quizzes_controller.py not being robust against None comparisons.
        """
        self.ctrl.clear_data()  # Ensuring a clean slate for the test.
        quiz_mgr = QuizzesController()  # Instantiate a new quiz manager.

        # Trying to create a new quiz and then a related question.
        new_quiz_id = quiz_mgr.add_quiz("CS Fundamentals", "Assess your knowledge in Computer Science.", datetime.now(), datetime.now() + timedelta(weeks=1))
        question_creation_result = quiz_mgr.add_question(new_quiz_id, "CS Basics", "How well do you understand the basics?")
        
        # Verifying if the question exists, which it should not.
        newly_added_question = quiz_mgr.get_question_by_id(question_creation_result)
        self.assertIsNone(newly_added_question, "The question should not exist as it was not added properly.")

    def test_expose_failure_03(self):
        """
        Test case for crashing the application by manipulating the quiz list to include a None value.
        Expected to crash at quizzes_controller.py on line 117 when attempting to iterate over quizzes
        in a function that assumes all elements are valid Quiz objects.
        """
        self.ctrl.quizzes.append(None)  # Manually append a None value to the quizzes list

        # Assert that None is actually in the quizzes list
        self.assertIn(None, self.ctrl.quizzes, "The quizzes list should contain a None value.")

        # Then, attempt to print a quiz, which should iterate over the quizzes list and may crash
        # No try-except block here; let the test framework catch the unhandled exception
        self.ctrl.print_quiz("dummy_id")

    def tearDown(self):
        # Clean up by removing the test file if it exists.
        try:
            os.remove('test_assignments.json')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
