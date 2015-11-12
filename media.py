class Movie:
	"""A structure for movies
	
	Attributes:
		title: A string of the movie title
		trailer_youtube_url: A string of the movie youtube trailer_url
		poster_image_url: A string of the movie poster image
		year: A string of the movie release year
	"""
	
	# Constructor for movie class 
	def __init__(self, title, trailer_url, poser_url, year):
		self.title = title
		self.poster_image_url = poser_url
		self.trailer_youtube_url = trailer_url
		self.year = year
