import os
import subprocess

ui_directory = './ui_files/' #fix
ui_gen_directory = './ui_gen/' #fix

for file_name in os.listdir(ui_directory)
    if file_name.endswith('.ui'):
        ui_file = os.path.join(ui_directory, file_name)
        py_file = os.path.join(ui_gen_directory, file_name.replace('.ui', '.py'))
        subprocess.call(['pyuic6', '-o', py_file, ui_file])