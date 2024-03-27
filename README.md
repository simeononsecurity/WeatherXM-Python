# WeatherXM Python Integration

## About

This Python script facilitates interaction with the WeatherXM API, allowing users to authenticate, fetch device lists, and retrieve weather history data. It's designed to work with WeatherXM's system for users to access weather data from their registered devices.

## Features

- User authentication with the WeatherXM API.
- Fetching a list of all devices associated with the user's account.
- Retrieving detailed weather history for each device.
- Saving weather data to JSON files organized by date.
- Console output of weather data in a human-readable format.

## Getting Started

### Prerequisites

- Python 3.6 or later.
- `requests` library.
- A `.env` file with your WeatherXM credentials.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/simeononsecurity/WeatherXM-Python.git
cd WeatherXM-Python
```

2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project with your WeatherXM API credentials:

```plaintext
WEATHERXMUSERNAME=your_username_here
WEATHERXMPASSWORD=your_password_here
```

### Usage

Run the script with Python:

```bash
python main.py
```

The script will authenticate with the WeatherXM API, fetch the list of devices, retrieve weather data for each device, save the data to JSON files, and print a summary to the console.

## Contributing

Contributions to enhance the functionality, improve the documentation, or fix bugs are welcome. Please open an issue or submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.