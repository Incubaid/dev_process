##  Product Organization Repositories

In a **product** organization ("prodorg") following repositories can exist:

- **home** repository
- Source **Code** repositories
- **Documentation** (GitBook) repositories
- **AtYourService (AYS) templates** repositories
- **Websites** (www) repositories

Below each of the prodorg repositories is discussed.


### Home repository

- Only one per prodorg
- Always named ```home```
- Is the main repo of a prodorg
- It holds 
  - Documentation common to the repos in the prodorg
  - Explains the purpose of all other repos in the prodorg
  - Starting point for people to find their way in all other repos in the prodorg
  - Holds specifications and product requirements document (PRD) information common to the repos in the prodorg
- Milestones
  - Are releases (no dates) for a product, used to group work for coding, testing, ...
- Types of issues in the ``home`` repo:
  - Only issues of type Question (type_question) and Feature Request (type_feature)
    - Used for questions and feature requests that are relevant to the whole product organization
    - All other questions and feature requests should be asked in the repository the question relates too 
- This is the ideal repo to define your roadmap covering multiple product and component repos in the prodorg

DO NOT USE THIS REPO FOR:
- Escalating bugs
- Story cards

  
### Code repositories

- No specific naming convention
- Can have any name but NOT starting with the prefixes used by for other types of repositories, as described on this page
- This is where most of the code of the products lives
- Milestones
  - Are releases for a product, used to group work for- issue types used
- Types of issues in code repos:
  - Issues of type Bug, Feature and Question
  - DO NOT use stories, tasks or tests at this level! 
- Bug/feature management
    - All reported issues or feature requests are grouped, it acts like a funnel    
- How to easily make sure bugs and features requests become tasks
  - Put unique story card name at beginning of title e.g. story1:...
  - The Incubaid development process tools will find the story, create a task for it and put this bug/feature request (fr) in as a task (in the task there will be link to this bug/fr) 


### Documentation (GitBook) repositories

- Always named as ```doc_$name```
- Often it makes more sense to leave the documentation inside the product/code repo
  - When put in a code repo, use a subdirectory ```/doc```
  - Advantage to keep it in a code repo is that documentation is linked to the code
- Possible good reasons to have the documentation separated from the code repositories
  - When the documentation is not related to code or related to more than one code repository  
- Milestones
  - For grouping features and bugs related the documentation
- Types of issues in documentation repos:
    - Issues of type Bug, Feature and Question
- Example:
    - https://github.com/0-complexity/doc_whmcs_reference_implementation
   

### www = websites repositories

- Always named as ```www_$name```
- Contains the code for a website
- When code changes website is updated and hosted automatically
- Types of issues in website repos:
    - Issues of type Bug, Feature and Question


### AYS templates (AtYourService)

- Always named as ```ays_$name```
  - ```ays_$customer_$envname``` e.g. ays_gig_gentTest1
- Milestones
  - For grouping feature requests and bugs
- Types of issues in AYS template repos:
    - Issues of type Bug, Feature and Question