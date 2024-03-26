# Text To Speech
import playsound, asyncio, edge_tts, os

def get_cache_path():
    # Get the absolute path of the current file
    current_file_path = os.path.abspath(__file__)

    # Navigate up the directory tree four times
    parent_dir = current_file_path
    rel_current_path = os.path.relpath(__file__)
    for _ in range(len(rel_current_path.split(os.sep))):
        parent_dir = os.path.dirname(parent_dir)

    # Append "cache" directory to the parent directory
    return os.path.join(parent_dir, "bin\\cache")

# Speak out loud the text
def Speak(text, voice="en-US-GuyNeural"):
    output = os.path.join(get_cache_path(), "audio.mp3")
    if not os.path.isdir(get_cache_path()):
        os.mkdir(get_cache_path())

    # TTS engine
    async def _main(text, voice):
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(_main(text, voice))

    print(text)
    playsound.playsound(output)
    os.remove(output)
