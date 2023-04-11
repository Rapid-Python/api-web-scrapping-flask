from config import app
from app.controller.naukri import naukri_controller
from app.service.other_function import check_debug

app.register_blueprint(naukri_controller)

debug_flag = check_debug()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=debug_flag)

