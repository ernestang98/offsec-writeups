# Solution

Target file: `C:\path\to\slay_the_dragon\src\core\config.py`

```
from os import path

######################
#     GAME CONFIG    #
######################

# Player
BASE_ATTACK = 1000 # change this
```

Change the source code in order to send more than 1 attack point per attack command. However, we encounter an error. Set verbose to `True` to find out why.

Target file: `C:\path\to\slay_the_dragon\src\client\networking\netclient.py`

```
class NetClient:
    def __init__(self, host: str, port: int, verbose: bool = True): # change this
        self.__client = Netcat((host, port), verbose=verbose)
```

It seems that when the battle ends, the client will send a validate command and the server will validate the battle by replaying it and it replays it based on the number of ATTACK commands we have sent as the client along with the ATTACK statistics that the server has which is the unedited version. If the battle is not won properly, then the server will throw an error. 

Target file: `C:\path\to\slay_the_dragon\src\server\service\battleservice.py`

```
...
        while True:
            self.history.log_commands_from_str(self.server.recv_command_str())

            match self.history.latest:
                case Command.ATTACK | Command.HEAL:
                    self.history.log_command(Command.BOSS_ATTACK)
                case Command.VALIDATE:
                    break
                case Command.RUN:
                    return
                case _:
                    self.server.exit(1)

        match self.__compute_battle_outcome():
            case Result.PLAYER_WIN_BATTLE:
                self.__handle_battle_win()
                return
            case Result.BOSS_WIN_BATTLE:
                self.server.exit()
            case _:
                self.server.exit(1)

    def __handle_battle_win(self):
        self.server.game.remove_next_boss()
        if self.__boss_available_for_next_battle():
            self.server.send_result(Result.VALIDATED_OK)
            return
        self.server.send_result(Result.OBTAINED_FLAG)
        self.server.send_flag()
        self.server.exit()

    def __boss_available_for_next_battle(self) -> bool:
        return not (self.server.game.next_boss is None)

    def __compute_battle_outcome(self) -> Optional[Result]:
        for command in self.history.commands:
            match command:
                case Command.ATTACK:
                    self.boss.receive_attack_from(self.player)
                    if self.boss.is_dead:
                        return Result.PLAYER_WIN_BATTLE
                case Command.HEAL:
                    self.player.use_potion()
                case Command.BOSS_ATTACK:
                    self.player.receive_attack_from(self.boss)
                    if self.player.is_dead:
                        return Result.BOSS_WIN_BATTLE
        return None
```

To solve this, send more than one ATTACK command per ATTACK

Target file: `C:\path\to\slay_the_dragon\src\core\models\commands.py`

```
class Command(Enum):
    ATTACK = "ATTACK\n" * 10000 # change this
    BATTLE = "BATTLE"
```

### Flag: 

TISC{L3T5_M33T_4G41N_1N_500_Y34R5_96eef57b46a6db572c08eef5f1924bc3}

### References

1. https://dencode.com/en/

2. https://www.base64decode.org/
