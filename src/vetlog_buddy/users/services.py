from vetlog_buddy.users.repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository, factor: float = 0.5) -> None:
        self.repo = repo
        self.factor = factor

    def is_invalid(self, user) -> bool:
        """Check if user is invalid using logic from filter_username"""
        # alias username
        username = user.username
        if not username:
            # empty string
            return True
        if username.isupper():
            # all uppercase
            return True
        if len(username) < 5:
            # too short
            return True
        if user.uppercase_ratio < self.factor:
            # too many uppercase
            return True
        return False

    def remove_invalid(self) -> int:
        """Remove invalid users from the DB, return count"""
        all_users = self.repo.get_all()
        invalid_users = [u for u in all_users if self.is_invalid(u)]
        count = 0
        for user in invalid_users:
            self.repo.delete(user)
            count += 1
        print(f"Removed {count} invalid users")
        return count

    def is_suspicious(self, user) -> bool:
        """Check if user is suspicious using logic from suspicious_username"""
        ratio = user.uppercase_ratio
        return 0.2 < ratio <= 0.5

    def list_suspicious(self) -> list:
        all_users = self.repo.get_all()
        suspicious_users = [u for u in all_users if self.is_suspicious(u)]
        count = len(suspicious_users)
        print(f"Found {count} suspicious users")
        # return count
        return suspicious_users
