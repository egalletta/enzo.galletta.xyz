""" 
    Copyright (C) 2020  Enzo E. Galletta
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. 
    
    API developed and hosted by SandboxNU (http://www.github.com/sandboxnu)
    Source code located at (https://github.com/sandboxnu/searchneu)
"""

from gql import gql, Client, AIOHTTPTransport


def get_course(subj: str, course_id: str) -> dict:
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://searchneu.com/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        """
        query getCourse ($subj: String!, $course_id: String!) {
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
    result = client.execute(
        query, variable_values={"subj": subj, "course_id": str(course_id)}
    )
    return result