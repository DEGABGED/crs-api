from lxml import html
import requests
import urllib
from crs_parser.models import Subject, Schedule
from crs_parser.helpers import string_safe_int

class CRSScheduleParser(object):
    # Class variable
    crs_url = 'https://crs.upd.edu.ph/schedule/'

    def __init__(self):
        self.subjects = []

    # Returns a list of Subject objects, given by the search term or alphabetical category "Subject"
    def get_by_search(self, subject, term="120182", clear=True):
        # Variables from the user supposedly
        term = urllib.parse.quote(term, safe='')
        subject = urllib.parse.quote(subject, safe='')

        # Create the url from where you will parse the website
        url = self.crs_url + term + '/' + subject
        page = requests.get(url)
        tree = html.fromstring(page.content)

        xpath = '//table[@id="tbl_schedule"]/tbody'
        count = len(tree.xpath(xpath)) + 1
        if (clear):
            self.subjects.clear()

        for row in range(1,count):
            subj_class = self.parse_subject(xpath + '[{r}]'.format(r=row), tree)
            if (subj_class != None):
                self.subjects.append(subj_class)

        return self.subjects

    # Parses a row in the CRS schedules table
    # Done by row since working with lists is a pain in the ass
    def parse_subject(self, row_xpath,tree):
        # If subject is dissolved, return nothing
        if (tree.xpath(row_xpath + '/tr/td[6]/strong/text()')[0] == "DISSOLVED"):
            return

        xpath = '//table[@id="tbl_schedule"]/tbody/tr/td[{col}]/text()'
        subject = Subject()

        # Get the easier fields first
        subject.class_code = tree.xpath(row_xpath + '/tr/td[1]/text()')[0]
        subject.class_name = tree.xpath(row_xpath + '/tr/td[2]/text()')[0]
        subject.credits = float(tree.xpath(row_xpath + '/tr/td[3]/text()')[0])
        subject.course = ' '.join(subject.class_name.split()[0:2])

        subject.slots_avail = string_safe_int(tree.xpath(row_xpath + '/tr/td[6]/strong/text()')[0])
        subject.slots_total = int(tree.xpath(row_xpath + '/tr/td[6]/text()')[1].strip(' /\n\t'))
        subject.demand = int(tree.xpath(row_xpath + '/tr/td[7]/text()')[0])

        # Parse the schedule and instructor
        sched, instr, *tail = tree.xpath(row_xpath + '/tr/td[4]/text()')
        subject.schedule = list(map(Schedule.parse, sched.split(';')))
        subject.instructor = instr.strip()

        # Gather all the remarks
        remarks = tree.xpath(row_xpath + '/tr/td[4]/em/text()')
        enlisting = tree.xpath(row_xpath + '/tr/td[5]/text()')[0].strip()
        restrict = '; '.join(map(lambda x: x.strip(), tree.xpath(row_xpath + '/tr/td[8]/text()')))

        subject.remarks = (remarks[0] + "; " if remarks else "") + "Enlisting unit - " + enlisting + "; " + restrict

        return subject

