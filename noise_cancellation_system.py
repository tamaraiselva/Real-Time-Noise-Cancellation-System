import pyaudio
import numpy as np
import wave
import os
import time

# Constants for audio processing
CHUNK = 8820
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
AMPLIFICATION_FACTOR = 2.0

# Noise cancellation function
def noise_cancellation(input_audio, mode="Single_Speaker_Scenario", reduction_level=0.8):
    if not np.any(input_audio):  # Check for silence
        return input_audio

    if mode == "Single_Speaker_Scenario":
        noise_profile = np.mean(input_audio)
    elif mode == "multiple_speakers_Scenario":
        noise_profile = np.median(input_audio)
    else:
        raise ValueError("Invalid mode. Choose 'Single_Speaker_Scenario' or 'multiple_speakers_Scenario'.")

    processed_audio = input_audio - reduction_level * noise_profile
    amplified_audio = processed_audio * AMPLIFICATION_FACTOR
    return np.clip(amplified_audio, -32768, 32767).astype(np.int16)

# Main function
def main():
    print("Real-Time Noise Cancellation System")
    p = pyaudio.PyAudio()

    try:
        if p.get_device_count() == 0:
            print("No audio devices found.")
            return

        # User configuration
        while True:
            try:
                mode_input = int(input("Enter 1 for Single Speaker Scenario.\nEnter 2 for Multiple Speaker Scenario: "))
                if mode_input == 1:
                    mode = "Single_Speaker_Scenario"
                    break
                elif mode_input == 2:
                    mode = "multiple_speakers_Scenario"
                    break
                else:
                    print("Invalid selection. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        reduction_level = 0.9
        output_dir = "output_audio"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "processed_audio.wav")

        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK,
        )

        frames = []
        print("Starting noise cancellation. Press Ctrl+C to stop.")

        try:
            while True:
                try:
                    raw_data = stream.read(CHUNK, exception_on_overflow=False)
                    input_audio = np.frombuffer(raw_data, dtype=np.int16)
                    processed_audio = noise_cancellation(input_audio, mode=mode, reduction_level=reduction_level)
                    stream.write(processed_audio.tobytes())
                    frames.append(processed_audio.tobytes())
                except Exception as e:
                    print(f"Audio processing error: {e}")
        except KeyboardInterrupt:
            print("Stopping noise cancellation...")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()

            if frames:
                wf = wave.open(output_file, "wb")
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b"".join(frames))
                wf.close()
                print(f"Processed audio saved to {output_file}")
            else:
                print("No audio data to save.")

    except Exception as e:
        print(f"Initialization error: {e}")

if __name__ == "__main__":
    main()
