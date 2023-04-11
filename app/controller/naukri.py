from flask import Blueprint, request
from app.service.naukri import fetch_naukri_job
from app.adapters.naukri import clean_get_input_naukri_jobs, clean_get_output_jobs

naukri_controller = Blueprint('nakuri', 'nakuri', url_prefix='/api/v1')


@naukri_controller.route('/naukri-jobs', methods=['GET'])
def get_naukri():

    clean_request = clean_get_input_naukri_jobs(request.args)

    response_data = fetch_naukri_job(
        number_of_result=clean_request['number_of_result'],
        search_keyword=clean_request['search_keyword'],
        search_keyword_hyphen=clean_request['search_keyword_hyphen'],
        location=clean_request['location'],
        page_number=clean_request['page_number']
    )

    return clean_get_output_jobs(response_data)
        
