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




        
    

        
    


