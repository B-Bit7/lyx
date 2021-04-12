import time, shutil, sys, os, random

def cpr(msg):
      columns = shutil.get_terminal_size().columns # rows - 8
      print(msg.center(columns))

def padToCenter(l:list,w:int)->str:
    """Manual centering"""
    padding =  ' '*(w//2) 
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

banner = open("kernel/boot/banner.txt", "r").read()

def bootfh():
      i = 0
      for i in range(13):
            print("{}".format('\n'*int(shutil.get_terminal_size().lines / 2 - 10)))
            print(padToCenter(banner.splitlines(),shutil.get_terminal_size().columns - 5))
            print("\n\n")
            cpr("[-------------------------]".replace("-", "=", i))
            time.sleep(round(random.uniform(0.3, 0.9), 1))
            os.system("cls")

def bootsh():
      i = 13
      for i in range(13):
            print("{}".format('\n'*int(shutil.get_terminal_size().lines / 2 - 10)))
            print(padToCenter(banner.splitlines(),shutil.get_terminal_size().columns - 5))
            print("\n\n")
            cpr("[============-------------]".replace("-", "=", i))
            if i < 6:
                  cpr("All files checked...")
            time.sleep(round(random.uniform(0.3, 0.9), 1))
            os.system("cls")

if __name__ == "__main__":
      bootsh()
      
