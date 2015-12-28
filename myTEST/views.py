from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
	data =datetime.datetime.now()
	return render_to_response('index.html',{'current_date': data})

def s(request):
	print(request)
	# def getType(obj):
	# 	for i in xrange(1,10):
	# 		pass
	# 	pass
	data =datetime.datetime.now()
	return render_to_response('s.html',{'current_date': request})