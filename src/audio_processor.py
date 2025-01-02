import pyaudio
import wave
from filters.single_speaker import SingleSpeakerFilter
from filters.multi_speaker import MultiSpeakerFilter

class AudioProcessor:
    def __init__(self):
        # Initialize PyAudio and filters
        self.pyaudio_instance = pyaudio.PyAudio()
        self.single_speaker_filter = SingleSpeakerFilter()
        self.multi_speaker_filter = MultiSpeakerFilter()

    def start_stream(self):
        self.input_stream = self.pyaudio_instance.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024
        )
        self.output_stream = self.pyaudio_instance.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            output=True
        )

    def stop_stream(self):
        self.input_stream.stop_stream()
        self.input_stream.close()
        self.output_stream.stop_stream()
        self.output_stream.close()
        self.pyaudio_instance.terminate()

    def process_audio(self, audio_chunk, scenario):
        if scenario == 'single':
            return self.single_speaker_filter.apply_filter(audio_chunk)
        elif scenario == 'multi':
            return self.multi_speaker_filter.apply_filter(audio_chunk)

    def save_audio(self, audio_chunks, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(audio_chunks))
