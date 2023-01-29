import requests
# from app.app import GithubUsers, db
import sys

API_URL = "https://api.github.com/users"
seed_count = 150
response = requests.get(url=API_URL).json()


args = []
for arg in range(1, len(sys.argv)):
    args.append(sys.argv[arg])
    if len(args) > 2:
        break

if args and len(args) > 1:
    if args[0] in ['-t', '--total'] and args[1].isdigit():
        SEED_COUNT = int(args[1])

data = []
for x in range(0, seed_count):
    print(x)
    data.append({
        'id': response[x]['id'],
        'username': response[x]['login'],
        'avatar': response[x]['avatar_url'],
        'typ': response[x]['type'],
        'url': response[x]['url'],
    })

print(data)

#
#
# data = [
#     GithubUsers(id=data['id'], username=data['login'], avatar=data['avatar_url'],
#                 typ=data['type'], url=data['url']) for data in response]
#
# db.session.add_all(data)
# db.session.commit()
# print('Successfully saved')






#
# print(data)
# print(len(data))
