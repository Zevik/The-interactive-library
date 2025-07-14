---
title: הספרייה האינטראקטיבית שלי
layout: base.njk
templateEngineOverride: njk, md
---

<div class="library-container">
  <header class="library-header">
    <h1>ספרייה אינטראקטיבית</h1>
    <p>מסע למידה מרתק בעולם הידע והגילוי</p>
  </header>

  <div class="search-wrapper">
    <input type="text" id="searchInput" placeholder="חיפוש..." class="search-field">
  </div>

  <div class="categories-container">
    {# Group all posts by category #}
    {% set postsByCat = collections.post | groupby("category") %}

    {% for category in postsByCat %}
      <div class="category-box" data-category="{{ category.key }}">
        <div class="category-header" onclick="toggleCategory('{{ loop.index }}')">
          <h2>{{ category.key }}</h2>
          <span class="item-count">{{ category.items | length }}</span>
          <span class="toggle-icon" id="toggle-{{ loop.index }}">▼</span>
        </div>
        
        <div class="category-content" id="content-{{ loop.index }}" style="display: none;">
          {% for post in category.items %}
            <div class="post-item" data-title="{{ post.data.title | lower }}">
              <a href="{{ post.url }}">{{ post.data.title }}</a>
            </div>
          {% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<script>
function toggleCategory(index) {
  const content = document.getElementById(`content-${index}`);
  const toggle = document.getElementById(`toggle-${index}`);
  
  if (content.style.display === 'none') {
    content.style.display = 'block';
    toggle.textContent = '▲';
  } else {
    content.style.display = 'none';
    toggle.textContent = '▼';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  
  searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const categoryBoxes = document.querySelectorAll('.category-box');
    
    categoryBoxes.forEach(box => {
      let hasVisiblePosts = false;
      const postItems = box.querySelectorAll('.post-item');
      
      postItems.forEach(item => {
        const title = item.getAttribute('data-title');
        if (searchTerm === '' || title.includes(searchTerm)) {
          item.style.display = 'block';
          hasVisiblePosts = true;
        } else {
          item.style.display = 'none';
        }
      });
      
      if (searchTerm === '') {
        box.style.display = 'block';
      } else {
        box.style.display = hasVisiblePosts ? 'block' : 'none';
        if (hasVisiblePosts) {
          const content = box.querySelector('.category-content');
          const toggle = box.querySelector('.toggle-icon');
          content.style.display = 'block';
          toggle.textContent = '▲';
        }
      }
    });
  });
});
</script>