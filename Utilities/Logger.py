# import logging
#
# class log_generator_class:
#
#     @staticmethod
#     def log_gen_method():
#         log_file = logging.FileHandler("./Logs/CredKart.log") # log file
#
#         logger = logging.getLogger()
#         # 2024-08-08 09:12:24,712 : INFO : test_Signup_002  : Opening browser
#         log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s') # log format
#         log_file.setFormatter(log_format) # log file --> log format
#         logger = logging.getLogger() # getLogger object
#         logger.addHandler(log_file) #  add new log everytime in same log file
#         logger.setLevel(logging.INFO) # Level set
#         return logger


"""
log level : 

debug
info
warning
error
critical

"""


import logging
import os


class LogGeneratorClass:

    @staticmethod
    def log_gen_method():

        logger = logging.getLogger("CredKartLogger")
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not logger.handlers:

            # Project path
            project_path = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            # Logs folder path
            log_folder = os.path.join(project_path, "Logs")

            # Create Logs folder automatically
            os.makedirs(log_folder, exist_ok=True)

            # Log file path
            log_file_path = os.path.join(log_folder, "CredKart.log")

            # File Handler
            file_handler = logging.FileHandler(log_file_path)

            # Console Handler
            console_handler = logging.StreamHandler()

            # Log format
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s'
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger