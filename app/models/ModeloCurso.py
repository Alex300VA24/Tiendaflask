from .entities.Profesor import Profesor
from .entities.Curso import Curso

class ModeloCurso():
    
    @classmethod
    def listar_cursos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT CUR.id, CUR.titulo, CUR.anoedicion, CUR.precio,
                PROF.apellidos, PROF.nombres, PROF.titulo
                FROM curso CUR JOIN profesor PROF ON CUR.profesor_id = PROF.id
                ORDER BY CUR.titulo ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            cursos = []
            for row in data:
                prof = Profesor(0, row[4], row[5], row[6])
                cur = Curso(row[0], row[1], prof, row[2], row[3])
                cursos.append(cur)
            return cursos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def leer_curso(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, titulo, anoedicion, precio
                    FROM curso WHERE id = '{0}'""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            curso = Curso(data[0], data[1], None, data[2], data[3])
            return curso
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def listar_cursos_vendidos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT COM.curso_id, CUR.titulo, CUR.precio,
                     COUNT(COM.curso_id) AS Unidades_Vendidas
                     FROM compra COM JOIN curso CUR ON COM.curso_id = CUR.id
                     GROUP BY COM.curso_id ORDER BY 4 DESC, 2 ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            cursos = []
            for row in data :
                cur = Curso(row[0], row[1], None, None, row[2])
                cur.unidades_vendidas = int(row[3])
                cursos.append(cur)
            return cursos
        except Exception as ex:
            raise Exception(ex)