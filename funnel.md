## Bugs & Feature Requests Funnel

IN: BUGS - FEATURES ->

![](http://www.rocketwatcher.com/wp-content/uploads/2011/01/Funnel-mod.jpg)

OUT: STORIES

### Principles

- The idea is that in a code repo you log all the bugs and feature requests
- Anyone can report bugs or feature requests
- The [product owner](roles.md) will sort through the issues and give them priorities (using labels)
- The bugs or feature request are grouped and planned to be executed (attached to milestones)
- There can be lots of milestones in a code repo, these milestones are used to link X number of bugs/FR's to a story in the milestone repo, see milestone section to understand purpose


### DO NOT

- Plan work directly on feature request or bugs, this results in very bad planning
  - There is a shortcut to create tasks automatically though, see below 


### WHY

- This forces product owners to think about organizing work and priorities


### How to automate task creation

- If you put $storycardname: at a prefix to the title of the issue then this bug/FR will automatically become a task underneath the story
- This only works if $storycardname is unique (which has to be for active stories)
- This is done by the Incubaid development process tools