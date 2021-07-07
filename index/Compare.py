import datetime
import filecmp
import requests
import threading
import os
from time import localtime, strftime

myToken = "your key"

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

folder_path = 'D:/list/' # 파일 내용 비교할 파일 가져오기(경로 입력)

# each_file_path_and_gen_time: 각 file의 경로와, 생성 시간을 저장함
each_file_path_and_gen_time = []
for each_file_name in os.listdir(folder_path):
    # getctime: 입력받은 경로에 대한 생성 시간을 리턴
    each_file_path = folder_path + each_file_name
    each_file_gen_time = os.path.getctime(each_file_path)
    each_file_path_and_gen_time.append(
        (each_file_path, each_file_gen_time)
    )

# 가장 생성시각이 큰(가장 최근인) 파일을 리턴 
most_recent_file_1 = max(each_file_path_and_gen_time, key=lambda x: x[1])[0]

# 가장 생성시각이 두번째로 큰(두번쨰로 최근인) 파일을 리턴 
uniq = set(each_file_path_and_gen_time)
most_recent_file_2 = sorted(uniq, reverse=True)[1][0]

nows = datetime.datetime.now()
print_now = nows.strftime('%Y-%m-%d %H:%M:%S')

fivelasts = nows - datetime.timedelta(minutes=5)

fivelast = fivelasts.strftime('%Y-%m-%d %H시 %M분')

filecmp = filecmp.cmp(most_recent_file_1, most_recent_file_2)

if filecmp == False:
    print(f"{print_now} - 변화가 생겼습니다.")
    post_message(myToken,"#Test", f"`{print_now} - 변화가 생겼습니다.`")
    os._exit(1)