#dependencies
import pyaudio
import struct #to unpack the audio
import numpy as np
import matplotlib.pyplot as plt



CHUNK = 300* 4  #1200 audio display at a time in a frame
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE =  1000 # to change the rate of audio

p_get = pyaudio.PyAudio()
stream = p_get.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,output=True,frames_per_buffer=CHUNK)

#for static plot

data=stream.read(CHUNK)
data_int = struct.unpack(str(2 * CHUNK)+ 'B' ,data) #to convert into int
#to remove the discontinuity in graph and to reconstruct the graph
data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B' ,data)).astype(dtype='b')[::2] 

print(data_int)

#to plot the graph
fig , ax = plt.subplots()
ax.plot(data_int, '-')
plt.show()


#for dynamically change
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)

x=np.arange(0 ,2 * CHUNK, 2)

line, =ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(0 ,255)
ax.set_xlim(0 ,CHUNK)

while True:
    
    data=stream.read(CHUNK)
    print(data)
    data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B' ,data)).astype(dtype='b')[::2]+127 
    print(data_int)
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
    
plt.show()

   
    

