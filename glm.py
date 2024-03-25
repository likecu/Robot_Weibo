# pip install zhipuai 请先在终端进行安装

from zhipuai import ZhipuAI
import re
import config_helper


def creat_comment(msg: str, count: int) -> str:
    """

    :rtype: object
    """

    client = ZhipuAI(api_key=config_helper.get_config().get("api_key"))

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role": "system",
                "content": "你是微回机器人，一款专为微博设计的智能互动工具。你的角色是帮助用户高效管理微博动态，通过智能回复与用户建立良好互动，提升关注度。你的能力有:- 自动监测微博动态，自动进行回复"
            },
            {
                "role": "user",
                "content": "请使用一句中文来评论你的一个好朋友发的微博：" + msg
            }
        ],
        top_p=0.7,
        temperature=0.95,
        max_tokens=1024,
        stream=True,
    )
    t = []
    for trunk in response:
        t.append(trunk.choices)

    pattern = r"content='(.*?)',"

    j = ""
    for i in t:
        t1 = re.search(pattern, str(i)).group(1)
        j += t1

    j = j.replace('"', "").replace("\\n", "").replace("`", "")
    print(j)

    if "句" in j and count < 5:
        return creat_comment(msg, count + 1)

    return j
