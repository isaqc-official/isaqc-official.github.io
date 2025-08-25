# ISAQC Website Guide

Welcome to the ISAQC website! This guide explains how to add and manage content such as stories (blog posts), resources, news, and more.

## Table of Contents

- [Adding Stories (Blog Posts)](#adding-stories-blog-posts)
- [Adding Resources (Projects)](#adding-resources-projects)
- [Adding News](#adding-news)
- [Adding Publications](#adding-publications)
- [Managing Social Links](#managing-social-links)
- [Site Configuration](#site-configuration)
- [Useful Folders](#useful-folders)
- [Customizing Appearance](#customizing-appearance)
- [Building and Running Locally](#building-and-running-locally)

---

## Adding Stories (Blog Posts)

Blog posts are stored in the [`_posts`](./_posts) directory. Each post is a Markdown file with a specific filename format: `YYYY-MM-DD-title.md`.

**Steps:**
1. Create a new file in `_posts/` named like `2024-06-01-my-story.md`.
2. Add [YAML front matter](https://jekyllrb.com/docs/front-matter/) at the top:

    ```yaml
    ---
    layout: post
    title: My Story Title
    date: 2024-06-01 12:00:00
    description: A brief summary of the story.
    tags: quantum computing story
    categories: stories
    giscus_comments: true
    ---
    ```

3. Write your content below the front matter in Markdown.

**Features:**
- Use `tags` and `categories` for organization.
- Enable comments by setting `giscus_comments: true` or `disqus_comments: true`.
- Add a table of contents by including:
    ```yaml
    toc:
      beginning: true
    ```
    in the front matter.

## Adding Resources (Projects)

Resources are managed as "projects" and stored in the [`_data/repositories.yml`](./_data/repositories.yml) and [`_pages/projects.md`](./_pages/projects.md).

**Steps:**
1. Add your project details to the appropriate data file (e.g., `_data/repositories.yml` for GitHub repos).
2. To display resources, edit [`_pages/projects.md`](./_pages/projects.md) and update the `display_categories` list or add new categories.
3. Each project card is generated automatically from the data.

**Features:**
- Projects can be categorized (e.g., self-study, club-session).
- Images and descriptions are shown in cards.
- Horizontal or grid layouts are supported via the `horizontal` flag in the front matter.

## Adding News

News items are stored in the [`_news`](./_news) directory as Markdown files.

**Steps:**
1. Create a new file in `_news/` named like `announcement_4.md`.
2. Add front matter:

    ```yaml
    ---
    layout: post
    date: 2024-06-01 08:00:00
    inline: true
    related_posts: false
    ---
    ```

3. Write your news content below.

**Features:**
- News is displayed on the [news page](./news.html) and optionally on the [about page](./_pages/about.md) if enabled.

## Adding Publications

Publications are managed using [Jekyll Scholar](https://github.com/inukshuk/jekyll-scholar) and stored in [`_bibliography/papers.bib`](./_bibliography/papers.bib).

**Steps:**
1. Add your BibTeX entries to `papers.bib`.
2. Publications are automatically listed on the [publications page](./_pages/publications.md).

**Features:**
- Supports badges (Altmetric, Dimensions).
- Author highlighting and links.

## Managing Social Links

Social links are configured in [`_config.yml`](./_config.yml) under the "Social integration" section.

**Steps:**
1. Add your usernames/IDs for platforms like GitHub, Instagram, LinkedIn, etc.
2. These will appear in the site header/footer and about page.

## Site Configuration

Global settings are managed in [`_config.yml`](./_config.yml):

- Change site title, description, and contact info.
- Enable/disable features like analytics, comments, dark mode, masonry layout, etc.
- Set blog and project categories/tags.

## Useful Folders

- `_posts/` — Blog stories
- `_news/` — News items
- `_pages/` — Static pages (about, cv, projects, publications, etc.)
- `_data/` — Data files (coauthors, cv, repositories, venues)
- `_includes/` — Reusable HTML snippets
- `_layouts/` — Page templates
- `assets/` — Images, audio, JS, CSS

## Customizing Appearance

- Change colors, fonts, and layout in [`_sass/`](./_sass/) and [`_includes/head.html`](./_includes/head.html).
- Add or modify images in [`assets/img/`](./assets/img/).

## Building and Running Locally

**Requirements:**
- [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
- [Bundler](https://bundler.io/)

**Steps:**
1. Install dependencies:
    ```sh
    bundle install
    ```
2. Build and serve locally:
    ```sh
    bundle exec jekyll serve
    ```
3. Visit `http://localhost:4000` in your browser.

---

## Additional Notes

- For advanced features (diagrams, code highlighting, comments), see the relevant plugin documentation.
- For troubleshooting, refer to [CONTRIBUTING.md](./CONTRIBUTING.md).

---

Happy editing!