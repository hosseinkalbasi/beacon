# Beacon
Testing Beacon Navigator for sending user behavior analytics data to a server


# Technologies Used
1. [FastAPI](https://fastapi.tiangolo.com/)
2. [Beacon Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon)


# Pre-requisites
1. Python 3
2. Libraries specified in requirements.txt

# Structure
1. `main.py` - The main file that runs the FastAPI server
2. `run.sh` - A bash script to run the server
3. `templates` - Contains the HTML templates
4. `static` - Contains the static files (including the JS file for Beacon Navigator
5. `models` - Contains the data models for the API endpoints
6. `requirements.txt` - Contains the required libraries

# How to Use
1. Clone the repository
2. Install the required libraries using `pip install -r requirements.txt`
3. Run the app using `uvicorn main:app --reload` (or via `bash run.sh`)
4. Open the browser and go to `http://localhost:8000/docs` to see the API documentation
5. Go to `http://localhost:8000/page/3` to see the sample page
6. Open your browser console and to see logged information
7. Click on the buttons to see the event being logged in the console
8. Move between browser tabs or close the tab to see the event being sent to the server
