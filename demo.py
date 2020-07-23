import requests
import re
from bs4 import BeautifulSoup

f = open("links.txt", "r")

cat_dic= {}

for l in f:
        line = l.split(',')
        link = line[2]
        s = link.split('\n')
        link = s[0]
        category = line[0]
        subCategoroy = line[1]
        # category = category.replace('-',"")
        # print(category + "|" + subCategoroy + "|" + link)
        # fetchData(link)
        if(category in cat_dic.keys()):
                cat_dic[category].append(link)
        else:
                cat_dic[category] = [link]

n = len(cat_dic)
for key,val in cat_dic.items():
        cat_name = key + ".csv"
        f2 = open(cat_name,'w')
        f2.write("CATEGORY,"+"SUBCATEGORY,"+"NAME\n")
        for k in val:
               k2 = k.split('/')
               n = len(k2)
               sub_cat = k2[n-1]
               result = requests.get(k,verify=False)
               soup = BeautifulSoup(result.text,'lxml')
               names = soup.find_all('h3',class_="ctgry-name")
               for name in names:
                       f2.write(key+ "," + sub_cat + "," + name.get_text() + "\n")
        f2.close()

# print(cat_dic)





f.close()