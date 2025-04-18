# -*- coding: utf-8 -*-
"""CLI To-Do List.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z19XjaoZtjQGrz-rh4QX7zMfY916R1el
"""

import argparse
import json
import os

todo_file = "todo_list.json"

def load_tasks():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": description, "done": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "[✔]" if task["done"] else "[ ]"
        print(f"{task['id']}. {status} {task['task']}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    parser_list = subparsers.add_parser("list", help="List all tasks")

    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("task_id", type=int, help="Task ID")
    parser_update.add_argument("new_description", type=str, help="New task description")

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", type=int, help="Task ID")

    parser_done = subparsers.add_parser("done", help="Mark task as done")
    parser_done.add_argument("task_id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "update":
        update_task(args.task_id, args.new_description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "done":
        mark_done(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()