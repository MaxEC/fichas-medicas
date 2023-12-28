from datetime import date
# from rut_chile import rut_chile


class FichaMedica():
    def __init__(self, row):
        # Info personal
        self.unidad = row[0].upper()
        self.nombre = ' '.join(row[1].split()).title()
        self.apellido_paterno = ' '.join(row[2].split()).title()
        self.apellido_materno = ' '.join(row[3].split()).title()
        self.rut = row[4].strip()
        self.fecha_de_nacimiento = row[5]
        self.domicilio = row[6].title()
        self.sistema_de_salud = row[7].title()
        self.seguro = row[8].title()

        # Info de contacto
        self.nombre_y_apellido_1 = ' '.join(row[9].split()).title()
        self.relacion_1 = row[10]
        self.numero_1 = row[11]
        self.email_1 = row[12].lower()
        self.nombre_y_apellido_2 = ' '.join(row[13].split())
        self.relacion_2 = row[14]
        self.numero_2 = row[15]
        self.email_2 = row[16].lower()

        # Antecedentes médicos
        self.grupo_sanguineo = row[17]
        self.alergias_alimenticias = ' '.join(row[18].split()).capitalize()
        self.alergias_medicamentos = ' '.join(row[19].split()).capitalize()
        self.alergias_plantas_o_insectos = ' '.join(
            row[20].split()).capitalize()
        self.enfermedades_cronicas = ' '.join(row[21].split()).capitalize()
        self.enfermedades_pasadas = ' '.join(row[22].split()).capitalize()
        self.condicion_extra = ' '.join(row[23].split()).capitalize()
        self.operaciones = ' '.join(row[24].split()).capitalize()
        self.esquema_covid = ' '.join(row[25].split())

        # Medicamentos actuales
        self.medicamentos_actuales = ' '.join(row[26].split()).capitalize()
        self.medicamentos_sos = ' '.join(row[27].split()).capitalize()
        self.medicamentos_urgente = ' '.join(row[28].split()).capitalize()
        self.obs = ' '.join(row[29].split()).capitalize()
