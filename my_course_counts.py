from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())

department_list = {
    'American Study':'AMST',
    'Arabic':'ARAB',
    'Art History':'ARTH',
    'Art Studio':'ARTS',
    'Biochemistry':'BICH',
    'Biology':'BIO',
    'Chemistry':'CHEM',
    'Chinese':'CHIN',
    'Cognitive Science':'COGS',
    'Computer Science':'COMP',
    'Cultural Study Program':'CSP',
    'Critical Theory and Social Justice':'CTSJ',
    'Diplomacy and World Affairs':'DWA',
    'English and Comparative Literary Studies':'ECLS',
    'Economics':'ECON',
    'Education':'EDUC',
    'English and Writing':'ENWR',
    'French':'FREN',
    'Geology':'GEO',
    'Germany':'GERM',
    'Greek':'GRK',
    'History':'HIST',
    'Italian':'ITAL',
    'Japanese':'JAPN',
    'Kinesiology':'KINE',
    'Language':'LANG',
    'Latin':'LATN',
    'Mathematics':'MATH',
    'Music':'MUSC',
    'Physical Activity':'PHAC',
    'Philosophy':'PHIL',
    'Physics':'PHYS',
    'Politics':'POLS',
    'Psychology':'PSYC',
    'Religions':'RELS',
    'Russian':'RUSN',
    'Sociology':'SOC',
    'Spanish':'SPAN',
    'Theater':'THEA',
    'Urban and Environmental Policy':'UEP'
    }

season_list = [
        'Spring',
        'Summer',
        'Fall'
    ]
'''
year_list=[
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018
]
'''
class Course:
    def __init__(self, year, season, department, number, section, title, units, instructors, meetings,
                 core):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.title = title
        self.units = units
        self.instructors = instructors
        self.meetings = meetings
        self.core = core

def get_counts():
        counts = []
        with open('counts.tsv') as fd:
            for line in fd.read().splitlines():
                year, season, department, number, section, title, units, instructors, meetings, core = line.split('\t')
                counts.append(Course(year, season, department, number, section, title, units, instructors, meetings, core))
        return counts

def filter_by_year(list_of_courses, time_year):
    '''
    this function takes as the argument a list of courses
    and returns a new list of courses, which is the courses in the argument list
    with the correct year
    '''
    results = []
    for count in list_of_courses:
        if time_year == count.year:
            results.append(count)
    return results

def filter_by_season(list_of_courses, semester):
    results = []
    for count in list_of_courses:
        if semester == count.season:
            results.append(count)
    return results

def filter_by_department(list_of_courses, department):
    results = []
    for count in list_of_courses:
        if department == count.department:
            results.append(count)
    return results


@app.route('/')
def view_root():
    return render_template('base.html')

@app.route('/department')
def view_department():
    departments = []
    for key, value in department_list.items():
        departments.append([key, value])
    departments.sort(key=lambda x: x[0])
    return render_template('department.html', counts=departments)

@app.route('/season')
def view_season():
    semesters = []
    for semester in season_list:
        semesters.append(semester)
    return render_template('season.html', seasons=semesters)

@app.route('/<year>/<semester>/')
def view_courses_time(year, semester):
    courses_list = get_counts()
    courses_list = filter_by_year(courses_list, year)
    courses_list = filter_by_season(courses_list, semester)
    return render_template('department.html', courses=courses_list)

@app.route('/<year>/<semester>/department/<abbrev>')
def view_courses_department(year, semester, abbrev):
    courses_list = get_counts()
    courses_list = filter_by_year(courses_list, year)
    courses_list = filter_by_season(courses_list, semester)
    courses_list = filter_by_department(courses_list, abbrev)
    return render_template('department.html', courses=courses_list)

def view_seasons(semester):
    courses_list = get_counts()
    courses_list = filter_by_season(courses_list, semester)



@app.route('/professor-directory')
def view_professor_list():
    professor_list = sorted(get_counts(), key=(lambda s: s.instructors))
    return render_template('professor-directory.html', salutation='Professor Directory',counts=professor_list)



@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)



