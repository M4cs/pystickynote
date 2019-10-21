from pystickynote.paths import CONFIG_PATH, NOTES_PATH, PATH_DIR
from configparser import ConfigParser
import os

example_config = """\
[DEFAULT]
background_color = #454545
text_color = #fafafa
alpha = 0.8
border_width = 0
title_size = 8
font_size = 10
box_height = 5
box_width = 50"""

class Config:
    def __init__(self):
        self.config = ConfigParser()
        if not os.path.exists(PATH_DIR):
            os.makedirs(PATH_DIR)
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'w') as file:
                file.write(example_config)
        if not os.path.exists(NOTES_PATH):
            with open(NOTES_PATH, 'w') as file:
                file.write('{}')
        self.config.read(CONFIG_PATH)
        self.config_dict = self.config['DEFAULT']
        self.background_color = self.config_dict['background_color']
        self.text_color = self.config_dict['text_color']
        self.alpha = self.config_dict['alpha']
        self.border_width = self.config_dict['border_width']
        self.font_size = self.config_dict['font_size']
        self.title_size = self.config_dict['title_size']
        try:
            self.height = self.config_dict['box_height']
            self.width = self.config_dict['box_width']
        except KeyError:
            self.config['DEFAULT']['box_height'] = '5'
            self.config['DEFAULT']['box_width'] = '50'
            with open(CONFIG_PATH, 'w') as config_file:
                self.config.write(config_file)
            self.height = self.config_dict['box_height']
            self.width = self.config_dict['box_width']