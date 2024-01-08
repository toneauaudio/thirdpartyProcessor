from pedalboard import Pedalboard, load_plugin
from pedalboard.io import AudioFile

# reads in audio and resamples to desired sample rate
samplerate = 44100.0
with AudioFile('AUDIOFILE.wav').resampled_to(samplerate) as f:
    audio = f.read(f.frames)

effect = .load_plugin("./VSTs/PLUGINNAME.vst3") # vst3 or au path here

effect.ratio = 15   # set hypthetical ratio to value

effected = effect(audio, sample_rate)   # apply effect to audio

# audio back as .wav file
with Audiofile('OUTPUTFILE.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)
