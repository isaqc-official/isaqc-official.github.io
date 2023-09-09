---
layout: post
title: Introduction to Qiskit
date: 2023-09-08 09:57:00+0530
description: A gentle introduction to programming on a quantum computer using Qiskit, a python library by IBM
tags: Introductory
categories: learning-to-code
giscus_comments: true
related_posts: false
---

You can download the jupyter file from  [here][1] in ipynb format. Run the notebook on an IBM qiskit session to follow along.

[1]:{{ site.url }}/assets/jupyter/tut1.ipynb

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/tut1.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/tut1.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
    {% jupyter_notebook jupyter_path %}
{% else %}
    <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

