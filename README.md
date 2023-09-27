# Stock-Data-API-with-Flask
This is a Python Flask web application that provides a RESTful API for retrieving real-time stock data. The API leverages the Alpha Vantage API to fetch stock information based on the provided stock symbol. Users can make GET requests to the API endpoint to retrieve stock details in JSON format.
Features:

Fetches stock data, including open, high, low, price, volume, and more.
Handles errors gracefully, providing appropriate error messages for invalid symbols or API failures.
Easily customizable with your own Alpha Vantage API key.

Usage:

Clone this repository to your local environment.
Replace the api_key variable in the code with your valid Alpha Vantage API key.
Run the Flask application, and the API will be accessible at http://localhost:5000/api/stock/<symbol>, where <symbol> is the stock symbol you want to retrieve data for.
