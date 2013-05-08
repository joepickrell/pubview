from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Journal(models.Model):
	# journals have names, ...?
	# linked to papers via Paper model

        name = models.CharField(max_length=1000)

	#
	# functions
	#
	def __unicode__(self):
		return self.name

	
class Paper(models.Model):
	# paper is collection of PaperVersions
	# need to keep title, year, abstract
	# linked to authors via Author

        title = models.CharField(max_length=1000)
        journal = models.ForeignKey(Journal)
        year = models.IntegerField()
	abstract = models.CharField(max_length = 100000)
	volume = models.IntegerField(default = -1)
	number = models.IntegerField(default = -1)
	startpage = models.IntegerField(default =-1)
	endpage = models.IntegerField(default = -1)
	#
	# functions
	#
	def __unicode__(self):
		return self.title
	#
	# get the authors
	#
	def get_authors(self):
		toreturn = []
		for a in self.author_set.all():
			toreturn.append(a.__unicode__())
		return ", ".join(toreturn)

class PaperVersion(models.Model):
	# need to be able to keep multiple versions of papers, e.g. arXiv version, published version
	# maybe don't need to keep the title here?
	# keep all the other meta-info? (e.g. volume, number, etc)
        paper = models.ForeignKey(Paper)
        journal = models.ForeignKey(Journal)
        year = models.IntegerField()
        title = models.CharField(max_length=1000)
	
	#
	# functions
	#
	def __unicode__(self):
		return self.title

class Author(models.Model):
	# authors linked to paper and coauthors

	firstname = models.CharField(max_length=500)
	lastname = models.CharField(max_length=500)
	papers = models.ManyToManyField(Paper)
	coauthors = models.ManyToManyField('self')
	#
	# functions
	#
	def __unicode__(self):
		toreturn = " ".join([self.firstname, self.lastname])
		return toreturn



class Account(models.Model):
	#
	# account can upvote/downvote
	#
	user = models.OneToOneField(User)
	votes = models.ManyToManyField(Paper, through='Vote')
	def __unicode__(self):
		return self.user.__unicode__()
        def alreadyvoted(self, pid):
		# has this account voted on this paper?
		v = self.votes.filter(pk = pid)
		if len(v) < 1:
			return False
		else:
			return True		

class Vote(models.Model):
        VOTE_TYPES = (
                ('U', 'Up'),
                ('D', 'Down'),
        )
        account = models.ForeignKey(Account)
        paper = models.ForeignKey(Paper)
        votetype = models.CharField(max_length = 2, choices = VOTE_TYPES)
	
