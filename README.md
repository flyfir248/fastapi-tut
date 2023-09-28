# FastAPI Inventory Management API

This is a simple inventory management API built using FastAPI. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on items in the inventory.

## Features

- Get an item by its ID.
- Get an item by its name.
- Create a new item.
- Update an existing item.
- Delete an item by its ID.

## Getting Started

1. Clone this repository to your local machine.

2. Install the required packages using pip:

   ```bash
   pip install fastapi
   pip install uvicorn
   ```

3. Run the API using uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   You should see output indicating that the server is running. By default, it runs on `http://localhost:8000`.

## API Endpoints

### Get Item by ID

- **Endpoint:** `/get-item/{item_id}`
- **Method:** GET
- **Description:** Get an item from the inventory by its ID.
- **Parameters:**
  - `item_id` (int, path, required) - The ID of the item in the inventory.
- **Response:** Returns the item details if found, or an error message if the item is not found.

### Get Item by Name

- **Endpoint:** `/get-by-name`
- **Method:** GET
- **Description:** Get an item from the inventory by its name.
- **Query Parameters:**
  - `name` (str, query, optional) - The name of the item.
- **Response:** Returns the item details if found, or an error message if the item is not found.

### Create Item

- **Endpoint:** `/create-item/{item_id}`
- **Method:** POST
- **Description:** Create a new item in the inventory.
- **Parameters:**
  - `item_id` (int, path, required) - The ID of the new item.
- **Request Body:** JSON object representing the new item. Example:
  ```json
  {
    "name": "milk",
    "price": 3.99,
    "brand": "premium"
  }
  ```
- **Response:** Returns the details of the created item if successful, or an error message if the item with the same ID already exists.

### Update Item

- **Endpoint:** `/update-item/{item_id}`
- **Method:** PUT
- **Description:** Update an existing item in the inventory.
- **Parameters:**
  - `item_id` (int, path, required) - The ID of the item to update.
- **Request Body:** JSON object representing the item updates. You can update the `name`, `price`, and `brand`. Example:
  ```json
  {
    "name": "updated-milk",
    "price": 4.99
  }
  ```
- **Response:** Returns the details of the updated item if successful, or an error message if the item with the specified ID does not exist.

### Delete Item

- **Endpoint:** `/delete-item`
- **Method:** DELETE
- **Description:** Delete an item from the inventory.
- **Query Parameters:**
  - `item_id` (int, query, required) - The ID of the item to delete.
- **Response:** Returns a success message if the item is successfully deleted, or an error message if the item with the specified ID does not exist.

## Error Handling

The API returns appropriate HTTP status codes and error messages for different scenarios. For example, it returns a `404 Not Found` status code and an error message when trying to access or modify an item that does not exist.

## Future Improvements

This is a basic example of an inventory management API. You can extend and enhance it in several ways:

- Add authentication and authorization mechanisms.
- Store data in a database instead of an in-memory dictionary.
- Implement input validation and data sanitization.
- Add more advanced search and filtering options.
- Implement pagination for listing items.
- Create a front-end interface to interact with the API.

Feel free to explore and customize this API according to your needs.
