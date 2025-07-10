---
title: הספרייה האינטראקטיבית שלי
layout: base.njk
---
# ברוכים הבאים לספרייה האינטראקטיבית

להלן רשימת כל דפי הלימוד הזמינים כרגע:

<ul>
{%- for page in collections.post -%}
  <li>
    <a href="{{ page.url }}">{{ page.data.title }}</a>
  </li>
{%- endfor -%}
</ul>

