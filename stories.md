## Stories are the Start of All

Stories help us to organize our work. They need to comply to certain requirements to be effective though.
  
A story normally represents the view of a person, e.g. "I as product owner for product X would like to see Y features to be implemented because... customer Z needs this... our strategy is..."


### Properties of a good story

- Well chosen name
- Clear description of what we want to achieve
- Priority set a label:
 - Critical
 - Urgent
 - Normal
 - Minor
- Milestone: is a label, linking the story to a specific release date, shared with other stories
- Assignee: is the [story card owner](roles.md)
- Estimnation of the effort in days or hours
- Estimated Time of Arrival (ETA) is **daily** reviewed estimation of a spefic date when work will be finished
- Clear set of requirements or link to another document in the same repository listing and describing all requirements
- Clear set of acceptance tests or link to another document in the same repository which has the acceptance tests detailed
- Links (URLs) in same repo to
  - Specifications
  - Product Requirements Document (PRF) if relevant
  - Features or bugs which are related to the story
- Format:
	- Title: ```Story title``` (```Story name```)
	- The story name is used as reference in [Tasks](./tickets_tasks.md) related to the story


### Stories can constantly be re-prioritized

![](http://agilemodeling.com/images/requirementsManagement.gif)


### Story format

#### Title: ```$storyDescription ($storyname)```

#### Body

```
## GOAL:

Clearly describe what needs to be achieved.

## DESCRIPTION

Describe what story is about.

## LINKS:

- Tasks: link to a Kanban board, using waffle.io, see [example here](https://waffle.io/gig-projects/org_development?search=js8beta:&label=type_task)
- Specs: link to the Markdown page holding the specifications for the story
- Repositories involved:
 - list of links to all involved repositories

## REQUIREMENTS:

- List all requirements

## REMARKS:

- List all remarks

##ESTIMATION: 

- ESTIMATION: [```number of hours```(h)|```number of days```(d)] optional inidication of number of agreegated mandays/hours needed to realize the goal and only set by the story card owner
- ETA: specific date inidicating when goal will be achieved, this estimation needs to be reviewed and updated every day while work is in progress
```

Example: [see here](https://github.com/Incubaid/dev_process/issues/21)


### When does a story card go into validation stage?

- For stories related to projects or customers:
	- When work or subproject is done and is ready for validation 
- For storries related to code: 
	- When code done
	- When autotests (if relevant) are created
	- When all documentation relevant to the story is done
		- Do not forget to document how to test the story card
		- Do not forget to document on how to install/build everything related with the story card 
	- When all tests are done
	
	
### When is a story card complete (closed)

- When validation was done by story card owner and other stakeholders
- Result should be that everyone is able to install and test the code/work relevant to the story, and this just by reading the story card 


### What are the duties of a story owner

- Format of story is fully compliant
- Content of story is properly done (description, requirements, ...)
	- Requirements are clear
	- All involved people understand the story properly
- Communicate around your story to all stakeholders at least every other day
	- How far are we
	- What are the blockers
	- What is planned now
	- Do this by commenting on story card
- Escalate to stakeholders when
	- Story has delay
	- There are questions
	- Do this by comments and also use relevant (e.g. Telegram) communication group to escalate to appropriate people
- In case of code:
	- Code is complete 
		- Features are in line with requirements
	- Tests are good enough
	- Good documentation that can be understood also by someone who did not work on the story
	- On validation phase the pull request is properly merged in (after validation of course)
	- Code can easily be build and installed by anyone
	- Everyone relevant understands story is done and declare victory!


### Use of Incubaid GitHub development tools

Our tools will automatically find the tasks and embed them in the story so it's very easy for people to follow what the linked tasks are and how far we are from completion.