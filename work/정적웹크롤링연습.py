from bs4 import BeautifulSoup
import urllib.request

response=urllib.request.urlopen("https://www.naver.com")
html_str=response.read().decode("utf-8")
print(html_str)

bs_obj=BeautifulSoup(html_str,"html.parser") #html가지고 BS객체 만들기
#print(type(bs_obj))
#print(bs_obj.prettify()) #html 예쁘게 보기
#print(type(bs_obj.strong))
#print(bs_obj.strong) #strong tag 첫번째 요소 찾기
#print(bs_obj.a) #a tag 첫번째 요소 찾기
#print(bs_obj.find_all("a")) #a tag 다 찾기
#print(bs_obj.select_one(".title"))  # .클래스 / # id / tag
print(bs_obj.select_one("#NM_THEME_CONTAINER > div.group_topstory > div:nth-child(1) > div > a.topstory_info > strong"))
