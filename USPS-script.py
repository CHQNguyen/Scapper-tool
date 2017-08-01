
from mechanize import Browser
import re


def select_control(control):
  r = re.compile(r'IgnoreControl')
  return bool(re.match(r, control.name))

# navigate to USPS site
url = 'https://moversguide.usps.com/icoa/move-info/icoa-main-flow.do?execution=e1s8&_flowId=icoa-main-flow'
br = Browser()
br.set_handle_robots(False)
br.open(url)
for form in br.forms():
    print "Form name:", form.name
    print form
br.form = list(br.forms())[0]
print br.form

br.form.set_all_readonly(False)
for control in br.form.controls:
    print control

# Navigate past acknowlegdment page
br.submit()
a = br.response()
br.select_form("forwadingPeriod")

for form in br.forms():
    print "2 Form name:", form.name
    print form

for control in br.form.controls:
    print control

# Filling out beginning and end date of move
br.form.set_all_readonly(False)
br.form['isPermanent'] = ['true',]
br.form['startDateStr']='5/30/2017'
br.form['endDateStr']='5/30/2017'
br.form['type'] = ['INDIVIDUAL',]
br.form['_eventId_back'] = ''
ctrl = br.form.find_control('_eventId_back')
ctrl.disabled = True

# Submitted information for the second page
br.submit()
for form in br.forms():
    print "Form name:", form.name
    print form

