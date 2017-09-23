#!/usr/bin/python

import cPickle
import numpy as np
import sys
import tensorflow as tf

###################################
#   10K Hz for sin and cos waves  #
#   500K Hz for sampling rate     #
###################################


def readInput(filename):
  fo = open(filename, 'rb')
  IQ_file = cPickle.load(fo)
  fo.close()

  return IQ_file



if __name__ == '__main__':
  

  print '===== Start loading datasets ====='
  #fo = open(sys.argv[1], 'rb')
  IQ_file_1 = readInput("/home/hhwu/tensorflow_work/cs231n/signal_cnn/test_input_1.bin")
  print "IQ_file_1: %d" % len(IQ_file_1)
  #IQ_file_2 = readInput("/home/hhwu/tensorflow_work/signal_cnn/test_input_2.bin")
  #print "IQ_file_2: %d" % len(IQ_file_2)
  #IQ_file_3 = readInput("/home/hhwu/tensorflow_work/signal_cnn/test_input_3.bin")
  #print "IQ_file_3: %d" % len(IQ_file_3)
  #IQ_file_4 = readInput("/home/hhwu/tensorflow_work/signal_cnn/test_input_4.bin")
  #print "IQ_file_4: %d" % len(IQ_file_4)


  plane = np.zeros((128,128))
 
  pixel_intensity = 4
  #for i in range(0, len(IQ_file_1)):
  for i in range(0, 1000):
    idx_I = int((IQ_file_1[i+1234500][0]+0.001)*64000)
    idx_Q = int((IQ_file_1[i+1234500][1]+0.001)*64000)

    print "(%d, %d)" % (idx_I, idx_Q)

    plane[idx_I][idx_Q] = pixel_intensity
 
  for i in range(0,128):
    for j in range(0,128):
      if plane[i][j] == 0.0:
        print " ",
      else:
        print "%d" % plane[i][j],

    print " ---"


  #displayFrame(plane, 1)

  sel = 0
  IQ_file = IQ_file_1
  hist_I = np.zeros(10)
  for i in range(0,len(IQ_file)):
    if IQ_file[i][sel] > -1 and IQ_file[i][sel] <= -0.8:
      hist_I[0] = int(hist_I[0]) + 1
    elif IQ_file[i][sel] > -0.8 and IQ_file[i][sel] <= -0.6:
      hist_I[1] = int(hist_I[1]) + 1
    elif IQ_file[i][sel] > -0.6 and IQ_file[i][sel] <= -0.4:
      hist_I[2] = int(hist_I[2]) + 1
    elif IQ_file[i][sel] > -0.4 and IQ_file[i][sel] <= -0.001:
      hist_I[3] = int(hist_I[3]) + 1
    elif IQ_file[i][sel] > -0.001 and IQ_file[i][sel] <= 0.0:
      hist_I[4] = int(hist_I[4]) + 1
    elif IQ_file[i][sel] > 0.0 and IQ_file[i][sel] <= 0.001:
      hist_I[5] = int(hist_I[5]) + 1
    elif IQ_file[i][sel] > 0.001 and IQ_file[i][sel] <= 0.4:
      hist_I[6] = int(hist_I[6]) + 1
    elif IQ_file[i][sel] > 0.4 and IQ_file[i][sel] <= 0.6:
      hist_I[7] = int(hist_I[7]) + 1
    elif IQ_file[i][sel] > 0.6 and IQ_file[i][sel] <= 0.8:
      hist_I[8] = int(hist_I[8]) + 1
    else:
      hist_I[9] = int(hist_I[9]) + 1

  for i in range(0,10):
    print hist_I[i]
