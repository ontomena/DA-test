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
                — {{ post.categories | first | capitalize }}{% if post.tags.size > 0 %}, {% for tag in post.tags %}{{ tag | downcase }}{% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}
              {% endif %}
            </span>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>

<div style="margin-top: 60px; padding-top: 24px; border-top: 1px solid #e0e0e0; color: #666; font-size: 0.95em;">
  {% assign excluded = "word,sound,video" | split: "," %}
  {% assign tag_names = "" | split: "," %}
  {% for tag in site.tags %}
    {% assign tag_name = tag[0] | downcase %}
    {% unless excluded contains tag_name %}
      {% assign single = tag_name | split: "|||" %}
      {% assign tag_names = tag_names | concat: single %}
    {% endunless %}
  {% endfor %}
  {% assign sorted_names = tag_names | sort | uniq %}
  {% for name in sorted_names %}
    <a href="{{ name | prepend: '/' | append: '/' | relative_url }}">{{ name }}</a>{% unless forloop.last %}, {% endunless %}
  {% endfor %}
</div>

</div>
