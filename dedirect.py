from concurrent.futures import ThreadPoolExecutor
import requests
import fire

def get_final_url(url):
	if not url.startswith('http'):
		url = 'https://'+url
	resp = requests.head(url, allow_redirects=True)
	print(resp.url)

def dedirect(url=None, max_threads=25):
	"""
		Follows redirects and print the final url 
	"""
	if url:
		return get_final_url(url)
	else:
		executor= ThreadPoolExecutor(max_workers=max_threads)
		while True:
			try:
				url = input()
				executor.submit(get_final_url, url)
			except Exception as e:
				break
		executor.shutdown(wait=True)

if __name__ == '__main__':
	fire.Fire(dedirect)