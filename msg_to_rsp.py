import socket
import re
def extract_msg(output_string):
    # Extract the content after 'magnitude:'
    magnitude_match = re.search(r'magnitude:\s*([^\,]+)', output_string)
    magnitude_content = magnitude_match.group(1) if magnitude_match else None
    # Extract the content after 'movement:'
    movement_match = re.search(r'movement:\s*([^\,]+)', output_string)
    movement_content = movement_match.group(1) if movement_match else None
    # print("Magnitude content:", magnitude_content)
    # print("Movement content:", movement_content)
    return magnitude_content, movement_content
def send_msg_to_rsp(magnitude, movement, ip_address, port=12345):
    # Create a socket object using AF_INET address family (IPv4) and SOCK_STREAM type (TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to server specified by ip_address and port
        s.connect((ip_address, port))
        # Format the message to be sent
        message = f'magnitude:{magnitude}, movement:{movement}'
        # Send the message
        s.sendall(message.encode('utf-8'))
        # Optionally, receive a response from the server
        response = s.recv(1024)
        print("Response from server:", response.decode('utf-8'))