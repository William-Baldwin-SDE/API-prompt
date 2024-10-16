import openai
import os

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get matching clubs based on user input
def get_matching_clubs(user_query, data):
    matched_clubs = []
    query_words = user_query.lower().split()  # Split the query into words
    
    for club in data:
        for tag in club["tags"]:
            if tag in query_words:  # If a tag matches a word in the query
                matched_clubs.append(club)
                break  # Stop checking after the first match to avoid duplicates
                
    return matched_clubs

# Function to generate the assistant's response
def generate_assistant_response(user_query, matched_clubs):
    if matched_clubs:
        # List all matching clubs
        club_list = "\n".join([f"- {club['name']}: {club['description']}" for club in matched_clubs])
        response_text = f"I found the following clubs that match your interests:\n{club_list}"
    else:
        # If no clubs are found
        response_text = "Sorry, I couldn't find any clubs matching your interests."

    # Use the OpenAI API to generate a more natural response
    response = openai.Client().chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that matches students with clubs."},
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": response_text}
        ]
    )

    # Return the assistant's response
    return response['choices'][0]['message']['content'].strip()
