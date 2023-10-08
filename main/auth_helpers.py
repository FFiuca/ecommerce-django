import threading

class Anon:
    pass

def get_current_user():
    return getattr(threading.local(), 'user', None)
