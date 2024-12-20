from .db import db
import hashlib

class UserDAL:
    @staticmethod
    def create_user(username, password, role, position=None, department=None):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        sql = """
            INSERT INTO users (username, password, role, position, department)
            VALUES (%s, %s, %s, %s, %s)
        """
        return db.execute(sql, (username, hashed_password, role, position, department))

    @staticmethod
    def get_user_by_username(username):
        sql = "SELECT * FROM users WHERE username = %s"
        return db.fetch_one(sql, (username,))

    @staticmethod
    def verify_password(username, password):
        user = UserDAL.get_user_by_username(username)
        if not user:
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return user['password'] == hashed_password

    @staticmethod
    def get_all_users():
        sql = "SELECT id, username, role, position, department, created_at FROM users"
        return db.fetch_all(sql)

    @staticmethod
    def update_user(user_id, data):
        fields = []
        values = []
        for key, value in data.items():
            if key != 'id' and key != 'password':
                fields.append(f"{key} = %s")
                values.append(value)
        
        if 'password' in data:
            fields.append("password = %s")
            hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
            values.append(hashed_password)
        
        values.append(user_id)
        sql = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
        return db.execute(sql, tuple(values))

    @staticmethod
    def delete_user(user_id):
        sql = "DELETE FROM users WHERE id = %s"
        return db.execute(sql, (user_id,)) 