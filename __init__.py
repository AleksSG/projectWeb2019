from urllib.request import urlopen
import bs4

class WebClient(object):

	def __init__(self):
		super(WebClient, self).__init__()

	def download_page(arg, page):
		f = urlopen(page)
		page = f.read()
		f.close()
		return page

	def search_acts(self, page):
		tree = bs4.BeautifulSoup(page, 'lxml')
		all_elem_ul = tree.find("ul", "goodlist_1")
		elems_li = all_elem_ul.find_all("li")

		#items_price = tree.find_all("div", "priceitem")
		#items_title = tree.find_all("span", "title")

		act_list = []
		
		for i in range(5):
			price = elems_li[i].find("span", "price")
			title = elems_li[i].find("span", "title")
			act_list.append((title.text, price.text))
		return act_list
		#print(price.text)
		#print(title.text)

	def run(self, page):
		page = self.download_page(page)
		data = self.search_acts(page)
		
		print(data)

if __name__ == "__main__":
	c = WebClient()
	c.run("https://www.banggood.com/Flashdeals.html")