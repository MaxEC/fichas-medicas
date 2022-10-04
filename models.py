from datetime import date

class FichaMedica():
    def __init__(self, row):
        # Info personal
        self.unidad = 'Lobatxs'
        self.nombre = ' '.join(row[1].split())
        self.apellido_paterno = ' '.join(row[2].split())
        self.apellido_materno = ' '.join(row[3].split())
        self.rut = row[4]
        self.fecha_de_nacimiento = date.fromisoformat(row[5]).strftime('dd/mm/yyyy')
        self.domicilio = row[6]
        self.sistema_de_salud = row[7]
        self.seguro = row[8]
        
        # Info de contacto
        self.nombre_y_apellido_1 = ' '.join(row[9].split())
        self.relacion_1 = row[10]
        self.numero_1 = row[11]
        self.email_1 = row[12]
        self.nombre_y_apellido_2 = ' '.join(row[13].split())
        self.relacion_2 = row[14]
        self.numero_2 = row[15]
        self.email_2 = row[16]
        
        # Antecedentes médicos
        self.grupo_sanguineo = row[17]
        self.alergias_alimenticias = ' '.join(row[18].split())
        self.alergias_medicamentos = ' '.join(row[19].split())
        self.alergias_plantas_o_insectos = ' '.join(row[20].split())
        self.enfermedades_cronicas = ' '.join(row[21].split())
        self.enfermedades_pasadas = ' '.join(row[22].split())
        self.operaciones = ' '.join(row[23].split())
        self.esquema_covid = ' '.join(row[24].split())
        
        # Medicamentos actuales
        self.medicamentos_actuales = ' '.join(row[25].split())
        self.medicamentos_sos = ' '.join(row[26].split())
        self.obs = ' '.join(row[27].split())
        