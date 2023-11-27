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
        self.ctrl.clear_data()
        quiz_controller = QuizzesController()
        """This case causes a crash when we add a integer as a title for a quiz instead of a String"""
        """It will cause a crash on line 63 in quizzes_controller.py"""
        final_result = quiz_controller.add_quiz(4, "Sample Quiz" ,datetime.now(),due_date=datetime.now() + timedelta(hours=1 , minutes=50))
        quizzes = self.ctrl.get_quizzes()
        self.assertEqual(len(quizzes), 0, "Unexpected quiz added to the list")

    
    def test_expose_failure_02(self):
        """This case causes a crash when we add a boolean as a title for a quiz instead of a String"""
        """It will cause a crash on line 63 in quizzes_controller.py"""
        self.ctrl.clear_data()
        quiz_controller = QuizzesController()
        
        final_result = quiz_controller.add_quiz(True, "Sample Quiz" ,datetime.now(),due_date=datetime.now() + timedelta(hours=1 , minutes=50))
        quizzes = self.ctrl.get_quizzes()
        self.assertEqual(len(quizzes), 0, "Unexpected quiz added to the list")

    
    def test_exposure_failure_03(self):
        """This case causes a crash when we successfully add a question and compare it with None"""
        """It will cause a crash on line 63 in quizzes_controller.py"""
        self.ctrl.clear_data()
        quiz_controller = QuizzesController()

        quiz_id = quiz_controller.add_quiz("Computer Science Quiz", "Test your Computer Science Knowledge", datetime.now(), datetime.now() + timedelta(days=7))
        final_result = quiz_controller.add_question(quiz_id, "Comp Scie Question", "Test your comp sci knowledge")
        added_question = quiz_controller.get_question_by_id(final_result)

        # Check that the question was added successfully
        self.assertIsNone(added_question, "Question was not added successfully")    


if __name__ == '__main__':
    unittest.main()