# FlaskMedAI-ML

![GitHub top language](https://img.shields.io/github/languages/top/naluthi/FlaskMedAI-ML) 
![Flask](https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask&logoColor=white) 
![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat&logo=openai&logoColor=white) 


## Table of Contents

- [Description](#description)
- [Files](#files)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Description

The repository consists of several key Python files that work together to run the Flask application and handle various operations relating to health advice. It integrates with the OpenAI API to generate responses for various health-related tasks, such as providing diagnoses, suggesting treatments, creating meal plans, recommending fitness routines, and more.

## Files

- `__init__.py`: Initializes the Flask application and sets up the necessary configuration.
- `main.py`: Acts as the entry point for the application.
- `routes.py`: Defines web routes/endpoints for the Flask application.
- `health.py`: Includes 8 functions, related to health or medical functionalities.

## Features

- **Doctor Chatbot**: Provides potential diagnoses based on the user's symptoms.
- **Treatment Chatbot**: Suggests home remedies and treatments for various conditions.
- **Meal Plan Chatbot**: Creates customized meal plans based on the user's dietary requirements or health goals.
- **Fitness Chatbot**: Generates fitness routines tailored to the user's needs and preferences.
- **Research Chatbot**: Provides links to recent and relevant research articles from reputable sources.
- **Doctor Network Chatbot**: Recommends nearby doctors based on the user's location and diagnosis.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/FlaskMedAI-ML.git
```

2. Navigate to the project directory:

```bash
cd FlaskMedAI-ML
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```

## Usage

1. Start the Flask application:

```bash
python main.py
```

2. Access the application in your web browser at `http://localhost:5000`.

3. Interact with the chatbots by providing prompts or queries related to your health concerns.

## License

This project is licensed under the [MIT License](LICENSE).

# Contact

[![Outlook](https://img.shields.io/badge/Microsoft\\_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](nick@luthi.us)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nickluthi)
