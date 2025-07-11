---
title: "חוקי הגשטאלט בפעולה: הדמיה אינטראקטיבית של תפיסה ויזואלית"
english_slug: gestalt-principles-proximity-similarity-closure-simulation
category: "פסיכולוגיה קוגניטיבית"
tags: [פסיכולוגיה, תפיסה, ויזואליזציה, גשטאלט]
---
# חוקי הגשטאלט בפעולה: הדמיה אינטראקטיבית של תפיסה ויזואלית

איך המוח שלנו הופך נקודות וקווים למשמעות? האם אתם רואים קבוצות או צורות שלמות גם כשחסר מידע? צללו פנימה והתנסו באופן אישי כיצד עקרונות תפיסתיים פשוטים מעצבים את החוויה הוויזואלית שלנו ברגע זה. בואו לשחק עם התפיסה שלכם!

<div class="gestalt-container">

    <div class="principle-section" id="proximity-section">
        <h2>קירבה (Proximity)</h2>
        <p class="principle-intro">גלו כיצד המרחק בין אלמנטים משפיע על תפיסת הקבוצות.</p>
        <div class="controls">
            <div class="control-group">
                 <label for="proximity-spacing-x">מרווח אופקי:</label>
                 <input type="range" id="proximity-spacing-x" min="5" max="60" value="15">
            </div>
            <div class="control-group">
                 <label for="proximity-spacing-y">מרווח אנכי:</label>
                 <input type="range" id="proximity-spacing-y" min="5" max="60" value="35">
            </div>
        </div>
        <div class="visualization proximity-viz">
             <!-- Dots will be generated here by JS -->
        </div>
    </div>

    <div class="principle-section" id="similarity-section">
        <h2>דמיון (Similarity)</h2>
        <p class="principle-intro">ראו איך אלמנטים דומים נקשרים לקבוצות, גם במרחק.</p>
        <div class="controls">
             <div class="control-group">
                  <label for="similarity-type">קריטריון דמיון:</label>
                  <select id="similarity-type">
                      <option value="color">צבע</option>
                      <option value="shape">צורה</option>
                      <option value="size">גודל</option>
                  </select>
             </div>
        </div>
        <div class="visualization similarity-viz">
            <!-- Elements will be generated here by JS -->
        </div>
    </div>

     <div class="principle-section" id="closure-section">
        <h2>סגירות (Closure)</h2>
         <p class="principle-intro">המוח שלנו אוהב להשלים צורות חסרות. ראו את הקסם!</p>
        <div class="controls">
             <div class="control-group checkbox-group">
                  <label for="closure-complete">הצג צורות שלמות:</label>
                  <input type="checkbox" id="closure-complete" checked>
             </div>
        </div>
        <div class="visualization closure-viz">
            <!-- Shapes will be generated here by JS -->
        </div>
    </div>

</div>

<button id="show-explanation-btn" aria-expanded="false">הסבר: עקרונות הגשטאלט</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>פענוח התפיסה: עקרונות הגשטאלט</h2>
    <p>עקרונות הגשטאלט מספקים לנו הצצה מרתקת לאופן שבו המוח שלנו אינו רק "מקבל" מידע ויזואלי, אלא "מארגן" אותו באופן אקטיבי כדי ליצור משמעות. במקום לראות אוסף של חלקים בודדים, אנו תופסים יחידות שלמות וקוהרנטיות. זכרו את המנטרה: "השלם גדול מסכום חלקיו".</p>

    <h3>קירבה (Proximity) - המרחק קובע</h3>
    <p>כפי שחוויתם בהדמיה, כשאובייקטים קרובים פיזית זה לזה, המוח נוטה לקבץ אותם יחד. שינוי המרווחים, אפילו במעט, יכול לשנות באופן דרמטי את האופן שבו אתם תופסים את המבנה הכולל – שורות הופכות לטורים, ולהפך. המוח מחפש את המרחק הקצר ביותר ומשתמש בו כרמז ליצירת קבוצות.</p>

    <h3>דמיון (Similarity) - כמו קורא לכמו</h3>
    <p>גם כשאובייקטים אינם קרובים זה לזה, אם הם חולקים מאפיין משותף (כמו צבע, צורה, גודל או אוריינטציה), המוח מקבץ אותם אוטומטית לקבוצה אחת. ראיתם בהדמיה איך אלמנטים בצבע מסוים או בצורה מסוימת נתפסו כשייכים יחד, למרות המרווחים השווים ביניהם. דמיון ויזואלי יוצר חיבור תפיסתי.</p>

    <h3>סגירות (Closure) - השלמת הפאזל</h3>
    <p>זהו אחד העקרונות המרשימים ביותר. המוח שלנו שונא חוסר שלמות! גם כשאנו רואים צורות חלקיות או מקוטעות, המוח נוטה "לסגור" או להשלים את הפערים באופן אוטומטי כדי לתפוס אובייקט שלם ומוכר (כמו עיגול, ריבוע או משולש). ההדמיה הראתה כיצד מספר קווים או נקודות יכולים להיתפס מיד כצורה מלאה, אפילו כשחלקים ממנה פיזית אינם שם.</p>
</div>

<style>
    :root {
        --primary-color: #4a90e2; /* A vibrant blue */
        --secondary-color: #7bdcb5; /* A soft green */
        --accent-color: #f5a623; /* An energetic orange */
        --background-color: #eef4f8; /* Light background */
        --card-background: #ffffff; /* White cards */
        --text-color: #333333; /* Dark gray text */
        --heading-color: #2c3e50; /* Darker blue/gray heading */
        --border-color: #dddddd;
        --shadow-color: rgba(0, 0, 0, 0.08);
        --animation-duration: 0.4s;
        --easing: ease-in-out;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: var(--heading-color);
        text-align: center;
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-bottom: 20px;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        display: inline-block;
        width: auto;
        max-width: 100%;
        margin-right: auto;
        margin-left: auto;
    }

    p {
        margin-bottom: 15px;
    }

    .principle-intro {
        font-size: 1.1em;
        color: #555;
        margin-top: -10px;
        margin-bottom: 20px;
        font-style: italic;
    }

    .gestalt-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin-bottom: 40px;
        justify-content: center;
        padding: 0 10px;
    }

    .principle-section {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 15px var(--shadow-color);
        flex: 1 1 300px; /* Allow flex grow, basis 300px */
        max-width: 400px; /* Max width per section */
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform var(--animation-duration) var(--easing), box-shadow var(--animation-duration) var(--easing);
    }

    .principle-section:hover {
         transform: translateY(-5px);
         box-shadow: 0 12px 20px rgba(0, 0, 0, 0.12);
    }

    .principle-section h2 {
        margin-top: 0;
        color: var(--primary-color);
        font-size: 1.6em;
        margin-bottom: 10px;
    }

    .controls {
        margin-bottom: 25px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%; /* Make controls take full width */
    }

    .control-group {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 15px;
    }

     .control-group:last-child {
         margin-bottom: 0;
     }

    .controls label {
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 1em;
        color: #555;
    }

    .controls input[type="range"],
    .controls select {
        width: 90%; /* Wider controls */
        padding: 8px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        font-size: 1em;
        background-color: #f9f9f9;
        transition: border-color var(--animation-duration) var(--easing), box-shadow var(--animation-duration) var(--easing);
        cursor: pointer;
        -webkit-appearance: none; /* Remove default browser styling */
        appearance: none;
    }

     .controls input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
         margin-top: -8px; /* Center thumb vertically */
     }

     .controls input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         cursor: pointer;
         border-radius: 50%;
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
     }

     .controls input[type="range"]::-webkit-slider-runnable-track {
         width: 100%;
         height: 6px;
         cursor: pointer;
         background: #ddd;
         border-radius: 3px;
     }

     .controls input[type="range"]:focus::-webkit-slider-runnable-track {
        background: #ccc;
     }

      .controls input[type="range"]::-moz-range-track {
         width: 100%;
         height: 6px;
         cursor: pointer;
         background: #ddd;
         border-radius: 3px;
     }


    .controls select:focus,
    .controls input[type="range"]:focus {
         border-color: var(--primary-color);
         box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
         outline: none;
    }

     .checkbox-group {
         flex-direction: row;
         align-items: center;
         justify-content: center;
     }

     .checkbox-group label {
         margin-bottom: 0;
         margin-left: 10px;
         cursor: pointer;
     }

     .controls input[type="checkbox"] {
         width: 20px;
         height: 20px;
         cursor: pointer;
         accent-color: var(--primary-color); /* Color the checkbox */
     }


    .visualization {
        width: 100%; /* Visualization takes full width */
        min-height: 250px; /* Slightly larger area */
        border: 1px solid var(--border-color);
        background-color: #fefefe;
        border-radius: 8px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 15px; /* More padding */
        box-sizing: border-box; /* Include padding in width/height */
        position: relative; /* For absolute positioning of elements if needed */
    }

    /* --- Proximity Specific Styles --- */
    .proximity-viz {
        flex-direction: column; /* Default to rows */
        align-items: center; /* Center rows/columns */
    }

    .proximity-row, .proximity-col {
        display: flex;
        transition: margin var(--animation-duration) var(--easing); /* Animate row/col margins */
    }

    .proximity-col {
         flex-direction: column;
    }

    .proximity-dot {
        width: 12px; /* Slightly smaller dots */
        height: 12px;
        border-radius: 50%;
        background-color: var(--primary-color);
        transition: margin var(--animation-duration) var(--easing), background-color 0.3s ease; /* Animate dot margins and color */
        flex-shrink: 0; /* Prevent dots from shrinking */
    }

    /* --- Similarity Specific Styles --- */
    .similarity-viz {
        display: grid;
        grid-template-columns: repeat(5, auto);
        gap: 10px; /* Slightly increased gap */
        justify-content: center;
        align-items: center;
    }

    .similarity-element {
        width: 18px; /* Slightly larger elements */
        height: 18px;
        border-radius: 50%; /* Default shape is circle */
        background-color: var(--primary-color); /* Default color */
        transition: background-color var(--animation-duration) var(--easing), transform var(--animation-duration) var(--easing), border-radius var(--animation-duration) var(--easing), width var(--animation-duration) var(--easing), height var(--animation-duration) var(--easing); /* Animate properties */
         display: flex; /* Center content if any */
         justify-content: center;
         align-items: center;
    }

    .similarity-element.shape-square {
        border-radius: 4px; /* Slightly rounded corners for squares */
    }

     .similarity-element.shape-triangle {
         width: 0;
         height: 0;
         border-left: 10px solid transparent;
         border-right: 10px solid transparent;
         border-bottom: 18px solid var(--primary-color); /* Triangle pointing up */
         background-color: transparent; /* No background for triangle */
         border-radius: 0; /* No border radius */
     }

    .similarity-element.color-secondary {
        background-color: var(--secondary-color);
    }
     .similarity-element.color-accent {
        background-color: var(--accent-color);
    }

     .similarity-element.size-small {
         width: 14px;
         height: 14px;
     }
      .similarity-element.size-large {
         width: 22px;
         height: 22px;
     }


    /* --- Closure Specific Styles --- */
    .closure-viz {
        display: flex;
        gap: 40px; /* More space between shapes */
        justify-content: center;
        align-items: center;
        padding: 20px; /* Add padding to prevent shapes touching edge */
    }

    .closure-shape {
        width: 100px; /* Larger shapes */
        height: 100px;
        border: 15px solid var(--primary-color); /* Thicker borders */
        box-sizing: border-box;
        position: relative;
        overflow: hidden; /* Hide internal parts if any */
        transition: border-color var(--animation-duration) var(--easing);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .closure-shape.circle {
         border-radius: 50%;
         border-right-color: transparent;
         border-top-color: transparent;
         border-left-color: transparent;
         transform: rotate(-45deg); /* Start rotated for Pac-Man look */
         transition: border-color var(--animation-duration) var(--easing), transform var(--animation-duration) var(--easing);
    }
     .closure-shape.square {
         border-radius: 0;
         border-right-color: transparent;
         border-bottom-color: transparent;
          transform: rotate(0deg); /* Default rotation for square */
          transition: border-color var(--animation-duration) var(--easing), transform var(--animation-duration) var(--easing);
     }

     .closure-shape.complete {
         border-color: var(--primary-color); /* All borders visible */
         transform: rotate(0deg); /* Return to normal rotation */
     }

     /* Add subtle animation for incomplete state to hint at dynamism */
     .closure-shape:not(.complete) {
         animation: incomplete-hint 3s infinite var(--easing);
     }

     @keyframes incomplete-hint {
        0% { opacity: 1; }
        50% { opacity: 0.9; } /* Subtle fade */
        100% { opacity: 1; }
     }


    /* --- Explanation Toggle Button --- */
    #show-explanation-btn {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--secondary-color);
        color: var(--heading-color);
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color var(--animation-duration) var(--easing), transform 0.2s ease-out, box-shadow var(--animation-duration) var(--easing);
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #show-explanation-btn:hover {
        background-color: #65c9a2; /* Slightly darker green */
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
    }

     #show-explanation-btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
     }


    /* --- Explanation Section --- */
    .explanation-section {
        background-color: var(--card-background); /* Use card background */
        padding: 30px;
        border-radius: 12px;
        margin-top: 20px;
        border-left: 5px solid var(--primary-color);
        box-shadow: 0 4px 10px var(--shadow-color);
         opacity: 0; /* Start hidden for fade-in */
         max-height: 0;
         overflow: hidden;
         transition: opacity var(--animation-duration) var(--easing) , max-height var(--animation-duration) var(--easing);
    }

     .explanation-section.visible {
         opacity: 1;
         max-height: 1000px; /* Sufficiently large value for height transition */
     }

    .explanation-section h2 {
        margin-top: 0;
        color: var(--primary-color);
        text-align: right; /* Align explanation headings right */
    }

     .explanation-section h3 {
         color: #555; /* Slightly softer heading color */
         margin-top: 20px;
         margin-bottom: 10px;
         border-bottom: 1px dotted var(--border-color);
         padding-bottom: 5px;
     }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.6em;
        }
        .principle-section {
            padding: 20px;
            flex-basis: 100%; /* Stack sections on smaller screens */
            max-width: 100%;
        }
        .visualization {
             min-height: 200px;
             padding: 10px;
        }
         .controls input[type="range"],
         .controls select {
             width: 100%;
         }
         .closure-viz {
             gap: 20px;
         }
         .closure-shape {
             width: 80px;
             height: 80px;
             border-width: 12px;
         }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {

        // --- Explanation Toggle with Animation ---
        const explanationBtn = document.getElementById('show-explanation-btn');
        const explanationDiv = document.getElementById('explanation');

        explanationBtn.addEventListener('click', () => {
            const isVisible = explanationDiv.classList.contains('visible');
            if (isVisible) {
                explanationDiv.classList.remove('visible');
                // Allow time for transition before hiding display
                setTimeout(() => {
                     explanationDiv.style.display = 'none';
                     explanationBtn.textContent = 'הסבר: עקרונות הגשטאלט';
                     explanationBtn.setAttribute('aria-expanded', 'false');
                }, 400); // Match CSS transition duration
            } else {
                explanationDiv.style.display = 'block';
                 // Use a small timeout to allow display:block to apply before starting transition
                 setTimeout(() => {
                     explanationDiv.classList.add('visible');
                     explanationBtn.textContent = 'הסתר הסבר';
                      explanationBtn.setAttribute('aria-expanded', 'true');
                 }, 10); // Small delay
            }
        });

        // --- Proximity Visualization ---
        const proximityViz = document.querySelector('.proximity-viz');
        const spacingXSlider = document.getElementById('proximity-spacing-x');
        const spacingYSlider = document.getElementById('proximity-spacing-y');
        const rows = 5;
        const cols = 5;

        function createProximityGrid(spacingX, spacingY) {
            proximityViz.innerHTML = ''; // Clear previous grid

            // Determine dominant direction for layout hint
            const groupRows = spacingY <= spacingX + 5; // Add a small buffer

            if (groupRows) {
                proximityViz.style.flexDirection = 'column';
                for (let i = 0; i < rows; i++) {
                    const row = document.createElement('div');
                    row.classList.add('proximity-row');
                    row.style.marginBottom = `${spacingY}px`; // Apply vertical spacing to row
                    if (i === rows - 1) row.style.marginBottom = '0px'; // No margin on last row

                    for (let j = 0; j < cols; j++) {
                        const dot = document.createElement('div');
                        dot.classList.add('proximity-dot');
                        dot.style.marginRight = `${spacingX}px`; // Apply horizontal spacing to dot
                        if (j === cols - 1) dot.style.marginRight = '0px'; // No margin on last dot in row
                        row.appendChild(dot);
                    }
                    proximityViz.appendChild(row);
                }
            } else { // Group by columns
                 proximityViz.style.flexDirection = 'row';
                 for (let j = 0; j < cols; j++) {
                     const col = document.createElement('div');
                     col.classList.add('proximity-col');
                     col.style.marginRight = `${spacingX}px`; // Apply horizontal spacing to column
                      if (j === cols - 1) col.style.marginRight = '0px'; // No margin on last column

                     for (let i = 0; i < rows; i++) {
                         const dot = document.createElement('div');
                         dot.classList.add('proximity-dot');
                          dot.style.marginBottom = `${spacingY}px`; // Apply vertical spacing to dot
                          if (i === rows - 1) dot.style.marginBottom = '0px'; // No margin on last dot in col

                         col.appendChild(dot);
                     }
                     proximityViz.appendChild(col);
                 }
            }
             // Set padding dynamically to ensure spacing doesn't push dots out initially
             proximityViz.style.padding = `${spacingY/2}px ${spacingX/2}px`;
             proximityViz.style.alignItems = groupRows ? 'flex-start' : 'center';
             proximityViz.style.justifyContent = groupRows ? 'center' : 'flex-start';

             // Readjust padding after layout change slightly for better centering
             requestAnimationFrame(() => {
                 proximityViz.style.padding = `${spacingY/2}px ${spacingX/2}px`;
                 proximityViz.style.alignItems = groupRows ? 'center' : 'center';
                 proximityViz.style.justifyContent = groupRows ? 'center' : 'center';
             });
        }

        spacingXSlider.addEventListener('input', () => createProximityGrid(parseInt(spacingXSlider.value), parseInt(spacingYSlider.value)));
        spacingYSlider.addEventListener('input', () => createProximityGrid(parseInt(spacingXSlider.value), parseInt(spacingYSlider.value)));

        // Initial Proximity render
        createProximityGrid(parseInt(spacingXSlider.value), parseInt(spacingYSlider.value));


        // --- Similarity Visualization ---
        const similarityViz = document.querySelector('.similarity-viz');
        const similarityTypeSelect = document.getElementById('similarity-type');

        function createSimilarityGrid(rows = 5, cols = 5, criterion) {
            similarityViz.innerHTML = ''; // Clear previous grid
            similarityViz.style.gridTemplateColumns = `repeat(${cols}, auto)`;
            similarityViz.style.gap = '10px'; // Ensure gap is set

            const elements = [];

            for (let i = 0; i < rows; i++) {
                for (let j = 0; j < cols; j++) {
                    const element = document.createElement('div');
                    element.classList.add('similarity-element');

                    // Apply similarity based on criterion and pattern
                    // Use a diagonal pattern for more interesting grouping
                    const isAlternate = (i + j) % 2 === 0;

                    // Reset classes/styles before applying new ones
                    element.className = 'similarity-element';
                    element.style.backgroundColor = '';
                    element.style.width = '';
                    element.style.height = '';
                    element.style.border = ''; // Clear triangle border
                    element.style.borderRadius = ''; // Clear triangle border radius

                    if (criterion === 'color') {
                         element.classList.add(isAlternate ? 'color-secondary' : 'color-accent');
                         element.style.backgroundColor = ''; // Let CSS class define color
                    } else if (criterion === 'shape') {
                        if (isAlternate) {
                             element.classList.add('shape-square');
                        } else {
                            element.classList.add('shape-triangle');
                        }
                        element.style.backgroundColor = var_primary_color; // Use JS variable for consistency
                         if (isAlternate) { // Square uses background-color
                             element.style.borderBottomColor = ''; // Clear triangle border if any
                             element.style.borderRadius = '4px'; // Apply square border radius
                         } else { // Triangle uses border-bottom-color
                             element.style.backgroundColor = 'transparent'; // Triangles have no background
                             element.style.borderBottomColor = var_primary_color;
                         }


                    } else if (criterion === 'size') {
                         element.classList.add(isAlternate ? 'size-large' : 'size-small');
                          element.style.backgroundColor = var_primary_color; // Default color
                    } else { // Default: all same color, same shape, same size
                         element.style.backgroundColor = var_primary_color;
                    }


                    elements.push(element);
                }
            }
             // Append all elements together for smoother rendering
             elements.forEach(el => similarityViz.appendChild(el));

        }

         // Helper to get CSS variable in JS
         const getCssVar = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
         const var_primary_color = getCssVar('--primary-color');
         const var_secondary_color = getCssVar('--secondary-color');
         const var_accent_color = getCssVar('--accent-color');


        similarityTypeSelect.addEventListener('change', (event) => {
            createSimilarityGrid(5, 5, event.target.value);
        });

        // Initial Similarity render
        createSimilarityGrid(5, 5, similarityTypeSelect.value);


         // --- Closure Visualization ---
        const closureViz = document.querySelector('.closure-viz');
        const closureCompleteCheckbox = document.getElementById('closure-complete');

        function createClosureShapes(complete) {
            closureViz.innerHTML = ''; // Clear previous shapes

            // Circle
            const circle = document.createElement('div');
            circle.classList.add('closure-shape', 'circle');
            if (complete) {
                circle.classList.add('complete');
            }
            closureViz.appendChild(circle);

             // Square
            const square = document.createElement('div');
            square.classList.add('closure-shape', 'square');
             if (complete) {
                 square.classList.add('complete');
            }
            closureViz.appendChild(square);
        }

        closureCompleteCheckbox.addEventListener('change', (event) => {
            createClosureShapes(event.target.checked);
        });

        // Initial Closure render
        createClosureShapes(closureCompleteCheckbox.checked);

    });
</script>