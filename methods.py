import csv
from datetime import datetime
from docxtpl import DocxTemplate
from models import FichaMedica

# Función para normalizar el RUT y eliminar caracteres especiales
def normalize_rut(rut):
    rut = rut.replace('.', '').replace('-', '').upper()
    return rut[:-1].lstrip('0') if len(rut) > 1 else rut

# Función para obtener la fecha desde el campo "Marca temporal"
def parse_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        return datetime.min

# Cargar fichas de antiguas.csv manteniendo la ficha más reciente por cada RUT
def cargar_fichas_antiguas(archivo_antiguas):
    fichas_antiguas = {}
    with open(archivo_antiguas, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            fecha_ficha = parse_fecha(row[0])  # Marca temporal
            rut = normalize_rut(row[5].strip())  # Normalizar RUT
            
            # Almacenar solo la ficha más reciente por RUT
            if rut not in fichas_antiguas or fecha_ficha > parse_fecha(fichas_antiguas[rut][0]):
                fichas_antiguas[rut] = row
    return fichas_antiguas

# Procesar nuevas.csv y actualizar con fichas antiguas si no hubo cambios
def procesar_nuevas_y_combinar(archivo_nuevas, fichas_antiguas):
    fichas_finales = []
    with open(archivo_nuevas, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            rut = normalize_rut(row[5].strip())  # Normalizar RUT
            cambios = row[1].strip().lower()  # Respuesta sobre cambios

            # Revisar si no hay cambios en los datos y usar ficha antigua
            if rut in fichas_antiguas and 'no han habido cambios' in cambios:
                ficha_final = FichaMedica(fichas_antiguas[rut])  # Usar ficha antigua
            else:
                ficha_final = FichaMedica(row)  # Usar la nueva ficha
                fichas_antiguas[rut] = row  # Actualizar o agregar en fichas antiguas
            fichas_finales.append(ficha_final)
    
    # Eliminar duplicados de la lista final usando RUT como clave
    fichas_unicas = {normalize_rut(ficha.rut): ficha for ficha in fichas_finales}
    return list(fichas_unicas.values())

# Generar documento final a partir de las fichas procesadas
def generar_documento(fichas, template_path='template.docx', output_path='Fichas Médicas.docx'):
    doc = DocxTemplate(template_path)
    context = {'fichas': fichas}
    doc.render(context)
    doc.save(output_path)
    print(f'Documento guardado en {output_path}: fichas médicas generadas = {len(fichas)}')