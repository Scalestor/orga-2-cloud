#!/usr/bin/env python3
import json
import sys
import argparse

print("Test-Action")
arguments = sys.argv[1:]


print(sys.argv)

print(f"I am a test-action. I have received the following parameters {arguments}")




class BaseAction():
    def __init__(self, action_id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) ==0:
            raise ValueError("Name cannot be empty!")
        self._name = value

BaseAction("0","json_pars[key]")