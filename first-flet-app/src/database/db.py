import pymysql
from pymysql.cursors import DictCursor
from .config import DB_CONFIG

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        if not self.conn:
            self.conn = pymysql.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                database=DB_CONFIG['database'],
                port=DB_CONFIG['port'],
                charset=DB_CONFIG['charset'],
                cursorclass=DictCursor
            )
            self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.conn = None
        self.cursor = None

    def execute(self, sql, params=None):
        try:
            self.connect()
            self.cursor.execute(sql, params or ())
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            self.conn.rollback()
            raise e

    def fetch_one(self, sql, params=None):
        try:
            self.connect()
            self.cursor.execute(sql, params or ())
            return self.cursor.fetchone()
        except Exception as e:
            raise e

    def fetch_all(self, sql, params=None):
        try:
            self.connect()
            self.cursor.execute(sql, params or ())
            return self.cursor.fetchall()
        except Exception as e:
            raise e

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# 创建全局数据库实例
db = Database() 