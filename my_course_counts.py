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

def filter_by_season(list_of_courses, time_season):
    results = []
    for count in list_of_courses:
        if time_season == count.season:
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
    for item in department_list:
        departments.append(item)
        sorted_list = departments
        sorted_list.sort(key=lambda x: x[0])
    return render_template('department.html', counts=departments)

# FIXME
@app.route('/<year>/<semester>/')
def view_courses(year, semester, abbrev):
    courses_list = get_counts()
    courses_list = filter_by_year(courses_list, year)
    courses_list = filter_by_season(courses_list, semester)
    return render_template('department.html', courses=courses_list)

@app.route('/<year>/<semester>/department/<abbrev>')
def view_courses(year, semester, abbrev):
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








def filter_by_department(list_of_courses, department):
    return list_of_courses # FIXME








'''
    for count in counts_list:
        if year == count.year and department == count.department:
            current_department = count
'''


'''
def main():
    # An example that ties everything together
    Course_Directory = get_data()
'''
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






       '''
    def __init__(self):
        self.courses_list = []

    def search_by_instructor(self, instructors):
        results = []
        for course in self.courses_list:
            match = True
            for instructor in instructors:
                if not str_contains(course.instructors, instructor):
                    match = False
                    break
            if match:
                results.append(course)
        return results

    def search_by_title(self, title):
        results = []
        for course in self.courses_list:
            match = True
            for word in course.title:
                if not str_contains(course.title, word):
                    match = False
                    break
                if match:
                    results.append(course)
            return results
                # veronica

    def search_by_season(self, season):
        results = []
        for course in self.courses_list:
            match = True
            if not str_contains(course.season, season):
                match = False
                break
            if match:
                results.append(course)
            return results
            # Veronica

    def search_by_department(self, department):
        results = []
        for course in self.courses_list:
            match = True
            if not str_contains(course.department, department):
                match = False
                break
            if match:
                results.append(course)
            return results
            # Veronica

    def search_by_core(self, core):
        results = []
        for course in self.courses_list:
            match = True
            if not str_contains(course.core, core):
                match = False
                break
        if match:
            results.append(course)
        return results

    def search_by_year(self, year):
        results = []
        for course in self.courses_list:
            match = True
            if not str_contains(course.year, year):
                match = False
            break
            if match:
                results.append(course)
            return results

    def search_by_number(self, number):
        results = []
        for course in self.courses_list:
            match = True
            if not str_contains(course.number, number):
                match = True
            break
            if match:
                results.append(course)
            return results


def get_data():
    course_directory = Course_Directory()
    instructor_list = []
    title_list = []
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            temp_list = line.split('\t')
            course = Course(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], title_list,
                            temp_list[6], instructor_list, temp_list[8], temp_list[9], temp_list[10], temp_list[11],
                            temp_list[12], temp_list[13], temp_list[14])
            for instructor in temp_list[7]:
                instructor_list.append(instructor)
            for word in temp_list[5]:
                title_list.append(word)
        course_directory.courses_list.append(course)
    return course_directory
'''
