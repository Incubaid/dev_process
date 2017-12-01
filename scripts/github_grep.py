#!/usr/bin/python3
import re

from js9 import j

def main(token, organization, regex, repo=None):
    client = j.clients.github.getClient("7473d1236b8f0b73ec82208f21ae4adc9e8d5408")
    organization = client.api.get_organization(organization)
    pattern = re.compile(regex, re.IGNORECASE)
    if repo:
        repo = organization.get_repo(repo)
        search_repo(repo, pattern)
    else:
        for repo in organization.get_repos():
            search_repo(repo, pattern)

def format(pattern, text):
    for match in pattern.finditer(text):
        start, end = match.span()
        yield "%s%s%s" % ("...",text[start-20:end+20],"...")

def search_repo(repo, pattern):
    for issue in repo.get_issues():
        title, matches = pattern.subn("\033[;7m\g<0>\033[0;0m", issue.title)
        if issue.body:
            body, body_matches = pattern.subn("\033[;7m\g<0>\033[0;0m", issue.body)
            matches += body_matches
        else:
            body_matches = 0
        matched_comments = list()
        for comment in issue.get_comments():
            comment_text, comment_matches = pattern.subn("\033[;7m\g<0>\033[0;0m", comment.body)
            if comment_matches:
                matched_comments.append((comment, comment_text))
                matches += comment_matches
        if matches:
            print("Found %s matches in %s" % (matches, issue.html_url))
            print("title:", title)
            if body_matches:
                print("body:", " ".join(format(pattern, body)))
            for comment, comment_text in matched_comments:
                print("comment:", comment.html_url)
                print("  ", " ".join(format(pattern, comment_text)))
            print()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", help="Repository name")
    parser.add_argument("token", help="Github authentication token")
    parser.add_argument("organization", help="Organization name")
    parser.add_argument("regex", help="Search expression")
    args = parser.parse_args()
    main(args.token, args.organization, args.regex, args.repo)
