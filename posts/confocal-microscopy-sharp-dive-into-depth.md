---
title: "מיקרוסקופיה קונפוקלית: צלילה חדה לתוך העומק"
english_slug: confocal-microscopy-sharp-dive-into-depth
category: "ביולוגיה"
tags: ["מיקרוסקיה", "קונפוקלי", "הדמיה", "פלואורסנציה", "אופטיקה", "הדמיה תלת-ממדית", "ביולוגיה"]
---
<h1>מיקרוסקיה קונפוקלית: צלילה חדה לתוך העומק</h1>
<p>דמיינו שאתם מנסים לצלול לעומק רקמה ביולוגית עבה ולצלם תמונה חדה להפליא של מה שקורה בפנים. במיקרוסקופ רגיל (שדה רחב), זה כמו לנסות לראות דרך ערפל - כל האור מכל העומקים מגיע בו-זמנית ויוצר תמונה מטושטשת. מיקרוסקופ קונפוקלי הוא הפתרון הקסום שמאפשר לנו "לחתוך" אופטית דרך הערפל הזה ולחשוף פרטים חדים בעומק הרקמה. בואו נראה איך זה עובד!</p>

<div class="app-container">
    <div class="views-container">
        <div class="view widefield-view">
            <h2>מיקרוסקופ שדה רחב (Widefield)</h2>
             <div class="focal-plane-indicator" data-view="widefield"></div>
            <div class="sample-layers">
                <!-- Layers simulating depth -->
                <div class="layer" data-z="0"></div>
                <div class="layer" data-z="1"></div>
                <div class="layer" data-z="2"></div>
                <div class="layer" data-z="3"></div>
                <div class="layer" data-z="4"></div>
                <div class="layer" data-z="5"></div>
            </div>
             <p class="view-description">כל העומקים מוארים ונאספים יחד - תמונה מטושטשת.</p>
        </div>
        <div class="view confocal-view">
            <h2>מיקרוסקופ קונפוקלי (Confocal)</h2>
             <div class="focal-plane-indicator" data-view="confocal"></div>
            <div class="sample-layers">
                 <!-- Layers simulating depth -->
                <div class="layer" data-z="0"></div>
                <div class="layer" data-z="1"></div>
                <div class="layer" data-z="2"></div>
                <div class="layer" data-z="3"></div>
                <div class="layer" data-z="4"></div>
                <div class="layer" data-z="5"></div>
            </div>
            <p class="view-description">רק העומק הממוקד עובר את ה-Pinhole - תמונה חדה!</p>
        </div>
    </div>

    <div class="controls">
        <label for="z-slider">מישור פוקוס (עומק Z): <span id="z-value">0</span></label>
        <input type="range" id="z-slider" min="0" max="5" value="0" step="1">
        <button id="start-z-stack">סרוק את העומק ובנה סט Z</button>
         <div id="z-stack-output" class="z-stack-output">
            <!-- Z-stack slices will appear here -->
             <p>סט ה-Z שייאסף יופיע כאן:</p>
        </div>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג את סוד הקונפוקל</button>

<div id="explanation" class="explanation-section" style="display: none;">
    <h2>הסבר מעמיק: הקסם שמאחורי מיקרוסקופיה קונפוקלית</h2>
    <p>כדי להבין את היתרון העצום של המיקרוסקופ הקונפוקלי, נצלול קודם לאתגר שהוא בא לפתור:</p>

    <h3>האתגר: ים של אורות סוררים בשדה רחב</h3>
    <p>במיקרוסקופ שדה רחב סטנדרטי, אנחנו מאירים את כל הדגימה בבת אחת (לרוב באמצעות פלואורסנציה). כל מולקולה פלואורסנטית בדגימה פולטת אור כשהיא מוארת, ללא קשר לעומק שלה. המצלמה או העין שלנו אוספות את כל האור הזה. הבעיה מתחילה כשאנחנו מנסים להתמקד בשכבה ספציפית: האור שבא מחוץ למישור הפוקוס שאנחנו רוצים לראות (מֵעֵבֶר לו ומִתַחְתָּיו) מגיע גם הוא לגלאי. האור ה"חוץ-מישורי" הזה לא ממוקד נכון על הגלאי והוא גורם לטשטוש משמעותי, ירידה חדה בניגודיות, ולמעשה "מסתיר" את הפרטים החדים במישור הפוקוס.</p>
     <p>חשבו על זה כמו לצלם תמונה ביום ערפילי - כל האובייקטים המרוחקים נראים מטושטשים ודועכים, והתמונה הכוללת מאבדת מחדותה.</p>

    <h3>הפתרון הקונפוקלי: לייזר ממוקד ודלת קסמים (Pinhole)</h3>
    <p>המיקרוסקופ הקונפוקלי מתגבר על זה באמצעות שני עקרונות גאוניים:</p>
    <ol>
        <li>**הארת נקודה:** במקום להאיר את כל שדה הראייה, לייזר ממוקד מאיר רק נקודה אחת ספציפית בתוך הדגימה, *בדיוק* במישור העומק שבו אנחנו רוצים להתמקד. המיקרוסקופ סורק את הדגימה נקודה אחר נקודה ושורה אחר שורה כדי לבנות תמונה שלמה.</li>
        <li>**סינון עם Pinhole:** האור הפלואורסנטי הנפלט מהנקודה המוארת נאסף חזרה ועובר דרך מערכת אופטית. לפני שהוא מגיע לגלאי (המצלמה), הוא חייב לעבור דרך Pinhole (חריר או "נקב פינים") - מסך אטום עם חור קטן מאוד. החור הזה ממוקם בצורה מדויקת כך ש**רק** האור שמגיע מהנקודה המוארת במישור הפוקוס יוכל לעבור דרכו.</li>
    </ol>
    <p>מה קורה לאור שבא מחוץ למישור הפוקוס? הוא אמנם נפלט גם הוא (מולקולות שהוארו בעקיפין או מאור מפוזר), אבל הוא לא ממוקד נכון על ה-Pinhole. הוא פוגע במסך האטום ונחסם! ה-Pinhole פועל כמו "מסנן מרחבי" אולטימטיבי, ומבטיח שכל פוטון שמגיע לגלאי אכן הגיע מהנקודה הספציפית והממוקדת במישור הפוקוס.</p>

    <h3>התוצאה: 'פרוסה אופטית' חדה כתער ויכולת בניית תלת-ממד</h3>
    <p>היכולת לסנן את האור ה"סורר" מחוץ למישור הפוקוס היא סוד הקסם. כל תמונה שאוסף המיקרוסקופ הקונפוקלי בעומק מסוים היא למעשה 'פרוסה אופטית' דקה וחדה להפליא של הדגימה באותו עומק, ללא הטשטוש שמגיע משכבות אחרות.</p>
    <p>על ידי איסוף סדרת פרוסות אופטיות כאלה בעומקים שונים (פעולה הנקראת סריקת Z או Z-stack), אנחנו מקבלים אוסף של תמונות שמכיל את כל המידע התלת-ממדי על הדגימה. באמצעות תוכנה מתאימה, ניתן לחבר את הפרוסות הללו יחד ולבנות מודל תלת-ממדי מרהיב של המבנה הפנימי של הדגימה ברזולוציה ובחדות שלא ניתן להשיג במיקרוסקופ שדה רחב.</p>

    <h3>לסיכום: יתרונות ושימושים מרכזיים</h3>
    <ul>
        <li>**חדות בעומק (Optical Sectioning):** הדמיה חדה של שכבות דקות בתוך דגימות עבות.</li>
        <li>**הדמיה תלת-ממדית:** בניית מודלים מרחביים מדויקים מסט פרוסות ה-Z.</li>
        <li>**ניגודיות משופרת:** סילוק אור מחוץ לפוקוס מגדיל משמעותית את היחס בין אות לרעש.</li>
        <li>**הפחתת Bleaching:** רק הנקודה המוארת במישור הפוקוס נחשפת ללייזר בעוצמה מלאה לאורך זמן.</li>
    </ul>
    <p>מיקרוסקופיה קונפוקלית היא כלי חיוני במחקר ביולוגי מתקדם, ומאפשרת לנו לראות לעומק מבנים תאיים, לנטר תהליכים דינמיים בתאים חיים, ולחקור אינטראקציות מולקולריות בתוך הסביבה הטבעית שלהן.</p>
</div>

<style>
    :root {
        --primary-color: #0056b3; /* Dark blue for accents */
        --secondary-color: #007bff; /* Bright blue */
        --success-color: #28a745; /* Green for buttons */
        --background-color: #eef2f7; /* Light blueish background */
        --card-background: #ffffff; /* White for sections/cards */
        --border-color: #d0d7de; /* Light grey border */
        --text-color: #333; /* Dark grey text */
        --shadow: 0 4px 8px rgba(0,0,0,0.1); /* Soft shadow */
        --transition-speed: 0.4s ease-out; /* Smooth transition */
        --layer-height: 180px; /* Standard height for layers container */
    }

    body {
         direction: rtl; /* Set RTL direction for Hebrew layout */
         font-family: 'Arial', sans-serif;
         line-height: 1.6;
         color: var(--text-color);
         background-color: var(--background-color);
         padding: 20px;
         margin: 0;
         text-align: right; /* Default text alignment for RTL */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center; /* Center titles for visual appeal */
        margin-bottom: 15px;
    }

    h1 {
        font-size: 2em;
        margin-bottom: 25px;
    }

    h2 {
        font-size: 1.5em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

     .view h2 { /* Smaller titles inside views */
         font-size: 1.3em;
         border-bottom: none;
         text-align: center;
     }

    p {
        margin-bottom: 15px;
    }

    .app-container {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: var(--shadow);
        direction: rtl; /* Ensure RTL layout */
    }

    .views-container {
        display: flex;
        justify-content: space-around;
        gap: 30px; /* Increased gap */
        margin-bottom: 25px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }

    .view {
        width: 48%; /* Adjusted width for gap */
        min-width: 300px; /* Ensure minimum width */
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 15px;
        background-color: #fcfcfc; /* Slightly lighter background */
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
        position: relative; /* Needed for absolute positioning of layers and indicator */
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

     @media (max-width: 768px) {
        .views-container {
            flex-direction: column;
            align-items: center;
        }
        .view {
            width: 95%;
            margin-bottom: 20px;
        }
    }

    .view-description {
        text-align: center;
        font-size: 0.9em;
        color: #555;
        margin-top: 10px;
        min-height: 3em; /* Reserve space to prevent layout shifts */
    }


    .sample-layers {
        width: 95%; /* Slightly smaller than view to allow padding */
        height: var(--layer-height); /* Fixed height */
        position: relative;
        border: 1px dashed #ccc; /* Visual guide for the sample area */
        background-color: #eee; /* Base color behind layers */
        margin-bottom: 15px;
    }

    .layer {
        position: absolute;
        top: 0;
        left: 0; /* Use left for RTL layout */
        width: 100%;
        height: 100%;
        transition: filter var(--transition-speed), opacity var(--transition-speed), transform var(--transition-speed); /* Smooth transitions */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.9em; /* Smaller font for layer number */
        font-weight: bold;
        opacity: 0.9; /* Default slight transparency */
         box-sizing: border-box; /* Include padding/border in element's total width and height */
         padding: 5px; /* Add padding inside layer */
         background-blend-mode: multiply; /* Blend background patterns */
         border-radius: 4px; /* Slight rounded corners for layers */
    }

     /* Enhanced Layer Patterns */
    .layer:nth-child(1) { background: rgba(255, 100, 100, 0.8), repeating-linear-gradient(45deg, #fdd, #fdd 8px, #fff 8px, #fff 16px); color: #a00; }
    .layer:nth-child(2) { background: rgba(100, 255, 100, 0.8), repeating-linear-gradient(-45deg, #dfd, #dfd 8px, #fff 8px, #fff 16px); color: #0a0; }
    .layer:nth-child(3) { background: rgba(100, 100, 255, 0.8), radial-gradient(circle, #ddf, #ddf 8px, #fff 8px, #fff 16px); color: #00a; }
    .layer:nth-child(4) { background: rgba(255, 255, 100, 0.8), conic-gradient(from 0deg at 50% 50%, #ffd 0deg, #ffd 60deg, #fff 60deg, #fff 120deg); color: #aa0; }
    .layer:nth-child(5) { background: rgba(100, 255, 255, 0.8), linear-gradient(to right, #dff, #dff 12px, #fff 12px, #fff 24px); color: #0aa; }
    .layer:nth-child(6) { background: rgba(255, 100, 255, 0.8), linear-gradient(to bottom, #fdf, #fdf 12px, #fff 12px, #fff 24px); color: #a0a; }

    /* Layer text */
    .layer::before {
         content: attr(data-z) ; /* Use Z value or layer number */
         position: absolute;
         bottom: 5px;
         right: 5px; /* Position in corner */
         background-color: rgba(255, 255, 255, 0.7);
         padding: 2px 5px;
         border-radius: 3px;
         font-size: 0.7em;
         color: #555;
    }

    .focal-plane-indicator {
        position: absolute;
        top: 0; /* Will be set by JS based on slider */
        right: 0; /* Use right for RTL */
        left: 0; /* Also use left to stretch across */
        height: 5px; /* Thickness of the indicator */
        background-color: var(--secondary-color); /* Blue indicator */
        z-index: 10; /* Above layers */
        pointer-events: none; /* Don't interfere with clicks */
        transition: top var(--transition-speed); /* Animate movement */
        width: 100%;
        opacity: 0.8;
    }


    .controls {
        text-align: center;
        margin-bottom: 25px;
        background-color: #f0f4f8; /* Different background for controls */
        padding: 20px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }

    .controls label {
        font-weight: bold;
        margin-left: 15px; /* Space for RTL */
        font-size: 1.1em;
        color: var(--primary-color);
    }

    #z-slider {
        width: calc(100% - 150px); /* Adjust width considering label and margin */
        max-width: 500px;
        vertical-align: middle;
        direction: ltr; /* Slider direction remains LTR */
        -webkit-appearance: none; /* Custom slider styles */
        appearance: none;
        height: 8px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
        margin-right: 15px; /* Space after slider */
    }

    #z-slider:hover {
        opacity: 1;
    }

    #z-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--primary-color);
    }

    #z-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--secondary-color);
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid var(--primary-color);
    }

    #start-z-stack {
        display: block;
        margin: 20px auto 0;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--success-color);
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

     #start-z-stack:hover:not(:disabled) {
        background-color: #218838;
        transform: translateY(-2px);
    }

     #start-z-stack:active:not(:disabled) {
        transform: translateY(0);
    }

     #start-z-stack:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }


    .z-stack-output {
        margin-top: 25px;
        padding-top: 15px;
        border-top: 1px solid var(--border-color);
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center slices */
        min-height: 80px; /* Reserve space */
        background-color: #fff;
        border-radius: 8px;
        padding: 10px;
        gap: 8px; /* Space between slices */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Inner shadow */
    }
     .z-stack-output p {
         width: 100%;
         text-align: center;
         font-style: italic;
         color: #777;
     }


    .z-slice {
        width: 60px; /* Larger slice previews */
        height: 60px;
        border: 1px solid #aaa;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: flex-end; /* Align content to bottom */
        align-items: center;
        font-size: 0.7em; /* Smaller font for label */
        color: #fff; /* White text */
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5); /* Text shadow for readability */
        background-size: cover;
        background-position: center;
        border-radius: 4px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        overflow: hidden; /* Hide layer content */
        transition: transform 0.2s ease;
        cursor: pointer; /* Indicate clickable */
    }

     .z-slice:hover {
         transform: scale(1.05); /* Slight scale on hover */
     }
     .z-slice span { /* Span for Z label */
        background-color: rgba(0,0,0,0.5);
        width: 100%;
        text-align: center;
        padding: 2px 0;
     }


    .toggle-button {
        display: block;
        width: fit-content;
        margin: 25px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--success-color);
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .toggle-button:hover {
        background-color: #218838;
         transform: translateY(-2px);
    }
     .toggle-button:active {
         transform: translateY(0);
     }


    .explanation-section {
        border: 1px solid var(--border-color);
        padding: 25px;
        border-radius: 12px;
        background-color: var(--card-background);
        margin-top: 20px;
        line-height: 1.7;
        direction: rtl;
        text-align: right;
        box-shadow: var(--shadow);
    }

    .explanation-section h2, .explanation-section h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
        text-align: right; /* Align explanation headings to the right */
        border-bottom: none; /* Remove border inside explanation */
        padding-bottom: 0;
    }

     .explanation-section h3 {
         font-size: 1.3em;
         color: #555;
     }

    .explanation-section p {
        margin-bottom: 18px;
    }

    .explanation-section ol, .explanation-section ul {
        list-style: none; /* Remove default list style */
        padding: 0;
        margin-bottom: 20px;
    }
     .explanation-section ol li {
         counter-increment: my-counter;
         margin-bottom: 10px;
         position: relative;
         padding-right: 30px; /* Space for custom bullet */
     }

     .explanation-section ol li::before {
         content: counter(my-counter) ".";
         position: absolute;
         right: 0;
         font-weight: bold;
         color: var(--secondary-color);
         width: 25px;
         text-align: center;
     }
     .explanation-section ul li {
         margin-bottom: 8px;
          position: relative;
         padding-right: 20px; /* Space for custom bullet */
     }
      .explanation-section ul li::before {
         content: '•'; /* Custom bullet point */
         position: absolute;
         right: 0;
         font-weight: bold;
         color: var(--secondary-color);
         width: 15px;
         text-align: center;
      }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const zSlider = document.getElementById('z-slider');
        const zValueSpan = document.getElementById('z-value');
        const widefieldLayers = document.querySelectorAll('.widefield-view .layer');
        const confocalLayers = document.querySelectorAll('.confocal-view .layer');
         const focalPlaneIndicators = document.querySelectorAll('.focal-plane-indicator');
        const startZStackButton = document.getElementById('start-z-stack');
        const zStackOutput = document.getElementById('z-stack-output');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationSection = document.getElementById('explanation');
         const layerHeight = parseFloat(getComputedStyle(document.querySelector('.sample-layers')).height); // Get height dynamically
         const numLayers = widefieldLayers.length; // Assume same number for both views


        const updateViews = (currentZ) => {
            zValueSpan.textContent = currentZ;

             // Position the focal plane indicator
             const indicatorPosition = (currentZ / (numLayers - 1)) * layerHeight;
             focalPlaneIndicators.forEach(indicator => {
                 indicator.style.top = `${indicatorPosition}px`;
             });


            widefieldLayers.forEach(layer => {
                const layerZ = parseInt(layer.dataset.z);
                const distance = Math.abs(layerZ - currentZ);
                // Simulate blur and dimming: greater distance = more blur and less opaque
                const maxDistance = numLayers - 1;
                const normalizedDistance = distance / maxDistance; // Normalize distance 0-1

                const blur = normalizedDistance * 10; // Max blur up to 10px
                const opacity = 1 - (normalizedDistance * 0.6); // Opacity drops to 0.4 at max distance

                layer.style.filter = `blur(${blur}px)`;
                layer.style.opacity = opacity.toFixed(2); // Keep some base opacity
                 layer.style.display = 'flex'; // Widefield always shows all layers (blurred/dimmed)
            });

            confocalLayers.forEach(layer => {
                const layerZ = parseInt(layer.dataset.z);
                const distance = Math.abs(layerZ - currentZ);
                // Simulate pinhole: only show layers *exactly* at the focal plane
                // For discrete layers, distance === 0 means in focus
                if (distance === 0) {
                    layer.style.display = 'flex'; // Show sharp layer
                    layer.style.opacity = '1';
                     layer.style.filter = 'blur(0px)'; // Ensure no blur
                     layer.style.zIndex = '2'; // Bring focused layer to front visually
                } else {
                    layer.style.display = 'none'; // Hide out-of-focus layers
                    layer.style.opacity = '0';
                     layer.style.zIndex = '1'; // Default stack order
                }
            });
        };

        // Initial view update
        const initialZ = parseInt(zSlider.value);
        updateViews(initialZ);

        // Update views on slider change
        zSlider.addEventListener('input', (event) => {
            const currentZ = parseInt(event.target.value);
            updateViews(currentZ);
        });

        // Z-stack simulation
        startZStackButton.addEventListener('click', async () => {
            zStackOutput.innerHTML = '<p>אוסף פרוסות ה-Z:</p>'; // Clear and add header
            startZStackButton.disabled = true;

            const minZ = parseInt(zSlider.min);
            const maxZ = parseInt(zSlider.max);
            const step = parseInt(zSlider.step);

            for (let z = minZ; z <= maxZ; z += step) {
                // Simulate moving focus
                zSlider.value = z;
                updateViews(z);

                // Wait briefly for the view update transition
                 await new Promise(resolve => setTimeout(resolve, 400)); // Increased delay for effect

                // Capture the confocal slice at this Z level
                const focusedConfocalLayer = Array.from(confocalLayers).find(layer => parseInt(layer.dataset.z) === z);

                 if (focusedConfocalLayer && getComputedStyle(focusedConfocalLayer).display !== 'none') {
                    // Create a visual representation of the captured slice
                    const sliceDiv = document.createElement('div');
                    sliceDiv.classList.add('z-slice');

                     // Simulate "capturing" the look of the focused layer
                    const layerStyle = getComputedStyle(focusedConfocalLayer);
                    sliceDiv.style.background = layerStyle.background;
                    sliceDiv.style.backgroundColor = layerStyle.backgroundColor; // Ensure background color is copied

                    const zLabel = document.createElement('span');
                    zLabel.textContent = `Z=${z}`;
                    sliceDiv.appendChild(zLabel);


                    zStackOutput.appendChild(sliceDiv);

                 }

                // Wait briefly before moving to the next Z
                await new Promise(resolve => setTimeout(resolve, 200));
            }

             const doneText = document.createElement('p');
             doneText.textContent = '... סט ה-Z נאסף בהצלחה! (כעת ניתן לבנות הדמיה תלת-ממדית מתוכנת).';
             doneText.style.cssText = 'width: 100%; text-align: center; margin-top: 10px; font-weight: bold; color: var(--success-color);';
             zStackOutput.appendChild(doneText);


            startZStackButton.disabled = false;
        });

        // Toggle explanation visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationSection.style.display === 'none';
            explanationSection.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג את סוד הקונפוקל';
             // Scroll to explanation if showing it (optional, but good UX)
             if (isHidden) {
                 explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
             } else {
                  // Or scroll back to the app if hiding
                 document.querySelector('.app-container').scrollIntoView({ behavior: 'smooth', block: 'start' });
             }

        });
    });
</script>
```