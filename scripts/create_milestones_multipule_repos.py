import github
cl = github.Github('******')
 
milestones = [{'name': '9.0.0', 'description': ''},
  {'name': '9.0.1', 'description': ''},
  {'name': '9.1.0', 'description': ''}]


repos = ['core9', 'developer', 'lib9', 'prefab9', 'ays9', 'portal9']

org = cl.get_organization('jumpscale')
for repo in repos:
    r = org.get_repo(repo)
    existing = r.get_milestones()
    existing = [l.title for l in existing]
    for milestone in milestones:
        if milestone['name'] not in existing:
            r.create_milestone(title=milestone['name'], description=milestone['description'])
