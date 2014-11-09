import requests
from bs4 import BeautifulSoup
import time

def leaderBoardSearch():
    page = 0
    user_num = 1
    username = input("Enter your username: ")
    is_done = 1
    while is_done == 1:
        search_page = 'https://oc.tc/stats?page='+str(page+1)
        page_src = requests.get(search_page)
        page_src_plain = page_src.text
        soup_ob = BeautifulSoup(page_src_plain)

        for user in soup_ob.findAll('img', {'class': 'avatar'}):
            time.sleep(.1)
            rank = user.get('title')
            entered_name = username.capitalize()
            current_name = rank.capitalize()
            if entered_name != current_name:
                print(rank + ' is number ' + str(user_num))
                user_num += 1

            else:
                print('You are number ' + str(user_num) + "!\n Please visit " + search_page + " for more information!")
                is_done = 0
                break

        page += 1

leaderBoardSearch()
