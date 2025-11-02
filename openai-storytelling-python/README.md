# OpenAI Storytelling Python App

## Overview
The OpenAI Storytelling Python App is a web application that allows users to create and share stories using the OpenAI API. The application is built with Python and utilizes a web framework to handle requests and responses.

## Features
- Create and edit stories using a user-friendly interface.
- Fetch and display a list of stories.
- Utilize the OpenAI API to generate story content.

## Project Structure
```
openai-storytelling-python
├── src
│   └── openai_storytelling
│       ├── __init__.py
│       ├── main.py
│       ├── api
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── services
│       │   └── openai_service.py
│       ├── models
│       │   └── story.py
│       ├── schemas
│       │   └── story_schema.py
│       ├── config.py
│       └── utils.py
├── tests
│   └── test_app.py
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd openai-storytelling-python
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Set up your environment variables by copying `.env.example` to `.env` and filling in the required values.
2. Run the application:
   ```
   python src/openai_storytelling/main.py
   ```
3. Open your browser and go to `http://localhost:5000` (or the specified port) to access the application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.