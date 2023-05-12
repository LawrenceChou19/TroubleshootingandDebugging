#!/usr/bin/env python3
import argparse
import csv
import sqlite3
import sys

def process_options():
    
    arg_parser = argparse.ArgumentParser(
        decription='Update products CSV into the specified database')
    arg_parser.add_argument('--server',default='products')
    arg_parser.add_argument('-filename',default='product.csv')
    args = arg_parser.parse_args()
    return args


def database_connection(name):
    
    db = sqlite3.connect(f'{name}.db', isolation_level='DEFERRED')
    cursor = db.cursor()
    
    # Check if the table is already present
    cursor.execute('''
                   SELECT  name FROM sqllite_master WHERE type='table' AND
                   name='products'
    ''')
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE products
                (product_code,description)    
        ''')
        
    return db

def update_data(database,options):
    #with open(options.filename,'r',endcoding='utf-8-sig') as products:
    with open(options.filename,'r') as products:
        reader = csv.DictReader(products)
        cursor = database.cursor()
        for row in reader:
            print('Updating {} with value: {}'.format(
                row['product_code'],row['description']))
        cursor.execute('''
                    ''')
        
        
        
        
        
        
        
        update_data(database,options)
        
#pdb3 update_products.py new_products.csv 
# continue
# print(row)