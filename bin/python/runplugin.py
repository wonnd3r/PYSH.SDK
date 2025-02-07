import os
import subprocess
PLUGINS_DIRECTORY = os.getenv("PLUGINS_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "plugins"))
for entry in os.listdir(PLUGINS_DIRECTORY):
    full_path = os.path.join(PLUGINS_DIRECTORY, entry)
    if os.path.isdir(full_path):
        main_py_path = os.path.join(full_path, 'main.py')
        if os.path.isfile(main_py_path):
            subprocess.run(['python3', main_py_path])
