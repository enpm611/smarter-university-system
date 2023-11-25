import unittest

from app.controllers.quizzes_controller import QuizzesController


class QuizzesTest(unittest.TestCase):
    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController("quizzes_test.py")

    def test_expose_failure_01(self):
        """
        Loads a json file with bad data.

        Since the load_data method assumes
        the JSON data is valid, it doesn't try
        to catch any errors when loading it.

        We can just simply make an invalid JSON file
        pass it into the function then.

        This is where the error occurs:
        File "/home/marc/Documents/enpm611/smarter-university-system/app/utils/data_loader.py", line 13, in load_data
        return json.load(fin)

        The error goes way further until this happens:
        json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
        """
        _ = QuizzesController("bad_data.json")
        assert _ is QuizzesController

    def test_expose_failure_02(self):
        """
        Another failed load, this time with JSON where there isn't a title key
        The load method doesn't check if title is a valid key when making a Quiz.

        File "/home/marc/Documents/enpm611/smarter-university-system/app/controllers/quizzes_controller.py", line 37, in _load_data
        quiz = Quiz.from_params(qobj['title'],qobj['text'],last_updated,available_date,due_date,id=qobj['id'])
                            ~~~~^^^^^^^^^
        KeyError: 'title'
        """
        _ = QuizzesController("bad_data2.json")
        assert _ is QuizzesController

    def test_expose_failure_03(self):
        """
        A third failed load, except this is in the section loop where it errors.
        The load method doesn't check if title is a valid key when making a Question

        File "/home/marc/Documents/enpm611/smarter-university-system/app/controllers/quizzes_controller.py", line 40, in _load_data
        question = Question.from_params(sobj['title'], sobj['text'],qst_last_updated,id=sobj['id'])
                                    ~~~~^^^^^^^^^
        KeyError: 'title'
        """
        _ = QuizzesController("bad_data3.json")
        assert _ is QuizzesController


if __name__ == "__main__":
    unittest.main()
