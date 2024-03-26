import json

import requests
import glm
import save_sql


def send_comment(msg_id, msg):
    with open("ck123.txt", "r") as f:
        cookie = f.readline()
    with open("crftoken.txt", "r") as f:
        crf_token = f.readline()

    url = "https://weibo.com/ajax/comments/create"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "client-version": "v2.44.76",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "server-version": "v2024.03.21.2",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": crf_token,
        "Referer": "https://weibo.com/u/5874567901",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Cookie": cookie
    }

    data = {
        "id": msg_id,
        "comment": msg,
        "pic_id": "",
        "is_repost": "0",
        "comment_ori": "0",
        "is_comment": "0"
    }

    response = requests.post(url, headers=headers, data=data)
    save_sql.insert_exe_log("评论执行成功", msg_id, response.text)
    # print(response.text)
    # print(msg)


debug = False


def debugger_point(**kwargs):
    # for key, value in kwargs.items():
    # print(f"{key}: {value}")
    # 判断是否有记录
    if save_sql.get_comment_count(kwargs.get("wb")["id"]) == 0:
        # 如果有记录,则调用接口
        result = glm.creat_comment(kwargs.get("wb")["text"], 1)

        save_sql.save_robot_comment(kwargs.get("wb")["user_id"], kwargs.get("wb")["screen_name"],
                                    kwargs.get("wb")["text"], result,
                                    kwargs.get("wb")["id"])
        if not debug:
            send_comment(kwargs.get("wb")["id"], result)


