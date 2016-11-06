
from routes import *
from replay.spider import lagou_spider
from models.job import JobModel
from flask import jsonify

main = Blueprint('job', __name__)

def sa_obj_to_dict(obj):
    return {k: v for (k, v) in obj.__dict__.items() if not k.startswith('_')}


@main.route('/')
def index():
    # jobs = [ sa_obj_to_dict(j) for j in JobModel.query.all()]
    # print(jobs)
    # jobs_json()
    return render_template('index.html')


@main.route('/api/jobs')
def jobs_json():
    jobs = [sa_obj_to_dict(j) for j in JobModel.query.all()]
    print(jobs)
    return jsonify(error=0, total=len(jobs), items=jobs)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/spider')
def spider():
    # lagou_spider()
    return 'hello'



