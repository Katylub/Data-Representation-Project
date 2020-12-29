# About this repository:
This repository contains the solutions for the **Data Representation** Project at GMIT.

The <b> Web application project</b>, is a recopilation and adapted version of the labs done during the course and was created to gather information of a customer; taking in consideration names, surname and price. The database can be used to adapt other business according to the needs.

## Project
In summary you will see:<br>

	• A basic Flask server that has a 

	• REST API, (to perform CRUD operations)

	• One database table and

	• Accompanying web interface (HTTP: methods and status code and JSON: JavaScript Object Notation ), using AJAX calls (with JQuery), to perform these CRUD operations

## MySql Database
The database have a Primary Key called ClientID that have autoincremental option for faster speed while implemeting queries and data independence when searching on records. 

The database contain a table called "clients" that provide information of clients as names, surname and price. The main idea is to adapt to different business. 

You can see the command to create the database [here.](https://github.com/Katylub/Data-Representation-Project/blob/main/create_database.py)  

## References
To create this program was necessary to use: 
1. Training Video and material provided during Data Representation course at GMIT
2. Research 

## Note 
- Please note that the virtual environment and the data base configuration have been ignored.
- The deployment to [PythonAnywhere](http://katylub.pythonanywhere.com/) and [Azure](https://gmitdatarep.azurewebsites.net), need additional MySql connection to the server. 
