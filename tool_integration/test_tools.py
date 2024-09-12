    I A  bin/test_tools.py (Modified)(python)  def test_all_submodule_tools():                                                                                                                     Row 34   Col 35   3:15  Ctrl-K H for help
#!/usr/bin/python

import argparse
import configparser
import os
import sys

# set up script constants
DEFAULT_SUBMODULE = "CCMS-Workflow-Tools"

def test_all_submodule_tools():
    # get command line arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-s", "--submodule", help="Name of submodule repository to search for test configurations to run.")
    arguments = argument_parser.parse_args(sys.argv[1:])
    # if argument submodule is not specified, use the default
    submodule = arguments.submodule
    if not submodule:
        submodule = DEFAULT_SUBMODULE
    # argument submodule should be present directly under working directory
    assert(os.path.isdir(submodule), "Specified submodule [" + submodule + "] could not be found in this test environment.")
    # check all top-level directories of the argument submodule
    directories = os.listdir(submodule)
    for directory in directories:
        if os.path.isdir(directory):
            # look for a "test" subdirectory under this directory
            test_directory = os.path.join(directory, "test")
            if os.path.isdir(test_directory):
                # look for a "test.properties" file under this test subdirectory
                test_properties_file = os.path.join(test_directory, "test.properties")
                if os.path.isfile(test_properties_file):
                    configuration = configparser.RawConfigParser()
                    configuration.read(test_properties_file)
                    test_parameters = dict(configuration.items("test properties"))
                    test_command = test_parameters["test_command"]
                    print("Test command = [" + test_command + "]")
