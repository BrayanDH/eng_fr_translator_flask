# Introduction

This project is an English to French Translation Website developed using Flask, a popular web framework for Python. The main objective of this project is to provide a user-friendly platform for translating English text into French.

# Features

- Translation Interface: Users can enter English text and receive the corresponding French translation.
- User-friendly Design: The website offers an intuitive and easy-to-use interface for a seamless translation experience.

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
  docker run -p 3000:3000 eng_fr_translator_flask
  ```

Open your web browser and visit http://localhost:3000 to access the Movie Review Website.

# Dependencies

The Movie Review Website utilizes the following dependencies:

- Flask
- IBM Watson Language Translator
- python-dotenv
- Docker
  Please refer to the requirements.txt file for the complete list of dependencies and their versions.

# Contributing

Contributions to the eng_fr_translator_flask are welcome! Feel free to open issues or submit pull requests.

# License

This project is licensed under the MIT License.

# Acknowledgments

Special thanks to the creators and maintainers of the libraries and frameworks used in this project.
