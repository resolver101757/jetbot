import logging

print_to_console = True # prints to screen


def format_logging(log_level , message_to_log , log_file = "logs\logs.log"):
    """Logs to file and console. logs to console if print_to_console is True

    Args:
        log_level ([type]): set to either : DEBUG, INFO, WARNING, ERROR, CRITICAL
        log_file ([type]): sets the path of the file to log to 
        message_to_log ([type]): details to write to the log file 
    """    
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')  
    logging.basicConfig(level=log_level) # DEBUG, INFO, WARNING, ERROR, CRITICAL
    logging.basicConfig(filename=log_file, filemode='a') # a for append
    # print to screen
    if print_to_console == True:
        print("log level: " + log_level + " message : " + message_to_log)

    # write to log file 
    if log_level == "DEBUG":
        logging.debug(message_to_log)
    elif log_level == "INFO":
        logging.info(message_to_log)
    elif log_level == "WARNING":
        logging.warning(message_to_log)
    elif log_level == "ERROR":
        logging.error(message_to_log)
    elif log_level == "CRITICAL":
        logging.critical(message_to_log)
    else:
        logging.debug(message_to_log)
