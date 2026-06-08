#!/usr/bin/env python3
# Author ID: rohit10@myseneca.ca

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    list_of_lines = read_data.split('\n')
    return list_of_lines[:-1]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
