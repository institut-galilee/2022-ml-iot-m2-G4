# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:30:00 2022

@author: prana
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 00:00:38 2022

@author: prana
"""
"""
import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""

import cv2
import numpy as np
import time
import speech_recognition as sr
import sys
import time
import asyncio


def check_space(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count

def check(arr,word):
    lenArr = len(arr)
    lenWord = len(word)
    count = 0
    for i in range(lenArr):
        for j in range (lenWord):
            if arr[i] == keyWord[j]:
                count = count + 1
    return count
    
import fitz
with fitz.open("test.pdf") as doc:
    text = []
    finalText = []
    charToString = ""
    for page in doc:
        tmp = page.getText().replace("\n"," ")
        print(f'text={len(tmp)}\n')
        text.append(tmp)
        # print(text)
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == " ":
                finalText.append(charToString)
                charToString = ""
            else:
                charToString = charToString + text[i][j]
print(finalText)
print("\n\n")

keyWord = finalText
toListText = []
rec = sr.Recognizer()


async def recText(rec,audio,keyWord,toListText):
    try:
        text = rec.recognize_google(audio,language="en-US")
        text = text.lower()
        lengthText = check_space(text)
        if lengthText > 0:
            for i in range (lengthText+1):
                toListText.append(text.split(" ")[i])
        if lengthText == 0:
            toListText.append(text.split(" ")[0])
        print(toListText)
        print(f"Rec { text }")
        warningCount = check(toListText,keyWord)
        if warningCount >= 3:
            from pygame import mixer
            mixer.init() 
            sound=mixer.Sound("output.mp3")
            #rec.pause_threshold
            sound.play()
            time.sleep(6)
            sys.exit()
            # continue
        print(f"Rec { text }")
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass

#load YOLO
net = cv2.dnn.readNet('yolov3-tiny.weights','yolov3-tiny.cfg')
classes =[]
with open('coco.names','r') as f:
    classes = [line.strip() for line in f.readlines()]

# layer_names = net.getLayerNames()
# outputLayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayersNames()]


outputLayers = net.getUnconnectedOutLayersNames()
# layerOutputs = net.forward(output_layer_names)


colors = np.random.uniform(0,255,size=(len(classes),3))

# loading image 
cap = cv2.VideoCapture(0) # 0 for 1st wbcam
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
img_id = 0
persone = 0
listLabel=[]


while True:
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source,duration = 0.2)
        audio = rec.record(source, duration=5)
        asyncio.run(recText(rec,audio,keyWord,toListText))
    _,img = cap.read()
    # time.sleep(10)
    height, width,channels = img.shape
    # detecting objects
    blob = cv2.dnn.blobFromImage(img,0.00392,(224,224),(0,0,0),swapRB=True,crop=False)
    
    # for b in blob:
    #     for n,img_blob in enumerate(b):
    #         cv2.imshow(str(n),img_blob)
    
    net.setInput(blob)
    outs = net.forward(outputLayers)
    class_ids = []
    confidences = []
    boxes = []
    
    
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence >0.3:
                # object detected
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                
                # rectangle co-ordinaters
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                boxes.append([x,y,w,h]) # put all rectangle areas
                confidences.append((float(confidence))) # how confidence was that object detected and show that percentage
                class_ids.append(class_id) # name of the object that was detected
    
    # print(len(boxes))
    indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.3,0.6)
    # print(indexes.flatten())
    
    
    
    
    
    # if len(indexes) > 0:
    #     indexes_flatten = indexes.flatten()
    #     for i in indexes_flatten:
    #         x,y,w,h = boxes[i]
    #         label = str(classes[class_ids[i]])
    #         confidence = str(round(confidences[i],2))
    #         color = colors[class_ids[i]]
    #         cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
    #         cv2.putText(img,label+" "+confidence, (x,y+30),font,1,(255,255,255),2)
    #     elapsed_time = time.time() - starting_time
    #     fps = img_id / elapsed_time
    #     cv2.putText(img,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
    #     cv2.imshow('Image',img)
    #     key = cv2.waitKey(1) # wait 1ms, the loop will start again and we will process the next frame
    #     if key == 27:
    #         break
    # else:
    #     print("coudn't find any object")
    #     break

    # indexes_flatten = indexes.flatten()
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            # for i in range(len(listLabel)):
            #     if listLabel[i] != classes[i]:
            #         listLabel.append(label)
            # print(label,end=" ")
            confidence = str(round(confidences[i],2))
            color = colors[class_ids[i]]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,label+" "+confidence, (x,y+20),font,1,(255,0,0),2)
    elapsed_time = time.time() - starting_time
    fps = img_id / elapsed_time
    cv2.putText(img,"FPS:"+str(round(fps,2)),(10,50),font,2,(0,0,0),1)
    cv2.imshow('Image',img)
    key = cv2.waitKey(1) # wait 1ms, the loop will start again and we will process the next frame
    if key == 27:
        break
    # print(label+"\n")
# cv2.waitKey(0)    
cap.release()  
cv2.destroyAllWindows()

