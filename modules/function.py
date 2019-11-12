import os
import shutil
import platform


def dir_create():
    dir_name = input('Укажите имя директории: ')
    temp_dir = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(temp_dir):
        while os.path.exists(temp_dir):
            print("Директория с таким имененем существует, укажите другое имя")
            dir_name = input('Укажите имя директории: ')
            temp_dir = os.path.join(os.getcwd(), dir_name)

    os.mkdir(temp_dir)
    print("Директория создана")

def dir_file_remove():
    while True:
        object_name = input('Укажите имя файла или директории: \n ')
        full_object_name = os.path.join(os.getcwd(), object_name)
        if os.path.exists(full_object_name):
            if os.path.isfile(full_object_name):
                try:
                    os.remove(full_object_name)
                    print("Файл удалён")
                    break
                except FileNotFoundError:
                    print('Системе не удается найти указанный файл')
                    continue
            try:
                shutil.rmtree(full_object_name)
                print('Директория удалена')
                break
            except FileNotFoundError:
                print('Системе не удается найти указанный путь')
        print('Системе не удается найти указанный путь, введите корректный путь:\n')


def dir_file_copy():
    while True:
        full_src_path = input('Укажите полный путь что копировать: \n')
        full_dst_path = input('Укажите полный путь куда копировать включая новое имя файла или папки: \n')
        if full_src_path == full_dst_path:
            print('Источник совпадает с назначением, повторите ввод:')
            continue

        if not os.path.exists(full_src_path):
            print('Источник для копирования не найден')
            continue

        if os.path.isfile(full_src_path):
            shutil.copy2(full_src_path, full_dst_path)
            print("Файл скопирован")
            break

        try:
            shutil.copytree(full_src_path, full_dst_path)
            print("Директория скопирована")
            break
        except FileNotFoundError:
            print('Системе не удается найти указанный путь')


def list_files_and_dirs():
    print('----------------Директории-------------------')
    list_dirs()
    print('------------------Файлы----------------------')
    list_files()

def list_dirs():
    for path in os.listdir(os.getcwd()):
        if not os.path.isfile(path):
            print(path)

def list_files():
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), file)):
            print(file)

def watch_os_info():
    print("Операционная система: ", platform.system(), platform.release(), platform.machine())

def about_creator():
    print('Created_by_iliak2')

