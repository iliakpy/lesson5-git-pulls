import leonid_funcs

def test_author_info():
    assert leonid_funcs.author_info() == 'Leonid Orlov'

def test_separator():
    assert leonid_funcs.separator(5)=="*****"

def test_is_correct_choice():
    menu_items=('Пункт_1', 'Пункт_2','Пункт_3','Пункт_4','Пункт_5','Пункт_6','Пункт_7',)
    assert leonid_funcs.is_correct_choice('5', menu_items)==True

#Грязная функция

#def test_filenames():
#    assert leonid_funcs.filenames() == ['.gitignore', 'modules.function.py', 'modules.function.py, 'new.py', 'other.py', 'filemanager.py', 'leonid_funcs.py', 'LICENSE', 'main_menu.py', 'task.txt', 'test.py', 'test_filemanager.py', 'test_python.py', 'victory.py']


