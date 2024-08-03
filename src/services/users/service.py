class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id)

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)
    
    def remove_user(self, user_id: int) -> User:
        return self.user_repository.remove_user(user_id)