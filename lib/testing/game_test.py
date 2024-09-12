class Game:
    def __init__(self, title):
        # Ensure title is a non-empty string
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string.")
        self._title = title  # Make title immutable by using a private variable

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
        # Return a unique list of all players who played this game
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        # Calculate the average score for a player in this game
        player_results = [result.score for result in self.results() if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        return 0


class Player:
    def __init__(self, username):
        # Ensure username is a valid string and between 2 and 16 characters
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        # Ensure username is between 2 and 16 characters
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self._username = value


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        # Ensure username is between 2 and 16 characters
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self._username = value

    def results(self):
        # Return a list of all results for this player
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        # Return a unique list of all games this player has played
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        # Check if the player has played a specific game
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        # Return the number of times the player played a specific game
        return sum(1 for result in self.results() if result.game == game)


class Result:
    all_results = []  # Global list to track all results

    def __init__(self, player, game, score):
        # Ensure player is an instance of Player, game is an instance of Game, and score is valid
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
