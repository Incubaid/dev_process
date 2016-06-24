## Labels

### Type

- To define type of issue
- 1 needs to be used (and only 1)!

| Name | Description | Used in | 
| --- | --- | --- | --- |
| story |  | home, org, project | 
| task |  |  home, org, project |
| ticket | type | org, project |
| bug | issue reported by anyone | code, ays, doc, www, quality |
| feature | improvement asked for by anyone | code, project, ays, doc, www, cockpit, org |
| question | anyone wants to ask something | home, code, project, ays, doc, www, cockpit | 
| monitor | monitoring system found an issue | project, cockpit, www |
| lead | lead for sales, can convert in business | project, org |
| test | a test task | org, cockpit |


### Priority

- Define priority in which issue needs to resolved
- 1 needs to be used, and only 1!

| Name | Description | Used in |
| --- | --- | --- |
| critical |  | all |
| urgent |  | all |
| normal |  | all |
| minor |  | all |


### Process 

- Define 2 optional process related labels

| Name | Description | Used in |
| --- | --- | --- |
| duplicate |  | all |
| wontfix |  | all |


### State

- Define state of issue in the Kanban flow
- 1 needs to be used, and only 1!
- Remark
  - These states need to be useful over all projects, e.g. over customer projects, code projects, stories, ...
  - Good filters should be used in waffle to represent a Kanban well 

| Name | Description | Used in | 
| --- | --- | --- | 
| new | new or issue in backlog (is no label, is the default)| all |
| inprogress | people are working on it | all |
| question | needs input | all |
| verification | testing, verification with customer | all |
| closed | nothing to do, 100% done | all |




