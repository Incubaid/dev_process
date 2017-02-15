## Code Organization Repositories

In a **product** organization \("codedorg"\) following repositories can exist:

* **home** repository
* Source **code** repositories
* **AYS** repositories \(AYS templates, is not same as cockpit repo's\)
* **Websites** \(www\) repositories \(optional\)

Below each of the codedorg repositories is discussed.

### Home repository

* Only one per "codedorg"
* Always named `home`
* Is the main repo of a codedorg
  * Is owned by the product owner \(is not the product manager\).
  * Product owner needs to make sure its clear he owns this organization/account & is responsible of content
* It holds
  * Documentation common to the repos in the codedorg
  * Explains the purpose of all other repos in the codedorg
  * Starting point for people to find their way in all other repos in the codedorg
  * Can hold specifications and product requirements document \(PRD\) information common to the repos in the codedorg \(in other words if not linked to 1 specific repo\)
* Milestones
  * Are version numbers if they are relevant over all products in the account/organization \(if relevant\)
* Types of issues in the `home` repo:
  * Only issues of type Question \(type\_question\) and Feature Request \(type\_feature\)
    * Used for questions and feature requests that are relevant to the whole Code Organization
    * All other questions and feature requests should be asked in the repository the question relates too
* This is the ideal repo to define your roadmap covering multiple product and component repos in the codedorg

* Suggest to include following documents:

  * **README.md** \(`$homerepo/Readme.md`\)
    * Link to all documents mentioned below
    * Linkts to join related [telegram](telegram.md) groups
    * Is starting point for full account/organization
  * **terminology.md** document \(`$homerepo/terminology.md`\)
    * Defining all relevant terms related to your products
  * **components.md** document \(`$homerepo/components.md`\)
    * Defining the components which make up the products
    * Describing what these components do
    * Links to relevant code repositories
  * **roadmap.md**
    * See the [Roadmap](roadmap.md) section

DO NOT USE THIS REPO FOR:

* Escalating bugs
* Story cards

### Code repositories

* No specific naming convention
* Can have any name but NOT starting with the prefixes used by for other types of repositories, as described on this page
* This repo has following content \(this content should not be in any other repo type\)
  * all code
  * all specs
    * specs related to code is just next to code
    * generic specs are in /specs directory
  * all documentation \(put underneath /doc in repo\)
  * all feature requests \(by means of FR issues\)
  * all bug issues \(by means of bug issues\)
* Milestones
  * Are releases for a product and linked to a delivery time
* Types of issues in code repos:
  * Issues of type Bug, Feature and Question
  * DO NOT use stories or tests at this level!
  * Question: should we allow tasks at this level??? \#TODO \*1
* Bug/feature management
  * All reported issues or feature requests are grouped, it acts like a funnel
* How to easily make sure bugs and features are linked to a story.
  * Put unique story card name at beginning of title e.g. story1:...
  * The Incubaid development process tools will find the story and make sure that the information gets linked.

### www = websites repositories

* Always named as `www_$name`
* Contains the code for a website
* Is simular to a code repo but this case for a website.
* When code changes website is updated and hosted automatically
* Types of issues in website repos:
  * Issues of type Bug, Feature and Question
* We use tools like caddy/hugo to automatically publish a website

### AYS templates repositories

* Always named as `ays_$name`: examples
  * `ays_$customer_$envname`
  * `ays_gig_testenv_dubai1`
* Milestones
  * For grouping feature requests and bugs
* Types of issues in AYS template repos:
  * Issues of type Bug, Feature and Question
  * Should we allow tasks here???



