from src.app import app
from src.models import create_table, connection



if __name__ == '__main__':
    conn = connection()
    create_table(conn)
    app.run(debug=True, port= 5000)