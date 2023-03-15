from flask import jsonify

def clean_get_input_naukri_jobs(request_data):
    return  {
        'number_of_result': request_data.get('number_of_result', 100),
        'search_keyword': request_data.get('search_keyword', ''),
        'search_keyword_hyphen': request_data.get('search_keyword').replace(' ', '-'),
        'page_number': request_data.get('page_number', 1)
    }


def clean_get_output_jobs(data):

    return jsonify(
        {
            'status': 200,
            'message': 'Successfully',
            'items': data
        }
    )

