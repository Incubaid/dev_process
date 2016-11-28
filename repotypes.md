
### different types of repo's (IMPORTANT)

#### all repo's have the following labels in common

- labels in common
  - priority related: critical, urgent, normal, minor
  - process related: duplicate , wontfix
  - state related: new, accepted,question, inprogress, verification, closed

#### home repo

- is a repo with as name ```home```, there can only be 1 per account
- it is the main repo of an organization
- it holds 
  - starting point of documentation
  - explains what other repo's are used & what their purpose is
  - holds the stories (goes over multiple repo's)
  - holds the tasks which are not related to 1 repo
  - holds specifications which are not related to 1 repo
  - holds info like product PRD, ... which are bigger than 1 repo
- milestones
  - defines a deadline for x nr of stories/tasks
  - a story or task can only belong to 1 deadline
- label: types
  - story, question, task, feature
- typename in blueprints: 'home'

#### product code related

- no special convention today, can be any name but NOT starting with the prefixes as described in next sections
- this is where the main code of products live
- milestones
  - defines sets of bugs, features or questions which need to be delivered in a certain time interval (a deadline)
- label: types
  - question, task, feature, bug
- typename in blueprints: 'code'

#### project related

- ```proj_$customer``` or ```proj_$customer_$projname```
  - projects relate to customers
  - we use this to organize our work related to 1 customer project, only useful if customer project is large enough
  - issues are used as tickets, monitoring issues, stories or tasks
- milestones
  - defines a deadline for the project, there can be multiple but tasks or stories can only belong to one
- choice to have 1 repo for all customer projects or more
- types
  - story, question, task, feature
- typename in blueprints: 'proj'


#### ays template related (At Your Service)

- are templates for ays
- we have them in 2 version ays7 & ays8
- types
  - story, question, task, feature
- typename in blueprints: 'ays7' , 'ays'  (no need to specify 8)

#### IT infrastructure environments managed by ays (COCKPITS)

- at your service is a concept of managing IT infrastructure from out of GIT
  - it documents a full it env
  - it has all required process information embedded in ays
  - all changes are strictly controlled by git & pull requests 
- an AYS repo starts with ays_ ...
  - ```ays_$customer_$envname``` e.g. ays_gig_gentTest1
- milestones
  - defines a deadline for the environment, there can be multiple but tasks or stories can only belong to one milestone
- types
  - story, question, task, feature, ticket, bug, monitor
- typename in blueprints: 'cockpit'

#### documentation/gitbook

- ```doc_$name```
- milestones
  - defines a deadline for the documentation/book 
- IMPORTANT
  - often it makes more sense to leave the documenation inside the product/code repo
  - when put in code repo put under subdir /doc
  - advantage to keep it in a code repo is that documentation is lined to the code
  - the only reason to put it in a separate repo is when the doc is not related to code or related to more than 1 code repo  
- types
  - story, question, task, feature, bug
- typename in blueprints: 'doc'

#### websites

- ```www_name```
  - all content for websites
  - normally we use hugo & caddy to host these websites
- milestones
  - defines a deadline for the project, there can be multiple but tasks or stories can only belong to one
- types
  - story, question, task, feature, bug
- typename in blueprints: 'www'



