# import asyncio
# from hume import HumeVoiceClient, MicrophoneInterface

# async def main() -> None:
#   # Paste your Hume API key here
#   HUME_API_KEY = "WgtY0RhzqRizbtGKYxK3nqcFL9ZEfNXL2kroQdwzaJAoUwBd"
#   # Connect and authenticate with Hume
#   client = HumeVoiceClient(HUME_API_KEY)

#   # Start streaming EVI over your device's microphone and speakers
#   async with client.connect() as socket:
#       await MicrophoneInterface.start(socket, device=0)
# asyncio.run(main())

# ------------------ Import necessary packages from hume and audio interface ----------------
import asyncio
import traceback
import sounddevice as sd
from scipy.io.wavfile import write
import base64
import math
from hume import HumeStreamClient
from hume.models.config import BurstConfig, ProsodyConfig
from llm_control import generate_action
from msg_to_rsp import extract_msg

# ------------------ Record audio ----------------------
samplerate = 44100  # Hertz
duration = 4  # seconds
filename = 'output.wav'
print(f"Recording for {duration} seconds...")
myrecording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
print("Recording complete. Saving the audio as output.wav")
write(filename, samplerate, myrecording)

# ------------------ Function to encode audio (base64 encoding) ---------------------
def encode_audio(filename):
    with open(filename, 'rb') as audio_file:
        return base64.b64encode(audio_file.read())

# ------------------ Hume API interaction -------------------------------------------
async def main():
    try:
        client = HumeStreamClient("API key here")
        burst_config = BurstConfig()
        prosody_config = ProsodyConfig()
        async with client.connect([burst_config, prosody_config]) as socket:
            encoded_audio = encode_audio(filename)
            await socket.reset_stream()
            result = await socket.send_bytes(encoded_audio)
            print("Received response from Hume")
            return result  # return the result
    except Exception:
        print(traceback.format_exc())


result = {}
result = asyncio.run(main())
# print(result)
# Below is specific to IPython/Jupyter Notebook:
# result = await main()  # 'await' can be used directly in a cell in Jupyter Notebook
# print(result)

# ------------- Sort the score from the result ---------------
score_raw = []
for i in range(48):
    score_raw.append(result['prosody']['predictions'][0]['emotions'][i]['score'])

# ------------- Find the first two highest score emotions ---------
score = score_raw[:]
score.sort(reverse=True)
index = score_raw.index(score[0])
# print(score[0])
# print(index)
# print(score_raw)
# print(result['prosody']['predictions'][0]['emotions'])
PC_1 = ''
PC_2 = ''
for i in range(48):
    if math.isclose(result['prosody']['predictions'][0]['emotions'][i]['score'], score[0], rel_tol=1e-19):
        PC_1 = result['prosody']['predictions'][0]['emotions'][i]['name']
for i in range(48):
    if math.isclose(result['prosody']['predictions'][0]['emotions'][i]['score'], score[1], rel_tol=1e-19):
        PC_2 = result['prosody']['predictions'][0]['emotions'][i]['name']
print(PC_1)
print(PC_2)

target_emotion = 'angry'
llm_response = generate_action(PC_1+' and '+PC_2, target_emotion)
print(llm_response)