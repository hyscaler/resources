from locust import HttpUser, task

class MyCustomUser(HttpUser):
    @task
    def visit_homepage(self):
        self.client.get("/")
