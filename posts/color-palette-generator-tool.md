---
title: "מגרש משחקים של צבעים"
english_slug: color-palette-generator-tool
category: "גרפיקה ועיצוב"
tags:
  - צבע
  - עיצוב
  - אינטראקטיבי
  - סימולציה
  - יצירה
---
# מגרש משחקים של צבעים

צאו למסע גילוי קסום בעולם הצבעים! כאן תוכלו לשחק, להתנסות וליצור פלטות צבעים מרהיבות בלחיצת כפתור. בחרו צבע בסיס וצפו כיצד המערכת יוצרת עבורכם, כאילו בקסם, פלטות צבעים מונוכרומטיות, אנלוגיות וטריאדיות הרמוניות. זה הזמן לחקור את יחסי הגומלין בין צבעים ולמצוא את השילובים המושלמים לפרויקט הבא שלכם, או סתם בשביל הכיף!

<div id="app">
    <div class="input-section">
        <label for="baseColor">בחרו את צבע ההתחלה שלכם:</label>
        <div class="color-input-wrapper">
             <input type="color" id="baseColor" value="#3498db">
             <span id="baseColorValue" class="hex-code">#3498DB</span>
        </div>
    </div>

    <div class="palettes-section">
        <div class="palette-container">
            <h3>פלטה מונוכרומטית: גוונים שקטים</h3>
            <p class="palette-description">וריאציות שונות של בהירות ורוויה של צבע אחד.</p>
            <div class="palette" id="monochromaticPalette">
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
            </div>
        </div>

        <div class="palette-container">
            <h3>פלטה אנלוגית: הרמוניה טבעית</h3>
            <p class="palette-description">צבעים סמוכים זה לזה בגלגל הצבעים.</p>
            <div class="palette" id="analogousPalette">
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
                <div class="color-swatch" data-color=""></div>
            </div>
        </div>

        <div class="palette-container">
            <h3>פלטה טריאדית: דינמיות ותוססת</h3>
             <p class="palette-description">שלושה צבעים המרוחקים באופן שווה על גלגל הצבעים.</p>
            <div class="palette" id="triadicPalette">
                 <div class="color-swatch" data-color=""></div>
                 <div class="color-swatch" data-color=""></div>
                 <div class="color-swatch" data-color=""></div>
                 <div class="color-swatch" data-color=""></div>
                 <div class="color-swatch" data-color=""></div>
            </div>
        </div>
    </div>
     <div class="feedback-message" id="feedbackMessage">הקוד הועתק!</div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        background: linear-gradient(135deg, #f4f7f6 0%, #e0e9f0 100%); /* Softer gradient background */
        color: #333;
        padding: 20px;
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1 {
        color: #2c3e50;
        text-align: center;
        font-weight: 700;
        margin-bottom: 15px;
    }

    h3 {
         color: #34495e;
         font-weight: 500;
         margin-top: 0;
         margin-bottom: 10px; /* Reduced margin */
         font-size: 1.25em;
    }

    p {
        text-align: center;
        margin-bottom: 30px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        color: #555;
    }

    .palette-description {
        font-size: 0.9em;
        color: #777;
        margin-bottom: 20px;
        text-align: center;
        min-height: 30px; /* Reserve space */
    }


    #app {
        background-color: #ffffff;
        border-radius: 16px; /* More rounded corners */
        padding: 30px 40px; /* More padding */
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); /* Deeper shadow */
        max-width: 900px; /* Wider max width */
        width: 100%;
        margin: 20px auto;
        box-sizing: border-box;
    }

    .input-section {
        text-align: center;
        margin-bottom: 40px;
        padding-bottom: 30px;
        border-bottom: 1px solid #eee; /* Separator */
    }

    .input-section label {
        font-size: 1.2em; /* Larger label */
        color: #555;
        margin-bottom: 15px; /* More space */
        display: block;
        font-weight: 500;
    }

     .color-input-wrapper {
         display: flex;
         align-items: center;
         justify-content: center;
         gap: 20px; /* Space between picker and hex code */
     }

    .input-section input[type="color"] {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        border: none;
        width: 65px; /* Slightly larger picker */
        height: 65px;
        border-radius: 50%;
        overflow: hidden;
        cursor: pointer;
        padding: 0;
        outline: none;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Add shadow transition */
        vertical-align: middle;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Add shadow to picker */
    }

    .input-section input[type="color"]::-webkit-color-swatch-wrapper {
        padding: 0;
    }

    .input-section input[type="color"]::-webkit-color-swatch {
        border: none;
        border-radius: 50%;
    }

    .input-section input[type="color"]::-moz-color-swatch-wrapper {
         padding: 0;
    }

     .input-section input[type="color"]::-moz-color-swatch {
        border: none;
        border-radius: 50%;
    }

    .input-section input[type="color"]:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }
     .input-section input[type="color"]:active {
        transform: scale(1.05);
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
    }


    #baseColorValue {
        display: inline-block;
        font-size: 1.2em; /* Larger font size */
        font-weight: 700; /* Bolder */
        color: #2c3e50;
        vertical-align: middle;
        min-width: 80px; /* Reserve space */
    }

    .palettes-section {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Allow slightly wider columns */
        gap: 30px;
        margin-top: 30px;
    }

    .palette-container {
        background-color: #fefefe; /* Lighter background for containers */
        border-radius: 10px; /* Slightly more rounded */
        padding: 25px; /* More padding */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Enhanced shadow */
        text-align: center;
        transition: transform 0.3s ease-in-out; /* Add transition */
    }

     .palette-container:hover {
        transform: translateY(-5px); /* Lift on hover */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
     }


    .palette {
        display: flex;
        justify-content: center;
        gap: 12px; /* Slightly larger gap */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .color-swatch {
        width: 50px; /* Slightly larger swatches */
        height: 50px;
        border-radius: 8px; /* More rounded swatch corners */
        background-color: #eee; /* Placeholder */
        transition: background-color 0.6s ease-out; /* Smooth color change animation */
        cursor: pointer; /* Indicate clickability */
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15); /* Swatch shadow */
        position: relative; /* For potential tooltip/feedback */
        overflow: hidden; /* For potential animation mask */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8em;
        color: rgba(255, 255, 255, 0); /* Hidden text by default */
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

     .color-swatch::before {
         content: attr(data-color); /* Display hex code from data attribute */
         position: absolute;
         top: 0;
         left: 0;
         right: 0;
         bottom: 0;
         background-color: rgba(0, 0, 0, 0.3); /* Semi-transparent overlay */
         color: white;
         display: flex;
         align-items: center;
         justify-content: center;
         opacity: 0; /* Hidden by default */
         transition: opacity 0.3s ease;
         pointer-events: none; /* Allow clicking the swatch underneath */
         direction: ltr; /* Ensure hex code is LTR */
         font-size: 0.7em;
         padding: 0 5px;
         word-break: break-all; /* Prevent overflow */
         text-align: center;
     }

    .color-swatch:hover {
         transform: translateY(-5px); /* Lift swatch on hover */
         box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }

     .color-swatch:hover::before {
         opacity: 1; /* Show hex code on hover */
     }

    .color-swatch.copied {
         animation: copied-feedback 0.6s ease-in-out; /* Animation for copy feedback */
     }

    @keyframes copied-feedback {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

     .feedback-message {
         position: fixed;
         bottom: 20px;
         left: 50%;
         transform: translateX(-50%);
         background-color: #28a745; /* Green */
         color: white;
         padding: 10px 20px;
         border-radius: 8px;
         box-shadow: 0 2px 10px rgba(0,0,0,0.2);
         z-index: 1000;
         opacity: 0;
         visibility: hidden;
         transition: opacity 0.3s ease-out, visibility 0.3s ease-out;
     }

    .feedback-message.visible {
        opacity: 1;
        visibility: visible;
    }


    #toggleExplanation {
        display: block;
        margin: 40px auto 30px auto; /* More margin */
        padding: 14px 30px; /* More padding */
        font-size: 1.1em; /* Larger font */
        color: #fff;
        background-color: #3498db;
        border: none;
        border-radius: 8px; /* More rounded */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease; /* Add box-shadow transition */
        text-align: center;
        max-width: 250px; /* Wider button */
        font-weight: 500;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    #toggleExplanation:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    #toggleExplanation:active {
        transform: translateY(0);
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    }

    .explanation {
        background-color: #ecf0f1;
        border-radius: 12px; /* More rounded */
        padding: 30px; /* More padding */
        margin: 20px auto;
        max-width: 900px; /* Matches app width */
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        display: none; /* Hidden by default */
        opacity: 0; /* For fade-in animation */
        transition: opacity 0.5s ease-out; /* Fade-in transition */
    }

     .explanation.visible {
        opacity: 1;
     }

    .explanation h3 {
        color: #2c3e50;
        margin-top: 0;
        margin-bottom: 20px; /* More space */
        text-align: right; /* RTL */
        font-weight: 700;
        font-size: 1.4em;
         border-bottom: 2px solid #bdc3c7; /* Separator */
         padding-bottom: 10px;
    }

    .explanation p {
        margin-bottom: 20px; /* More space */
        color: #555;
        text-align: right; /* RTL */
         max-width: none; /* Remove max-width inherited from general p */
    }

    .explanation ul {
        list-style: none;
        padding: 0;
        margin-top: 20px;
    }

    .explanation li {
        background-color: #ffffff;
        border: 1px solid #dcdcdc; /* Lighter border */
        border-radius: 8px; /* More rounded */
        padding: 18px; /* More padding */
        margin-bottom: 12px; /* More margin */
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.06); /* Enhanced shadow */
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        line-height: 1.8; /* Improved readability */
    }

    .explanation li:hover {
         transform: translateX(-8px); /* More pronounced shift */
         box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    .explanation li strong {
        color: #34495e;
        display: inline-block;
        margin-left: 8px; /* More space after the term */
        font-weight: 700;
        font-size: 1.1em;
    }

     /* Responsive adjustments */
    @media (max-width: 768px) {
        #app, .explanation {
            padding: 20px;
             margin: 15px auto;
        }

        .palettes-section {
            grid-template-columns: 1fr; /* Stack palettes on small screens */
            gap: 20px;
        }

        .palette {
            gap: 8px;
        }

        .color-swatch {
            width: 40px;
            height: 40px;
             font-size: 0.6em;
        }

         .color-swatch::before {
             font-size: 0.6em;
              padding: 0 3px;
         }


        .input-section {
            margin-bottom: 30px;
             padding-bottom: 20px;
        }

        .input-section label {
             font-size: 1.1em;
             margin-bottom: 10px;
        }

        .input-section input[type="color"] {
            width: 50px;
            height: 50px;
        }

         #baseColorValue {
             font-size: 1em;
         }

         #toggleExplanation {
             padding: 12px 25px;
             font-size: 1em;
             margin: 30px auto 20px auto;
             max-width: 200px;
         }

         .explanation h3 {
             font-size: 1.2em;
             margin-bottom: 15px;
         }

         .explanation li {
             padding: 15px;
             margin-bottom: 10px;
         }
         .explanation li strong {
             font-size: 1em;
         }
    }

     @media (max-width: 480px) {
         body {
             padding: 10px;
         }
          h1 {
             font-size: 1.8em;
          }
         #app, .explanation {
             padding: 15px;
             margin: 10px auto;
         }
         .palette {
             gap: 6px;
         }
         .color-swatch {
            width: 35px;
            height: 35px;
             border-radius: 5px;
         }
          .color-swatch::before {
             font-size: 0.5em;
              padding: 0 2px;
         }
     }


</style>

<button id="toggleExplanation">מה עומד מאחורי הצבעים?</button>

<div class="explanation" id="explanationContent">
    <h3>המדריך הקצר להרמוניית צבעים</h3>
    <p>מאחורי כל פלטת צבעים מוצלחת עומדים עקרונות של הרמוניה, המבוססים לרוב על יחסים גאומטריים בגלגל הצבעים. הבנה של סוגי פלטות שונות יכולה לעזור לכם ליצור שילובים נעימים לעין ובעלי אפקט רצוי.</p>
    <ul>
        <li>
            <strong>פלטה מונוכרומטית:</strong> פלטה זו נוצרת על ידי שימוש בגוונים, בהירויות ורמות רוויה שונות של צבע אחד בלבד. היא יוצרת מראה אחיד, רגוע ואלגנטי, ונחשבת קלה מאוד לעבודה.
        </li>
        <li>
            <strong>פלטה אנלוגית:</strong> מורכבת מצבע הבסיס ושניים עד ארבעה צבעים הסמוכים לו על גלגל הצבעים. פלטות אלו נמצאות לעיתים קרובות בטבע, ויוצרות הרמוניה נעימה, עדינה וזורמת. מומלץ לבחור צבע דומיננטי אחד ולהשתמש באחרים כתומכים או כצבעי הדגשה.
        </li>
        <li>
            <strong>פלטה טריאדית (משולשת):</strong> מורכבת משלושה צבעים המרוחקים מרחק שווה זה מזה על גלגל הצבעים (כלומר, בזווית של 120 מעלות). פלטה זו עשירה ובעלת ניגודיות גבוהה, מה שהופך אותה לדינמית ותוססת. שימוש בפלטה טריאדית דורש תשומת לב לאיזון, כאשר לרוב צבע אחד הוא הדומיננטי והשניים האחרים משמשים להדגשות.
        </li>
    </ul>
    <p>הכלי מאפשר לכם לראות את העקרונות הללו בפעולה ולהתנסות בהשפעה של בחירת צבע בסיס שונה על כל סוגי הפלטות. שחקו עם הצבעים וגלו שילובים חדשים!</p>
</div>

<script>
    // Helper function to convert Hex to HSL
    function hexToHsl(hex) {
        // Remove # if it exists
        hex = hex.replace(/^#/, '');

        // Parse hex values
        let r = parseInt(hex.substring(0, 2), 16) / 255;
        let g = parseInt(hex.substring(2, 4), 16) / 255;
        let b = parseInt(hex.substring(4, 6), 16) / 255;

        // Find greatest and smallest channel values
        let max = Math.max(r, g, b), min = Math.min(r, g, b);
        let h, s, l = (max + min) / 2;

        if (max === min) {
            h = s = 0; // achromatic
        } else {
            let d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
            switch (max) {
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }

        // Return HSL values (H in degrees 0-360, S and L in percentage 0-100)
        return [Math.round(h * 360), Math.round(s * 100), Math.round(l * 100)];
    }

    // Helper function to convert HSL to Hex
    function hslToHex(h, s, l) {
        h = h % 360; // Ensure hue is within 0-360
        if (h < 0) h += 360; // Handle negative hues
        s = Math.max(0, Math.min(100, s)) / 100; // Ensure saturation is within 0-100 and normalize
        l = Math.max(0, Math.min(100, l)) / 100; // Ensure lightness is within 0-100 and normalize

        let r, g, b;

        if (s === 0) {
            r = g = b = l; // achromatic
        } else {
            const hue2rgb = (p, q, t) => {
                if (t < 0) t += 1;
                if (t > 1) t -= 1;
                if (t < 1/6) return p + (q - p) * 6 * t;
                if (t < 1/2) return q;
                if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
                return p;
            };
            let q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            let p = 2 * l - q;
            r = hue2rgb(p, q, h/360 + 1/3);
            g = hue2rgb(p, q, h/360);
            b = hue2rgb(p, q, h/360 - 1/3);
        }

        const toHex = x => {
            const hex = Math.round(x * 255).toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        };

        return `#${toHex(r)}${toHex(g)}${toHex(b)}`.toUpperCase(); // Return uppercase hex
    }

    // Function to generate palettes
    function generatePalettes(baseColorHex) {
        const [h, s, l] = hexToHsl(baseColorHex);

        // Monochromatic Palette: Vary lightness and saturation significantly
        const monochromatic = [
             hslToHex(h, s * 0.5, l * 0.3), // Darkest, desaturated
             hslToHex(h, s * 0.7, l * 0.5), // Darker, less saturated
             hslToHex(h, s, l),             // Base
             hslToHex(h, s * 0.8, l * 0.7), // Lighter, less saturated
             hslToHex(h, s * 0.6, l * 0.9)  // Lightest, desaturated
        ].map(color => { // Ensure L and S are within bounds
            let [h, s_norm, l_norm] = hexToHsl(color); // Get normalized HSL
             return hslToHex(h, Math.max(0, Math.min(100, s_norm)), Math.max(0, Math.min(100, l_norm)));
         });


        // Analogous Palette: Vary hue +/- 30 and +/- 60 degrees
         const analogousHues = [
            h,                    // Base (center)
            (h + 30) % 360,       // +30 degrees
            (h - 30 + 360) % 360, // -30 degrees
             (h + 60) % 360,       // +60 degrees
             (h - 60 + 360) % 360 // -60 degrees
        ];
         // Order them visually from one end to the other for the UI
         analogousHues.sort((a, b) => {
             // Simple sort based on hue difference from base, wrapping around 360
             let diffA = Math.abs(a - h);
             let diffB = Math.abs(b - h);
             // Handle wrapping around 0/360
             if (diffA > 180) diffA = 360 - diffA;
             if (diffB > 180) diffB = 360 - diffB;

             // Sort based on hue value itself to get a progression in the UI
             return a - b;
         });

        const analogous = analogousHues.map(aH => hslToHex(aH, s, l));

        // Triadic Palette: 3 colors at 120 degrees, use base and two variations
        const triadic = [
             hslToHex(h, s, l),              // Base
             hslToHex((h + 120) % 360, s, l), // Color 1
             hslToHex((h + 240) % 360, s, l), // Color 2
             hslToHex(h, s * 0.8, l * 0.8),   // Darker, slightly desaturated base
              hslToHex((h + 120) % 360, s * 0.8, l * 0.8), // Darker variation of Color 1
         ].map(color => { // Ensure L and S are within bounds
            let [h, s_norm, l_norm] = hexToHsl(color); // Get normalized HSL
             return hslToHex(h, Math.max(0, Math.min(100, s_norm)), Math.max(0, Math.min(100, l_norm)));
         });


        return {
            monochromatic,
            analogous,
            triadic
        };
    }

     // Function to update the UI with generated palettes
    function updateUI(palettes) {
        const monoSwatches = document.querySelectorAll('#monochromaticPalette .color-swatch');
        const analSwatches = document.querySelectorAll('#analogousPalette .color-swatch');
        const triadicSwatches = document.querySelectorAll('#triadicPalette .color-swatch');

        // Apply colors with transition
        palettes.monochromatic.forEach((color, index) => {
            if (monoSwatches[index]) {
                 monoSwatches[index].style.backgroundColor = color;
                 monoSwatches[index].setAttribute('data-color', color); // Update data attribute for hover
             }
        });

        palettes.analogous.forEach((color, index) => {
             if (analSwatches[index]) {
                 analSwatches[index].style.backgroundColor = color;
                 analSwatches[index].setAttribute('data-color', color); // Update data attribute for hover
             }
        });

        palettes.triadic.forEach((color, index) => {
             if (triadicSwatches[index]) {
                 triadicSwatches[index].style.backgroundColor = color;
                 triadicSwatches[index].setAttribute('data-color', color); // Update data attribute for hover
             }
        });
    }

    // Copy color code to clipboard
     function copyColorToClipboard(hexColor) {
         navigator.clipboard.writeText(hexColor).then(() => {
             showFeedbackMessage("הקוד הועתק: " + hexColor);
         }).catch(err => {
             console.error('Failed to copy: ', err);
             // Fallback for older browsers or failed attempts
             const textarea = document.createElement('textarea');
             textarea.value = hexColor;
             textarea.style.position = 'fixed'; // Make it invisible
             textarea.style.opacity = 0;
             document.body.appendChild(textarea);
             textarea.focus();
             textarea.select();
             try {
                 document.execCommand('copy');
                  showFeedbackMessage("הקוד הועתק (Fallback): " + hexColor);
             } catch (err) {
                 console.error('Fallback copy failed: ', err);
                  showFeedbackMessage("ההעתקה נכשלה", true); // Indicate failure
             }
             document.body.removeChild(textarea);
         });
     }

     // Show temporary feedback message
     function showFeedbackMessage(message, isError = false) {
         const feedback = document.getElementById('feedbackMessage');
         feedback.textContent = message;
         feedback.style.backgroundColor = isError ? '#dc3545' : '#28a745'; // Red for error, green for success
         feedback.classList.add('visible');
         setTimeout(() => {
             feedback.classList.remove('visible');
         }, 2000); // Hide after 2 seconds
     }


    // Event listener for color input change
    const baseColorInput = document.getElementById('baseColor');
    const baseColorValueSpan = document.getElementById('baseColorValue');
    const colorSwatches = document.querySelectorAll('.color-swatch'); // Get all swatches

    baseColorInput.addEventListener('input', (event) => {
        const hexColor = event.target.value.toUpperCase();
        baseColorValueSpan.textContent = hexColor;
        const palettes = generatePalettes(hexColor);
        updateUI(palettes);
    });

     // Add click listener to each swatch for copying color
     colorSwatches.forEach(swatch => {
         swatch.addEventListener('click', () => {
             const colorToCopy = swatch.style.backgroundColor; // Get computed color
             // Convert RGB or other formats to Hex if necessary for display
             // A simpler approach is to rely on the data-color attribute we set
             const hexColor = swatch.getAttribute('data-color');
             if (hexColor) {
                 copyColorToClipboard(hexColor);
                  // Add a quick animation class
                 swatch.classList.add('copied');
                 setTimeout(() => {
                     swatch.classList.remove('copied');
                 }, 600); // Match animation duration
             }
         });
     });


    // Initial generation on page load
    const initialColor = baseColorInput.value;
    baseColorValueSpan.textContent = initialColor.toUpperCase();
    const initialPalettes = generatePalettes(initialColor);
    updateUI(initialPalettes);

    // Explanation toggle functionality
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationContentDiv = document.getElementById('explanationContent');

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationContentDiv.style.display === 'none' || explanationContentDiv.style.display === '';
        if (isHidden) {
            explanationContentDiv.style.display = 'block';
            // Trigger fade-in animation after display is block
            requestAnimationFrame(() => {
                 explanationContentDiv.classList.add('visible');
            });
        } else {
             explanationContentDiv.classList.remove('visible');
             // Hide element after fade-out
             setTimeout(() => {
                 explanationContentDiv.style.display = 'none';
             }, 500); // Match transition duration
        }
    });

     // Ensure explanation is hidden and not visible on initial load (CSS handles display: none, JS ensures opacity for animation)
     explanationContentDiv.style.display = 'none';
     explanationContentDiv.classList.remove('visible');


     // Polyfill for requestAnimationFrame for broader compatibility
     if (!window.requestAnimationFrame) {
         window.requestAnimationFrame = function(callback, element) {
             var lastTime = 0;
             var currTime = new Date().getTime();
             var timeToCall = Math.max(0, 16 - (currTime - lastTime));
             var id = window.setTimeout(function() { callback(currTime + timeToCall); },
               timeToCall);
             lastTime = currTime + timeToCall;
             return id;
         };
     }


</script>