import librosa as lb
import numpy as np
import matplotlib.pyplot as plt

def plot_mel_spectrogram(audio_file):
    # Load audio file
    y, sr = lb.load(audio_file)

    # Compute STFT and convert to dB scale
    D = lb.stft(y)
    S_db = lb.amplitude_to_db(np.abs(D), ref=np.max)

    # Compute mel spectrogram and convert to dB scale
    M = lb.feature.melspectrogram(y=y, sr=sr)
    M_db = lb.power_to_db(M, ref=np.max)

    # Plot mel spectrogram
    fig, ax = plt.subplots()
    img = lb.display.specshow(M_db, y_axis='linear', x_axis='time', ax=ax, fmax=15000)
    ax.set(title='Spectrogram - Pre Filter', xlabel='Time', ylabel='Frequency (Hz)')
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.savefig('../figs/After_audiofilter.png')

# Example usage
plot_mel_spectrogram('Sound_With_ReducedNoise.wav')
