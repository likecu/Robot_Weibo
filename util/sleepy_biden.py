import time

import config_helper
import random

import save_sql


def sleepy_biden(**kwargs):
    begin = int(save_sql.WeiboDatabase.query("sleep_range_begin"))
    end = int(save_sql.WeiboDatabase.query("sleep_range_end"))
    sleep_time = random.randint(begin, end)
    print("进行休眠：" + str(sleep_time) + "s")
    time.sleep(sleep_time)
    save_sql.insert_exe_log(kwargs.get("info"), "1", kwargs.get("info"))


def sleepy_biden_long():
    save_sql.WeiboDatabase.insert_exe_log("执行时间", "1", "")
    time.sleep(int(save_sql.WeiboDatabase.query("time")))

def sleepy_biden_long_long():
    save_sql.WeiboDatabase.insert_exe_log("执行时间", "1", "")
    time.sleep(600)