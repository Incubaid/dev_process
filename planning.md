## planning

This section describes who in general we plan our work.

### product related

#### step 0: prepare

- per company there is an organization (on github)
- there is a home repo in which we can document stories, generic specs, docs, ...
- each product repo has a code repo
- all the labels are well set in all repo's following our [label specs](labels.md)


#### step 1: roadmap / strategic planning

- in home repo
  - Readme.md  (```$homerepo/Readme.md```)
    - link to docs mentioned below 
  - create terminology doc  (```$homerepo/terminology.md```)
    - define all relevant terms to do with your products 
  - create components doc  (```$homerepo/components.md```)
    - define the components which make up the product
    - what do these components do
    - link to relevant code repo's
  - create roadmap doc  (```$homerepo/roadmap.md```)
    - define a planning & link to milestones
    - each milestone is linked to X nr of components & stories
    - stories are linked to the milestone on this repo
 
- setup communication
  - create milestone groups on telegram
    - make sure right people have access to it   
    - all relevant stakeholders & story card owners
  
- milestone pages
  - (```$homerepo/milestone_$name.md```)
  - describe the goal & deadline of this milestone
  - describe story card owners (optional)
  - there is a link to the issues filtered on appropriate milestone 
    - lists the stories which belong to this milestone 
  - each milestone is linked to telegram group: ```milestone_$shortcompanyname_$shortMilestoneName```, put this link
  - choose a milestone owner
  - make sure its clear that a milestone is active or not !!!

#### step 2: story card preparation

- is an ongoing process
- create all story cards relevant for 1 or more milestones
- choose the story card owners wisely
- for each story card there can be a telegram group (optional)
  - ```story_$shortcompanyname_$shortStoryName```
  - link to this group

#### step 3: stakeholder meeting (see [meetings doc](meetings.md))

- call stakeholder meeting to discuss milestone(s)
  - use telegram group: ```milestone_$shortcompanyname_$name``` to announce
- when approved, announce over telegram
- when not approved do more of these meetings, go back to step 2 when required


#### step 4: milestone meeting (see [meetings doc](meetings.md))

- present milestone & related story cards to everyone involved in the organization
- this is the official start of getting this milestone done

#### step 5: story group meetings (see [meetings doc](meetings.md))

- the story owners organize meetings to discuss progress
- happens every day, needs to be very short < 15 min
- use telegram group: ```milestone_$shortcompanyname_$name``` to coordinate
- use ```story_$shortcompanyname_$shortStoryName``` to communicate specifically about 1 story when this becomes relevant (is optional)

#### step 6: demo meeting (see [meetings doc](meetings.md))

- give demo's about what has been accomplished
- use telegram group: ```milestone_$shortcompanyname_$name```

#### step 7: milestone acceptance meeting (see [meetings doc](meetings.md))

- discuss how the milestone went, learn for future
- use telegram group: ```milestone_$shortcompanyname_$name```








