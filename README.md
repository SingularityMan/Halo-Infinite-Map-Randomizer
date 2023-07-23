# Halo-Infinite-Map-Randomizer

Map Maker Bot is a Python script that uses PyAutoGUI to automate key presses and generate a map. It's primarily used to add objects to a grid in a pseudo-random manner based on user's specifications.

To get started, you will need Python 3, openai and the PyAutoGUI library.

You can install PyAutoGUI and openai via pip:

pip install pyautogui
pip install openai

Note: Make sure to have an API Key from Openai. You won't be able to use GPT-4 without it but you can still use it manually if you don't have an API key.

Instructions for Best Results:

Include your api key in either the "api_key" file or inside the system environment variables, whichever you prefer, in order to use GPT-4.

1. Download the optimized map for this bot from this link: [halowaypoint.com](https://www.halowaypoint.com/halo-infinite/ugc/maps/2cc7880e-f7bb-4bb4-9c07-bbb6c6189a07). While you may choose any map, the above-mentioned one is optimized for randomization.

2. Once your map is loaded, choose the object you'd like to have randomized. It's recommended to use only static objects as the script is primarily designed for them. Make sure to leave the object highlighted before exiting the object browser table.

![Image 1](https://github.com/SingularityMan/Halo-Infinite-Map-Randomizer/blob/main/Halo%20Infinite%206_19_2023%209_13_19%20PM.png)

3. Select the highlighted object and add it to the map. Proceed to the object properties menu, which is adjacent to the object browser menu. Ensure that your settings match the image below (paying special attention to the highlighted "Size X" tab), and leave the Object Mode, Transform, Position, and Rotation tabs open:

![Image 2](https://github.com/SingularityMan/Halo-Infinite-Map-Randomizer/blob/main/Halo%20Infinite%206_19_2023%209_13_33%20PM.png)
  
4. Return to the object browser with the desired object still highlighted, then close the object browser and delete the object from the map.

5. Switch to test mode, wait for a moment, then return to Forge mode. Position your view to look straight down at the ground, in a top-down view.

![Image 3](https://github.com/SingularityMan/Halo-Infinite-Map-Randomizer/blob/main/Halo%20Infinite%206_19_2023%209_12_40%20PM.png)

6. Run the mapmakerbot.py script and carefully follow the instructions on the console. This stage is delicate as the script allows for a lot of customization and object transformation, but has limited error handling. Paying careful attention can help prevent errors, crashes, or unexpected outcomes.

# Running the Script

To run the script, simply clone the repository and execute the script with Python.

Usage
When you run the script, it will prompt you for several inputs:

1. Whether to use GPT-4 to generate a structure or biome. If the user answers 'y' then you will be prompted to choose between mode 1 (structures) or mode 2 (biomes). Then it will ask you what to build. Make sure to specify how many objects to add on the map. You should also be very specific, such as where to add them (x,y,z coordinates) and how many to add. Keep in mind, GPT-4 is not very good at building structures but it is very good at creating biomes. Makes sure you have the desired object highlighted before continuing.

2. If you answered 'n' then you will be prompted to specify how many repetitions, i.e. how many objects to add to the map.

3. Whether to randomize object selection. Default is 1 but you can specify as much as you'd like within the same object subfolder. Good for planting different types of trees, grass, foliage, etc.
   
4. Whether to stack objects one on top of the other. (for example placing trees on top of hills instead of directly on the ground)

5. How many milliseconds between key presses.

6. Whether to enable object properties. If you answer 'y' you can modify the rotation, position and scaling of the objects. You can leave it at "default", randomize with 'r' (which will prompt you to provide a range of randomization) or your own specified value. For the Z-axis, you can also specify "Floor" to place the object directly on the ground, which is 500 on the z-axis on the default randomization map. 

# Built With
Python 3
PyAutoGUI
GPT-4 API

# License
This project is licensed under the GNU General Public License Version 2, June 1991. See the LICENSE file for details.

# Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

# Authors
SingularityMan

# Acknowledgments:
Thanks to PyAutoGUI for providing the functionality that this project is based on.
