## labels

### type

- to define type of issue
- 1 needs to be used (and only 1) !!!

| name | description | used in repo's| color |
| -- | -- | -- | -- |
| story |  | home, proj, cockpit, doc, www | todo |
| task |  | home, code, proj, ays, cockpit, doc, www | todo |
| ticket | type | proj, cockpit | todo |
| bug | issue reported by anyone | code, ays, cockpit, doc, www | todo |
| feature | improvement asked for by anyone | home, code, proj, ays, doc, cockpit, www | todo |
| question | anyone wants to ask something | home, code, proj, ays, doc, cockpit, www | todo |
| monitor | monitoring system found an issue | proj, cockpit, www | todo |
| unknown | unknown | home, code, proj, ays, doc, cockpit, www | todo |

### priority

- define priority in which issue needs to resolved
- 1 needs to be used (and only 1) !!!

| name | description | used in repo's | color |
| -- | -- | -- | -- |
| critical |  | ALL | todo |
| urgent |  | ALL | todo |
| normal |  | ALL | todo |
| minor |  | ALL | todo |

### process 

- define 2 optional process related labels

| name | description | used in repo's | color |
| -- | -- | -- | -- |
| duplicate |  | ALL | todo |
| wontfix |  | ALL | todo |

### state

- define state of issue in the kanban flow
- 1 needs to be used (and only 1) !!!
- REMARK
  - these states need to be useful over all projs e.g. over customer projs, code projs, stories, ...
  - good filters should be used in waffle to represent a kanban well 

| name | description | used in repo's | color |
| -- | -- | -- | -- |
| new | new or issue in backlog | ALL | todo |
| accepted | accepted in milestone & now tracked in kanban as to be done | ALL | todo |
| question | needs input | ALL | todo |
| inprogress | people are working on it | ALL | todo |
| verification | testing, verification with customer | ALL | todo |
| closed | nothing to do, 100% done | ALL | todo |
