# chatBot-for-food-ordering

### Overview
This project is a chatbot designed to take orders from users and update the information in a MySQL database. The chatbot is built using Google Dialogflow for natural language understanding, FastAPI for the backend server, and MySQL for the database. The backend server is hosted using Facebook's FastAPI framework.

### Features
1. Natural language understanding using Dialogflow
2. Order management through a chatbot interface
3. Integration with MySQL database
4. Backend server with FastAPI

### Architecture
1. Dialogflow: Handles user interaction and understanding.
2. FastAPI: Serves as the backend server to process requests from Dialogflow and interact with the database.
3. MySQL: Stores order information and other related data.

### Prerequisites
1. Python 3.8+
2. MySQL Server
3. Dialogflow account
4. Facebook's FastAPI library

### Install the dependencies:
Install the dependencies to connect the backed server to the datbase i used mypysql for my project and uvicorn to get the local backend server but we will get the http connection which is not secure to make it secure use ngrok.
...ngrok hhtp localhost

### Set up MySQL:
Install MySQL server if not already installed.
Create a database named order_management.
Create a user and grant necessary permissions.

### Configure Dialogflow:
Create a new agent in Dialogflow.
Configure the intents and entities as per your requirements.
Set up a webhook in Dialogflow to point to your FastAPI server endpoint.

## Configuration

### Update database configuration:
In the config.py file, update the database connection details:
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/order_management"

### Configure FastAPI server:
In the main.py file, ensure the webhook URL matches your Dialogflow webhook settings.

## Usage

### Start the FastAPI server:
uvicorn main:app --reload

### Interact with the chatbot:
Use the Dialogflow console or integrate the Dialogflow agent with your preferred messaging platform (e.g., Facebook Messenger, Slack) to start taking orders.

### API Endpoints:
POST /webhook
Endpoint for Dialogflow webhook to handle incoming requests.

{
    "queryResult": {
        "queryText": "I want to order a pizza",
        "parameters": {
            "food_name": "pizza",
            "number": 1
        }
    }
}

### Database Schema
![CleanShot 2024-06-13 at 11 14 32](https://github.com/pinni-vamshi/chatBot-for-food-ordering/assets/87227207/f9dac3b1-e020-48e0-af4d-ceb12034122e)

![CleanShot 2024-06-13 at 11 15 47](https://github.com/pinni-vamshi/chatBot-for-food-ordering/assets/87227207/8ddf1142-905f-403b-af63-a096b5221299)

![CleanShot 2024-06-13 at 11 16 09](https://github.com/pinni-vamshi/chatBot-for-food-ordering/assets/87227207/dba664f8-0194-4a31-bcc1-f9281464977b)

### Contributing
Contributions are welcome! Please create a pull request with your changes.

### Notes
Ensure that you replace placeholders such as yourusername and other configurations with actual values specific to your setup.
This README assumes basic familiarity with setting up Dialogflow agents and working with FastAPI.
Feel free to add or modify any sections as per your specific project requirements!
