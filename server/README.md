
#  Late Show API - Flask Code Challenge 

Welcome to the **Late Show API** project! This Flask application is built for managing and querying data about TV show episodes, their guests, and their appearances.


##  Features

- View all episodes
- View episode details with guest appearances
- View all guests
- Create new appearances (with validation)

## Models & Relationships

- **Episode** has many **Guests** through **Appearances**
- **Guest** has many **Episodes** through **Appearances**
- **Appearance** belongs to one **Episode** and one **Guest**

## Validations

- Appearance must have a `rating` between `1` and `5` (inclusive)
- Cascading deletes set for appearances when a related episode or guest is removed



##  Features

- View all episodes
- View episode details with guest appearances
- View all guests
- Create new appearances (with validation)

## Models & Relationships

- **Episode** has many **Guests** through **Appearances**
- **Guest** has many **Episodes** through **Appearances**
- **Appearance** belongs to one **Episode** and one **Guest**

##  Validations

- Appearance must have a `rating` between `1` and `5` (inclusive)
- Cascading deletes set for appearances when a related episode or guest is removed

## Prerequisites
Before running this project, ensure you have the following installed on your machine:

- Python 3.9+ – for running the Flask backend.

- pip – Python package manager (comes with Python).

- virtualenv –  for managing a clean Python environment:

- Flask-Migrate – for handling database migrations.

- SQLAlchemy – ORM for managing database models.

- Faker – for generating dummy data in the seed file.

- Postman – for testing endpoints.

# Author
This project was done by Eric Kipkoech,for any inquiries please reach out.