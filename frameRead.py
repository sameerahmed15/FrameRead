import cv2
import os
import time

myPath='imgs'   # file name where the frames will be saved
frameNum=50     #increase or decrease value to store less or more frames per second
minBlur=500
grayImage=False
saveData=True   
showImage=True
count=0
countSave=0
global countFolder

#Path of the video file
cap=cv2.VideoCapture('50m_100m_9ths_0p5kts_0p4m_0deg_002_c_overhead.mkv')

def saveDataFunc():
    global countFolder
    countFolder=0
    while os.path.exists(myPath+str(countFolder)):
        countFolder=countFolder+1
    os.makedirs(myPath+str(countFolder))

if saveData:saveDataFunc()

while True:

    success, img=cap.read()
    img= cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    if grayImage: img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if saveData:
        blur=cv2.Laplacian(img, cv2.CV_64F).var()
        if count % frameNum==0 and blur>minBlur:
            nowTime=time.time()
            cv2.imwrite(myPath + str(countFolder)+ '/' + str(countSave) + "_" + str(int(blur)) + " " + str(nowTime) + ".png", img )
            countSave += 1

        count += 1 

    if showImage:
        cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()       

