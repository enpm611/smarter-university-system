import unittest

from app.controllers.quizzes_controller import QuizzesController
from datetime import datetime

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController()
        
    def test_expose_failure_01(self):
        """
        This function demonstrates a lack of error checking in the add
        quiz function of the QuizController module. Notice how using an
        integer instead of a string for the title induces a TypeError on
        line 63 of quizzes_controller.py
        """
        q_id = self.ctrl.add_quiz(0, "<-- bad id", datetime(2001, 1, 24), datetime(2003, 7, 13))
        self.assertEqual(
            q_id,
            None,
            'The new id should not have been created!'
        )
        
    def test_expose_failure_02(self):
        """
        This function demonstrates a lack of error checking in the _save_data
        function of the QuizzesController module. Adding "None" into the list
        of quizzes before trying to add another quiz will result in an
        AttributeError on line 54 of quizzes_controller.py

        We assert that the id returned when adding a quiz object to the controller
        should be the same id of the quiz object returned when querying the
        get_quiz_by_id function for that ID
        """
        self.ctrl.quizzes.append(None)
        q_id = self.ctrl.add_quiz("Good Title", "Good Text", datetime(2001, 1, 24), datetime(2003, 7, 13))
        quiz = self.ctrl.get_quiz_by_id(q_id)
        self.assertEqual(
            quiz.id,
            q_id,
            'The newly created quiz ID should match the ID of the queried quiz!'
        )
    
    def test_expose_failure_03(self):
        """
        This function demonstrates a lack of error checking in the _load_data
        function of the QuizController module. Notice how using an integer
        instead of a string for the title induces a TypeError on line 63 of
        quizzes_controller.py

        We assert that in the event of a failure to read data from a file,
        None should be returned
        """
        self.ctrl.file_name = 'discussions_test.json'
        quizzes = self.ctrl._load_data()
        self.assertEqual(
            quizzes,
            None,
            'Quizzes should have failed to read from a poorly structured JSON!'
        )
    
if __name__ == '__main__':
    unittest.main()