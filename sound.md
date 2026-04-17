---
layout: default
title: Sound
permalink: /sound/
category_name: sound
---

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
