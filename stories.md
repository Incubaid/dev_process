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
- Milestone: is a label, linking the story to a specific date e.g. nov_end (see [milestones](milestones.md))
- Assignee: is the [story card owner](roles.md)
- Estimation of the effort in days or hours (this needs to be redone on max 2 daily basis by story card owner)
    - only put this in title
- Links (URLs)  to
  - Specifications (in code repo)
  - QA acceptance criteria (code repo)
  - Product Requirements Document (PRD) if relevant (core repo or home repo in product org/account)
  - Features or bugs which are related to the story (code repo)
  - Kanban about releated FR/Bugs (using version=milestone or prefix in BUG/FR)
- Format:
	- Title: ```Story title``` [```time left e.g.4d```] (```Story name```)
	- The story name is used as reference in [Tasks](./tickets_tasks_bug_fr.md) related to the story


### Stories can constantly be re-prioritized

![](http://agilemodeling.com/images/requirementsManagement.gif)


### Story format

#### Title: ```$storyDescription [4d] ($storyname)```

- See [specs](specs.md) for definition time estimates.
- The time estimate is in title, this is the remaining time for this story
    - this is only set by the story card owner !!!
    - this needs to be set on max 2 daily basis !!!
    - time is working time (sum over all people)
    - this is an estimate this is not the sum of the times used inside the story or specs underneith

#### Body

see [specs](specs.md) for definition of task tables and time estimates.

```
## GOAL:

Clearly describe what needs to be achieved.

## DESCRIPTION

Describe what story is about.

## TASKS

- is an optional task table, see [specs](specs.md)
- i suggest not to use underlying tasks, you can but risk is high that people will use these tasks as feature requests or bugs, better just to use this table as a high level overview and as a way how to calculate how much needs to be done.

## LINKS:

- Tasks: link to a Kanban board, using waffle.io, see [example here](https://waffle.io/gig-projects/org_development?search=js8beta:&label=type_task)
- Specs: link to the Markdown page holding the specifications for the story (code repo)
- ...

## REQUIREMENTS:

- very high level overview and/or links to requirements (which are in code repo)
    - only the high level overview, the rest is in the code repo's

## REMARKS:

- List all remarks
```


### When does a story card go into validation stage?

- For stories related to projects or customers:
	- When work or subproject is done and is ready for validation

- For storries related to code:
	- When code done
	- When autotests (if relevant) are created
        - When autotests are already executed and succesful.
	- When all documentation relevant to the story is done
		- Do not forget to document how to test the story card
		- Do not forget to document on how to install/build everything related with the story card
	- When all tests are done


### When is a story card complete (closed)

- When validation was done by story card owner and other stakeholders
- Result should be that everyone is able to install and test the code/work relevant to the story, and this just by reading the story card


### Use of Incubaid GitHub development tools

Our tools will automatically find the tasks and embed them in the story so it's very easy for people to follow what the linked tasks are and how far we are from completion.

### Suggestions

- do not use documentation phase in kanban, documentation is a part executing on the story like any other task (specs, ...)
    - specs/documentation should 20% be done before you start with story and while doing story the specs/docs get completed
