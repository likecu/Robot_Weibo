# pip install zhipuai 请先在终端进行安装

from zhipuai import ZhipuAI
import re


def creat_comment(msg: str,pic_url: str) -> str:
    """

    :rtype: object
    """
    client = ZhipuAI(api_key="dd97d0d253aba54d54857ebb8cfbc8f0.3FsOg1C64N2rpzmq")

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role": "system",
                "content": "用一句话来评论你的一个好朋友发的微博,图片为微博的配图："
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "msg"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": pic_url
                        }
                    }]
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

    print(j)

    return j
