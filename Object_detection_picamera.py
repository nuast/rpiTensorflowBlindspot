
######## Object Detecting Blindspot Camera Using Tensorflow Classifier #########
#
# By: Ed E, Davincey R and Jack B
# Based on code by: Evan Juras

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py


# Print ben shapiro
print("""
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                           ``.-::::-..`                                                                                                                                                                 
                      `-/ossyhdddddmhyys+:.                                                                                                                                                             
                    .:+ossyhyyyhdmmNNhyyyyso:`                                                                                               ``-::-```                                                  
                  `-://////ys-.-:+shNdyyyyhhhy+.         .oooo+-                     `/oo+- /d/                     -h/                     ://++++///`                                                 
                ./++///////:--...-/odyssyssyyyys:`       :Md//mN- `://:` ./.://.     hM+/o: +Ms://.  -///-` ./-:/:` -y: ./.:/` -///.       .+++++/--/+-                                                 
               :sooo+++//++-.-/+-oyhyooosoooosssy+`      :MmyyNh``hNoomh`/MdooNm`    omho:` +MdosNd` /o+yN+ /MdosNh`/Mo /Mdys`oNyohN+     `/+/.::``:+++.                                                
              :ss++////:////--:.-sos+/+++ooosssssso`     :Md--hN/-MNssyh./Ms  mM.    `.:sNy +Ms  mM`-hyoyMy /Ms `mM./Mo /Ms   mM. -Md      :+/:``-/+++/`                                                
             .//+//:::::////o:-:oyhmhooooossyyyysyds     :Mmssmm:`ymo+++ /Mo  dN.   `yysyms +Mo  mN`+Nh+sNy /MmsyNy /Mo /Mo   +mhshm/       :/+//++++/`                                                 
             ::///:::://++o+y:-:+hNNNdhsooooossssyhh-    `::::-`   .:::. .:.  ::     .:::.  .:.  ::  -::`:- /Ms-:-  .:. .:.    .:::.         `.-//:..`                                                  
            .ooooooooooooosods:+hNNmmmmdddyyyyhhyhhho                                                       /m+                                                                                         
            :sssososssssyyyhhyyydhhhhhhhhddmmmmmhhhhs                                                        ``                                                                                         
            :sssssssssssyyyyyyyyyyyhhhhhdhhdmmNdoooss             `                                                                                                                                     
            .++//++syssysyyyyyyyyyyyhhhhhdddmmNh++oso     .----- `/                    --                -                                                                                              
            `/::::/yyyyhyyyyyyyyyyyhhdddmmmmmNNNoooo/    :.----.:`+--:``:-:- /--:.`:--`-/--: `--:` /--:` / :--`---:`                                                                                    
             -::::oyhhmhyyyyyyhyyyhhhdddmNNmmNNNh+o+`    / /`-:`:`+  -:-/--/ +  .:`---`--  + --.+. +  ./`+ /. `/  -:                                                                                    
              -::/yyydmdhyyyyhhyhhhhddmNNMmdmNNNy//-     .-.-.-. `/--:``:--. /  .-`--:`--  / ::-/. +--:` / :`  -:-:`                                                                                    
              `:/+yyhdmdhhyyyhyhhhdddmmNNNmmmmmNy:.        ...`                                    +                                                                                                    
               `:oyyhdmhhhyyyhhhhhdddmmmNNNmmmmNm-                                                 `                                                                                                    
                 :shhdmhhhhhyhhhhhdmddmmmNNmmmms.                                                                                                                                                       
                   /ymmhhhhhhhhhhsshhhmmdmNmdo.                                                                                                                                                         
                     -+yhhhhyhydhysyhmNNmdy/`                                                                                                                                                           
                        `-:+osyyyyhhso+/.`                                                                                                                                                              
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                               `.                                          .`                                                                                                                           
                   -osysss/`   od                                    ``   `m/        `h:               /h`                                   `h/                                                        
                  sd+.```-yd-  sm    ``    ```   ``     ``          .h+`` `M/ ```    `:.   `.-.`       .:    .--.`         .-.`    `` .-.`    :.    `.-.`                                               
                 /M:      `hd  sm  .ss.  /sssyh- /d.   `yy         .oMy++``Mysssyh:  `m:  syooss.      +d  -hsooso       -yyoshs`  sysoosho` `d/  `shsos+                                               
                 sN`       oM. sm.oh/`   ````.dh `yh`  +m.          .M+   `Mh.  `ym  .M/ `ms.` `       +N  /N/.  `      .Ns...:Ns  yN.   -No `N+  yd.                                                   
                 oN.       sN` sNymo`   .osooomd  .mo -N/           .M+   `M+    oN` .M/  .+sys/`      +N   :oyyo-      /Myssssyo  yd     dh `N+ `No                                                    
                 .my.     :mo  sm`-hy.  dh.` `dd   -m:hy   `.`      .N+   `M/    oN` .M/     `:mo      +N     `.oN.     -N+`       yN.   -No `N+  hh`                                                   
                  .shs++oyh/   od  `od: odo+osyh    +md`   om.       ydo+.`m/    +m` `m: `so++sd:      +m  /so+oyy`      :hyo+os-  ymyo+ohs` `m/  .yyo+o+                                               
                    `--:-.     `.    ..  .-:-``.    /N:   `d+        `-:-` .`    `.   .`  .-:--`       `.  `--:-.         `.-:-.   yh`-:-.    .`    .-:-.                                               
                                                 :/od/    `-                                                                       yh                                                                   
                                                 -/:.                                                                              -:                                                                   
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                           
         ,---._                                   ,--.                                                     
       .-- -.' \    ,---,         ,----..     ,--/  /|                                                     
       |    |   :  '  .' \       /   /   \ ,---,': / '                                                     
       :    ;   | /  ;    '.    |   :     ::   : '/ /                                                      
       :        |:  :       \   .   |  ;. /|   '   ,                                                       
       |    :   ::  |   /\   \  .   ; /--` '   |  /                                                        
       :         |  :  ' ;.   : ;   | ;    |   ;  ;                                                        
       |    ;   ||  |  ;/  \   \|   : |    :   '   \                                                       
   ___ l         '  :  | \  \ ,'.   | '___ |   |    '                                                      
 /    /\    J   :|  |  '  '--'  '   ; : .'|'   : |.  \                                                     
/  ../  `..-    ,|  :  :        '   | '/  :|   | '_\.'                                                     
\    \         ; |  | ,'        |   :    / '   : |                                                         
 \    \      ,'  `--''           \   \ .'  ;   |,'                                                         
  "---....--'                     `---`    '---'                                                           
    ,---,.    ,---,                                                                                        
  ,'  .' |  .'  .' `\                                                                                      
,---.'   |,---.'     \                                                                                     
|   |   .'|   |  .`\  |                                                                                    
:   :  |-,:   : |  '  |                                                                                    
:   |  ;/||   ' '  ;  :                                                                                    
|   :   .''   | ;  .  |                                                                                    
|   |  |-,|   | :  |  '                                                                                    
'   :  ;/|'   : | /  ;                                                                                     
|   |    \|   | '` ,/                                                                                      
|   :   .';   :  .'                                                                                        
|   | ,'  |   ,.'                                                                                          
`----'    '---'                                         ,--.                                               
    ,---,       ,---,                     ,---,       ,--.'|  ,----..      ,---,.                          
  .'  .' `\    '  .' \            ,---.,`--.' |   ,--,:  : | /   /   \   ,'  .' |        ,---,       ,---, 
,---.'     \  /  ;    '.         /__./||   :  :,`--.'`|  ' :|   :     :,---.'   |       /_ ./|      /_ ./| 
|   |  .`\  |:  :       \   ,---.;  ; |:   |  '|   :  :  | |.   |  ;. /|   |   .' ,---, |  ' :,---, |  ' : 
:   : |  '  |:  |   /\   \ /___/ \  | ||   :  |:   |   \ | :.   ; /--` :   :  |-,/___/ \.  : /___/ \.  : | 
|   ' '  ;  :|  :  ' ;.   :\   ;  \ ' |'   '  ;|   : '  '; |;   | ;    :   |  ;/| .  \  \ ,' '.  \  \ ,' ' 
'   | ;  .  ||  |  ;/  \   \\   \  \: ||   |  |'   ' ;.    ;|   : |    |   :   .'  \  ;  `  ,' \  ;  `  ,' 
|   | :  |  ''  :  | \  \ ,' ;   \  ' .'   :  ;|   | | \   |.   | '___ |   |  |-,   \  \    '   \  \    '  
'   : | /  ; |  |  '  '--'    \   \   '|   |  ''   : |  ; .''   ; : .'|'   :  ;/|    '  \   |    '  \   |  
|   | '` ,/  |  :  :           \   `  ;'   :  ||   | '`--'  '   | '/  :|   |    \     \  ;  ;     \  ;  ;  
;   :  .'    |  | ,'            :   \ |;   |.' '   : |      |   :    / |   :   .'      :  \  \     :  \  \ 
|   ,.'      `--''               '---" '---'   ;   |.'       \   \ .'  |   | ,'         \  ' ;      \  ' ; 
'---'                                          '---'          `---`    `----'            `--`        `--`  
                                                                                                                                                                                                                                                                                                                  
""")

# Import packages
import time
import unicornhat as unicorn
from UHScroll import *
unicorn.clear()
unicorn.brightness(0.5)
unicorn_scroll('NUAST','yellow',255,0.1)
unicorn_scroll('WAIT','red',255,0.1)
def displayChar(inp,r,g,b) :
    unicorn.clear()
    for i in range(8):
        for i2 in range(8):
            unicorn.set_pixel(i,7-i2, r,g,b) if inp[i][i2] == 'o' else unicorn.show() #8-12 because the image is reversed otherwise - YOU STILL NEED T$
global printArr
printArr = []
flashScreen = [
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o']
]
person = [
['x','x','x','o','o','x','x','x'],
['x','x','x','o','o','x','x','x'],
['o','o','o','o','o','o','o','o'],
['o','x','o','o','o','o','x','o'],
['o','x','o','o','o','o','x','o'],
['o','x','o','o','o','o','x','o'],
['x','o','o','x','x','o','o','x'],
['o','o','x','x','x','x','o','o']
]
warn = [
['o','o','o','o','o','o','o','o'],
['o','o','o','x','x','o','o','o'],
['o','o','o','x','x','o','o','o'],
['o','o','o','x','x','o','o','o'],
['o','o','o','x','x','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','x','x','o','o','o'],
['o','o','o','x','x','o','o','o']
]

load = [
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o'],
['x','x','o','x','x','o','x','x'],
['x','x','o','x','x','o','x','x']
]

displayChar(load, 0,0,255) # Blue load symb
unicorn.show()



import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
import sys
# This is OnBoot_init.py to run on boot.

# Set up camera constants
IM_WIDTH = 640
IM_HEIGHT = 480
#IM_WIDTH = 640    Use smaller resolution for
#IM_HEIGHT = 480   slightly faster framerate

camera_type = 'picamera'
parser = argparse.ArgumentParser()
parser.add_argument('--usbcam', help='Run the script without errors',
                    action='store_true')
args = parser.parse_args()
if args.usbcam:
    camera_type = 'usb'

# This is needed since the working directory is the object_detection folder.
sys.path.append('..')

# Import utilites
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'data','mscoco_label_map.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 90

## Load the label map.
# Label maps map indices to category names, so that when the convolution
# network predicts `5`, we know that this corresponds to `airplane`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')
print(num_detections)
# Initialize frame rate calculation
frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize camera and perform object detection.
# The camera has to be set up and used differently depending on if it's a
# Picamera or USB webcam.

# I know this is ugly, but I basically copy+pasted the code for the object
# detection loop twice, and made one work for Picamera and the other work
# for USB.

### USB webcam ###
if camera_type == 'usb':
    # Initialize USB webcam feed
    camera = cv2.VideoCapture(0)
    ret = camera.set(3,IM_WIDTH)
    ret = camera.set(4,IM_HEIGHT)
    unicorn_scroll("READY", 'green', 255,0.1)
   
    while(True):

        # Clear the detection file
        p = open('/home/pi/tensorflow1/models/research/object_detection/objDet.txt','w+')
        p.write(" ")
        p.close()
        t1 = cv2.getTickCount()

        # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value
        ret, frame = camera.read()
        frame_expanded = np.expand_dims(frame, axis=0)
        
        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: frame_expanded})
        
        
        printArr = []
        # Draw the results of the detection (aka 'visulaize the results')
        resOutput = vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8,
            min_score_thresh=0.6)
        #vis_util saves results as plaintext - formatted as Obj: Detection%
        print("Scanning...")
        imnotaweebijustlikeanime = open('objDet.txt','r')
        lmao = str(imnotaweebijustlikeanime.read())
        imnotaweebijustlikeanime.close()
        if "person" in lmao:
           print("Found person! FLASHING!")
           unicorn.brightness(1)
           displayChar(flashScreen,255,255,255)
           unicorn.show()
           time.sleep(0.5)
           unicorn.brightness(0.5)
           displayChar(warn,255,255,0)
           unicorn.show()
           time.sleep(1)
           
           unicorn_scroll("DANGER STAY BACK",'red', 255,0.1)          
            
        cv2.putText(frame,"FPS: {0:.2f}".format(frame_rate_calc),(30,50),font,1,(255,255,0),2,cv2.LINE_AA)
        
        # All the results have been drawn on the frame, so it's time to display it.
        #cv2.imshow('Object detector', frame)

        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc = 1/time1

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()

cv2.destroyAllWindows()
# OMG IT WORKS - WE DID IT :))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))) Saturday 7:57pm :)))) now time to add TTS