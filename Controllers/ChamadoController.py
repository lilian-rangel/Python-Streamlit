from typing import List
import services.database as db
import models.Chamado as chamado

def IncluirChamado(chamado):
    count = db.cursor.execute("""
    INSERT INTO Chamados (cliName, cliEnviroment, cliPriority, cliDescription) 
    VALUES (?,?,?,?)""",
    chamado.name, chamado.enviroment, chamado.priority, chamado.description).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM CHAMADOS")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(chamado.Chamados(row[0], row[1], row[2], row[3], row[4]))
    
    return costumerList

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM Chamados WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()