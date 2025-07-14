---
title: "מחזור המים בטבע: מסע קסום על פני כדור הארץ"
english_slug: water-cycle-in-nature-earths-water-journey
category: "מדעי כדור הארץ"
tags:
  - מחזור המים
  - הידרולוגיה
  - סביבה
  - מדע
  - כדור הארץ
---
<h1>מחזור המים בטבע: מסע קסום על פני כדור הארץ</h1>
<p>הצטרפו אלינו למסע מופלא בעקבות טיפות המים! גלו איך הן מטיילות בין השמים, האדמה והאוקיינוסים, משנות צורה בלי הפסקה וחוזרות תמיד להתחיל את המסע מחדש. בואו נחקור יחד את סודות מחזור המים, מנוע החיים של כדור הארץ!</p>

<!-- Interactive App -->
<div id="water-cycle-app">
    <!-- Background Illustration Elements -->
    <div class="scene-element sky"></div>
    <div class="scene-element sun"></div>
    <div class="scene-element clouds"></div>
    <div class="scene-element mountains"></div>
    <div class="scene-element land"></div>
    <div class="scene-element plants"></div>
    <div class="scene-element river"></div>
    <div class="scene-element lake"></div>
    <div class="scene-element ocean"></div>
    
    <!-- Particle Container for Animations -->
    <div class="particle-container"></div>

    <!-- Hotspots - Positioned over relevant areas -->
    <div class="hotspot" id="hotspot-evaporation" data-process="evaporation" style="top: 70%; left: 18%;">
        <div class="hotspot-indicator">💦<span class="hotspot-label">התאדות</span></div>
        <div class="info-box">
            <h3>התאדות</h3>
            <p>השמש מחממת את האוקיינוסים, האגמים והנהרות, ומים נוזליים הופכים לאדי מים קלילים שעולים השמיימה.</p>
             <div class="process-indicator">⬆️</div>
        </div>
    </div>

     <div class="hotspot" id="hotspot-transpiration" data-process="transpiration" style="top: 58%; left: 55%;">
         <div class="hotspot-indicator">🌿<span class="hotspot-label">דיות</span></div>
        <div class="info-box">
            <h3>דיות</h3>
            <p>גם הצמחים מצטרפים למסיבה! הם משחררים אדי מים זעירים דרך העלים שלהם אל האוויר.</p>
            <div class="process-indicator">⬆️</div>
        </div>
    </div>

    <div class="hotspot" id="hotspot-condensation" data-process="condensation" style="top: 20%; left: 45%;">
         <div class="hotspot-indicator">☁️<span class="hotspot-label">התעבות</span></div>
        <div class="info-box">
            <h3>התעבות</h3>
            <p>אדי המים מתקררים גבוה בשמים, מתגבשים לטיפות זעירות או גבישי קרח ויוצרים עננים יפהפיים!</p>
             <div class="process-indicator">➡️☁️</div>
        </div>
    </div>

    <div class="hotspot" id="hotspot-precipitation" data-process="precipitation" style="top: 38%; left: 65%;">
        <div class="hotspot-indicator">🌧️<span class="hotspot-label">משקעים</span></div>
        <div class="info-box">
            <h3>משקעים</h3>
            <p>כשהעננים מתמלאים ונעשים כבדים, המים נופלים ארצה כגשם, שלג, ברד או טל.</p>
             <div class="process-indicator">⬇️</div>
        </div>
    </div>

    <div class="hotspot" id="hotspot-runoff" data-process="runoff" style="top: 65%; left: 75%;">
         <div class="hotspot-indicator">🏞️<span class="hotspot-label">נגר עילי</span></div>
        <div class="info-box">
            <h3>נגר עילי</h3>
            <p>חלק מהמים זורמים על פני הקרקע, יוצרים זרמים ונחלים ומגיעים לנהרות, אגמים ולבסוף לאוקיינוס.</p>
             <div class="process-indicator">➡️🏞️</div>
        </div>
    </div>
    
     <div class="hotspot" id="hotspot-infiltration" data-process="infiltration" style="top: 75%; left: 50%;">
         <div class="hotspot-indicator">🧱💧<span class="hotspot-label">חלחול</span></div>
        <div class="info-box">
            <h3>חלחול ומי תהום</h3>
            <p>חלק אחר של המים נספג לתוך האדמה, מחלחל עמוק ומצטבר במאגרי מי תהום תת-קרקעיים.</p>
             <div class="process-indicator">⬇️🧱</div>
        </div>
    </div>

     <div class="hotspot" id="hotspot-collection" data-process="collection" style="top: 85%; left: 30%;">
         <div class="hotspot-indicator">🌊<span class="hotspot-label">איסוף</span></div>
        <div class="info-box">
            <h3>איסוף</h3>
            <p>בסופו של דבר, כל המים מתנקזים ומתאספים באוקיינוסים, אגמים, נהרות ומאגרים תת-קרקעיים, ומשם - המסע מתחיל שוב!</p>
             <div class="process-indicator">↩️</div>
        </div>
    </div>

</div>

<!-- CSS Styling -->
<style>
    #water-cycle-app {
        position: relative;
        width: 100%;
        max-width: 960px; /* Increased size for better detail */
        height: 540px; /* 16:9 aspect ratio */
        margin: 20px auto;
        border-radius: 15px; /* Softer corners */
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* Deeper shadow */
        background: linear-gradient(to bottom, #a5d8ff 0%, #a5d8ff 55%, #89c994 55%, #89c994 100%); /* More vibrant colors */
        direction: rtl; /* Ensure RTL layout for content */
    }

    .scene-element {
        position: absolute;
        box-sizing: border-box;
    }

    .sky {
        top: 0; left: 0; width: 100%; height: 60%;
        background: linear-gradient(to bottom, #a5d8ff 0%, #66a3ff 100%); /* Gradient sky */
    }
    .sun {
        top: 8%; right: 10%; /* Positioned right for RTL */
        width: 80px; height: 80px;
        background: radial-gradient(circle, #ffffa0 0%, #ffd700 60%, transparent 70%); /* Softer sun with glow */
        border-radius: 50%;
        animation: sun-glow 10s infinite alternate ease-in-out; /* Subtle animation */
    }
    @keyframes sun-glow {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(1.05); opacity: 0.9; }
    }

    .clouds {
        top: 10%; left: 0; width: 100%; height: 30%;
        background: none; /* Will use multiple cloud elements */
        animation: clouds-move 60s linear infinite; /* Clouds drifting */
        z-index: 2; /* Above mountains */
    }

    /* Individual cloud elements can be added via JS or CSS */
    .clouds::before, .clouds::after {
        content: '';
        position: absolute;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 50px;
        filter: blur(8px);
        opacity: 0.8;
    }
     .clouds::before { top: 20%; left: 5%; width: 200px; height: 80px; }
     .clouds::after { top: 40%; left: 40%; width: 150px; height: 70px; transform: scale(0.8); }
     .clouds > div { /* Placeholder for more clouds */
         position: absolute; background: rgba(255, 255, 255, 0.9); border-radius: 50px; filter: blur(8px); opacity: 0.7;
         width: 180px; height: 90px; top: 10%; left: 70%;
     }


    @keyframes clouds-move {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100px); } /* Drift left */
    }

    .mountains {
        bottom: 30%; left: 0; width: 100%; height: 40%;
        background: linear-gradient(to top, #6b4c32 0%, #a08a7d 60%, #d4c2b8 100%); /* Layered mountain look */
        clip-path: polygon(0% 100%, 5% 70%, 15% 90%, 25% 50%, 35% 80%, 45% 40%, 55% 75%, 65% 35%, 75% 60%, 85% 20%, 95% 50%, 100% 30%, 100% 100%);
        z-index: 1; /* Below clouds */
    }
    .land {
        bottom: 0; left: 0; width: 100%; height: 40%;
        background: linear-gradient(to top, #556b2f 0%, #8fbc8f 100%); /* Earthy gradient */
        z-index: 0;
    }
     .plants {
         bottom: 40%; left: 50%; width: 20%; height: 10%;
         background: #2e8b57; /* Darker green */
         border-radius: 50% 50% 0 0 / 100% 100% 0 0;
         z-index: 3; /* Above land */
     }
    .river {
        bottom: 40%; left: 40%; width: 15%; height: 40%;
        background: #4682b4;
        clip-path: polygon(0% 0%, 15% 0%, 100% 100%, 85% 100%); /* Simple path */
        z-index: 4; /* Above land */
    }
    .lake {
        bottom: 40%; left: 65%; width: 20%; height: 15%;
        background: #4682b4;
        border-radius: 50%;
        z-index: 4; /* Above land */
    }
    .ocean {
        bottom: 0; left: 0; width: 45%; height: 40%;
        background: linear-gradient(to top, #104e8b 0%, #1e90ff 100%); /* Deep ocean gradient */
        z-index: 4; /* Above land */
    }

    /* Hotspot Styling */
    .hotspot {
        position: absolute;
        cursor: pointer;
        z-index: 15; /* Above scene elements */
        display: flex;
        flex-direction: column; /* Stack indicator and label */
        align-items: center;
        transform: translate(-50%, -50%); /* Center the hotspot div on its coordinate */
    }

    .hotspot-indicator {
        width: 40px; /* Larger indicator */
        height: 40px;
        background-color: rgba(255, 255, 255, 0.9);
        border: 3px solid #4682B4; /* Border color matching water */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.5em;
        color: #4682B4;
        transition: all 0.3s ease;
        box-shadow: 0 0 8px rgba(0,0,0,0.3);
    }

     .hotspot-indicator .hotspot-label {
         position: absolute;
         bottom: -25px; /* Position label below indicator */
         left: 50%;
         transform: translateX(-50%);
         font-size: 0.8em;
         color: #333;
         background-color: rgba(255, 255, 255, 0.8);
         padding: 2px 8px;
         border-radius: 5px;
         white-space: nowrap;
         opacity: 0;
         transition: opacity 0.3s ease;
     }

    .hotspot:hover .hotspot-indicator {
        transform: scale(1.1);
        background-color: #e0f7ff; /* Light blue on hover */
    }

     .hotspot:hover .hotspot-indicator .hotspot-label {
         opacity: 1;
     }


    .info-box {
        position: absolute;
        width: 220px; /* Wider info box */
        background-color: rgba(255, 255, 255, 0.98); /* More opaque */
        border: 1px solid #4682B4; /* Matching border */
        border-radius: 10px; /* Rounded corners */
        padding: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); /* Deeper shadow */
        z-index: 20;
        display: none; /* Hidden by default */
        text-align: right; /* For RTL */
        direction: rtl; /* For RTL */
        font-family: 'Arial', sans-serif; /* Clearer font */
        transform: translate(-50%, -10px); /* Default position below hotspot center */
        bottom: 100%; /* Position above the hotspot by default */
        left: 50%;
        white-space: normal; /* Allow text wrapping */
        transition: opacity 0.3s ease, transform 0.3s ease; /* Smooth transition */
        opacity: 0; /* Start hidden with opacity */
        pointer-events: none; /* Don't block clicks when hidden */
    }

    .info-box.visible {
         display: block;
         opacity: 1;
         pointer-events: auto; /* Enable clicks when visible */
    }


    /* Positioning adjustments for info boxes based on location */
    /* Boxes near bottom should appear above */
     .hotspot#hotspot-evaporation .info-box,
     .hotspot#hotspot-transpiration .info-box,
     .hotspot#hotspot-runoff .info-box,
     .hotspot#hotspot-infiltration .info-box,
     .hotspot#hotspot-collection .info-box {
         bottom: calc(100% + 15px); /* Position above the hotspot indicator + small gap */
         top: auto;
         transform: translate(-50%, 0); /* Keep centered, no Y translation needed with 'bottom' */
     }

     /* Boxes near top (condensation, precipitation) should appear below */
     .hotspot#hotspot-condensation .info-box,
     .hotspot#hotspot-precipitation .info-box {
         top: calc(100% + 15px); /* Position below the hotspot indicator + small gap */
         bottom: auto;
         transform: translate(-50%, 0);
     }


    .info-box h3 {
        margin-top: 0;
        margin-bottom: 8px; /* More space below heading */
        font-size: 1.1em; /* Slightly larger heading */
        color: #005f73; /* Dark blue heading color */
        border-bottom: 1px solid #e0e0e0; /* Lighter border */
        padding-bottom: 8px;
    }

    .info-box p {
        margin: 0;
        font-size: 0.95em; /* Slightly larger text */
        color: #333;
        line-height: 1.4; /* Better readability */
    }

    .info-box .process-indicator {
        margin-top: 10px; /* Space above indicator */
        font-size: 1.4em; /* Larger icon */
        text-align: center;
        color: #0077b6; /* Blue icon color */
    }

    /* Arrow for info boxes */
    .info-box::after {
        content: '';
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 12px solid transparent; /* Larger arrow */
        border-right: 12px solid transparent;
    }

    .hotspot#hotspot-evaporation .info-box::after,
    .hotspot#hotspot-transpiration .info-box::after,
    .hotspot#hotspot-runoff .info-box::after,
    .hotspot#hotspot-infiltration .info-box::after,
    .hotspot#hotspot-collection .info-box::after {
         /* Arrow points down, base on bottom edge */
         border-top: 12px solid rgba(255, 255, 255, 0.98);
         bottom: -12px;
         top: auto;
    }

    .hotspot#hotspot-condensation .info-box::after,
    .hotspot#hotspot-precipitation .info-box::after {
         /* Arrow points up, base on top edge */
         border-bottom: 12px solid rgba(255, 255, 255, 0.98);
         top: -12px;
         bottom: auto;
    }

    /* Particle Animations */
    .particle-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Particles don't block clicks */
        z-index: 10; /* Below hotspots */
    }

    .water-particle, .vapor-particle {
        position: absolute;
        width: 6px; height: 6px; /* Small particles */
        border-radius: 50%;
        opacity: 0.8;
        pointer-events: none;
        will-change: transform, opacity; /* Optimize animation */
    }

    .water-particle { background-color: rgba(70, 130, 180, 0.9); /* Blue */ }
    .vapor-particle { background-color: rgba(255, 255, 255, 0.8); /* White/transparent */ }

    /* Animation Keyframes (Examples - actual animation properties will be set by JS) */
    @keyframes flow-up { /* Evaporation/Transpiration */
        0% { transform: translate(0, 0); opacity: 1; }
        100% { transform: translate(var(--moveX), var(--moveY)); opacity: 0; }
    }
     @keyframes flow-down { /* Precipitation */
        0% { transform: translate(0, 0); opacity: 1; }
        100% { transform: translate(var(--moveX), var(--moveY)); opacity: 0; }
    }
     @keyframes flow-sideways { /* Runoff/Collection */
        0% { transform: translate(0, 0); opacity: 1; }
        100% { transform: translate(var(--moveX), var(--moveY)); opacity: 0; }
    }
      @keyframes flow-down-in { /* Infiltration */
        0% { transform: translate(0, 0); opacity: 1; }
        100% { transform: translate(var(--moveX), var(--moveY)); opacity: 0; }
    }


    /* Toggle Button Styling */
    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape */
        background-color: #0077b6; /* Blue button */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    #toggle-explanation:hover {
        background-color: #023e8a; /* Darker blue on hover */
    }

    #toggle-explanation:active {
        transform: scale(0.98);
    }

    /* Explanation Styling */
    #explanation {
        margin: 20px auto;
        max-width: 960px;
        padding: 20px;
        background-color: #f8f9fa; /* Light background */
        border: 1px solid #e9ecef;
        border-radius: 8px;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        color: #333;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    #explanation h2, #explanation h3 {
        color: #005f73; /* Dark blue headings */
        margin-bottom: 10px;
        border-bottom: 1px solid #e0e0e0;
        padding-bottom: 5px;
    }

    #explanation ul {
        list-style: disc inside;
        padding-right: 20px; /* Indent list for RTL */
    }

    #explanation li {
        margin-bottom: 8px;
    }

     #explanation strong {
         color: #0077b6; /* Highlight key terms */
     }


</style>

<!-- Explanation Button -->
<button id="toggle-explanation">הצג הסבר מפורט על מחזור המים</button>

<!-- Hidden Explanation -->
<div id="explanation" style="display: none;">
    <h2>הסבר מפורט: מסע המים במחזוריות נצחית</h2>
    <p>מחזור המים בטבע, המכונה גם המחזור ההידרולוגי, מתאר את התנועה המתמדת של מים על פני כדור הארץ, מעליו ומתחת לפניו. זהו תהליך חיוני לקיום חיים, המאפשר את זמינות המים המתוקים.</p>

    <h3>השלבים המרכזיים של מחזור המים:</h3>
    <ul>
        <li><strong>התאדות (Evaporation):</strong> תהליך בו מים נוזליים על פני הקרקע, מאוקיינוסים, אגמים, נהרות ומקווי מים אחרים, הופכים לאדי מים ועולים לאטמוספירה עקב חום השמש.</li>
        <li><strong>דיות (Transpiration):</strong> תהליך דומה להתאדות, בו צמחים משחררים אדי מים דרך פתחים זעירים בעליהם (פיוניות) אל האוויר.</li>
        <li><strong>התעבות (Condensation):</strong> כאשר אדי המים באטמוספירה עולים לגובה ונתקלים באוויר קר יותר, הם מתקררים והופכים בחזרה לטיפות מים זעירות או גבישי קרח. טיפות אלו מצטברות ויוצרות עננים.</li>
        <li><strong>משקעים (Precipitation):</strong> כאשר טיפות הממים או גבישי הקרח בעננים גדלים וכבדים מספיק, כוח הכבידה גורם להם ליפול חזרה לכדור הארץ. המשקעים יכולים להיות בצורת גשם, שלג, ברד או טל, תלוי בטמפרטורת האוויר.</li>
        <li><strong>איסוף (Collection):</strong> המים שירדו כמשקעים נאגרים במקומות שונים: חלקם זורמים על פני השטח, חלקם נספגים באדמה, וחלקם נופלים ישירות לאוקיינוסים, אגמים ונהרות.</li>
        <li><strong>נגר עילי (Surface Runoff):</strong> מים שזורמים על פני הקרקע במורד שיפועים, ומתנקזים בסופו של דבר לנחלים, נהרות, אגמים, ולבסוף לאוקיינוסים.</li>
        <li><strong>חלחול ומי תהום (Infiltration & Groundwater):</strong> חלק מהמים המחלחלים לתוך האדמה, עוברים דרך שכבות קרקע וסלע נקבוביות, ומצטברים במאגרים תת-קרקעיים הנקראים מי תהום. מי תהום יכולים לזרום לאט מתחת לפני השטח ולחזור בסופו של דבר למקווי מים עיליים או להישאב על ידי צמחים ובני אדם.</li>
    </ul>

    <p>מחזור המים הוא תהליך מתמיד ולולאה סגורה - אין סוף או התחלה אמיתיים, אלא רק מעברים בין שלבים שונים ומצבי צבירה שונים של המים. אנרגיית השמש היא הכוח המניע העיקרי מאחורי מחזור זה.</p>

    <p><strong>חשיבות מחזור הממים:</strong> מחזור המים חיוני לוויסות האקלים הגלובלי, להובלת חומרי מזון ומינרלים, לשמירה על מאזן המים המתוקים הדרושים לצמחים, בעלי חיים ובני אדם, ולעיצוב פני השטח של כדור הארץ לאורך זמן.</p>
</div>

<!-- JavaScript -->
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const hotspots = document.querySelectorAll('.hotspot');
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggle-explanation');
        const particleContainer = document.querySelector('.particle-container');
        let activeInfoBox = null;
        let currentAnimationTimer = null;

        // Define approximate start/end coordinates for particle animations (percentages)
        // These should roughly align with hotspot positions and next stages in the cycle
        const processFlows = {
            evaporation: {
                start: [{ x: 18, y: 70 }], // Ocean hotspot
                end: [{ x: 45, y: 20 }], // Condensation hotspot
                particleType: 'vapor-particle',
                duration: 4000, // ms
                count: 15,
                spread: 10 // Random spread around start/end
            },
             transpiration: {
                start: [{ x: 55, y: 58 }], // Plants hotspot
                end: [{ x: 45, y: 20 }], // Condensation hotspot
                particleType: 'vapor-particle',
                duration: 3500,
                count: 10,
                spread: 8
            },
            condensation: {
                 start: [{ x: 45, y: 20 }], // Condensation hotspot
                 end: [{ x: 65, y: 38 }], // Precipitation hotspot
                 particleType: 'water-particle',
                 duration: 2000,
                 count: 20,
                 spread: 15
            },
            precipitation: {
                 start: [{ x: 65, y: 38 }], // Precipitation hotspot
                 end: [{ x: 75, y: 65 }, {x: 50, y: 75}], // Runoff or Infiltration
                 particleType: 'water-particle',
                 duration: 3000,
                 count: 25,
                 spread: 15
            },
            runoff: {
                 start: [{ x: 75, y: 65 }], // Runoff hotspot (or near precipitation landing)
                 end: [{ x: 30, y: 85 }], // Collection hotspot
                 particleType: 'water-particle',
                 duration: 3000,
                 count: 15,
                 spread: 10
            },
            infiltration: {
                 start: [{ x: 50, y: 75 }], // Infiltration hotspot (or near precipitation landing)
                 end: [{ x: 30, y: 85 }], // Collection hotspot (via groundwater flow - abstract)
                 particleType: 'water-particle', // Represents underground flow abstractly
                 duration: 5000,
                 count: 10,
                 spread: 5
            },
             collection: {
                 start: [{ x: 30, y: 85 }], // Collection hotspot
                 end: [{ x: 18, y: 70 }], // Back to Evaporation (closing the loop - abstract)
                 particleType: 'water-particle',
                 duration: 4000,
                 count: 10,
                 spread: 10
            }
            // Note: Condensation particles might start in the sky area generally, not exactly on the hotspot.
            // Precipitation particles might land anywhere below the clouds.
            // Runoff particles start where rain lands on high ground and flow down.
            // Infiltration particles start where rain lands on land and go down.
            // Collection particles are already in water bodies.
            // The defined 'start' in processFlows uses hotspot locations for simplicity in this implementation.
        };


        // Function to show an info box
        function showInfoBox(hotspot) {
            // Hide any currently active info box
            if (activeInfoBox) {
                activeInfoBox.classList.remove('visible');
            }

            const infoBox = hotspot.querySelector('.info-box');
            infoBox.classList.add('visible');
            activeInfoBox = infoBox;

            // The CSS handles basic positioning (above/below) and centering via transform.
            // More complex boundary checks could be added here if needed.
        }

        // Function to hide an info box
        function hideInfoBox(infoBox) {
            if (infoBox) {
                 infoBox.classList.remove('visible');
                 if (activeInfoBox === infoBox) {
                     activeInfoBox = null;
                 }
            }
        }

        // Function to start particle animation
        function startProcessAnimation(processType) {
            stopCurrentAnimation(); // Stop any previous animation

            const flow = processFlows[processType];
            if (!flow) return;

            const containerRect = particleContainer.getBoundingClientRect();
            const containerWidth = containerRect.width;
            const containerHeight = containerRect.height;

            // Clear existing particles
            particleContainer.innerHTML = '';

            // Create and animate particles
            for (let i = 0; i < flow.count; i++) {
                const startPos = flow.start[Math.floor(Math.random() * flow.start.length)];
                const endPos = flow.end[Math.floor(Math.random() * flow.end.length)];

                 // Add random spread to start and end positions
                 const startX = startPos.x + (Math.random() - 0.5) * flow.spread;
                 const startY = startPos.y + (Math.random() - 0.5) * flow.spread;
                 const endX = endPos.x + (Math.random() - 0.5) * flow.spread;
                 const endY = endPos.y + (Math.random() - 0.5) * flow.spread;


                const particle = document.createElement('div');
                particle.classList.add(flow.particleType);
                particle.style.left = `${startX}%`;
                particle.style.top = `${startY}%`;

                // Calculate movement delta in pixels for CSS variables
                const moveX = (endX - startX) * containerWidth / 100;
                const moveY = (endY - startY) * containerHeight / 100;

                particle.style.setProperty('--moveX', `${moveX}px`);
                particle.style.setProperty('--moveY', `${moveY}px`);

                // Apply animation with calculated duration and random delay
                const delay = Math.random() * (flow.duration / 2); // Stagger particles
                particle.style.animation = `${getAnimationName(processType)} ${flow.duration}ms linear ${delay}ms forwards`;

                particleContainer.appendChild(particle);

                // Remove particle after animation ends
                particle.addEventListener('animationend', function() {
                    particle.remove();
                });
            }

            // Store timer to potentially stop animation early
            currentAnimationTimer = setTimeout(stopCurrentAnimation, flow.duration + (flow.duration / 2)); // Stop after all particles should be done
        }

        // Helper to get correct animation name based on process type
        function getAnimationName(processType) {
             if (processType === 'evaporation' || processType === 'transpiration') return 'flow-up';
             if (processType === 'precipitation' || processType === 'infiltration') return 'flow-down';
             if (processType === 'runoff' || processType === 'collection' || processType === 'condensation') return 'flow-sideways'; // Condensation particles move horizontally towards rain start
             return 'flow-sideways'; // Default
        }


        // Function to stop current particle animation and clear particles
        function stopCurrentAnimation() {
            if (currentAnimationTimer) {
                clearTimeout(currentAnimationTimer);
                currentAnimationTimer = null;
            }
             // Aggressively clear particles
            particleContainer.innerHTML = '';
        }


        // Add click listeners to hotspots
        hotspots.forEach(hotspot => {
            hotspot.addEventListener('click', function(event) {
                event.stopPropagation(); // Prevent click from bubbling to document

                const processType = this.getAttribute('data-process');
                const infoBox = this.querySelector('.info-box');

                if (infoBox.classList.contains('visible')) {
                    // If already visible, hide it and stop animation
                    hideInfoBox(infoBox);
                    stopCurrentAnimation();
                } else {
                    // If not visible, show it and start animation
                    showInfoBox(this);
                    startProcessAnimation(processType);
                }
            });
        });

        // Add click listener to the document body to hide info boxes and stop animation
        document.addEventListener('click', function(event) {
            // Check if the click is outside of any hotspot or visible info box
            let target = event.target;
            let isInsideHotspotOrInfo = false;
            while(target && target !== document.body) {
                 if (target.classList && (target.classList.contains('hotspot') || target.classList.contains('info-box'))) {
                     isInsideHotspotOrInfo = true;
                     break;
                 }
                 target = target.parentElement;
            }

            if (activeInfoBox && !isInsideHotspotOrInfo) {
                 hideInfoBox(activeInfoBox);
                 stopCurrentAnimation(); // Stop animation when info box is hidden
            }
        });

         // Prevent clicks inside info boxes from hiding them immediately (already handled by stopPropagation above)


        // Toggle explanation visibility
        toggleButton.addEventListener('click', function() {
            if (explanationDiv.style.display === 'none') {
                explanationDiv.style.display = 'block';
                toggleButton.textContent = 'הסתר הסבר מפורט';
            } else {
                explanationDiv.style.display = 'none';
                toggleButton.textContent = 'הצג הסבר מפורט על מחזור המים';
            }
        });
    });
</script>
```