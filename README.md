# todo_list

This project is a web application designed for task management and tracking their completion. 
Each task is assigned unique tags to denote its characteristics. Additionally, tasks include information such as creation date, 
deadline, and current completion status, enabling efficient monitoring and control of the workflow. 
Users are provided with the ability to toggle the task status, facilitating convenient tracking of their progress.

## Installation

Python3 must be already installed

```shell
git clone https://github.com/callogan/todo_list
cd todo_list
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Features

* Ability to create task with attributes, necessary to control them
* Switching task status when it reached completion phase
* Designating tasks by tags
