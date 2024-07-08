#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 1 - Create a blockchain

@author: kishan
"""

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

#Part 1 - Building a Blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        

























