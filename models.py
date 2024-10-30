from datetime import date
# from rut_chile import rut_chile

class FichaMedica():
    def __init__(self, row):
        # Info personal
        self.unidad = ''
        self.nombre = ' '.join(row[2].split()).title()
        self.apellido_paterno = ' '.join(row[3].split()).title()
        self.apellido_materno = ' '.join(row[4].split()).title()
        self.rut = row[5].strip()
        self.fecha_de_nacimiento = row[6]
        self.domicilio = row[7].title()
        self.sistema_de_salud = row[8].title()
        self.seguro = row[9].title()

        # Info de contacto
        self.nombre_y_apellido_1 = ' '.join(row[10].split()).title()
        self.relacion_1 = row[11]
        self.numero_1 = row[12]
        self.email_1 = row[13].lower()
        self.nombre_y_apellido_2 = ' '.join(row[14].split())
        self.relacion_2 = row[15]
        self.numero_2 = row[16]
        self.email_2 = row[17].lower()

        # Antecedentes médicos
        self.grupo_sanguineo = row[18]
        self.alergias_alimenticias = ' '.join(row[19].split()).capitalize()
        self.alergias_medicamentos = ' '.join(row[20].split()).capitalize()
        self.alergias_plantas_o_insectos = ' '.join(
            row[21].split()).capitalize()
        self.enfermedades_cronicas = ' '.join(row[22].split()).capitalize()
        self.enfermedades_pasadas = ' '.join(row[23].split()).capitalize()
        self.condicion_extra = ' '.join(row[24].split()).capitalize()
        self.operaciones = ' '.join(row[25].split()).capitalize()
        self.esquema_covid = ' '.join(row[26].split())

        # Medicamentos actuales
        self.medicamentos_actuales = ' '.join(row[27].split()).capitalize()
        self.medicamentos_sos = ' '.join(row[28].split()).capitalize()
        self.medicamentos_urgente = ' '.join(row[29].split()).capitalize()
        self.obs = ' '.join(row[30].split()).capitalize()
