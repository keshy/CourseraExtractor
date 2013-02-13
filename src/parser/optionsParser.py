'''
Created on Feb 7, 2013

Option Parser wrapper for command line utility

@author: Krishnan_Narayan
'''

import optparse
import sys

__description__ = 'Simple script to pull down all resources from the course Introduction to Astronomy: Reference: https://class.coursera.org/introastro-2012-001/class/index'
__author__ = 'Krishnan Narayan'
__version__ = '0.0.1'
__date__ = '2013/02/12'
__minimum_python_version__ = (2, 5, 1)
__maximum_python_version__ = (3, 3, 0)

def OptionParserWrapper():
    oParser = optparse.OptionParser(usage='usage: %prog [options] coursera_page.html \n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-d', '--dest', help='String that indicates the path to the destination folder where the resources would be saved')
    oParser.add_option('-v', '--verbose', action='store_true', default=False, help='Display download details')
    
    (options, args) = oParser.parse_args()
    if len(args) != 1:
        oParser.print_help()
        print('')
        print('Author: Krishnan Narayan')
        exit()
    else:
        return options, args
    
def TestPythonVersion(enforceMaximumVersion=False, enforceMinimumVersion=False):
    if sys.version_info[0:3] > __maximum_python_version__:
        if enforceMaximumVersion:
            print('This program does not work with this version of Python (%d.%d.%d)' % sys.version_info[0:3])
            print('Please use Python version %d.%d.%d' % __maximum_python_version__)
            sys.exit()
        else:
            print('This program has not been tested with this version of Python (%d.%d.%d)' % sys.version_info[0:3])
            print('Should you encounter problems, please use Python version %d.%d.%d' % __maximum_python_version__)
    if sys.version_info[0:3] < __minimum_python_version__:
        if enforceMinimumVersion:
            print('This program does not work with this version of Python (%d.%d.%d)' % sys.version_info[0:3])
            print('Please use Python version %d.%d.%d' % __maximum_python_version__)
            sys.exit()
        else:
            print('This program has not been tested with this version of Python (%d.%d.%d)' % sys.version_info[0:3])
            print('Should you encounter problems, please use Python version %d.%d.%d' % __maximum_python_version__)

if __name__ == '__main__':
    TestPythonVersion()
    OptionParserWrapper()
