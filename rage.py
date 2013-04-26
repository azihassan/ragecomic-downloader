import urllib2
import sys
import os
import json

def download(remote, local):
	with open(local, 'w') as out: 
		u = urllib2.urlopen(remote)
		while True:
			chunk = u.read(1024)
			
			if not chunk:
				break

			out.write(chunk)

def imgurddl(url):
	exts = ['jpg', 'png', 'gif', 'jpeg']
	
	if 'imgur.com' in url:
		for ext in exts:
			if url.endswith(ext):
				return url

		return url + '.png'
	
	return url

if __name__ == '__main__':
	url = 'http://www.reddit.com/r/fffffffuuuuuuuuuuuu.json'
	entries = json.loads(urllib2.urlopen(url).read())
	
	try:
		landing_dir = sys.argv[1]
	except IndexError:
		landing_dir = 'pics'

	landing_dir = os.path.join(os.path.dirname(__file__), landing_dir)
	
	for rage in entries['data']['children']:
		remote = imgurddl(rage['data']['url'])
		local = os.path.join(landing_dir, os.path.basename(remote))

		sys.stdout.write('Downloading ' + remote + '...')

		if os.path.exists(local):
			sys.stdout.write('\t[Skipped]\n')
		else:
			download(remote, local)
			sys.stdout.write('\t[Done]\n')
