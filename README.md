# JiraTickets
Generate random Jira tickets!

*Note This script is written in python 3.5 and only tested with python3.5*

You can generate any number of tickets for any number of projects.

You can easily generate 1, 2, or 3 releases, but any more would require a code change.

to use, simply run `python3 generate.py > <your_output_file.csv>`

Project Type - determined by initialization  
Project Name - determined by initialization  
Project Key - determined by initialization  
Issue Type - randomly selected on each generate  
Summary - randomly selected on each generate  
Status  - randomly selected on each generate  
Assignee - randomly selected on each generate  
Reporter - Always the same  
Description - randomly selected on each generate  
Priority - randomly selected on each generate  
Date Created - randomly selected on each generate  
Date Modified - randomly selected, then re-selected if it before creation date  
Fix Version - not assigned  
Fix Version - not assigned  
Fix Version -  not assigned  
Affects Version - current version  
Affects Version - not assigneed  
Affects Version - not assigneed  
