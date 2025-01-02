from audio_processor import AudioProcessor

def main():
    # Create an instance of AudioProcesssor
    audio_processor = AudioProcessor()

    # Ask the user to choose a scenario
    scenario = input("Select scenario (single/multi): ").strip().lower()
    if scenario not in ['single', 'multi']:
        print("Invalid scenario. Please choose 'single' or 'multi'.")
        return

    # Start audio streaming
    audio_processor.start_stream()
    print("Processing audio... Press Ctrl+C to stop.")

    processed_audio_chunks = []

    try:
        while True:
            # Read a chunk of audio from the input stream
            audio_chunk = audio_processor.input_stream.read(1024)
            # Process the audio chunk
            processed_chunk = audio_processor.process_audio(audio_chunk, scenario)
            # Write the processed audio to the output stream
            audio_processor.output_stream.write(processed_chunk)
            # Store the processed chunk for saving
            processed_audio_chunks.append(processed_chunk)
    except KeyboardInterrupt:
        print("\nStopping audio processing.")
    finally:
        # Stop the audio streams and save the output
        audio_processor.stop_stream()
        audio_processor.save_audio(processed_audio_chunks, f'output/processed_{scenario}_audio.wav')
        print(f"Processed audio saved to 'output/processed_{scenario}_audio.wav'.")

if __name__ == "__main__":
    main()
