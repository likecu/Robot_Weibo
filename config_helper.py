import json
import os
import sys

import logging.config

logger = logging.getLogger("weibo")


def get_config():
    """获取config.json文件信息"""
    config_path = os.path.split(os.path.realpath(__file__))[0] + os.sep + "config.json"
    if not os.path.isfile(config_path):
        logger.warning(
            "当前路径：%s 不存在配置文件config.json",
            (os.path.split(os.path.realpath(__file__))[0] + os.sep),
        )
        sys.exit()
    try:
        with open(config_path, encoding="utf-8") as f:
            config = json.loads(f.read())
            # 重命名一些key, 但向前兼容
            handle_config_renaming(config, oldName="filter", newName="only_crawl_original")
            handle_config_renaming(config, oldName="result_dir_name", newName="user_id_as_folder_name")
            return config
    except ValueError:
        logger.error(
            "config.json 格式不正确，请参考 " "https://github.com/dataabc/weibo-crawler#3程序设置"
        )
        sys.exit()


def handle_config_renaming(config, oldName, newName):
    if oldName in config and newName not in config:
        config[newName] = config[oldName]
        del config[oldName]
