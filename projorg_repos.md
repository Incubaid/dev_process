## Project Organization Repositories

In a **project** organization ("projorg") following repositories can exist:

- **home** repository
- **Organization** repositories
- **Project** repositories
- **Environment** repositories
- **Cockpit** repositories

Below each of the "projorg" repositories is discussed.


### Home repository

- Only one per projorg organization
- Always named ```home```
- Starting point for people to find their way in all other repos in the projorg
- Types of issues in home repos:
  - Issues of type Question and Task
    - Used for questions and tasks that are relevant to the whole product organization
    - All other questions ans tasks should be created as issues in the repository the question or task relates too
  - Question for questions not related to one specific other repoistory
- Following documents need to be included:
  - **README.md** (```$homerepo/Readme.md```)
    - Link to all documents mentioned below 
  - **terminology.md** document (```$homerepo/terminology.md```)
    - Defining all relevant terms related to your products 
  - **components.md** document (```$homerepo/components.md```)
    - Defining the components which make up the products
    - Describing what these components do
    - Links to relevant code repositories
  - **roadmap.md**
    - See the [Roadmap](roadmap.md) section 
- Example:
  - https://github.com/gig-projects/home


### Organization repositories

- Always named as ```org_$name```
- Suggested standard organization repos:
    - org_development (engineering)
    - org_support (all support requests (tickets) which are not in project repo yet)
    - org_internalit (internal IT & organization of company)
    - org_product (product management)
    - org_marketing
    - org_finance
    - org_legal
    - org_hr 
    - org_quality (all QA related issues, automation code, performance testing, portal testing and automated tests)
- Milestones
  - Defines a deadline (date) for the projects, there can be multiple, but tasks or stories can only belong to one
  - Freely chosen per project
- Types of issues in organization repos:
  - Story, Lead, Ticket, Monitoring, Question or Task
- Examples:
  - org_marketing (https://github.com/gig-projects/org_marketing)
  - org_development (https://github.com/gig-projects/org_development)


### Project repositories

- Always named as ```proj_$customer``` or ```proj_$customer_$projname```
  - Projects relate to customers
  - We use this to organize our work related to 1 customer, only useful if customer project is large enough
  - Do not create specific ```proj_$customer_$projname``` unless if subproject is large enough
- Milestones
  - defines a deadline for the project, there can be multiple but tasks or stories can only belong to one
  - freely chosen per project
- Types of issues in project repos:
  - Story, Lead, Ticket, Monitoring, Question or Task


### Environment repositories

- Always named as `env_$customername_$environmentname`
  - We use the following convention for `$environmentname`: `$countrycode - $G8type - $environmentnumber`
  - `$G8type` can be one of the following:
    - **scale** = for scaleout environments (separate CPU 1U nodes (1 motherboard per server) which are scale able, storage and CPU all in one unit)
    - **conv** = converged environment (multiple nodes in one system eg. 4+ nodes in one physical box with shared backplane. Storage + multiple CPU nodes in one box)
    - **stor** = for environments which are using +2 storage nodes with a minimum CPU config (5 nodes)
    - **G8** = for our G8 configs (CPU + separate storage on 70 disk nodes)
  - Examples:
    - `env_leal_mu_g8_1`
    - `env_gig_be_scale_1`
- Milestones
  - Defines the deadline (date) for the environment to be operational
- Freely chosen per project
- Types of issues in environment repos:
  - Monitoring, Question or Task (auto-created)
  

### Cockpit repositories

- Always named as `cockpit_$customername_$purpose`
  - $customername = the reseller of the operator capacity, or "gig" for internal use
  - $purpose = a short useful name which describes the cockpit function, e.g.:
    - `git` for our internal gitrobot
    - `resell` if it is cockpit for a reseller
    - `demo` if it is a Cockpit for demo purposes
  - Examples:
    - `cockpit_combell_resell`
    - `cockpit_gig_moehaha-demo`
- Used to deploy an infrastructure from out of GitHub
  - Documents a full IT enveronment
  - Has all required process information embedded in AYS service instances
  - All changes are strictly controlled by GitHub with pull requests 
- Is the cockpit environment which runs our management framework, e.g.
    - AYS robot
    - Telegram Chatbot
    - Rogerthat Chatbot
    - Portal
- Used to manage a G8 environment
- AYS repositories are inside
    - There can be more than one AYS repository hosted inside a Cockpit repo 
        - Hosts the AYS service recipes and AYS service instances which make up the environment to be managed
        - Is a directory which has an empty file .ays inside
- Milestones
  - Defines a deadline for the environment, freely to be chosen
- Types of issues can be of type
  - Story, Task, Bug, Feature, Question, Monitor or Test