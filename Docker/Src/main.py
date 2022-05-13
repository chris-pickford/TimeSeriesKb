"""


Naming Conventions:

Package:            thispackage (short name)
Module:             this_module (short name)
Class:              ThisIsAClass
Function:           this_is_a_function
Public Method:      this_is_a_public_method
Non-Public Method:  _this_is_a_non_public_method
Variables:          thisIsAVariable
Constant:           THIS_IS_A_CONSTANT

"""

__status__  = "development"
__version__ = 'mdl 1.0.1'
__author__  = 'Chris Pickford <drchrispickford@gmail.com>'

'''
Ensure any virtual environments have been activated before running scripts
'''
import os
import sys
import config as cfg

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cwd = os.getcwd()
print('Working directory set as:', cwd)

PROJECT_NAME = 'TimeSeriesKb'
config = cfg.privateConfig(cfg.OS, PROJECT_NAME)
newUser = cfg.credentials()
logFileName = PROJECT_NAME +'.log'
_ = config.set_logging(logFileName)



rootPath = config.ROOT
sys.path.append(os.path.join(rootPath))
sys.path.append(os.path.join(config.PACKAGE_ROOT, 'DataCrane'))

config.abort_pass_programme(logString='-------Program Started-------')

from DataCrane.dbutility import gnrl_database_interaction as gdbi
from DataCrane.dbutility import credentials
config.abort_pass_programme(logString=' Imported DataCrane ')

##################################################################################################################



def main():
    print('Starting program')

    dataIn = {'credentials': newUser,
              'logFileName': 'BigQuery.log'}

    connection = gdbi.GBQConnection(config, credentials=newUser, logFileName=logFileName,
                                    projectId='crafty-ring-247514')

    sqlConnection = gdbi.ExecuteSQL(
        connection=connection,
        query=os.path.join(config.PROJECT_ROOT, 'all_data.sql'),
        outputPath=None
    )

    print('Got to pre execution stage')

    message, data = sqlConnection.execute_script(saveToTable='crafty-ring-247514.Kickboxing_attendance.test')
    print(message['traceback'])

    print('Program complete')






if __name__ == '__main__':
    main()






