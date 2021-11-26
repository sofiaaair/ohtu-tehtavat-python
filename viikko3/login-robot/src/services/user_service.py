from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        exist = self._user_repository.find_by_username(username)

        if self.validate(username, password) and not exist:
            user = self._user_repository.create(
                User(username, password)
            )
            return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise AuthenticationError("Username must contain at least 3 characters")

        user = user = self._user_repository.find_by_username(username)
        if user:
            raise AuthenticationError("Username already exist")

        if not re.match("^[a-z]+$", username):
            raise AuthenticationError("Username must contain characters a-z")

        if len(password) < 8:
            raise AuthenticationError("Password must contain at least 8 characters")

        if re.search('[0-9]',password) is  None:
            raise AuthenticationError("Password must contain numbers")

        return True
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


