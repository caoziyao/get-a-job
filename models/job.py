import time

from . import ModelMixin
from . import db
import uuid


"""
 [{'createTime': '2016-11-04 10:36:39', 'companyShortName': '慧择网', 'explain': None, 'publisherId': 1355929, 
 'jobNature': '全职', 'promotionScoreExplain': None, 'deliver': 0, 'salary': '10k-20k', 'positionName': 'Python工程师', 
 'financeStage': '成长型(B轮)', 'companyFullName': '深圳市慧择时代科技有限公司', 'companySize': '500-2000人', 
 'positionAdvantage': '准上市公司 多样化福利 领导nice', 'adWord': 0, 'education': '大专', 'plus': None, 'approve': 1, 
 'secondType': None, 'imState': 'threeDays', 'score': 0, 'positionId': 2544334, 'gradeDescription': None, 
 'district': '南山区', 'companyLabelList': ['带薪年假', '定期体检', '绩效奖金', '午餐补助']
"""
class JobModel(db.Model, ModelMixin):  
    __tablename__ = 'job'
    id = db.Column(db.String(40), primary_key=True)
    # title = db.Column(db.String(40))
    # # company_name = db.Column(db.String(128))
    # location = db.Column(db.String(128))
    # ctime = db.Column(db.Integer)
    # # salary = db.Column(db.String(40))
    # field = db.Column(db.String(40))
    # company_size = db.Column(db.String(40))
    # stage = db.Column(db.String(40))
    # lng = db.Column(db.Float)
    # lat = db.Column(db.Float)
    # gis_loc = db.Column(db.String(128))
    # jid = db.Column(db.Integer)

    companyShortName =  db.Column(db.String(40))
    companyFullName =  db.Column(db.String(128))
    # ctime = j['ctime']
    financeStage = db.Column(db.String(60))
    workYear = db.Column(db.String(60))
    createTime = db.Column(db.String(60))
    positionLables = db.Column(db.String(60))
    salary = db.Column(db.String(40))
    businessZones = db.Column(db.String(60))
    city = db.Column(db.String(60))
    positionName = db.Column(db.String(60))
    district = db.Column(db.String(60))
    companyLabelList =  db.Column(db.String(120))
    positionAdvantage =  db.Column(db.String(120))
    jobNature = db.Column(db.String(60))
    companySize = db.Column(db.String(60))
    industryField = db.Column(db.String(60))
    formatCreateTime = db.Column(db.String(60))
    education = db.Column(db.String(60))
    
    companyLogo = db.Column(db.String(120))
    positionId = db.Column(db.String(60))
    addr = db.Column(db.String(120))
    compURL = db.Column(db.String(120))

    def __init__(self, info):
        self.id = str(uuid.uuid1())
        self.savedb(info)

    def __repr__(self):
        return '<Job %r %r>' % (self.companyShortName, self.salary)

    def savedb(self, j):
        busine = j['businessZones']
        comp = j['companyLabelList'] 
        self.companyShortName = j['companyShortName']
        # ctime = j['ctime']
        self.financeStage = j['financeStage']
        self.workYear = j['workYear']
        self.createTime = j['createTime']
        self.positionLables = j['positionLables']
        self.salary = j['salary']
        self.businessZones = ' '.join(busine if busine is not None else '')       # list 2 string
        self.city = j['city']
        self.positionName = j['positionName']
        self.district = j['district']
        self.companyLabelList = ' '.join(comp if comp is not None else '')  # list 2 string
        self.positionAdvantage = j['positionAdvantage']
        self.jobNature = j['jobNature']
        self.companySize = j['companySize']
        self.industryField = j['industryField']
        self.formatCreateTime = j['formatCreateTime']
        self.education = j['education']
        self.companyFullName = j['companyFullName']
        self.companyLogo = j['companyLogo']
        self.positionId = j['positionId']
        self.addr = j['addr']
        self.compURL = j['compURL']

"""
{'companyShortName': '华瑞智生活', 'positionAdvantage': '五险一金,下午茶,全勤奖,羁绊补贴', 'education': '大专', 'positionNam
e': 'Python', 'positionId': 2538977, 'salary': '12k-18k', 'companySize': '15-50人', 'createTime': '2016-11-03 09:53:20', 'ci
ty': '深圳', 'companyFullName': '深圳华瑞智生活科技有限公司', 'formatCreateTime': '2天前发布', 'workYear': '3-5年', 'jobNatu
re': '全职', 'positionLables': None, 'companyLogo': 'i/image/M00/62/86/Cgp3O1f-3NuAbNcqAAANA38NI_4947.png', 'district': '南 
山区', 'industryField': '移动互联网', 'businessZones': ['大冲'], 'financeStage': '初创型(未融资)', 'addr': '深圳-南山区-大冲
-大冲一路华润置地大厦E座36B', 'companyLabelList': None}
"""
