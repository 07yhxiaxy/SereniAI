# Author: Yuxuan Du & Mark Xia
import cv2
import asyncio
import math
from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig
# Specify the path to save the image
save_path = './saved_img.jpg'
# Initialize the webcam
webcam = cv2.VideoCapture(0)
# finally:
    # Ensure the webcam is released and all OpenCV windows are closed
    # webcam.release()
    # cv2.destroyAllWindows()
    # print("Camera off. Program ended.")
async def main():
    while True:
        # Video capture part
        if not webcam.isOpened():
            print("Error: Camera is not accessible.")
            exit()
        try:
            # Attempt to capture a frame from the webcam
            check, frame = webcam.read()
            # If a frame was not captured successfully, continue to the next iteration
            if not check:
                print("Failed to capture frame.")
            # Display the captured frame in a window
            cv2.imshow("Capturing", frame)
            if frame is not None:
                cv2.imwrite(save_path, frame)
                print(f"Image saved at {save_path}!")
            # key = cv2.waitKey(1) & 0xFF
            # # If 's' is pressed, save the image
            # if key == ord('q'):
            #     break
            # # If 'q' is pressed, quit the program
            # else:
            #     if frame is not None:
            #         cv2.imwrite(save_path, frame)
            #         print(f"Image saved at {save_path}!")
            #     else:
            #         print("No frame to save.")
            #     break
        except KeyboardInterrupt:
            # Handle the case where the script is interrupted by the user
            print("Caught KeyboardInterrupt, shutting down.")
            webcam.release()
            cv2.destroyAllWindows()
        # Hume part
        client = HumeStreamClient("tnMeVDLCMKY1GAn6iPbVXdGlDFFWZL76jwZUXlg2kGf7MTPM")
        config = FaceConfig(identify_faces=True)
        async with client.connect([config]) as socket:
            result = await socket.send_file("./saved_img.jpg")
            # print(result)
            if(len(result['face'])==1):
                # print("ok")
                # print(result)
                score_raw = []
                for i in range(48):
                    score_raw.append(result['face']['predictions'][0]['emotions'][i]['score'])
                # ------------- Find the first two highest score emotions ---------
                score = score_raw[:]
                score.sort(reverse=True)
                index = score_raw.index(score[0])
                PC_1 = ''
                PC_2 = ''
                for i in range(48):
                    if math.isclose(result['face']['predictions'][0]['emotions'][i]['score'], score[0], rel_tol=1e-19):
                        PC_1 = result['face']['predictions'][0]['emotions'][i]['name']
                for i in range(48):
                    if math.isclose(result['face']['predictions'][0]['emotions'][i]['score'], score[1], rel_tol=1e-19):
                        PC_2 = result['face']['predictions'][0]['emotions'][i]['name']
                print(PC_1)
                print(PC_2)
asyncio.run(main())