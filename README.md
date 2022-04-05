## Setup and Execution
- Make sure python3.9 is installed: `python3 --version`
- Launch this command to install development setup for the application `sudo apt-get install python3.9-dev libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0`
- Then launch this command `pip3 install -r requirements.txt ` to install required python package.
- Then type this command `cd src`
- Finally, type `python3 main.py`to run the program.


Once the program start you can say some word listed in the string pattern (in the terminal) for example 'placement, teacher, test, school, etc. '. Once these words are detected by the program, there will be a audio file (output.mp3) alert the professor then the programme will stop automatically<br>
You can also see the webcam detect some object like 'person, bicycle, car, etc.'.<br>
The object which are detectable by the webcam are listed in `coco.names`  

## Source code from internet
  - Pranavan
    - For converting pdf to list of string: https://pymupdf.readthedocs.io/en/latest/tutorial.html 
    - For speech recognition: https://www.youtube.com/watch?v=9GJ6XeB-vMg&ab_channel=NeuralNine
    - For object detection: https://www.youtube.com/watch?v=1LCb1PVqzeY&ab_channel=eMasterClassAcademy  
  - Myriam
    - For  Communication with PC using Android: https://www.geeksforgeeks.org/how-to-communicate-with-pc-using-android/
    - For TensorFlow Lite Object Detection Android: https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/android

We used these sites to test our basic application and then we developed according to our application

## Help
- If you have `_portaudio as pa` error go to this [site](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error) and try to run the steps mention in it. 



