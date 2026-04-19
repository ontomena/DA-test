---
layout: default
title: poetry
permalink: /poetry/
tag_name: poetry
---

<div id="{{ page.tag_name }}-page">
<h1>{{ page.tag_name }}</h1>

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
