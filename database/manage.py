import psycopg2 as psql


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='project_internet_magazin',
            user='postgres',
            password='muty82ball',
            host='localhost',
            port='5432'
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'update', "insert", 'alter']
        if query_type in data:
            db.commit()
            if query_type == "create":
                return f"created successfull"
            return f"{query_type} query successfull"
        else:
            return cursor.fetchall()

class Check:
    @staticmethod
    def login_check(username: str, password: str):
        query = f"SELECT * FROM customers WHERE username = '{username}' and password = '{password}'"
        data = Database.connect(query, "select")
        if len(data) == 1:
            return True

        else:
            return False


def add_column():
    query = f"""
            INSERT INTO customers(first_name, last_name, username, password, birth_date) 
            VALUES('Mustafo', 'Aliyev', 'mustafo12', 'mustafo4530', '2002-02-14')"""
    return Database.connect(query, "insert")
