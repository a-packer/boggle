from unittest import TestCase
from app import app
from boggle import Boggle
from flask import session


class BoggleTestCase(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_home(self):
        """Make sure home is showing the high score and number of plays"""

        with self.client as client:

            res = self.client.get('/')
            html = res.get_data(as_text=True)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boggle Game!</h1>', html)
            self.assertIn('board', session)


    def test_valid_word(self):
        """Test if word is valid (in dictionary and on board) by modifying the board in the session"""

        with self.client as client:

            with client.session_transaction() as sess:
                sess['board'] = [["H", "A", "P", "P", "Y"], 
                                 ["A", "A", "T", "T", "T"], 
                                 ["P", "A", "P", "T", "T"], 
                                 ["P", "A", "T", "P", "A"], 
                                 ["Y", "A", "T", "T", "Y"]
                                 ]

        res = self.client.get('/check-word?word=happy')
        self.assertEqual(res.json['result'], 'ok')


    def test_invalid_word(self):
        """Test for word in dictionary but not on board"""

        with self.client as client:

            with client.session_transaction() as sess:
                sess['board'] = [["H", "A", "P", "P", "Y"], 
                                 ["A", "A", "T", "T", "T"], 
                                 ["P", "A", "P", "T", "T"], 
                                 ["P", "A", "T", "P", "A"], 
                                 ["Y", "A", "T", "T", "Y"]
                                 ]

            res = self.client.get('/check-word?word=impossible')
            self.assertEqual(res.json['result'], 'not-on-board')

    def not_valid_word(self):
        """Test for word not in dictionary"""

        with self.client as client:
            
                self.client.get('/')
                response = self.client.get('/check-word?word=ppy')
                self.assertEqual(response.json['result'], 'not-word')

    

        