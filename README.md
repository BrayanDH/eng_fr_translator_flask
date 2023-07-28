# Introduction

This project is an English to French Translation Website developed using Flask, a popular web framework for Python. The main objective of this project is to provide a user-friendly platform for translating English text into French.

# Features

- Translation Interface: Users can enter English text and receive the corresponding French translation.
- User-friendly Design: The website offers an intuitive and easy-to-use interface for a seamless translation experience.
- Dockerized: The website is packaged as a Docker image and can be run locally using Docker.

# Getting Started

# API_Key

you need to create an account on IBM Cloud and get your API_Key and URL for the Language Translator service. You can create a free account on IBM Cloud [here](https://cloud.ibm.com/registration).

need to create a .env file in the `machinetranslation` directory of the project and add the following lines to it:

```
apikey=
url=

```

## To run eng_fr_translator locally, follow these steps:

Install Docker on your machine: [Docker Installation Guide ](https://docs.docker.com/engine/install/)

- Clone this repository:

  ```
  git clone https://github.com/BrayanDH/eng_fr_translator_flask.git
  ```

- Navigate to the project directory:

  ```
  cd eng_fr_translator_flask
  ```

- Build the Docker container:

  ```
  docker build -t eng_fr_translator_flask .
  ```

- Run the container:

  ```
  docker run -p 8080:8080 eng_fr_translator_flask
  ```

To run the Todo App locally without docker, follow these steps:

Install Python on your machine: [Python Installation](https://www.python.org/downloads/)

1. Clone the repository: Open a terminal and clone the `eng_fr_translator_flask` project repository from GitHub:

   ```
   git clone https://github.com/BrayanDH/eng_fr_translator_flask.git
   ```

2. Navigate to the project directory:

   ```
   cd eng_fr_translator_flask
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install all the necessary dependencies for the project.

4. Run the application:

   ```
   python server.py
   ```

   or

   ```
   server.py
   ```

   This will start the Flask server, and the application will be available at http://localhost:8080.

Once you have completed these steps, you can access the English to French Translation Website by opening your web browser and visiting http://localhost:8080. From there, you can use the translation interface to enter English text and receive the corresponding French translation.

Open your web browser and visit http://localhost:8080 to access the Movie Review Website.

# Dependencies

The Movie Review Website utilizes the following dependencies:

- Flask
- ibm-watson
- python-dotenv
- Docker
  Please refer to the requirements.txt file for the complete list of dependencies and their versions.

# Contributing

Contributions to the eng_fr_translator_flask are welcome! Feel free to open issues or submit pull requests.

# License

This project is licensed under the MIT License.

# Acknowledgments

Special thanks to the creators and maintainers of the libraries and frameworks used in this project.
