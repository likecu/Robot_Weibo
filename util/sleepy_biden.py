import time

import config_helper
import random

import save_sql


def sleepy_biden(i):
    begin = int(save_sql.query("sleep_range_begin"))
    end = int(save_sql.query("sleep_range_end"))
    sleep_time = random.randint(begin, end)
    print("进行休眠：" + str(sleep_time) + "s")
    time.sleep(sleep_time)


def sleepy_biden_long():
    time.sleep(int(save_sql.query("time")))
