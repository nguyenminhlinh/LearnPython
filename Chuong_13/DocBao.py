import requests
from bs4 import BeautifulSoup
import webbrowser
count = 0
while True:
    url = requests.get("https://dantri.com.vn")
    print(url)
    soup = BeautifulSoup(url.content, "html.parser")
    # print(soup)
    titles = soup.find_all(class_="article-title")
    # print(titles)
    new_title = titles[count].text.strip()
    # print(new_title)
    children = titles[count].findChildren("a" , recursive=False)
    print(children)
    find_a = children[0]['href']
    print("\nBài báo:" + " \"" + new_title + "\"")
    print("Bạn có muốn xem không? (Y/N)")
    ans = input("").lower()
    if ans == "y":
        url = "https://dantri.com.vn/%s" % find_a
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Try again!")
        count+=1
        continue
    else:
        print("Just \"y\" or \"n\"!")
        break