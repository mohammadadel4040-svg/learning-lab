import sqlite3


class UserStore:

    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    # Create database + table
    def init_db(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)

        conn.commit()
        conn.close()

    # Load all users
    def load(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": r[0], "name": r[1], "email": r[2]}
            for r in rows
        ]

    # Save new user
    def save(self, users):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users")

        for user in users:
            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (user["id"],
                 user["name"],
                 user["email"])
            )

        conn.commit()
        conn.close()

    # Find user
    def find_by_id(self, user_id):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE id=?",
            (user_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }

        return None

    # Update user
    def update_user(self, user_id, updated_data):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET name=?, email=? WHERE id=?",
            (updated_data["name"],
             updated_data["email"],
             user_id)
        )

        conn.commit()
        success = cursor.rowcount > 0
        conn.close()

        return success

    # Delete user
    def delete_user(self, user_id):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id=?",
            (user_id,)
        )

        conn.commit()
        success = cursor.rowcount > 0
        conn.close()

        return success
