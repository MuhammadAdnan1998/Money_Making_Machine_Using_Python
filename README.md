# Money Making Machine

## Overview
The **Money Making Machine** is a Streamlit-powered web application designed for entertainment and inspiration. This app provides a fun way to "generate" virtual money, discover potential side hustles, and get motivational quotes about financial success.

## Features
- **Instant Cash Generator:** Simulate money generation with a random amount.
- **Side Hustle Ideas:** Fetch a side hustle suggestion from an API.
- **Money-Making Motivation:** Retrieve an inspirational financial quote.

## Technologies Used
- Python
- Streamlit
- Requests (for API calls)
- Random (for generating virtual money)
- Time (for simulating delays)

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/money-making-machine.git
   ```
2. Navigate to the project directory:
   ```sh
   cd money-making-machine
   ```
3. Install required dependencies:
   ```sh
   pip install streamlit requests
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## API Configuration
The app fetches side hustle ideas and money quotes from an external API. Ensure your backend server is running at `http://127.0.0.1:8000/` or modify the API URLs accordingly in the code.

## Usage
- Click **Generate Money** to see a random amount.
- Click **Generate Hustle** to get a side hustle idea.
- Click **Get Inspired** for a motivational money quote.

## Contribution
Feel free to fork this repository and submit pull requests with improvements. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
**Note:** This application is for entertainment purposes only and does not generate real money.

