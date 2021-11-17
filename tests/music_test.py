import unittest
from app.models import Music


class MusicTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Music class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_music = Music(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_music,Music))


if __name__ == '__main__':
    unittest.main()
