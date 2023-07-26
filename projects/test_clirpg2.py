import clirpg2
import requests

class TestlClirpg2:
    user_name = "Mark"
    name_length = 5

    # def test_get_user_name(monkeypatch):

    # # monkeypatch the "input" function, so that it returns "Mark".
    # # This simulates the user entering "Mark" in the terminal:
    #     monkeypatch.setattr('builtins.input', lambda : 'Mark')

    # # go about using input() like you normally would:
    #     i = input("What is your name?")
    #     assert i == "Mark"


    def test_get_user_name_len (self):
        result = clirpg2.get_user_name_len(self.user_name)
        assert type(result) == int

    def test_make_url_for_getting_a_random_name(self):
        url = clirpg2.make_url_for_getting_a_random_name(self.name_length)
        page = requests.get(url)
        assert page.status_code == 200

    def test_get_user_game_name(self):
        url = clirpg2.make_url_for_getting_a_random_name(self.name_length)
        new_user_name = clirpg2.get_user_game_name(url)
        assert type(new_user_name) == str

    