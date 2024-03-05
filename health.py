import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Doctor Function
def doctor(prompt: str) -> str:
    # Tell chatbot what to do
    bot_desc = f"""
    You are a primary care physician and when given symptoms 
    from your patient you give them 3 possible diagnosis' {prompt}: 
    """

    # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    doctor_result: str = response["choices"][0]["text"]

    return doctor_result


# Treatments Function
def treatments(prompt: str) -> str:
    # Tell chatbot what to do
    bot_desc = f"""
    You are a primary care naturalpathic physician
    and you will give your patient home remedies to do
    at home to help with {prompt}, until they are able to see a doctor for {prompt}: "
    """

    # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    treatment_result: str = response["choices"][0]["text"]

    return treatment_result


# Mealplan Bot
def mealplan(prompt: str) -> str:
    bot_desc = f"""
    You are a nutritionist who creates mealplans for {prompt},
    and gives nutritional guidance and advice based on {prompt}, given by the use."
    """
    # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    mealplan: str = response["choices"][0]["text"]

    return mealplan


# Fitness Bot
def fitness(prompt: str) -> str:
    bot_desc = f"""
    You are a fitness coach specializing in kinesiology 
    and your job is to generate a fitness plan for clients 
    based on {prompt}.
    """

    # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    fitness_plan: str = response["choices"][0]["text"]

    return fitness_plan

# Research Bot

def research(prompt: str) -> str:
    bot_desc = f"""
    You are an researching assistant who provides links to research articles from: 
    mayoclinic.org, cdc.gov, and webmd.com that are recent and relevant 
    to the {prompt} given by a patient. You always give three to five articles
    to the user."""

    # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    research_info: str = response["choices"][0]["text"]

    return research_info


# Find Doctor Bot
def network(prompt: str) -> str:
    bot_desc = f"""
    You are a healthcare worker reccomending doctors to a patient 
    based on location and diagnosis. Given {prompt} and you will 
    give me three doctors that are the closest to the patients location. 
    You will also provide the doctors name, specialty, office phone number, 
    email, office address, office hours, and rating out of five stars.
    """

      # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=300)
    
    # Output from chatbot
    doctor_info: str = response["choices"][0]["text"]

    return doctor_info

    
# Keyword Bot
def keyword(prompt: str) -> str:

    bot_desc = f"""
    You are an assistent whose job is to look for key words
    in the users {prompt} that relate to their available options
    and direct them to one of the following tools related to 
    their {prompt}. You will only reply with one word.
    1. If the user lists symptoms and wants a diagnosis reply with "doctor".
    2. If the user wants treatments for a diagnosis or a list of symptoms reply with "treatments".
    3. If the user wants fitness or excercise advice reply with "fitness".
    4. If the user wants a mealplan or recipe reply with "mealplan"
    5. If the user wants more information on a topic reply with "research"
    6. If the user is looking for a doctor in their area with reply with "network".
    7. If the user wants information relating to diets reply with "diet".
    """

     # OpenAI response and max words
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=bot_desc, max_tokens=500)
    
    # Output from chatbot
    reply: str = response["choices"][0]["text"]
    return reply


def main():

    print("Healthee Helper: What can I help you with?")
    message = input("User: ")

    tool = keyword(message)

        # Route to the appropriate tool based on the keyword
    if tool == "Doctor" or "doctor":
        result = doctor(message)
        print(result)
    elif tool == "Treatments" or "treatments":
        result = treatments(message)
        print(result)
    elif tool == "Mealplan" or "mealplan":
        result = mealplan(message)
        print(result)
    elif tool == "Research" or "research":
        result = research(message)
        print(result)
    elif tool == "network" or "Network":
        result = network(message)
        print(result)
        
if __name__ == "__main__":
    main()
