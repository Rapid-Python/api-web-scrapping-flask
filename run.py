from config import app
from app.controller.naukri import naukri_controller

app.register_blueprint(naukri_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

