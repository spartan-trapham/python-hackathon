from src.entities.users import User
from src.entities.roles import Role
class UserRepository:
    def __init__(self, user: User, role: Role):
        self.user = user
        self.role = role

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def remove_user(self, user_id: int) -> User:
        user = self.get_user(user_id)
        self.db.delete(user)
        self.db.commit()
        return user