import cv2
import time
import dropbox
import random 

startTime = time.time()
print("intializing...")
def takeSnap():
    number = random.randint(0,100)
    vcobj = cv2.VideoCapture(0)
    result = True
    while(result):
        ret , frame = vcobj.read()
        imgName = "img" + str(number) + ".png"
        cv2.imwrite(imgName,frame)
        result = False
    return imgName
    print("snapShot Taken")
    vcobj.release()
    cv2.destroyAllWindows()

def UploadFiles(img): 
    access_token = 'Bfyw1uzaYMwAAAAAAAAAATMP0ywQp0VAQZ3g8UNQ5ekzr2gDnZ1KpuHB7gcqC7Wl'
    file = img  
    file_from = file
    file_to = "/testFolder/" + (img)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("files uploaded successfully")

def Main():
    while(True):
        if((time.time() - startTime) >= 5):
            name = takeSnap()
            UploadFiles(name)
            
Main()
