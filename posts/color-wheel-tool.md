---
title: "גלגל הצבעים - המעבדה המרכזית לשילובי צבעים"
english_slug: color-wheel-tool
category: "פיזיקה"
tags:
  - צבע
  - עיצוב
  - אמנות
  - אינטראקטיבי
---
# גלגל הצבעים - המעבדה המרכזית לשילובי צבעים

הצבעים הם שפה ויזואלית עוצמתית, והם אף פעם לא עובדים לבד. יש להם קשרים סודיים, סיפורים שהם מספרים יחד. גלגל הצבעים הוא המפה לאוצר הזה – הוא מגלה לנו אילו צבעים "מדברים" אחד עם השני הכי טוב, יוצרים הרמוניה או ניגודיות מרהיבה. המעבדה האינטראקטיבית הזו מזמינה אתכם להתנסות, לבחור צבע אחד, ולראות מיד אילו שילובים קסומים נולדים ממנו. בואו נשחק עם הצבעים!

<div class="color-tool-container">
    <div class="color-selector-area">
        <label for="baseColor">בחרו את צבע ההתחלה שלכם:</label>
        <input type="color" id="baseColor" value="#3498db">
        <div class="selected-color-preview">
             <div class="selected-color-display"></div>
             <div class="selected-color-hex">#3498DB</div>
        </div>
         <p class="tip">טיפ: לחצו על כל קוביית צבע למטה כדי להעתיק את קוד ה-Hex שלה!</p>
    </div>

    <div class="color-schemes">
        <h3>השילובים שנולדו מזה:</h3>
        <div class="scheme-row">
            <div class="color-box complementary" data-label="משלים"></div>
            <div class="color-label">צבע משלים</div>
        </div>
         <div class="scheme-row">
            <div class="color-box analogous-1" data-label="אנלוגי 1"></div>
            <div class="color-box analogous-2" data-label="אנלוגי 2"></div>
             <div class="color-label">אנלוגיים (שכנים קרובים)</div>
        </div>
         <div class="scheme-row">
            <div class="color-box triadic-1" data-label="טריאדי 1"></div>
             <div class="color-box triadic-2" data-label="טריאדי 2"></div>
            <div class="color-label">טריאדי (משולש מאוזן)</div>
        </div>
        <div class="scheme-row">
             <div class="color-box split-complementary-1" data-label="מפוצל משלים 1"></div>
            <div class="color-box split-complementary-2" data-label="מפוצל משלים 2"></div>
            <div class="color-label">מפוצל משלים</div>
        </div>
    </div>
</div>

<button id="toggleExplanation" aria-expanded="false">מה עשיתי פה? (הסבר)</button>

<div id="explanation" style="display: none;" aria-hidden="true">
    <h2>פיצוח סוד גלגל הצבעים</h2>
    <p>גלגל הצבעים הוא לא סתם עיגול יפהפה – הוא מפה חכמה שמראה איך צבעים קשורים זה לזה. הוא מסדר את הצבעים כמו שאנחנו רואים אותם בספקטרום, ומסביר למה צבעים מסוימים נראים מדהים יחד ואחרים פחות.</p>

    <h3>שילובי צבעים מנצחים:</h3>
    <ul>
        <li><strong>צבעים משלימים (Complementary):</strong> דמיינו שני צבעים בדיוק אחד מול השני בגלגל. הם הכי שונים שיש, והשילוב שלהם יוצר "וואו!" מיידי, ניגודיות שקשה להתעלם ממנה. מושלם כשרוצים שמשהו יבלוט!</li>
        <li><strong>צבעים אנלוגיים (Analogous):</strong> שלושה צבעים שיושבים ממש זה ליד זה בגלגל. הם כמו משפחה קרובה - דומים, הולכים טוב יחד, ויוצרים אווירה רגועה והרמונית.</li>
        <li><strong>שילוב טריאדי (Triadic):</strong> קחו משולש שווה צלעות, סובבו אותו על הגלגל, ושלושת הצבעים שתראו בקודקודי המשולש הם השילוב הטריאדי. זה שילוב שמציע ניגודיות תוססת (כי הצבעים מרוחקים יחסית), אבל עדיין מאוזנת ומעניינת.</li>
        <li><strong>שילוב מפוצל משלים (Split-Complementary):</strong> קצת יותר מתוחכם: בחרו צבע בסיס, מצאו את הצבע המשלים שלו, ובמקום להשתמש בו – השתמשו בשני הצבעים שיושבים *ליד* הצבע המשלים. זה נותן המון עניין ויזואלי וניגודיות, אבל עדינה יותר מהשילוב המשלים הרגיל.</li>
    </ul>
    <p>הכלי הזה הוא המגרש משחקים שלכם לחקור את העקרונות האלה. בחרו צבע, ראו את השילובים, וגלו איך להשתמש בכוח של הצבע בעיצוב, באמנות, או פשוט כדי להבין טוב יותר את העולם הצבעוני שלנו!</p>
</div>

<style>
    :root {
        --primary-color: #E74C3C; /* Dynamic, warm primary */
        --primary-color-dark: #C0392B;
        --text-color: #2C3E50; /* Darker, more modern text */
        --bg-color: #ECF0F1; /* Light, subtle background */
        --card-bg: #FFFFFF; /* Clean card background */
        --border-color: #BDC3C7; /* Soft border */
        --shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Softer, larger shadow */
        --hover-scale: 1.03; /* Subtle scale on hover */
        --animation-duration: 0.4s;
        --animation-ease: ease-in-out;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font stack */
        line-height: 1.7; /* Improved readability */
        color: var(--text-color);
        background-color: var(--bg-color);
        padding: 25px; /* More padding */
        direction: rtl;
        text-align: right;
        margin: 0; /* Remove default body margin */
        min-height: 100vh; /* Full viewport height */
        box-sizing: border-box;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
        position: relative; /* For potential underline animation */
    }

    .color-tool-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: var(--card-bg);
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        box-shadow: var(--shadow);
        margin-bottom: 30px; /* More space below */
        width: 100%;
        max-width: 700px; /* Max width for large screens */
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    .color-selector-area {
        margin-bottom: 40px; /* More space below selector */
        text-align: center;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .color-selector-area label {
        display: block;
        margin-bottom: 15px; /* More space below label */
        font-size: 1.2em; /* Larger font */
        font-weight: bold;
        color: var(--text-color);
    }

    .color-selector-area input[type="color"] {
        width: 90px; /* Larger picker */
        height: 90px; /* Larger picker */
        border: none;
        padding: 0;
        background: none;
        cursor: pointer;
        border-radius: 50%;
        overflow: hidden;
        outline: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow on picker */
        transition: transform 0.2s var(--animation-ease); /* Hover animation */
    }

    .color-selector-area input[type="color"]::-webkit-color-swatch-wrapper {
        padding: 0;
    }

    .color-selector-area input[type="color"]::-webkit-color-swatch {
        border: 5px solid var(--primary-color); /* Thicker border */
        border-radius: 50%;
    }

     .color-selector-area input[type="color"]::-moz-color-swatch-wrapper {
        padding: 0;
    }

    .color-selector-area input[type="color"]::-moz-color-swatch {
        border: 5px solid var(--primary-color);
        border-radius: 50%;
    }

    .color-selector-area input[type="color"]:hover {
        transform: scale(1.05); /* Scale up on hover */
    }


    .selected-color-preview {
         display: flex;
         align-items: center;
         justify-content: center;
         margin-top: 20px; /* Space above preview */
    }

    .selected-color-display {
        width: 120px; /* Wider display */
        height: 35px; /* Slightly taller */
        border-radius: 6px;
        border: 1px solid var(--border-color);
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.08);
        transition: background-color var(--animation-duration) var(--animation-ease);
        margin-left: 10px; /* Space between display and hex */
    }

     .selected-color-hex {
         font-family: 'Courier New', monospace;
         font-size: 1em; /* Slightly larger */
         color: var(--text-color);
         font-weight: bold;
     }

     .tip {
         font-size: 0.9em;
         color: #555;
         margin-top: 15px;
     }


    .color-schemes {
        width: 100%;
        max-width: 650px; /* Slightly wider scheme section */
    }

    .color-schemes h3 {
         text-align: center;
         margin-bottom: 25px; /* More space below heading */
         color: var(--text-color);
         font-size: 1.3em;
    }

    .scheme-row {
        display: flex;
        align-items: center;
        margin-bottom: 20px; /* More space between rows */
        padding: 15px 20px; /* More internal padding */
        border: 1px solid var(--border-color);
        border-radius: 8px; /* More rounded corners */
        background-color: #FAFAFA; /* Slightly lighter background */
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        flex-wrap: wrap;
        justify-content: flex-end;
        transition: transform 0.2s var(--animation-ease); /* Subtle hover animation */
    }

    .scheme-row:hover {
         transform: translateY(-3px); /* Lift slightly on hover */
         box-shadow: 0 5px 12px rgba(0,0,0,0.1);
    }

    .color-box {
        width: 55px; /* Larger boxes */
        height: 55px; /* Larger boxes */
        border-radius: 6px; /* More rounded */
        margin: 5px; /* Even margin around boxes */
        border: 1px solid var(--border-color);
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.1);
        transition: background-color var(--animation-duration) var(--animation-ease), transform 0.2s var(--animation-ease);
         flex-shrink: 0;
         cursor: pointer; /* Indicate clickable */
    }

     .color-box:hover {
         transform: scale(var(--hover-scale)); /* Scale on hover */
         border-color: var(--primary-color); /* Highlight border on hover */
     }


    .color-label {
        font-weight: bold;
        margin-right: auto;
        flex-grow: 1;
        text-align: left;
        font-size: 1.1em;
        color: var(--text-color);
    }


    button {
        display: block;
        margin: 30px auto; /* More space around button */
        padding: 14px 30px; /* Larger padding */
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        transition: background-color 0.3s var(--animation-ease), transform 0.15s var(--animation-ease), box-shadow 0.3s var(--animation-ease);
        box-shadow: var(--shadow);
        font-weight: bold;
    }

    button:hover {
        background-color: var(--primary-color-dark); /* Darker shade */
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15); /* Stronger shadow on hover */
    }

    button:active {
        transform: scale(0.98);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }

    #explanation {
        background-color: var(--card-bg);
        padding: 30px;
        border-radius: 12px;
        box-shadow: var(--shadow);
        margin-top: 30px;
        border-right: 6px solid var(--primary-color); /* Thicker highlight */
        max-width: 700px; /* Match container width */
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
         transition: opacity var(--animation-duration) var(--animation-ease); /* Fade transition */
    }

     #explanation h2 {
         margin-top: 0;
         border-bottom: 1px solid var(--border-color); /* Separator */
         padding-bottom: 10px;
         margin-bottom: 20px;
     }

      #explanation h3 {
          margin-top: 20px;
          margin-bottom: 10px;
          color: var(--text-color);
      }


     #explanation ul {
         padding-right: 25px; /* Adjust padding for RTL list */
         margin-bottom: 20px;
     }

     #explanation li {
         margin-bottom: 12px; /* More space between list items */
         line-height: 1.8;
     }

     #explanation strong {
         color: var(--primary-color-dark);
     }


    @media (max-width: 650px) {
         .color-tool-container, #explanation {
              padding: 20px; /* Adjust padding on smaller screens */
         }

         .scheme-row {
             flex-direction: column;
             align-items: flex-end;
             padding: 15px;
         }

         .scheme-row .color-box {
             margin: 4px 0; /* Stack boxes vertically */
              width: 45px; /* Slightly smaller boxes */
              height: 45px;
         }

         .color-label {
             margin-right: 0;
             margin-top: 10px;
             text-align: right;
             width: 100%;
         }

         .selected-color-preview {
              flex-direction: column; /* Stack preview elements */
         }

         .selected-color-display {
             margin-left: 0;
             margin-bottom: 10px;
         }

         .color-selector-area label {
             text-align: center;
         }
    }

     /* Animation for showing explanation */
     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(10px); }
         to { opacity: 1; transform: translateY(0); }
     }

    #explanation[style*="display: block"] { /* Target when display is block */
        animation: fadeIn var(--animation-duration) var(--animation-ease) forwards;
    }


</style>

<script>
    // --- Color Conversion Functions (Hex, RGB, HSL) ---
    // These are necessary to easily manipulate colors based on hue, saturation, lightness.

    // Convert Hex to RGB
    function hexToRgb(hex) {
        const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
        hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

    // Convert RGB to HSL
    function rgbToHsl(r, g, b) {
        r /= 255;
        g /= 255;
        b /= 255;
        const max = Math.max(r, g, b);
        const min = Math.min(r, g, b);
        let h, s, l = (max + min) / 2;

        if (max === min) {
            h = s = 0; // achromatic
        } else {
            const d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
            switch (max) {
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }

        return { h: h * 360, s: s * 100, l: l * 100 };
    }

    // Convert HSL to Hex
    function hslToHex(h, s, l) {
         s /= 100;
         l /= 100;
         const k = n => (n + h / 30) % 12;
         const a = s * Math.min(l, 1 - l);
         const f = n =>
            l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(k(n) - 9, 1)));
         const componentToHex = c => {
            const hex = Math.round(c * 255).toString(16);
            return hex.length === 1 ? "0" + hex : hex;
         };
        return "#" + componentToHex(f(0)) + componentToHex(f(8)) + componentToHex(f(4));
    }


    // --- Color Scheme Calculation ---
    function calculateSchemes(hexColor) {
        const rgb = hexToRgb(hexColor);
        if (!rgb) return {};

        const hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
        const h = hsl.h;
        const s = hsl.s;
        const l = hsl.l;

        // Ensure hue is positive and within 0-360
        const normalizeHue = (hue) => (hue % 360 + 360) % 360;

        const schemes = {};

        // Complementary: Hue + 180
        schemes.complementary = hslToHex(normalizeHue(h + 180), s, l);

        // Analogous: Hue +/ 30 degrees (common)
        schemes.analogous1 = hslToHex(normalizeHue(h + 30), s, l);
        schemes.analogous2 = hslToHex(normalizeHue(h - 30), s, l);

        // Triadic: Hue +/ 120 degrees
        schemes.triadic1 = hslToHex(normalizeHue(h + 120), s, l);
        schemes.triadic2 = hslToHex(normalizeHue(h - 120), s, l);

        // Split Complementary: Hue + 180 +/- 30 degrees
        // A common variation uses +/- 30 from complementary, not necessarily exactly 150/210 from base. Let's stick to the original structure logic (150/210 from base) for now as it matches the original code's intent implicit in the -30/+30 structure around +180.
         schemes.splitComplementary1 = hslToHex(normalizeHue(h + 180 - 30), s, l); // 150 deg from base
         schemes.splitComplementary2 = hslToHex(normalizeHue(h + 180 + 30), s, l); // 210 deg from base


        return schemes;
    }

    // --- Update UI ---
    const baseColorInput = document.getElementById('baseColor');
    const selectedColorDisplay = document.querySelector('.selected-color-display');
    const selectedColorHex = document.querySelector('.selected-color-hex');
    const colorBoxes = document.querySelectorAll('.color-box');
     const root = document.documentElement; // For CSS variables

    // Mapping from JS scheme names (camelCase) to HTML class names (kebab-case)
    const schemeNameToClassMap = {
        complementary: 'complementary',
        analogous1: 'analogous-1',
        analogous2: 'analogous-2',
        triadic1: 'triadic-1',
        triadic2: 'triadic-2',
        splitComplementary1: 'split-complementary-1',
        splitComplementary2: 'split-complementary-2'
    };

    function updateColors(event) {
        const selectedHex = event.target.value.toUpperCase(); // Ensure uppercase
        selectedColorDisplay.style.backgroundColor = selectedHex;
        selectedColorHex.textContent = selectedHex;

        // Update primary color CSS variable based on the selected color's hue
        const rgb = hexToRgb(selectedHex);
        if (rgb) {
            const hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
             // Use a bright, saturated version of the chosen color's hue for UI elements
             const uiPrimary = hslToHex(hsl.h, 80, 55); // Example: 80% Sat, 55% Light
             const uiPrimaryDark = hslToHex(hsl.h, 80, 45); // Example: 80% Sat, 45% Light

            root.style.setProperty('--primary-color', uiPrimary);
            root.style.setProperty('--primary-color-dark', uiPrimaryDark);
             // The color picker border is styled using --primary-color in CSS
        }


        const schemes = calculateSchemes(selectedHex);

        for (const [schemeName, hexColor] of Object.entries(schemes)) {
             const className = schemeNameToClassMap[schemeName];
             if (className) {
                 const box = document.querySelector(`.color-box.${className}`);
                 if (box) {
                     box.style.backgroundColor = hexColor;
                      box.setAttribute('data-hex', hexColor.toUpperCase()); // Store hex for copying/tooltip
                      // Add title attribute for simple tooltip
                      const label = box.getAttribute('data-label') || 'צבע';
                      box.setAttribute('title', `${label}: ${hexColor.toUpperCase()}`);
                 }
             }
        }
    }

    // --- Click to Copy Hex Code ---
    function copyHexToClipboard(event) {
        const hex = event.target.getAttribute('data-hex');
        if (hex) {
            navigator.clipboard.writeText(hex).then(() => {
                // Optional: Add a visual feedback (e.g., temporary text change, toast notification)
                console.log('Hex code copied: ' + hex); // For debugging
                 const originalTitle = event.target.getAttribute('title');
                 event.target.setAttribute('title', 'הועתק!');
                 setTimeout(() => {
                     event.target.setAttribute('title', originalTitle);
                 }, 1000); // Restore original title after 1 second
            }).catch(err => {
                console.error('Failed to copy: ', err);
                 const originalTitle = event.target.getAttribute('title');
                 event.target.setAttribute('title', 'שגיאת העתקה');
                  setTimeout(() => {
                     event.target.setAttribute('title', originalTitle);
                 }, 1000);
            });
        }
    }


    // --- Explanation Toggle ---
    const toggleButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');

    toggleButton.addEventListener('click', function() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר (פיצוח סוד גלגל הצבעים)' : 'מה עשיתי פה? (הסבר)';
         toggleButton.setAttribute('aria-expanded', !isHidden);
         explanationDiv.setAttribute('aria-hidden', isHidden);
    });


    // --- Initialize ---
    // Initial update on page load
    updateColors({ target: baseColorInput });

    // Listen for color changes
    baseColorInput.addEventListener('input', updateColors); // Use 'input' for live update

     // Add click listener to color boxes for copying hex
    colorBoxes.forEach(box => {
        box.addEventListener('click', copyHexToClipboard);
         // Add initial title attribute for the tooltip functionality
          const label = box.getAttribute('data-label') || 'צבע';
          box.setAttribute('title', `${label}: ...`); // Placeholder, will be updated
    });

     // Update titles after initial color calculation
     requestAnimationFrame(() => { // Ensure DOM is ready after initial update
         colorBoxes.forEach(box => {
             const hex = box.getAttribute('data-hex');
              if(hex) {
                 const label = box.getAttribute('data-label') || 'צבע';
                 box.setAttribute('title', `${label}: ${hex}`);
              }
         });
     });


</script>