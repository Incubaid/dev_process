## GitHub Organizations \(gitorg\)

![](Screen Shot 2016-06-05 at 3.26.51 PM.png)

We define 2 types of organizations:

* Product organizations \("prodorg"\)
* Project organizations \("projorg"\)

Whatever we describe can be used on github as well as on similar tools like Gogs.

### Product organizations

* Groups repositories related to the development of a product
* Typically code repositories or the home repository
* Examples:
  * [https://github.com/jumpscale](https://github.com/jumpscale)
  * [https://github.com/openvstorage](https://github.com/openvstorage)
  * [https://github.com/0-complexity](https://github.com/0-complexity)
  * [https://github.com/incubaid](https://github.com/incubaid)

Details in the section about [product organization repositories](prodorg_repos.md)

**Are always in Github.**

### Project/Company organizations

* Groups repositories related to the management of projects, customers or sales
* Gogs is an amazing tool to support all kinds of processes, next to just software developement processes
* There is no code in a project organization
* Examples:
  * [https://github.com/gig-projects/](https://github.com/gig-projects/)

Details in the section about [project organization repositories](projorg_repos.md)

**Are always in GOGS**

### Gogs versus Github

* We suggest you use Github for all product related repositories, especially when you work with opensource software. Github is today by far the leading git management tool for these types of projects.

* We suggest you use Gogs for all project organizations, because these repo's need to be private and security is more important. We have forked a version of Gogs which integrates with itsyou.online, this allows you to have very good security & single sign on \(IYO\).



