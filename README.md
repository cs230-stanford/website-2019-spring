# Website
This repository contains the code for the new CS230 website (launched in January 2019)

# To Do:
 * Add toggle content to the FAQ
 * Complete documentation for updating website
 * Update previous project list

# Accessing Website:
 * The web interface for AFS: https://afs.stanford.edu/
 * The class folder is located at /afs/ir/class/cs230/WWW

# To host:

 * Run JEKYLL\_ENV=production jekyll build
 * Copy contents of \_site folder to server

# Improvements
 * Better FAQ
 * Answer include box for sections 


# How to edit a page?

### Get a local version of the website running

- Clone a local repo of this reposiroty.
- Unzip the folder and cd into it from terminal.
- Run "gem install bundler jekyll" or "sudo gem install bundler jekyll" to install Jekyll.
- Run "jekyll serve".
- A local version of the website should be accesible at `http://127.0.0.1:4000`.

### Edit the markdown file

Open the markdown file for the page you want to edit. Notice that if you edit this page then reload the website, your changes will have been added. Edit the text, clean up typos, make sure it looks good, and don't forget to add a desciption in the top section.

(3) Some hints
- Other than the description, don't edit the first few rows of text between `--` and `--`.
- For shortcuts to adding hyperlinks and markdown formatting use this [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
- HOW TO ADD LATEX? Write normal latex code and surround it in dollar signs: `$$inline math$$`.  For centered math put it on a newline:

`$$centered math$$`
 
- The only difference is HOW TO ADD IMAGES?  The raw images should go in the following folder "doks-theme/assets/images/lecture/[lecture number]". Instead of using `![Alt text](image.png)` use the following `{% include image.html description="add description" link="external url image source" image="lecture/[lecture number]/[image.png]" caption="true"%}`

(4) Add changes

Once you are done editing your lecture markdown file then either submit a pull request on the Github page or email me the file.  If you need images that arn't already on the repository then send them to me as well.