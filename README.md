> A Desktop Application utilizing Dependency Injection, Software Interfaces, and Layered Architecture. Built for extensibility. In-development.

# Project Name
"MetaQuery DB"

## Table of Contents
* [General Info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Todo List](#todo-list)
* [Known Issues](#known-issues)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General Info
This is a simple database query desktop application. Not designed for extensive creation of records, however will accept full SQL Sybase commands. Project is in development.

## Screenshots
* Basic Window
![Example screenshot](/metaquery-db/readme/MetaQueryDB-capture1.PNG)
![Example screenshot](/metaquery-db/readme/metaquery-capture3.PNG)


## Technologies
* Python 3
* Tkinter
* PyMongo
* MySQL
* MongoDB

## Features
* CRUD
* Quick switching from one database to another

## To-do List:
* Use new ui builder with table display functionality
* Complete MongoDB commands.
* Create credentials input pane
* Create .exe
* Add MySQL Shell
* Add Mongo Atlas

## Known Issues 
* UI button titles always use SQL language. 
* MySQL results object is non-reversible and non-subscriptable. Displays results upside down, needs to be reversed somehow.
* SQL data display is not in a table format. Difficult to do with limited tKinter interface. Layered design will allow for easy implementation of improved ui in the future. 
* MongoDB "View Columns" WIP - needs map or reduce function applied - see comments in code.
* MongoDB "Cross Ref:" does not work - commented out in code
* MongoDB "Run Command" does not work - commented out - challenging with pymongo syntax interpretation


## Status
Project is: _in development_.

## Inspiration
This was originally a learning project involving simple CRUD operations for a language-specific "Hello, World.". Developing a desktop, however simple, is exciting and I decided to develop the database functions into an independent study project.

## Contact
Created by Ashley Thomas (https://www.ashthomasweb.com/) - feel free to contact me!