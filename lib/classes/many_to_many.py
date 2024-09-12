class Game:
    def __init__(self, title):
        # Validation to ensure title is a string and longer than 0 characters
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string.")
        self._title = title  # Use _title to make it immutable

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Raise an exception if someone tries to change the title
        raise AttributeError("Cannot modify the title once set.")


    def results(self):
        # Return a list of all results for this game
        return [result for result in Result.all_results if result.game == self]

    def players(self):
        # Return a unique list of all players that played this game
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        # Return the average score of the player for this game
        player_results = [result.score for result in self.results() if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        return 0


class Player:
    def __init__(self, username):
        # Validate that the username is a string and between 2 and 16 characters
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self._username = value

    def results(self):
        # Return a list of all results for this player
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        # Return a unique list of all games played by the player
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        # Check if the player played a specific game
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        # Return the number of times the player played a specific game
        return sum(1 for result in self.results() if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        # Return the player with the highest average score in the game
        players = game.players()
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))

class Result:
    all_results = []  # List to track all results globally

    def __init__(self, player, game, score):
        # Validate that player is a Player instance, game is a Game instance, and score is a valid int
        if not isinstance(player, Player) or not isinstance(game, Game):
            raise Exception("Invalid player or game instance.")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise Exception("Score must be an integer between 1 and 5000.")
        self._player = player
        self._game = game
        self._score = score
        Result.all_results.append(self)  # Add this result to the global list

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
