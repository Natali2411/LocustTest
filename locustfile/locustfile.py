# import random
import urllib3
from locust import HttpUser, task, constant_pacing
from locust.log import setup_logging
# import config
from common.config import *
# from load_tests.common.db import TestData
from common.api import API

# constant - for a fixed amount of time
# constant_pacing - for an adaptive time that ensures the task runs (at most) once every X seconds
# between - for a random time between a min and max value


setup_logging("INFO", None)
urllib3.disable_warnings()


class AttackTest(HttpUser):
    sites_list = sites_list
    wait_time = constant_pacing(2)


    def on_start(self):
        pass

    @task(5)
    def get_rash_sites(self):
        # GET /api/request54
        for url in self.sites_list:
            self.client.get(
                url=url, headers=API.api_headers()
            )

    @task(0)
    def stop_test(self):
        self.environment.runner.quit()




#class WebsiteUser(HttpUser):
host = "http://127.0.0.1"
min_wait = 10
max_wait = 10000
task_set = [AttackTest]
#tasks = {LocationInfo: 2}
