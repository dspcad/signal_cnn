#!/usr/bin/python

import cPickle
import numpy as np
from nptdms import TdmsFile
import sys

if __name__ == '__main__':
  tdms_file = TdmsFile("./RX4.tdms")
  #tdms_file = TdmsFile("C:\Users\Jeff\Downloads\USRP\forNetworkEmulator\8_14PacketSyncClock\forMatlab\RXIQ.tdms")
  channelI = tdms_file.object('Data group', 'I')
  I = channelI.data

  
  channelQ = tdms_file.object('Data group', 'Q')
  Q = channelQ.data
  
  print(I.shape)
  print(Q.shape)

  data_list = []
  for i in range(0,3000000):
  #for i in range(0,I.shape[0]):
    IQ_pair = np.zeros(2)
    IQ_pair[0] = I[i]
    IQ_pair[1] = Q[i]

    data_list.append(IQ_pair)

  ouf = open(sys.argv[1], 'w')
  cPickle.dump(data_list, ouf, 1)
  ouf.close()
  #ouf = open(sys.argv[2], 'w')
  #cPickle.dump(Q[0:15000], ouf, 1)
  #ouf.close()

  fo = open(sys.argv[1], 'rb')
  test_file = cPickle.load(fo)
  fo.close()

  #print test_file
  print len(test_file)
