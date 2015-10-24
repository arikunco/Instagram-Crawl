#!/usr/bin/python
from instagram.client import InstagramAPI
import httplib2
import json
import sys
import numpy

client_id = 'ccc83b59127e49abb5169df4b815fb73'
client_secret = '3064f663f15b43bfb8ea9afa000d7a6c'
access_token = '261673262.ccc83b5.0632f8626ca34630bd660e279a36f304'

api = InstagramAPI(client_id=client_id, client_secret=client_secret,access_token= access_token)

def username_to_id(username):
    """Accepts a username and returns its ID."""
    user = api.user_search(q=username, count=1)
    if username != user[0].username:
        logger.error('Username to ID failed')
    return user[0].id

username_food = ['pramudit4rn','nick.birc','pinsudan','boterkaaseierenblog','dobroty_od_a','in.happenstance','sophgoesvegan','abeolac','parischezsharon','brooklynjapwife','taramilktea','taylorann_2505','iamkeerthi','besst','bloomzy','tommyarini','carlabananax3','chef_meir_adoni','ichakhairunissa','irmanbob','bakingmoments','ingepurnamasari','mikahara_87']

for i in username_food:
	userid = username_to_id(i)
	print '============================='
	print 'mulai dari user id =', userid
	print 'username =', i
	all_media_ids = []
	all_media_caps = []
	all_media_img = []
	#print(userid)
	media_ids,next = api.user_recent_media(user_id=str(userid), count=20)
	temp,max_tag=next.split('max_id=')
	max_tag=str(max_tag)

	for media_id in media_ids:
			#print media_id.caption.text
			#print media_id.images['standard_resolution'].url
			all_media_ids.append(media_id.id)
			all_media_caps.append(media_id.caption)
			all_media_img.append(media_id.images['standard_resolution'].url)
	counter = 1
		
	while next and counter < 2:
		more_media, next =api.user_recent_media(user_id=str(userid), max_id=max_tag)
		temp,max_tag=next.split('max_id=')
		max_tag=str(max_tag)
		for media_id2 in more_media:
			#print media_id2.caption.text
			#print media_id2.images['standard_resolution'].url
			all_media_ids.append(media_id2.id)
			all_media_caps.append(media_id2.caption)
			all_media_img.append(media_id2.images['standard_resolution'].url)
		counter+=1
	all_media_caps = str(all_media_caps).replace(i,'')
	# print all_media_ids
	# print len(all_media_ids)
	print len(all_media_img)
	#with open("selfie_"+i+".txt", "w") as text_file:
	with open("food_"+i+".txt", "w") as text_file:
		text_file.write(format(all_media_caps))
		text_file.write(format(all_media_img))
	#print all_media_caps
	# print len(all_media_caps)
	#print all_media_img
	
#csvku = numpy.concatenate((all_media_caps,all_media_img))
#print csvku