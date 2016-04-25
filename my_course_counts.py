from os import chdir
from os.path import dirname, realpath
import re

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

class Course:
    def __init__(self, year, season, department, number, section, title, units, instructors_meetings,
                 core, seats, enrolled, reserved, reserved_open, waitlisted):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.title = title
        self.units = units
        self.instructors_meetings = instructors_meetings
        self.core = core
        self.seats = seats
        self.enrolled = enrolled
        self.researved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted

def get_data():
    course_list = []
    with open('counts.tsv') as fd:
        course = fd.read().splitlines()
        for term in course:
            temp_list = re.split(r'\t+', term)
            year = temp_list [0]
            season = temp_list [1]
            department = temp_list [2]
            number = temp_list [3]
            section = temp_list [4]
            title = temp_list [5]
            units = temp_list [6]
            instructors =  temp_list [7]
            meetings = temp_list [8]
            core = temp_list [9]
            seats = temp_list [10]
            enrolled = temp_list [11]
            reserved = temp_list [12]
            reserved_open = temp_list [13]
            waitlisted = temp_list  [14]

            course = Course(year, season, department, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted)
            course_list.append(course)

    return course_list

def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())

def search_by_year(self, year):
    results = []
    for course in self.course:
        match = False
        for year in course.year:
            if str_contains(year, string):
                match = True
                break
        if match:
                results.append(course)
        return results

def search_by_number(self, number):
    results = []
    for course in self.course:
        match = False
        for number in course.number:
            if str_countains(number, string):
                match = True
                break
        if match:
            results.append(course)
        return results






'''
def get_year():
    courses = []
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            year, season, department, number, section, title, units, instructors, meetings,
    		core, seats, enrolled, reserved, reserved_open, waitlisted = line.split('\t')
            course.append(Course(year, season, department, number, section, title, units, instructors, meetings,
    				core, seats, enrolled, reserved, reserved_open, waitlisted))
    return sorted(students, key=(lambda s: s.year))
'''




@app.route('/')
def view_root():
    return render_template('base.html')

# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

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
