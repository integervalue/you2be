import sqlite3

def create_database():
    #Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('database/you2be.db')
    cursor = conn.cursor()

    #Read the schema.sql file
    with open('database/schema.sql', 'r') as schema_file:
        schema_sql = schema_file.read()

    #Execute the SQL statements in the schema.sql file
    cursor.executescript(schema_sql)

    #Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
