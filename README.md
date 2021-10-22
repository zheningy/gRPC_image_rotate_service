# gRPC_image_rotate_service

Pre-requirement
-----------
* MacOS
* Python3

How to run
-----------
1. run `./setup`
2. run `./build`
3. run `./server --port <...> --host <...>` to start the server
4. In another terminal, run `./client --port <...> --host <...> --input <...> --output <...> --rotate <...> --mean` to process image


Future work
-----------
1. Right now this service use numpy to decode and encode image and opencv to process the image of ndarray format. Between rotate and mean filter, it would go through ndarray->NLImage, then NLImage->ndarray, which could be avoided if merge those two functions together.
2. For large image, I improve the gRPC message size limit to support it. However it would occupy more memory, a possible way to handle this could be chunk the original big image and send to the server in batches.

