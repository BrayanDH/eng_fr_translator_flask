# Data Visualization Final Project (Dash)

This project is a Data Visualization Final Project developed using Dash, a web application framework for Python. The primary objective of this project is to create an interactive dashboard that visualizes US Domestic Airline Flights Performance data.

## Features

- Yearly Airline Performance Report: Users can view monthly flight cancellation data, average flight time by reporting airline, percentage of diverted airport landings per reporting airline, number of flights from each state, and number of flights to destination state by reporting airline.
- Yearly Average Flight Delay Statistics: Users can view average carrier delay time, average weather delay time, average NAS delay time, average security delay time, and average late aircraft delay time by airline.

## Getting Started

```
git clone https://github.com/BrayanDH/Dash_Data_Visualization_Panel.git
```

- Navigate to the project directory:

  ```
  cd Dash_Data_Visualization_Panel
  ```

- Build the Docker container:

  ```
  docker build -t Dash_Data_Visualization_Panel .
  ```

- Run the container:

  ```
  docker run -p 8080:8080 Dash_Data_Visualization_Panel
  ```

To run the Todo App locally without docker, follow these steps:
Install Docker on your machine: [Python Installation](https://www.python.org/downloads/)

To run the Data Visualization Final Project locally without docker, follow these steps:

1. Clone this repository:

   ```
   git clone https://github.com/BrayanDH/Data_Visualization_Final_Project.git
   ```

2. Navigate to the project directory:

   ```
   cd Data_Visualization_Final_Project
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Start the application:

   ```
   python app.py
   ```

   or

   ```
   app.py
   ```

5. Open your web browser and visit http://localhost:8050 to access the Data Visualization Final Project.

## Dependencies

The Data Visualization Final Project utilizes the following dependencies:

- Pandas
- Dash
- Plotly

Please refer to the `requirements.txt` file for the complete list of dependencies and their versions.

## Contributing

Contributions to the Data Visualization Final Project are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the creators and maintainers of the libraries and frameworks used in this project.

---
