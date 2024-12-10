# logs.py
# author: Elouan Passereau
# date: 10.12.2024
# version: 1.0
# Description: This script contains the functions to log the actions of the script
# Usage: Import the script and use the log_action function to log the actions
# Example: log_action("This is a test", True, None, True)
# Example: log_action("This is a test", False, "This is an error", True)
# License: GPL-3.0 : https://www.gnu.org/licenses/gpl-3.0.html 


import os
from datetime import datetime

def create_log_directory(log_directory):
  """
    Create the log directory if it does not exist whith the path given in parameter
    :param log_directory: The path of the log directory
    :type log_directory: str
  """
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

def get_log_filename(log_directory):
  """
    Get the log filename with the path given in parameter
    :param log_directory: The path of the log directory
    :type log_directory: str
  """
    now = datetime.now()
    return f"{log_directory}{now.strftime('%Y-%m-%d_%H')}.log"

def log_action(action, success=True, error_message=None, empr=False):
  """
    Log the action with the success and the error message if there is one and print it if empr is True
    :param action: The action to log
    :type action: str
    
    :param success: The success of the action
    :type success: bool

    :param error_message: The error message if there is one
    :type error_message: str
  """

    log_filename = get_log_filename()
    with open(log_filename, 'a') as log_file:
        log_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Action: {action} - Success: {'Yes' if success else 'No'} - Error: {error_message}\n")
        if not success and error_message:
            log_file.write(f"\n")
    if empr==True:
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Action: {action} - Success: {'Yes' if success else 'No'} - Error: {error_message}")
