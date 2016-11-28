## 0-Bugs

Principle how to sort through bugs and keep the process as light as possible.

### [Blog article from VMware Israel team](http://galzellermayer.blogspot.ae/2013/05/0-bugs-policy.html)

**Blog from development team at VMware Israel**
(small mods to fit in our process)

How many bugs do you manage? 50? 200? 2000?

Maybe you cannot even tell what the exact number is, because it keeps changing.

I know exactly how many bugs we have in our product: zero.

How much time do you spend in bug triage meetings and on bug management (moving them around from version to version)?

I spend half an hour once a month. And I never see the same bug more than once.

Often, we wonder how should we handle bugs when working in scrum/agile?

The answer is 0 bugs policy. It is based on our experience in several of the Scrum teams in VMware Israel.

Other ways we tried failed, with 0 bugs policy it just works.

The following blog is a manifest that describes what is the 0 bugs policy and why it is the only way to go.

The 0 bugs policy is an advanced yet very simple process for handling bugs. 

Whenever you encounter a new bug, you should either fix that bug, or close it as "won't fix" and don't think about it again. That's it. Simple.

Now, let’s talk about why this is the only way to go.

Bugs can be generalized into 2 categories:

1. Bugs that were opened during the current iteration for user stories (features you are now implementing) - Fix them right away, otherwise the story/feature is not really DONE.
	- If this concept is not crystal clear, than this blog is not for you.

2. All the other bugs (regression, customer bugs, etc.). Non-sprint bugs.

- You can either fix them right away (or in the next sprint; Poteto potato).
- You can close them as "won't fix" - if the value of the fix does not worth the effort to fix it.
- You can defer the bug.

Let's talk about deferring the bug.  
Just DON'T. If you don't fix it right now, just close it. 

Why?

It will cost you more to fix it later... a lot more... tons more!

Because a sprint from now:

- You will not remember nor understand this bug as good as now. 
- The right environment - both for QA and for dev. – might not be available.
- The code might change and the behavior will be slightly different.
- 2-3 sprint from now (not to say the next release) you will not remember it at all and you will have to 
spend a lot of time understanding the bug and reproduce it.
- You will need to maintain the deferred bugs, either if they are managed in their own backlog or part of the main backlog. You will need to prioritize them, and that takes time.
- Also, it is annoying. Have you ever been part of a bug triage meeting? It’s a day-killer. Trust me.
- You will never – and this is a known secret – fix this bug. 
- It will be in your system forever. Why?
	-  If you have decided not to fix it now, it means you have more important things ahead. Features. Probably. Trust me. You will always have more features. Even in the next release (-;.
	-  As the time will go by, you will defer more and more bugs, and then this bug will have to compete both against new and cool features and also with new and not cool bugs. So, if you didn't fix it now, when you don't have all the other important bugs as well, why the hell do you think you would do it later?


OK. So we have agreed that the 0 bugs policy is in fact GREAT!

### Our conclusions

- Each product/code account has milestones defined = product versions
- Per code repo there are normally not more than 3 milestones
  - Version number 1 (nearest to today)
  - Version number 2 (next release)
  - Roadmap (always use this name!)
- **Bugs are NEVER put on roadmap**, following this page they are in version 1 or 2 after now.
- FR can be put on roadmap when not in one of 2 next releases, but no specific timing yet.