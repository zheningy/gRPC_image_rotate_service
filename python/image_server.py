from concurrent import futures
import logging

import grpc
import numpy as np
import cv2
import argparse
import image_pb2_grpc
from util import decode_image, encode_imgage  

MAX_MESSAGE_LENGTH = 1024 * 1024 * 64

class Image(image_pb2_grpc.NLImageServiceServicer):

    def RotateImage(self, request, context):
        rotate_img = decode_image(request.image)
    
        if request.rotation == 1:
            rotate_img = cv2.rotate(rotate_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif request.rotation == 2:
            rotate_img = cv2.rotate(rotate_img, cv2.ROTATE_180)
        elif request.rotation == 3:
            rotate_img = cv2.rotate(rotate_img, cv2.ROTATE_90_CLOCKWISE)
        return encode_imgage(rotate_img)

    
    def MeanFilter(self, request, context):
        mean_image = decode_image(request)
        kernel = np.ones((3,3),np.float32)/9
        mean_image = cv2.filter2D(mean_image, -1, kernel)
        return encode_imgage(mean_image)


def serve(port, host):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options = [
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
    ])
    image_pb2_grpc.add_NLImageServiceServicer_to_server(Image(), server)
    server.add_insecure_port(host + ':' + port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port', type=str
    )
    parser.add_argument(
        '--host', type=str
    )    
    args = parser.parse_args()
    serve(args.port, args.host)