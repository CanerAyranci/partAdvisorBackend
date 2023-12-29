import requests

response = requests.get('https://9ec2-193-255-125-93.ngrok-free.app/api/tires/')
print(response.json())