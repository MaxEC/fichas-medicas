from methods import cargar_fichas_antiguas, procesar_nuevas_y_combinar, generar_documento

if __name__ == '__main__':
    archivo_antiguas = 'FICHAS ANTIGUAS.csv'
    archivo_nuevas = 'FICHAS NUEVAS.csv'
    
    # Cargar fichas de antiguas.csv
    fichas_antiguas = cargar_fichas_antiguas(archivo_antiguas)
    
    # Procesar nuevas.csv y combinar datos
    fichas_finales = procesar_nuevas_y_combinar(archivo_nuevas, fichas_antiguas)
    
    # Generar documento final
    generar_documento(fichas_finales)