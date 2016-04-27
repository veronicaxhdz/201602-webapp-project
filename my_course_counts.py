def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())


class Course:
    def __init__(self, year, season, department, number, section, title, units, instructors, meetings,
                 core, seats, enrolled, reserved, reserved_open, waitlisted):
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
        self.seats = seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted


class Course_Directory:
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


def main():
    # An example that ties everything together
    Course_Directory = get_data()
