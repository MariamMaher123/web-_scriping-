import requests
import bs4
num_page=1
trade=[]
name=[]
price=[]

url=(f"https://www.amazon.eg/s?k=%D9%87%D8%A7%D9%81+%D8%A8%D9%88%D8%AA&page=1&qid=1670862080&ref=sr_pg_1")
page=requests.get(url)
bs=bs4.BeautifulSoup(page.content , 'html.parser')

pnage = bs.find('span', {"class": "s-pagination-item s-pagination-disabled"}, {"aria-disabled": "true"})
ppage = pnage.text
num=int(ppage)
#print(num)
while num_page <= num:
  url=(f"https://www.amazon.eg/s?k=%D9%87%D8%A7%D9%81+%D8%A8%D9%88%D8%AA&page={num_page}&qid=1670862080&ref=sr_pg_{num_page}")
  page=requests.get(url)
  bs=bs4.BeautifulSoup(page.content , 'html.parser')
  num_page+=1
 # print all trade mark for boots
  trade_mark=bs.find_all('span' , {"class": "a-size-base-plus a-color-base"})
  #Names and description
  name_des=bs.find_all('span' , {"class":"a-size-base-plus a-color-base a-text-normal"})
  #price
  prices=bs.find_all('span' , {"class":"a-price-whole"})
  for i in range(len(prices)):
        trade.append(trade_mark[i].text)
        name.append(name_des[i].text)
        price.append(prices[i].text.replace(".‎",""))

  #print("page ", num_page)
print("                           #######################################################################################################")
for index , nam in enumerate(name):
    print({ f"The price is {price[index]} ""جنيه" ,f"Trade is {trade[index]}" , f"Description is {nam}" }   )
print("                            #######################################################################################################")
#print(len(price) , len(trade) , len(name))



