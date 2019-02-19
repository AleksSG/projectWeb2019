from urllib.request import urlopen
import bs4

class WebClient(object):

	def __init__(self):
		super(WebClient, self).__init__()

	def download_page(arg):
		f = urlopen("http://www.eps.udl.cat/ca/")
		page = f.read()
		f.close()
		return page

	def search_acts(self, page):
		tree = bs4.BeautifulSoup(page, 'lxml')
		activities = tree.find_all("div", "featured-links-item")
		act_list = []
		for act in activities:
			title = act.find("span", "flink-title")
			link = act.find("a")
			act_list.append((title.text, link["href"]))
		return act_list

	def run(self):
		page = self.download_page()
		data = self.search_acts(page)
		
		print(data)

if __name__ == "__main__":
	c = WebClient()
	c.run()