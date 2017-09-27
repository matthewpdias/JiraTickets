import random

random.seed

#generate a "created at" date
def get_create_date():
    month = random.randint(8, 10)
    year = 2017
    day = random.randint(1, 30)
    return str(month) + '/' + str(day) + '/' + str(year)

#generate a "date updated"
def generate_date():
    month = random.randint(9, 12)
    date = random.randint(1, 30)
    year = 2017
    return month, date, year

#get date modified
def get_update_date(date):

    create_date = date.split('/')

    #until the function returns successfully
    while True:
        modify_date = generate_date()

        #if the modify was a year ahead
        #
        # Not used when year is the same
        #
        #if int(create_date[2]) < modify_date[2]:
        #    return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

        #if the modify was in the same year and a later month
        if int(create_date[2]) == modify_date[2] and int(create_date[0]) < modify_date[0]:
            return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

        #if the modify was in the same year and month but on the same or a future day
        elif int(create_date[2]) == modify_date[2] and int(create_date[0]) == modify_date[0] and int(create_date[1]) <= modify_date[1]:
            return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

def get_status(self):
    if self.cur_ver == release_versions[self.project_key][0]:
        statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
    elif self.cur_ver == release_versions[self.project_key][1]:
        statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
    else:
        statuses = ['Closed', 'Resolved', 'Resolved', 'In Progress','In Progress','In Progress', 'Open', 'Open', 'Open', 'Open']
    return random.choice(statuses)

def get_assignee():
    assignees =['Justin', 'Matt', 'Tyler', 'Eddie', 'Shane']
    return random.choice(assignees)

class Project:
    #initializer
    def __init__(self, p_type, p_name, p_key):
        self.project_type = p_type
        self.project_name = p_name
        self.project_key = p_key
        self.issue_type = "not_set"
        self.cur_ver = release_versions[p_key][0]
        self.summary = "not_set"
        self.status = "not_set"
        self.assignee = "not_set"
        self.reporter = "not_set"
        self.description = "not_set"
        self.priority = "not_set"
        self.created_at = "not_set"
        self.updated_at = "not_set"
        self.fix_ver1 = "not_set"
        self.fix_ver2 = "not_set"
        self.fix_ver3 = "not_set"
        self.affects_ver1 = "not_set"
        self.affects_ver2 = "not_set"
        self.affects_ver3 = "not_set"
        self.release_ver = 1

    def advance_version(self):
    		#if we are on 0, go to 1
        if self.release_ver == 1:
            self.cur_ver = release_versions[self.project_key][1]
            self.release_ver = 2
           #if we are on 1, go to 2
        elif self.release_ver == 2:
            self.cur_ver = release_versions[self.project_key][2]
            self.release_ver = 3

    def get_status(self):
        if self.cur_ver == release_versions[self.project_key][0]:
            statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
        elif self.cur_ver == release_versions[self.project_key][1]:
            statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
        else:
            statuses = ['Closed', 'Resolved', 'Resolved', 'In Progress','In Progress','In Progress', 'Open', 'Open', 'Open', 'Open']
        return random.choice(statuses)

    #print a .csv row
    def generate_ticket(self):
        self.issue_type = "Epic"

        self.epic_name = self.summary = self.description = epic_dictionary[self.project_key]
        epic_dictionary[self.project_key].remove(self.epic_name)

        self.status =  self.get_status()
        self.assignee = get_assignee()
        self.reporter = 'Chris'
        self.priority = get_priority()
        self.created_at = get_create_date()
        self.updated_at = get_update_date(self.created_at)
        self.fix_ver1 = self.cur_ver
        self.fix_ver2 = ""
        self.fix_ver3 = ""
        self.affects_ver1 = ""
        self.affects_ver2 = ""
        self.affects_ver3 = ""

        print(self.project_type + "," + self.project_name + "," + self.project_key + "," + self.issue_type + "," + self.epic_name  + "," self.summary + "," + self.status + "," + self.assignee + "," + self.reporter + "," + self.description + "," + self.priority + ","
        + self.created_at + "," + self.updated_at + "," + self.fix_ver1 + "," + self.fix_ver2 + "," + self.fix_ver3 + "," + self.affects_ver1 + "," + self.affects_ver2 + "," + self.affects_ver3)


    epic_dictionary = {
        'AWEB': ['Producer Web responsiveness improvements', 'Producer Web fault tolerence', 'Producer Web security evaluations'],
        'PWEB': ['Provider Web responsiveness improvements', 'Provider Web fault tolerence', 'Provider Web security evaluations'],
        'MWEB': ['Member Web responsiveness improvements', 'Member Web fault tolerence', 'Member Web security evaluations'],
        'PMOB': ['Provider Mobile responsiveness improvements', 'Provider Mobile fault tolerence', 'Provider Mobile security evaluations'],
        'MMOB': ['Member Mobile responsiveness improvements', 'Member Mobile fault tolerence', 'Member Mobile security evaluations'],
        'CLMS': ['Claims responsiveness improvements', 'Claims fault tolerence', 'Claims security evaluations'],
        'BILL': ['Billing responsiveness improvements', 'Billing fault tolerence', 'Billing security evaluations'],
        'DABA': ['Database responsiveness improvements', 'Database fault tolerence', 'Database security evaluations'],
        'BESR': ['Backend Services responsiveness improvements', 'Backend Services fault tolerence', 'Backend Services security evaluations'],
        'PBSR': ['Public Services responsiveness improvements', 'Public Services fault tolerence', 'Public Services security evaluations'],
        'RPRT': ['Reporting responsiveness improvements', 'Reporting fault tolerence', 'Reporting security evaluations'],
        }

#
# *Note* this MUST match the release schedule in generate_issues.py
#
#release schedule. You can change the numbers, but adding or removing a column will effect other functions

release_versions = {
    'AWEB' : ['4.3.0', '4.3.0', '4.4.1'],
    'PWEB' : ['5.2.2', '5.2.3', '5.2.4'],
    'MWEB' : ['2.1.7', '2.1.8', '3.0.1'],
    'PMOB' : ['3.2.6', '3.3.0', '3.3.1'],
    'MMOB' : ['6.8.5', '6.9.0', '7.0.1'],
    'CLMS' : ['2.4.4', '2.4.5', '3.0.0'],
    'BILL' : ['2.0.2', '2.0.2', '2.0.2'],
    'DABA' : ['1.4.1', '1.5.0', '1.5.2'],
    'BESR' : ['2.4.1', '2.4.2', '2.5.0'],
    'PBSR' : ['3.2.4', '3.3.0', '3.3.1'],
    'RPRT' : ['1.4.7', '1.4.7', '1.4.7'],
}

#initialize projects. You can have as many projects with any names without changing any code
proj1 = Project('software','Producer Web', 'AWEB')
proj2 = Project('software','Provider Web', 'PWEB')
proj3 = Project('software','Member Web', 'MWEB')
proj4 = Project('software','Provider Mobile', 'PMOB')
proj5 = Project('software','Member Mobile', 'MMOB')
proj6 = Project('software','Claims', 'CLMS')
proj7 = Project('software','Billing', 'BILL')
proj8 = Project('software','Database', 'DABA')
proj9 = Project('software','Backend Services', 'BESR')
proj10 = Project('software','Public Services', 'PBSR')
proj11 = Project('software','Reporting', 'RPRT')

#create a list of projects and add our projects to this list
projlist = []
projlist.append(proj1)
projlist.append(proj2)
projlist.append(proj3)
projlist.append(proj4)
projlist.append(proj5)
projlist.append(proj6)
projlist.append(proj7)
projlist.append(proj8)
projlist.append(proj9)
projlist.append(proj10)
projlist.append(proj11)

print("Project Type,Project Name,Project Key,Issue Type,Summary,Status,Assignee,Reporter,Description,Priority,Date Created,Date Modified,Fix Version,Fix Version,Fix Version,Affects Version,Affects Version,Affects Version")

for project in projlist do:
    Project.generate_ticket
    project.advance_version()
    Project.generate_ticket
    project.advance_version()
    Project.generate_ticket
    project.advance_version()
