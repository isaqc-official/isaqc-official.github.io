---
layout: page
title: news
permalink: /news/
nav: true
nav_order: 3
---

{% assign news_posts = site.news | sort: 'date' | reverse %}
{% for post in news_posts %}
### {{ post.title }}
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more]({{ post.url }})

---
{% endfor %}

<!-- # Latest News

Welcome to our news page!
Here you'll find all the latest updates and announcements.

## March 15, 2025 - Project Launch!
We are excited to announce the launch of our new project. More details soon.

## February 28, 2025 - New Feature Released
Check out our latest feature in the [updates section](/updates). -->