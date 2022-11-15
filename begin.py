import os
import imageio
import numpy as np
import torch
import glob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
import io
import base64
import warnings
import cv2
from demo import load_checkpoints
from demo import make_animation
from skimage import img_as_ubyte
warnings.filterwarnings("ignore")
#os.system("matplotlib inline")


######## Upload a square video in mp4
#####################################

#You can crop video here: https://ezgif.com/crop-video**
#Convert video here: https://convert-video-online.com**

vid = '../input/iko-iko-square.mp4'

fps_of_video = int(cv2.VideoCapture(vid).get(cv2.CAP_PROP_FPS))
frames_of_video = int(cv2.VideoCapture(vid).get(cv2.CAP_PROP_FRAME_COUNT))

print('Video Input = ' + vid + ', FPS = ' + str(fps_of_video) + ', Total Frames = ' + str(frames_of_video))




###### Upload one or more face photos
#####################################

uploaded = ["../input/iko-iko-square.png"]

os.system("rm -rf raw_images aligned_images")
os.system("mkdir raw_images aligned_images")
i = 0
raw_photolist = []
for fn in uploaded:
  os.rename(fn, fn.replace(" ", ""))
  fn = fn.replace(" ", "")
  pho = "photo-" + str(i) + "." + fn.split(".")[1]
  #TEMP! REVERT: cp = mv -f
  os.system("cp " + fn + " raw_images/" + pho)
  raw_photolist.append(pho)
  i += 1
print('Image Input = ' + raw_photolist[0])


###### Crop face in photos
##########################

success = False
try:
  os.system("python align_images.py raw_images/ aligned_images/")
  pho_file = os.system("ls aligned_images")
  if len(pho_file) == 0:
    os.system("cp raw_images/* aligned_images/")
  else:
    success = True
except BaseException:
  os.system("cp raw_images/* aligned_images/")

aligned_photolist = []
for photoname in raw_photolist:
  newname = photoname.split('.')[0] + '_01.png'
  aligned_photolist.append(newname if success else photoname)

print('Image Aligned = ' + aligned_photolist[0])
