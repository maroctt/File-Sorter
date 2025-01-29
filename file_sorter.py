def sort_files():
    import os, shutil
    path =f'{input("Ingrese la ruta de la carpeta que desea ordenar: ")}/'
    if not os.path.exists(path):
        print('La ruta indicada no existe')
        return

    num = int(input("Ingrese el número de carpetas que desea crear"))
    folder_map = {}

    for i in range(num):
        nombre = input(f"Ingrese el nombre de la carpeta {i}: ")
        formato = input(f"Ingrese el formato de archivo de la carpeta {nombre} (imagen, texto, csv): ")

        if formato == "imagen":
            extensiones = ['.png', '.jpeg', '.jpg']
        elif formato == "texto":
            extensiones = ['.pdf', '.txt']
        elif formato == "csv":
            extensiones = ['.csv']

        folder_map[nombre] = extensiones

        print(f'Carpeta "{nombre}" creada. En ella irán archivos con extensiones: {", ".join(extensiones)}')

    file_names = os.listdir(path)

    for folder in folder_map.keys():
        if not os.path.exists(path + folder):
            os.makedirs(path + folder)


    for file in file_names:
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):  
            continue
    
        for folder, extensions in folder_map.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(path, folder, file))
                    print(f'Movido: {file} → {folder}')
                      
    print('\n✅ Su carpeta ha sido organizada 🧹')
