import urllib.request as req
import json
import os
dir_name = "google"

# if the dir is not created, create one
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# get url for scrapping
url = "https://www.google.com/doodles/json/2024/1?hl=zh-TW"
# get url request
f = req.urlopen(url)
# s = f.read()
# pics = json.loads(s)
# convert to dict in list
pics = json.load(f)
# print(type(pics))

for i in pics:
    # i is dict outside list
    # get dict["title"]
    print(i["title"])
    # create img path
    img = "https:" + i["high_res_url"]
    # check img path
    # print(img)s
    # urlretrieve(img_url, path) to store img to flie
    # split url by ignoring "/"
    fp = dir_name + "/" + img.split("/")[-1]
    # print(fp)
    req.urlretrieve(img,fp)
    # print("-"*30)