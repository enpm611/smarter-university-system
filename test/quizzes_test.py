from datetime import datetime, timedelta
import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        quiz_controller = QuizzesController()
        # Pass integer valued title instead of string - this causes the program to crash with a TypeError: unsupported operand type(s) for +: 'int' and 'str'
        # Alternatively, if we Pass None title instead of string - the program crashes with another 
        # TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

        # The program crashes at File "/smarter-university-system/app/controllers/quizzes_controller.py", line 63, in add_quiz as follows
        result = quiz_controller.add_quiz(1, "Sample Text", datetime.now(), due_date=datetime.now() + timedelta(hours=0, minutes=50))
        self.assertIsNone(result, "Expected result to be None")
    
    def test_expose_failure_02(self):
        quiz_controller = QuizzesController()
        quiz_id = quiz_controller.add_quiz("Test Quiz", "Sample Text", datetime(2023, 2, 15, 12, 30, 0), datetime(2023, 12, 15, 12, 30, 0))
        question_id = quiz_controller.add_question(quiz_id, "Test Question", "sample text")
        # Pass a string instead of a boolean for is_correct - this causes an AssertionError: 
        # 'dbac66b82d475c3ae04064efe1d78547' is not None : answer_id should not be generated

        # The program crashes at File "/smarter-university-system/test/quizzes_test.py", line 42 in add_question as follows
        answer_id = quiz_controller.add_answer(question_id, "Test Answer", "passing string instead of the expected boolean datatype")
        self.assertIsNone(answer_id, "answer_id should not be generated")

    def test_expose_failure_03(self):
        quiz_controller = QuizzesController()
        # Pass title that has a timestamp in it - this causes the program to crash with a TypeError: Object of type datetime is not JSON serializable
        # Additionally, this also corrupts the assignments.json file by attempting to add partial data
        
        # The program crashes at File "/smarter-university-system/app/controllers/quizzes_controller.py", line 81, in add_question: self._save_data()
        quiz_id = quiz_controller.add_quiz("Test Quiz", "Sample Text", datetime.now(), due_date=datetime.now() + timedelta(hours=0, minutes=50))
        res = quiz_controller.add_question(quiz_id, datetime.now(), "sample text")
        self.assertIsNone(res, "Expected result to be None")


if __name__ == '__main__':
    unittest.main()
