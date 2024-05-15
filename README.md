# Inventory Management System API

This project is an Inventory Management System designed using Flask. It allows users to create, delete, update and retrieve products. 


Key Features

1. Product creation, deletion, update and retrieval.
2. Adding product to cart and purchasing product
3. Keeping track of product quantity in regards to purchase or add to cart functions, i.e the product quantity should reduce when a purchase is made, or when it is added to the "user's" cart; users should be informed when a product is "out of stock"
4. Products should have (name, category, labels(e.g size, colour etc), quantity, price) A product can have one or more labels.

## Testing

Two sample  accounts have been created for testing purposes. The details are as follows:

- Sam Ethan
  - email: samethan@example.com
  - password: 1234ABDCEF
- Sim Emma
  - email: samiemma@example.com
  - password: 1234ABDCEF

- Adminer is used for database management. The details are as follows:
  - System: PostgreSQL
  - Server: db
  - Username: postgres (the value of POSTGRES_USER in the .env file)
  - Password: dbPassword (the value of POSTGRES_PASSWORD in the .env file)
  - Database: inventory (the value of POSTGRES_DB in the .env file)