# import requests module 
import requests 
  
# Making a get request 
response = requests.get('https://api.github.com/userid=123') 
  
# print request object 
print(response.url) 
  
# print status code 
print(response.status_code) 