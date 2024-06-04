import configparser
import os

# Path to the configuration file
config_file_path = os.path.join(os.path.dirname(__file__), '../configurations/config.ini')

# Create a ConfigParser instance and read the configuration file
config = configparser.ConfigParser()
config.read(config_file_path)


# Function to get a setting from a specific section
def get_setting(section, option):
    return config.get(section, option)


# Function to get all settings from a specific section
def get_section(section):
    return dict(config.items(section))
