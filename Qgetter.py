import requests
import json
import argparse
import os

# Program description.
'''
Qgetter can get QQ headimages, nicknames and headimages of groups with a known QQ ID or GROUP ID.
Qgetter is based on the open Tencent™ QQ headimage and nickname API inteface.
Note: If U did not get a satisfactory result, please check does your QQ ID or
GROUP ID exists.
--Written by Sun Xiao
'''

def getHeadImg(QQID, save):
	'''Get the personal head image.'''
	headImg = requests.get(f'http://q1.qlogo.cn/g?b=qq&nk={QQID}&s=640').content
	with open(save, 'wb') as f:
		f.write(headImg)

def getNickName(QQID):
	'''Get the personal nick name.'''
	resp = requests.get(
		f'http://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins={QQID}')\
	.content.decode('GBK')
	resp = json.loads(resp[17:-1])
	return list(resp.values())[0][6]

def getGroupHeadImg(GROUPID, save):
	'''Get both the personal headimage and nickname.'''
	groupHeadImg = requests.get(
		f'http://p.qlogo.cn/gh/{GROUPID}/{GROUPID}/640/').content
	with open(save, 'wb') as f:
		f.write(groupHeadImg)

def parseOpts():
	'''Parse the command line options.'''
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-m', '--mode', required=True, 
		choices=('hi', 'nk', 'hn', 'gh'), 
		help='What do you want to get.Avalible options:   \
	①hi  :  Get personal head image.   \
	②nk  :  Get personal nick name.   \
	③hn  :  Get both the head image and the nick name.\
	④gh  :  Get head image of a group.')
	parser.add_argument('-i', '--id', required=True, 
		help='The target QQ ID or GROUP ID.', type=int)
	parser.add_argument('-s', '--save', required=False, 
		help='The name of the file that will \
be saved if U want to get an head image.')
	res = parser.parse_args()
	return res.mode, res.id, res.save

mode, id_, save = parseOpts()
if mode != 'nk' and save != None and os.path.exists(save):
	# Give a notice if the filename is already exists.
	while True:
		if_replace = input(
		'This file is already exists!Do U want to replace it? [y/n]')
		if if_replace == 'y':
			break
		elif if_replace == 'n':
			os._exit(0)
		else:
			print('Please choose from \'y\' or \'n\'!')
elif mode != 'nk' and save == None:
	print('Please enter a filename to save!')
	os._exit(0)

id_ = int(id_)
if mode == 'hi':
	getHeadImg(id_, save)
	print(f'Already saved the head image of {id_} to {save}.')
elif mode == 'nk':
	print(f'The nick name of {id_}:', getNickName(id_))
elif mode == 'hn':
	getHeadImg(id_, save)
	print(f'Already saved the head image of {id_} to {save}.')
	print(f'The nick name of {id_}:', getNickName(id_))
else:
	getGroupHeadImg(id_, save)
	print(f'Already saved the group image of {id_} to {save}.')