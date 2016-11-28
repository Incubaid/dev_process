## Tools

### WIKI/GITBOOK

- suggest to extensively use wiki in markdown format to write
  - stories
  - issues
  - specs
- you can use the amazing gitbook tool to convert the markdown docs to an ebook (see this one)


### gitbook editor

- https://www.gitbook.com/editor

### how to use gitbook toolchain locally

```
npm update -g
npm install gitbook-cli -g
npm install gitbook-plugin-mermaid2
npm install phantom
gitbook update
```

to serve local content
```
cd $directory_gitbook_md_files
gitbook install
gitbook serve
```

to create a pdf
```
```


- more info see https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md



### plugins to gitbook

book.json file

```json
{
    "gitbook": ">=2.0.0",
    "plugins": ["edit-link","googledocs","atoc","github","gitbookcode","chart","image-captions","mermaid2","highlight2","codeblock","zingchart"],
    "pluginsConfig": {
            "edit-link": {
                "base": "https://github.com/Incubaid/dev_process/edit/master/",
                "label": "Edit This Page"
            },
    "googledocs": {
            "rm": "minimal",
            "frameborder": "0",
            "width": "100%",
            "height": "500px",
            "noembed": "new window"
        },
     "atoc": {
            "addClass": true,
            "className": "atoc"
        },
    "chart": {
            "type": "highcharts"
        },
    "github": {
            "url": "https://github.com/Incubaid/dev_process"
        }
    }
}




```

is example file to be put in gitbook (in root of folder), enables next plugins.

#### table of contents

- [plugin](https://plugins.gitbook.com/plugin/atoc)

#### gdocs inclusion

see [link](https://plugins.gitbook.com/plugin/googledocs)

example
```
http://spreadsheets.google.com/ccc?key={key}&hl=en
```

#### mermaid

SEEMS NOT TO BE WORKING ON ALL SYSTEMS (e.g. on my OSX I can't get it to work, but on gitbook site it works)

- [plugin](https://plugins.gitbook.com/plugin/mermaid2)
- [info about mermaid](http://knsv.github.io/mermaid/)

```
\{% mermaid %\}
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
\{% endmermaid %\}
```


#### include codeblock

- [plugin](https://plugins.gitbook.com/plugin/include-codeblock)

```
\[import\](fixtures/test.js)
```

```
\[import, lang-typescript\]\(hello-world.ts\)
```

```
\[import:<start-lineNumber>-<end-lineNumber>\]\(path/to/file\)
```

dont use the '\' in examples above



#### include

to include other markdown docs, ideal to avoid repetition

- [plugin](https://plugins.gitbook.com/plugin/include)

```
\!\INCLUDE "file.md"
```

dont use the '\' in example above


#### zingchart

docs see
https://www.zingchart.com/docs/

```
\{% zingchart width=300, height=300 %\}
{
    "type":"bar",  
    "series":[  
        { "values": [35, 42, 67, 89]},
        { "values": [28, 40, 39, 36]}
    ]
}
\{% endzingchart %\}
```

{% zingchart width=300, height=300 %}
{
    "type":"bar",  
    "series":[  
        { "values": [35, 42, 67, 89]},
        { "values": [28, 40, 39, 36]}
    ]
}
{% endzingchart %}
 