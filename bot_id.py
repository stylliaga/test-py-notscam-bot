import requests

TOKEN = '1185958724:AAG1eNwHEYK_0kqAzP3Ax5yjnKNZfSIsPuo'

URL = 'https://api.telegram.org/bot{TOKEN}'.format(TOKEN=TOKEN)

r = requests.get(f'{URL}/getUpdates')

print(r.json())
