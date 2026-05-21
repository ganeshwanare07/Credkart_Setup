# from configparser import RawConfigParser
#
# config = RawConfigParser()
# config.read("Configuration/config_SIT.ini")
#
# class ReadConfigClass:
#
#     @staticmethod
#     def get_data_for_email():
#         return config.get("login_data", "email")
#
#     @staticmethod
#     def get_data_for_password():
#         return config.get("login_data", "password")
#
#     @staticmethod
#     def get_data_for_login_url():
#         return config.get("application_url", "login_url")  # https://automation.credence.in/login
#
#     @staticmethod
#     def get_data_for_registration_url():
#         return config.get("application_url", "registration_url")  # https://automation.credence.in/register


from configparser import ConfigParser
import os

config = ConfigParser()

project_path = os.path.dirname(os.path.dirname(os.path.abspath("/Users/ganeshwanare/Desktop/Ganesh/new test data/Testing Notes Credence/Assignments/Automation_Practice/Test_Cases_And_Projects/Automation_Test_Cases_34/Configurations/config_SIT.ini")))

config_path = os.path.join(project_path, "Configurations", "config_SIT.ini")

print("Config file path:", config_path)

config.read(config_path)

print("Sections found:", config.sections())


class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email")

    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "password")

    @staticmethod
    def get_data_for_login_url():
        return config.get("application_url", "login_url")  # https://automation.credence.in/login

    @staticmethod
    def get_data_for_registration_url():
        return config.get("application_url", "registration_url")  # https://automation.credence.in/register

