---
# Page settings
layout: default
keywords:
comments: false

# Hero section
title: Project
description: One of CS230's main goals is to prepare you to apply machine learning algorithms to real-world tasks, or to leave you well-qualified to start machine learning or AI research. The final project is intended to start you in these directions.



# Micro navigation
micro_nav: true

---

# Getting Started

## Project Starter Package

The teaching team has put together a [github repository](https://github.com/cs230-stanford/cs230-code-examples) with project code examples, including a computer vision and a natural language processing example (both in Tensorflow and Pytorch). There is also a series of [posts](https://cs230-stanford.github.io/) to help you familiarize yourself with the project code examples, get ideas on how to structure your deep learning project code, and to setup AWS. The code examples posted are optional and are only meant to help you with your final project. The code can be reused in your projects, but the examples presented are not complex enough to meet the expectations of a quarterly project. 
<!-- For specific questions about the code/posts, please drop by Guillaume Genthial (Tensorflow NLP), Olivier Moindrot (Tensorflow Vision), Surag Nair (PyTorch) or Russell Kaplan's (AWS setup) office hours. -->

## Project Topics

This quarter in CS230, you will learn about a wide range of deep learning applications. Part of the learning will be online, during in-class lectures and when completing assignments, but you will really experience hands-on work in your final project. We would like you to choose wisely a project that fits your interests. One that would be both motivating and technically challenging.

Most students do one of three kinds of projects:

 * **Application project.** This is by far the most common: Pick an application that interests you, and explore how best to apply learning algorithms to solve it.
 * **Algorithmic project.** Pick a problem or family of problems, and develop a new learning algorithm, or a novel variant of an existing algorithm, to solve it.
 * **Theoretical project.** Prove some interesting/non-trivial properties of a new or an existing learning algorithm. (This is often quite difficult, and so very few, if any, projects will be purely theoretical.)
Some projects will also combine elements of applications and algorithms.

Many fantastic class projects come from students picking either an application area that they're interested in, or picking some subfield of machine learning that they want to explore more. So, pick something that you can get excited and passionate about! Be brave rather than timid, and do feel free to propose ambitious things that you're excited about. (Just be sure to ask us for help if you're uncertain how to best get started.) Alternatively, if you're already working on a research or industry project that deep learning might apply to, then you may already have a great project idea.

## Project Hints

A very good CS230 project will be a publishable or nearly-publishable piece of work. Each year, some number of students continue working on their projects after completing CS230, submitting their work to a conferences or journals. Thus, for inspiration, you might also look at some recent deep learning research papers. Two of the main machine learning conferences are [ICML](https://icml.cc/) and [NIPS](https://nips.cc/). Finally, looking at class projects from previous years of CS230 ([Fall 2017](/project/2017#fall), [Winter 2018](/project/2018#winter), [Spring 2018](/project/2018#spring), [Fall 2018](/project/2018#fall)) and other machine learning/ deep learning classes ([CS229](http://cs229.stanford.edu/), [CS229A](https://web.stanford.edu/class/cs229a/), [CS221](http://web.stanford.edu/class/cs221/), [CS224N](http://web.stanford.edu/class/cs224w/), [CS231N](http://cs231n.stanford.edu/)) is a good way to get ideas.

Once you have identified a topic of interest, it can be useful to look up existing research on relevant topics by searching related keywords on an academic search engine such as: [http://scholar.google.com](http://scholar.google.com). Another important aspect of designing your project is to identify one or several datasets suitable for your topic of interest. If that data needs considerable pre-processing  to suit your task, or that you intend to collect the needed data yourself, keep in mind that this is only one part of the expected project work, but can often take considerable time. We still expect a solid methodology and discussion of results, so pace your project accordingly.

Notes on a few specific types of projects:

 * **Computation power.** We will update you if we manage to get you free GPU credits but in any case both [Google Cloud](https://cloud.google.com/edu/) and [Microsoft Azure](https://azure.microsoft.com/en-us/education/) offer free academic units which you can apply to.
 * **Preprocessed datasets.** While we don't want you to have to spend much time collecting raw data, the process of inspecting and visualizing the data, trying out different types of preprocessing, and doing error analysis is often an important part of machine learning. Hence if you choose to use preprepared datasets (e.g. from Kaggle, the UCI machine learning repository, etc.) we encourage you to do some data exploration and analysis to get familiar with the problem.
 * **Replicating results.** Replicating the results in a paper can be a good way to learn. However, we ask that instead of just replicating a paper, also try using the technique on another application, or do some analysis of how each component of the model contributes to final performance.

# Project Deliverables

This section contains the detailed instructions for the different parts of your project.

**Submission:** We will be using Gradescope for submission of all four parts of the final project. We’ll announce when submissions are open for each part. You should submit on Gradescope as a group: that is, for each part, please make one submission for your entire project group and tag your team members.

**Evaluation:** We will not be disclosing the breakdown of the 40% that the final project is worth amongst the different parts, but the poster and final report will combine to be the majority of the grade. Projects will be evaluated based on:

 * The technical quality of the work. (I.e., Does the technical material make sense? Are the things tried reasonable? Are the proposed algorithms or applications clever and interesting? Do the authors convey novel insight about the problem and/or algorithms?)
 * Significance. (Did the authors choose an interesting or a “real" problem to work on, or only a small “toy" problem? Is this work likely to be useful and/or have impact?)
 * The novelty of the work. (Is this project applying a common technique to a well-studied problem, or is the problem or method relatively unexplored?)

In order to highlight these components, it is important you present a solid discussion regarding the learnings from the development of your method, and summarizing how your work compares to existing approaches.



## Proposal

**Deadline:** October 14th, Sunday 11:59 PM

In the project proposal, you'll pick a project idea to work on early and receive feedback from the TAs. If your proposed project will be done jointly with a different class' project, you should obtain approval from the other instructor and approval from us. Please come to the project office hours to discuss with us if you would like to do a joint project. You should submit your proposals on Gradescope. All students should already be added to the course page on Gradescope via your SUNet IDs. If you are not, please create an account with **your Stanford email** and enroll in CS230.

In the proposal, below your project title, include the project category. The category can be one of:

 * Computer Vision
 * Natural Language Processing
 * Generative Modeling
 * Speech Recognition
 * Reinforcement Learning
 * Healthcare
 * Others (Please specify!)

Your project proposal should include the following information:
 * What is the problem that you will be investigating? Why is it interesting?
 * What are the challenges of this project?
 * What dataset are you using? How do you plan to collect it?
 * What method or algorithm are you proposing? If there are existing implementations, will you use them and how? How do you plan to improve or modify such implementations?
 * What reading will you examine to provide context and background? If relevant, what papers do you refer to?
 * How will you evaluate your results? Qualitatively, what kind of results do you expect (e.g. plots or figures)? Quantitatively, what kind of analysis will you use to evaluate and/or compare your results (e.g. what performance metrics or statistical tests)?

Presenting pointers to one relevant dataset and one example of prior research on the topic are a valuable (optional) addition. 


| **Project mentors** | Based off of the topic you choose in your proposal, we’ll suggest a project mentor given the areas of expertise of the TAs. This is just a recommendation; feel free to speak with other TAs as well.
| **Format** | Your proposal should be a PDF document, giving the title of the project, the project category, the full names of all of your team members, the SUNet ID of your team members, and a 300-500 word description of what you plan to do.
| **Grading** | The project proposal is mainly intended to make sure you decide on a project topic and get feedback from TAs early. As long as your proposal follows the instructions above and the project seems to have been thought out with a reasonable plan, you should do well on the proposal.
| **Submission** | Submit on Gradescope (see description under deadline for instructions)

## Milestone

**Deadline:** November 9th, Friday 11:59pm

The milestone will help you make sure you're on track, and should describe what you've accomplished so far, and very briefly say what else you plan to do. You should write it as if it's an “early draft" of what will turn into your final project. You can write it as if you're writing the first few pages of your final project report, so that you can re-use most of the milestone text in your final report. Please write the milestone (and final report) keeping in mind that the intended audience is Profs. Ng and Katanforoosh and the TAs. Thus, for example, you should not spend two pages explaining what logistic regression is. Your milestone should include the full names of all your team members and state the full title of your project. **Note:** We will expect your final writeup to be on the same topic as your milestone. In order to help you the most, we expect you to submit your running code. Your code should contain a baseline model for your application. Along with your baseline model, you are welcome to submit additional parts of your code such as data pre-processing, data augmentation, accuracy matric(s), and/or other models you have tried. Please clean your code before submitting, comment on it, and cite any resources you used. Please **do not submit your dataset**. However, you may include a few samples of your data in the report if you wish.

## Poster

**Date:** December 14th, Friday (8:30am - 11:30am) 
**Location:** TBD 

The class projects will be presented at a poster presentation, at a location and time that will be announced later. Each team should prepare a poster, and be prepared to give a very short explanation, in front of the poster, about their work. At the poster session, you'll also have an opportunity to see what everyone else did for their projects. We will supply poster-boards and easels for displaying the posters.

## Final Report

**Deadline:**  December 16th, Sunday 11:59PM 

Because the teaching staff will have only a few hours to see a large number of posters at the poster session, we'll only be able to get an overview of the work you did at the session. We know that most students work very hard on the final projects, and so we are extremely careful to give each writeup ample attention, and read and try very hard to understand everything you describe in it.

After the class, we will also post all the final writeups online so that you can read about each other's' work. If you do not want your write-up to be posted online, then please create a private Piazza post or contact us at cs230-project@cs.stanford.edu at least a week in advance of the final submission deadline.