import logging
import module 
import sys
import os

py_script = os.path.basename(__file__)

logging.basicConfig(filename="fichero_de_logging.log", \
                    filemode='w', \
                    level=logging.DEBUG, \
                    format=' %(asctime)s -  %(levelname)s - %(message)s')

######################################################################################
# Definición de niveles de criticidad de logging.
######################################################################################

def log_d(mensaje): logging.debug(f"{py_script} {mensaje}")
def log_i(mensaje): logging.info(f"{py_script} {mensaje}")
def log_w(mensaje): logging.warning(f"{py_script} {mensaje}")
def log_e(mensaje): logging.error(f"{py_script} {mensaje}")
def log_c(mensaje): logging.critical(f"{py_script} {mensaje}")

log_d(' - Start of program')

def factorial(n):
    log_d('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        log_d('i is ' + str(i) + ', total is ' + str(total))
    log_d('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))

module.pinta()
log_d('End of program')