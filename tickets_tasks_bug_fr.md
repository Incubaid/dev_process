## Tickets, Tasks, Bugs & Feature Requests

### What is what

* Ticket: new suggested types: customercase/issue

  * An issue raised by a customer or internal employee
  * Escalates issues like downtime, performance degradation, question, ...
  * Tickets are put on project repo's or support repo

* Bug

  * Issue of product
  * Only raised by support person or developer \(gig or external if opensource\)
  * If customers see a bug they normally will create a ticket first and the support person will create a bug and follow up
  * Is done on the code repository
  * If someone tumbles upon a blocking bug, the link to the issue needs to posted to the Bug Assesment Meeting \(BAM\) Telegram group so that the whole organization does not have to wait to the next BAM meeting for the assessment of the blokker

* Feature request \(FR\)

  * Raised by developers or anyone having interest in the code base \(is done on the code repository\), these feature requests are funneled and prioritized before they become story cards

* Tasks

  * Only used on `org_repo's` or `proj_repo's`!
  * The tasks are linked to the subject for which the task is \(not the projecy where people belong too\)
    * E.g. if our legal council needs to help on a contract in `proj_mauritius` then the task is in `proj_mauritius` NOT in `org_legal`

### Bug/FR format:

#### Title: `$storyname:$taskDescription [4h]` or `$taskDescription [4h]`

* Time format is optional
* Can be in h or days e.g. 4h or 4d
* E.g.: `storyx:cuisine start of postgresql does not work [1h]`

#### Body for Feature Request:

* requirements for FR or link to requirements in same repo
* define why this is important for you \(because you filed this FR\)
* define required deadlines if relevant
* optionally: link to acceptance criteria or specify them here
* link to specs if any in the same repo
* remarks
* optional: time estimate see [specs](specs.md)

#### Body for Bugs:

* screenshots if relevant
* on which environment this was seen
* link to logs if any
* remarks
* optional: time estimate see [specs](specs.md)

### Task format:

* IMPORTANT:
  * do not overuse tasks, this leads to abuse very quickly and is not really compatible with scrum or kanban
  * personally I would never use them and only put tasklists on story card level if you really feel the need for it
  * scrum is all about the story card owner having a good view on what the story is about and with gut feel & knowledge put best estimate in the title of remaining time \(gutfeel is much more reliable then trying to put tasks in\)
  * if you try to describe work by tasks its never correct and at least 50% error because tasks are never complete, in my personal optinion this simply does not work.
* DO NOT describe them too formal !!!!, needs to be a quick placeholder
* DO NOT Describe \(all this belongs to code repo\)
  * features
  * bugs
  * requirements
  * docs
  * remarks to do with product
* only content should be purely process driven

#### Title: `$storyname:$taskDescription [4h]`

* Time format is optional
* Can be in h or days e.g. 4h or 4d
* E.g.: `storyx:cleanup the text for button something [1h]`
* E.g.: `storyx:complete the autotest nr ... [1d]`

### Body:

* Each task is linked to 1 owner who executes the task
* Sometimes its useful that the owner of the task puts a time estimate e.g. \[1h\], this is always the remaining time going from now. This needs to be revisited often



