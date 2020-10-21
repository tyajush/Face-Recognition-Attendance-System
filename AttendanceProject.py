import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('att.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def deleteEntry():
    f = open("att.csv", "w")
    f.truncate()
    f.writelines('Name,Time')
    f.close()


def start():
    encodeListKnownFaces = findEncodings(images)

    #testing data from webcam
    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

        #there can be multiple faces in cam
        #finding face locations
        faceCurrFrame = face_recognition.face_locations(imgS)
        encodesCurrFrame = face_recognition.face_encodings(imgS,faceCurrFrame)

        for encodeFace,faceLoc in zip(encodesCurrFrame,faceCurrFrame):
            matches = face_recognition.compare_faces(encodeListKnownFaces,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnownFaces,encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)
            else:
                name = 'Unknown'
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


        cv2.imshow('webcam' , img)
        cv2.waitKey(1)

        if cv2.getWindowProperty('webcam', cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()



#def register():
    




