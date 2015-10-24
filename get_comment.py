#!/usr/bin/python
from instagram.client import InstagramAPI
import httplib2
import json
import sys
import numpy
import urllib
import time 

client_id = ''
client_secret = ''
access_token = ''

api = InstagramAPI(client_id=client_id, client_secret=client_secret,access_token= access_token)

def username_to_id(username):
	"""Accepts a username and returns its ID."""
	user = api.user_search(q=username, count=1)
	if username != user[0].username:
		logger.error('Username to ID failed')
	return user[0].id

username_selfies = ['arikunc0r0']

for i in username_selfies:
	userid = username_to_id(i)
	print '============================='
	print 'mulai dari user id =', userid
	print 'username =', i
	all_media_ids = []
	#all_media_caps = []
	#all_media_img = []
	media_ids,next = api.user_recent_media(user_id=str(userid), count=3)
	print(media_ids)
	for media_id in media_ids:
		print(media_id.id)
		print(api.media_comments(media_id.id))
