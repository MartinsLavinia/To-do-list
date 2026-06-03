from dotenv import load_dotenv
import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

load_dotenv()

def criar_nota(titulo, conteudo):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
        INSERT INTO notas (not_titulo, not_conteudo)
        VALUES (%s, %s)
    """

    cursor.execute(sql, (titulo, conteudo))

    conn.commit()

    cursor.close()
    conn.close()

def listar_notas():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM notas"

    cursor.execute(sql)

    notas = cursor.fetchall()

    cursor.close()
    conn.close()

    return notas 

def buscar_nota(id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM notas WHERE not_id = %s"

    cursor.execute(sql, (id,))

    nota = cursor.fetchone()

    cursor.close()
    conn.close()

    return nota

def update_nota(id, titulo, conteudo):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
        UPDATE notas
        SET not_titulo = %s,
            not_conteudo = %s
        WHERE not_id = %s
    """

    cursor.execute(sql, (titulo, conteudo, id))

    conn.commit()

    cursor.close()
    conn.close()

def excluir_nota(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM notas WHERE not_id = %s",
        (id,)
    )

    conn.commit()