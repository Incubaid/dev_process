# Incubaid Agile Development Process

[Incubaid](http://www.incubaid.com) is a Belgian startup incubator with a proven track record of bringing innovative and exciting cloud infrastructure products to market.

The goal of this ebook is to describe a set of conventions on how a development process can work based on agile methodologies.

These ideas are opinionated but do result out of years trying to create good products and still maintain flexibility.

We invite everyone to contribute to this set of documents.

* https://github.com/Incubaid/dev_process

Please use the issue tracker to ask questions, post feedback, ask for improvements, report bugs, ...

* https://github.com/Incubaid/dev_process/issues


## Agile

- We are strong advocates of [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development) processes like [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development) and [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)
- We believe the best process uses ideas from both


## Book

- [PDF version](https://github.com/Incubaid/dev_process/releases)

## To build & edit yourself

- checkout this repository (git)
- install nodejs: https://nodejs.org/en/download/
- install gitbook

```
sudo npm install gitbook-cli -g
```

- go to the downloaded repo and do

```
sudo gitbook install
gitbook serve
```

- you can also install the editor: https://www.gitbook.com/editor

to build the website to html

```
gitbook build .
```

to generate pdf's

install https://calibre-ebook.com/download

```
export PATH=/Applications/calibre.app/Contents/MacOS:$PATH
gitbook pdf .
```
