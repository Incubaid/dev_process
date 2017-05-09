#!/usr/bin/env python
import argparse
import json
import requests

user = accesstoken = repo = ''

wanted_labels = {
  'priority_critical': {
    "name": "priority_critical",
    "color": "b60205"
  },
  'priority_major':{
    "name": "priority_major",
    "color": "f9d0c4"
  },
  'priority_minor':{
    "name": "priority_minor",
    "color": "f9d0c4"
  },
  'process_duplicate':{
    "name": "process_duplicate",
    "color": "d4c5f9"
  },
  'process_wontfix':{
    "name": "process_wontfix",
    "color": "d4c5f9"
  },
  'state_inprogress':{
    "name": "state_inprogress",
    "color": "c2e0c6"
  },
  'state_planned':{
    "name": "state_planned",
    "color": "c2e0c6"
  },
  'state_question':{
    "name": "state_question",
    "color": "c2e0c6"
  },
  'state_verification':{
    "name": "state_verification",
    "color": "c2e0c6"
  },
  'type_bug':{
    "name": "type_bug",
    "color": "fef2c0"
  },
  'type_feature':{
    "name": "type_feature",
    "color": "fef2c0"
  },
  'type_question':{
    "name": "type_question",
    "color": "fef2c0"
  },
  'type_ticket':{
    "name": "type_ticket",
    "color": "fef2c0"
  }
}

update_to = {
    'bug':'type_bug',
    'duplicate':'process_duplicate',
    'enhancement':'type_feature',
    'help wanted':'type_question',
    'in progress':'state_inprogress',
    'invalid':'process_wontfix',
    'question':'state_question',
    'wontfix':'process_wontfix'
}

def get_existing_labels():
    return requests.get('https://api.github.com/repos/'+repo+'/labels', auth=(user,accesstoken)).json()

def delete_label(label_name):
    requests.delete('https://api.github.com/repos/'+repo+'/labels/'+label_name, auth=(user, accesstoken))

def update_label(oldname, label_data):
    requests.patch('https://api.github.com/repos/'+repo+'/labels/'+oldname, json.dumps(label_data), auth=(user,accesstoken))

def create_label(label_data):
    requests.post('https://api.github.com/repos/'+repo+'/labels', json.dumps(label_data), auth=(user,accesstoken))

def main(user,accesstoken, repo):
    existing_labels = [l['name'] for l in get_existing_labels()]
    updated=[]
    for existing_label in existing_labels:
        if existing_label not in update_to and existing_label not in wanted_labels:
            delete_label(existing_label)
            continue
        if existing_label in update_to:
            update_label(existing_label, wanted_labels[update_to[existing_label]])
            updated.append(update_to[existing_label])
        else:
            update_label(existing_label, wanted_labels[existing_label])
            updated.append(existing_label)
    for new_label in wanted_labels.values():
        if new_label['name'] not in updated:
            create_label(new_label)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Github username', required=True)
    parser.add_argument('-p', help='Github accesstoken', required=True)
    parser.add_argument('-r', help='Github repository ( organization/repo )', required=True)
    args = parser.parse_args()
    user = args.u
    accesstoken = args.p
    repo = args.r
    main(args.u, args.p, args.r)