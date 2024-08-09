import requests
import concurrent.futures
import time
from collections import defaultdict

def send_request(url):
    response = requests.get(url)
    return response.status_code

url = 'PAST_YOUR_URL_HERE'

# Number of requests you want to send
number_of_requests = 1000
max_workers = 100  # Increase the number of threads to allow more concurrent requests

# Dictionary to hold the count of each status code
status_count = defaultdict(int)

# Track the start time
start_time = time.time()

# Use ThreadPoolExecutor to send requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = []
    for i in range(number_of_requests):
        futures.append(executor.submit(send_request, url))
        # Adding a small sleep to control the rate of requests
        if (i + 1) % 100 == 0:
            time.sleep(1)  # Adjust this sleep time to fine-tune your request rate

    for future in concurrent.futures.as_completed(futures):
        try:
            status = future.result()
            status_count[status] += 1
        except Exception as e:
            print(f'Request failed: {e}')

# Track the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Calculate requests per minute
requests_per_minute = (number_of_requests / total_time) * 60

# Print out the count of each status code
print("Response status counts:")
for status_code, count in status_count.items():
    print(f'{status_code}: {count}')

print(f'Total requests: {number_of_requests}')
print(f'Total time taken: {total_time:.2f} seconds')
print(f'Request rate: {requests_per_minute:.2f} requests per minute')
