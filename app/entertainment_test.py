import unittest
from models import entertainment
Entertainment = entertainment.Entertainment

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.entertainment_news = Entertainment(1,'Axios','Axios are a new media company delivering vital, trustworthy news and analysis in the most efficient, illuminating and shareable ways possible.','12-12-18','https://www.axios.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.entertainment_news,Entertainment))


if __name__ == '__main__':
    unittest.main()