# Simple Pomodoro App
This is a Python/Kivy-based application designed to enhance studying/programming using the pomodoro technique. It eliminates the need for using your phone, annoying ad-driven web or mobile apps,  manual time adjustments, and constraints on resizing the app to suit personal preferences while using it on your desktop.

The app follows the standard Pomodoro technique, offering predefined time intervals:

Pomodoro: 25 minutes
Short Break: 5 minutes
Long Break: 35 minutes

This is just my personal time preference for studying. If you wish to change the time to your liking, you may do so by changing the integer values in source code under: 

pomodoro_time = 25 * 60 <br>
short_break_time = 5 * 60 <br>
long_break_time = 35 * 60 <br>


# Installation
1. Clone this repository to your local machine using the following command:

git clone https://github.com/onelastbyt3/simplepomodoroapp.git

2. Ensure you have Python installed (version 3.10 or later).

3. Install the required dependencies by running the following command:

pip install -r requirements.txt

4. Run the app using the following command:

python simplepomodoroapp.py

# How to Use
Once the app is launched, there is a "Simple Pomodoro App" label along with three buttons: Pomodoro, Short Break, and Long Break.

Click the "Pomodoro" button to start a 25-minute study session, the "Short Break" button to initiate a 5-minute break, or the "Long Break" button to begin a 35-minute break. <br>
During each phase, a countdown timer will be displayed at the top-most box indicating the time remaining. <br>

The app will send notifications when each study or break block is completed. <br>
Additionally, you may resize the app to whatever size you want and have it anywhere on your screen. <br>

# License
This project is licensed under the MIT License.

# Contributions
Contributions to this project are welcome, as this was a simple project with many features/design elements still lacking such as pause functionality, time adjustment UI, and so forth. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Happy pomodoro-ing!
