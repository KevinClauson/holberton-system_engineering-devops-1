#!/usr/bin/python3
"""
using https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns information about his/her TODO list progress
"""
import sys
import requests
import csv


def make_request(data, num):
    """
    makes employee request and returns json dict response
    """
    root = 'https://jsonplaceholder.typicode.com'
    url = root + data + num
    return requests.get(url).json()


def app():
    """
    returns info about employee todo list
    """
    num = str(sys.argv[1])
    employee = make_request('/users/', num)
    todos = make_request('/todos/?userId=', num)
    name = employee.get('name')
    all_tasks = [[t.get('completed'), t.get('title')] for t in todos]
    filename = num + '.csv'
    with open(filename, 'w') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=',', quoting=csv.QUOTE_ALL
        )
        for task in all_tasks:
            spamwriter.writerow([name, num, task[0], task[1]])


if __name__ == '__main__':
    """
    MAIN App
    """
    app()