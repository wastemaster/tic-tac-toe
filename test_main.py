""" Main Tests """
from starlette.testclient import TestClient
import numpy as np
from main import app
from models import PlayerEnum

client = TestClient(app)


def make_move(player, x_position, y_position):
    """ Helper function to make a move """
    response = client.post(
        "/move/",
        json={"player": player, "location": [x_position, y_position]},
    )
    return response


def test_read_main():
    """ Test index response code """
    response = client.get("/")
    assert response.status_code == 200


def test_board_api():
    """ Test board response code """
    response = client.get("/board")
    assert response.status_code == 200


def test_reset_api_code():
    """ Test reset response code """
    response = client.get("/reset")
    assert response.status_code == 200


def test_reset_api_json_winner():
    """ board winner after reset is none """
    response = client.get("/reset")
    assert response.json()['winner'] is None


def test_initial_board_api_json_winner():
    """ board winner after reset is none """
    client.get("/reset")

    response = client.get("/board")
    assert response.json()['winner'] is None


def test_reset_api_json_board():
    """ board state after reset """
    response = client.get("/reset")
    board = np.array(response.json()['board'])
    assert np.all(board == '_')


def test_board_after_reset_api():
    """ board state after reset is also empty """
    client.get("/reset")
    response2 = client.get("/reset")

    board = np.array(response2.json()['board'])
    assert np.all(board == '_')


def test_make_two_moves_same_place():
    """ it is not allowed to occupy cell that is already occupied """
    # reset board
    reset_response = client.get("/reset/")
    assert reset_response.status_code == 200

    # move 1
    response1 = make_move(PlayerEnum.NAUGHT, 0, 0)
    assert response1.status_code == 200

    # move 2 at same position
    response2 = make_move(PlayerEnum.CROSS, 0, 0)

    assert response2.status_code == 400


def test_cross_can_start_game():
    """ X can start game """
    # reset board
    reset_response = client.get("/reset")
    assert reset_response.status_code == 200

    # move 1
    response1 = make_move(PlayerEnum.CROSS, 0, 0)
    assert response1.status_code == 200


def test_naught_can_start_game():
    """ O can start game """
    # reset board
    client.get("/reset")

    # move 1
    response2 = make_move(PlayerEnum.NAUGHT, 0, 0)
    assert response2.status_code == 200


def test_cross_cannot_make_two_moves():
    """ X cannot make two moves one after another """
    # reset board
    client.get("/reset")

    # move 1
    response1 = make_move(PlayerEnum.CROSS, 0, 0)
    assert response1.status_code == 200

    # move 2
    response2 = make_move(PlayerEnum.CROSS, 0, 1)
    assert response2.status_code == 400


def test_naught_cannot_make_two_moves():
    """ Y cannot make two moves one after another """
    # reset board
    client.get("/reset")

    # move 1
    response = make_move(PlayerEnum.NAUGHT, 0, 0)
    assert response.status_code == 200

    # move 2
    response2 = make_move(PlayerEnum.NAUGHT, 0, 1)
    assert response2.status_code == 400
