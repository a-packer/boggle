from unittest import TestCase
from app import app
from boggle import Boggle
from flask import session


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client:
            res = self.client.get('/')
            html = response.data
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boggle Game!</h1>', html)
            self.assertIn('board', session)

# class BoggleTestCase(TestCase):
    
#     def test_home(self):
#         """make sure home_page and session has expected info"""
#         with app.test_client() as client:
#             res = client.get('/')
#             html = res.get_data(as_text=True)

#             self.assertEqual(res.status_code, 200)
#             self.assertIn('<h1>Boggle Game!</h1>', html)
#             self.assertIn('board', session)


#     def test_play_count(self):
#         """check number of plays tracking"""
#         with app.test_client() as client:
#             res = client.get('/')
#             self.assertEqual(res.status_code, 200)
#             self.assertIsNone(session.get('nplays'))
    

#     def test_valid_word(self):
#         with app.test_client() as client:
#             with client.session_transaction as game_session:
#                 game_session['board'] = [
#                     ['B', 'A', 'T', 'D', 'E'],
#                     ['A', 'B', 'C', 'D', 'E'],
#                     ['T', 'B', 'A', 'D', 'E'],
#                     ['A', 'B', 'C', 'T', 'E'],
#                     ['A', 'B', 'C', 'D', 'E']
#                 ]
#             response = app.client.get('/check-word?word=cat')
#             app.assertEqual(response.json['result'], 'ok')


#     def test_invalid_word(self):
#         """Test if word is in the dictionary"""

#         app.client.get('/')
#         response = app.client.get('/check-word?word=impossible')
#         app.assertEqual(response.json['result'], 'not-on-board')

    

        