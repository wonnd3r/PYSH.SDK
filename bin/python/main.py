import os
import sys
import shutil
import webbrowser
import time
import subprocess
import requests
import zipfile
from pathlib import Path
subprocess.run(["python3", "runplugin.py"])
clear = lambda: os.system('clear')
spinner = "\|/-"
SDK_DIRECTORY = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1"))
PLUGINS_DIRECTORY = os.getenv("PLUGINS_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "plugins"))
desktop_path = os.path.join(os.getenv("HOME"), "Desktop")
TEMPLATE1 = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "resources", "templates", "1"))
TEMPLATE2 = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "resources", "templates", "2"))
TEMPLATE3 = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "resources", "templates", "3"))
TEMPLATE4 = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "resources", "templates", "4"))
TEMPLATE5 = os.getenv("SDK_DIRECTORY", os.path.join(os.getenv("HOME"), "pysh-v0.0.1", "resources", "templates", "5"))
clear()
def title():
    print("\033[33m ______   __  __     ______     __  __     ______     _____     __  __")
    print("/\\  ==  \\/\\ \\_\\ \\   /\\  ___\\   /\\ \\_\\ \\   /\\  ___\\   /\\  __-.  /\\ \\/ /")
    print("\\ \\  _-/ \\ \\____ \\  \\ \\___  \\  \\ \\  __ \\  \\ \\___  \\  \\ \\ \\/\\ \\ \\ \\  _!-.")
    print(" \\ \\_\\    \\/\\_____\\  \\/\\_____\\  \\ \\_\\ \\_\\  \\/\\_____\\  \\ \\____-  \\ \\_\\ \\_\\")
    print("  \\/_/     \\/_____/   \\/_____/   \\/_/\\/_/   \\/_____/   \\/____/   \\/_/\\/_/ ")
    print("\033[0m\n")
def generate_template():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("GENERATE TEMPLATE:")
    print("\n")
    print("[1] BASIC TEMPLATE")
    print("[2] GUI TEMPLATE")
    print("[3] GAME TEMPLATE")
    print("[4] DATA BASE TEMPLATE")
    print("[5] CHATBOT TEMPLATE")
    print("[6] BACK")
    print("\n")
    while True:
        try: # Generate template
            choice = int(input("Select an option: "))
            if 1 <= choice <= 6:
                if choice == 1:
                    base_name = "PYSH_BASIC_TEMPLATE"
                    destination_path = os.path.join(desktop_path, base_name)
                    copy_count = 0
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(desktop_path, f"{base_name}_COPY{'_COPY' * copy_count}")
                        copy_count += 1
                    shutil.copytree(TEMPLATE1, destination_path)
                    time.sleep(1.5)
                    generate_template()
                if choice == 2:
                    base_name = "PYSH_GUI_TEMPLATE"
                    destination_path = os.path.join(desktop_path, base_name)
                    copy_count = 0
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(desktop_path, f"{base_name}_COPY{'_COPY' * copy_count}")
                        copy_count += 1
                    shutil.copytree(TEMPLATE2, destination_path)
                    time.sleep(1.5)
                    generate_template()
                if choice == 3:
                    base_name = "PYSH_GAME_TEMPLATE"
                    destination_path = os.path.join(desktop_path, base_name)
                    copy_count = 0
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(desktop_path, f"{base_name}_COPY{'_COPY' * copy_count}")
                        copy_count += 1
                    shutil.copytree(TEMPLATE3, destination_path)
                    time.sleep(1.5)
                    generate_template()
                if choice == 4:
                    base_name = "PYSH_DATA_BASE_TEMPLATE"
                    destination_path = os.path.join(desktop_path, base_name)
                    copy_count = 0
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(desktop_path, f"{base_name}_COPY{'_COPY' * copy_count}")
                        copy_count += 1
                    shutil.copytree(TEMPLATE4, destination_path)
                    time.sleep(1.5)
                    generate_template()
                if choice == 5:
                    base_name = "PYSH_CHATBOT_TEMPLATE5"
                    destination_path = os.path.join(desktop_path, base_name)
                    copy_count = 0
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(desktop_path, f"{base_name}_COPY{'_COPY' * copy_count}")
                        copy_count += 1
                    shutil.copytree(TEMPLATE5, destination_path)
                    time.sleep(1.5)
                    generate_template()
                if choice == 6:
                    menu()
            else:
                print(f"Please enter a number between 1 and 5.")
                time.sleep(1.5)
                generate_template()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            generate_template()
def generate_task():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("GENERATE TASK:")
    print("\n")
    print("[1] TASK 1       [11] TASK 11        [21] TASK 21")
    print("[2] TASK 2       [12] TASK 12        [22] TASK 22")
    print("[3] TASK 3       [13] TASK 13        [23] TASK 23")
    print("[4] TASK 4       [14] TASK 14        [24] TASK 24")
    print("[5] TASK 5       [15] TASK 15        [25] TASK 25")
    print("[6] TASK 6       [16] TASK 16        [26] TASK 26")
    print("[7] TASK 7       [17] TASK 17        [27] TASK 27")
    print("[8] TASK 8       [18] TASK 18        [28] TASK 28")
    print("[9] TASK 9       [19] TASK 19        [29] TASK 29")
    print("[10] TASK 10     [20] TASK 20        [30] TASK 30        [31] BACK")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 31:
                if choice == 31:
                    menu()
            else:
                print(f"Please enter a number between 1 and 30.")
                time.sleep(1.5)
                generate_task()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            generate_task()
def about():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("ABOUT:")
    print("\n")
    print("This SDK was created to help new programmers invent, create, and share.")
    print("It has not been an easy project; it has truly taken many hours of work.")
    print("You can find all the code and usage instructions on GitHub.")
    print("\n")
    print("Developed by wonnd3r")
    print("License GPL-3.0")
    print("\n")
    print("[1] BACK")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 1:
                menu()
            else:
                print(f"Please enter 1 to go back")
                time.sleep(1.5)
                about()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            about()
def credits():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("CREDITS:")
    print("\n")
    print("Developed by wonnd3r")
    print("License GPL-3.0")
    print("\n")
    print("[1] BACK")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 1:
                menu()
            else:
                print(f"Please enter 1 to go back")
                time.sleep(1.5)
                credits()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            credits()
def plugins():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("PLUGINS YOU HAVE INSTALLED:")
    print("\n")
    for entry in os.listdir(PLUGINS_DIRECTORY):
        full_path = os.path.join(PLUGINS_DIRECTORY, entry)
        if os.path.isdir(full_path):
            main_py_path = os.path.join(full_path, 'main.py')
            if os.path.isfile(main_py_path):
                print(entry)
    print("\n")
    print("[1] BACK")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 1:
                more()
            else:
                print(f"Please enter 1 to go back")
                time.sleep(1.5)
                plugins()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            plugins()
def uninstall():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("ARE YOU SURE YOU WANT TO UNINSTALL PYSH?")
    print("\n")
    print("[1] YES")
    print("[2] NO")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 2:
                if choice == 1:
                    uninstall2()
                if choice == 2:
                    menu()
            else:
                print(f"Please enter a number between 1 and 2.")
                time.sleep(1.5)
                uninstall()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            uninstall()
def uninstall2():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    while True:
        try:
            choice = str(input("Type sudo code: "))
            if choice == "HB75fS7gs2":
                uninstall3()
            else:
                print(f"ERROR! Wrong code!")
                time.sleep(2)
                menu()
        except ValueError:
            print("Please enter a valid password!")
            time.sleep(2)
            menu()
def uninstall3():
    for i in range(64):
        clear()
        title()
        sys.stdout.write(f"\r\033[0mUninstalling PYSH...\033[0m {spinner[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)
    try:
        shutil.rmtree(SDK_DIRECTORY)
    except FileNotFoundError:
        menu()
    except OSError as e:
        menu()
def more():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("MORE:")
    print("\n")
    print("[1] PLUGINS")
    print("[2] UNINSTALL")
    print("\n")
    print("[3] BACK")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 3:
                if choice == 1:
                    plugins()
                if choice == 2:
                    uninstall()
                if choice == 3:
                    menu()
            else:
                print(f"Please enter a number between 1 and 3.")
                time.sleep(1.5)
                more()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            credits()
def menu():
    clear()
    title()
    print("---------------------------------------------------------------------------------------------------------")
    print("\n")
    print("PYSH OPTIONS:")
    print("\n")
    print("[1] GENERATE TEMPLATE")
    print("[2] GENERATE TASK")
    print("[3] ABOUT")
    print("[4] GITHUB REPOSITORY")
    print("[5] CREDITS")
    print("[6] MORE")
    print("\n")
    while True:
        try:
            choice = int(input("Select an option: "))
            if 1 <= choice <= 6:
                if choice == 1:
                    generate_template()
                if choice == 2:
                    generate_task()
                if choice == 3:
                    about()
                if choice == 4:
                    webbrowser.open("https://github.com/wonnd3r/PYSH.SDK")
                    menu()
                if choice == 5:
                    credits()
                if choice == 6:
                    more()
            else:
                print(f"Please enter a number between 1 and 6.")
                time.sleep(1.5)
                menu()
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1.5)
            menu()
# Start program
for i in range(32):
    clear()
    title()
    sys.stdout.write(f"\r\033[0mLoading PYSH...\033[0m {spinner[i % 4]}")
    sys.stdout.flush()
    time.sleep(0.1)
menu()
