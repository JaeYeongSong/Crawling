from time import sleep
import os
import threading
import datetime
import requests

myToken = "your key"

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

now_times = datetime.datetime.now()
nows = now_times.strftime('%Y-%m-%d %H:%M:%S')

text_intro = "-------------------------------------------------"
print(f"{nows} - 프로그램이 시작되었습니다.")
text_intro_01 = f"{nows} - 프로그램이 시작되었습니다."

print(f"{nows} - 5분(300초)마다 티스토리에서 값을 불러와 비교합니다.")
text_intro_02 = f"{nows} - 5분(300초)마다 티스토리에서 값을 불러와 비교합니다."

post_message(myToken,"#Test", text_intro)
post_message(myToken,"#Test", text_intro_01)
post_message(myToken,"#Test", text_intro_02)

sleep(5)

re_now_times = datetime.datetime.now()
re_nows = re_now_times.strftime('%Y-%m-%d %H:%M:%S')

print(f"{nows} - Crawling 프로그램이 정상적으로 실행되었습니다.")
print(f"{nows} - 300초 뒤에 프로그램이 반복 실행됩니다.")
os.system('D:/Crawling.py')

sleep(300)

def restart():
    now_times = datetime.datetime.now()
    now = now_times.strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"{now} - Crawling 프로그램이 정상적으로 실행되었습니다.")
    os.system('D:/Crawling.py')

    print(f"{now} - Compare 프로그램이 정상적으로 실행되었습니다.")
    os.system('D:/Compare.py')

    threading.Timer(300, restart).start()

restart()