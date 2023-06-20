import pyautogui
import time
import random

class MapMakerBot:
    def __init__(self):
        self.keys = ['space', 'd', 'a', 'c']
        self.key_movement = {'space': (0, 1), 'd': (1, 0), 'a': (-1, 0), 'c': (0, -1)}
        self.position = (0, 0)
        self.previous_key = None
        self.object_positions = []
        self.repetitions = int(input('How many repetitions? '))
        self.frequency = int(input('How often to place object (0 for always, otherwise type in one integer (HIGHLY recommend between 0-1 but you can raise as much as you want.) '))
        self.space = int((input('How much space to randomize between movement? (1 movement = 1 keyboard press in a given direction, recommend between 7-15 but its up to you.): ')))
        if input('Stack objects one on top of the other? (y/n) ').lower() == 'y':
            self.stack = True
        else:
            self.stack = False
        self.seconds = float(input('How many milliseconds between keyboard presses (recommended between 0-1?) '))
        self.bounding_values = input('What are the bounding values? (min_x, min_y, max_x, max_y). Make sure to separate each number with a comma. ').split(', ')
        self.min_x = float(self.bounding_values[0])
        self.min_y = float(self.bounding_values[1])
        self.max_x = float(self.bounding_values[2])
        self.max_y = float(self.bounding_values[3])
        print('min_x: ', self.min_x, 'min_y: ', self.min_y, 'max_x: ', self.max_x, 'max_y: ', self.max_y)
        self.xscale, self.yscale, self.zscale = None, None, None
        self.pitch, self.yaw, self.roll = None, None, None
        self.xpos, self.ypos, self.zpos = None, None, None
        self.get_object_properties()
        print('Starting in 10 seconds...')
        time.sleep(10)  # initial pause

    def get_object_properties(self):
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

            position_enabled = input('Enable position modification? (y/n) ')

            if position_enabled.lower() == 'y':

                self.xpos = input('Which x_position? (you can also type "default" for default or "r" for random) ')
                self.ypos = input('Which y_position? (you can also type "default" for default or "r" for random) ')
                if self.stack is False:
                    self.zpos = input('Which z_position? (you can also type "default" for default, "r" for random or "floor" if you want the object placed on the ground.) ')
                    if self.zpos == 'floor':
                        self.zpos = 505.71

                if self.xpos != 'default' and self.xpos != 'r':
                    self.xpos = int(self.xpos)
                if self.ypos != 'default' and self.ypos != 'r':
                    self.ypos = int(self.ypos)
                if self.stack is False:
                    if self.zpos != 'default' and self.zpos != 'r':
                        self.zpos = int(self.zpos)


            # Ask whether to enable scale modification
            scale_enabled = input('Enable scale modification? (y/n) ')
            if scale_enabled.lower() == 'y':

                self.xscale = input('What xscale? (type "default" for default or "r" for random) ')
                self.yscale = input('What yscale? (type "default" for default or "r" for random) ')
                self.zscale = input('What zscale? (type "default" for default or "r" for random) ')

                if self.xscale != 'default' and self.xscale != 'r':
                    self.xscale = int(self.xscale)
                if self.yscale != 'default' and self.yscale != 'r':
                    self.yscale = int(self.yscale)
                if self.zscale != 'default' and self.zscale != 'r':
                    self.zscale = int(self.zscale)
        else:
            self.object_properties = False

    def press_key(self, key, press_count=1):
        for _ in range(press_count):
            pyautogui.keyDown(key)
            pyautogui.keyUp(key)

    def add_object(self):

        self.press_key('r')
        self.press_key('enter')
        time.sleep(self.seconds)
        if self.object_properties:

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
                        pyautogui.typewrite(str(random.randint(16, 300)))
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('xscale', self.xscale)

            self.press_key('s')
            if self.yscale != 'default':
                if self.yscale is not None:
                    if self.yscale != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('yscale', self.yscale)
                        pyautogui.typewrite(str(self.yscale))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('yscale', self.yscale)
                        pyautogui.typewrite(str(random.randint(16, 300)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')
            if self.zscale != 'default':
                if self.zscale is not None:
                    if self.zscale != 'r':
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('zscale', self.zscale)
                        pyautogui.typewrite(str(self.zscale))
                        self.press_key('enter')
                    else:
                        self.press_key('enter')
                        time.sleep(self.seconds)
                        print('zscale', self.zscale)
                        pyautogui.typewrite(str(random.randint(16, 300)))
                        self.press_key('enter')

            # Input position
            for _ in range(4):
                print('pressing s')
                self.press_key('s')
                time.sleep(self.seconds)

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
                        pyautogui.typewrite(str(random.randint(-2000, 2000)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')

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
                        pyautogui.typewrite(str(random.randint(-2000, 2000)))
                        self.press_key('enter')

            time.sleep(self.seconds)
            self.press_key('s')

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
                            pyautogui.typewrite(str(random.randint(500, 1800)))
                            self.press_key('enter')
                        else:
                            self.press_key('enter')
                            time.sleep(self.seconds)
                            print('zpos', self.zpos)
                            pyautogui.typewrite(str(self.zpos))
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

    def next_position(self, key, press_count):
        return (self.position[0] + self.key_movement[key][0] * press_count,
                self.position[1] + self.key_movement[key][1] * press_count)

    def within_bounding_box(self, position):
        return self.min_x <= position[0] <= self.max_x and self.min_y <= position[1] <= self.max_y

    def generate_map(self, repetitions):
        for _ in range(repetitions):
            randomizer = random.randint(0, self.frequency)

            if randomizer == 0 and self.position not in self.object_positions:
                self.add_object()
                self.object_positions.append(self.position)

            while True:
                current_key = random.choice(self.keys)
                if current_key != self.previous_key:
                    press_count = random.randint(5, self.space)
                    new_position = self.next_position(current_key, press_count)

                    if self.within_bounding_box(new_position):
                        self.press_key(current_key, press_count)
                        self.previous_key = current_key
                        self.position = new_position
                        break
                    else:
                        self.previous_key = None

    def reset_position(self):
        x_distance = self.position[0]
        y_distance = self.position[1]

        x_key = 'd' if x_distance < 0 else 'a'
        y_key = 'space' if y_distance < 0 else 'c'

        for _ in range(abs(x_distance)):
            self.press_key(x_key, 1)
        for _ in range(abs(y_distance)):
            self.press_key(y_key, 1)

        self.position = (0, 0)
        self.previous_key = None


while True:
# Using the bot, breaks when player types 'n'
    bot = MapMakerBot()
    bot.generate_map(bot.repetitions)
    bot.reset_position()
    if input('Would you like to add another object? (y/n) ') == 'n':
        break