---
title: "מסע פלאי: כך הדם שלנו נקריש ונעצור דימום"
english_slug: marvelous-journey-how-blood-clots-and-stops-bleeding
category: "ביולוגיה"
tags: ["קרישת דם", "המוסטאזיס", "טסיות דם", "פיברין", "פקטורי קרישה", "סימולציה", "אינטראקטיבי"]
---
# מסע פלאי: כך הדם שלנו נקריש ונעצור דימום

הופס! חתך קטן באצבע, או שריטה בברך. זה קורה מהר, קצת כואב, והדם מתחיל לזרום... האם ידעת שתוך שניות בודדות, הגוף שלך מפעיל מנגנון הצלה מדהים כדי לעצור את הדימום ולאחות את הפצע? בוא נצא למסע בזעיר אנפין ונראה איך הקסם הזה קורה!

<div class="blood-clotting-simulation">
    <div class="vessel-container">
        <div class="vessel-wall top-wall"></div>
        <div class="vessel-wall bottom-wall"></div>
        <div class="injury"></div>
        <div class="blood-flow">
            <!-- Blood cells will be generated by JS -->
        </div>
        <div class="platelet-area"></div>
        <div class="cascade-area"></div>
        <div class="fibrin-area"></div>
        <div class="clot-area"></div>
    </div>
    <div class="controls">
        <button id="actionBtn">התחל מסע!</button>
        <button id="resetSimBtn" style="display:none;">התחל מחדש</button>
    </div>
    <div class="messages"></div>
</div>

<style>
:root {
    --vessel-color: #e74c3c; /* Arterial red */
    --wall-color: #c0392b; /* Darker red */
    --platelet-color: #f1c40f; /* Yellow */
    --cascade-color: #3498db; /* Blue */
    --fibrin-color: #2ecc71; /* Green */
    --clot-color: rgba(192, 57, 43, 0.9); /* Dark red, semi-transparent */
    --background-color: #ecf0f1; /* Light gray */
    --border-color: #bdc3c7; /* Gray border */
    --text-color: #34495e; /* Dark text */
    --button-color: #3498db; /* Blue button */
    --button-hover-color: #2980b9;
    --button-text-color: white;
}

.blood-clotting-simulation {
    width: 100%;
    max-width: 650px; /* Slightly wider */
    margin: 30px auto;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 25px; /* More padding */
    box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* Softer, larger shadow */
    background-color: var(--background-color);
    position: relative;
    direction: rtl;
    text-align: right;
    font-family: 'Arial', sans-serif; /* Better font */
    overflow: hidden; /* Hide overflowing animations briefly */
}

.vessel-container {
    width: 95%; /* Slightly less than 100% */
    margin: 0 auto;
    height: 180px; /* Taller vessel */
    position: relative;
    overflow: hidden;
    margin-bottom: 25px;
    border-radius: 5px;
    background: linear-gradient(to right, #f0f0f0, #ffffff, #f0f0f0); /* Brighter background */
}

.vessel-wall {
    position: absolute;
    width: 100%;
    height: 25px; /* Thicker walls */
    background-color: var(--wall-color);
    z-index: 10;
}

.top-wall {
    top: 0;
    left: 0;
    border-bottom: 2px solid rgba(0,0,0,0.1);
}

.bottom-wall {
    bottom: 0;
    left: 0;
    border-top: 2px solid rgba(0,0,0,0.1);
}

.injury {
    position: absolute;
    top: 25px; /* Below top wall */
    left: 50%; /* Center horizontally */
    transform: translateX(-50%);
    width: 50px; /* Wider injury */
    height: calc(100% - 50px); /* Between walls */
    background-color: rgba(var(--vessel-color), 0.1); /* Represents the wound opening */
    border-left: 3px dashed var(--vessel-color); /* Visual cue for rupture */
    border-right: 3px dashed var(--vessel-color);
    z-index: 5;
    box-sizing: border-box; /* Include border in size */
}

.blood-flow {
    position: absolute;
    top: 25px; /* Inside the vessel */
    left: 0;
    width: 100%;
    height: calc(100% - 50px);
    overflow: hidden;
    z-index: 3;
}

.blood-cell {
    position: absolute;
    width: 10px; /* Larger blood cells */
    height: 10px;
    background-color: var(--vessel-color);
    border-radius: 50%;
    animation: flow linear infinite;
    opacity: 0.9;
    box-shadow: inset 0 0 2px rgba(0,0,0,0.2); /* Simple inner shadow */
}

@keyframes flow {
    0% { transform: translateX(-20px); } /* Start further left */
    100% { transform: translateX(calc(100% + 20px)); } /* End further right */
}

/* Blood cell distribution and animation timing - managed by JS for better control */


.platelet-area {
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px; /* Wider than injury for buildup */
    height: calc(100% - 50px);
    z-index: 6;
    overflow: hidden;
    pointer-events: none; /* Don't block clicks */
}

.platelet {
    position: absolute;
    width: 12px; /* Larger platelets */
    height: 12px;
    background-color: var(--platelet-color);
    border-radius: 4px; /* Slightly rounded square */
    box-shadow: 0 0 4px rgba(0,0,0,0.3);
    opacity: 0; /* Start hidden */
    transition: transform 0.8s ease-out, opacity 0.6s ease-out; /* Smoother transition */
    transform: scale(0.5); /* Start small */
}

.cascade-area {
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px; /* Wider area for cascade visualization */
    height: calc(100% - 50px);
    z-index: 7;
    pointer-events: none;
    display: flex; /* Use flexbox for abstract layout */
    align-items: center;
    justify-content: center;
}

.cascade-step {
    width: 20px; /* Larger step indicators */
    height: 20px;
    background-color: var(--cascade-color);
    border-radius: 50%;
    opacity: 0;
    transform: scale(0); /* Start invisible and small */
    margin: 0 5px; /* Space between steps */
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
}


.fibrin-area {
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);
    width: 90px; /* Area where fibrin forms */
    height: calc(100% - 50px);
    z-index: 8;
    overflow: hidden;
}

.fibrin-strand {
    position: absolute;
    width: 3px; /* Thicker strands */
    height: 0;
    background-color: var(--fibrin-color);
    opacity: 0.7; /* Slightly less opaque */
    transform-origin: top center;
}

.clot-area {
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%);
    width: 0; /* Start with no width */
    height: calc(100% - 50px);
    background-color: var(--clot-color);
    z-index: 9;
    border-radius: 8px; /* More rounded clot */
    overflow: hidden;
    transition: width 1.2s ease-out, opacity 0.8s ease-out; /* Smoother and longer width animation */
    opacity: 0; /* Start hidden */
    display: flex; /* Use flex for trapped cells */
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    padding: 5px; /* Inner padding */
    box-sizing: border-box;
}

.clot-cell {
    width: 8px;
    height: 8px;
    background-color: rgba(var(--vessel-color), 0.7); /* Trapped blood cells */
    border-radius: 50%;
    margin: 2px; /* Space between trapped cells */
    opacity: 0.8;
    transition: opacity 0.5s ease-in;
}


.controls {
    text-align: center;
    margin-bottom: 25px;
}

.controls button {
    padding: 12px 25px; /* Larger buttons */
    font-size: 1.1em;
    cursor: pointer;
    margin: 0 8px;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
}

#actionBtn {
    background-color: var(--button-color);
    color: var(--button-text-color);
}

#actionBtn:hover {
    background-color: var(--button-hover-color);
}
#actionBtn:active {
    transform: scale(0.98);
}


#resetSimBtn {
     background-color: var(--border-color);
    color: var(--text-color);
}
#resetSimBtn:hover {
    background-color: #b0b6ba;
}
#resetSimBtn:active {
    transform: scale(0.98);
}


.messages {
    position: absolute;
    bottom: 10px; /* Position above padding */
    left: 20px; /* Add left/right padding */
    right: 20px;
    text-align: center;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.95); /* More opaque background */
    border-top: 1px solid #eee;
    border-radius: 5px;
    min-height: 30px;
    font-size: 1em; /* Larger font */
    color: var(--text-color);
    opacity: 0; /* Start hidden */
    transition: opacity 0.5s ease-in-out;
    z-index: 20; /* Above other elements */
}

.explanation-section {
    margin-top: 40px; /* More space */
    padding-top: 25px;
    border-top: 2px solid var(--border-color); /* Thicker border */
    display: none;
    color: var(--text-color);
    font-family: 'Arial', sans-serif;
    line-height: 1.7;
}

.explanation-section h2 {
    color: var(--wall-color); /* Themed color */
    border-bottom: 2px solid var(--vessel-color);
    padding-bottom: 8px;
    margin-bottom: 20px;
    font-size: 1.8em;
}
.explanation-section h3 {
     color: var(--button-hover-color); /* Themed color */
     margin-top: 20px;
     margin-bottom: 10px;
     font-size: 1.3em;
}


.explanation-section ul, .explanation-section ol {
    padding-right: 25px; /* More padding */
}

.explanation-section li {
    margin-bottom: 12px; /* More space between list items */
}

.explanation-section strong {
    color: var(--text-color);
}


#toggleExplanationBtn {
    display: block;
    width: fit-content;
    margin: 25px auto; /* More space */
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    border: 1px solid var(--border-color);
    border-radius: 5px;
    background-color: white;
    color: var(--text-color);
    transition: background-color 0.2s ease, color 0.2s ease;
}
#toggleExplanationBtn:hover {
    background-color: #f0f0f0;
    color: #000;
}
#toggleExplanationBtn:active {
    transform: scale(0.98);
}

</style>

<button id="toggleExplanationBtn">הצג/הסתר הסבר מעמיק</button>

<div class="explanation-section" id="explanation">
    <h2>הסבר: קרישת דם והמוסטאזיס</h2>
    <p>תהליך קרישת הדם, או בשמו המקצועי המוסטאזיס (עצירת דימום), הוא אחד הפלאים בגופנו. זהו מנגנון הגנה חיוני שמטרתו העליונה היא לעצור איבוד דם בעקבות פגיעה ולשמור על תקינות מערכת הדם.</p>

    <h3>למה זה כל כך חשוב?</h3>
    <ul>
        <li>**שמירה על הנפח:** מניעת איבוד דם גם מחתך קטן יכולה להיות קריטית, ועל אחת כמה וכמה בפציעות גדולות יותר.</li>
        <li>**שמירה על הלחץ:** נפח דם תקין חיוני לשמירה על לחץ דם יציב ולאספקת חמצן וחומרים חיוניים לכל תאי הגוף.</li>
        <li>**הכנה לריפוי:** הקריש שנוצר לא רק אוטם את הפצע אלא גם מספק "פיגום" ראשוני לתאים שיגיעו אחר כך כדי לתקן את הרקמה הפגועה.</li>
    </ul>

    <h3>השחקנים המרכזיים במגרש</h3>
    <p>כדי להבין את הסימולציה שראינו, בואו נכיר את הגיבורים הראשיים של תהליך הקרישה:</p>
    <ul>
        <li>**טסיות דם (Platelets):** אלו לא תאים של ממש, אלא שברי תאים זעירים חסרי גרעין, שנוצרים באופן קבוע במח העצם. הן פועלות כמו 'חיילים' שמגיעים ראשונים לאזור הפציעה. הן מרגישות את הפגיעה (באמצעות היחשפות לחלבונים בדופן כלי הדם הפגוע, כמו קולגן), נדבקות לאזור ולעצמן, ויוצרות פקק ראשוני, כמו 'אטם' רך.</li>
        <li>**פקטורי קרישה (Coagulation Factors):** זוהי תזמורת של חלבונים שונים (יש יותר מתריסר כאלה, המסומנים לרוב בספרות רומיות) המומסים בפלזמת הדם (החלק הנוזלי של הדם). כשאזור הפציעה 'חושף' אותם לחומרים מסוימים, הם מתחילים להפעיל זה את זה בסדרה מורכבת של תגובות שרשרת – זהו "מסלול הקרישה".</li>
        <li>**פיברינוגן (Fibrinogen) ופיברין (Fibrin):** פיברינוגן הוא אחד החלבונים הללו (פקטור I), והוא נמצא בפלזמה בצורתו המסיסה. השלב המרכזי במסלול הקרישה מוביל ליצירת אנזים בשם תרומבין (Thrombin). תרומבין הוא ה'מפתח' שהופך את הפיברינוגן המסיס לפיברין - חלבון בלתי מסיס היוצר סיבים עדינים אך חזקים.</li>
    </ul>

    <h3>שלבי האקשן: מסע הקרישה</h3>
    <p>הסימולציה הראתה את השלבים המרכזיים, בואו נעבור עליהם שוב:</p>
    <ol>
        <li>**שלב ראשון: כיווץ מיידי (Vasoconstriction):** ברגע הפציעה, שרירים קטנים בדופן כלי הדם מתכווצים. זה מקטין את קוטר כלי הדם ומאט משמעותית את זרימת הדם באזור, צעד ראשון וחיוני להפחתת איבוד הדם.</li>
        <li>**שלב שני: פקק הטסיות (Primary Hemostasis):** הטסיות מזהות את הפציעה, נמשכות אליה במהירות, נצמדות זו לזו ויוצרות "פקק" ראשוני, מעין "פלסטר" זמני ורך שאוטם חלקית את החור. הן גם משחררות חומרים כימיים שמגייסים עוד טסיות ומפעילים את השלב הבא.</li>
        <li>**שלב שלישי: מסלול הקרישה (Coagulation Cascade):** זוהי השרשרת המורכבת של פקטורי הקרישה שפועלים בזה אחר זה. קיימים שני מסלולים עיקריים שמתחילים באופן שונה (פנימי וחיצוני), אך שניהם מתכנסים למסלול משותף ששיאו הוא יצירת הכמות הגדולה של האנזים תרומבין.</li>
        <li>**שלב רביעי: רשת הפיברין נבנית (Fibrin Formation):** התרומבין שנוצר בשלב 3 פועל במהירות להפוך את חלבון הפיברינוגן המומס לסיבי פיברין בלתי מסיסים. הסיבים האלה נשזרים כמו רשת דייגים דחוסה סביב פקק הטסיות.</li>
        <li>**שלב חמישי: הקריש הסופי נוצר (Clot Formation):** רשת הפיברין החזקה לוכדת בתוכה עוד טסיות דם, כדוריות דם אדומות (שנותנות לקריש את צבעו האדום) וכדוריות דם לבנות. יחד, הם יוצרים מבנה יציב וקשיח - קריש הדם - שאוטם לחלוטין את כלי הדם הפגוע ועוצר סופית את הדימום.</li>
    </ol>

    <h3>מה קורה אחרי?</h3>
    <p>ברגע שהפצע מתחיל להחלים והרקמה מתחדשת, הקריש כבר לא נחוץ. הגוף מפעיל מנגנון נוסף (פיברינוליזה) שבו אנזים בשם פלסמין מפרק בהדרגה את רשת הפיברין, והקריש נעלם.</p>

    <h3>כשהמנגנון משתבש</h3>
    <p>כמו בכל מערכת מורכבת בגוף, גם במנגנון הקרישה יכולות להיות תקלות:</p>
    <ul>
        <li>**קרישת יתר (Thrombophilia):** מצב שבו הדם נוטה להיקרש בקלות רבה מדי, לפעמים בתוך כלי דם תקינים, מה שעלול ליצור חסימות מסוכנות (פקקת - Thrombosis) ולגרום לאירועים כמו שבץ או התקף לב.</li>
        <li>**דימום יתר (Bleeding Disorders):** קושי של הדם להיקרש באופן יעיל. המחלה המפורסמת ביותר היא המופיליה, הנגרמת לרוב מפגם גנטי באחד מפקטורי הקרישה.</li>
    </ul>
    <p>אז בפעם הבאה שתישרטו קלות, זכרו את המסע המדהים שמתרחש בתוך הגוף שלכם כדי לשמור עליכם!</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const actionBtn = document.getElementById('actionBtn');
    const resetSimBtn = document.getElementById('resetSimBtn');
    const vesselContainer = document.querySelector('.vessel-container');
    const injury = vesselContainer.querySelector('.injury');
    const bloodFlowArea = vesselContainer.querySelector('.blood-flow');
    const plateletArea = vesselContainer.querySelector('.platelet-area');
    const cascadeArea = vesselContainer.querySelector('.cascade-area');
    const fibrinArea = vesselContainer.querySelector('.fibrin-area');
    const clotArea = vesselContainer.querySelector('.clot-area');
    const messagesDisplay = document.querySelector('.messages');

    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationSection = document.getElementById('explanation');

    let currentStep = 0;
    const steps = [
        { text: "שלב 1: כיווץ כלי הדם", action: stepVasoconstriction, message: "הופס! חתך קטן. כלי הדם מתכווץ מיד כדי להאט את הדימום הראשוני." },
        { text: "שלב 2: גיוס טסיות דם", action: stepPlateletPlug, message: "כעת, טסיות הדם הקטנות רצות להדביק את החור!" },
        { text: "שלב 3: שרשרת הקרישה מתחילה", action: stepCoagulationCascade, message: "במקביל, מנגנון קסום של חלבונים (פקטורי קרישה) מופעל בשרשרת..." },
        { text: "שלב 4: רשת הפיברין נבנית", action: stepFibrinFormation, message: "...כדי ליצור את ה'דבק' החזק ביותר - הפיברין!" },
        { text: "שלב 5: הקריש נסגר!", action: stepClotFormation, message: "הפיברין לוכד תאי דם וטסיות, נוצר קריש יציב שעוצר את הדימום!" },
    ];

    let bloodCells = [];
    let bloodFlowInterval = null;

    function showMessage(msg) {
        messagesDisplay.textContent = msg;
        messagesDisplay.style.opacity = 1;
    }

    function hideMessage() {
         messagesDisplay.style.opacity = 0;
         messagesDisplay.textContent = ''; // Clear message content
    }

    function createBloodCells(num) {
        bloodFlowArea.innerHTML = ''; // Clear existing cells
        bloodCells = [];
        const flowHeight = bloodFlowArea.offsetHeight;
        const flowWidth = bloodFlowArea.offsetWidth;

        for (let i = 0; i < num; i++) {
            const cell = document.createElement('div');
            cell.classList.add('blood-cell');
            // Randomize starting position and animation properties
            const startX = -20 - Math.random() * 100; // Start outside left edge
            const startY = Math.random() * flowHeight; // Random height within the flow area
            const duration = 5 + Math.random() * 5; // Random duration between 5s and 10s
            const delay = Math.random() * duration; // Random animation delay

            cell.style.top = `${startY}px`;
            cell.style.left = `${startX}px`; // Set initial position for animation
            cell.style.animation = `flow ${duration}s linear infinite`;
            cell.style.animationDelay = `-${delay}s`; // Use negative delay to start in a random animation state
            cell.style.animationPlayState = 'running'; // Ensure animation is running

            bloodFlowArea.appendChild(cell);
            bloodCells.push(cell);
        }
    }

    function stopBloodFlow() {
         bloodCells.forEach(cell => cell.style.animationPlayState = 'paused');
    }

    function resumeBloodFlow() {
         bloodCells.forEach(cell => cell.style.animationPlayState = 'running');
    }


    function clearSimulation() {
        currentStep = 0;
        hideMessage();
        stopBloodFlow(); // Ensure existing animation is stopped
        bloodFlowArea.innerHTML = ''; // Remove blood cells
        plateletArea.innerHTML = ''; // Remove platelets
        cascadeArea.innerHTML = ''; // Remove cascade steps
        fibrinArea.innerHTML = ''; // Remove fibrin strands
        clotArea.innerHTML = ''; // Remove trapped cells from clot
        clotArea.style.width = '0';
        clotArea.style.opacity = 0;
        injury.style.borderColor = 'var(--vessel-color)'; // Reset injury border
        injury.style.borderStyle = 'dashed'; // Reset injury border style

        // Re-create initial blood flow
        createBloodCells(20); // More blood cells initially
        resumeBloodFlow();

        actionBtn.textContent = "התחל מסע!";
        actionBtn.style.display = 'inline-block';
        resetSimBtn.style.display = 'none';
    }

    function stepVasoconstriction() {
        // Animate visual vasoconstriction
        injury.style.borderColor = 'var(--wall-color)'; // Indicate tightening color
        injury.style.borderStyle = 'solid'; // Change to solid line to indicate closure

        // Keep blood flow running initially
        resumeBloodFlow();
    }

    function stepPlateletPlug() {
        const numPlatelets = 40; // More platelets
        const injuryWidth = plateletArea.offsetWidth;
        const injuryHeight = plateletArea.offsetHeight;
        const vesselTop = 0; // relative to plateletArea top
        const vesselBottom = injuryHeight; // relative to plateletArea top

        // Simulate platelets flowing towards and clumping at the injury
        for (let i = 0; i < numPlatelets; i++) {
            const platelet = document.createElement('div');
            platelet.classList.add('platelet');

            // Start upstream, random Y
            const startX = -50 - Math.random() * 100; // Further upstream
            const startY = vesselTop + Math.random() * injuryHeight; // Random height within injury bounds

            platelet.style.left = `${startX}px`;
            platelet.style.top = `${startY}px`;
            platelet.style.opacity = 0.2; // Start semi-transparent
            plateletArea.appendChild(platelet);

            // Animate movement to a clustered position around the injury center
            const targetX = (injuryWidth / 2) + (Math.random() - 0.5) * (injuryWidth * 0.8); // Cluster more spread
            const targetY = vesselTop + Math.random() * injuryHeight; // Settle within bounds

            setTimeout(() => {
                 platelet.style.opacity = 1;
                 platelet.style.transform = `translate(${targetX - startX}px, ${targetY - startY}px) scale(1)`; // Move and scale up
                 platelet.style.transition = `transform 1s ease-out ${i * 30}ms, opacity 0.8s ease-out ${i * 30}ms`;
            }, 50); // Small delay to ensure style is set before transition
        }

        // Pause blood flow *after* platelets have mostly arrived
        setTimeout(() => {
             stopBloodFlow();
        }, numPlatelets * 30 + 800); // Pause after final platelet animation starts + buffer
    }

    function stepCoagulationCascade() {
        // Visualize cascade steps appearing sequentially
        const numSteps = 8;
        cascadeArea.innerHTML = ''; // Clear previous cascade visuals
        const stepsContainer = document.createElement('div'); // Container for flexbox
        stepsContainer.style.display = 'flex';
        stepsContainer.style.alignItems = 'center';
        stepsContainer.style.justifyContent = 'center';
        stepsContainer.style.width = '100%';
        stepsContainer.style.height = '100%';
        cascadeArea.appendChild(stepsContainer);


        for (let i = 0; i < numSteps; i++) {
            const step = document.createElement('div');
            step.classList.add('cascade-step');
            stepsContainer.appendChild(step);

            setTimeout(() => {
                step.style.opacity = 1;
                step.style.transform = 'scale(1)'; // Grow effect
                step.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
            }, i * 200); // Stagger activation
        }
    }

     function stepFibrinFormation() {
        const fibrinAreaWidth = fibrinArea.offsetWidth;
        const fibrinAreaHeight = fibrinArea.offsetHeight;
        const numStrands = 30; // More fibrin strands for density

        fibrinArea.innerHTML = ''; // Clear previous fibrin

        for (let i = 0; i < numStrands; i++) {
            const strand = document.createElement('div');
            strand.classList.add('fibrin-strand');

            // Random horizontal position within the area
            const posX = Math.random() * (fibrinAreaWidth - 3); // -3 for strand width
            strand.style.left = `${posX}px`;
            // Always start just outside the top, grow downwards
            const startY = -fibrinAreaHeight * 0.1; // Start slightly above area
            strand.style.top = `${startY}px`;
            // Random angle, mostly vertical or slightly diagonal
             strand.style.transform = `rotate(${Math.random() * 60 - 30}deg)`; // Angles between -30 and 30 degrees


            fibrinArea.appendChild(strand);

            // Animate growing height and opacity
            setTimeout(() => {
                 strand.style.height = `${fibrinAreaHeight * 1.2}px`; // Grow slightly past the bottom
                 strand.style.opacity = 0.7 + Math.random() * 0.3; // Randomize opacity slightly
                 strand.style.transition = 'height 1.5s ease-out, opacity 0.8s ease-out';
            }, i * 80); // Stagger strand appearance
        }

        // Add trapped blood cells to the clot area (which is still hidden)
        // These will appear when the clot itself becomes visible
        clotArea.innerHTML = ''; // Clear any previous trapped cells
        const numTrappedCells = 25; // Number of cells to show trapped
        for(let i = 0; i < numTrappedCells; i++) {
             const clotCell = document.createElement('div');
             clotCell.classList.add('clot-cell');
             // Position is random within the clot area, handled by flexbox
             clotArea.appendChild(clotCell);
        }
     }

    function stepClotFormation() {
        // Make the clot area visible and expand it to cover the injury
        clotArea.style.width = '100%'; // Expand to cover the full area width
        clotArea.style.opacity = 1;

        // Ensure blood flow is stopped
        stopBloodFlow();

        // Final message and button state
        setTimeout(() => {
            showMessage("הדימום נפסק! הקריש נוצר ואוטם את הפצע.");
            actionBtn.style.display = 'none';
            resetSimBtn.style.display = 'inline-block';
        }, 1200); // Delay after clot animation starts
    }


    function handleActionClick() {
        if (currentStep < steps.length) {
            const stepInfo = steps[currentStep];
            showMessage(stepInfo.message); // Show message for the step
            stepInfo.action(); // Execute the step's action

            currentStep++; // Move to the next step

            if (currentStep < steps.length) {
                 actionBtn.textContent = steps[currentStep].text; // Update button text for next step
            } else {
                 actionBtn.textContent = "הושלם!"; // Final text
                 actionBtn.disabled = true; // Disable button after last step action is triggered
            }

        }
    }

    actionBtn.addEventListener('click', handleActionClick);
    resetSimBtn.addEventListener('click', clearSimulation);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג/הסתר הסבר מעמיק';
    });

    // Initial setup
    clearSimulation(); // Set up the initial state with blood flow
});
</script>
```