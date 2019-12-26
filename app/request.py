from app import app
import datetime
import urllib.request,json
from .models import news,sources,entertainment

News = news.News
Sources = sources.Sources
Entertainment = entertainment.Entertainment

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
news_base_url = app.config["NEWS_HIGHLIGHTS_BASE_URL"]

# Getting the sources base url
sources_base_url = app.config["NEWS_SOURCE_BASE_URL"]

# Getting the entertainment news base url
entertainment_base_url = app.config["NEWS_ENTERTAINMENT_BASE_URL"]


def get_news(country):
	'''
	Function that gets the json response to our url request
	'''
	get_news_url = news_base_url.format(country,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['articles']:
			news_result_list = get_news_response['articles']
			news_results = process_newsResults(news_result_list)


	return news_results


def process_newsResults(news_list):
	'''
	Function that processes the news results and transforms them to a list of objects
	'''

	news_results = []
	for news_item in news_list:
		title = news_item.get('title')
		description = news_item.get('description')
		publishedAt = news_item.get('publishedAt')
		content = news_item.get('content')
		url = news_item.get('url')
		img_url = news_item.get('urlToImage')

		date_time_obj = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
		publishedAt = date_time_obj.date()

		if img_url:
			news_object = News(title,description,publishedAt,content,url,img_url)
			news_results.append(news_object)

	return news_results




def get_sources():
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = sources_base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_result_list = get_sources_response['sources']
			sources_results = process_sourcesResults(sources_result_list)


	return sources_results




def process_sourcesResults(sources_list):
	'''
	Function that processes the sources results and transforms them to a list of objects
	'''

	sources_results = []
	for source_item in sources_list:
		name = source_item.get('name')
		description = source_item.get('description')
		source_url = source_item.get('url')

		source_object = Sources(name,description,source_url)
		sources_results.append(source_object)

	return sources_results




def getEntertainmentNews(category):
	'''
	Function that processes the entertainment news results and transforms them to a list of objects
	'''

	get_entertainmentNews_url = entertainment_base_url.format(category,api_key)

	with urllib.request.urlopen(get_entertainmentNews_url) as url:
		get_entertainmentNews_data = url.read()
		get_entertainmentNews_response = json.loads(get_entertainmentNews_data)

		entertainmentNews_results = None

		if get_entertainmentNews_response['articles']:
			entertainmentNews_result_list = get_entertainmentNews_response['articles']
			entertainmentNews_results = process_EntertainmentNews_Results(entertainmentNews_result_list)


	return entertainmentNews_results




def process_EntertainmentNews_Results(entertainmentNews_result_list):
	'''
	Function that processes the sources results and transforms them to a list of objects
	'''
	idNumber = 1
	entertainmentNews_results = []
	for entertainment_item in entertainmentNews_result_list:
		name = entertainment_item.get('name')
		description = entertainment_item.get('description')
		publishedAt = entertainment_item.get('publishedAt')
		source_url = entertainment_item.get('url')

		date_time_obj = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
		publishedAt = date_time_obj.date()


		entertainmentNews_object = Entertainment(idNumber,name,description,publishedAt,source_url)
		entertainmentNews_results.append(entertainmentNews_object)
		idNumber=idNumber+1

	return entertainmentNews_results