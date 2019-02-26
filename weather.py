from urllib.request import urlopen
import bs4
import xmltodict
import pprint
import json

api_id = "86065364c55637f337a6a0e6456dd09e"

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()

    #USING XMLTODICT
    def download_page(self):
        # connect to the web site

        #Per defecte es JSON, sino s'ha de especificar &mode=xml
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=LLeida,es&appid="+ api_id +"&unit=metric")
        
        # get the download_page
        page = f.read()
        f.close()
        return page

    #USING BS4
    # def search_activities(self, page):
    #     tree = bs4.BeautifulSoup(page,"lxml")
    #
    #     t = tree.find("temperature")
    #     w = tree.find("weather")
    #
    #     print(t["value"]+" and "+w["value"])
    #     return None

    def search_activities(self, page):
        '''xml = xmltodict.parse(page)
        pprint.pprint(xml)'''

        dicc = json.loads(page)
        pprint.pprint(dicc)
        temp = dicc['main']['temp']
        weather = dicc['weather'][0]['description']

        return str(temp-273)+"C and "+ weather

    def run(self):
        # download a web page
        page = self.download_page()
        # search activities in web page
        data = self.search_activities(page)
        # print the activities
        print(data)

if __name__ == "__main__":
    c = WebClient()
    c.run()