## Tickets, Tasks, Bugs & Feature Requests

### What is what

- Ticket
    - An issue raised by a customer or internal employee
    - Escalates issues like downtime, performance degradation, question, ...
    - Tickets are put on project repo's or support repo
 
- Bug
    - Issue of product
    - Only raised by support person or developer (gig or external if opensource)
    - If customers see a bug they normally will create a ticket first and the support person will create a bug and follow up
    - Is done on the code repository
    - If someone tumbles upon a blocking bug, the link to the issue needs to posted to the Bug Assesment Meeting (BAM) Telegram group so that the whole organization does not have to wait to the next BAM meeting for the assessment of the blokker
    
- Feature request (FR)
    - Raised by developers or anyone having interest in the code base (is done on the code repository), these feature requests are funneled and prioritized before they become story cards

- Tasks
    - Only used on ```org_repo's``` or ```proj_repo's```!
    - The tasks are linked to the subject for which the task is (not the projecy where people belong too)
        - E.g. if our legal council needs to help on a contract in ```proj_mauritius``` then the task is in ```proj_mauritius``` NOT in ```org_legal```


### Task format:

#### Title: ```$storyname:$taskDescription [4h]```

- Time format is optional
- Can be in h or days e.g. 4h or 4d 
- E.g.: ```storyx:cleanup the text for button something [1h]```
- E.g.: ```storyx:complete the autotest nr ... [1d]```

	
### Body:

```
## GOAL:

- Clearly describe the goal what needs to be achieved when the task is delivered.
- Often optional !!! and defined at story card level

## DESCRIPTION

- describe what task is about

## REQUIREMENTS

- Add specifications, remarks, implementation hints, requirements
- This is often optional, and defined at story card level 

**ESTIMATION**: [```number of hours```(h)|```number of days```(d)] 

```

- Goal is optional, often they are put at story card level
- Requirements are optional, normally they are put at story card level
- Estimation is optional
- Each task is linked to 1 owner who is responsible for putting the hours right

Example: [link](https://github.com/Incubaid/dev_process/issues/20)