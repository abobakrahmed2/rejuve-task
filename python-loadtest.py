import requests
import threading

def send_request():
    url = 'http://localhost'  # Change to the actual URL of your Nginx load balancer
    response = requests.get(url)
    print(response.text)

# Simulate concurrent users
num_users = 10
threads = []
for _ in range(num_users):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
