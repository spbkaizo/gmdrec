""" Loading user settings.

    Probably should expose a dataclass.
"""
import yaml
import logging

try:
    with open('settings.conf') as config_file:
        settings = yaml.safe_load(config_file)
except (FileNotFoundError, IOError):
    logging.warning('settings.conf file not found')

recorder = ''
URI = ''

client_id = settings['client_id']
client_secret = settings['client_secret']
server_url = settings['server_url']
wipers = settings['calibration']
