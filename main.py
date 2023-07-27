import cv2
import numpy as np


net = cv2.dnn.readNetFromTensorflow('path_to_model_file')
with open('path_to_labels_file', 'r') as f:
    classes = f.read().strip().split('\n')


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    if not ret:
        break

    
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224), (104, 177, 123))

    
    net.setInput(blob)

    
    detections = net.forward()

    for detection in detections[0, 0]:
        confidence = detection[2]

        if confidence > 0.5:  
            class_id = int(detection[1])
            class_label = classes[class_id]
            box = detection[3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            start_x, start_y, end_x, end_y = box.astype('int')

           
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
            cv2.putText(frame, class_label, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2

                        
  cv
