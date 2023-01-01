import csv
from docxtpl import DocxTemplate

from models import FichaMedica

if __name__ == '__main__':
    input_csv = f'Fichas Médicas 2022.csv'
    input_delimitador = ','

    fichas = []
    ruts = []
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=input_delimitador)
        next(reader)
        for row in reader:
            f = FichaMedica(row)
            if f.rut in ruts:
                # replace for newer entrance
                index = ruts.index(f.rut)
                fichas[index] = f
            else:
                fichas.append(f)
                ruts.append(f.rut)

    fichas.sort(key=lambda x: (x.unidad, x.apellido_paterno))
    doc = DocxTemplate('template.docx')
    context = {'fichas': fichas}
    doc.render(context)
    doc.save('Fichas Médicas 2022.docx')
