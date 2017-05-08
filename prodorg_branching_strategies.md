##  Product Organization Branching Strategies

### Strategy:

```
   [master]                            [feature]                             [hotfix]
     |
     |
     |   (start working on new feature)
     |----------------------------------->|
     |                                    |
     |                                    |
     | (feature is tested,                |
     |    documented and code reviewed)   |
     | (Pull request created)             |
     |                                    |
     |<-----------------------------------|
     |                                    x
     |                           (branch gets deleted)
     |
     |
     |  (start working on new feature)
     |----------------------------------->|
     |                                    |
     |                                    |
     |                                    |
     |                                    |
     |                                    |
     |    (feature is tested,             |
     |       documented and code reviewed)|
     |     (Pull request created)         |
     |<-----------------------------------|
     |                                    x
     |                         (branch gets deleted)
     |
     |
     |
     |(All release features and bugs
     |   are done. QA sign off on release)
     |
     *   (Tag current HEAD with release)
     |   (start working on new version)
     |
     |
     |
     |
     |
     |
     |
     |
     |
     |
     |       (Serious bug is discovered! Must be hotfixed)
     |----------------------------------------------------------------------->|
     |     (recreate branch from release tag)                                 |
     |                                                                        |
     |                                                                        |
     |                                                                        |
     |  (hotfixed. Merge back into master. use git describe to tag)           |
     *<---------------------------------------------------------------------- |
     |                                                                        x
     |                                                               (branch gets deleted)
     |
     |
     |
     |
     v
 ```


 ### Branches:
  - **Master branch**
     - Would have the latest development
     - Can be unstable
     - Will contain all issues (bugs and Feature Requests) product owner has accepted into this version
     - QA will be validating against it when development is complete
     - Once QA has signed off, gets tagged as "v<version number>"
  - **Feature branch (name: feature. e.g.: refactor_sal)**
     - Branches off of master
     - Gets merged back into master
     - can be a feature request or breaking code
     - Contains only work relevant to issue
     - Must be rebased from _master_ each day
     - Pull Request is created when work is done.
     - Work is deemed done when:
        - bug is fixed/FR is complete according to specs
        - documented (when applicable
        - tests written (when applicable)
  - **Hotfix branch (name: hotfix__version)**
    - Branches off of version tag
    - Addresses a blocking issue
    - `git-describe` will be used to call it v8.1.0-1-gcommithash
    - tag it
    - Cherry-pick into all branches that should have this applied to them


    *** In case of more than one concurrent version being developed, the later version is treated as feature until the previous version is released. The later version then gets merged into master as current development version
