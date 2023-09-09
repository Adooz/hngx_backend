# Flask API README

This README provides information about a Flask API that retrieves query parameters from requests, validates them, and returns a JSON response with specific information. The API is designed to be a simple example and can be extended as needed for your project.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoint](#endpoint)
  - [Query Parameters](#query-parameters)
  - [Response](#response)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before using this Flask API, make sure you have the following prerequisites installed on your system:

- Python 3
- Flask
- pytz

You can install Flask and pytz using pip:

```bash```
pip install Flask pytz


## Installation

To set up and run this Flask API on your local machine, follow these steps:

1. **Clone the Repository:**

   First, clone this GitHub repository to your local machine using the following command:

   ```bash```
   git clone https://github.com/Adooz/hngx_backend.git

Navigate to the Project Directory:

Change your current directory to the project folder by running:

```bash```
cd hngx_backend


Run the Flask Application:

Start the Flask application by running the following command:

```bash```
python3 app.py


Access the API:

Once the Flask application is running, you can access the API using your web browser or a tool like curl. For example, to make a GET request to the /api endpoint, use a URL like:

```bash```
http://localhost:5000/api?slack_name=your_name&track=backend

That's it! You've successfully installed and set up the Flask API on your local machine. You can now use it to retrieve information based on the provided query parameters.

## Usage

### Endpoint

The API exposes a single endpoint:

- `GET /api`: Retrieves information based on query parameters.

### Query Parameters

The `/api` endpoint accepts the following query parameters:

- `slack_name` (string, required): The name of the Slack user.
- `track` (string, required): The track of the user. Currently, only the "backend" track is supported. You can extend this with more tracks in the code.

### Response

The API returns a JSON response with the following information:

- `slack_name`: The name of the Slack user.
- `current_day`: The current day of the week in UTC.
- `utc_time`: The current UTC time with validation of +/-2 minutes.
- `track`: The track of the user.
- `github_file_url`: An empty string.
- `github_repo_url`: The URL of the GitHub repository.
- `status_code`: The status code of the response (200 for success).

## Example

To use the API, you can make a GET request to the `/api` endpoint with the required query parameters. Here's an example using `curl`:

```bash```
curl -X GET "http://localhost:5000/api?slack_name=Kingsley%20Ndonake&track=backend"

## Contributing

We welcome contributions to improve and enhance this Flask API. Whether you want to fix a bug, add a feature, or suggest improvements, your contributions are valuable. Here's how you can contribute:

1. **Fork the Repository:**

   Click the "Fork" button on the top right of this repository to create your copy of the project on your GitHub account.

2. **Clone Your Fork:**

   Clone your forked repository to your local machine:

   git clone https://github.com/Adooz/hngngx_backend.git

Create a Branch:

Create a new branch for your contributions:


git checkout -b feature-name


Make Changes:

Make the necessary changes or additions to the codebase. Ensure that your changes follow the project's coding standards.

Test Your Changes:

Test your changes locally to ensure they work as expected and do not introduce new issues.

Commit Your Changes:

Commit your changes to your branch with a meaningful commit message:

```bash```
git commit -m "Add feature: your feature description"

Push to Your Fork:

Push your changes to your GitHub fork:

git push origin feature-name
Create a Pull Request:

Visit the original repository on GitHub and click the "New Pull Request" button. Follow the prompts to create a pull request for your changes.

Please provide a clear and detailed description of your contribution in the pull request description.

Review and Collaborate:

Collaborate with project maintainers through the pull request to address feedback or make necessary changes. Your contribution will be reviewed, and once approved, it will be merged into the main project.

Celebrate Your Contribution:

Congratulations! Your contribution has been successfully merged into the project. Thank you for improving our Flask API!

Reporting Issues
If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Describe the problem or suggestion in detail, and we will address it as soon as possible.

We appreciate your help in making this Flask API better and more reliable.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License

MIT License
