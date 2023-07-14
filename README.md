# graphqlSocialMediaAPI

Welcome to graphqlSocialMediaAPI, a GraphQL API (being)built using Graphene Django.

## Introduction

graphqlSocialMediaAPI provides a powerful and flexible GraphQL interface for managing social media-related functionality. It leverages the Graphene Django library to seamlessly integrate GraphQL capabilities with a Django backend.

## Features

STILL BEING WORKED ON

## Prerequisites

To run graphqlSocialMediaAPI locally, you'll need the following prerequisites:

Django==4.2.3 
graphene==3.2.2 
graphene-django==3.1.2 
graphql-core==3.2.3

## Getting Started

Follow these steps to get graphqlSocialMediaAPI up and running:

1. Clone the repository: https://github.com/varunpandey2106/graphqlSocialMediaAPI.git
2. Install the required dependencies:

pip install -r requirements.txt

3. Set up the Django database:

python manage.py migrate

4. Start the development server:

python manage.py runserver


5. Access the API at `http://localhost:8000/graphql` in your browser or a GraphQL client.

6.
## API Usage

graphqlSocialMediaAPI exposes a GraphQL endpoint for interacting with the API. You can access it via `http://localhost:8000/graphql` (or the URL where you deployed the API).

Detailed documentation on the API schema, queries, mutations, and available fields can be found in the GraphQL playground accessible at the endpoint mentioned above.

Here's a simple example query to get started:

```graphql
query {
  users {
    id
    name
    followers {
      name
      
    }
  }
}

Contributing
Contributions are welcome! If you'd like to contribute to graphqlSocialMediaAPI, please follow these steps:

Fork the repository.
Create a new branch for your feature/fix: git checkout -b feature-name.
Make your changes and commit them: git commit -m "Add feature/fix".
Push to the branch: git push origin feature-name.
Submit a pull request.
License
This project is licensed under the MIT License.

Contact
If you have any questions or feedback, feel free to reach out to me at varun.pandey2106@gmail.com or create an issue in the GitHub repository.

Happy coding!


