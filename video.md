---
layout: default
title: video
permalink: /video/
---

<div id="video-page">
<h1>video</h1>

<div class="posts-grid">
  {% assign video_posts = site.posts | where_exp: "post", "post.categories contains 'video'" %}
  {% for post in video_posts %}
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
</div>
