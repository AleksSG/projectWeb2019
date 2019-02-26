# projectWeb2019
This repository has:
- Web Scraping from [Banggood](https://www.banggood.com/Flashdeals.html)
- A small API example from [Open Weather Map API](https://api.openweathermap.org/data/2.5/weather?q=LLeida,es&appid=86065364c55637f337a6a0e6456dd09e&unit=metric)

It supports a **numeric** argument which defines the length of the title scratched. (10 default)
```
python banggood.py 5
```
It **does not** support error handling in arguments given such as -2, "text" or 10000.

It will print a list result with the following format:

[("title1", "price_offer1", "price_regular1"),
("title2", "price_offer2", "price_regular2"),]

Which can be replaced with any future notification method to send the user.

