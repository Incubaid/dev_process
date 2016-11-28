## Coding Cycle

### Step 1: story

- story needs to be defined
- first requirements done

### Step 2: branch

- work on branch with as name the story card short name (WHICH NEEDS TO BE UNIQUE PER STORY CARD)
- this can go over multiple repo's if have to
- NEVER WORN ON MASTER !!!!!!!!

### Step 3: code

- work on your code in iterative steps
- this can be done by multiple people

### Step 4: test / codereviews

- create pull request for codereviews if it doesn't exist yet
	- only 1 pull request per story (is 1 branch) per repo
- anyone, tester or developer can test this branch in a production env, which means testing infrasturcture needs to be setup to allow easy tests & building from any branch or set of branches
- this needs to be part of coding, go back to step 3 for many iterations !!!!

### Step 4b: someone needs your code

- if other story needs your code, intermediate pull requests can be created & validated & merged in on the other branch or master (careful) !!!
- best to avoid step 4B if not required, normally it means your story was too big and should have been cut in multiple pieces.

### Step 5: validate

- the code normally should be tested already by step 3 & 4
- now the story is put on validate state
- a pull request is being created if it doesn't exist yet, anyone relevant can test/validate/codereview
- the story owner will finally accept the pull request
- this will merge the pull request back into master (trunk)




