import unittest

from app.controllers.quizzes_controller import QuizzesController


class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')

    # test exposes the issue where the '+' operation fails due to operands being NoneType and 'str'.
    def test_expose_failure_01(self):
        # clear previosuly generated data
        self.ctrl.clear_data()

        # Generates exception in quizzes_controller.py at Line 63
        self.ctrl.add_quiz(None, None, None, None)

    # test exposes the issue of using utf-8 without normalising the string which enables safe utf-8 conversion.
    def test_expose_failure_02(self):
        # clear previosuly generated data
        self.ctrl.clear_data()

        quiz_id = self.ctrl.add_quiz("A", "B", 1, 1)
        # Generates exception in utils.py at Line 11, initiating from quizzes_controller at Line 78
        self.ctrl.add_question(quiz_id, '\udbff\udfff', "D")

    # test exposes the issue of accepting values that cannot be serialised via a JSON Encoder.
    def test_expose_failure_03(self):
        # clear previosuly generated data
        self.ctrl.clear_data()

        quiz_id = self.ctrl.add_quiz("A", "B", 1, 1)
        # Generates exception in data_loader.py at Line 21, initiating from quizzes_controller at Line 78
        self.ctrl.add_question(quiz_id, b"some binary string", "D")


if __name__ == '__main__':
    unittest.main()
