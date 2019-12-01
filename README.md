# Inventory-Management-Software-in-Python
Inventory Management software in Tkinter library in python

This is GUI based inventory management software implemented in tkinter library of python. Database file is attached along with this repository that contains all the necessary tables and columns for this project. 

Functionalities implemented:
1) Stock Management: This is used to add the new items that are brought in the inventory. It can also be used to update the existing items that are available in inventory. e.g, sometimes quantities of the products needs to be modified. Delete functionality is also provided to remove the items that are discontinued or not brought due to any reason.
2) Billing Section: Billing section is also there that would create the invoice and save it in .txt format in generated_bill folder that is also provided in this repository. It is used to create an invoice using item no. Customer name and customer phone number are mandatory part to generate invoice that would have invoice id as a random number between 1 and 1000.

Pre-Requisites:
1) Make sure you have latest python version installed on your system.
2) Make sure you have tkinkter, pymysql libraries installed on your system.
3) Make sure you have mysql database installed on your system along with phpMyadmin to access database graphically.

Steps to run:
1) Create a database named 'ims' in phpmyadmin and now import ims.sql file that is provided in this repository.
2) Run stock_login.py file from your terminal or command prompt.
3) Enter login id and password (default id is admin and password is admin)

---------------------------You are good to go -----------------------------------

Important Note:-
My mysql username is root and password is NULL and hostname is localhost. So, Make sure you change your settings according to your own username, password and hostname in all the three python files which otherwise would generate an error.

Feel free to contact me at haymant_1998@outlook.com

---------------------------Hope it works-----------------------------------------
