import unittest
import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('assignments.json')
    
    def test_expose_failure_01(self):#Maggie's code
 
        """
        Test use of integer 1 instead of boolean value in add_answer
        """
        self.ctrl.clear_data()

        #Check add files a sample quiz and receive its ID 
        test_quiz_id = self.ctrl.add_quiz('quiz 1','True or false?',datetime(2020, 5, 18),datetime(2020, 5, 19))
        
        # Add question
        self.ctrl.add_question(test_quiz_id, "Question 1", "The sky is blue")
        # quiz_id:str, title:str, text:str

        # Add answer
        self.ctrl.add_answer(test_quiz_id, "true", 1)
        # question_id:str, text:str, is_correct:bool

        """ 
        File "/Users/maggietrimpin/Documents/repos/smarter-university-system/app/controllers/quizzes_controller.py", line 19, in __init__
            self.quizzes:List[Quiz] = self._load_data()
                              ^^^^^^^^^^^^^^^^^
        File "/Users/maggietrimpin/Documents/repos/smarter-university-system/app/controllers/quizzes_controller.py", line 27, in _load_data
            for qobj in load_data(self.file_name):
        """
        self.assertIsNotNone(test_quiz_id, "The quiz can be retrieved.")
        #self.ctrl.clear_data()    

    
    def test_expose_failure_02(self):#Joshua and Shwe's code
        """  
        Fails to create a quiz, since the title parameter is None, expecting a string 
        """
        
        #Deletes contents in assignment.json
        self.ctrl.clear_data()

        #Add a sample quiz to assignment.json files  
        test_quiz_id = self.ctrl.add_quiz(None,"Math quiz 1",datetime.datetime(2020, 5, 17),datetime.datetime(2020, 5, 18))
        
        """
        File "/home/arup/Documents/Enpm611/smarter-university-system-maggie_branch/app/controllers/quizzes_controller.py", line 63
        """
        # Try to retrieve recently incorrectly created quiz 
        self.assertIsNotNone(test_quiz_id , "The test answer should not be retrievable")
        
        #Deletes contents in assignment.json
        self.ctrl.clear_data()

def test_expose_failure_03(self):#Harsh's unit test
        self.ctrl.clear_data()

        # add quiz 
        quiz_id = self.ctrl.add_quiz("New quiz","New quiz",datetime.datetime.now(),datetime.datetime.now()+ datetime.timedelta(minutes=75))
        # quiz added successfully
        
        # add question
        question_id = self.ctrl.add_question(quiz_id,datetime.datetime.now(),"quiz question")
        # Here it will cause an error as datetime object has been passed to function which requires a string. This will cause the function to crash

        # Failing at 
        """
        File "d:\Fall 23\Software Engineering\smarter-university-system\app\controllers\quizzes_controller.py", line 81, in add_question
        self._save_data()
        ---
        File "d:\Fall 23\Software Engineering\smarter-university-system\app\controllers\quizzes_controller.py", line 55, in _save_data
        save_data(self.file_name,json_data)
        """
        # get question by id
        question = self.ctrl.get_question_by_id(question_id)

        self.assertIsNotNone(question,"Question")
     
if __name__ == '__main__':
    unittest.main()
