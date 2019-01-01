class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,image,publish_date,url):
        self.id =id
        self.title = title
        self.description = description
        self.image = 'https://image.tmdb.org/t/p/w500/'+ image
        self.publish_date = publish_date
        self.url = url