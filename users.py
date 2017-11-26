import random

from locust import TaskSet,  task
from pyquery import PyQuery

from constants import *

class AbstractUser(TaskSet):
    min_wait = 1000
    max_wait = 10000

    def on_start(self):
        r = self.get_index()
        pq = PyQuery(r.content, parser='html')
        self.sitemap_links = []
        for a in pq.find("a"):
            print "Element:", str(a.attrib)
            if "href" in a.attrib:
                if HOST in a.attrib['href']:
                    print "Endpoint: ", str(a.attrib['href'])
                    self.sitemap_links.append(a.attrib['href'][:HOST.lenght])
                self.sitemap_links.append(a.attrib['href'])
            print "\nlinks\n", str(self.sitemap_links)+"\n##################################\n"

    def get_index(self):
        return self.client.get("/")

    @task(30)
    def load_page(self):
        url = random.choice(self.sitemap_links)
        self.client.get(url)

    def stop(self):
        self.interrupt()


class ArchlinuxUser(AbstractUser):

    @task(30)
    def load_page(self):
        url = random.choice(self.sitemap_links)
        self.client.get(url)
    # @task(30)
    # class SubTaskSet(AbstractUser):

        # def on_start(self):
        #     self.client.get("/")
        #
        #
        # @task
        # def my_task(self):
        #     pass

