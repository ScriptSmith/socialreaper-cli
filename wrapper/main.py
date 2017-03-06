import socialreaper
from os import environ

def iter(gen):
	result = []

	for item in gen:
		print(item)
		result.append(item)

	socialreaper.tools.to_csv(result)

class Facebook():
	def __init__(self, api_key):
		self.source = socialreaper.Facebook(api_key)

	def posts(self, *args, **kwargs):
		iter(self.source.posts(*args, **kwargs))

	def post_comments(self, *args, **kwargs):
		iter(self.source.post_comments(*args, **kwargs))

	def page_posts(self, *args, **kwargs):
		iter(self.source.page_posts(*args, **kwargs))

	def page_posts_comments(self, *args, **kwargs):
		iter(self.source.page_posts_comments(*args, **kwargs))

class Twitter():
	def __init__(self, app_key=None, app_secret=None, oauth_token=None, oauth_token_secret=None, *args, **kwargs):
		if not args and not kwargs:
			app_key = environ['twitter_app_key']
			app_secret = environ['twitter_app_secret']
			oauth_token = environ['twitter_oauth_token']
			oauth_token_secret = environ['twitter_oauth_token_secret']

		self.source = socialreaper.Twitter(app_key, app_secret, oauth_token, oauth_token_secret)

	def search(self, *args, **kwargs):
		iter(self.source.search(*args, *kwargs))

	def hashtag(self, *args, **kwargs):
		iter(self.source.hashtag(*args, *kwargs))

	def user(self, *args, **kwargs):
		iter(self.source.user(*args, *kwargs))


class Reddit():
	def __init__(self, application_id=None, application_secret=None, *args, **kwargs):
		if not args and not kwargs:
			application_id = environ['reddit_application_id']
			application_secret = environ['reddit_application_secret']

		self.source = socialreaper.Reddit(application_id, application_secret)

	def search(self, *args, **kwargs):
		iter(self.source.search(*args, **kwargs))

	def subreddit(self, *args, **kwargs):
		iter(self.source.subreddit(*args, **kwargs))

	def user(self, *args, **kwargs):
		iter(self.source.user(*args, **kwargs))

	def threads(self, *args, **kwargs):
		iter(self.source.threads(*args, **kwargs))

	def thread_comments(self, *args, **kwargs):
		iter(self.source.thread_comments(*args, **kwargs))

	def search_thread_comments(self, *args, **kwargs):
		iter(self.source.search_thread_comments(*args, **kwargs))

	def subreddit_thread_comments(self, *args, **kwargs):
		iter(self.source.subreddit_thread_comments(*args, **kwargs))


class Youtube():
	def __init__(self, api_key=None, *args, **kwargs):
		if not args and not kwargs:
			api_key = environ['youtube_api_key']

		self.source = socialreaper.Youtube(api_key)

	def videos(self, *args, **kwargs):
		iter(self.source.videos(*args, **kwargs))

	def search(self, *args, **kwargs):
		iter(self.source.search(*args, **kwargs))

	def channel(self, *args, **kwargs):
		iter(self.source.channel(*args, **kwargs))

	def video_comments(self, *args, **kwargs):
		iter(self.source.video_comments(*args, **kwargs))

	def search_video_comments(self, *args, **kwargs):
		iter(self.source.search_video_comments(*args, **kwargs))

	def channel_video_comments(self, *args, **kwargs):
		iter(self.source.channel_video_comments(*args, **kwargs))

	def guess_channel_id(self, *args, **kwargs):
		iter(self.source.guess_channel_id(*args, **kwargs))

