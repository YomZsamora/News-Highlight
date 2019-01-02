import unittest
from models import news
News = news.News


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_highlight = News('Uhuru signs law to clean up NYS','CS Kobia says embezzlement will become a thing of the past.','12/19/2018','https://www.nation.co.ke/news/Uhuru-signs-law-to-clean-up-NYS/1056-4916440-v39b0n/index.html','https://image.tmdb.org/t/p/w500/khsjha27hbs','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_highlight,News))


if __name__ == '__main__':
    unittest.main()