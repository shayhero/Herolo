#CONSTANTS
import inspect

URL = "https://automation.herolo.co.il/"
USERNAME = "viewer"
INSTANCE = "demo"
PASSWORD = "AStrip01"


def whoami():
    return inspect.stack()[1][3]
