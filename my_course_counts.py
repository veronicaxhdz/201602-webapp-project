from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())


department_list = {
    'American Study': 'AMST',
    'Arabic': 'ARAB',
    'Art History': 'ARTH',
    'Art Studio': 'ARTS',
    'Biochemistry': 'BICH',
    'Biology': 'BIO',
    'Chemistry': 'CHEM',
    'Chinese': 'CHIN',
    'Cognitive Science': 'COGS',
    'Computer Science': 'COMP',
    'Cultural Study Program': 'CSP',
    'Critical Theory and Social Justice': 'CTSJ',
    'Diplomacy and World Affairs': 'DWA',
    'English and Comparative Literary Studies': 'ECLS',
    'Economics': 'ECON',
    'Education': 'EDUC',
    'English and Writing': 'ENWR',
    'French': 'FREN',
    'Geology': 'GEO',
    'Germany': 'GERM',
    'Greek': 'GRK',
    'History': 'HIST',
    'Italian': 'ITAL',
    'Japanese': 'JAPN',
    'Kinesiology': 'KINE',
    'Language': 'LANG',
    'Latin': 'LATN',
    'Mathematics': 'MATH',
    'Music': 'MUSC',
    'Physical Activity': 'PHAC',
    'Philosophy': 'PHIL',
    'Physics': 'PHYS',
    'Politics': 'POLS',
    'Psychology': 'PSYC',
    'Religions': 'RELS',
    'Russian': 'RUSN',
    'Sociology': 'SOC',
    'Spanish': 'SPAN',
    'Theater': 'THEA',
    'Urban and Environmental Policy': 'UEP'
}

season_list = [
    'spring',
    'summer',
    'fall'
]

year_list = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017

]


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
            year, season, department, number, section, title, units, instructors, meetings, core, *rest = line.split(
                '\t')
            counts.append(Course(year, season, department, number, section, title, units, instructors, meetings, core))
    return counts


def filter_by_year(list_of_courses, time_year):
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


@app.route('/year')
def view_year():
    years = []
    for year in year_list:
        years.append(year)
    return render_template('year.html', years=years)


@app.route('/<year>/season')
def view_season(year):
    semesters = []
    for semester in season_list:
        semesters.append(semester)
    return render_template('season.html', year=year, semesters=semesters)


@app.route('/<year>/<season>/department')
def view_department(year, season):
    departments = []
    for key, value in department_list.items():
        departments.append([key, value])
    departments.sort(key=lambda x: x[0])
    return render_template('department.html', year=year, seasons=season, counts=departments)


@app.route('/<year>/<season>/department/<abbrev>')
def view_courses_department(year, season, abbrev):
    courses_list = get_counts()
    print(len(courses_list))
    courses_list = filter_by_year(courses_list, year)
    print(len(courses_list))
    courses_list = filter_by_season(courses_list, season)
    print(len(courses_list))
    courses_list = filter_by_department(courses_list, abbrev)
    return render_template('department-abbrev.html', year=year, season=season, courses=courses_list)


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
