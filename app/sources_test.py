import unittest
from models import sources
Sources = sources.Sources

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Axios','Axios are a new media company delivering vital, trustworthy news and analysis in the most efficient, illuminating and shareable ways possible.','https://www.axios.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()