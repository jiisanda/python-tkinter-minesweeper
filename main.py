from zero import ZeroClient

from bands import RegisteredPlayer
from server import fetch_player_count, window

ZERO_CLIENT = ZeroClient("localhost", 5559)


def register_player():
    resp = ZERO_CLIENT.call("register_player", None, return_type=RegisteredPlayer)
    return resp.is_registered
    # If player is registered and players count is true then we start the game


if __name__ == '__main__':

    player_registered = register_player()
    if player_registered and fetch_player_count() == 2:
        window.mainloop()



