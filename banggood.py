from urllib.request import urlopen
import bs4

page = "https://www.banggood.com/Flashdeals.html"
title_lenght = 10

class WebClient(object):
	'''Class manager of the Web page given'''
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

		act_list = []

		for i in range(5):
			price_offer = elems_li[i].find("span", "price")
			price_regular = elems_li[i].find("span", "price_old")
			title = elems_li[i].find("span", "title")
			act_list.append((title.text[:title_lenght], "Offer: " + price_offer.text, "Regular: "+price_regular.text))

		return act_list
		#print(price.text)
		#print(title.text)

	def show_products(self, page):
		downloaded_page = self.download_page(page)
		data = self.search_acts(downloaded_page)
		print(data)

if __name__ == "__main__":
	c = WebClient()
	c.show_products(page)