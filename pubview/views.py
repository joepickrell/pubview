# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from pubview.models import Paper, Account, Vote


@login_required
def vote(request, paper_id):
    p = get_object_or_404(Paper, pk=paper_id)
    try:
        v = Vote(account = request.user.account, paper = p, votetype = request.POST['votetype'])
    except (KeyError, Vote.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'pubview/detail.html', {
            'paper': p,
            'error_message': "Vote type doesn't exist",
        })
    else:
	#has this user already voted on this paper?
        if request.user.account.alreadyvoted(paper_id)==False:
		# save if not
		v.save()
	else:
		# is the vote the same?
		testv = Vote.objects.get(account = request.user.account, paper = p)
		if testv.votetype != v.votetype:
			testv.votetype = v.votetype
			testv.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pubview:index'))
