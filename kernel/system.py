import kernel.boot.boot as boot
import kernel.bluescreen
import kernel.filecheck as filecheck

def run():
      boot.bootfh()
      files = filecheck.check()
      allfiles = open("kernel/checkedfiles.ini", "r").read().splitlines()
      if all(element == files[0] for element in files):
            print("all files are here")
            boot.bootsh()
      else:
            pass

if __name__ == "__main__":
      run()

