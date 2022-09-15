How to run: 
Download the WHOLE folder Nick posted on google drive - something like 26,181 files 
Unzip the downloaded folder (to do this right click on the folder and select “Extract All” or “Extract”
For Windows: 
Open your computer’s terminal 
cd to the unzipped folder and open the folder 
Set your restriction to unrestricted: 
Command: Set-ExecutionPolicy Unrestricted
Create a virtual environment (Nick’s isn’t sufficient since VE’s are different between Windows and MacOS) 
Command: python -m venv <yolo_env2>
Note: <yolo_env2> is just whatever you want to name the environment 
Copy the contents from Nick’s yolo_env/bin folder 
Paste (without replacing the existing files) into your new virtual environment’s Scripts folder (when it asks if you want to replace the existing 10-ish files, SAY NO) 
Back in the terminal - activate your virtual environment 
Command: .\<yolo_env2>\Scripts\activate 

For MacOS:
Open your computer’s terminal
cd to the unzipped folder and open the folder
Open yolo_env virtual environment
Command: source yolo_env/bin/activate

Continue here:
Install the required libraries
Command: pip install -r requirements.txt 
Command: pip install pillow
Command: pip install ffpyplayer 
Command: python -m pip install --upgrade pip setuptools virtualenv
Command: python -m pip install "kivy[base]" kivy_examples
Run the program: 
Commend: python main.py
Note: you must have the video you want evaluated in the same folder as main.py and named "sharkvideo.mp4" 

Note: if issues pop up with python or pip command, try python3 & pip3
