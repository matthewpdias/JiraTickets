import random

random.seed

def get_issue_type():
    selection = random.randint(1, 4)
    if selection == 1:
        return "Bug"
    elif selection == 2:
        return "Story"
    else:
        return "Task"

def get_new_version(version):
    return "2.0.0"
    #randomly increment

def get_description(type):
    story = ["add user pictures to APP", "update the API for service1", "please create a home view for component A", "update the buttons in component B", "add automatic restart to service2", "generate logs for service2", "update base for future releases", "enable user reporting of bugs in APP", "import user data from component A to component B"]

    task = ["changing colors on APP", "adding optional short API urls", "minor UI tweak for componentA", "changing graphics to new logo in base", "changing encryption hash for passwords", "running performance tests on service2", "backing up customer logs for APP", "adding server to reduce latency for API", "updating security setting on API servers", "submitting a new version of APP to app store", "changing fonts for component B"]

    bug = ["APP login page is slow", "buttons in component A are not visible", "missing routes in component A", "service1 not restarting", "graphics not displaying in base", "typo on component B loading screen", "API requests unresponsive from app", "problem opening multiple instances of APP", "mutliple logins cause service1 to crash", "API cannont handle two identical requests simultaneously", "bug in base casuing users to be logged out"]

    if type == "Bug":
        return random.choice(story)
    elif type == "Story":
        return random.choice(bug)
    else:
        return random.choice(task)

def get_assignee():
    assignees =['Justin', 'Matt', 'Tyler', 'Eddie', 'Shane']
    return random.choice(assignees)
    #randomly select option

def get_priority():
    priorities = ['Lowest', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Highest']
    return random.choice(priorities);

def get_create_date():
    if random.randint(1,2) == 1:
        month = random.randint(10, 12)
        year = 2016
        day = random.randint(1, 30)
    else:
        month = random.randint(1, 2)
        year = 2017
        day = random.randint(1, 28)
    return str(month) + '/' + str(day) + '/' + str(year)

def generate_date():
    roll = random.randint(1, 3)
    if roll == 1:
        month = random.randint(10, 12)
        year = 2016
        date = random.randint(1, 30)
    elif roll == 2:
        month = random.randint(1, 2)
        year = 2017
        date = random.randint(1, 28)
    else :
        month = 3
        date = random.randint(1, 8)
        year = 2017
    return month, date, year

def get_update_date(date):

    create_date = date.split('/')

    #until the function returns successfully
    while True:
        modify_date = generate_date()

        #if the modify was a year ahead
        if int(create_date[2]) < modify_date[2]:
            return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

        #if the modify was in the same year and a later month
        elif int(create_date[2]) == modify_date[2] and int(create_date[0]) < modify_date[0]:
            return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

        #if the modify was in the same year and month but on the same or a future day
        elif int(create_date[2]) == modify_date[2] and int(create_date[0]) == modify_date[0] and int(create_date[1]) <= modify_date[1]:
            return str(modify_date[0])+ '/'+ str(modify_date[1]) + '/' + str(modify_date[2])

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
        self.release_ver = 1;

    def advance_version(self):
        if self.cur_ver == release_versions[self.project_key][0]:
            self.cur_ver = release_versions[self.project_key][1]
            self.release_ver = 2
        if self.cur_ver == release_versions[self.project_key][1]:
            self.cur_ver = release_versions[self.project_key][2]
            self.release_ver = 3

    def get_status(self):
        if self.release_ver == 1:
            statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
        elif self.release_ver == 2:
            statuses = ['Open', 'In Progress', 'Resolved', 'Resolved', 'Resolved', 'Closed', 'Closed', 'Closed']
        else:
            statuses = ['Closed', 'Resolved', 'Resolved', 'In Progress','In Progress','In Progress', 'Open', 'Open', 'Open', 'Open']
        return random.choice(statuses)

    def get_prev_version(self):
        if self.release_ver == 3:
            return release_versions[self.project_key][1]
        elif self.release_ver == 2:
            return release_versions[self.project_key][0]
        else:
            return self.cur_ver

    #print a .csv row
    def generate_ticket(self):
        self.issue_type = get_issue_type()
        self.summary = get_description(self.issue_type)
        self.status =  self.get_status()
        self.assignee = get_assignee()
        self.reporter = 'Chris'
        self.description = self.summary
        self.priority = get_priority()
        self.created_at = get_create_date()
        self.updated_at = get_update_date(self.created_at)
        self.fix_ver1 = ""
        self.fix_ver2 = ""
        self.fix_ver3 = ""
        self.affects_ver1 = self.cur_ver
        self.affects_ver2 = ""
        self.affects_ver3 = ""

        print(self.project_type + "," + self.project_name + "," + self.project_key + "," + self.issue_type + "," + self.summary + "," + self.status + "," + self.assignee + "," + self.reporter + "," + self.description + "," + self.priority + ","
        + self.created_at + "," + self.updated_at + "," + self.fix_ver1 + "," + self.fix_ver2 + "," + self.fix_ver3 + "," + self.affects_ver1 + "," + self.affects_ver2 + "," + self.affects_ver3)




################################################################################
#######           GENERATE TICKETS BELOW HERE
################################################################################



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

#Put the projects in a list, to make them easier to loop over
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

#Print the CSV headers
print("Project Type,Project Name,Project Key,Issue Type,Summary,Status,Assignee,Reporter,Description,Priority,Date Created,Date Modified,Fix Version,Fix Version,Fix Version,Affects Version,Affects Version,Affects Version")

#make 300 tickets at release 1
for i in range (300):
    cur_proj = random.choice(projlist)
    cur_proj.generate_ticket()

#iterate projects to next release
for project in projlist:
    project.advance_version()

#make 500 tickets at release 2
for i in range (500):
    cur_proj = random.choice(projlist)
    cur_proj.generate_ticket()

#iterate projects to next release
for project in projlist:
    project.advance_version()

#make 500 tickets at release 3
for i in range (200):
    cur_proj = random.choice(projlist)
    cur_proj.generate_ticket()
