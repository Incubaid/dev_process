## Roles & Responsibilities

* The below roles need to be documented in the relevant proj or org repo's of a PROJORG \(GitHub Project organization\)
* It's basically describing who owns which role in the organization

### Scrum Team Lead

* Owns a team of people working on one or more stories
* Scrum Lead needs to make sure
  * People understand Scrum and our Agile principles
  * People are coached
  * People improve in their career
  * People are happy in their job and are motivated
  * Eliminate all blockers which people might experience
* Scrum leads are often also story owners \(of X nr of stories\)
* Scrum teams have their own repo: `org_development_$scrumTeamname`
* Scrum teams are well defined in `org_development` repo

### Project Owner

* Responsible for a `proj_$customer_$proj` or `proj_$company_$proj` repo

* Responsibility

  * Define milestones
  * Make sure the repo is clean
  * Verify / Check all stories as defined in repo \(guarantees quality, priorities, communication around it, ...\)
  * Work with product owners to make sure you get the features as required.
  * Organize project meetings \(see [Meetings](meetings.md) to be defined \#TODO: \*2\)

* There is only one project manager per repo

* in readme.md of repo there needs to be clear definition about project & owner & contact info

* They use their telegram group: `$company_proj_$customer_$proj`

### Product Owners

* Responsible for a github/gogs account/organization e.g. jumpscale

  * They use the home repo to define the structure in the account

* Important to structure the accounts/organizations well so they represent a product

* Responsibility

  * Define milestones=versions on the repo's, make sure they are consistent
  * Make sure the repos in the account/organization are clean
  * Make sure everyone using the repo's behave well
    * proper defined bugs/fr
    * proper branching
  * Work with Project Managers & other company stakeholders to make sure the repo structure is ok.
  * Organize product meetings \(PM\) \(see [Meetings](meetings.md)

* There can be more than 1 owner per repo, but try to only have 1.

* The home repo is important to organize the full account/organization.

* They use their telegram group: `$company_product_$name`

### Product Manager

* Owns product from a go2market/commercial/marketing perspective.
* Defines roadmap.
* Organizes stakeholder meetings.
* Owns one or more repo's \(prod\_...\) on gogs

### Story owners \(product related\)

* Main responsibilities:
  * Story card is developed in time
  * Story card is clear and understood by all required
  * Requirements for the card are met
  * Done means done! \(see [Agile Principles](agileprinciples.md)\)
  * Communicate to product owners about the card
  * Organize story meetup in order to talk with people contributing to the story, follow-up on progress
  * Define tasks that need to be delivered to deliver the story card

### What are the duties of a story owner

* Format of story is fully compliant
* Content of story is properly done \(description, requirements, ...\)
  * Requirements are clear
  * All involved people understand the story properly
* Be part of product meetings \(PM's\), give info:
  * How far are we
  * What are the blockers
  * What is planned now
  * Do this by commenting on story card
* Escalate to product owner\(s\) & Scrum Owner when
  * Story has delay
  * There are questions
  * Do this by comments and also use relevant \(e.g. Telegram\) communication group to escalate to appropriate people
* Guarantee Story gets done which means
  * Code is complete
    * Features are in line with requirements
  * Tests are good enough
  * Good documentation that can be understood also by someone who did not work on the story
  * On validation phase the pull request is properly merged in \(after validation of course\)
  * Code can easily be build and installed by anyone
  * Everyone relevant understands story is done and declare victory!

### Stakeholder

* Anybody who has something to loose or win by the acceptance/progress on a story card
* Stakeholder main responsibility is to be part of product stakeholder meeting \(PSM\)
* This is a very generic definition & can be quite broad.



