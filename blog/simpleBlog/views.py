from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from simpleBlog.models import Post, Comment
import datetime

def vote(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	p.likes += 1
	p.save()
	return HttpResponseRedirect(reverse('post_detail', args=(p.id,)))

def comment(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	comment_content = request.POST['comment']
	c = Comment(content=comment_content, pub_date=datetime.date.today(), parent=p)
	if c.content:
		c.save()
		return HttpResponseRedirect(reverse('post_detail', args=(p.id,)))
	else:			
		# Redisplay the poll voting form.
		return render_to_response('simpleBlog/detail.html', {
			'post': p, 
			'error_message': "Commenting Failed! You didn't enter any text.",
		}, context_instance=RequestContext(request))