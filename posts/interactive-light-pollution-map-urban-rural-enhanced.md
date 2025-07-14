---
title: "מסע לכוכבים: הדמיית זיהום אור והשפעתו על שמי הלילה"
english_slug: interactive-light-pollution-map-urban-rural-enhanced
category: "אסטרונומיה"
tags:
  - אסטרונומיה
  - סביבה
  - הדמיה
  - פיזיקה
  - זיהום אור
---

# מסע לכוכבים: הדמיית זיהום אור והשפעתו על שמי הלילה

העירוניות המודרנית מביאה איתה אור רב, שמייצר תחושת ביטחון ותנועה, אך יש לו גם השפעה פחות נראית לעין: הוא גונב לנו את הכוכבים. האם אי פעם עצרתם בעיר סואנת והתקשיתם לראות אפילו את הירח, בעוד שבטיול בטבע הרחק מהציוויליזציה נגלה לעיניכם שביל חלב עוצר נשימה? האפליקציה האינטראקטיבית שלפניכם מזמינה אתכם לחקור את התופעה המרתקת הזו. שחקו עם עוצמת האור המלאכותי בשני סוגי סביבות – עירונית וכפרית – וגלו כיצד זיהום האור מעצב מחדש את הנוף השמימי שלנו.

<div class="app-container">
  <div class="sky-comparison">
    <div class="sky-panel urban">
      <h3>שמיים באזור עירוני</h3>
      <div class="sky-view urban-sky">
        <div class="pollution-glow urban-glow"></div>
        <!-- Stars will be generated here by JS -->
      </div>
      <div class="controls">
        <label for="urbanLight">עוצמת זיהום האור בעיר:</label>
        <input type="range" id="urbanLight" name="urbanLight" min="0" max="100" value="80">
        <span id="urbanValue">80%</span>
      </div>
    </div>
    <div class="sky-panel rural">
      <h3>שמיים באזור כפרי</h3>
      <div class="sky-view rural-sky">
        <div class="pollution-glow rural-glow"></div>
        <!-- Stars will be generated here by JS -->
      </div>
      <div class="controls">
        <label for="ruralLight">עוצמת זיהום האור בכפר:</label>
        <input type="range" id="ruralLight" name="ruralLight" min="0" max="100" value="10">
         <span id="ruralValue">10%</span>
      </div>
    </div>
  </div>
</div>

<button id="toggleExplanation" class="explanation-button">לגלות את הסוד: מהו זיהום אור?</button>

<div id="explanation" class="explanation-hidden">
  <h2>מהו זיהום אור וכיצד הוא גונב לנו את הכוכבים?</h2>
  <p>זיהום אור הוא תוצאה של תאורה מלאכותית מוגזמת, לא מכוונת (למשל, אור המוקרן לשמיים במקום לכיוון הרצוי) או לא יעילה. בעיקר באזורים עירוניים, כמות גדולה של אור נשלחת לכל הכיוונים. כשהאור הזה פוגש חלקיקי אבק, טיפות מים ומזהמים באטמוספירה, הוא מתפזר ויוצר "הילה" זוהרת מעל מקורות האור. ההילה הזו מטשטשת ומסתירה את האור החלש שמגיע מהכוכבים, מה שהופך את צפיית הכוכבים למשימה כמעט בלתי אפשרית באזורים מוארים.</p>

  <h3>עיר מול כפר: קרב האור והחושך</h3>
  <p>ההבדל הדרמטי שראיתם בהדמיה נובע ישירות מצפיפות האור. בערים הגדולות, שפע של פנסי רחוב, שלטי ניאון, תאורת בניינים ומכוניות יוצרים כמויות אדירות של אור מלאכותי. גם אם חלק קטן ממנו מוקרן כלפי מעלה, הסך הכולל עצום. באזורים כפריים, לעומת זאת, יש הרבה פחות מקורות אור, מה שמאפשר לשמי הלילה להישאר חשוכים יותר, וכך לגרמי השמיים לזרוח ללא הפרעה משמעותית. זו הסיבה שאסטרונומים (חובבים ומקצועיים כאחד) נודדים לאזורים מבודדים וחשוכים כדי לבצע תצפיות איכותיות.</p>

  <h3>השפעות רחבות יותר של זיהום האור: לא רק הכוכבים נפגעים</h3>
  <ul>
    <li>**פגיעה בטבע:** בעלי חיים רבים, במיוחד אלה הפעילים בלילה, מסתמכים על מחזור האור-חושך הטבעי לניווט, ציד, רבייה ותקשורת. זיהום אור יכול לשבש את דרכי הנדידה של עופות, לבלבל חרקים, לפגוע בדפוסי שינה של יונקים ואף להשפיע על גידול צמחים.</li>
    <li>**השפעה על בריאות האדם:** חשיפה ממושכת לאור מלאכותי בשעות הלילה, בעיקר האור הכחול הנפלט ממסכים ומנורות לד מסוימות, עלולה לשבש את ייצור המלטונין – הורמון חשוב לוויסות השעון הביולוגי (מחזור שינה-עירות). שיבוש זה נקשר לבעיות שינה ואף לסיכון מוגבר לבעיות בריאותיות אחרות בטווח הארוך.</li>
    <li>**בזבוז אנרגיה ומשאבים:** תאורה לא יעילה שמאירה גם את השמיים במקום רק את מה שצריך, היא פשוט בזבוז. זה עולה כסף, דורש ייצור אנרגיה (שלעיתים קרובות מזהם) ותורם לפליטות גזי חממה.</li>
  </ul>

  <h3>מה אפשר לעשות כדי להחזיר את הכוכבים?</h3>
  <p>ישנן דרכים פשוטות לצמצם את זיהום האור: שימוש בתאורה המכוונת רק כלפי מטה (במקום כלפי מעלה או לצדדים), שימוש בעוצמת תאורה נמוכה ככל האפשר, העדפת תאורה בצבע "חם" יותר (פחות אור כחול), וכיבוי אורות שאינם בשימוש. מאמצים קטנים ברמה האישית והקהילתית יכולים לעזור לשמור על היופי הטבעי של שמי הלילה, לטובת הטבע, בריאותנו, וכמובן – כדי שנוכל להמשיך לחלום תחת שמיים זרועי כוכבים.</p>
</div>

<style>
  :root {
    --dark-blue: #0a1f44; /* Deeper base color */
    --deep-purple: #2a0a44; /* For gradients */
    --star-white: #ffffff;
    --star-glow: rgba(255, 255, 255, 0.8); /* Brighter star simulation */
    --pollution-color-low: rgba(255, 193, 7, 0.1); /* Amber/Orange faint glow */
    --pollution-color-high: rgba(255, 255, 220, 0.3); /* White/Yellow brighter glow */
    --primary-accent: #4db6ac; /* Teal accent */
    --secondary-accent: #81c784; /* Green accent */
    --text-color: #e0e0e0; /* Lighter text for dark background */
    --panel-bg: #1a2e52; /* Dark panel background */
    --border-radius: 12px;
    --padding: 25px;
    --margin: 20px;
    --control-height: 60px; /* More space for controls */
  }

  body {
    font-family: 'Arial', sans-serif;
    line-height: 1.7;
    color: var(--text-color);
    background: linear-gradient(to bottom, var(--dark-blue), var(--deep-purple)); /* Subtle gradient background */
    min-height: 100vh; /* Full viewport height background */
    padding: var(--padding);
    direction: rtl;
    text-align: right;
    overflow-x: hidden; /* Prevent horizontal scroll */
  }

  h1, h2, h3 {
      text-align: center;
      color: var(--primary-accent);
      margin-bottom: var(--margin);
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
  }

  h2 {
      font-size: 1.8em;
  }

  h3 {
      font-size: 1.3em;
      margin-bottom: 15px;
  }

  p {
      margin-bottom: var(--margin);
      font-size: 1.1em;
      color: rgba(224, 224, 224, 0.9); /* Slightly transparent text */
  }

  .app-container {
    display: flex;
    justify-content: center;
    margin: var(--margin) auto;
    max-width: 1100px; /* Slightly wider */
    background-color: var(--panel-bg);
    border-radius: var(--border-radius);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3); /* Softer, larger shadow */
    padding: var(--padding);
    border: 1px solid rgba(255, 255, 255, 0.1); /* Subtle border */
  }

  .sky-comparison {
    display: flex;
    flex-wrap: wrap;
    gap: var(--padding);
    width: 100%;
  }

  .sky-panel {
    flex: 1;
    min-width: 320px; /* Slightly wider minimum */
    background-color: var(--dark-blue);
    border-radius: var(--border-radius);
    padding: var(--padding);
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid rgba(255, 255, 255, 0.08);
  }

  .sky-panel h3 {
    margin-top: 0;
    margin-bottom: var(--margin);
    color: var(--star-white);
    font-weight: normal;
  }

  .sky-view {
    width: 100%;
    height: 300px; /* Taller view */
    background: linear-gradient(to top, #00081a, var(--dark-blue) 80%); /* Darker gradient for sky */
    border-radius: var(--border-radius);
    margin-bottom: var(--margin);
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5); /* Inner shadow for depth */
  }

   .pollution-glow {
       position: absolute;
       bottom: 0;
       left: 0;
       width: 100%;
       height: 80%; /* Glow from the bottom */
       background: radial-gradient(ellipse at bottom, var(--pollution-color-low) 0%, transparent 60%);
       pointer-events: none; /* Allow clicking through */
       transition: background 0.5s ease-out, opacity 0.5s ease-out; /* Smooth glow change */
       opacity: 0; /* Start hidden */
   }

  .star {
    position: absolute;
    background-color: var(--star-white);
    border-radius: 50%;
    opacity: 0; /* Start hidden for animation */
    box-shadow: 0 0 2px var(--star-glow); /* Subtle star glow effect */
    animation: twinkle linear infinite; /* Add twinkling animation */
  }

   @keyframes twinkle {
       0%, 100% { opacity: 1; }
       50% { opacity: 0.5; }
   }


  .controls {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch; /* Stretch controls */
    height: var(--control-height);
    justify-content: space-between; /* Space between elements */
  }

  .controls label {
    margin-bottom: 8px;
    font-weight: normal;
    color: var(--primary-accent);
    text-align: center;
  }

  .controls input[type="range"] {
    width: 100%; /* Full width */
    -webkit-appearance: none;
    appearance: none;
    height: 12px; /* Thicker slider track */
    background: #334a6d; /* Darker track color */
    outline: none;
    opacity: 0.9;
    transition: opacity .2s, background .3s ease; /* Add background transition */
    border-radius: 6px;
    margin-bottom: 8px;
    cursor: grab; /* Indicate draggable */
  }

   .controls input[type="range"]:active {
       cursor: grabbing;
   }


  .controls input[type="range"]:hover {
    opacity: 1;
    background: #4a6a96; /* Lighter on hover */
  }

  .controls input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px; /* Larger thumb */
    height: 24px; /* Larger thumb */
    background: var(--primary-accent);
    cursor: pointer;
    border-radius: 50%;
    border: 3px solid var(--panel-bg); /* Border matches panel background */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    transition: background 0.3s ease;
  }

  .controls input[type="range"]::-moz-range-thumb {
    width: 24px;
    height: 24px;
    background: var(--primary-accent);
    cursor: pointer;
    border-radius: 50%;
    border: 3px solid var(--panel-bg);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    transition: background 0.3s ease;
  }

   .controls input[type="range"]::-webkit-slider-thumb:hover,
   .controls input[type="range"]::-moz-range-thumb:hover {
       background: var(--secondary-accent); /* Change thumb color on hover */
   }


  .controls span {
      font-weight: bold;
      color: var(--secondary-accent); /* Accent color for value */
      font-size: 1.2em;
      display: block; /* Ensure it takes full width */
      text-align: center;
  }


  .explanation-button {
    display: block;
    margin: var(--margin) auto;
    padding: 12px 25px; /* More padding */
    background: linear-gradient(to right, var(--secondary-accent), var(--primary-accent)); /* Gradient button */
    color: white;
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    letter-spacing: 0.5px;
  }

  .explanation-button:hover {
    background: linear-gradient(to right, var(--primary-accent), var(--secondary-accent));
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
    transform: translateY(-2px); /* Subtle lift */
  }

   .explanation-button:active {
       transform: translateY(0); /* Press down effect */
       box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
   }

  #explanation {
    margin-top: var(--padding);
    padding: var(--padding);
    background-color: var(--panel-bg);
    border-radius: var(--border-radius);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    direction: rtl;
    text-align: right;
    border: 1px solid rgba(255, 255, 255, 0.08);
    opacity: 1;
    max-height: 2000px; /* Large value for smooth transition */
    overflow: hidden;
    transition: opacity 0.6s ease-out, max-height 0.6s ease-out; /* Transition for show/hide */
  }

  #explanation.explanation-hidden {
    opacity: 0;
    max-height: 0; /* Collapse the div */
    padding-top: 0;
    padding-bottom: 0;
    margin-top: 0;
    /* display: none; /* Or just rely on max-height/opacity */
  }


  #explanation h2 {
      text-align: right;
      color: var(--primary-accent);
  }

  #explanation ul {
      padding-right: 25px; /* Adjust padding for RTL list */
      margin-top: 15px;
      margin-bottom: 15px;
      list-style: disc outside; /* Explicitly set list style */
      color: rgba(224, 224, 224, 0.9);
  }

  #explanation li {
      margin-bottom: 10px;
      line-height: 1.5;
  }


  /* Responsive adjustments */
  @media (max-width: 800px) { /* Adjusted breakpoint */
    .sky-comparison {
      flex-direction: column;
    }

    .sky-panel {
        min-width: 100%;
    }

    body {
        padding: 15px;
    }

    .app-container {
        padding: 15px;
    }

    .sky-panel {
        padding: 15px;
    }

    .explanation-button {
        font-size: 1rem;
        padding: 10px 20px;
    }

    #explanation {
        padding: 15px;
    }

    h1 {
        font-size: 1.8em;
    }

    h2 {
        font-size: 1.5em;
    }

    h3 {
        font-size: 1.2em;
    }

    p {
        font-size: 1em;
    }
  }

</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const urbanSky = document.querySelector('.urban-sky');
    const ruralSky = document.querySelector('.rural-sky');
    const urbanLightSlider = document.getElementById('urbanLight');
    const ruralLightSlider = document.getElementById('ruralLight');
    const urbanValueSpan = document.getElementById('urbanValue');
    const ruralValueSpan = document.getElementById('ruralValue');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggleExplanation');
    const urbanGlow = urbanSky.querySelector('.pollution-glow');
    const ruralGlow = ruralSky.querySelector('.pollution-glow');


    const numStars = 300; // More stars for a richer sky
    const maxStarSize = 3; // Max size in pixels
    const minStarSize = 0.5; // Min size in pixels

    // Function to create a star element with varying magnitudes
    function createStar() {
      const star = document.createElement('span');
      star.classList.add('star');

      // Simulate different star magnitudes by varying size and base opacity
      const size = Math.random() * (maxStarSize - minStarSize) + minStarSize;
      star.style.width = `${size}px`;
      star.style.height = `${size}px`;

      // Base opacity correlated with size (brighter stars are larger)
      const baseOpacity = Math.pow(size / maxStarSize, 1.5) * 0.7 + 0.3; // Non-linear correlation
      star.dataset.baseOpacity = baseOpacity.toString(); // Store base opacity as string

      star.style.left = `${Math.random() * 100}%`;
      star.style.top = `${Math.random() * 100}%`;
      star.style.opacity = 0; // Will be set correctly on initial update and animated

      // Add random animation delay for twinkling effect
      star.style.animationDelay = `${Math.random() * 2}s`;
      star.style.animationDuration = `${2 + Math.random() * 3}s`; // Vary twinkling speed

      return star;
    }

    // Populate sky views with stars
    function populateSky(skyElement) {
      for (let i = 0; i < numStars; i++) {
        skyElement.appendChild(createStar());
      }
    }

    // Update sky visibility and glow based on light pollution
    function updateSky(skyElement, lightLevel, glowElement) {
      const stars = skyElement.querySelectorAll('.star');
      const pollutionFactor = lightLevel / 100; // Ranges from 0 to 1

      // Update star visibility
      stars.forEach(star => {
        const baseOpacity = parseFloat(star.dataset.baseOpacity);

        // Pollution effect: Higher pollution reduces visibility, especially of fainter stars
        // Use a non-linear scale for pollution effect, stronger for high pollution levels
        const visibilityMultiplier = Math.max(0, 1 - Math.pow(pollutionFactor, 2) * 1.2); // Faster drop-off at higher pollution

        // Apply multiplier to base opacity
        let effectiveOpacity = baseOpacity * visibilityMultiplier;

        // Make fainter stars disappear completely at moderate/high pollution
        if (pollutionFactor > 0.3 && baseOpacity < 0.5 && Math.random() > (1 - (pollutionFactor - 0.3) * 1.5)) {
             effectiveOpacity = 0;
        }
        if (pollutionFactor > 0.6 && baseOpacity < 0.7 && Math.random() > (1 - (pollutionFactor - 0.6) * 2)) {
             effectiveOpacity = 0;
        }
         if (pollutionFactor > 0.8 && baseOpacity < 0.9 && Math.random() > (1 - (pollutionFactor - 0.8) * 3)) {
             effectiveOpacity = 0;
         }


        // Ensure opacity is within bounds and apply small minimum for bright stars
        star.style.opacity = Math.max(0, Math.min(1, effectiveOpacity));
      });

       // Update pollution glow visibility and color
       if (glowElement) {
           const glowOpacity = pollutionFactor * 0.8; // Glow becomes more opaque with higher pollution
           // Interpolate color based on pollution level (from subtle amber to brighter white/yellow)
           const r = Math.round(255);
           const g = Math.round(193 + (255 - 193) * pollutionFactor);
           const b = Math.round(7 + (220 - 7) * pollutionFactor);
           const glowColor = `rgba(${r}, ${g}, ${b}, ${0.1 + pollutionFactor * 0.2})`; // Base alpha + scaled alpha

           glowElement.style.opacity = glowOpacity;
           glowElement.style.background = `radial-gradient(ellipse at bottom, rgba(${r}, ${g}, ${b}, ${0.1 + pollutionFactor * 0.2}) 0%, transparent 60%)`;
       }
    }

    // Initial population
    populateSky(urbanSky);
    populateSky(ruralSky);

    // Initial update based on default slider values, with a small delay to allow stars to render before fading
    setTimeout(() => {
        updateSky(urbanSky, urbanLightSlider.value, urbanGlow);
        urbanValueSpan.textContent = `${urbanLightSlider.value}%`;
        updateSky(ruralSky, ruralLightSlider.value, ruralGlow);
        ruralValueSpan.textContent = `${ruralLightSlider.value}%`;
    }, 100); // Small delay


    // Add event listeners to sliders
    urbanLightSlider.addEventListener('input', (event) => {
      const lightLevel = event.target.value;
      updateSky(urbanSky, lightLevel, urbanGlow);
      urbanValueSpan.textContent = `${lightLevel}%`;
    });

    ruralLightSlider.addEventListener('input', (event) => {
      const lightLevel = event.target.value;
      updateSky(ruralSky, lightLevel, ruralGlow);
       ruralValueSpan.textContent = `${lightLevel}%`;
    });

    // Add event listener for explanation toggle button
    toggleButton.addEventListener('click', () => {
      const isHidden = explanationDiv.classList.toggle('explanation-hidden');
       // Optional: Change button text based on state
       if (isHidden) {
           toggleButton.textContent = 'לגלות את הסוד: מהו זיהום אור?';
       } else {
           toggleButton.textContent = 'להסתיר את ההסבר';
       }
       // If showing, scroll to the explanation div
       if (!isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
       }
    });
     // Set initial button text (Explanation starts hidden by default via CSS)
     toggleButton.textContent = 'לגלות את הסוד: מהו זיהום אור?';


     // Handle initial state of explanation div via JS if needed (CSS handles it now)
     // explanationDiv.classList.add('explanation-hidden'); // Ensures it's hidden on load

  });
</script>