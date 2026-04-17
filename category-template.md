---
layout: default
title: Categoryname
permalink: /categoryname/
category_name: categoryname
---

{% comment %}
  === CATEGORY PAGE TEMPLATE ===
  
  A category page represents one of the three main site sections
  (currently word / sound / video). Each post has exactly one category.
  
  The hybrid query below pulls posts where category == name OR tags
  contains name — so a post with category "sound" and tag "word" 
  appears on BOTH /sound/ AND /word/, giving cross-section visibility.
  
  The nil-safe query handles the case where a category/tag doesn't
  yet appear on any posts — renders an empty grid rather than 
  crashing the build.
  
  To create a new category page:
    1. Replace "Categoryname" (capitalised) with the capitalised name
       (e.g. "Photography").
    2. Replace "categoryname" (lowercase, two occurrences) with the 
       lowercase name (e.g. "photography").
    3. Save as <lowercase-name>.md in the repo root.
    4. Add a nav menu entry in _layouts/default.html if desired.
  
  Nothing below this front matter needs changing.
{% endcomment %}

<div id="{{ page.category_name }}-page">
<h1>{{ page.category_name | capitalize }}</h1>

<div class="posts-grid">
  {% assign cat_posts = site.categories[page.category_name] %}
  {% assign tag_posts = site.tags[page.category_name] %}
  {% assign combined = "" | split: "," %}
  {% if cat_posts %}{% assign combined = combined | concat: cat_posts %}{% endif %}
  {% if tag_posts %}{% assign combined = combined | concat: tag_posts %}{% endif %}
  {% assign all_posts = combined | uniq | sort: 'date' | reverse %}

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
