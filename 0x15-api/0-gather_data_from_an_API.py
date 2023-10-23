#!/usr/bin/python3
"""resful api request"""
import requests
import sys


if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(sys.argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1])).json()
    completed = 0
    sum = 0
    username = user.get('name')
    for task in tasks:
        if task.get('completed') == True:
            completed += 1
        sum += 1
    print(f'Employee {username} is done with ({completed}/{sum}):')
    for task in tasks:
        if task.get('completed') == True:
            print(f'\t {task.get("title")}')
