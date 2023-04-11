# Naukri Jobs API
This code provides a Flask API for fetching job listings from Naukri job portal.

## Setup and Installation
Before running the code, make sure to install the following dependencies:

* Flask
* requests

You can install them using pip:

    pip install flask requests

## Usage

To use this API, start the Flask server using the command:

        python run.py

Then, you can send a GET request to the API endpoint `/api/v1/naukri-jobs` with the following parameters:

* number_of_result: Number of job listings to fetch (default: 20)
* search_keyword: Search keyword to filter job by job keyword.
* search_keyword_hyphen: Search keyword with hyphens instead of spaces
* location: Location of job listings
* page_number: Page number of job listings to fetch (default: 1)

The API will return a JSON response with the job listings, including their title, company, location, and job description.

## Code Structure

This code uses a Flask Blueprint to define the API endpoint `/api/v1/naukri-jobs`. The endpoint calls the function `fetch_naukri_job` from the naukri service module to fetch the job listings from Naukri job portal.

The `clean_get_input_naukri_jobs` and `clean_get_output_jobs` functions from the naukri adapter module are used to clean and format the request parameters and response data, respectively.

