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

def get_year():
    year = []
    with open('counts.csv') as file:
        text = file.read()
    course_list = text.splitlines()
    for  in list:
        temp_list = re.split(r'\t+', term)
        title = temp_list[0]
        year = temp_list[1]





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
