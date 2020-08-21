# Installing
You can install the package with
```
pip install snakepixel-beta
```
Once you have done this you can move on.

# Importing
You can import the package with 
```python
import snakepixel
```

# Using the library
You'll want to first create a variable to make this easier for us.
```python
snakeapi = snakepixel.snakepixelmethods.basicsnakepixelmethods()
snakeapisb = snakepixel.snakepixelmethods.skyblocksnakepixelmethods()
```
We should also create a variable that stores our api key.
```python
key = "YOURAPIKEY"
```
All commands will throw ```snakepixelexceptions.InvalidAPIKey``` if your api key is invalid.
Now, lets start with our first command.

# basicsnakepixelmethods

# get_key(key)
Returns a json containing info on a specific key.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.get_key(key))
```

# get_boosters(key)
Returns a json containing info on all boosters.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.get_boosters(key))
```

# gamecount(key, game)
Returns a json with playercounts of game.
Example usage:
```python
key = "YOURAPIKEY"k
print(snakeapi.gamecount(key, "skywars")
```
If you entered an invalid game it will throw ```snakepixelerrors.InvalidGameType```

# playercount(key)
Returns playercount of the network.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.playercount(key))
```

# guild(key, id)
Returns json with info of guild.
ID should be the id of your guild. There is a method called ```get_guild_id_by_name``` and ```get_guild_id_by_uuid``` but these are private functions and cannot be used.
Example usage:
```python
key = "YOURAPIKEY"
guildid = "YOURGUILDID"
print(snakeapi.guild(key, guildid)
```
If you entered an invalid guild id it will throw ```snakepixelexceptions.InvalidGuildID```

# get_leaderboards(key, game)
Returns json with leaderboard info on the game.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.guild(key, "skywars"))
```
Will raise ```snakepixelerrors.InvalidGameType``` if you entered an invalid game.

# player_with_name(key, name) (deprecated)
Uses a deprecated endpoint to get a json with player info.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.player_with_name(key, "DigestedMosquito"))
```
If you entered an invalid username it will throw ```snakepixelerrors.InvalidUsername```

# player_with_uuid(key, uuid) (the better version of player_with_name)
Returns a json with player info much like player_with_name.
Example usage
```python
key = "YOURAPIKEY"
uuid = "use mojang api to get uuid somehow im too lazy to put the code i used to do this"
print(snakeapi.player_with_uuid(key, uuid))
```
If you entered an invalid uuid it will throw ```snakepixelerrors.InvalidUUID```

# playerrank(key, name)
Returns player rank.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.playerrank(key, "digestedmosquito"))
#would return mvp+ because im mvp+
```
Will throw ```snakepixelerrors.InvalidUsername``` if you entered a bad username.

# status(key, uuid)
Returns json with status of player (what game, what map)
Example usage:
```python
key = "YOURAPIKEY"
uuid = "mojang api stuff"
print(snakeapi.status(key, uuid))
```
Will throw ```snakepixelerrors.InvalidUUID``` if you enter an invalid uuid.

# watchdog(key)
Returns json with watchdog stats.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapi.watchdog(key))
```

# skyblocksnakepixelmethods

# currentauctionsofplayer(key, player)
Returns json with current player auctions (no bin).
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapisb.currentauctionsofplayer(key, "digestedmosquito"))
```
Note: cannot raise InvalidUsername on this function, its on your own to put in a valid username or use another function to check usernames.

# currentauctions(key, page)
Returns json with 32 pages of auctions (very big), some values are encrypted.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapisb.currentauctions(key, 12))
```
Will raise ```snakepixelexceptions.PageNumberOutOfRange``` if you enter a page number over 32.

# bazaar(key)
Returns json with every item in the bazaar with all the info on it.
Example usage:
```python
key = "YOURAPIKEY"
print(snakeapisb.bazaar(key))
```

# profile_with_uuid(key, uuid)
Returns json with player's profiles. Will also contain encrypted data.
Example usage:
```python
key = "YOURAPIKEY"
uuid = "mojang api stuff"
print(snakeapisb.profile_with_uuid(key))
```
Will raise ```snakepixelexceptions.InvalidUUID``` if the uuid is invalid.

# Contact
Contact CatsRCool#2238 on discord if you have questions.
