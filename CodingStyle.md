## Coding Style and convention.

Contributing to open source project implies to working with different people that have different habits. In order to not loose time in useless disscusion about coding style we describe here the convention we want to enforce in our code repositories.


### Always use a linter

Following the convention of the language you are using helps other people to understand your code and make code easier to read.

Linter does more then just make the code easier to read, more idiomatic but it can often warn you about dangerous construct or buggy code.

For Atom:
 - python: https://github.com/AtomLinter/linter-pylint
 - go: https://github.com/joefitzgerald/gometalinter-linter

### Format your code

Write clean code. Universally formatted code promotes ease of writing, reading, and maintenance.

- For Go Always run `gofmt -s -w file.go` on each changed file before committing your changes. Most editors have plug-ins that do this automatically.  
For Atom: https://github.com/joefitzgerald/gofmt

- For Python we choose to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/)  
Always run `autopep8 -a --max-length 120 file.py` on each changed file before committing your changes. Most editors have plug-ins that do this automatically.  
For Atom: https://github.com/markbaas/atom-python-autopep8



### Pull request
Pull request descriptions should be as clear as possible and include a reference to all the issues that they address.

Commit messages must start with a capitalized and short summary (max. 50 chars) written in the imperative, followed by an optional, more detailed explanatory text which is separated from the summary by an empty line.

Code review comments may be added to your pull request. Discuss, then make the suggested modifications and push additional commits to your feature branch. Post a comment after pushing. New commits show up in the pull request automatically, but the reviewers are notified only when you comment.

Pull requests must be cleanly rebased on top of the version branch without multiple branches mixed into the PR.

**Git tip:** If your PR no longer merges cleanly, use rebase master in your feature branch to update your pull request rather than merge master.

Before you make a pull request, squash your commits into logical units of work using git rebase -i and git push -f. A logical unit of work is a consistent set of patches that should be reviewed together: for example, upgrading the version of a vendored dependency and taking advantage of its now available new feature constitute two separate units of work. Implementing a new function and calling it in another file constitute a single logical unit of work. The very high majority of submissions should have a single commit, so if in doubt: squash down to one.

Include an issue reference like Closes #XXXX or Fixes #XXXX in commits that close an issue. Including references automatically closes the issue on a merge.

### Make sure your code pass the test suite:
After every commit, make sure the test suite passes. Include documentation changes in the same pull request so that a revert would remove all traces of the feature or fix.
