from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate track parameter (You can extend this with more tracks)
    if track not in ["backend"]:
        return jsonify({"error": "Invalid track"}), 400

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime("%A")

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.now(pytz.utc)
    utc_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define GitHub repository and file URLs
    github_repo_url = "https://github.com/Adooz/hngx_backend.git"
    github_file_url = f"{github_repo_url}/blob/main/app.ext"

    # Manually build the JSON response with the desired order of keys
    response_json = (
        '{{"slack_name": "{slack_name}", "current_day": "{current_day}", '
        '"utc_time": "{utc_time_str}", "track": "{track}", '
        '"github_file_url": "{github_file_url}", '
        '"github_repo_url": "{github_repo_url}", '
        '"status_code": {status_code}}}'
    ).format(
        slack_name=slack_name,
        current_day=current_day,
        utc_time_str=utc_time_str,
        track=track,
        github_file_url=github_file_url,
        github_repo_url=github_repo_url,
        status_code=200
    )

    # Set the Content-Type header to specify JSON response
    response = app.response_class(
        response=response_json,
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
