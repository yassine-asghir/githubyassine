from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(2,5)

    @task
    def get_double(self):
        self.client.get("/5")