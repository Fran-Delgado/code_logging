import logging
import os 

py_script = os.path.basename(__file__)

def log_d(mensaje):
    logging.debug(py_script+ " "+mensaje)


def pinta():
    print("estoy dentro de module")
    log_d(" - estoy dentro de module")