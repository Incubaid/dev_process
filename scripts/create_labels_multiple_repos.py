import github
cl = github.Github('*******')

labels = [{'color': 'e11d21', 'name': 'priority_critical'},
 {'color': 'f6c6c7', 'name': 'priority_major'},
 {'color': 'f6c6c7', 'name': 'priority_minor'},
 {'color': 'd4c5f9', 'name': 'process_duplicate'},
 {'color': 'd4c5f9', 'name': 'process_wontfix'},
 {'color': 'bfe5bf', 'name': 'state_inprogress'},
 {'color': 'bfe5bf', 'name': 'state_question'},
 {'color': 'bfe5bf', 'name': 'state_verification'},
 {'color': 'fef2c0', 'name': 'type_bug'},
 {'color': 'fef2c0', 'name': 'type_feature'},
 {'color': 'fef2c0', 'name': 'type_question'}]

repos = ['core9', 'developer', 'lib9', 'prefab9', 'ays9', 'portal9']

org = cl.get_organization('jumpscale')
for repo in repos:
    r = org.get_repo(repo)
    existing = r.get_labels()
    existing = [l.name for l in existing]
    for label in labels:
        if label['name'] not in existing:
            r.create_label(name=label['name'], color=label['color'])

