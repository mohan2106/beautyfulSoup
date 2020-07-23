import requests
import re
from bs4 import BeautifulSoup

result = requests.get("https://www.bigbazaar.com/products/home-needs/cleaning-accessories",verify=False)
# print("Result status: \n")
print(result.status_code)
# print("body: \n")
# print(result.content)

src = result.content
soup = BeautifulSoup(result.text,'lxml')
# below command will convert the soup in userfriendly readable model
# print(soup.prettify()) 
link = soup.find_all('a',class_="")

f = open("links.txt", "w")
# f.write("Now the file has more content!")

def extract_data(link,category):
    print(category)
    print(link)
    diff = link.split('/')
    n = len(diff)
    cat_name = diff[n-2]
    category = diff[n-1]
    f.write(cat_name +"," + category + "," + link + "\n")


for i in link:
    try:
        lk = i['href']
        name = i.get_text()
        if(re.search("https://www.bigbazaar.com/products/*",lk)):
            extract_data(lk,name)
    except:
        pass

f.close()

'''
f.write("CATEGORY, SUB CATEGORY , PRODUCT NAME , PRODUCT PRICE\n")


categories = []
for cat in soup.find_all('div',class_='_2dS-v'):
    categories.append(cat)

# print(categories[0].find('h2').get_text())
for item in categories:
    # print(item.find('h2').get_text())
    cat_name = item.find('h2').get_text()
    data = item.find_all('div',class_='_1Jgt5')
    for j in data:
        # print("\t" + j.find('h3').get_text())
        sub_cat_name = j.find('h3').get_text()
        subCat = j.find_all('div',class_='_2wg_t')
        for product in subCat:
            name = product.find('div',class_='jTy8b').get_text()
            price = product.find('span',class_='bQEAj').get_text()
            # print("\t\t" + "name = " + name  + " ,price = "+price)
            f.write(cat_name + "," + sub_cat_name + ","+name + "," + price + "\n")
            # f.write('{:30s},{:30s},{:50s},{:5s}\n'.format(cat_name,sub_cat_name,name,price))


f.close()'''