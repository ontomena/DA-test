---
layout: default
title: word
permalink: /word/
---

<div id="word-page">
<h1>word</h1>

<div class="posts-grid">
  {% assign word_only = site.posts | where_exp: "post", "post.categories contains 'word'" %}
  {% assign text_only = site.posts | where_exp: "post", "post.categories contains 'text'" %}
  {% assign word_posts = word_only | concat: text_only | sort: 'date' | reverse | uniq %}
  {% for post in word_posts %}
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
