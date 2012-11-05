from django.db import models
import datetime

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=5000)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=1)

	def __unicode__(self):
		return self.title

	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()

	def was_published_this_year(self):
		return self.pub_date.date().year == datetime.date.today().year

	def was_published_this_month(self):
		return was_published_this_year and self.pub_date.date().month == datetime.date.today().month 

	was_published_today.short_description = "Published today?"
	was_published_this_month.short_description = "Published this month?"
	was_published_this_year.short_description = "Published this year?"

class Comment(models.Model):
	content = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	parent = models.ForeignKey(Post)

	def __unicode__(self):
		return self.content