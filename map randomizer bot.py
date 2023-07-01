import pyautogui
import time
import random
import openai
import ast

class MapMakerBot:
    def __init__(self):

        # Include ai_generate as a global variable
        global ai_generate
        global tuple_list

        if ai_generate:
            self.ai_generate = True
        else:
            self.ai_generate = False

        # self.keys = ['space', 'd', 'a', 'c']
        # self.key_movement = {'space': (0, 1), 'd': (1, 0), 'a': (-1, 0), 'c': (0, -1)}
        # self.position = (0, 0)
        # self.previous_key = None
        # self.object_positions = []

        if self.ai_generate:
            self.repetitions = len(tuple_list)
        else:
            self.repetitions = range(int(input('How many repetitions? ')))
        self.tab_selection = input('Randomize object selection? (y/n) ')
        if self.tab_selection.lower() == 'y':
            self.tab_selection = 1
            self.tab_selection_destination_end = int(input('Randomize ending point for object selection (must be greater than 1)? '))
            self.tab_selection_destination = random.randint(1, self.tab_selection_destination_end)
            if self.tab_selection_destination_end < 1:
                self.tab_selection_destination_end = 1
        else:
            self.tab_selection = 0
            self.tab_selection_destination = 0
        #self.frequency = int(input('How often to place object (0 for always, otherwise type in one integer (HIGHLY recommend between 0-1 but you can raise as much as you want.) '))
        #self.space = int((input('How much space to randomize between movement? (1 movement = 1 keyboard press in a given direction, recommend between 7-15 but its up to you.): ')))
        if input('Stack objects one on top of the other? (y/n) ').lower() == 'y':
            self.stack = True
        else:
            self.stack = False
        self.seconds = float(input('How many milliseconds between keyboard presses (recommended between 0-1?) '))

        """self.bounding_values = input('What are the bounding values? (min_x, min_y, max_x, max_y). Make sure to separate each number with a comma. ').split(', ')
        self.min_x = float(self.bounding_values[0])
        self.min_y = float(self.bounding_values[1])
        self.max_x = float(self.bounding_values[2])
        self.max_y = float(self.bounding_values[3])
        print('min_x: ', self.min_x, 'min_y: ', self.min_y, 'max_x: ', self.max_x, 'max_y: ', self.max_y)"""

        self.xscale, self.yscale, self.zscale = None, None, None
        self.xscale_min, self.yscale_min, self.zscale_min, self.xscale_max, self.yscale_max, self.zscale_max = None, None, None, None, None, None
        self.pitch, self.yaw, self.roll = None, None, None
        self.pitch_min, self.yaw_min, self.roll_min, self.pitch_max, self.yaw_max, self.roll_max = None, None, None, None, None, None
        self.xpos, self.ypos, self.zpos = None, None, None
        self.xpos_min, self.ypos_min, self.zpos_min, self.xpos_max, self.ypos_max, self.zpos_max = None, None, None, None, None, None
        self.get_object_properties()
        print('Starting in 10 seconds...')
        time.sleep(10)  # initial pause

    def get_object_properties(self):

        if self.ai_generate:
            object_properties = 'y'
        else:
            object_properties = input('Enable object properties? (y/n) ')

        if object_properties.lower() == 'y':
            self.object_properties = True

            # Ask whether to enable rotation modification
            rotation_enabled = input('Enable rotation modification? (y/n) ')

            # Ask for rotation values
            if rotation_enabled.lower() == 'y':

                self.pitch = input('What pitch? (you can also type "default" for default or "r" for random) ')
                self.yaw = input('What yaw? (you can also type "default" for default or "r" for random) ')
                self.roll = input('What roll? (you can also type "default" for default or "r" for random) ')

                if self.pitch != 'default' and self.pitch != 'r':
                    self.pitch = int(self.pitch)
                if self.yaw != 'default' and self.yaw != 'r':
                    self.yaw = int(self.yaw)
                if self.roll != 'default' and self.roll != 'r':
                    self.roll = int(self.roll)

            if self.ai_generate:
                position_enabled = 'y'
            else:
                position_enabled = input('Enable position modification? (y/n) ')

            if position_enabled.lower() == 'y':

                if self.ai_generate is False:
                    self.xpos = input('Which x_position? (you can also type "default" for default or "r" for random) ')
                    self.ypos = input('Which y_position? (you can also type "default" for default or "r" for random) ')

                    if self.stack is False:
                        self.zpos = input('Which z_position? (you can also type "default" for default, "r" for random or "floor" if you want the object placed on the ground.) ')
                        if self.zpos == 'floor':
                            self.zpos = 500

                    if self.xpos != 'default' and self.xpos != 'r':
                        self.xpos = int(self.xpos)
                    elif self.xpos == 'r':
                        self.xpos_min = int(input('What is the minimum x position? '))
                        self.xpos_max = int(input('What is the maximum x position? '))

                    if self.ypos != 'default' and self.ypos != 'r':
                        self.ypos = int(self.ypos)
                    elif self.ypos == 'r':
                        self.ypos_min = int(input('What is the minimum y position? '))
                        self.ypos_max = int(input('What is the maximum y position? '))

                    if self.stack is False:
                        if self.zpos != 'default' and self.zpos != 'r':
                            self.zpos = int(self.zpos)
                        elif self.zpos == 'r':
                            self.zpos_min = int(input('What is the minimum z position? '))
                            self.zpos_max = int(input('What is the maximum z position? '))

            # Ask whether to enable scale modification
            scale_enabled = input('Enable scale modification? (y/n) ')
            if scale_enabled.lower() == 'y':

                self.xscale = input('What xscale? (type "default" for default or "r" for random) ')
                self.yscale = input('What yscale? (type "default" for default or "r" for random) ')
                self.zscale = input('What zscale? (type "default" for default or "r" for random) ')

                if self.xscale != 'default' and self.xscale != 'r':
                    self.xscale = int(self.xscale)
                elif self.xscale == 'r':
                    self.xscale_min = input('What is the minimum xscale? ')
                    self.xscale_max = input('What is the maximum xscale? ')
                    self.xscale_min = int(self.xscale_min)
                    self.xscale_max = int(self.xscale_max)
                if self.yscale != 'default' and self.yscale != 'r':
                    self.yscale = int(self.yscale)
                elif self.yscale == 'r':
                    self.yscale_min = input('What is the minimum yscale? ')
                    self.yscale_max = input('What is the maximum yscale? ')
                    self.yscale_min = int(self.yscale_min)
                    self.yscale_max = int(self.yscale_max)
                if self.zscale != 'default' and self.zscale != 'r':
                    self.zscale = int(self.zscale)
                elif self.zscale == 'r':
                    self.zscale_min = input('What is the minimum zscale? ')
                    self.zscale_max = input('What is the maximum zscale? ')
                    self.zscale_min = int(self.zscale_min)
                    self.zscale_max = int(self.zscale_max)
        else:
            self.object_properties = False

    def press_key(self, key, press_count=1):
        for _ in range(press_count):
            pyautogui.keyDown(key)
            pyautogui.keyUp(key)

    def add_object(self, x_ai=None, y_ai=None, z_ai=None):

        # Open object browser menu
        self.press_key('r')

        # Randomize tab selection if enabled
        if self.tab_selection != 0:
            self.tab_selection_destination = random.randint(1, self.tab_selection_destination_end+1)
            while self.tab_selection < self.tab_selection_destination:
                self.press_key('s')
                self.tab_selection += 1
            while self.tab_selection > self.tab_selection_destination:
                self.press_key('w')
                self.tab_selection -= 1

        self.press_key('enter')
        time.sleep(self.seconds)
        if self.object_properties or self.ai_generate:

            self.press_key('r')
            #pyautogui.mouseInfo()
            for _ in range(4):
                time.sleep(self.seconds)
                self.press_key('q')

            time.sleep(self.seconds)

            if self.xscale != 'default':
                if self.xscale is not None:
                    if self.xscale != 'r':
                        self.press_key('enter')
                        pyautogui.typewrite(str(self.xscale))
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('xscale', self.xscale)
                    else:
                        self.press_key('enter')
                        pyautogui.typewrite(str(random.randint(self.xscale_min, self.xscale_max)))
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        # print('xscale', self.xscale)

            self.press_key('s')
            if self.yscale != 'default':
                if self.yscale is not None:
                    if self.yscale != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        # print('yscale', self.yscale)
                        pyautogui.typewrite(str(self.yscale))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        # print('yscale', self.yscale)
                        pyautogui.typewrite(str(random.randint(self.yscale_min, self.yscale_max)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')
            if self.zscale != 'default':
                if self.zscale is not None:
                    if self.zscale != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        # print('zscale', self.zscale)
                        pyautogui.typewrite(str(self.zscale))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        # print('zscale', self.zscale)
                        pyautogui.typewrite(str(random.randint(self.zscale_min, self.zscale_max)))
                        self.press_key('enter')

            # Input position
            for _ in range(4):
                print('pressing s')
                self.press_key('s')
                time.sleep(self.seconds)

            if x_ai is None:
                if self.xpos != 'default':
                    if self.xpos is not None:
                        if self.xpos != 'r':
                            self.press_key('enter')
                            time.sleep(self.seconds)
                            print('xpos', self.xpos)
                            pyautogui.typewrite(str(self.xpos))
                            self.press_key('enter')
                        else:
                            self.press_key('enter')
                            time.sleep(self.seconds)
                            print('xpos', self.xpos)
                            pyautogui.typewrite(str(random.randint(self.xpos_min, self.xpos_max)))
                            self.press_key('enter')
            else:
                self.press_key('enter')
                time.sleep(self.seconds)
                print('xpos', self.xpos)
                pyautogui.typewrite(str(x_ai))
                self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')

            if y_ai is None:
                if self.ypos != 'default':
                    if self.ypos is not None:
                        if self.ypos != 'r':
                            self.press_key('enter')
                            time.sleep(self.seconds)
                            print('ypos', self.ypos)
                            pyautogui.typewrite(str(self.ypos))
                            self.press_key('enter')
                        else:
                            self.press_key('enter')
                            time.sleep(self.seconds)
                            print('ypos', self.ypos)
                            pyautogui.typewrite(str(random.randint(self.ypos_min, self.ypos_max)))
                            self.press_key('enter')
            else:
                self.press_key('enter')
                time.sleep(self.seconds)
                print('ypos', self.ypos)
                pyautogui.typewrite(str(y_ai))
                self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')

            if z_ai is None:
                if self.stack is False:
                    if self.zpos != 'default':
                        if self.zpos is not None:
                            if self.zpos != 'r':
                                self.press_key('enter')
                                time.sleep(self.seconds)
                                print('zpos', self.zpos)
                                pyautogui.typewrite(str(self.zpos))
                                self.press_key('enter')
                            elif self.zpos == 'r':
                                self.press_key('enter')
                                time.sleep(self.seconds)
                                print('zpos', self.zpos)
                                pyautogui.typewrite(str(random.randint(self.zpos_min, self.zpos_max)))
                                self.press_key('enter')
                            else:
                                self.press_key('enter')
                                time.sleep(self.seconds)
                                print('zpos', self.zpos)
                                pyautogui.typewrite(str(self.zpos))
                                self.press_key('enter')
            else:
                self.press_key('enter')
                time.sleep(self.seconds)
                print('zpos', self.zpos)
                pyautogui.typewrite(str(z_ai))
                self.press_key('enter')

            time.sleep(self.seconds)
            for _ in range(2):
                self.press_key('s')
                time.sleep(self.seconds)

            if self.yaw != 'default':
                if self.yaw is not None:
                    if self.yaw != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('yaw', self.yaw)
                        pyautogui.typewrite(str(self.yaw))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('yaw', self.yaw)
                        pyautogui.typewrite(str(random.randint(0, 180)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')
            if self.pitch != 'default':
                if self.pitch is not None:
                    if self.pitch != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('pitch', self.pitch)
                        pyautogui.typewrite(str(self.pitch))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('pitch', self.pitch)
                        pyautogui.typewrite(str(random.randint(0, 180)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')
            if self.roll != 'default':
                if self.roll is not None:
                    if self.roll != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('roll', self.roll)
                        pyautogui.typewrite(str(self.roll))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('roll', self.roll)
                        pyautogui.typewrite(str(random.randint(0, 180)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            # Press w
            for _ in range(12):
                self.press_key('w')
                time.sleep(self.seconds)
            print('pressing w')
            time.sleep(self.seconds)
            self.press_key('q')
            self.press_key('r')

        if self.stack is True:
            self.press_key('end')

    """def next_position(self, key, press_count):
        return (self.position[0] + self.key_movement[key][0] * press_count,
                self.position[1] + self.key_movement[key][1] * press_count)

    def within_bounding_box(self, position):
        return self.min_x <= position[0] <= self.max_x and self.min_y <= position[1] <= self.max_y"""

    def generate_map(self, repetitions):

        for _, __ in enumerate(repetitions):

            """# randomizer = 0

            # if randomizer == 0:"""

            if self.ai_generate:
                self.add_object(x_ai=__[0], y_ai=__[1], z_ai=__[2])
            else:
                self.add_object()

                """if self.position not in self.object_positions:
                    self.object_positions.append(self.position)"""

            """if self.space > 0:
                while True:
                    current_key = random.choice(self.keys)
                    if current_key != self.previous_key:
                        press_count = random.randint(1, self.space)
                        new_position = self.next_position(current_key, press_count)

                        if self.within_bounding_box(new_position):
                            self.press_key(current_key, press_count)
                            self.previous_key = current_key
                            self.position = new_position
                            break
                        else:
                            self.reset_position()
                            self.previous_key = None"""

    """def reset_position(self):
        x_distance = self.position[0]
        y_distance = self.position[1]

        x_key = 'd' if x_distance < 0 else 'a'
        y_key = 'space' if y_distance < 0 else 'c'

        for _ in range(abs(x_distance)):
            self.press_key(x_key, 1)
        for _ in range(abs(y_distance)):
            self.press_key(y_key, 1)

        self.position = (0, 0)
        self.previous_key = None"""

ai_generate = False
ai_pass = False
mode = 0
tuple_list = []

while True:

    # Use GPT-4 to create a structure in Halo Infinite Forge
    if ai_generate is False:
        ai_generate = True if input("Would you like to use GPT-4 to generate a structure? (y/n) ") == 'y' else False
        if ai_generate is True:
            mode = int(input("Which mode would you like to use? (1, 2) "))
            query = input("What would you like to build? ")

            string1 = "You are a creative AI assistant skilled in architectural design within the environment of Halo Infinite Forge. Your task is to plan and create a 3D structure by arranging a specified number of 8x8x8 crates or any other type of object with dimensions specified by the player. These structures could range from simple designs like walls and towers, to complex ones like castles and mazes. Each crate can be placed anywhere within the coordinates of -2000 to 2000 on the X, Y and Z axis, and not less than 500 on the Z axis (ground level). You may stack objects on top of each other to form multilevel structures. The objects should be placed like lego bricks, adjacent to each other (unless otherwise specified by the user), although you may space them apart if necessary to create architectural features like rooms, halls, or corridors. To communicate your design, you will generate a list of comma-separated tuples containing (<x-axis integer>, <y-axis integer>, <z-axis integer>) coordinates, representing an object's position. Replace the letters in the tuple with an integer representing the corresponding axis. Replace the letters in the tuple with an integer representing the corresponding axis. Remember, we're working within a 3D space, so consider how your structure will look from all sides. Design  with intention and creativity, while keeping within the constraints of the specified number of objects and the game's coordinate system. Start with a foundation and build upwards, considering structural integrity, functionality, and aesthetics. Do not include any additional text or acknowledgement in your responses, only the list of coordinates. Make sure to contain the exact number of tuples for each object. Now, let's create something amazing!"
            string2 = "You are a creative AI assistant skilled in architectural design within the environment of Halo Infinite Forge. Your task is to plan and create a 3D structure by arranging a specified number of objects. These structures could range from simple designs like walls and towers, to complex ones like castles and mazes. Each object can be placed anywhere within the coordinates of -2000 to 2000 on the X and Y axis, and not less than 500 on the Z axis (ground level). The distribution and number of objects will be determined by the player. To communicate your design, you will generate a list of (x, y, z) coordinates, each representing an object's position, with each set of coordinates enclosed in parentheses and separated by commas, Replace the letters in the tuple with an integer representing the corresponding axis. Remember, we're working within a 3D space, so consider how your structure will look from all sides. Design  with intention and creativity, while keeping within the constraints of the specified number of objects and the game's coordinate system. Do not include any additional text or acknowledgement in your responses, only the list of coordinates and separate the output in paragraphs of tuples. Now, let's create something amazing!"

            match mode:
                case 1:
                    mode = string1
                case 2:
                    mode = string2

            while ai_generate and ai_pass is False:
                try:
                    ai_pass = False
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": mode},
                            {"role": "user", "content": "Build"+query}

                        ]
                    )

                    print(response.choices[0]['message']['content'])

                    response_string = response.choices[0]['message']['content']

                    # remove all whitespace
                    response_string = response_string.replace("\n", "").replace(" ", "")


                    # split the string into individual tuples
                    tuples = ast.literal_eval(response_string)

                    # create an empty list to hold the tuples
                    tuple_list = []

                    for tuple_string in tuples:
                        tuple_list.append(tuple_string)

                    print("DEBUG")
                    print(tuple_list)

                    response2 = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "Given the user query for a structure, '{}', and the generated coordinates: {} and the AI mode, which is {}. Does this set of coordinates accurately represent the requested structure or biome? Does the set of coordinates match the number of objects requested by the user? If it is a structure, does it follow design patterns set in architecture to resemble to object? If it is a biome, does it accurately reflect the requested quantity and distribution of the objects?\n"
                                                          "If it does, please respond with 'YES'. If not, provide a brief explanation about the discrepancy, suggest how the coordinates could be improved to more accurately represent the requested structure, and prompt the AI to generate a more accurate structure. For the sake of context, include the original output received as part of the feedback and specify the bot to output comma-separated tuples only, nothing more. Remember: The list of tuples generated by the AI represents the position of the objects. We want the combination of coordinates to accurately represent the object we are trying to build. Explain clearly what the requirements are, including the exact coordinate requirements requested (explicitly list the coordinate requirements, i.e. between -300 - 300 x axis, between 400 - 500 y axis, etc.). Be as detailed as possible and include an example of an improved output with comma-separated tuples written in the format: (<x-axis integer>, <y-axis integer>, <z-axis integer>). The z-coordinate of the floor is 500. \n".format(query, tuple_list, mode) }
                        ]
                    )

                    print(response2.choices[0]['message']['content'])

                    if 'YES' in response2.choices[0]['message']['content']:
                        ai_pass = True
                    else:
                        query = response2.choices[0]['message']['content']
                        ai_pass = False

                except:
                    print("ERROR")
                    continue

    # Using the bot, breaks when player types 'n'

    if ai_generate:
        bot = MapMakerBot()
        bot.generate_map(tuple_list)
    else:
        bot = MapMakerBot()
        bot.generate_map(bot.repetitions)
    # bot.reset_position()
    if input('Would you like to add another object? (y/n) ') == 'n':
        break
    else:
        ai_generate = False
        ai_pass = False
