# import random
import urllib3
from locust import HttpUser, task, constant_pacing
from locust.log import setup_logging
# import config
from utilities.load_tests.common import config
# from load_tests.common.db import TestData
from utilities.load_tests.common.api import API

# constant - for a fixed amount of time
# constant_pacing - for an adaptive time that ensures the task runs (at most) once every X seconds
# between - for a random time between a min and max value


setup_logging("INFO", None)
urllib3.disable_warnings()


class GatewayLoadTest(HttpUser):
    settings = config.env
    wait_time = constant_pacing(2)
    olr_identities = None

    def on_start(self):
        self.client.verify = False
        #self.olr_identities = TestData().get_was_olr_identities()

    # @task(5)
    # def get_request_5kb(self):
    #     # GET /api/request5
    #     url = self.settings["api_base_url"] + self.settings["request5_url"]
    #     self.client.get(
    #         url=url, headers=API.api_headers(self.olr_identities[0])
    #     )
    #     self.olr_identities.pop(0)
    #     print(self.olr_identities)

    @task(5)
    def get_request_54kb(self):
        # GET /api/request54
        url = self.settings["api_base_url"] + self.settings["request54_url"]
        self.client.get(
            url=url, headers=API.api_headers() # self.olr_identities[0]
        )
        # self.olr_identities.pop(0)
        # print(self.olr_identities)
    #
    # @task(5)
    # def get_request_100kb(self):
    #     # GET /api/request100
    #     url = self.settings["api_base_url"] + self.settings["request100_url"]
    #     self.client.get(
    #         url=url, headers=API.api_headers(self.olr_identities[0])
    #     )
    #     self.olr_identities.pop(0)
    #     print(self.olr_identities)

    @task(0)
    def stop_test(self):
        self.environment.runner.quit()




#class WebsiteUser(HttpUser):
host = "http://127.0.0.1"
min_wait = 10
max_wait = 10000
task_set = [GatewayLoadTest]
#tasks = {LocationInfo: 2}


"""
# setup Environment and Runner
env = Environment(user_classes=[BusinessHourInfo, LocationInfo])
env.create_local_runner()

# start a WebUI instance
env.create_web_ui("127.0.0.1", 8089)

# start a greenlet that periodically outputs the current stats
gevent.spawn(stats_printer(env.stats))

# start a greenlet that save current stats to history
gevent.spawn(stats_history, env.runner)

# start the test
env.runner.start(1, spawn_rate=10)

# in 60 seconds stop the runner
gevent.spawn_later(60, lambda: env.runner.quit())

# wait for the greenlets
env.runner.greenlet.join()

# stop the web server for good measures
env.web_ui.stop()
"""