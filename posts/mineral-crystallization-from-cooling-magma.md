---
title: "המסע המופלא של המגמה: להפוך לנוצצים - איך נוצרים מינרלים?"
english_slug: mineral-crystallization-from-cooling-magma
category: "מדעי הסביבה / כדור הארץ"
tags:
  - מינרלים
  - מגמה
  - התגבשות
  - גיאולוגיה
  - סדרת בואן
  - סלעים פלוטוניים
  - סלעים וולקניים
---
<div id="app-container">
    <div id="sim-area">
        <div id="temperature-display">טמפרטורה: <span id="current-temp">...</span>°C</div>
        <div id="crucible">
            <div id="magma"></div>
            <div id="crystal-container"></div>
            <div id="cooling-overlay"></div> <!-- Added for cooling effect -->
        </div>
        <div id="rock-preview">
            <h4>תוצאה משוערת:</h4>
            <p id="rock-type">... מחכה לסימולציה ...</p>
        </div>
    </div>

    <div id="controls">
        <label for="cooling-rate">קצב קירור:</label>
        <select id="cooling-rate">
            <option value="very-slow">איטי מאוד (עומק רב)</option>
            <option value="slow" selected>איטי (עומק בינוני)</option>
            <option value="medium">בינוני</option>
            <option value="fast">מהיר (קרוב לפני השטח)</option>
            <option value="very-fast">מהיר מאוד (התפרצות געשית)</option>
        </select>
        <button id="start-sim">התחל מסע התגבשות!</button>
        <button id="reset-sim" disabled>התחל מחדש</button>
    </div>

    <div id="legend">
        <h4>כוכבי המסע (מינרלים):</h4>
        <div class="legend-item"><span class="legend-color olivine-pyroxene-color"></span> אוליבין / פירוקסן</div>
        <div class="legend-item"><span class="legend-color plagioclase-color"></span> פלגיוקלז</div>
        <div class="legend-item"><span class="legend-color biotite-color"></span> ביוטיט</div>
        <div class="legend-item"><span class="legend-color k-feldspar-color"></span> אשלגן פלדספר</div>
        <div class="legend-item"><span class="legend-color quartz-color"></span> קוורץ</div>
         <div class="legend-item"><span class="legend-color rest-color"></span> מינרלים אחרים / זכוכית</div>
    </div>
</div>

<h1>המסע המופלא של המגמה: להפוך לנוצצים - איך נוצרים מינרלים?</h1>
<p>דמיינו את ליבת כדור הארץ, מקום של חום עז ולחץ עצום. שם, סלעים נמסים ויוצרים נוזל לוהט ומסתורי - המגמה! עכשיו דמיינו את המגמה הזו מטפסת מעלה, פוגשת סביבה קרירה יותר, ומתחילה מסע טרנספורמציה מדהים. כיצד הנוזל הלוהט הזה הופך לסלעים קשיחים, מלאי גבישים צבעוניים ונוצצים כמו הגרניט המוכר? הצטרפו לסימולציה כדי לגלות את הסוד!</p>

<button id="toggle-explanation">הצצה אל מאחורי הקלעים (הסבר מדעי)</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מסע ההתגבשות המדהים</h2>
    <h3>מהי מגמה ומדוע היא מתגבשת?</h3>
    <p>מגמה היא סלע מותך לוהט, לרוב בעומק רב בכדור הארץ. היא נוצרת באזורים שבהם הטמפרטורה והלחץ גבוהים מספיק כדי להתיך סלעים. כשהמגמה מוצאת דרכה מעלה, לתוך סדקים בקרום או אל פני השטח (אז נקראת "לבה"), היא מתחילה להתקרר. תהליך הקירור הזה הוא המפתח לשינוי: האטומים והמולקולות החופשיים יחסית במצב הנוזלי מתחילים לאבד אנרגיה ולהתארגן במבנים מסודרים וחוזרים על עצמם – מבנים גבישיים. כל מבנה גבישי כזה הוא מינרל ספציפי.</p>

    <h3>הקצב קובע הכל: השפעת קצב הקירור</h3>
    <p>קצב הקירור הוא הגורם הדרמטי ביותר המשפיע על התוצאה הסופית:</p>
    <ul>
        <li><strong>קירור איטי מאוד (עומק רב):</strong> כשהמגמה כלואה עמוק בפנים, היא מתקררת לאט לאט, לעיתים במשך אלפי או מיליוני שנים. קצב קירור כזה מאפשר לאטומים "זמן איכות" למצוא את מקומם, לנוע בחופשיות יחסית (בתוך הנוזל שעדיין חם), ולהצטרף לגבישים קיימים. התוצאה: נוצרים מעט מוקדי התגבשות (גרעיני גיבוש), אך הגבישים שכן נוצרים גדלים לגדלים מרשימים, הנראים לעין בלתי מזוינת בקלות. סלעים כאלה נקראים <strong>סלעים פלוטוניים</strong> או <strong>אינטרוסיביים</strong> (חודרים), ומרקמם גס גביש (פנריטי). גרניט הוא הדוגמה הקלאסית.</li>
        <li><strong>קירור מהיר מאוד (פני השטח - לבה):</strong> כשהלבה פורצת בהתפרצות געשית, היא נחשפת מייד לאוויר או למים ומתקררת במהירות מסחררת (תוך שעות, ימים או שנים). קצב קירור כזה "מקפיא" את האטומים במקומם לפני שהספיקו להתארגן לגבישים גדולים. התוצאה: נוצרים המון מוקדי התגבשות זעירים, אך הגבישים נשארים קטנים עד מיקרוסקופיים. סלעים כאלה נקראים <strong>סלעים וולקניים</strong> או <strong>אקסטרוסיביים</strong> (פורצים), ומרקמם דק גביש (אפניטי). בזלת היא הדוגמה המוכרת ביותר. במקרים קיצוניים של קירור מהיר במיוחד, כלל לא נוצרים גבישים, ונוצרת זכוכית וולקנית כמו אובסידיאן.</li>
    </ul>

    <h3>סדרת בואן: מי מופיע ראשון בחגיגה?</h3>
    <p>הגיאולוג נורמן ל. בואן גילה שמינרלים שונים מתגבשים מסוג מגמה נפוץ (בזלתית) בסדר טמפרטורות יחסית קבוע ככל שהמגמה מתקררת. הסדר, המכונה <strong>סדרת בואן</strong>, מתחיל במינרלים המתגבשים בטמפרטורות הגבוהות ביותר (כמו אוליבין ופירוקסן), וממשיך כשהטמפרטורה יורדת למינרלים אחרים (פלגיוקלז, ביוטיט, אמפיבול), ומסתיים בטמפרטורות הנמוכות ביותר עם מינרלים כמו אשלגן פלדספר, מוסקוביט וקוורץ. הסימולציה שלנו מציגה גרסה פשוטה ומרהיבה של סדר ההופעה הזה, ומאפשרת לכם לראות כיצד קצב הקירור משפיע לא רק על גודל הגבישים, אלא גם על הרכב המינרלים ש"מצליחים" להתגבש בסלע הסופי.</p>
</div>

<style>
    /* Overall App Styling */
    #app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px auto;
        padding: 25px;
        border-radius: 12px;
        background-color: #f0f4f8; /* Soft light background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        max-width: 600px; /* Limit width for better appearance */
        font-family: 'Arial', sans-serif; /* Modern font */
    }

    #sim-area {
         position: relative; /* For absolute positioning of temp */
         width: 100%;
         max-width: 350px; /* Control sim width */
         display: flex;
         flex-direction: column;
         align-items: center;
         margin-bottom: 25px;
    }

    #temperature-display {
        position: absolute;
        top: -30px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.9em;
        z-index: 10; /* Above crucible */
        min-width: 150px;
        text-align: center;
    }

    /* Crucible (Container) Styling */
    #crucible {
        width: 100%;
        height: 400px; /* Slightly taller */
        border: 12px solid #5a3b2b; /* Darker, richer brown */
        border-top: none; /* No top border */
        border-radius: 0 0 60px 60px; /* More pronounced rounded bottom */
        position: relative;
        overflow: hidden; /* Hide content outside bounds */
        background-color: #c0805a; /* Base color for crucible sides */
        box-shadow: inset 0 -10px 15px rgba(0, 0, 0, 0.3); /* Inner shadow for depth */
    }

    /* Magma (Simulated Liquid) Styling */
    #magma {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        /* Initial hot magma gradient */
        background: linear-gradient(to bottom, rgba(255, 100, 0, 0.95), rgba(255, 50, 0, 0.8), rgba(200, 0, 0, 0.6));
        opacity: 1; /* Starts fully opaque */
        transition: opacity var(--sim-duration) linear, background var(--sim-duration) linear; /* Use CSS variable for duration */
    }

     #cooling-overlay {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background-color: rgba(70, 90, 110, 0); /* Start transparent */
         transition: background-color var(--sim-duration) linear; /* Smooth transition to cooler color */
     }


    /* Crystal Container and Crystal Styling */
    #crystal-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Ignore clicks on crystal layer */
        z-index: 5; /* Below temperature, above magma */
    }

    .crystal {
        position: absolute;
        border-radius: 50%; /* Keep initial circles */
        background-color: rgba(255, 255, 255, 0.8); /* Default, slightly transparent white */
        width: 3px; /* Start very small */
        height: 3px;
        /* transition: width 0.5s ease-out, height 0.5s ease-out; */ /* Growth will be handled by JS for dynamic speed */
        transform: translate(-50%, -50%); /* Center the crystal on its x,y coords */
        box-sizing: border-box;
        opacity: 0; /* Start invisible */
        animation: fadeIn 0.5s ease-out forwards; /* Fade in when nucleated */
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    /* Specific Mineral Colors & Appearance */
    .olivine-pyroxene-color { background-color: darkolivegreen; border: 1px solid #556b2f; }
    .crystal.olivine-pyroxene { background-color: darkolivegreen; border: 1px solid #556b2f; } /* Dark green/brown */

    .plagioclase-color { background-color: lightgray; border: 1px solid gray; }
     /* Plagioclase can be more rectangular/tabular, try slightly different shapes if possible? Or just varied size */
    .crystal.plagioclase { background-color: lightgray; border: 1px solid gray; border-radius: 20%; } /* Slightly less round */


    .biotite-color { background-color: black; border: 1px solid #222; }
    /* Biotite is flaky, maybe simulate with slightly flatter shape or darker border */
    .crystal.biotite { background-color: black; border: 1px solid #222; border-radius: 10%; } /* Flaky appearance attempt */


    .k-feldspar-color { background-color: lavenderblush; border: 1px solid pink; }
    .crystal.k-feldspar { background-color: lavenderblush; border: 1px solid pink; } /* Pinkish/white */

    .quartz-color { background-color: rgba(128, 128, 128, 0.5); border: 1px solid #666; }
     /* Quartz is glassy, maybe semi-transparent */
    .crystal.quartz { background-color: rgba(128, 128, 128, 0.5); border: 1px solid #666; } /* Semi-transparent gray */

     .rest-color { background-color: #555; border: 1px solid #333;}
     .crystal.rest { background-color: #555; border: 1px solid #333;} /* Represents uncrystallized/fine matrix */


    /* Controls and Legend Styling */
    #controls {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center;
        align-items: center;
        gap: 15px 20px; /* Row and column gap */
        margin-bottom: 25px;
        padding: 15px;
        background-color: #eef2f7;
        border-radius: 8px;
        width: 100%;
        max-width: 500px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    #controls label {
        font-weight: bold;
        color: #333;
    }

    #controls select,
    #controls button {
        padding: 10px 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    #controls select {
        background-color: white;
        appearance: none; /* Remove default arrow */
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007bff%22%20d%3D%22M287%2C114.7L159.2%2C221.3c-5.3%2C4.2-12.9%2C4.2-18.2%2C0L5.4%2C114.7c-6-4.7-6.9-13.7-2.1-19.8c4.7-6%2C13.7-6.9%2C19.8-2.1l123.7%2C97.8l123.7-97.8c6-4.7%2C15-3.9%2C19.8%2C2.1C293.9%2C101%2C293%2C109.1%2C287%2C114.7z%22%2F%3E%3C%2Fsvg%3E');
        background-repeat: no-repeat;
        background-position: right 10px top 50%;
        background-size: 12px auto;
        padding-right: 30px; /* Make space for arrow */
    }

    #start-sim {
        background-color: #28a745; /* Success green */
        color: white;
        border-color: #28a745;
    }

    #start-sim:hover:not(:disabled) {
        background-color: #218838;
        border-color: #1e7e34;
    }

    #reset-sim {
        background-color: #dc3545; /* Danger red */
        color: white;
        border-color: #dc3545;
    }
     #reset-sim:hover:not(:disabled) {
        background-color: #c82333;
        border-color: #bd2130;
    }


    #controls button:disabled,
     #controls select:disabled {
        background-color: #e9ecef;
        color: #6c757d;
        border-color: #ced4da;
        cursor: not-allowed;
        opacity: 0.7;
    }

    #legend {
        margin-top: 25px;
        padding: 15px;
        border: 1px solid #d4d4d4;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        width: 100%;
        max-width: 500px;
    }

    #legend h4 {
        margin-top: 0;
        margin-bottom: 12px;
        text-align: center;
        color: #333;
        font-size: 1.1em;
    }

    .legend-item {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        font-size: 0.95em;
        color: #555;
    }

    .legend-color {
        display: inline-block;
        width: 20px; /* Larger color swatches */
        height: 20px;
        margin-inline-end: 10px;
        border: 1px solid #ccc; /* Add border for visibility */
        box-sizing: border-box;
        border-radius: 4px; /* Slightly rounded legend colors */
    }

     /* Specific Legend Color Borders (Match crystal borders) */
    .olivine-pyroxene-color { border: 1px solid #556b2f; }
    .plagioclase-color { border: 1px solid gray; }
    .biotite-color { border: 1px solid #222; }
    .k-feldspar-color { border: 1px solid pink; }
    .quartz-color { border: 1px solid #666; }
    .rest-color { border: 1px solid #333; }


    /* Explanation Section Styling */
    #toggle-explanation {
        margin: 20px auto;
        display: block;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }

    #toggle-explanation:hover {
        background-color: #0056b3;
    }

    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f9f9f9;
        max-width: 700px; /* Allow explanation to be wider */
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
        color: #333;
    }

    #explanation h2 {
        color: #0056b3;
        margin-top: 0;
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    #explanation h3 {
        color: #555;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        margin-top: 10px;
        margin-bottom: 15px;
        padding-inline-start: 25px;
    }

    #explanation li {
        margin-bottom: 8px;
    }

     #rock-preview {
        margin-top: 20px;
        padding: 10px 15px;
        border: 1px dashed #007bff;
        border-radius: 5px;
        background-color: #eef7ff;
        text-align: center;
        width: 100%;
        box-sizing: border-box;
     }

     #rock-preview h4 {
         margin: 0 0 5px 0;
         color: #0056b3;
     }

     #rock-preview p {
         margin: 0;
         font-style: italic;
         color: #555;
     }


</style>

<script>
    const magmaDiv = document.getElementById('magma');
    const crystalContainer = document.getElementById('crystal-container');
    const coolingOverlay = document.getElementById('cooling-overlay'); // Added overlay
    const coolingRateSelect = document.getElementById('cooling-rate');
    const startSimButton = document.getElementById('start-sim');
    const resetSimButton = document.getElementById('reset-sim');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');
    const temperatureDisplay = document.getElementById('current-temp');
    const rockTypeDisplay = document.getElementById('rock-type');

    let animationFrameId = null;
    let startTime = null;
    let simulationDuration = 40000; // 40 seconds for the full simulation
    let isSimRunning = false;
    let crystals = []; // Store crystal data: { type, x, y, nucleationTime, element, mineralDef }

    // Define simulation duration as a CSS variable
    document.documentElement.style.setProperty('--sim-duration', `${simulationDuration / 1000}s`);


    // Mineral data with crystallization temp ranges (simulated, arbitrary units) and max size
    // Ranges are relative to the start/end temps of the sim
    const minerals = [
        { type: 'Olivine/Pyroxene', class: 'olivine-pyroxene', tempRange: [1200, 1050], maxSize: 30, legendColorClass: 'olivine-pyroxene-color' },
        { type: 'Plagioclase', class: 'plagioclase', tempRange: [1100, 800], maxSize: 25, legendColorClass: 'plagioclase-color' },
        { type: 'Biotite', class: 'biotite', tempRange: [900, 750], maxSize: 20, legendColorClass: 'biotite-color' },
        { type: 'K-Feldspar', class: 'k-feldspar', tempRange: [800, 650], maxSize: 35, legendColorClass: 'k-feldspar-color' },
        { type: 'Quartz', class: 'quartz', tempRange: [700, 550], maxSize: 40, legendColorClass: 'quartz-color' }
    ];

    // Cooling rate settings: temp range covered, nucleation probability multiplier, growth speed multiplier
    const coolingRates = {
        'very-slow': { tempEnd: 550, nucleationFactor: 1.5, growthFactor: 0.001, durationMultiplier: 2, rockType: 'סלע פלוטוני (גס גביש)' },
        'slow': { tempEnd: 600, nucleationFactor: 1.0, growthFactor: 0.0008, durationMultiplier: 1.5, rockType: 'סלע פלוטוני/בינוני (גס/בינוני גביש)' },
        'medium': { tempEnd: 750, nucleationFactor: 0.7, growthFactor: 0.0005, durationMultiplier: 1.0, rockType: 'סלע בינוני (דק גביש עם גבישים גדולים)' }, // Porphyritic texture
        'fast': { tempEnd: 900, nucleationFactor: 0.4, growthFactor: 0.0002, durationMultiplier: 0.7, rockType: 'סלע וולקני (דק גביש)' },
        'very-fast': { tempEnd: 1050, nucleationFactor: 0.1, growthFactor: 0.00005, durationMultiplier: 0.5, rockType: 'סלע וולקני (זכוכיתי/דק גביש מאוד)' } // May only get minimal or no crystals
    };
    const simTempStart = 1250; // Starting temp for all simulations

    // Initialize legend colors dynamically
    function initializeLegend() {
        minerals.forEach(mineral => {
            const legendSpan = document.querySelector(`.legend-color.${mineral.legendColorClass}`);
            if (legendSpan) {
                // Color is applied via CSS class, just ensure element exists
            }
        });
         // Add 'rest' color to legend dynamically if needed, or just keep it in CSS
         const restLegendSpan = document.querySelector('.legend-color.rest-color');
         if(!restLegendSpan) {
              const restItem = document.createElement('div');
              restItem.classList.add('legend-item');
              restItem.innerHTML = '<span class="legend-color rest-color"></span> מינרלים אחרים / זכוכית';
              document.getElementById('legend').appendChild(restItem); // Assuming rest color is needed
         }
    }


    function startSimulation() {
        if (isSimRunning) return;

        isSimRunning = true;
        startTime = performance.now();
        crystals = [];
        crystalContainer.innerHTML = ''; // Clear previous crystals

        const selectedRate = coolingRateSelect.value;
        const rateSetting = coolingRates[selectedRate];
        const currentSimDuration = simulationDuration * rateSetting.durationMultiplier;
        document.documentElement.style.setProperty('--sim-duration', `${currentSimDuration / 1000}s`);


        // Reset magma/overlay appearance and set transitions
        magmaDiv.style.transition = `opacity ${currentSimDuration / 1000}s linear, background ${currentSimDuration / 1000}s linear`;
        coolingOverlay.style.transition = `background-color ${currentSimDuration / 1000}s linear`;

        // Start hot state
        magmaDiv.style.opacity = 1;
        magmaDiv.style.background = 'linear-gradient(to bottom, rgba(255, 100, 0, 0.95), rgba(255, 50, 0, 0.8), rgba(200, 0, 0, 0.6))';
        coolingOverlay.style.backgroundColor = 'rgba(70, 90, 110, 0)'; // Start transparent

        // End cool state (matches rest/matrix color)
        // Need to delay setting the *end* state transition until the sim starts? Or just rely on progress calculation?
        // Let's rely on progress and manual updates for flexibility

        rockTypeDisplay.textContent = '... מתגבש ...';

        startSimButton.disabled = true;
        coolingRateSelect.disabled = true;
        resetSimButton.disabled = false;

        animationFrameId = requestAnimationFrame(updateSimulation);
    }

    function updateSimulation(currentTime) {
        if (!startTime) startTime = currentTime; // Initialize startTime on first frame

        const selectedRate = coolingRateSelect.value;
        const rateSetting = coolingRates[selectedRate];
        const currentSimDuration = simulationDuration * rateSetting.durationMultiplier;

        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / currentSimDuration, 1); // Progress from 0 to 1

        // Simple non-linear simulated temperature drop (cools faster at the beginning)
        const currentSimTemp = simTempStart - (simTempStart - rateSetting.tempEnd) * (1 - Math.cos(progress * Math.PI / 2)); // Ease-out quad

        // Update temperature display
        temperatureDisplay.textContent = Math.round(currentSimTemp);

         // Update magma appearance based on temperature/progress
         // Opacity decreases as solidification happens
         magmaDiv.style.opacity = Math.max(0.3, 1 - progress * 0.8); // Becomes less opaque
         // Background color shifts towards cooler shades
         const r = Math.max(50, 255 - progress * 200);
         const g = Math.max(50, 100 - progress * 50);
         const b = Math.max(50, 0 + progress * 50);
         magmaDiv.style.background = `linear-gradient(to bottom, rgba(${r}, ${g}, ${b}, ${magmaDiv.style.opacity}), rgba(${r*0.8}, ${g*0.8}, ${b*0.8}, ${magmaDiv.style.opacity*0.8}))`;

         // Update cooling overlay transparency
         coolingOverlay.style.backgroundColor = `rgba(70, 90, 110, ${progress * 0.4})`; // Blueish tint increases with cooling


        // Nucleate new crystals
        minerals.forEach(mineral => {
            // Check if current temp is within crystallization range for this mineral
            if (currentSimTemp <= mineral.tempRange[0] && currentSimTemp > mineral.tempRange[1]) {
                 // Nucleation chance: higher early in the temp range, higher with slower cooling, higher with less existing crystals nearby?
                 // Simple chance based on rate factor and position within mineral's temp range
                 const tempRangeFraction = (mineral.tempRange[0] - currentSimTemp) / (mineral.tempRange[0] - mineral.tempRange[1]); // 0 at start of range, 1 at end
                 const nucleationChance = rateSetting.nucleationFactor * (tempRangeFraction * 0.5 + 0.5) * (1/currentSimDuration) * 10000; // Adjusted for duration

                 if (Math.random() < nucleationChance) {
                     nucleateCrystal(mineral, elapsedTime);
                 }
            }
        });

        // Grow existing crystals
        crystals.forEach(crystal => {
             // Growth happens as long as temp is below the start temp of the mineral
             // Growth rate depends on cooling rate, time since nucleation, and current temperature relative to range
             if (currentSimTemp <= crystal.mineralDef.tempRange[0]) {
                 const timeSinceNucleation = elapsedTime - crystal.nucleationTime;
                 // Growth is proportional to time since nucleation and rate's growth factor
                 // And also faster when temp is within the mineral's range
                 const tempGrowthMultiplier = (currentSimTemp > crystal.mineralDef.tempRange[1]) ?
                                                (crystal.mineralDef.tempRange[0] - currentSimTemp) / (crystal.mineralDef.tempRange[0] - crystal.mineralDef.tempRange[1]) * 0.5 + 0.5 // Faster within range
                                                : 0.2; // Slower below range, if any growth is possible

                 const growth = timeSinceNucleation * rateSetting.growthFactor * tempGrowthMultiplier;
                 const newSize = Math.min(3 + growth, crystal.mineralDef.maxSize); // Start at 3px, grow up to max size

                 crystal.element.style.width = `${newSize}px`;
                 crystal.element.style.height = `${newSize}px`;
                 // Position is centered by transform: translate(-50%, -50%)
             }
        });

        if (progress < 1) {
            animationFrameId = requestAnimationFrame(updateSimulation);
        } else {
            endSimulation();
        }
    }

    function nucleateCrystal(mineral, currentTime) {
        const containerRect = crystalContainer.getBoundingClientRect();
        // Adjust nucleation area slightly inwards
        const safePadding = 15; // Avoid edges
        const x = safePadding + Math.random() * (containerRect.width - 2 * safePadding);
        const y = safePadding + Math.random() * (containerRect.height - 2 * safePadding);

        const crystalElement = document.createElement('div');
        crystalElement.classList.add('crystal', mineral.class);
        crystalElement.style.left = `${x}px`; // Position refers to the center due to transform
        crystalElement.style.top = `${y}px`;
        // Initial size and opacity set by CSS and animation
        crystalContainer.appendChild(crystalElement);

        crystals.push({
            type: mineral.type,
            x: x,
            y: y,
            nucleationTime: currentTime,
            element: crystalElement,
            mineralDef: mineral // Store mineral definition for growth logic
        });
    }

    function endSimulation() {
        isSimRunning = false;
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;

        // Final state cleanup/feedback
        temperatureDisplay.textContent = 'התגבש!';
        magmaDiv.style.transition = ''; // Remove transitions
        coolingOverlay.style.transition = ''; // Remove transitions

         // Add 'rest' matrix color if not fully crystallized (high tempEnd or fast cooling)
        const selectedRate = coolingRateSelect.value;
        const rateSetting = coolingRates[selectedRate];
        const finalTemp = simTempStart - (simTempStart - rateSetting.tempEnd); // Actual simulated end temp
        const totalCrystallizedArea = crystals.reduce((sum, c) => {
            const size = parseFloat(c.element.style.width); // Get final size
            return sum + (size/2) * (size/2) * Math.PI; // Approximate area (circle)
        }, 0);
        const containerArea = crystalContainer.offsetWidth * crystalContainer.offsetHeight;
        const crystallizationPercentage = Math.min(100, (totalCrystallizedArea / containerArea) * 150); // Arbitrary scaling for visual density
        const remainingMagmaOpacity = Math.max(0, 1 - crystallizationPercentage / 100); // Less crystals = more remaining magma look

        // Apply final matrix background based on crystallization level
        if (crystallizationPercentage < 95 && finalTemp > minerals[minerals.length -1].tempRange[1] ) { // If not fully cooled/crystallized down to Quartz range
             // Apply the 'rest' color as a background layer or part of the magma gradient
             // Simplest is to set the magma div background to the final state color if significant liquid remains
             magmaDiv.style.background = '#555'; // Dark grey for uncrystallized matrix/glass
             magmaDiv.style.opacity = 1; // Make it solid opaque

             // If we want to show crystals EMBEDDED in matrix, keep crystals and set background
             // crystalContainer.style.background = '#555'; // Alternatively, set background on crystal layer
             // magmaDiv.style.opacity = 0; // Hide original magma gradient
        } else {
             // If mostly crystallized, the background can represent densely packed crystals or lighter matrix
             magmaDiv.style.background = '#ccc'; // Lighter matrix color
             magmaDiv.style.opacity = 1;
        }
         // Ensure the cooling overlay is fully applied if sim finished
         coolingOverlay.style.backgroundColor = `rgba(70, 90, 110, 0.4)`;


        // Determine rock type based on average crystal size or rate setting
        const avgCrystalSize = crystals.length > 0 ?
                                crystals.reduce((sum, c) => sum + parseFloat(c.element.style.width), 0) / crystals.length
                                : 0;

        let rockDescription = rateSetting.rockType;
         if(crystals.length === 0 && selectedRate === 'very-fast') {
             rockDescription = 'זכוכית וולקנית (אובסידיאן)';
         } else if (crystals.length > 0 && avgCrystalSize < 5 && selectedRate !== 'very-fast') {
             rockDescription = `סלע וולקני (דק גביש מאוד) - נוצרו גבישים זעירים: ${crystals.length} בסה"כ`;
         } else if (avgCrystalSize >= 5 && avgCrystalSize < 15) {
             rockDescription += ` - גבישים קטנים-בינוניים (${crystals.length} בסה"כ)`;
         } else if (avgCrystalSize >= 15 && avgCrystalSize < 30) {
              rockDescription += ` - גבישים בינוניים-גדולים (${crystals.length} בסה"כ)`;
         } else if (avgCrystalSize >= 30) {
              rockDescription += ` - גבישים גדולים מאוד (${crystals.length} בסה"כ)`;
         } else if (crystals.length > 0) {
              rockDescription += ` - ${crystals.length} גבישים בסה"כ`;
         }


        rockTypeDisplay.textContent = `התגבשות הסתיימה! תוצאה: ${rockDescription}`;


        startSimButton.disabled = false;
        coolingRateSelect.disabled = false;
        resetSimButton.disabled = false;
    }

    function resetSimulation() {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
        isSimRunning = false;
        startTime = null;
        crystals = [];
        crystalContainer.innerHTML = ''; // Clear crystals

        // Reset magma/overlay appearance immediately, remove transitions
        magmaDiv.style.transition = '';
        coolingOverlay.style.transition = '';

        magmaDiv.style.opacity = 1; // Reset magma appearance
        magmaDiv.style.background = 'linear-gradient(to bottom, rgba(255, 140, 0, 0.9), rgba(255, 69, 0, 0.7), rgba(255, 0, 0, 0.5));'; // Reset magma color
        coolingOverlay.style.backgroundColor = 'rgba(70, 90, 110, 0)'; // Reset overlay

        temperatureDisplay.textContent = '...';
        rockTypeDisplay.textContent = '... מחכה לסימולציה ...';


        startSimButton.disabled = false;
        coolingRateSelect.disabled = false;
        resetSimButton.disabled = true;
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצצה אל מאחורי הקלעים (הסבר מדעי)';

        // Optional: Scroll to explanation if showing it
        if (isHidden) {
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Event listeners
    startSimButton.addEventListener('click', startSimulation);
    resetSimButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial state setup
    initializeLegend();
    resetSimulation(); // Set initial state on load

</script>
---