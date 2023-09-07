import requests
from time import time

BASE_URL = 'http://127.0.0.1:5000'  
TOTAL_RUNS = 100
def register_user(username, password):
    r = requests.post(f"{BASE_URL}/register", json={"username": username, "password": password})
    return r.status_code

def login_user(username, password):
    r = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    return r.status_code

def load_test_post():
    register_user("load_test_user", "load_test_pass")
    login_user("load_test_user", "load_test_pass")

    start = time()
    for i in range(TOTAL_RUNS):
        r = requests.post(f"{BASE_URL}/item", json={'id': str(i), 'name': 'item' + str(i)})
    end = time()
    print("POST Load Test completed in ", end - start, " seconds.")

def load_test_get():
    start = time()
    for i in range(TOTAL_RUNS):
        r = requests.get(f"{BASE_URL}/item/{i}")
    end = time()
    print("GET Load Test completed in ", end - start, " seconds.")

def load_test_put():
    start = time()
    for i in range(TOTAL_RUNS):
        r = requests.put(f"{BASE_URL}/item/{i}", json={"name": "updated_item" + str(i)})
    end = time()
    print("PUT Load Test completed in ", end - start, " seconds.")

def load_test_delete():
    start = time()
    for i in range(100):
        r = requests.delete(f"{BASE_URL}/item/{i}")
    end = time()
    print("DELETE Load Test completed in ", end - start, " seconds.")

if __name__ == "__main__":
    load_test_post()
    load_test_get()
    load_test_put()
    load_test_delete()
