#!/usr/bin/python

import sys, os

from pubview.models import Author, Paper, Journal, PaperVersion, Account, Vote
from django.contrib.auth.models import User

#Clear the whole database
Author.objects.all().delete()
Paper.objects.all().delete()
Journal.objects.all().delete()
PaperVersion.objects.all().delete()
Account.objects.all().delete()


#u = User.objects.create_user('johndoe', 'john@doe.com', 'johnpassword')
#u.save()
u = User.objects.filter(username__startswith='john')[0]
a = Account(user = u)
a.save()
#u = Account.objects.filter(user__username__startswith='john')

a1 = Author(firstname ="Joseph", lastname = "Pickrell")
a2 = Author(firstname="Jonathan", lastname="Pritchard")
a1.save()
a2.save()
j = Journal(name = "Fake Journal")
j.save()
j2 = Journal(name = "arXiv q-bio")
j2.save()


p1 = Paper(title = "Awesome Paper 1", journal =j, year = 2011, abstract = "This is a paper about stuff. We show stuff.")
p1.save()

p2 = Paper(title = "Awesome Paper 2", journal =j, year = 2011, abstract = "Genomics!")
p2.save()
pv2 = PaperVersion(title = "Awesome Paper 2", journal =j, year = 2011, paper = p2)
pv2 = PaperVersion(title = "Awesome Paper 2", journal =j2, year = 2010, paper = p2)

p3 = Paper(title = "Awesome Paper 3", journal =j, year = 2011, abstract = "Previous paper on this topic was bullshit.")
p3.save()

a1.papers.add(p1, p2)
a2.papers.add(p1, p3)
a1.coauthors.add(a2)
a2.coauthors.add(a1)
a1.save()
a2.save()

like = Vote(account = a, paper = p1, votetype = "U")
like.save()
