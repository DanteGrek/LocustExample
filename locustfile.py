from locust import HttpLocust, web
from users import ArchlinuxUser, HOST
import json


@web.app.route("/remote_stats")
def remote_stats():
    return

class WebsiteUser(HttpLocust):
    host = HOST
    min_wait = 10
    max_wait = 1000
    task_set = ArchlinuxUser