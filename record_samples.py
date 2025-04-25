import os
import sounddevice as sd
import soundfile as sf

def record_sample(filename, duration=2, samplerate=16000):
    print(f"Recording... Say: {os.path.basename(filename).split('.')[0]}")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"Saved: {filename}")


if __name__ == "__main__":
    os.makedirs("data/sales", exist_ok=True)
    os.makedirs("data/support", exist_ok=True)
    os.makedirs("data/billing", exist_ok=True)

    for i in range(1, 6):
        record_sample(f"data/sales/sales{i}.wav")
        record_sample(f"data/support/support{i}.wav")
        record_sample(f"data/billing/billing{i}.wav")
