<p align="center">
    <h3 align="center">
        <span style="font-size: 2em; font-weight: bold;">C</span>hunithm 
        <span style="font-size: 2em; font-weight: bold;">H</span>yper 
        <span style="font-size: 2em; font-weight: bold;">U</span>ltra 
        <span style="font-size: 2em; font-weight: bold;">S</span>creen 
        <span style="font-size: 2em; font-weight: bold;">A</span>lignment 
        <span style="font-size: 2em; font-weight: bold;">N</span>ormalizer
    </h3>
</p>


<br/>

## Introduction

This program helps you play Chunithm on a non-32 inch monitor by increasing the window size to emulate a 32 inch screen while aligning the bottom of the window with the bottom of your monitor. \
Note that because of that some elements in-game won't be visible anymore.

If you already own [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) and are too lazy to calculate the right scaling ratio and top pixels to crop, you can still follow the installation and run the program once to get the exact values depending on your screen.

## Requirements

This program was tested on Windows 11 with Python 3.11.7.

## Installation

1. Clone this repo and access it

	```bash
	git clone https://github.com/ValentinChanter/CHUSAN
	cd CHUSAN
	```

2. (Optional) Create and switch to your virtual environment if needed

	```bash
	python -m venv /path/to/new/virtual/environment
	source /path/to/new/virtual/environment/bin/activate
	# or
	conda create --name <my-env>
	conda activate <my-env>
	```

3. Install the python dependency

	```bash
	pip install -r requirements.txt
    # or
    pip install pygetwindow
	```

4. Change constants in the first lines of code to your screen size/resolution if needed

    ```py
    CURRENT_SCREEN_SIZE = 27        # in inches
    CURRENT_SCREEN_WIDTH = 2560     # in pixels
    CURRENT_SCREEN_HEIGHT = 1440    # in pixels
    ```

## Usage

1. Run the program using python. Press Ctrl+C to restore the original window size.

	```bash
	python ./main.py
	```

## Future improvements

Whenever I'll have time if I ever do, I'll likely:
- implement upscaling using DLSS and/or FSR
- add a `config.json` for the screen size/resolution