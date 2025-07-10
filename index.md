---
title: הספרייה האינטראקטיבית שלי
layout: base.njk
templateEngineOverride: njk, md
---
# ברוכים הבאים לספרייה האינטראקטיבית

להלן רשימת כל דפי הלימוד, מקובצים לפי נושא:

{# Step 1: Group all posts by their 'category' frontmatter field #}
{% set postsByCat = collections.post | groupby("category") %}

{# Step 2: Loop through each group (each category) #}
{% for category in postsByCat %}
  
  <h2>{{ category.key }}</h2>
  
  <ul>
    {# Step 3: Loop through each post within the current category group #}
    {% for post in category.items %}
      <li>
        <a href="{{ post.url }}">{{ post.data.title }}</a>
      </li>
    {% endfor %}
  </ul>

{% endfor %}