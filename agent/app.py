python
app_securo.py — versão corrigida
import sqlite3

def fazer_login(usuario, senha):
    # Defesa adicional: evita entradas vazias e texto excessivo
    if not usuario or not senha:
        return "Acesso Negado."

    if len(usuario) > 64 or len(senha) > 128:
        return "Acesso Negado."

    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # NOTA: '?' são placeholders; os valores são enviados separadamente.
    # O SQLite trata o usuário como dado, nunca como SQL.
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"

    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."
    