---
layout: default
title: Tagname
permalink: /tagname/
tag_name: tagname
---

{% comment %}
  === TAG PAGE TEMPLATE ===
  
  A tag page shows all posts tagged with a given theme
  (e.g. album, poetry, projects, research, performance).
  Tags are many-per-post, whereas categories are one-per-post.
  
  The nil-safe query below handles the case where the tag
  doesn't yet appear on any posts — renders an empty grid
  rather than crashing the build.
  
  To create a new tag page:
    1. Replace "Tagname" (capitalised) with the capitalised tag name.
    2. Replace "tagname" (lowercase, two occurrences) with the lowercase
       tag name.
    3. Save as <lowercase-name>.md in the repo root.
  
  Nothing below this front matter needs changing.
{% endcomment %}

<div id="{{ page.tag_name }}-page">
<h1>{{ page.tag_name | capitalize }}</h1>

<div class="posts-grid">
  {% assign raw_posts = site.tags[page.tag_name] %}
  {% assign all_posts = "" | split: "," %}
  {% if raw_posts %}{% assign all_posts = raw_posts | sort: 'date' | reverse %}{% endif %}

  {% for post in all_posts %}
    <a href="{{ post.url | relative_url }}" class="post-card">
      {% if post.image %}
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="post-thumbnail">
      {% else %}
        <div class="post-thumbnail" style="background: #e8e8e8;"></div>
      {% endif %}
      
      <h2>{{ post.title }}</h2>
      
      {% if post.categories.size > 0 %}
        <div class="post-categories">{{ post.categories | first | capitalize }}</div>
      {% endif %}
      {% if post.tags.size > 0 %}
        <div class="post-categories">
          {% for tag in post.tags %}{{ tag | downcase }}{% unless forloop.last %}, {% endunless %}{% endfor %}
        </div>
      {% endif %}
      
      <div class="post-meta">{{ post.date | date: "%d %b %Y" }}</div>
      
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
    </a>
  {% endfor %}
</div>
</div>
