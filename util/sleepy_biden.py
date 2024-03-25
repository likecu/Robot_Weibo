import time

import config_helper
import random


def sleepy_biden(**kwargs):
    begin = config_helper.get_config().get("sleep_range_begin")
    end = config_helper.get_config().get("sleep_range_end")
    time.sleep(random.randint(begin, end))


def sleepy_biden_long():
    begin = config_helper.get_config().get("sleep_range_begin")
    large = config_helper.get_config().get("sleep_range_end")
    time.sleep(random.randint(begin, large))
