## Coding Cycle

### Step 1: Story

- Story needs to be defined in milestone
- First requirements done
- Feature requests/bugs are created on code repositories


### Step 2: Issues
- Every FR/Bugs should have been assigned to a specific version/realease by the product owner.
- Product owner might put original estimates on issues.
- On accepting an issue, the developer should amend/set the estimate.
- Estimates can always be updated according to findings. Comments must be made as to why.
- Issue should be put _in progress_ (by applying the appropriate label) once started.


### Step 3: Branch
- The branch version should have been created by the product owner.
- create a local branch on which you are going to fix a bug or implement a feature.
  - this local branch should branch off from the version branch on the origin remote.
  - the local branch must be rebased often from the base version branch. It's the developer's responsibility to always make sure their branch doesn't steer away from the version branch.


### Step 4: Code

Important : See [coding style](CodingStyle.md)

- Only produce code that is related to the bug or FR you're working on.
- Don't mix two bug fixes or features in your local branch!
- write the tests related to the code you create
- write the documentation of the feature you implement

### Step 5: Commit

- Once your code is ready, the **tests are written and the documentation is good enough**, push your local branch to remote and create a pull request. Your pull request should ask to merge your branch to the version branch, never to master. (check [branching strategy](prodorg_branching_strategies.md) for more details)
- Include the reference to the issue you're solving in your commit
  - E.g. "Implemented live migration cockpit: #10"

### Step 6: Auto test perfome by CI
- If the project you're working on has a CI enabled, make sure that all the test passes and that your branch doesn't have conflicts.
- People won't even start reviewing your code if the tests don't pass or if your branch is out of date.

### Step 7: code reviews
- Your code will be reviewed by your peer.
- disscusion can happen on the pull request to see how to solve best a problem or if someone has a better solution to the problem.
- restart the cycle from step 3 to step 5 till everyone agree on the code produced.

### Step 8: Validate

- The code normally should be tested already by step 4 and 5
- Now the issue is put on _validate_ state
- The story owner will finally accept the pull request
- This will merge the pull request back into the version branch.
- delete your branch.
