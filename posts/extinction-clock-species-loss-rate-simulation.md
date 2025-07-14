---
title: "שעון ההכחדה: הדמיית קצב אובדן מינים"
english_slug: extinction-clock-species-loss-rate-simulation
category: "אקולוגיה"
tags:
  - הכחדה
  - מינים בסכנה
  - מגוון ביולוגי
  - משבר אקלים
  - שימור טבע
---
# שעון ההכחדה: הדמיית קצב אובדן מינים
האם תהיתם פעם איך נראה קצב הכחדת המינים המואץ בעולם שלנו, שמדענים רבים מכנים "גל ההכחדה השישי"? קצב זה, המושפע בעיקר מפעילות אנושית, מהיר פי עשרות ואף מאות מקצב ההכחדה הטבעי. בואו נדמה אותו לרגע באמצעות "שעון ההכחדה".

<div id="extinction-app-container">
    <h2>שעון הכחדה מואץ</h2>
    <div class="display-area">
        <div id="clock-display" class="display-box time-display">זמן מדומה: מתחיל ב-1900</div>
        <div id="species-counter" class="display-box species-count">מינים שנכחדו (משוער): 0</div>
    </div>
    <button id="start-simulation">הפעל את השעון (הדמיה מ-1900 ועד היום)</button>
    <p id="simulation-note">ההדמיה מציגה אומדן מופשט ומואץ דרמטית של קצב אובדן מינים לאורך תקופה של מעל 120 שנים. זהו פישוט לצורך המחשה.</p>
</div>

<button id="toggle-explanation" class="toggle-btn">הצג מידע נוסף על הכחדה</button>
<div id="explanation" class="explanation-section">
    <h2>הסיפור המלא: מהי הכחדה וגל ההכחדה השישי?</h2>
    <h3>הכחדה: תהליך טבעי שהפך למשבר</h3>
    <p>הכחדה היא חלק ממחזור החיים על פני כדור הארץ. מינים נעלמים באופן טבעי עקב שינויים איטיים בסביבה ותהליכים אבולוציוניים. אולם, ההיסטוריה הגיאולוגית מראה גם גלי הכחדה המוניים ומהירים יותר, שנגרמו מאסונות טבע עצומים.</p>
    <h3>הגלים הגדולים בהיסטוריה</h3>
    <p>עד היום תועדו לפחות חמישה אירועי הכחדה המוניים, בהם אחוז עצום מהמינים על פני כדור הארץ נעלמו. הידוע שבהם התרחש לפני כ-66 מיליון שנה וסיים את עידן הדינוזאורים (הלא-עופיים).</p>
    <h3>גל ההכחדה השישי: אנחנו הסיבה?</h3>
    <p>מדענים רבים מצביעים על כך שאנו נמצאים כיום בעיצומו של גל הכחדה שישי - אך הפעם, הגורם העיקרי הוא האדם. קצב אובדן המינים הנוכחי גבוה פי 100 עד 1000 מקצב ההכחדה הטבעי, ורבים מהמינים נכחדים לפני שבכלל הספקנו לגלות או לחקור אותם.</p>
    <h3>למה זה קורה? הגורמים העיקריים</h3>
    <p>הסיבות העיקריות למשבר הן: **הרס בתי גידול** (חקלאות, ערים, תשתיות), **ניצול יתר** (ציד, דיג, קציר לא-בר-קיימא), **שינויי אקלים** (הנגרמים מפליטת גזי חממה), **זיהום** (אוויר, מים, קרקע) ו**מינים פולשים** (המתחרים ופוגעים במינים מקומיים).</p>
    <h3>מדוע אכפת לנו? השלכות אובדן המגוון הביולוגי</h3>
    <p>אובדן מינים הוא לא רק טרגדיה אקולוגית. הוא פוגע ישירות במערכות התומכות בחיים שלנו: אספקת מזון ומים נקיים, אקלים יציב, תרופות, ואפילו איכות האוויר שאנו נושמים. מגוון ביולוגי עשיר הוא הבסיס למערכות אקולוגיות בריאות ויציבות, החיוניות לשגשוג האנושות.</p>
    <h3>מה ניתן לעשות? פעולות לשימור</h3>
    <p>החדשות הטובות הן שניתן לפעול. שימור והגנה על בתי גידול, מעבר לאנרגיה מתחדשת, צמצום צריכה וזיהום, ניהול בר-קיימא של משאבי טבע והעלאת מודעות ציבורית - כל אלה צעדים חיוניים להאטת הקצב ושיקום המערכות הטבעיות של כדור הארץ.</p>
</div>

<style>
    /* כללי */
    #extinction-app-container {
        font-family: 'Arial', sans-serif; /* נניח פונט כללי */
        text-align: center;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #d3d3d3;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 600px;
    }

    #extinction-app-container h2 {
        color: #333;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    .display-area {
        display: flex;
        flex-direction: column; /* ערימה במובייל */
        gap: 15px; /* רווח בין הקופסאות */
        margin-bottom: 20px;
    }

    @media (min-width: 600px) { /* בשולחן עבודה */
        .display-area {
            flex-direction: row;
            justify-content: center;
        }
        .display-box {
             flex: 1; /* יתפרסו באופן שווה */
        }
    }

    .display-box {
        font-size: 1.3em;
        padding: 15px 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #f0f0f0; /* רקע בהיר יותר */
        min-width: 220px;
        text-align: center;
        overflow: hidden; /* למקרה של גלישה */
        white-space: nowrap; /* למנוע שבירת שורה */
        text-overflow: ellipsis; /* הוספת שלוש נקודות בגלישה */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.08);
    }

    .time-display {
         color: #555; /* צבע ניטרלי יותר לזמן */
    }

    .species-count {
        color: #c0392b; /* אדום דרמטי יותר */
        font-weight: bold;
        transition: color 0.3s ease-in-out; /* מעבר צבע חלק */
    }

    /* אנימציה עדינה למונה כשהוא מתעדכן */
    .species-count.pulse {
        animation: pulse-red 0.5s ease-out;
    }

    @keyframes pulse-red {
        0% { transform: scale(1); color: #c0392b; }
        50% { transform: scale(1.05); color: #e74c3c; }
        100% { transform: scale(1); color: #c0392b; }
    }


    /* כפתור הדמיה */
    #start-simulation {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        margin-top: 15px;
        background-color: #2ecc71; /* ירוק מודרני */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #start-simulation:hover:not(:disabled) {
        background-color: #27ae60;
        transform: translateY(-2px); /* אפקט הרמה קל */
    }

     #start-simulation:active:not(:disabled) {
        transform: translateY(0); /* אפקט לחיצה */
    }

    #start-simulation:disabled {
        background-color: #bdc3c7; /* אפור בהיר */
        cursor: not-allowed;
        opacity: 0.7;
    }

    #simulation-note {
        font-size: 0.9em;
        color: #7f8c8d; /* אפור עדין */
        margin-top: 15px;
        line-height: 1.4;
    }

    /* הסבר מורחב */
    .toggle-btn {
        display: block;
        margin: 30px auto 20px auto;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #3498db; /* כחול מרענן */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
    .toggle-btn:hover {
         background-color: #2980b9;
         transform: translateY(-1px);
    }
     .toggle-btn:active {
        transform: translateY(0);
    }

    .explanation-section {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #d3d3d3;
        border-radius: 10px;
        background-color: #f9f9f9; /* רקע מעט שונה מהאפליקציה */
        text-align: right; /* RTL */
        line-height: 1.6;
        color: #333;
        opacity: 0; /* התחלה שקופה לאנימציה */
        max-height: 0; /* התחלה נסתרת */
        overflow: hidden;
        transition: opacity 0.5s ease-in-out, max-height 0.5s ease-in-out; /* אנימציית הצגה/הסתרה */
    }
    .explanation-section.visible {
        opacity: 1;
        max-height: 1000px; /* גובה מספיק גדול כדי להכיל את התוכן */
    }


    .explanation-section h2, .explanation-section h3 {
        color: #333;
        margin-bottom: 15px;
    }
     .explanation-section h3 {
         font-size: 1.2em;
         margin-top: 20px;
         border-bottom: 1px dashed #ccc; /* קו תחתון עדין לכותרות משנה */
         padding-bottom: 5px;
     }
</style>

<script>
    const startTime = new Date('1900-01-01T00:00:00Z'); // Start of simulation period
    const endTime = new Date(); // Today
    const totalSimulatedTime = endTime.getTime() - startTime.getTime(); // Total time span in ms
    const totalSimulatedExtinctions = 50000; // Example: Estimate ~50,000 species extinct since 1900 - KEEP THIS AS A SIMULATION VALUE
    const simulationDurationRealTime = 30000; // Simulate over 30 seconds in real time (ms) - MADE IT SLIGHTLY FASTER FOR IMPACT

    const clockDisplay = document.getElementById('clock-display');
    const speciesCounter = document.getElementById('species-counter');
    const startButton = document.getElementById('start-simulation');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    let animationStartTime = null;
    let isRunning = false;
    let animationFrameId = null;
    let lastExtinctionCount = 0; // To track when the counter increments

    function updateSimulation(currentTime) {
        if (!animationStartTime) {
            animationStartTime = currentTime;
        }

        const elapsedTimeReal = currentTime - animationStartTime;
        const progress = Math.min(elapsedTimeReal / simulationDurationRealTime, 1); // Progress from 0 to 1

        const currentSimulatedTime = startTime.getTime() + totalSimulatedTime * progress;
        const currentExtinctions = Math.round(totalSimulatedExtinctions * progress);

        // Update clock display
        const simulatedDate = new Date(currentSimulatedTime);
        // Format date nicely
        clockDisplay.textContent = `זמן מדומה: ${simulatedDate.toLocaleDateString('he-IL', { year: 'numeric', month: 'long', day: 'numeric' })}`;

        // Update counter display and trigger animation if count increased
        if (currentExtinctions > lastExtinctionCount) {
             // Remove pulse class immediately, re-add after a short delay to ensure re-trigger
            speciesCounter.classList.remove('pulse');
            // Use setTimeout 0 to allow reflow, then add class back
            setTimeout(() => {
                 speciesCounter.textContent = `מינים שנכחדו (משוער): ${currentExtinctions.toLocaleString('he-IL')}`;
                 speciesCounter.classList.add('pulse');
            }, 0); // Timeout 0 allows it to happen on the next repaint
            lastExtinctionCount = currentExtinctions;
        } else {
             // Update text even if not pulsing, important for the final count
            speciesCounter.textContent = `מינים שנכחדו (משוער): ${currentExtinctions.toLocaleString('he-IL')}`;
        }


        if (progress < 1) {
            animationFrameId = requestAnimationFrame(updateSimulation);
        } else {
            isRunning = false;
            startButton.textContent = 'ההדמיה הסתיימה';
            startButton.disabled = true;
             // Ensure the final count is displayed correctly
            speciesCounter.textContent = `מינים שנכחדו (משוער): ${totalSimulatedExtinctions.toLocaleString('he-IL')}`;
            cancelAnimationFrame(animationFrameId); // Ensure cleanup
        }
    }

    startButton.addEventListener('click', () => {
        if (!isRunning) {
            isRunning = true;
            animationStartTime = null; // Reset animation start time
            startButton.textContent = 'הדמיה בעיצומה...';
            startButton.disabled = true;
            // Reset displays for new simulation
            const initialDate = new Date(startTime);
            clockDisplay.textContent = `זמן מדומה: ${initialDate.toLocaleDateString('he-IL', { year: 'numeric', month: 'long', day: 'numeric' })}`;
            speciesCounter.textContent = `מינים שנכחדו (משוער): 0`;
            lastExtinctionCount = 0; // Reset tracking
            speciesCounter.classList.remove('pulse'); // Ensure no residual animation class
            animationFrameId = requestAnimationFrame(updateSimulation);
        }
    });

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('visible');
        if (isHidden) {
            explanationDiv.classList.remove('visible');
            toggleButton.textContent = 'הצג מידע נוסף על הכחדה';
        } else {
            explanationDiv.classList.add('visible');
            toggleButton.textContent = 'הסתר מידע נוסף';
        }
    });

    // Initial display state
    const initialDate = new Date(startTime);
    clockDisplay.textContent = `זמן מדומה: ${initialDate.toLocaleDateString('he-IL', { year: 'numeric', month: 'long', day: 'numeric' })}`;
    speciesCounter.textContent = `מינים שנכחדו (משוער): 0`;


</script>
---