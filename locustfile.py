from locust import HttpLocust
from users import ArchlinuxUser
from constants import *
# PW = "traixe"
#
#
# class UserBehavior(TaskSet):
#     min_wait = 1000
#     max_wait = 10000
#
#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         headers = {
#             'origin': "https://spikefashion-dev.myshopify.com",
#             'upgrade-insecure-requests': "1",
#             'content-type': "application/x-www-form-urlencoded",
#             'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#             'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#             'referer': "https://spikefashion-dev.myshopify.com/password",
#             'accept-encoding': "gzip, deflate, br",
#             'accept-language': "en-US,en;q=0.9",
#         }
#         self.client.headers = headers
#         self.login()
#
#     def login(self):
#         respon = self.client.get("/password")
#         print str(respon.cookies)
#         with self.client.post("/password", data={"pasword": "traixe"},
#                                catch_response=True) as response:
#             if response.status_code != 302:
#                 #print "!!!"+str(response.status_code)+"\n"+str(response.content)
#                 response.failure(str(response.status_code)+"\n")
#
#     # @task(11)
#     # def collections_types(self):
#     #     self.client.get("collections/types?q=blazer")
#     #         # if response.status_code != 200:
#     #         #     response.failure()
#     #
#     @task(10)
#     def index(self):
#         self.client.get("/collections")
#
#     @task(1)
#     def stop(self):
#         self.interrupt()
#
#     # @task(1)
#     # def profile(self):
#     #     self.client.get("/profile")

class WebsiteUser(HttpLocust):
    host = HOST
    min_wait = 10
    max_wait = 1000
    task_set = ArchlinuxUser