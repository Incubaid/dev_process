# The Ideas
All projects within Incubaid are using a stable trunk based development model. This mean that the master branch, the trunk, is always working (stable) and up to date with the latest code.

New features (stories) are developed and bugs are fixed on separate branches, story-branches.  When they are “done”  (developed, tested, documented), the story-branch is merged back to the trunk. Work is NOT “done” if it is not on trunk.

Next to story-branches  there are release-branches. Only cherry-picks FROM trunk TO the release-branch are supported. The cherry-picks should be almost exclusively bug fixes. New features can be added only after the approval of the necessary stakeholders.

Continuous Integration (CI) tests are running against the trunk and in case something breaks, the issue gets resolved asap.

It is an obligation for developers not to break the build with any commit. This requires a lot of discipline. Rollback/revert of a commit is a strategy to prevent the damage (lost time) from breaking the trunk.