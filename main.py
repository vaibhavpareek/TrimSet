import cv2
import pyfiglet
from os import path,system
def banner():
  print("\033[1;34;48m* PYTHON BASED SCRIPT \033[1;32;48mDeveloped By @Vaibhav Pareek\033[1;31;48m")
  print("\033[1;34;48m* It prepare the video dataset \033[1;31;48m")
  ascii_banner = pyfiglet.figlet_format("TrimSet",font="slant")
  print(ascii_banner)
  print("\033[1;34;48m* Run the video till you want to smaller clips. \033[1;31;48m")
  print("\033[1;35;48m")
def exit_banner():
  print(pyfiglet.figlet_format("Thanks for using TrimSet",font="slant"))

#run video till you want  to divide into the no of videos
banner()
try:
  vd = input("Enter Video Location : ")
  cap = cv2.VideoCapture(vd) 
  if (cap.isOpened()== False):  
    print("Error opening video  file") 
  i,count=0,1
  size=(1,2)
  flag=True
  while(cap.isOpened()):
      ret, frame = cap.read()
      if(path.isdir('Images')==False):
        system("mkdir Images/")
      if ret == True:
          cv2.imshow('Frame', frame)
          height, width, layers = frame.shape
          size = (width,height) 
          if flag:
            out = cv2.VideoWriter('Images/dataset'+str(count)+'.avi',0,15, size)
            flag=False
          out.write(frame)
          i = i + 1
          if(i==70):
            out.release()
            i=0
            print('Images/project'+str(count)+'.avi')
            count = count + 1
            out = cv2.VideoWriter('Images/dataset'+str(count)+'.avi',0,15, size)
          if cv2.waitKey(30)==13 or 0xFF == ord('q'):
              break
      else:
          break
  cap.release()    
  cv2.destroyAllWindows() 
  print("Successfully trimmed")
except Exception as e:
  exit_banner()
  exit(0)
