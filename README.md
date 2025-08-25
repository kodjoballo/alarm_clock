# ⏰ Alarm Clock

## 📌 Description
A simple **Python alarm clock** that counts down for a given number of minutes and seconds, then plays a sound (`alarm.mp3`) when the timer reaches zero.  

It uses:
- **`time`** → to track countdown  
- **ANSI escape codes** → to update the timer dynamically in the terminal  
- **`playsound`** → to play an audio file when time is up  

---

## 🚀 How to Run

### 1. Install Dependencies
This project requires the `playsound` module. Install it with:

```js
pip install playsound
```

⚠️ If installation fails, try:

```js

python -m pip install playsound
pip install --upgrade setuptools wheel

```

### 2. Add an Alarm Sound

Place an audio file named alarm.mp3 in the project directory.
Example:

```js
alarm_clock/
│
├── alarm_clock.py
└── alarm.mp3
```

### 3. Run the Program

From the project folder:
```js
python.exe alarm_clock.py
```

or from any python interpreter

You will be asked to input:

Minutes

Seconds

Example:

```js

Please provide the minutes: 0
Please provide the seconds: 10

```


The timer counts down and plays the alarm sound when finished.

### 4. 🖼️ Screenshot

<p align="center">

![image alt](https://github.com/kodjoballo/alarm_clock/blob/main/Alarm_clock.png?raw=true)

</p>


### 5. 📚 Concepts Used

Countdown timer with time.sleep()

User input with input()

Formatted output with f-strings ({minutes:02d}:{seconds:02d})

Playsound library to play audio files

Terminal control with ANSI escape codes (\033[H\033[J)


### ⚠️ Notes

The dynamic countdown display works best in a real terminal, not in IDE consoles.

Ensure your alarm.mp3 is a short, valid audio file (MP3 or WAV).

On some systems, playsound may require additional codecs.


### Source code here 👇


[source_code](https://github.com/kodjoballo/alarm_clock/blob/main/alarm_clock.py)



