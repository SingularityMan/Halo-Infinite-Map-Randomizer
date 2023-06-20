# Halo-Infinite-Map-Randomizer

Map Maker Bot is a Python script that uses PyAutoGUI to automate key presses and generate a map. It's primarily used to add objects to a grid in a pseudo-random manner based on user's specifications.

To get started, you will need Python 3 and the PyAutoGUI library.

You can install PyAutoGUI via pip:

pip install pyautogui

Instructions for Best Results:

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

1. Number of repetitions: The number of times to repeat the operation.

2. Frequency of object placement: How often to place an object. A value of 0 means always.

3. Space to randomize between movements: Defines the randomness in the bot's movement.

4. Stack objects: Whether to stack objects on top of each other.

5. Time between keyboard presses: The delay between keyboard actions.

6. Bounding values: The bounding values for the x and y coordinates of the map. It is used to limit the scope (or the area) of randomization.
It will also ask you for object properties like rotation, scale, and position (x, y, z). These parameters can be set to 'default', 'r' for random or specific numerical values.

# Built With
Python 3
PyAutoGUI

# License
This project is licensed under the GNU General Public License Version 2, June 1991. See the LICENSE file for details.

# Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

# Authors
SingularityMan

# Acknowledgments:
Thanks to PyAutoGUI for providing the functionality that this project is based on.
