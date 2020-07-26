import requests

BASE = 'http://127.0.0.1:5000/'

data = [
    {'likes': 112, 'name': 'Daily dose of standup', 'views': 10000},
    {'likes': 1243, 'name': 'Day in the life of', 'views': 10000123},
    {'likes': 15512, 'name': 'Travel Guide', 'views': 1123124},
    {'likes': 657324124, 'name': 'Are we living in a simulation', 'views': 529352324},
]

for i in range(len(data)):
    response = requests.put(
        BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)

input()
response = requests.get(BASE + 'video/0')

print(response.json())
