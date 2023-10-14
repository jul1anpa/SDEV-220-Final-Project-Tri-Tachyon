# Library Hold System Mockup
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
6. Create a superuser (to access the admin interface)
7. Run a development server on your machine using the runserver command
8. Get ready to create a virtual library (no real books, sadly.)


### Usage
The system uses four custom model types defined in models.py to replicate an online libary
These include:
__-->__ Item (attributes: name, stock, item_type, author, description, created_date, image
        methods: is_available
)
__-->__ Cart (attributes: session_key, items)
__-->__ CartItem (attributes: cart, item, quantity)
__-->__ Hold (attributes: item, quantity, timestamp, is_active)




Configuration details (e.g., settings, environment variables)
Dependencies and requirements
License and copyright information
Links to further documentation and resources
