from json import loads, dumps
from time import time

def checkuserexists(guild_id, user_id):
    with open('dontdm.json', 'r') as f:
        users = loads(f.read())
    if guild_id in users:
        for user in users[guild_id]["mutedMembers"]:
            if user["id"] == user_id:
                return True
    return False

def setuser(guild_id, user_id, expire):
    with open('dontdm.json', 'r') as f:
        users = loads(f.read())
    if guild_id not in users:
        users[guild_id] = {}
        users[guild_id]["mutedMembers"] = []
    users[guild_id]["mutedMembers"].append({"id": user_id, "expire": expire})
    with open('dontdm.json', 'w') as f:
        f.write(dumps(users, indent=4))

def removeuser(guild_id, user_id):
    with open('dontdm.json', 'r') as f:
        users = loads(f.read())
    if guild_id in users:
        for user in users[guild_id]["mutedMembers"]:
            if user["id"] == user_id:
                users[guild_id]["mutedMembers"].remove(user)
    with open('dontdm.json', 'w') as f:
        f.write(dumps(users, indent=4))

def deleteexpiredusers():
    with open('dontdm.json', 'r') as f:
        users = loads(f.read())
    for guild_id in list(users):
        for user in users[guild_id]["mutedMembers"]:
            if user["expire"] < int(time()):
                removeuser(guild_id, user["id"])
        if users[guild_id]["mutedMembers"] == []:
            del users[guild_id]
            with open('dontdm.json', 'w') as f:
                f.write(dumps(users, indent=4))