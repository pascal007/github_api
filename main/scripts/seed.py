import sys
sys.path.insert(0, '..')
import requests
from main.app import GithubUsers, db_uri, create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

create_app().app_context().push()

engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)

s = Session()

if GithubUsers.query.all():
    print('Data already exist in the database')
    sys.exit(0)

API_URL = "https://api.github.com/users"
seed_count = 150
response = requests.get(url=API_URL, params={'per_page': 100})

try:
    if response.status_code == 200:
        response = response.json()
        args = []
        for arg in range(1, len(sys.argv)):
            args.append(sys.argv[arg])
            if len(args) > 2:
                break

        if args and len(args) > 1:
            if args[0] in ['-t', '--total'] and args[1].isdigit():
                seed_count = int(args[1])

        data = list()
        id_set = set()
        counter = 0
        while seed_count > 0:
            for resp in response:
                if resp['id'] in id_set:
                    continue
                data.append({
                    'id': resp['id'],
                    'username': resp['login'],
                    'avatar_url': resp['avatar_url'],
                    'type': resp['type'],
                    'url': resp['html_url']
                })
                id_set.add(resp['id'])

                counter += 1
                seed_count -= 1
                if seed_count == 0:
                    break
            if seed_count > 0:
                response = requests.get(url=API_URL, params={'per_page': 100, 'since': counter}).json()

        s.bulk_insert_mappings(GithubUsers, mappings=data)
        s.commit()
        print("stored successfully")

    else:
        print("Error in seeding data")

except Exception as e:
    print("Unable to seed data", e)
