# News Highlight

An application that lists news articles from various sources and helps the busy people to keep up with the current affairs.

[![news.png](https://i.postimg.cc/dVt6sJPc/news.png)](https://postimg.cc/w7ZLF8jw)

## Description
This application is developed to help a user to go through everyday's highlights. User can follow the link to the source in case he/she wants to read the full article about any news. User can see the image, description and the time a news article was created. User can select a news source from various news sources and can read all the news articles from that particular source.

## Specifications

### Behaviour Driven Development:

1. display an option to select a news source
   - INPUT:"Select a news source"
   - OUTPUT:"A page displaying all the news articles from that news source" 
2. displays a link to see full article of a news on the source website
   - INPUT:"source link clicked"
   - OUTPUT:"A page on the source website displaying full article on that news"


## Technologies Used

- Python 3.6
- Flask Framework
- Pip
- HTML & CSS(Bootstrap)

## Setup/Installation Requirements
   * To run the application, in your terminal:

    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements.
    4. Edit the start.sh file with your api key from the news.org website
    6. Run chmod a+x start.sh
    7. Run ./start.sh
    8. Access the application through `localhost:5000`

	
### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

## Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/yomZsamora/News-Highlight/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/yomZsamora/News-Highlight/issues/new). Please include sample queries and their corresponding results.


### License

*MIT*
Copyright (c) 2019 **Yommie Samora**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
