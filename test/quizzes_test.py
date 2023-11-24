import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_add_quiz(self):
        """
        test_add_quiz
        Test for breaking the add_quiz function
        Failing on Line 63
        """
        self.ctrl.clear_data()
        quiz1ID = self.ctrl.add_quiz("Quiz1", "easy quiz", "2023-12-25", "2024-01-16")
        
        # check that we have one quiz in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz")

        # check that we can retrieve the added quiz
        quiz1 = self.ctrl.get_quiz_by_id(quiz1ID)
        self.assertIsNotNone(quiz1, "The quiz can be retrieved")

        # check that adding a quiz resulting in a None ID crashes the program
        quiz2ID = self.ctrl.add_quiz(None, "test", None, None)
        self.assertIsNone(quiz2ID, 'None quiz ID, quiz_controller.py, Line 63')
        
    def test_add_quiz_date(self):
       """
       test_add_quiz_date
       Dates should be validated prior to Line 64 of quizzes_controller.py
       """
       self.ctrl.clear_data()
       # add quiz with valid due date
       _ = self.ctrl.add_quiz("Quiz1", "Functions", "2023-11-23", "2024-06-13")
       quizzes = self.ctrl.get_quizzes()
       self.assertEquals(len(quizzes), 1, "quiz was added successfully")
       # add quiz with an invalid due date (due date is 23 years before available date and is referring to a non-existent 13th month)
       quiz2 = self.ctrl.add_quiz("Quiz2", "Maps", "01-01-2023", "13-13-2000")
       _ = self.ctrl.add_question(quiz2, "Will this work?", "This is adding a question to a quiz with an invalid due date.")
       self.assertEquals(len(quizzes), 1, "Quiz with invalid due date should not be added.")
        
    def test_load_data(self):
       """
       test_load_data
       Loading a json file with bad data.
       Giving an invalid JSON file while calling the load_data method will cause an error in line 17 load_data of quizzes_controller.py
       return json.load(fin)
       The error goes way further until this happens:
       json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
       """
       # Create quizzes controller
       quiz1 = QuizzesController('quizzes_test.py')
       # assert quiz1 is of class QuizzesController
       self.assertIsInstance(quiz1, QuizzesController, "Quiz1 is not an instance of QuizzesController")

       # Create quizzes controller with bad data
       quiz2 = QuizzesController("bad_data.json")
       # assert quiz2 is of class QuizzesController
       self.assertIsInstance(quiz2, QuizzesController, "Quiz2 is not an instance of QuizzesController")

if __name__ == '__main__':
    unittest.main()