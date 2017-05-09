#!/usr/bin/env python
import argparse
import json
import requests

user = accesstoken = ''

def get_repos(organization):
    repos = requests.get('https://api.github.com/search/repositories?q=user:'+organization, auth=(user,accesstoken)).json()
    return [r['name'] for r in repos['items']]

def get_milestones(organization, repo):
    milestones = requests.get('https://api.github.com/repos/'+organization+'/'+repo+'/milestones?state=all', auth=(user,accesstoken)).json()
    return [{'title':m['title'],'state':m['state'],'description':m['description'],'due_on':m['due_on'],'number':m['number']} for m in milestones]


def update_milestone(organization, repo, milestone):
    requests.patch('https://api.github.com/repos/'+organization+'/'+repo+'/milestones/'+str(milestone['number']), json.dumps(milestone), auth=(user,accesstoken))

def create_milestone(organization, repo, milestone):
    requests.post('https://api.github.com/repos/'+organization+'/'+repo+'/milestones', json.dumps(milestone), auth=(user,accesstoken))

def main(organization, fromrepo, destrepos=[]):
    repos = get_repos(organization)
    if fromrepo not in repos:
        print('No "'+fromrepo+'" repository found')
        return
    repos.remove(fromrepo)

    if destrepos:
        for repo in destrepos:
            if repo not in repos:
                print('No "'+repo+'" repository found')
                return
        repos = destrepos

    from_milestones_list = get_milestones(organization,fromrepo)
    from_milestones = dict()
    for milestone in from_milestones_list:
        from_milestones[milestone['title']] = milestone

    for repo in repos:
        print('updating milestones for '+repo)
        updated_milestones = []
        milestones = get_milestones(organization, repo)
        for milestone in milestones:
            if milestone['title'] in from_milestones:
                from_milestone = from_milestones[milestone['title']]
                milestone['description'] = from_milestone['description']
                milestone['due_on'] = from_milestone['due_on']
                milestone['state'] = from_milestone['state']
                update_milestone(organization, repo, milestone)
                updated_milestones.append(milestone['title'])
        for milestone in from_milestones:
            if from_milestones[milestone]['state'] != 'open':
                continue
            if milestone not in updated_milestones:
                pass
                create_milestone(organization, repo, from_milestones[milestone])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Github username', required=True)
    parser.add_argument('-p', help='Github accesstoken', required=True)
    parser.add_argument('-o', help='Github organization', required=True)
    parser.add_argument('-s', help='Repository to copy the milestones from', default='home')
    parser.add_argument('-d', help='Repository to copy the milestones to', default=None)
    args = parser.parse_args()
    user = args.u
    accesstoken = args.p
    main(args.o, args.s, args.d.split(','))
