import os 
# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, __file__) 
print(file_path)