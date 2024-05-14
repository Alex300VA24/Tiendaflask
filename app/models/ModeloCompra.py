from .entities.Curso import Curso
from .entities.Compra import Compra


class ModeloCompra():
    @classmethod
    def registrar_compra(self, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO compra (uuid, curso_id, usuario_id)
                        VALUES (uuid(), '{0}', {1})""".format(compra.curso.id, compra.usuario.id)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def listar_compras_usuario(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT COM.fecha, CUR.id, CUR.titulo, CUR.precio
                     FROM compra COM JOIN curso CUR ON COM.curso_id = CUR.id
                     WHERE COM.usuario_id = {0}""".format(usuario.id)
            cursor.execute(sql)
            data = cursor.fetchall()
            compras = []
            for row in data :
                cur = Curso(row[1], row[2], None, None, row[3])
                com = Compra(None, cur, usuario, row[0])
                compras.append(com)
            return compras
        except Exception as ex:
            raise Exception(ex)