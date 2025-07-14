---
title: "קסם הצבע: מסך מול דפוס (RGB נגד CMYK)"
english_slug: color-magic-screen-vs-print-rgb-vs-cmyk
category: "אמנות ועיצוב / עיצוב גרפי"
tags:
  - צבע
  - RGB
  - CMYK
  - ערבוב צבעים
  - אופטיקה
  - עיצוב דיגיטלי
  - עיצוב לדפוס
---
<h1>קסם הצבע: מסך מול דפוס (RGB נגד CMYK)</h1>
<p class="intro-text">היי, מעצב/ת, אמן/ית, או סתם סקרן/ית צבע! נתקלת פעם בעיצוב שנראה לוהט על המסך, אבל יצא מהמדפסת כאילו עבר... משהו? זה לא באג במערכת, זו פשוט הפיזיקה של הצבע בפעולה. מוכנים לשחק ולגלות את ההבדל העצום בין איך שאור מתנהג לבין איך שדיו מתנהג?</p>

<div class="color-mixer-container">
  <div class="mixer-section rgb-mixer">
    <h2>צבעי אור (RGB)</h2>
    <p class="model-description">מודל חיבורי (Additive) - מתחילים מחושך, מוסיפים אור.</p>
    <div class="color-display rgb-display">
        <div class="color-circle red-circle"></div>
        <div class="color-circle green-circle"></div>
        <div class="color-circle blue-circle"></div>
        <div class="result-overlay"></div> <!-- To show the final calculated color or simply for styling -->
    </div>
    <div class="sliders">
      <label for="rgb-r">אדום (R): <span id="rgb-r-value">0</span></label>
      <input type="range" id="rgb-r" min="0" max="255" value="0">
      <label for="rgb-g">ירוק (G): <span id="rgb-g-value">0</span></label>
      <input type="range" id="rgb-g" min="0" max="255" value="0">
      <label for="rgb-b">כחול (B): <span id="rgb-b-value">0</span></label>
      <input type="range" id="rgb-b" min="0" max="255" value="0">
    </div>
     <div class="actions">
         <button class="reset-button" data-target="rgb">איפוס RGB</button>
     </div>
  </div>

  <div class="mixer-section cmyk-mixer">
    <h2>צבעי דפוס (CMYK)</h2>
    <p class="model-description">מודל חיסורי (Subtractive) - מתחילים מלבן, "בולעים" אור עם דיו.</p>
    <div class="color-display cmyk-display">
        <div class="color-circle cyan-circle"></div>
        <div class="color-circle magenta-circle"></div>
        <div class="color-circle yellow-circle"></div>
        <div class="color-circle black-circle"></div>
         <div class="result-overlay"></div> <!-- To show the final calculated color or simply for styling -->
    </div>
    <div class="sliders">
      <label for="cmyk-c">ציאן (C): <span id="cmyk-c-value">0</span>%</label>
      <input type="range" id="cmyk-c" min="0" max="100" value="0">
      <label for="cmyk-m">מג'נטה (M): <span id="cmyk-m-value">0</span>%</label>
      <input type="range" id="cmyk-m" min="0" max="100" value="0">
      <label for="cmyk-y">צהוב (Y): <span id="cmyk-y-value">0</span>%</label>
      <input type="range" id="cmyk-y" min="0" max="100" value="0">
      <label for="cmyk-k">שחור (K): <span id="cmyk-k-value">0</span>%</label>
      <input type="range" id="cmyk-k" min="0" max="100" value="0">
    </div>
     <div class="actions">
        <button class="reset-button" data-target="cmyk">איפוס CMYK</button>
    </div>
  </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --background-light: #f8f9fa;
        --card-background: #ffffff;
        --text-color: #343a40;
        --border-color: #dee2e6;
        --rgb-red: #ff0000;
        --rgb-green: #00ff00;
        --rgb-blue: #0000ff;
        --cmyk-cyan: #00ffff;
        --cmyk-magenta: #ff00ff;
        --cmyk-yellow: #ffff00;
        --cmyk-black: #000000;
    }

    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* For Hebrew layout */
        text-align: right; /* For Hebrew text alignment */
    }

    h1, h2, h3 {
        color: #212529; /* Darker heading color */
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2em;
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 10px;
        display: inline-block;
        margin-right: auto;
        margin-left: auto;
        width: auto; /* Adjust width */
        max-width: 100%;
    }

    p.intro-text {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 40px;
        color: var(--secondary-color);
        max-width: 800px;
        margin-right: auto;
        margin-left: auto;
    }

    .color-mixer-container {
        display: flex;
        justify-content: center; /* Center mixers */
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        margin-bottom: 40px;
    }

    .mixer-section {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Added subtle shadow */
        padding: 30px; /* Increased padding */
        border-radius: 12px; /* More rounded corners */
        width: 320px; /* Slightly wider */
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transitions */
    }

     .mixer-section:hover {
         transform: translateY(-5px); /* Lift slightly on hover */
         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Deeper shadow on hover */
     }

    .mixer-section h2 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.5em;
        color: var(--primary-color);
    }

    .model-description {
        font-style: italic;
        color: var(--secondary-color);
        text-align: center;
        margin-bottom: 25px; /* Space below description */
        font-size: 0.95em;
    }


    .color-display {
        width: 200px; /* Larger circles */
        height: 200px;
        border: 3px solid #000; /* Thicker border */
        margin: 0 auto 30px auto;
        border-radius: 50%; /* Still circles */
        position: relative; /* For absolute positioning of circles inside */
        overflow: hidden; /* Clip circles to the display bounds */
        display: flex; /* Use flex for centering circles */
        justify-content: center;
        align-items: center;
    }

    .rgb-display {
         background-color: #000; /* Black background for RGB */
         border-color: #333;
    }

     .cmyk-display {
         background-color: #fff; /* White background for CMYK */
         border-color: #ccc;
     }


    .color-circle {
        position: absolute;
        width: 100%; /* Circles fill the display area */
        height: 100%;
        border-radius: 50%;
        mix-blend-mode: screen; /* Additive mixing for RGB */
        opacity: 0; /* Start transparent */
        transition: opacity 0.1s ease-out; /* Smooth transition */
    }

    .cmyk-display .color-circle {
        mix-blend-mode: multiply; /* Subtractive mixing for CMYK */
    }

    .red-circle { background-color: var(--rgb-red); }
    .green-circle { background-color: var(--rgb-green); }
    .blue-circle { background-color: var(--rgb-blue); }

    .cyan-circle { background-color: var(--cmyk-cyan); }
    .magenta-circle { background-color: var(--cmyk-magenta); }
    .yellow-circle { background-color: var(--cmyk-yellow); }
    .black-circle { background-color: var(--cmyk-black); } /* Black circle */


    .sliders {
        width: 100%;
        margin-bottom: 20px;
    }

    .sliders label {
        display: flex;
        justify-content: space-between;
        align-items: center; /* Vertically align */
        margin-top: 15px; /* More space between sliders */
        width: 100%;
        font-weight: bold;
        color: #555;
    }

    .sliders label span {
        direction: ltr; /* Ensure numbers are LTR */
        font-weight: normal;
        color: var(--text-color);
        min-width: 30px; /* Reserve space for value */
        text-align: left; /* Align value to left */
    }

    .sliders input[type="range"] {
        display: block;
        width: 100%;
        margin-top: 5px;
        -webkit-appearance: none; /* Override default appearance */
        appearance: none;
        background: #ddd; /* Track background */
        border-radius: 5px;
        height: 8px; /* Track thickness */
        outline: none;
        transition: opacity .2s;
    }

    .sliders input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Thumb size */
        height: 20px;
        background: var(--primary-color); /* Thumb color */
        border-radius: 50%;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .sliders input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--primary-color);
        border-radius: 50%;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .sliders input[type="range"]:hover::-webkit-slider-thumb {
        background: var(--primary-color); /* Keep same on hover */
        transform: scale(1.1); /* Slightly enlarge thumb on hover */
    }
    .sliders input[type="range"]:hover::-moz-range-thumb {
        background: var(--primary-color);
        transform: scale(1.1);
    }

    .actions {
        width: 100%;
        text-align: center;
        margin-top: 15px;
    }

    .reset-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        background-color: var(--secondary-color);
        color: white;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .reset-button:hover {
        background-color: #5a6268;
        transform: translateY(-2px);
    }

    .reset-button:active {
         transform: translateY(0);
    }


  #toggle-explanation {
    display: block;
    margin: 40px auto 20px auto; /* More vertical space */
    padding: 12px 25px; /* Slightly larger button */
    font-size: 1.1em; /* Larger text */
    cursor: pointer;
    border: none;
    background-color: var(--primary-color);
    color: white;
    border-radius: 6px; /* More rounded */
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
  }

  #toggle-explanation:hover {
      background-color: #0056b3;
      transform: translateY(-2px);
  }
   #toggle-explanation:active {
         transform: translateY(0);
    }


  #explanation {
    background-color: #e9ecef;
    padding: 30px; /* Increased padding */
    border-radius: 12px; /* More rounded */
    margin-top: 20px;
    direction: rtl;
    text-align: right;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05); /* Inner shadow */
    border: 1px solid #ced4da;
  }

  #explanation h2,
  #explanation h3 {
    text-align: right; /* Align explanation headings to the right */
    color: #343a40;
    margin-bottom: 15px;
    border-bottom: 1px dashed #ccc; /* Add a subtle separator */
    padding-bottom: 8px;
  }

   #explanation h2 {
       text-align: center; /* Main explanation title centered */
        border-bottom: none;
        padding-bottom: 0;
   }


  #explanation h3 {
      margin-top: 25px;
      margin-bottom: 10px;
      color: #495057;
      font-size: 1.2em;
  }

  #explanation p,
  #explanation ul {
    line-height: 1.8; /* More comfortable reading */
    margin-bottom: 18px; /* More space after paragraphs */
    font-size: 1em;
  }

   #explanation ul {
       list-style-type: disc;
       padding-right: 25px; /* Increased padding for list */
   }

   #explanation ul li {
       margin-bottom: 10px;
   }

    /* Add responsive adjustments */
    @media (max-width: 768px) {
        .color-mixer-container {
            flex-direction: column;
            align-items: center;
        }

        .mixer-section {
            width: 95%; /* Allow sections to take more width */
            max-width: 350px; /* Max width on smaller screens */
        }

        h1 {
            font-size: 1.8em;
        }

        p.intro-text {
            font-size: 1em;
        }

         #toggle-explanation {
             width: 95%;
             box-sizing: border-box;
             font-size: 1em;
         }
         #explanation {
             padding: 20px;
         }
    }

</style>

<button id="toggle-explanation">רוצים לדעת יותר? הצגת הסבר</button>

<div id="explanation" style="display: none;">
  <h2>קסם הצבע: אור מול דפוס - ההסבר המלא</h2>
  <p>עכשיו ששיחקתם קצת עם המיקסרים, בואו נבין לעומק למה ראיתם את ההבדלים האלה ואיך זה משפיע על העבודה שלכם.</p>

  <h3>מסכי הקסם: צבעי אור (RGB)</h3>
  <p>דמיינו שאתם בחדר חשוך לגמרי. הפעלתם פנס אדום, פנס ירוק ופנס כחול. כשהאורות האלה מתערבבים, הם יוצרים צבעים חדשים. ככה בדיוק עובד מסך המחשב, הטלפון או הטלוויזיה שלכם! כל פיקסל במסך מורכב משלושה "פינסים" קטנטנים: אדום (Red), ירוק (Green) וכחול (Blue). כשאתם מגבירים את עוצמת ההארה של הפינסים האלה, אתם "מוסיפים" אור, ולכן קוראים לזה מודל **חיבורי (Additive)**.</p>
  <ul>
    <li>**נקודת התחלה:** חושך מוחלט (מסך כבוי - שחור).</li>
    <li>**מה קורה כשמוסיפים?** מוסיפים אור! הצבע הופך בהיר יותר.</li>
    <li>**השילוש הקדוש:** אדום + ירוק = צהוב, אדום + כחול = מג'נטה, ירוק + כחול = ציאן.</li>
    <li>**שיא הבהירות:** אדום + ירוק + כחול בעוצמה מלאה = **לבן מבריק!**</li>
    <li>**שימוש עיקרי:** כל מה שנועד לצפייה על מסך - אתרים, אפליקציות, סרטונים, מצגות דיגיטליות.</li>
  </ul>

  <h3>עולם הדיו: צבעי דפוס (CMYK)</h3>
  <p>עכשיו דמיינו שיש לכם דף נייר לבן. נייר לבן מחזיר אלינו כמעט את כל האור שפוגע בו. כשאתם שמים עליו דיו, הדיו הזה "בולע" או "מחְסִיר" חלק מהאור שפוגע בנייר, ואנחנו רואים את הצבע שנשאר. זו הסיבה שזה נקרא מודל **חיסורי (Subtractive)**. הדיו הסטנדרטי לדפוס מגיע בארבעה צבעים: ציאן (Cyan), מג'נטה (Magenta), צהוב (Yellow), ולפעמים גם שחור (Key/Black), שיוצרים יחד את ראשי התיבות CMYK.</p>
    <ul>
    <li>**נקודת התחלה:** משטח מחזיר אור (נייר לבן).</li>
    <li>**מה קורה כשמוסיפים?** מוסיפים דיו! הדיו בולע אור, והצבע שמוחזר לעין כהה יותר.</li>
    <li>**השילוש החסר:** ציאן + מג'נטה = כחול כהה, ציאן + צהוב = ירוק כהה, מג'נטה + צהוב = אדום כהה.</li>
    <li>**שיא הכהות:** ציאן + מג'נטה + צהוב תיאורטית אמורים לתת שחור, אבל בפועל לרוב מקבלים חום עכור. הוספת דיו **שחור (K)** חיונית כדי לקבל שחור עשיר ועמוק, לחסוך בדיו הצבעוני, ולאפשר הדפסת טקסט שחור חד. ערבוב מלא של CMY+K נותן **שחור עמוק**.</li>
    <li>**שימוש עיקרי:** כל מה שמודפס - ספרים, מגזינים, כרטיסי ביקור, פליירים, אריזות.</li>
  </ul>

  <h3>אז למה הצבעים נראים אחרת? ה"גאמוט" (טווח צבעים)</h3>
  <p>ההבדל המהותי בין מודל הוספת אור (RGB) למודל בולע אור (CMYK) הוא הסיבה לפערים. מסכי RGB יכולים להציג טווח צבעים גדול ובוהק יותר (Gamut) ממה שניתן להשיג עם דיו CMYK סטנדרטי על נייר. צבעים כמו ירוקים נאונים, כחולים חשמליים או סגולים זרחניים שפגשתם על המסך פשוט לא קיימים בטווח הצבעים של CMYK. כשמעצבים קובץ ב-RGB ושולחים אותו להדפסה במדפסת CMYK, הצבעים האלה יומרו אוטומטית (או שתומרו אותם ידנית בתוכנת העיצוב), ולרוב ייראו פחות רוויים, עמומים או פשוט שונים.</p>
  <p> **המסקנה למעצבים:** תמיד עבדו במודל הצבע המתאים ליעד הסופי! RGB לדיגיטל, CMYK לדפוס. זה ימנע הרבה הפתעות ויתסכולים מיותרים.</p>

</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Helper function to update slider value text and circle opacity
    function updateColorMixer(type) {
      const sliders = type === 'rgb' ? rgbSliders : cmykSliders;
      const values = type === 'rgb' ? rgbValues : cmykValues;
      const display = type === 'rgb' ? rgbDisplay : cmykDisplay;
      const circles = type === 'rgb' ? rgbCircles : cmykCircles;
      const isRGB = type === 'rgb';

      for (const key in sliders) {
        const value = parseInt(sliders[key].value);
        values[key].textContent = value + (isRGB ? '' : '%');

        // Update opacity of the corresponding circle
        let opacity = value / (isRGB ? 255 : 100);
        if (isRGB) {
             // For RGB, opacity = intensity (more opacity = more light)
             circles[key].style.opacity = opacity;
        } else {
             // For CMYK, opacity = ink coverage (more opacity = more ink absorption)
             // Opacity directly maps to ink percentage
             circles[key].style.opacity = opacity;
        }
      }
       // Optional: Update result overlay background color (for static preview)
       // This part can be removed if the visual mixing is sufficient
       // const r = parseInt(rgbSliders.r.value);
       // const g = parseInt(rgbSliders.g.value);
       // const b = parseInt(rgbSliders.b.value);
       // rgbDisplay.style.backgroundColor = `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;
       // const c = parseInt(cmykSliders.c.value);
       // const m = parseInt(cmykSliders.m.value);
       // const y = parseInt(cmykSliders.y.value);
       // const k = parseInt(cmykSliders.k.value);
       // const rgbFromCmyk = cmykToRgb(c,m,y,k); // Re-use or remove cmykToRgb if not needed for result-overlay
       // cmykDisplay.style.backgroundColor = `#${rgbFromCmyk.r.toString(16).padStart(2, '0')}${rgbFromCmyk.g.toString(16).padStart(2, '0')}${rgbFromCmyk.b.toString(16).padStart(2, '0')}`;
    }

    // --- RGB Mixer Logic ---
    const rgbSliders = {
      r: document.getElementById('rgb-r'),
      g: document.getElementById('rgb-g'),
      b: document.getElementById('rgb-b')
    };
    const rgbValues = {
      r: document.getElementById('rgb-r-value'),
      g: document.getElementById('rgb-g-value'),
      b: document.getElementById('rgb-b-value')
    };
    const rgbDisplay = document.querySelector('.rgb-display');
    const rgbCircles = {
        r: rgbDisplay.querySelector('.red-circle'),
        g: rgbDisplay.querySelector('.green-circle'),
        b: rgbDisplay.querySelector('.blue-circle')
    };
    const rgbResetButton = document.querySelector('.reset-button[data-target="rgb"]');


    for (const key in rgbSliders) {
      rgbSliders[key].addEventListener('input', () => updateColorMixer('rgb'));
    }

    // RGB Reset button
    rgbResetButton.addEventListener('click', () => {
        for (const key in rgbSliders) {
            rgbSliders[key].value = 0;
        }
        updateColorMixer('rgb');
    });


    // --- CMYK Mixer Logic ---
    const cmykSliders = {
      c: document.getElementById('cmyk-c'),
      m: document.getElementById('cmyk-m'),
      y: document.getElementById('cmyk-y'),
      k: document.getElementById('cmyk-k')
    };
    const cmykValues = {
      c: document.getElementById('cmyk-c-value'),
      m: document.getElementById('cmyk-m-value'),
      y: document.getElementById('cmyk-y-value'),
      k: document.getElementById('cmyk-k-value')
    };
    const cmykDisplay = document.querySelector('.cmyk-display');
     const cmykCircles = {
        c: cmykDisplay.querySelector('.cyan-circle'),
        m: cmykDisplay.querySelector('.magenta-circle'),
        y: cmykDisplay.querySelector('.yellow-circle'),
        k: cmykDisplay.querySelector('.black-circle')
    };
     const cmykResetButton = document.querySelector('.reset-button[data-target="cmyk"]');


    // The CMYK to RGB conversion function is no longer needed for the *visual overlap* simulation,
    // as the simulation happens directly in CSS using mix-blend-mode and opacity.
    // Keeping it commented out in case a future feature requires predicting the final RGB hex.
    /*
    function cmykToRgb(c, m, y, k) {
      c /= 100; m /= 100; y /= 100; k /= 100;
      const r = 255 * (1 - Math.min(1, c + k));
      const g = 255 * (1 - Math.min(1, m + k));
      const b = 255 * (1 - Math.min(1, y + k));
      return { r: Math.round(r), g: Math.round(g), b: Math.round(b) };
    }
    */

    for (const key in cmykSliders) {
      cmykSliders[key].addEventListener('input', () => updateColorMixer('cmyk'));
    }

     // CMYK Reset button
    cmykResetButton.addEventListener('click', () => {
        for (const key in cmykSliders) {
            cmykSliders[key].value = 0;
        }
        updateColorMixer('cmyk');
    });


    // --- Explanation Toggle Logic ---
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
      const isHidden = explanationDiv.style.display === 'none';
      explanationDiv.style.display = isHidden ? 'block' : 'none';
      toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים לדעת יותר? הצגת הסבר';
    });

    // Initial updates to set the starting visual state
    updateColorMixer('rgb');
    updateColorMixer('cmyk');
  });
</script>
```