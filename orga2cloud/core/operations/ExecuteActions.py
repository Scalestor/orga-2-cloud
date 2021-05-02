
"""
2021-05-02:
Question
- how to properly start the action. Subprocess or os.system?
- how to parse the arguments. ? https://stackoverflow.com/questions/18006161/how-to-pass-dictionary-as-command-line-argument-to-python-script
- or should it be stored on the db?

"""

import os
import subprocess
import json

import pymongo
from bson.objectid import ObjectId

connection_string_status = "mongodb://127.0.0.1:27017"
myclient = pymongo.MongoClient(connection_string_status)
main_db = myclient["orga2cloud"]
main_status_collection = main_db.get_collection("current_status")

def operation_execute_action(action_id,runtime_id,user_id):
    """

    :param path:
    :return:
    """
    print(f"Starting operation execute {action_id}")



    # 1 First - get the action-JSON to execute
    # 2 Get the path and create the action-object

    job_id = "608ecd74c7e172541cda16d6"
    user_id =None
    runtime_id=None


    test_cursor = main_status_collection.find( {"_id" : ObjectId(action_id)})
    for x in test_cursor:
        print(x)

