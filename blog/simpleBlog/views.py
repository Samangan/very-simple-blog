from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from simpleBlog.models import Post, Comment

def vote(request, post_id):
	return HttpResponse("hello vote")