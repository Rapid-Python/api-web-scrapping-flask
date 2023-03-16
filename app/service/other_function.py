from config import debug_flag

def check_debug():
    return True if debug_flag == 'True' else False

