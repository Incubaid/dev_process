### This requires JS9

reponame = 'proj_ico'
owner = 'gig'

defaults = [{'color': '#e11d21', 'name': 'priority_critical'},
 {'color': '#f6c6c7', 'name': 'priority_major'},
 {'color': '#f6c6c7', 'name': 'priority_minor'},
 {'color': '#d4c5f9', 'name': 'process_duplicate'},
 {'color': '#d4c5f9', 'name': 'process_wontfix'},
 {'color': '#bfe5bf', 'name': 'state_inprogress'},
 {'color': '#bfe5bf', 'name': 'state_question'},
 {'color': '#bfe5bf', 'name': 'state_verification'},
 {'color': '#fef2c0', 'name': 'type_bug'},
 {'color': '#fef2c0', 'name': 'type_feature'},
 {'color': '#fef2c0', 'name': 'type_question'}]

cl = j.clients.gogs.getRestClient('https://docs.greenitglobe.com', 443, accesstoken='*****')
for label in defaults:
  cl.labelCreate(reponame=reponame, label_name=label['name'], label_color=label['color'], owner=owner)

### to create for all repos in an org
for repo in cl.reposList(owner):
     repo = repo[1].split(owner+'/')[1]
     for label in defaults:
         cl.labelCreate(reponame=repo, label_name=label['name'], label_color=label['color'], owner=owner)
