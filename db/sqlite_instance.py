import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('/app/data/my_database.db') 
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(f'The error {e} occurred')
    return conn


def main():
    connection = create_connection()

if __name__ == '__main__':
    main()