import requests 
from bs4 import BeautifulSoup
import time

q_url = 'https://catalog.onliner.by/sdapi/catalog.api/search/notebook?page={}&page={}'

start_total = time.perf_counter()
f = open('parsed links.txt', 'w')
total_notebooks = 0

for page in range(1, 238): #237
	start = time.perf_counter()
	cur_url = q_url.format(page, page)
	print('cur_url: {}'.format(cur_url))
	
	r = requests.get(cur_url).json()
	notebooks_count = len(r['products'])
	total_notebooks += notebooks_count
	print('count of notebooks: {}'.format(notebooks_count))
	
	for i in range(notebooks_count):
		#print('notebook\'s url: {}'.format(r['products'][i]['html_url']))
		f.write(r['products'][i]['html_url'] + '\n')
	
	run = time.perf_counter() - start
	print('parsed {} pages, time of parsing the last page: {:.2f} seconds'.format(page, run))

run_total = time.perf_counter() - start_total
print('parsed {} notebooks with total runtime: {:.2f} seconds'.format(total_notebooks, run_total))
