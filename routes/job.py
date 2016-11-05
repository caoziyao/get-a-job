
from routes import *


main = Blueprint('job', __name__)


@main.route('/')
def index():
    return 'hello job'



