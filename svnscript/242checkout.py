#!/usr/bin/env python3

import os, json, subprocess

"""
Script to pull down students code from CS242 Programming Studio
"""

directory     = "%s/cs242mod/" % (os.environ['HOME'])
students_json = "./students.json"
svn_dir       = "https://subversion.ews.illinois.edu/svn/sp16-cs242/"

class NoStudentsJsonException(Exception):
    def __init__(self, message):
        self.message = message

class SVNNotInstalled(Exception):
    def __init__(self, message):
        self.message = message

def which(program):
    """ Executable checking code taken from StackOverflow """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def setup_dir(students):
    """ Sets up directory structure of students repositories if not setup """
    if not os.path.exists(directory):
        os.makedirs(directory)
    for student in students:
        student_dir = "%s%s" % (directory, student)
        if not os.path.exists(student_dir):
            os.makedirs(student_dir)

def checkout_update_dirs(students):
    """ Checks out students svn repo's if not checked out, else updates"""
    if which("svn") is None:
        raise SVNNotInstalled("SVN software not installed")
    svn_checkout = "svn checkout %s" % (svn_dir)
    for student in students:
        student_dir = "%s%s" % (directory, student)
        if not os.path.exists("%s/%s" % (student_dir, ".svn")):
            print("Student: %s repository not checked out, checking out" % (student))
            command = "%s%s %s" % (svn_checkout, student, student_dir)
            print("Running Command %s" % (command))
            out = subprocess.call(command, shell=True)
            print("Process returned with error code %s" % out)
        else:
            print("Updating student: %s svn repository" % (student))
            command = "svn update %s" % (student_dir)
            print("Running Command %s" % (command))
            out = subprocess.call(command, shell=True)
            print("Process returned with error code %s" % out)

def get_students():
    """ Populates students with list of students from json """
    if os.path.exists(students_json) and os.path.isfile(students_json):
        with open(students_json, encoding='utf-8') as fh:
            return (json.loads(fh.read()))["netids"]
    else:
        raise NoStudentsJsonException("No students.json file found, refer to README.md")

def main():
    students = get_students()
    setup_dir(students)
    checkout_update_dirs(students)

if __name__ == "__main__":
    main()
