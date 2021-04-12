import os

def menu():
    while True:
        os.system("cls")
        import shutil
        items = open("desktop/mainitems.ini", "r").read().splitlines()
        print("┌{}─|".format("─"*(shutil.get_terminal_size().columns - 2)))
        i = 1
        for item in items:
            if "{sep}" in item:
                print("│")
            elif "{nonum}" in item:
                print("│          {}".format(item.replace(" {nonum}", "")))
            else:
                print(f"│   {i}.     {item}")
                i += 1
        input()
