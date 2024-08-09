# python-rate-limit-check
Small script to ddos url and give you response codes

Only settings you need to change is 

url = 'PAST_YOUR_URL_HERE' # url where you will send requests
number_of_requests = 1000 # number of request in total to send
max_workers = 100  # Increase the number of threads to allow more concurrent request

e.g how it should work

root@ubuntu:~/# python3 script.py
Response status counts:
429: 757
404: 243
Total requests: 1000
Total time taken: 10.16 seconds
Request rate: 5903.54 requests per minute
