#!/usr/bin/env python
import argparse
import json
import requests

user = accesstoken = ''


def main(organization, repos, version, branch, message, draft, prerelease):
    url = 'https://api.github.com/repos/{org}/{repo}/releases'

    for repo in repos:
        if not message:
            message = "release {}".format(version)
        if version[0] != 'v':
            version = "v{}".format(version)

        release = {
            "tag_name": version,
            "target_commitish": branch,
            "name": version,
            "body": message,
            "draft": draft,
            "prerelease": prerelease
        }

        print("create release {} on {}/{}".format(version, organization, repo))
        release = requests.post(url.format(org=organization, repo=repo,), json.dumps(release), auth=(user, accesstoken)).json()
        print("created at {}".format(release['html_url']))


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Github username', required=True)
    parser.add_argument('-t', help='Github accesstoken', required=True)
    parser.add_argument('-o', help='Github organization', required=True)
    parser.add_argument('-r', help='Repositories to create milestones to', nargs='+')
    parser.add_argument('-v', help='version of the release')
    parser.add_argument('-b', help='branch on which create the tag')
    parser.add_argument('-m', help='release message')
    parser.add_argument('-d', help='create a draft release', default=False, type=str2bool, nargs='?', const=True)
    parser.add_argument('-p', help='create pre-release', default=False, type=str2bool, nargs='?', const=True)
    args = parser.parse_args()

    user = args.u
    accesstoken = args.t

    main(args.o, args.r, args.v, args.b, args.m, args.d, args.p)
