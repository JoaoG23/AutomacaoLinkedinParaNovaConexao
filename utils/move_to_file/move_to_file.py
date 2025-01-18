import os
from utils.logging.log_manager.log_manager import write_to_log

def move_to_file(source, destination):
    try:
        os.rename(source, destination)

        write_to_log(f"File moved from {source} to {destination}")
    except FileNotFoundError as e:
        raise e
        