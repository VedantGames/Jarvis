import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("C:/Users/ASUS/Music/Movavi Video Editor/Recorded Audio/a.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
singal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(singal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array, 'bo-')
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()