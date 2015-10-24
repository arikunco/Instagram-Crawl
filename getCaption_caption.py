#!/usr/bin/python
from instagram.client import InstagramAPI
import httplib2
import json
import sys
import numpy
import time 

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
#'misedventure', 'nadinelist', 'she_whowanders', 'dionwiyoko', 'kezban_akdag', 'yudhass', 'shasya_santoso', 'thaismadnight', 'pertifektionxx', 'lawilly_fraiseetbrioche', 'jase__11', 'harrieram', 'lukespartacus', 'rosiebondi', 'kholishra', 'isabellecathrin', 'gdscano', 'pkd_official', '_oscarespinosa', 'egoitzzarallo', 'mila_msc_', 
#username_activity = ['moviefreak1312']

#username_capt = ['charcharstokes', 'kotoko64', 'ashleighrice123', 'lisanelliganfitness', 'ahmedsetiawan25', 'princessdiana1209', 'soulsister76', 'pmtathletes','julietteamad', 'lisasgetfit', 'ironny_k', 'allyouneedislove_quotes', 'xneekag']

username_capt = ['harcharstokes','ashleighrice123','lisanelliganfitness','ahmedsetiawan25','princessdiana1209','soulsister76','pmtathletes','julietteamad','lisasgetfit','ironny_k','allyouneedislove_quotes','beth_southwell_98','brendarippee','hanneloretimmers','serina_bogaerts','maddiemagpie','thestarstruck','langleav','angie_dp83','kotoko64','demetraleigh']
for i in username_capt:
	userid = username_to_id(i)
	time.sleep(5)
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

	# print all_media_ids
	# print len(all_media_ids)
	print len(all_media_img)
	#with open("selfie_"+i+".txt", "w") as text_file:
	with open("caption_"+i+".txt", "w") as text_file:
		text_file.write(format(all_media_caps))
		text_file.write(format(all_media_img))
	time.sleep(5)

	#print all_media_caps
	# print len(all_media_caps)
	#print all_media_img
	
#csvku = numpy.concatenate((all_media_caps,all_media_img))
#print csvku