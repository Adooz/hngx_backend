from flask import Flask, request, jsonify
import datetime
import pytz
from collections import OrderedDict

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    """
    Retrieves query parameters from the request, validates the 'track' parameter, gets the current day and time in UTC,
    and prepares a response JSON with the retrieved information and other predefined values.

    :return: JSON response with the following information:
             - slack_name: The name of the Slack user.
             - current_day: The current day of the week in UTC.
             - utc_time: The current UTC time with validation of +/-2 minutes.
             - track: The track of the user.
             - github_file_url: An empty string.
             - github_repo_url: The URL of the GitHub repository.
             - status_code: The status code of the response (200 for success).
    """

    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate track parameter (You can extend this with more tracks)
    if track not in ["backend"]:
        return jsonify({"error": "Invalid track"}), 400

    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.now(pytz.utc)
    utc_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define GitHub repository and file URLs
    github_repo_url = "https://github.com/Adooz/hngx_backend.git"
    github_file_url = f"{github_repo_url}/blob/main/app.ext"
    # Prepare the response JSON
    response_data = OrderedDict([
        ("slack_name", slack_name),
        ("current_day", current_day),
        ("utc_time", utc_time_str),
        ("track", track),
        ("github_file_url", github_file_url),
        ("github_repo_url", github_repo_url),
        ("status_code", 200)
    ])


    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
