# Library Hold System Mockup Documentation
_This repository stores all files related to the SDEV 220 Group 3 project._


### Description:
This repository provides the framework for a library hold system application utilizing Django in Python.  
This application allows a user to replicate an online library using the Object-Relational Mapping component of Django.


### Installation instructions (e.g., requirements, setup)
*__Requirements: Python version>=3.6, Django experience__*
1. After cloning the repository, open the root directory of the project in your coding environment
2. Open terminal and navigate to the project's root directory
3. Create and activate a virtual environment within the root directory
4. pip install -r requirements.txt
5. Use the migrate command to create your database
6. Create a superuser (to access the admin interface) using the createsuperuser command
7. Run a development server on your machine using the runserver command
8. Get ready to create a virtual library (no real books, sadly.)


### Usage
The system uses four custom model types defined in models.py to replicate an online libary  
These include: 


- __Item__ (attributes: [name, stock, item_type, author, description, created_date, image]  
        methods: is_available)  
The Item model represents a book, DVD, etc. that a user could add to their cart and place a hold on.  
_Item objects can be created and managed via the admin interface_


- __Cart__ (attributes: session_key, items)  
The Cart model represents a cart that stores items a user has placed inside of it. When a cart gets added to for the first time, a new Cart object is created. The Cart object stores a user's session key which will associate the Cart object with that specific user.  


- __CartItem__ (attributes: cart, item, quantity)  
The CartItem model represents an item that has been added to a cart. When an Item object is added to a cart, a new CartItem object is created. The CartItem object associates itself with the Item object via a foreign key upon construction.  


- __Hold__ (attributes: item, quantity, timestamp, is_active)  
The Hold model represents a cart item that has been checked out. Upon checkout with a Cart object, new Hold objects are created that are constructed based on the CartItem's associated with the Cart.   _Hold objects can be accessed using the admin interface_  

  
  
  
To begin, you should populate the database with Item objects so that there is a catalog to choose from.  
While your server is running, navigate to the admin/ url and login to the admin interface using your credentials.  
From here you create new Item objects that will appear in the user interface.  
You'll notice there is also an option to view existing Holds from the admin interface.  
Once you populate your database with Items you can then view them by visiting the port url of your server.  
You should now see your Items listed in the catalog!  
When a user adds an Item object to their cart for the first time, a new Cart object will be created.  
The user's Cart will then store a copy of the Item object via a new CartItem object.  
When a user decides to checkout, new Hold objects will be created based on the existing CartItem's within the Cart.  
The user's Cart will then be deleted and their Holds will be stored in the database.  
Note that the stock of Items will be affected when a user places a Hold on a CartItem.
