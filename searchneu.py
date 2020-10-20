from gql import gql, Client, AIOHTTPTransport

def get_course(subj: str, course_id: int) -> dict:
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://searchneu.com/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        """
        query getCourse ($subj: String!, $course_id: Int!) {
            class(subject: $subj, classId: $course_id) {
                latestOccurrence {
                    name
                    desc
                }
            }
        }
        """
    )
    # Execute the query on the transport
    result = client.execute(query, variable_values={'subj': subj, 'course_id': course_id})
    return result