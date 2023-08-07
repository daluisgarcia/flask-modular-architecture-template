from werkzeug.security import check_password_hash, generate_password_hash

from core import AppRepository
from core.auth.models import User


class UserRepository(AppRepository):

    def __hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def __check_passwords(self, password_stored: str, password_input: str) -> bool:
        return check_password_hash(password_stored, password_input)

    def get_all_users_for_form(self) -> list:
        users = User.query.all()
        return [(user.id, user.username) for user in users]

    def get_user_by_id(self, user_id: int) -> User:
        return User.query.get(user_id)

    def login_user(self, username: str, password: str) -> User | None:
        user = User.query.filter_by(username=username).first()

        if user is None or not self.__check_passwords(user.password, password):
            return None

        return user

    def register_user(self, username: str, password: str) -> User | None:
        user = User(username=username, password=self.__hash_password(password))
        self.commit(user)
        self.close_session()
        return user
