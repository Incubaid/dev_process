## Meetings

### Organization/Project Stakeholders meeting

- Organized by organization owners (teamleads) or project managers
  - Can be a regular call e.g. once per week
  - He/she feels communication between stakeholders is required to meet the deadlines as defined
  - Update progress towards the deadline

- Who
    - manager of this organization or this project
    - all stakeholders who have something to lose or win by stories discussed on this meeting

- When
  - anytime when company priorities or deadlines need to be discussed

- Use waffle.io kanboard representation to see prio's

- Communicate using telegram in organization/project group
    - in ```$company_org_marketing```


### Product Demo meeting

- When 1 or more stories are ready do be demo'd then milestone owner or story card owner can decide to hold a demo meeting

- Who
  - Anyone who is interested to learn about progress made on a story card

- Goal
  - Show progress made
  - Demonstrate the story(ies) is(are) "DONE"
  - Show people the starting points so they can repeat it themselves

- Communicate using telegram in product group
    - in ```$company_org_product_...```

### Scrum meeting

Only relevant for product development.

- meeting done per scrum team
- daily basis
- max 15 min
- they go over all open stories (which is normally max 3 per any point in time)
- Each scrum team member:
  - What did I do since last meeting
  - What am I planning to work on
  - What is blocking me
  - What is remaining effort from my side for completion of this full story card
- Communicate using telegram in product group
  - in ```$company_org_development_$scrumTeamName```


### Product Meeting (PM)

Only relevant for product development.
- Is combination of product stakeholder meeting, story master & scrum meeting from before.

- Is done per product group (see [product management](productmgmt.md) )
    - example product groups
        - ovc / g8os / itsyou.online / oneapp / jumpscale
    - these product groups need to be defined in ```org_development``` repo in github/gogs
        - is important everyone understands which product groups there are
    - each product group needs to have a clear owner

- 3 goals
    - assess progress per product group and see if milestones will be met
    - discuss blocking items (critical path) in relation to progress (any blocking potential item)
    - assess blocking bugs (means do we break the current iteration and add some bug to be resolved now)

- When
    - 1-5 days, means daily for fast changing products where deadlines are close

- Who
    - all storycard masters which are linked to product group
    - each stakeholder who wants to be detailed involved in the specific product
    - once every month (at least once): more people are involved to attend the product meeting this to discuss and make sure

- Preparation
    - these meetings need to be well prepared to make them efficient, prepared by product owner

- Communication
    - Call for meetings on telegram channel, when info worth sharing about product group also use this
    - Telegram: ```$company_product_$shortnameOfProductGroup```
        - e.g. gig_product_ovc
        - e.g. gig_product_g8os
        - e.g. gig_product_js

- Use waffle.io kanboard representation to see prio's

### Product Stakeholders Meeting (PSM)

- normally happens over multiple product groups at once (sometimes can be 1)
- 2 goals:
    - assess how we did and if needed move stories to next milestone (stakeholder meeting)
    - as preparation on next milestone: define which stories need to go in which milestone (stakeholder meeting)

- When
    - decided in PM meeting, if they feel its needed to bring all stakeholders together
        - can be because of unforeseen delay, can be planning for next release
    - whenever org owner of company believes this is required

- Who
    - Everyone in company who has something to lose or win by delaying or prioritizing stories

- What this is not!!!
    - No discussions about content: FR/BUGS, Requirements, ... all of this needs to be properly prepared

- Principles
    - These meetings need to be super efficient.
        - Normally lots of people are on these meetings that is why its super important to keep them dense and short.
        - Preparation is done by product owners & in PM meetings, THIS NEEDS TO BE DONE WELL.
            - Don't call for a PSM if no proper preparation done
    - If story not well prepared, it gets skipped and needs to wait for next PSM.

- Communication
    - Telegram: ```$company_product_stakeholders```
    - There needs to be a PSM per product group, is ok to do more at once
