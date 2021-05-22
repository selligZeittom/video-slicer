import cv2
import os
import pathlib
import numpy as np

FILES = [
   {
      'path' : os.path.join(pathlib.Path().absolute(), 'data', 'jump1.mp4'), 'folder' : 'JUMP1', 'done' : False
   },
   {
      'path' : os.path.join(pathlib.Path().absolute(), 'data', 'jump2.mp4'), 'folder' : 'JUMP2', 'done' : False
   },
   {
      'path' : os.path.join(pathlib.Path().absolute(), 'data', 'sand1.mp4'), 'folder' : 'SAND1', 'done' : False
   },
]

if __name__ == "__main__":
   for file in FILES:
      path = file['path']
      output_folder = file['folder']
      done = file['done']
      print('Currently working on : {}'.format(path))
      
      if not done:   
         # read video
         stream = cv2.VideoCapture(path)
         number_of_frames = int(stream.get(cv2.CAP_PROP_FRAME_COUNT))
         i = 0

         # create directory
         try:
            os.mkdir(os.path.join(pathlib.Path().absolute(), 'frames', output_folder))
         except OSError:
            print('Failed to create output dir...')

         # read each frame
         while stream.isOpened():
            ret, frame = stream.read()
            if ret == False:
               break
            path_to_write = os.path.join(pathlib.Path().absolute(), 'frames', output_folder, 'frame_{}.jpg'.format(i))
            cv2.imwrite(path_to_write, frame)
            i += 1
            print(i)
         stream.release()