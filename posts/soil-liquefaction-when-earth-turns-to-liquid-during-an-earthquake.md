---
title: "האדמה שהופכת למרק: סימולציית גלישת קרקע ברעידת אדמה"
english_slug: soil-liquefaction-when-earth-turns-to-liquid-during-an-earthquake
category: "מדעי הסביבה / כדור הארץ"
tags: רעידת אדמה, גלישת קרקע, גיאולוגיה, סיכון סייסמי, הנדסה אזרחית
---
<p>רעידות אדמה הן אירוע טבעי ומפחיד, ומוכרות ביכולתן לגרום לנזק אדיר למבנים. אבל דמיינו שהקרקע עצמה עליה בנוי המבנה שלכם פשוט מאבדת את יציבותה והופכת לחומר דמוי נוזל תחת רגליו? זוהי גלישת קרקע, תופעה נפוצה והרסנית המתרחשת במהלך רעידות אדמה מסוימות. בואו נראה איך זה קורה בסימולציה קצרה.</p>

<div id="simulation-container">
    <div id="tank">
        <div id="water"></div>
        <div id="soil"></div>
        <div id="building">
            <div class="window"></div>
            <div class="window"></div>
            <div class="window"></div>
        </div>
        <div id="soil-surface-overlay"></div> <!-- For visual effects like bubbles/movement -->
        <div id="sand-boils-container"></div> <!-- Container for dynamic sand boils -->
    </div>
     <div id="controls">
        <button id="shake-button">התחל סימולציה</button>
    </div>
    <div id="status-message">ממתין לפעולה...</div>
</div>

<style>
/* גלובליים ותצוגת הקונטיינר */
#simulation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px auto;
    padding: 25px;
    border: 1px solid #ddd;
    border-radius: 12px;
    max-width: 450px;
    background-color: #f5f8fa; /* בהיר ואוורירי */
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    font-family: 'Arial', sans-serif; /* גופן נקי */
    position: relative; /* להכיל אלמנטים אבסולוטיים אם נרצה */
}

#tank {
    width: 250px; /* רוחב גדול יותר */
    height: 300px; /* גובה גדול יותר */
    border: 5px solid #5a67d8; /* צבע כחול סגול עשיר יותר */
    border-radius: 8px;
    position: relative;
    overflow: hidden;
    margin-bottom: 25px;
    background: linear-gradient(to bottom, rgba(173, 216, 230, 0.5), rgba(100, 149, 237, 0.4)); /* רקע כחול בהיר-בינוני לזכוכית */
    box-shadow: inset 0 0 15px rgba(0, 123, 255, 0.2); /* אפקט זכוכית פנימי */
}

#water {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 150px; /* מפלס מים קבוע */
    background-color: rgba(0, 123, 255, 0.6); /* כחול מעט שקוף */
    z-index: 0;
    /* הוספת אפקט מים עדין - קשה ללא SVG/Canvas, נשתמש בגרדיאנט או אנימציה פשוטה */
     background: linear-gradient(to top, rgba(0, 123, 255, 0.7), rgba(0, 123, 255, 0.3));
     filter: saturate(1.2); /* להדגיש מעט את הצבע */
}

#soil {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 200px; /* גובה שכבת הקרקע */
    background-color: #d2b48c; /* צבע חול/אדמה */
    z-index: 1;
    transition: background-color 1s ease-in-out, opacity 1s ease-in-out; /* מעבר חלק לצבע/שקיפות בעת גלישה */
    /* אפקט טקסטורה עדינה */
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0IiBoZWlnaHQ9IjQiPgo8cmVjdCB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSIjZDJiNGNjIj48L3JlY3Q+CjxjaXJjbGUgeD0iMSIgeT0iMSIgcj0iMC41IiBmaWxsPSIjY2JhMGE0Ij48L2NpcmNsZT4KPGNpcmNsZSB4PSIzIiB5PSIzIiByPSIwLjUiIGZpbGw9IiNjYmEwYTQiPjwvY2lyY2xlPgo8L3N2Zz4='); /* דוגמת גרגרים מינימלית */
    background-size: 4px 4px;
}

/* מצב קרקע נוזלית */
#soil.liquefied {
    background-color: #a08a6a; /* צבע כהה ורטוב יותר */
    opacity: 0.7; /* להראות מעט את המים שמתחת/מתערבבים */
     /* אפקט תנועה או בועות */
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2IiBoZWlnaHQ9IjYiPgo8cmVjdCB3aWR0aD0iNiIgaGVpZ2h0PSI2IiBmaWxsPSIjYTBsYThhNiI+PC9yZWN0Pgo8Y2lyY2xlIHg9IjMiIHk9IjMiIHI9IjEiIGZpbGw9IiM3NTY0NDQiIG9wYWNpdHk9IjAuNSI+PC9jaXJjbGU+Cjwvc3ZnPg=='); /* דוגמת 'בועות' או ערבוב */
    background-size: 6px 6px;
    animation: soil-disturb 1s infinite linear; /* אנימציה עדינה לערבוב */
}

@keyframes soil-disturb {
    0% { background-position: 0 0; }
    100% { background-position: 6px 6px; }
}


#building {
    position: absolute;
    bottom: 200px; /* התחלה מעל הקרקע */
    left: 50%;
    transform: translateX(-50%);
    width: 60px; /* רחב יותר */
    height: 80px; /* גבוה יותר */
    background-color: #7f8c8d; /* צבע בניין אפור נעים */
    border: 3px solid #2c3e50; /* בורדר כהה יותר */
    border-bottom: none; /* גג שטוח */
    z-index: 2;
    transition: bottom 4s ease-in, transform 4s ease-in; /* מעבר חלק לשקיעה והטיה אפשרית */
     box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
}

#building .window {
    width: 12px;
    height: 18px;
    background-color: #ecf0f1; /* צבע חלון בהיר */
    border: 1px solid #bdc3c7;
    position: absolute;
}

#building .window:nth-child(1) { top: 10px; left: 10px; }
#building .window:nth-child(2) { top: 10px; right: 10px; }
#building .window:nth-child(3) { top: 35px; left: 10px; }
/* ניתן להוסיף עוד חלונות */


/* מיקום הבניין לאחר שקיעה */
#building.sunk {
    bottom: 20px; /* שוקע נמוך יותר */
    transform: translateX(-50%) rotate(5deg); /* שוקע ומעט נוטה */
}


/* שכבת כיסוי לפני הקרקע לאפקטים עיליים */
#soil-surface-overlay {
    position: absolute;
    bottom: 200px; /* מתחיל מעל הקרקע */
    left: 0;
    width: 100%;
    height: 10px; /* שכבה דקה */
    z-index: 3; /* מעל הבניין */
    pointer-events: none; /* לא להפריע ללחיצות */
    opacity: 0; /* נסתר בהתחלה */
     transition: opacity 0.5s ease-in;
}

/* אפקט בעבוע/מזרקות קלות */
#soil-surface-overlay.active {
    opacity: 1;
     background: radial-gradient(circle at 50% 100%, rgba(0, 123, 255, 0.4) 0%, rgba(0, 123, 255, 0) 80%);
    animation: surface-boil 1.5s infinite linear; /* אנימציה עדינה של "הרתחה" */
}

@keyframes surface-boil {
    0% { transform: translateY(0); opacity: 1; }
    50% { transform: translateY(-3px); opacity: 0.8; }
    100% { transform: translateY(0); opacity: 1; }
}

/* קונטיינר למזרקות חול דינמיות */
#sand-boils-container {
    position: absolute;
    bottom: 200px; /* מעל הקרקע */
    left: 0;
    width: 100%;
    height: 30px; /* גובה אזור למזרקות */
    z-index: 4; /* מעל הכל */
    pointer-events: none;
    overflow: hidden; /* לחתוך מזרקות שיוצאות מהמסגרת */
}

/* סגנון למזרקת חול בודדת - תיווצר ב-JS */
.sand-boil {
    position: absolute;
    bottom: 0; /* מתחיל מהשכבה התחתונה של הקונטיינר */
    width: 8px;
    height: 8px;
    background-color: #cba0a4; /* צבע חול רטוב */
    border-radius: 50%; /* צורה עגולה */
    opacity: 0;
    transform: translate(-50%, 0) scale(0.5); /* מוסתר וקטן בהתחלה */
    animation: boil-erupt 1.5s ease-out forwards; /* אנימציית התפרצות */
}

@keyframes boil-erupt {
    0% { opacity: 0; transform: translate(-50%, 0) scale(0.5); }
    30% { opacity: 1; transform: translate(-50%, -10px) scale(1); }
    70% { opacity: 1; transform: translate(-50%, -25px) scale(0.8); }
    100% { opacity: 0; transform: translate(-50%, -30px) scale(0.6); }
}


#controls {
    margin-bottom: 15px;
}


#shake-button {
    padding: 12px 25px;
    font-size: 18px;
    cursor: pointer;
    background-color: #1abc9c; /* טורקיז ירוק מושך */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-weight: bold;
}

#shake-button:hover {
    background-color: #16a085;
}

#shake-button:active {
    transform: scale(0.98); /* אפקט לחיצה */
}

#shake-button:disabled {
    background-color: #bdc3c7; /* אפור בהיר */
    cursor: not-allowed;
    transform: scale(1);
}

#status-message {
    margin-top: 10px;
    font-size: 15px;
    color: #34495e; /* כחול אפור כהה */
    min-height: 1.5em; /* שמירת מקום לטקסט */
    text-align: center;
    font-style: italic;
}

/* Shaking Animation for the tank */
@keyframes shake {
  0% { transform: translateX(0) translateY(0); }
  25% { transform: translateX(-8px) translateY(3px); } /* טלטול משולב */
  50% { transform: translateX(8px) translateY(-3px); }
  75% { transform: translateX(-6px) translateY(2px); }
  100% { transform: translateX(0) translateY(0); }
}

.shaking #tank {
  animation: shake 0.4s ease-in-out infinite; /* אנימציה חזקה ומהירה יותר */
}

/* Explanation Styling */
#toggle-explanation {
    display: block; /* Make it a block element */
    margin: 25px auto; /* Center it */
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background-color: #3498db; /* כחול מעודן */
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    font-weight: normal;
}

#toggle-explanation:hover {
    background-color: #2980b9;
}

#explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px dashed #3498db;
    border-radius: 8px;
    background-color: #ecf0f1; /* רקע בהיר להסבר */
    line-height: 1.6; /* רווח שורות נוח לקריאה */
}

#explanation h2, #explanation h3 {
    color: #2c3e50; /* כותרות כהות */
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #bdc3c7; /* קו תחתון עדין */
    padding-bottom: 5px;
}

#explanation p {
    margin-bottom: 15px;
}

#explanation ul {
    margin-bottom: 15px;
    padding-left: 25px; /* הזחה לרשימה */
}

#explanation li {
    margin-bottom: 10px;
    line-height: 1.5;
}

#explanation strong {
    color: #e74c3c; /* הדגשה באדום לתנאים/השלכות */
}

</style>

<button id="toggle-explanation">הצג פרטים מדעיים</button>

<div id="explanation" style="display: none;">
    <h2>מהי גלישת קרקע (Liquefaction)?</h2>
    <p>דמיינו שקרקע יכולה להתנהג כמו נוזל צמיג לרגע קצר. זוהי בדיוק גלישת קרקע: תופעה בה <strong>קרקע רוויה במים</strong> מאבדת את חוזקה ויציבותה כתוצאה מטלטול פתאומי, לרוב ברעידת אדמה. במקום לשאת משקל, היא פשוט 'נמסה'.</p>

    <h2>מתי ולמה זה קורה?</h2>
    <p>התופעה דורשת צירוף של מספר גורמים:</p>
    <ul>
        <li>**סוג קרקע:** בדרך כלל מדובר בקרקעות גרגיריות (שאינן מלוכדות, כמו חול או טין) שבהן החללים בין הגרגרים יחסית גדולים.</li>
        <li>**נוכחות מים:** מפלס מי התהום חייב להיות גבוה, כך שמרבית החללים בקרקע מלאים במים.</li>
        <li>**טלטול חזק:** רעידת אדמה עוצמתית מספקת אנרגיה כדי לגרום לגרגירים לאבד מגע זה עם זה.</li>
    </ul>
    <p><strong>התהליך הפיזיקלי:</strong> בקרקע רגילה, גרגירי החול או הטין נוגעים זה בזה ונושאים את העומס (משקל המבנה והקרקע) באמצעות חיכוך. כאשר מגיעים גלי הרעידה, הם גורמים לגרגרים לזוז ולהתארגן מחדש במהירות. הסידור מחדש הזה מקטין את הנפח הכולל של הקרקע אך המים הכלואים בתוך החללים אינם יכולים לצאת החוצה במהירות. הדבר גורם לעלייה דרמטית בלחץ המים בתוך הנקבוביות. הלחץ העולה של המים למעשה "דוחף" את הגרגרים זה מזה ומפחית את הלחץ היעיל שפועל בין הגרגרים. כשהלחץ היעיל מתקרב לאפס, הקרקע מאבדת את חוזק הגזירה שלה לחלוטין ומתנהגת כמו נוזל. מים וחול עשויים אף לפרוץ לפני השטח במזרקות הנקראות "מזרקות חול" (sand boils).</p>

    <h2>ההשלכות על מבנים ותשתיות</h2>
    <p>קרקע שאינה יציבה היא מתכון לאסון עבור כל מה שבנוי עליה או בתוכה:</p>
    <ul>
        <li>**שקיעה והטיה:** מבנים כבדים כמו בתים ובניינים יכולים לשקוע לתוך הקרקע "הנוזלית" או להטות בצורה מסוכנת.</li>
        <li>**ציפה:** מבנים קלים יחסית או אלמנטים תת-קרקעיים (כמו צינורות ביוב או מיכלים) עלולים לצוף כלפי מעלה.</li>
        <li>**התפשטות לרוחב (Lateral Spreading):** גושי קרקע נוזלית על שיפועים עדינים יכולים לנוע לרוחב ולגרום נזק לגשרים, כבישים וצנרת תת-קרקעית.</li>
        <li>**כשל מדרונות:** במדרונות תלולים יותר, גלישת קרקע יכולה להוביל למפולות קרקע הרסניות.</li>
    </ul>

    <h2>כיצד מתמודדים עם הסיכון?</h2>
    <p>מהנדסי קרקע פיתחו שיטות שונות כדי לצמצם את הסיכון באזורים פגיעים:</p>
    <ul>
        <li>**שיפור הקרקע:** הגדלת צפיפות הקרקע (למשל על ידי דחיסה) או הזרקת חומרים לתוכה כדי לחבר את הגרגרים.</li>
        <li>**ניקוז:** יצירת נתיבים למים להתפזר במהירות במהלך הרעידה ומניעת עליית לחץ מי הנקבוביות.</li>
        <li>**יסודות עמוקים:** בניית יסודות (כמו כלונסאות) שחודרים דרך שכבת הקרקע הפגיעה ומגיעים לשכבה יציבה ועמוקה יותר.</li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const shakeButton = document.getElementById('shake-button');
    const tank = document.getElementById('tank');
    const soil = document.getElementById('soil');
    const building = document.getElementById('building');
    const statusMessage = document.getElementById('status-message');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const sandBoilsContainer = document.getElementById('sand-boils-container');
    const soilSurfaceOverlay = document.getElementById('soil-surface-overlay');


    // Initial state constants
    const initialBuildingBottom = 200; // Corresponds to initial soil height
    const finalBuildingBottom = 20; // Arbitrary low value near tank bottom
    const shakeDuration = 2000; // Duration of shaking animation in ms
    const liquefactionStartDelay = 1000; // Delay after shaking starts before liquefaction visuals begin
    const sinkingDuration = 4000; // Matches CSS transition duration for sinking

    // State variables
    let simulationActive = false;
    let sandBoilInterval = null;

    // --- Helper Functions ---

    // Function to create and animate a single sand boil
    function createSandBoil() {
        const boil = document.createElement('div');
        boil.classList.add('sand-boil');

        // Random horizontal position within the tank
        const randomLeft = Math.random() * 90 + 5; // 5% to 95% width
        boil.style.left = randomLeft + '%';

        sandBoilsContainer.appendChild(boil);

        // Remove the element after its animation finishes
        boil.addEventListener('animationend', () => {
            boil.remove();
        });
    }

    // Function to start creating sand boils periodically
    function startSandBoils() {
        // Clear any existing interval
        stopSandBoils();
        // Create boils every X milliseconds
        sandBoilInterval = setInterval(createSandBoil, 300); // Adjust frequency
        // Create a few immediately
         for (let i = 0; i < 3; i++) {
            // Add slight delay for initial boils
             setTimeout(createSandBoil, i * 100);
         }
    }

    // Function to stop creating sand boils
    function stopSandBoils() {
        if (sandBoilInterval) {
            clearInterval(sandBoilInterval);
            sandBoilInterval = null;
        }
         // Remove any leftover boils
         sandBoilsContainer.innerHTML = '';
    }


    // --- Simulation Logic ---

    // Reset function
    function resetSimulation() {
        simulationActive = false;

        // Reset building position and state
        building.style.transition = 'none'; // Disable transition for reset
        building.style.bottom = initialBuildingBottom + 'px';
        building.classList.remove('sunk');

        // Reset soil state
        soil.classList.remove('liquefied');
        soilSurfaceOverlay.classList.remove('active'); // Hide surface effect

        // Stop and remove sand boils
        stopSandBoils();


        // Reset tank animation
        tank.classList.remove('shaking');

        // Reset status message
        statusMessage.textContent = 'ממתין לפעולה...';

        // Reset button state and text
        shakeButton.disabled = false;
        shakeButton.textContent = 'התחל סימולציה';

        // Force reflow to apply transition: none before re-enabling
        void building.offsetWidth;
        // Re-enable building transition
        building.style.transition = `bottom ${sinkingDuration / 1000}s ease-in, transform ${sinkingDuration / 1000}s ease-in`;
    }

    // Event listener for shake button
    shakeButton.addEventListener('click', () => {
        // If simulation is already active (shaking or sinking), do nothing
        if (simulationActive) {
            return;
        }

        // If the button says "הפעל מחדש", call reset and return
        if (shakeButton.textContent === 'הפעל מחדש') {
             resetSimulation();
             return;
        }

        // --- Start new simulation ---
        simulationActive = true;
        shakeButton.disabled = true;
        shakeButton.textContent = '...רעידת אדמה מתרחשת...'; // Update button text to indicate process

        // 1. Start Shaking
        statusMessage.textContent = '...טלטול חזק מתחיל...';
        tank.classList.add('shaking');


        // 2. After a delay, start liquefaction visuals and sinking
        setTimeout(() => {
             // Stop shaking animation
             tank.classList.remove('shaking');
             statusMessage.textContent = '...הקרקע מאבדת יציבות...';

            // Apply liquefied state to soil visuals
            soil.classList.add('liquefied');
            soilSurfaceOverlay.classList.add('active'); // Activate surface effect

            // Start sand boils
            startSandBoils();

            // Start building sinking animation
            building.classList.add('sunk');
             statusMessage.textContent = '...המבנה שוקע...';

            // 3. After sinking animation ends, update status and button
            setTimeout(() => {
                // Stop sand boils and surface effect once simulation state stabilizes
                stopSandBoils();
                 soilSurfaceOverlay.classList.remove('active'); // Ensure surface effect stops

                statusMessage.textContent = 'המבנה שקע עקב גלישת קרקע!'; // Final message

                // Enable button again for reset/replay
                shakeButton.textContent = 'הפעל מחדש';
                shakeButton.disabled = false;
                simulationActive = false; // Simulation ended

            }, sinkingDuration); // Matches the CSS transition duration

        }, shakeDuration); // Duration of shaking before liquefaction starts visuals and sinking
    });


    // --- Explanation Toggle ---
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר פרטים מדעיים' : 'הצג פרטים מדעיים';
    });

    // --- Initial Setup ---
    resetSimulation(); // Ensure simulation is in a clean state on load
});
</script>
```