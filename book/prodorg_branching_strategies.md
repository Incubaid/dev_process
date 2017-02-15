##  Code Organization Branching Strategies

### Strategy:

```
  [hotfix]                      [master]                            [version]                             [issue]
                                   |
                                   |
                                   |   (start working on new version)
                                   |----------------------------------->|
                                   |                                    |  (start working on an issue)
                                   |                                    |----------------------------------->|
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    | (feature is tested,                |
                                   |                                    |       documented and code reviewed)|
                                   |                                    |     (Pull request created)         |
                                   |                                    |<-----------------------------------|
                                   |                                    |                                    x
                                   |                                    |                         (branch gets deleted)
                                   |                                    |
                                   |                                    |
                                   |                                    |
                                   |                                    |  (start working on an issue)
                                   |                                    |----------------------------------->|
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    |                                    |
                                   |                                    | (feature is tested,                |
                                   |                                    |       documented and code reviewed)|
                                   |                                    |     (Pull request created)         |
                                   |                                    |<-----------------------------------|
                                   |                                    |                                    x
                                   |                                    |                         (branch gets deleted)
                                   |(All release features and bugs      |
                                   |   are done. QA sign off on release)|
                                   |<-----------------------------------|
                                   |   (Tag merge with release)
                                   |
                                   |
                                   |   (start working on new version)
                                   |----------------------------------->|
                                   |                                    |
        (bug detected!             |                                    |
             hotfix required)      |                                    |
     |<----------------------------|                                    |
     |                             |                                    |
     |                             |                                    |
     |                             |                                    |
     |                             |                                    |
     |---------------------------->|                                    |
     x                             |  (hotfix cherry-picked to version) |
  (branch gets deleted)            |----------------------------------->|
                                   |                                    |
                                   |                                    |
                                   |                                    v
                                   |
                                   v
 ```


 ### Branches:
  - **Master branch**
     - Would always have the latest production version
     - Would always be stable
  - **Version branch (name: version number. e.g.: 8.1.0)**
     - Branches off of master
     - QA will be validating against it
     - Will contain all issues (bugs and Feature Requests) product owner has accepted into this version
     - Gets merged back into master and tagged as "v<version number>"
  - **Issue branch (name: issue number. e.g.: 666)**:
     - Issue can be a feature request or a bug
     - Contains only work relevant to issue
     - Must be rebased from _version branch_ each day
     - Pull Request is created when branch is done.
     - Branch is deemed done when:
        - bug is fixed/FR is complete according to specs
        - documented (when applicable)
        - tests written (when applicable)
  - **Hotfix branch (name: hotfix__version)**
    - Branches off of version tag
    - Addresses a blocking issue
    - Cherry-picked into version branches
    - Merged into master (after review)
