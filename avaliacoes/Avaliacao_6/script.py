import mysql.connector

conexao = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        user='gustavo',
        password='bd_rules',
        database='BD'
    )
cursor = conexao.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100)
        )
    """)

cursor.execute("INSERT INTO games (nome) VALUES ('Hollow Knight')")
cursor.execute("INSERT INTO games (nome) VALUES ('ULTRAKILL')")
conexao.commit()

cursor.execute("SELECT * FROM games")
for row in cursor.fetchall():
    print(row)

cursor.close()
conexao.close()