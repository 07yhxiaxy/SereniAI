# import asyncio

# from hume import HumeStreamClient, StreamSocket
# from hume.models.config import FaceConfig

# async def main():
#     client = HumeStreamClient("YOUR API KEY")
#     config = FaceConfig(identify_faces=True)
#     async with client.connect([config]) as socket:
#         result = await socket.send_file("./face.jpg")
#         print(result)

# asyncio.run(main())

import subprocess # Replace 'script.sh' with the path to your Bash script 
ssh_command = 'ssh pi@172.20.10.3'
#result = subprocess.run(['ls'], text=True, capture_output=True)
mag = 'soft '
move = 'squeeze'
result = subprocess.run(['./execute_example_pi_commmand.sh',mag+move], text=True, capture_output=True)
print(result.stdout)