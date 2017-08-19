import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Program begins')

def manual_power(n, powerOf):
    """Takes n to the power of powerOf manually"""
    logging.debug('manual_power called with(' + str(n) + ', ' + str(powerOf) + ')')
    try:
        assert isinstance(n, int), "n must be an integer"
        assert isinstance(powerOf, int), "powerOf must be an integer"
        assert powerOf > 1, "powerOf must be greater than one"
    except AssertionError as asserr:
        logging.debug('Assertion raised error:' + asserr.args[0] + ', failing silently')
        return -1
    endn = n
    for i in range(1, powerOf):
        endn *= n
        logging.debug('Iteration #' + str(i) + ': endn = ' + str(endn))
    logging.debug('end state of endn in function: ' + str(endn))
    return endn

manual_power(2, 2)
manual_power(8, 5)
manual_power(4, "goat")
manual_power(999, 0)
manual_power("love", "dogs")