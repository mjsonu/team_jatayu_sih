import pyaudio
import os
from scipy.fftpack import fft
import struct #to unpack the audio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 300 * 4 #4096 audio display at a time in a frame
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE =  35000 

p_get = pyaudio.PyAudio()
stream = p_get.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,output=True,frames_per_buffer=CHUNK)

plt.ion()
fig=plt.figure()

ax2=fig.add_subplot(111)
ax=fig.add_subplot(322)
fig,(ax,ax2) =plt.subplots(2)

#plotting variable
x=np.arange(0 ,2 * CHUNK, 2)
x_fft=np.linspace(0,RATE,CHUNK)

#creating an object of random data
line, =ax.plot(x, np.random.rand(CHUNK),'-',lw=2)
line_fft, = ax2.plot(x_fft,np.random.rand(CHUNK), '-',lw=2 )

#to set the axes 
ax.set_ylim(0 ,255)
ax.set_xlim(0 , 2*CHUNK)
ax.set_title('Audio Waveform')
ax.set_xlabel('Samples')
ax.set_ylabel('Volume')

ax2.set_xlim( 20, RATE / 2)
#for dynamically change
while True:
    data=stream.read(CHUNK)
    #print(data)
    data_unpack=struct.unpack(str(2 * CHUNK)+ 'B' ,data)
    
    data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B' ,data)).astype(dtype='b')[::2]+127 
    print(data_int)
    line.set_ydata(data_int)
    #to set fft 
    y_fft=fft(data_unpack)
    line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) *2 /(256*CHUNK))
    #to update the canvas
    fig.canvas.draw()
    fig.canvas.flush_events()
    
plt.show()    

