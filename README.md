# AfricAI Quiz App - Backend

The AfricAI Quiz App is an educational tool designed to provide middle school kids with knowledge about African political, economic, and cultural history. This backend component of the app is built using Flask to serve the API endpoints for retrieving quiz questions and managing quiz sessions.

## Features

- **API Endpoints:** The backend provides API endpoints for retrieving quiz questions and managing quiz sessions.

- **Quiz Questions:** A comprehensive set of quiz questions is available to engage users with topics related to African history.

- **Session Management:** The backend keeps track of user quiz sessions, ensuring a smooth and engaging experience.


API Endpoints
-'/': Welcome endpoint to verify that the API is up and running.
-'/get_question': Endpoint to retrieve quiz questions for users.
'/submit_answer': Endpoint to submit user answers and get feedback.
'/start_session': Endpoint to initiate a new quiz session for a user.

Data Structure
The quiz questions are stored in the database using a structured model. Each question consists of a question text, answer choices, and a correct answer.

Technologies Used
-Flask: A lightweight Python web framework used for building the API.
-SQLite: A simple and lightweight database for storing quiz questions and user sessions.

Usage
1.Access the API endpoints using your preferred method (e.g., web browser, Postman, curl).
2.Retrieve quiz questions using the /get_question endpoint.
3.Submit user answers using the /submit_answer endpoint to get feedbaStart a new quiz session using the  endpoint.

License
This project is licensed under the MIT License - see the LICENSE file for details.
