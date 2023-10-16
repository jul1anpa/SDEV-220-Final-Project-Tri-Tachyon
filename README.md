# Library Hold System Mockup Documentation
_This repository stores all files related to the SDEV 220 Group 3 project._


### Description
This repository provides the framework for a library hold system application utilizing Django in Python.  
This application allows a user to replicate an online library using the Object-Relational Mapping component of Django.


### Installation instructions (e.g., requirements, setup)
*__Requirements: Python version>=3.6, Django experience__*
1. After cloning the repository, open the root directory of the project in your coding environment
2. Open terminal and navigate to the project's root directory
3. Create and activate a virtual environment within the root directory

```
python -m venv <insert_name_of_virtual_environment_here>
```

4. Activate the virtual environment
5. Install the required packages using pip

```
pip install -r requirements.txt
```

6. Use the migrate command to create your database _(This is not required if you would like to use the prepopulated database. If you would like to create your own database, please delete the current db.sqlite3 file located in the directory)_

```
python manage.py migrate
```

7. Create a superuser (to access the admin interface) using the createsuperuser command

```
python manage.py createsuperuser
```

8. Run a development server on your machine using the runserver command

```
python manage.py runserver
```

9. Get ready to create a virtual library (no real books, sadly.)


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
The Hold model represents a cart item that has been checked out. Upon checkout with a Cart object, new Hold objects are created that are constructed based on the CartItem's associated with the Cart.
_Hold objects can be accessed using the admin interface_

__The framework comes with a prepopulated database, but if you would like to create your own Items please follow the steps below:__  
  
1. While your server is running, navigate to the admin/ url and login to the admin interface using your credentials.
2. From here you can create new Item objects that will appear in the user interface.
_(You'll notice there is also an option to view existing Holds from the admin interface.)_
3. Once you create a new Item you can then view it by visiting the port url of your server.
4. You should now see your newly created Items listed in the catalog!
