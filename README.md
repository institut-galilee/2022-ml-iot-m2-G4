## Setup and Execution
- Make sure python3.9 is installed: `python3 --version`
- Launch this command to install developpment setup for the application `sudo apt-get install python3.9-dev libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0`
- Then launch this command `pip3 install -r requirements.txt ` to install required python package.
- Finally type `python3 main.py`to run the program.


Once the program start you can say some word listed in string pattern (in ther terminal) for example 'placement, teacher, test, school, etc. '. Once these words are detected by the program there will be a cheating.mp3 audio file will alerte the professeur then the programme will stop automatically<br>
You can also see the webcam detect some object like 'person, bicycle, car, etc.'.<br>
Object which are detectable by the webcam are listed in `coco.names`  

## Help
- If you have `_portaudio as pa` error go to this [site](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error) and try to run the steps mention in it. 



