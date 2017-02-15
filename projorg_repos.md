## Project Organization Repositories

In a **project/company** organization \("projorg"\) following repositories can exist:

* **home** repository \(home\)
* **Project** repositories \(proj\__...\)_
* **Organization** repositories \(org\_...\)
* **Product** repositories \(prod\_...\)
* **Cockpit** repositories \(cockpit\__..._\)
* **Websites** \(www\) repositories \(optional\) \(www\_...\)

Below each of the "projorg" repositories is discussed.

### Home repository

* Only one per projorg organization
* Always named `home`
* Starting point for people to find their way in all other repos in the projorg
* Types of issues in home repos:
  * Issues of type Question and Task
    * Used for questions and tasks that are relevant to the whole product organization
    * All other questions ans tasks should be created as issues in the repository the question or task relates too
  * Question for questions not related to one specific other repository
  * Overall 
* Example:
  * [https://docs.greenitglobe.com/gig/home](https://docs.greenitglobe.com/gig/home)

### Project repositories

* Always named as `proj_$customer` or `proj_$customer_$projname`
  * Projects relate to customers or specific projects \(so not linked to a team\)
  * We use this to organize our work related
    * to 1 customer, only useful if customer project is large enough
    * to specific projects inside an organization if they are not linked to 1 group of people
  * Do not create specific `proj_$customer_$projname` unless if subproject is large enough
* Milestones
  * defines a deadline for the project, there can be multiple but tasks or stories can only belong to one
  * freely chosen per project
* Types of issues in project repos:
  * Story, Lead, Ticket, Monitoring, Question or Task
* DO NOT USE STORIES FOR
  * feature requests or bugs
* Owned by project owner \(sometimes called project manager\)

### Organization repositories

* Always named as `org_$name`
* These are repo's which are specific to a group of people
  * group of people can be
    * for development eg. a scrump team: naming convention org\_devel\_cairo1
* Suggested standard organization repos:
  * org\_development \(engineering\)
  * org\_support \(all support requests \(tickets\) which are not in project repo yet\)
  * org\_internalit \(internal IT & organization of company\)
  * org\_product \(product management\)
  * org\_marketing
  * org\_finance
  * org\_legal
  * org\_hr
  * org\_quality \(all QA related issues, automation code, performance testing, portal testing and automated tests\)
* Milestones
  * Defines a deadline \(date\) for the projects, there can be multiple, but tasks or stories can only belong to one
  * Freely chosen per project
* Types of issues in organization repos:
  * Story, Lead, Ticket, Monitoring, Question or Task
* Examples:
  * org product mgmt \([https://docs.greenitglobe.com/gig/org\\_products\](https://docs.greenitglobe.com/gig/org\_products\)\)
* Owned by person who owns the organization e.g. marketing manager, ...

### Product repositories

* Always named as prod`_$name`
* REMARK: is not part of product organization repo's, this is the commercial side of the business, belongs to a product manager
* Is product management / integration information.
* e.g.
  * how does the product relate to the component repo's \(underneath the product organization repo's\)
  * naming conventions
  * roadmaps \(customer facing\)
  * integration \(AYS templates\)

### Environment repositories

* Always named as `env_$customername_$environmentname`
  * We use the following convention for `$environmentname`: `$countrycode - $G8type - $environmentnumber`
  * `$G8type` can be one of the following:
    * **scale** = for scaleout environments \(separate CPU 1U nodes \(1 motherboard per server\) which are scale able, storage and CPU all in one unit\)
    * **conv** = converged environment \(multiple nodes in one system eg. 4+ nodes in one physical box with shared backplane. Storage + multiple CPU nodes in one box\)
    * **stor** = for environments which are using +2 storage nodes with a minimum CPU config \(5 nodes\)
    * **G8** = for our G8 configs \(CPU + separate storage on 70 disk nodes\)
  * Examples:
    * `env_leal_mu_g8_1`
    * `env_gig_be_scale_1`
* Milestones
  * Defines the deadline \(date\) for the environment to be operational
* Freely chosen per project
* Types of issues in environment repos:
  * Monitoring, Question or Task \(auto-created\)
* If testing e.g. on an environment and issues are found create ticket\_ issues on this repo.
* There can be an ays repo inside \(info about the environment, even multiple version of ays repo's\)
* 
### Cockpit repositories

* Always named as `cockpit_$customername_$purpose`
  * $customername = the reseller of the operator capacity, or "gig" for internal use
  * $purpose = a short useful name which describes the cockpit function, e.g.:
    * `git` for our internal gitrobot
    * `resell` if it is cockpit for a reseller
    * `demo` if it is a Cockpit for demo purposes
  * Examples:
    * `cockpit_combell_resell`
    * `cockpit_gig_moehaha-demo`
* Used to deploy an infrastructure from out of GIT
  * Documents a full IT environment
  * Has all required process information embedded in AYS service instances
  * All changes are strictly controlled by GIT with pull requests
* Is the cockpit environment which runs our management framework, e.g.
  * AYS robot
  * Telegram Chatbot
  * Rogerthat Chatbot
  * Portal
* Can be used to manage X nr of G8 environment
  * Can also checkout an env\_... repo and the AYS info is in the env repo \(see above\)
* AYS repositories are inside
  * There can be more than one AYS repository hosted inside a Cockpit repo
    * Hosts the AYS service recipes and AYS service instances which make up the environment to be managed
    * Is a directory which has an empty file .ays inside
* Milestones
  * Defines a deadline for the environment, freely to be chosen
* Types of issues can be of type
  * Story, Task, Bug, Feature, Question, Monitor or Test, CustomerCase, Issue



