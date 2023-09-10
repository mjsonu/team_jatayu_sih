#dependencies
import pyaudio
import struct #to unpack the audio
import numpy as np
import matplotlib.pyplot as plt



CHUNK = 300* 4 #4096 audio display at a time in a frame
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE =  1000 #44.1 hz

p_get = pyaudio.PyAudio()
stream = p_get.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,output=True,frames_per_buffer=CHUNK)

#for static plot
data=stream.read(CHUNK)
#print(data)



#to convert into int
data_int = struct.unpack(str(2 * CHUNK)+ 'B' ,data)
#to remove the discontinuity in graph and to reconstruct the graph
data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B' ,data)).astype(dtype='b')[::2] 

print(data_int)

#to plot the graph
fig , ax = plt.subplots()
ax.plot(data_int, '-')
plt.show()

   
    

