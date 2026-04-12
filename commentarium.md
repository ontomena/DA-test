---
layout: default
title: commentarium
permalink: /commentarium/
---

<h1>commentarium</h1>

<div class="posts-grid">
  {% for post in site.posts %}
    <a href="{{ post.url | relative_url }}" class="post-card">
      {% if post.image %}
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="post-thumbnail">
      {% else %}
        <div class="post-thumbnail" style="background: #e8e8e8;"></div>
      {% endif %}
      
      <h2>{{ post.title }}</h2>
      
      <div class="post-categories">
        {% for category in post.categories %}
          {{ category | capitalize }}{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </div>
      
      <div class="post-meta">{{ post.date | date: "%d %b %Y" }}</div>
      
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
    </a>
  {% endfor %}
</div>
