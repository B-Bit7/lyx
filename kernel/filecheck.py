import os

exsist = []
def check():
      inchfile = open("kernel/checkedfiles.ini", "r")
      data = inchfile.read()
      files = data.replace("=NC", "").splitlines()
      inchfile.close()
      for file in files:
            if not(file == ""):
                  print(os.path.isfile(file))
                  if os.path.isfile(file) == True:
                        exsist.append(os.path.isfile(file))
                  elif os.path.isfile(file) == False:
                        exsist.append(os.path.isfile(file))
                  else:
                        print("Oh no something went wrong... Reinstalling the program may fix the problem.")
                        input("Press enter to continue... ")
                        exit(3)
      return exsist
      
      
      
            
