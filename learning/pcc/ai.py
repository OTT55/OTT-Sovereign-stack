users = {
    "kolvt" : {
        "first" : 'kolakanwi',
        "last" : 'van tegha',
        "location" : 'doulai'  
    },
    "jon" : {
        "first" : 'jonathan',
        "last" : 'richards',
        "location" : 'usa',
    },
    "nalk" : {
        "first" : 'naliana',
        "last" : 'kul',
        "location" : 'finland',
    },
}

for username, user in users.items():
        print(f"\nUsername : {username}")
        full_name = f"{user['first']} {user['last']}"
        location = user['location']
        print(f"\tFull name: {full_name.title()}")
        print(f"\tLocation : {location.title()}")
