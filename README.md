# AutoShutdown
Auto shutdown the windows 10 device working on dark mode by just one click. The code closes all the program and then shuts the device.

## Installation of requred modules
1) cv2  
&nbsp;&nbsp;&nbsp;&nbsp;Using pip:
```bash
pip install opencv-python
```
&nbsp;&nbsp;&nbsp;&nbsp;Using conda:
```bash  
conda install -c conda-forge opencv
```
2) pyautogui
```bash
Using pip:
pip install pyautogui
Using conda:
conda install -c conda-forge pyautogui
```

## Usage
-> First save all your files which are currently unsaved.  
-> There are two ways to use this:  
    1) If you don't want to run the program from command line again and again, create a .exe file with [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/usage.html). Make the icon's view to Small/List/Details from view>your-choice.
    2) The common method, run the program from any ide. But, remember to make the view of the icon to Small/List/Details from the above mentioned method.

## Possible problems and their solutions
-> An Infinite Loop:
    Reasons:
        -Some files are not saved before the usage of program.
        -Icon view is not set to small/list/details.
    Solution:
        -Just smash the mouse pointer any of the corner of the screen.

## Warnings
    -Currently works on only dark mode.
    -Does not saves the work, it has to be done manually before running the program.
    -View of the icons should be set to small/list/details.