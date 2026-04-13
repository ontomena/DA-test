import wave
import struct

def create_silent_wav(filename, duration_seconds=3):
    """Create a silent WAV file"""
    sample_rate = 44100
    num_channels = 2
    bits_per_sample = 16
    
    num_samples = int(sample_rate * duration_seconds)
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(bits_per_sample // 8)
        wav_file.setframerate(sample_rate)
        
        # Write silent frames (all zeros)
        for _ in range(num_samples):
            for _ in range(num_channels):
                wav_file.writeframes(struct.pack('h', 0))
    
    print(f"Created {filename}")

# Create 3 placeholder audio files
create_silent_wav('sound-clip-1.wav', 2)
create_silent_wav('sound-clip-2.wav', 3)
create_silent_wav('sound-clip-3.wav', 2)

print("Silent audio placeholders created")
