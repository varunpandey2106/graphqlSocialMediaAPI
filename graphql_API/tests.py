from graphene.test import Client
from django.test import TestCase
from graphql_SM_API.schema import schema

class GraphQLUserTest(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_retrieve_by_id(self):
        expected = {
            'data': {
                'user': None
            }
        }

        response = self.client.execute('''
            query {
                user(id: 2) {
                    id
                    name
                    followers {
                        name
                    }
                }
            }
        ''')

        self.assertEqual(response, expected)


#testing user creation

    def test_create_user(self):
        expected = {
            'data': {
                'createUser': {
                    'ok': True,
                    'user': {
                        'id': '3',
                        'name': 'clark kent'
                    }
                }
            }
        }

        response = self.client.execute('''
            mutation createUser 
            {
                createUser(input: { name: "clark kent" }) {
                    ok
                    user {
                        id
                        name
                    }
                }
            }
        ''')

        self.assertEqual(response, expected)
        
    
    def test_retrieve_user_with_posts(self):
        expected = {
            "data": {
                "user": {
                    "id": "2",
                    "name": "Bruce Wayne",
                    "followers": [
                        {
                            "name": "Bruce Wayne"
                        }
                    ],
                    "postSet": [
                        {
                            "content": "I am Batman"
                        }
                    ]
                }
            }
        }

        rest = self.query(
            """
            {
              user(id: 2) {
                id
                name
                followers {
                  name
                }
                post {
                  content
                }
              }
            }
            """
        )
        self.assertEqual(rest.status_code, 200)
        self.assertEqual(expected, rest.json())

   





        
    

        
    


