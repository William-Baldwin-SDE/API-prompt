from dotenv import load_dotenv
import os
from query_handler import generate_assistant_response, get_matching_clubs
from club_data import dummy_data

# Load environment variables from the .env file
load_dotenv()

def main():
    # Get user input
    user_query = input("Ask your assistant: ")
    
    # Find matching clubs
    matched_clubs = get_matching_clubs(user_query, dummy_data)
    
    # Generate assistant's response
    response = generate_assistant_response(user_query, matched_clubs)
    
    # Print the response to the user
    print(response)

if __name__ == "__main__":
    main()
