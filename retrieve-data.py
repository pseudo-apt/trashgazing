from spacetrack import SpaceTrackClient

# Downloads the space debris current positions to adjust positional estimates.

user = ""
password = ""
c = SpaceTrackClient(user, password)
c.authenticate()
data = c.get_space_debris()
with open('tle.json', 'w+') as f:
    f.write(data)
c.close()
