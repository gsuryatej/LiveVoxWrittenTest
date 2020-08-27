#!/usr/bin/env python

import os
import sys
import argparse
import cx_Oracle
import config

try:
    import json
except ImportError:
    import simplejson as json

class Inventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()
        
        # Called with `--list`
        if self.args.list:
            self.populate_from_db()

        # Called with `--host [hostname]`
        elif self.args.host:
            # Not implemented, since we return `_meta` key for `--list` call
            self.inventory = self.empty_inventory()

        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory))

    def populate_from_db(self):
        try:
            with cx_Oracle.connect(config.username,config.password,config.dsn,encoding=config.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT host_name, var_name, var_value FROM host_vars;')
                    vars_ = cursor.fetchall()
                    for v in vars_:
                        self.add_host_var(v['host_name'], v['var_name'], v['var_value'])
                    return self.inventory
        except cx_Oracle.Error as error:
            print(error)

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

    def add_host_var(self, host_name, var_name, var_value):
        meta_dict = self.inventory.get( '_meta', {} )
        hosts_dict = meta_dict.get( 'hostvars', {} )
        host_vars = hosts_dict.get( host_name, {} )
        host_vars[var_name] = var_value
        hosts_dict[host_name] = host_vars
        meta_dict = hosts_dict
        self.inventory['_meta'] = meta_dict

# Get the Inventory
Inventory()