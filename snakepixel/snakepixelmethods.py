import requests

from .snakepixelerror import InvalidAPIKey, InvalidGuildName, InvalidUUID, InvalidGameType, InvalidGuildID, InvalidUsername, \
    PageNumberOutOfRange


class basicsnakepixelmethods:
    @staticmethod
    def __check_key(key):
        if requests.get(f"https://api.hypixel.net/key?key={key}").json()["success"] == False:
            raise InvalidAPIKey
        else:
            return True

    # not my function
    @staticmethod
    def __get_rank(key, name):
        url = f"https://api.hypixel.net/player?key={key}&name={name}"
        res = requests.get(url)
        data = res.json()

        if data["player"] == None:
            raise InvalidUsername
        if "prefix" in data["player"]:
            player_prefix = (data["player"]["prefix"])
            if player_prefix == "§d[PIG§b+++§d]":
                # print('Rank acquired- PIG')
                return (f"[PIG+++]")
            elif player_prefix == "§c[SLOTH]":
                # print('Rank acquired- Sloth')
                return ("[SLOTH]")
        if "rank" in data["player"]:
            rank = data["player"]["rank"]
            if rank == 'ADMIN':
                # print('Rank acquired- Admin')
                return ('[ADMIN]')
            elif rank == 'MODERATOR':
                # print('Rank acquired- Moderator')
                return ('[MOD]')
            elif rank == 'HELPER':
                # print('Rank acquired- Helper')
                return ('[HELPER]')
            elif rank == 'YOUTUBER':
                # print('Rank acquired- Youtube')
                return ('[YOUTUBE]')
        if "newPackageRank" in data["player"]:
            rank = (data["player"]["newPackageRank"])
            if rank == 'MVP_PLUS':
                if "monthlyPackageRank" in data["player"]:
                    mvp_plus_plus = (data["player"]["monthlyPackageRank"])
                    if mvp_plus_plus == "NONE":
                        # print('Rank acquired- MVP+')
                        return ('[MVP+]')
                    else:
                        # print('Rank acquired- MVP+')
                        return ("[MVP++]")
                else:
                    # print('Rank acquired- MVP+')
                    return ("[MVP+]")
            elif rank == 'MVP':
                # print('Rank acquired- MVP')
                return ('[MVP]')
            elif rank == 'VIP_PLUS':
                # print('Rank acquired- VIP+')
                return ('VIP+')
            elif rank == 'VIP':
                # print('Rank acquired- VIP')
                return ('[VIP]')
        else:
            # print('Rank acquired- Non')
            return ('')

    @classmethod
    def get_key(self, key):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/key?key={key}").json()
        return data

    @classmethod
    def get_boosters(self, key):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/key?key={key}").json()
        return data

    @classmethod
    def __get_guild_id_by_name(self, key, name: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/findGuild?key={key}&byName={name}").json()
        if data["guild"] == None:
            raise InvalidGuildName
        else:
            return data["guild"]

    @classmethod
    def __get_guild_id_by_uuid(self, key, uuid):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/findGuild?key={key}&byUuid={uuid}").json()
        if data["success"] == False:
            if data["cause"] == "Malformed UUID":
                raise InvalidUUID
        else:
            return data["guild"]

    @classmethod
    def gamecount(self, key, game: str):
        # TODO Add list of valid games to documentation
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/gameCounts?key={key}").json()
        try:
            return data["games"][game.upper()]
        except KeyError:
            raise InvalidGameType

    @classmethod
    def playercount(self, key):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/playerCount?key={key}").json()
        return data["playerCount"]

    # id can be gotten from get_guild_id_by_uuid or get_guild_id_by_name
    @classmethod
    def guild(self, key, id):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/guild?key={key}&id={id}").json()
        if data["success"] == False:
            if data["cause"] == "Malformed guild ID":
                raise InvalidGuildID
        else:
            return data

    @classmethod
    def get_leaderboards(self, key, game: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/leaderboards?key={key}").json()
        try:
            return data["leaderboards"][game.upper()]
        except KeyError:
            raise InvalidGameType

    # deprecated, might not work
    @classmethod
    def player_with_name(self, key, name: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/player?key={key}&name={name}").json()
        if data["player"] == None:
            raise InvalidUsername
        else:
            return data

    @classmethod
    def player_with_uuid(self, key, uuid: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/player?key={key}&uuid={uuid}").json()
        if data["success"] == False:
            if data["cause"] == "Malformed UUID":
                raise InvalidUUID
        else:
            return data

    @classmethod
    def playerrank(self, key, name: str):
        self.__check_key(key)
        return self.__get_rank(key, name)

    @classmethod
    def status(self, key, uuid: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/status?key={key}&uuid={uuid}").json()
        if data["success"] == False:
            if data["cause"] == "Malformed UUID":
                raise InvalidUUID
        else:
            return data

    @classmethod
    def watchdog(self, key):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/watchdogstats?key={key}").json()
        return data


class skyblocksnakepixelmethods:
    @staticmethod
    def __check_key(key):
        if requests.get(f"https://api.hypixel.net/key?key={key}").json()["success"] == False:
            raise InvalidAPIKey
        else:
            return True

    @classmethod
    def currentauctionsofplayer(self, key, player: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/skyblock/auction?key={key}&player={player}").json()
        return data

    @classmethod
    def currentauctions(self, key, page: int):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={key}&page={str(page)}").json()
        if data["success"] == False:
            if data["cause"] == "Page not found":
                raise PageNumberOutOfRange
        else:
            return data

    @classmethod
    def bazaar(self, key):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={key}").json()
        return data

    @classmethod
    def profile_with_uuid(self, key, uuid: str):
        self.__check_key(key)
        data = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={key}&uuid={uuid}").json()
        if data["success"] == False:
            if data["cause"] == "Malformed UUID":
                raise InvalidUUID
        else:
            return data
