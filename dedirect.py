from concurrent.futures import ThreadPoolExecutor
import requests
import fire

def get_final_url(url, max_threads):
	if not url.startswith('http'):
		url = 'https://'+url
	resp = requests.head(url, allow_redirects=True)
	print(resp.url)

def dedirect(url=None, max_threads=25):
	"""
		Follows redirects and print the final url 
	"""
	if url:
		return get_final_url(url, max_threads)
	else:
		while True:
			try:
				with ThreadPoolExecutor(max_workers=25) as executor:
					executor.submit(get_final_url, input(), max_threads)
			except:
				break

if __name__ == '__main__':
	fire.Fire(dedirect)