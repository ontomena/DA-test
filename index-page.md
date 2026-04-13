---
layout: default
title: index
permalink: /index-page/
---

<div id="index-page">
<h1>index</h1>

<div class="alphabetical-index">
  {% assign posts_by_title = site.posts | sort: 'title' %}
  {% assign grouped_posts = posts_by_title | group_by_exp: "post", "post.title | slice: 0 | upcase" %}
  
  {% for group in grouped_posts %}
    <div class="index-section">
      <h2 class="index-letter">{{ group.name }}</h2>
      <ul class="index-list">
        {% for post in group.items %}
          <li>
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <span class="index-meta">
              ({{ post.date | date: "%Y" }})
              {% if post.categories.size > 0 %}
                — {{ post.categories | join: ", " | capitalize }}
              {% endif %}
            </span>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>
</div>
