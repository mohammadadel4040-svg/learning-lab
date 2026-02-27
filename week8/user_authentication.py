# Week 8 - Secure User Authentication System
# This week is Object-Oriented Programming and Encapsulation

from datetime import datetime


class User:

    def __init__(self, username, password, privilege_level="standard"):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__privilege_level = privilege_level
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []

    # private password hashing
    def __hash_password(self, password):
        return f"hashed_{password}"

    # authentication method
    def authenticate(self, password):

        if self.__account_status == "locked":
            self.__log_activity("Login attempt on locked account")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.__login_attempts = 0
            self.__log_activity("Successful login")
            return True
        else:
            self.__login_attempts += 1
            self.__log_activity(
                f"Failed login attempt {self.__login_attempts}"
            )

            if self.__login_attempts >= 3:
                self.lock_account()

            return False

    def check_privileges(self, required_level):

        hierarchy = {"guest": 0, "standard": 1, "admin": 2}

        return hierarchy.get(
            self.__privilege_level, 0
        ) >= hierarchy.get(required_level, 0)

    def lock_account(self):
        self.__account_status = "locked"
        self.__log_activity("Account locked")

    def reset_login_attempts(self):
        self.__login_attempts = 0
        self.__account_status = "active"

    def __log_activity(self, message):
        self.__activity_log.append(
            f"{datetime.now()} - {message}"
        )

    # Safe public info
    def get_safe_info(self):
        return {
            "username": self.__username,
            "privilege": self.__privilege_level,
            "status": self.__account_status
        }
