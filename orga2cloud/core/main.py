#!/usr/bin/env python3

import classes.ProcessClass

from operations.FindActions import operation_find_action
from operations.ExecuteActions import operation_execute_action
#from orga2cloud.processes import *

import sys
import json
import getopt
import pymongo
required_arguments = ["file"]

connection_string_status = "mongodb://127.0.0.1:27017"
myclient = pymongo.MongoClient(connection_string_status)
main_db = myclient["orga2cloud"]
main_status_collection = main_db.get_collection("current_status")

print(main_status_collection)



def main(argv):

    # Parsing arguments
    try:
        opts, remainder_args = getopt.getopt(argv, "f:", ["file="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')

    for opt,opt_arg in opts:
        if opt=="-f":
            print(f"Received filename {opt_arg}")
            filename  = opt_arg

    print(remainder_args)



    loaded_json = json.load((open(filename)))["TESTID"]
    action_name = loaded_json["actions"]["start"]["action_name"]
    print(f"Looking for  action {action_name}")
    action_path = operation_find_action(action_name)
    print(f"Action path is {action_path}")
    action_parameters = loaded_json["actions"]["start"]["action_parameters"]

    action_id = "608ecd74c7e172541cda16d6"
    test_cursor = main_status_collection.find({"properties.Id": "TESTID"})

    operation_execute_action(action_id,  "test_rt_id", "test_user_id")


if __name__ == "__main__":
    print("Welcome message")
    main(sys.argv[1:])