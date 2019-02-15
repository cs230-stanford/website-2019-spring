---
# Page settings
layout: default
keywords:
comments: false

# Hero section
title: AWS Setup
description: How to set up AWS for deep learning projects

# Micro navigation
micro_nav: true

# Page navigation
page_nav:
    prev:
        content: Previous page
        url: '/blog/tips'
    next:
        content: 
        url: '#'
---

## **Get your AWS credits**

For this winter 2018 session, AWS is offering GPU credits for CS230 students. If no one on your team has requested AWS credit yet, please follow the instructions on the AWS piazza post to get your credits.

## **Create a Deep Learning EC2 instance**

Follow Amazon’s [getting started guide](https://aws.amazon.com/blogs/machine-learning/get-started-with-deep-learning-using-the-aws-deep-learning-ami/) for creating a **Deep Learning instance**. Be sure to pick the Ubuntu version of the deep learning Amazon Machine Images (AMI) at the third screen. For the instance type, we recommend using **p2.xlarge**. This is available in the **US East (Northern Virginia)** region (it’s not available in Northern California). Follow the instructions to SSH into the instance.

**IMPORTANT**: Be sure to not forget to **turn off your instance** when you are not using it! If you leave it running, you will be billed continuously for the hours it is left on and you will run out of credits very quickly.

## **Clone the project code examples**

It’s not required to base your project on the Project Code Examples, but it might be helpful. (Some of you might be using existing code from another GitHub repo instead, for example.) For an introduction to the code examples, see [our tutorial](/blog/tips). To clone, run this command inside your SSH session with the amazon server:

```python
git clone https://github.com/cs230-stanford/cs230-code-examples.git
```

## **Start training**

You’re ready to start training! Follow the instructions in the [project tutorial](/blog/tips) to start training a model. We’re excited about the amazing things you will build!
