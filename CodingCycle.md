## Coding Cycle

### Step 1: Story 

- Story needs to be defined in milestone
- First requirements done


### Step 2: Branch

- Work on branch with as name the story card short name (which needs to be unique per story card as defined in milestone repo)
  - Only create branches for story cards, not for tasks
  - This can go over multiple repo's if needed
- Never commit to master!


### Step 3: Code

- Work on your code in iterative steps
- This can be done by multiple people


### Step 4: Commit / code reviews

- Perform a peer review before you commit. The goal is that you go over your diff while explaining to your peer what you changed. It happens very often that you find bugs or shortcomings while you are explaining your work.
- Include the reference to the task in your commit
   - Notation format storyname#taskreference
   - E.g. "Implemented live migration cockpit#10"


### Step 5: Test / code reviews

- Create pull request for code reviews if it doesn't exist yet
	- Only 1 pull request per story (is 1 branch) per repo
- Anyone, tester or developer, can test this branch in a production environment, which means testing infrasturcture needs to be setup to allow easy tests and building from any branch or set of branches
- This needs to be part of coding, go back to step 3 for many iterations!


### Step 5b: Someone needs your code

- If other stories depend on your code, intermediate pull requests can be created, validated and merged in on the other branch or master (careful!)
- Best to avoid this step if not required, normally it means your story was too big and should have been cut in multiple pieces


### Step 6: Validate

- The code normally should be tested already by step 4 and 5
- Now the story is put on validate state
- A pull request is being created if it doesn't exist yet, anyone relevant can test/validate/codereview
- The story owner will finally accept the pull request
- This will merge the pull request back into master (trunk)