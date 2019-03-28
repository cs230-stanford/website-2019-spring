# CS230 Website
This repository contains the code for the new CS230 website (launched in January 2019), which is based on the [Doks](https://doks.themejack.com/green/) Jekyll theme.

# How to Edit a Page?

### Get a local version of the website running

- Clone a local copy of this repository.
- Unzip the folder and `cd` into it from terminal.
- If you haven't already installed Jekyll](https://jekyllrb.com/), then run `gem install bundler jekyll` or `sudo gem install bundler jekyll`.
- Run `jekyll serve`.
- A local version of the website should be accessible at `http://127.0.0.1:4000`.

### Edit the Markdown file

Open the Markdown file (`.md`) for the page you want to edit. Generally, don't edit the first few rows of text between `--` and `--`.  Notice that if you edit this page then reload the website, your changes will have been added. Don't forget to **commit your changes** to the Github page.


# How to Publish a Page?

### Generate a publishable version

From terminal run `JEKYLL\_ENV=production jekyll build` in the top folder for a local version of the website. A publishable HTML version of the website will be available in the `\_site` folder.

### Transfer content to server

Transfer the content of the `\_site` folder to Stanford's AFS server with either the [web interface](https://afs.stanford.edu/) or SFTP tools.  CS230's website folder is located at `/afs/ir/class/cs230/WWW`.  For more information on transferring files to AFS read [here](https://uit.stanford.edu/service/afs/file-transfer).


# Helpful hints

For shortcuts to Markdown formatting check out this [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).  Below are specific formatting tricks for this repository.

### Hyperlinks
For external links use `[link](https://...)` and for local links use `[link](/path/to/file)`.

### Images
The raw images should go in the following folder `doks-theme/assets/images/[article type]/[number]`. Instead of using `![Alt text](image.png)` use the following `{% include image.html description="add description" link="external url image source" image="[article type]/[number]/[image.png]" caption="true"%}`.

### Latex
This repository uses [MathJax](https://www.mathjax.org/) to render Latex.  Simply write normal Latex code in the Markdown files and surround it in dollar signs.  For `$$inline math$$` simply put it directly in a sentence, while for

<center>`$$centered math$$`</center>

put it on a newline.

# What can be improved

Below is a list of suggested changes for the website and content:

- Standardize previous project list and make a standardized method for adding new ones.
- Add a toggle answer include for the FAQ, Sections, and Lectures.
- Simplify Syllabus.