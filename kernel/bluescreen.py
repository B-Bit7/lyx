import os

def FNEE(filename, errcode):
      os.system("color 17")
      print("")
      print(" Something wrent wrong in our system.")
      print(" The file(s) {} is missing or got corrupted.".format(filename))
      print("\n Reinstalling the program may fix the problem.")
      print(" If you see this error after uninstalling send the follwing code to the creator")
      print(" he will probably help you!")
      print("\n {}".format(errcode))

if __name__ == "__main__":
      FNEE("test.test", "00x00000")
      input()
