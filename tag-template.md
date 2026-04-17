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
  
  To create a new tag page:
    1. Replace "Tagname" (capitalised) with the capitalised tag name.
    2. Replace "tagname" (lowercase, two occurrences) with the lowercase
       tag name.
    3. Save as <lowercase-name>.md in the repo root.
  
  The tag will show up on posts automatically once posts are tagged
  with it in their front matter.
  
  Nothing below this front matter needs changing.
{% endcomment %}

<div id="{{ page.tag_name }}-page">
<h1>{{ page.tag_name | capitalize }}</h1>

<div class="posts-grid">
  {% assign all_posts = site.tags[page.tag_name] | sort: 'date' | reverse %}
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
