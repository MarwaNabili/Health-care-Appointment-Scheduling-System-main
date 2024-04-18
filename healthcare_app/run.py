from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """ Create and return a database connection """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",  # It's safer to use an environment variable for the password
            database="healthcare"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

@app.route('/data')
def index():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM some_table")
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return str(data)
        except mysql.connector.Error as err:
            print(f"SQL Error: {err}")
            return "Database query failed", 500
    else:
        return "Failed to connect to the database", 500
    
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
