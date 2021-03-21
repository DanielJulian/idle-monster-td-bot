## Idle Monster TD Bot Windows
 Python script to automate some of the mechanics of the IdleMonsterTD game using computer vision. Only works on windows

## How it works
Every X amounts of seconds the script will:

- Take a screenshot of the game window
- Match multiple templates against the screenshot using the template matching technique.
- If any template is found, the mechanic will be triggered by finding the coordinates of the template, and clicking on that position.



## Dependencies

Install the dependencies running:
```
pip install -r requirements.txt 
```


Then, you have to manually download and install the pywin32 wheel for your python and windows version
https://pypi.org/project/pywin32/
