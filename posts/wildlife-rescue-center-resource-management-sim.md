---
title: "מרכז הצלה לחיות בר: סימולציית ניהול משאבים"
english_slug: wildlife-rescue-center-resource-management-sim
category: "מדעי הסביבה / אקולוגיה וקיימות"
tags: ["חיות בר", "שיקום", "ניהול משאבים", "קיימות", "סביבה", "סימולציה"]
---
# מרכז הצלה לחיות בר: האם תצליחו להחזיר אותן הביתה?

ציפור שנתקלה בחלון, שועל שנפגע על הכביש, צבי שנלכד בפלסטיק... מדי יום מגיעות למרכזי שיקום חיות בר פצועות הזקוקות לעזרה. אבל המשאבים מוגבלים, ההחלטות קשות, והסיכויים לא תמיד לטובתנו. האם יש לכם מה שנדרש כדי לנהל מרכז הצלה מצליח ולהחזיר כמה שיותר חיות אל הטבע?

בואו התנסו עכשיו:

<div id="app">
    <div class="header">
        <img src="placeholder_logo.png" alt="Wilderness Rescue Center Logo" class="logo"> <!-- Placeholder for logo -->
        <h2>מרכז הצלה לחיות בר</h2>
    </div>

    <div class="game-area">
        <div class="panels-container">
            <div class="panel resources-panel">
                <h3><i class="icon">💰</i> משאבים זמינים</h3>
                <div id="resources" class="resources-grid">
                    <p><i class="icon">👩‍⚕️</i> זמן וטרינר: <span id="vetTime"></span> יח'</p>
                    <p><i class="icon">🐛</i> מזון מיוחד: <span id="specialFood"></span> יח'</p>
                    <p><i class="icon">🏠</i> כלובים ייעודיים: <span id="specialCages"></span> יח'</p>
                    <p><i class="icon">💵</i> תקציב: <span id="budget"></span> ש"ח</p>
                </div>
            </div>

            <div class="panel status-panel">
                 <h3><i class="icon">📊</i> סטטוס המרכז</h3>
                 <p><i class="icon">🌿</i> חיות ששוחררו: <span id="releasedCount">0</span></p>
                 <p><i class="icon">❤️‍🩹</i> חיות בטיפול פעיל: <span id="activeCount">0</span></p>
                 <p><i class="icon">🚨</i> חיות במצב קשה (בבחינה): <span id="criticalCount">0</span></p>
            </div>

            <div class="panel incoming-panel">
                <h3><i class="icon">📥</i> מקרים חדשים מגיעים <span id="incomingCount">(0)</span></h3>
                <div id="incomingAnimals">
                    <p class="empty-state">אין מקרים חדשים כרגע.</p>
                </div>
            </div>

             <div class="panel active-panel">
                <h3><i class="icon">🏥</i> חיות בטיפול <span id="activeTreatmentCount">(0)</span></h3>
                 <div id="activeAnimals">
                     <p class="empty-state">אין חיות בטיפול כרגע.</p>
                 </div>
            </div>
        </div>

         <div class="decisions-panel panel">
             <h3><i class="icon">⏭️</i> התקדמות</h3>
             <button id="nextDayBtn" class="btn-primary">יום נוסף במרכז</button>
         </div>

        <div class="messages-panel panel">
            <h3><i class="icon">📢</i> עדכונים ואירועים</h3>
            <div id="messages">
                <p class="message system">ברוכים הבאים למרכז ההצלה לחיות בר! התכוננו ליום הראשון...</p>
            </div>
        </div>
    </div>
</div>

<style>
    /* General Styles */
    #app {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font */
        max-width: 1000px; /* Slightly wider */
        margin: 20px auto;
        padding: 25px; /* More padding */
        border: 1px solid #d3e0ea; /* Lighter border */
        border-radius: 12px; /* More rounded corners */
        background-color: #f0f4f8; /* Light background */
        direction: rtl;
        text-align: right;
        color: #333;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Add shadow */
        overflow: hidden; /* Clear floats/margins */
    }

    .header {
        text-align: center;
        margin-bottom: 30px;
    }

    .header h2 {
         color: #0056b3; /* Blue heading */
        margin-top: 10px;
         font-size: 2em;
    }

     .logo {
         height: 60px; /* Adjust as needed */
         width: auto;
         /* Placeholder style */
         background-color: #aed6f1;
         border-radius: 50%;
         display: inline-block;
     }


    .game-area {
        display: flex;
        flex-wrap: wrap; /* Allow panels to wrap */
        gap: 20px; /* Space between sections */
    }

    .panels-container {
        flex: 2; /* Takes more space */
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
        gap: 20px;
        align-items: start; /* Align top */
    }

    .panel {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #e0e7eb;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease-in-out; /* Add transition for hover/interaction */
    }

     .panel:hover {
         transform: translateY(-3px); /* Subtle lift on hover */
     }

    .panel h3 {
        margin-top: 0;
        color: #0056b3;
        font-size: 1.3em;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    .panel h3 .icon {
        margin-left: 8px; /* Space icon from text */
        font-size: 1.2em;
    }


    .resources-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); /* Two columns if space allows */
        gap: 10px;
    }

    .resources-panel p, .status-panel p {
        margin: 0; /* Remove default paragraph margin */
        font-size: 1em;
        color: #555;
        display: flex;
        align-items: center;
    }
     .resources-panel p .icon, .status-panel p .icon {
         margin-left: 5px;
         color: #007bff; /* Blue icons */
     }


    #incomingAnimals, #activeAnimals {
        min-height: 80px; /* More space */
        padding-top: 10px;
    }

     .empty-state {
         text-align: center;
         color: #777;
         font-style: italic;
         padding: 20px 0;
     }


    .animal-card {
        border: 1px solid #cfe2ff; /* Light blue border */
        padding: 15px; /* More padding */
        margin-bottom: 15px; /* More space between cards */
        border-radius: 8px; /* Rounded corners */
        background-color: #e9f5ff; /* Very light blue */
        display: flex;
        justify-content: space-between;
        align-items: flex-start; /* Align items to the top */
        flex-wrap: wrap;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease-in-out; /* Animation for state changes */
         position: relative; /* Needed for potential status indicator */
    }

     .animal-card.status-released { background-color: #d4edda; border-color: #c3e6cb; } /* Green */
     .animal-card.status-critical { background-color: #fff3cd; border-color: #ffeeba; } /* Yellow */
     .animal-card.status-euthanized, .animal-card.status-died { background-color: #f8d7da; border-color: #f5c6cb; opacity: 0.7; } /* Red, slightly transparent */
     .animal-card.status-active { background-color: #e9f5ff; border-color: #cfe2ff; } /* Default light blue */


    .animal-card > div:first-child { /* Content area */
        flex-basis: 65%; /* Content takes more space */
        margin-bottom: 10px; /* Space before actions on wrap */
    }
     .animal-card .actions { /* Actions area */
        flex-basis: 30%; /* Actions take less space */
        text-align: left; /* Align buttons to the left */
         display: flex; /* Arrange buttons */
         gap: 5px; /* Space between buttons */
         flex-wrap: wrap; /* Allow buttons to wrap */
     }


    .animal-card h4 {
        margin: 0 0 8px 0; /* Space below title */
        color: #004085; /* Darker blue */
        font-size: 1.1em;
    }

    .animal-card p {
        margin: 4px 0; /* Space between lines */
        font-size: 0.95em;
        color: #555;
    }

    .animal-card ul {
        padding: 0;
        margin: 8px 0 0 0;
        list-style: none;
    }
     .animal-card li {
         font-size: 0.9em;
         color: #555;
         margin-bottom: 3px;
     }


    .animal-card button {
        padding: 8px 12px; /* More padding */
        border: none;
        border-radius: 5px; /* Rounded buttons */
        cursor: pointer;
        font-size: 0.9em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        white-space: nowrap; /* Prevent button text wrap */
    }

    .animal-card button.treat-btn { background-color: #28a745; color: white; } /* Green */
    .animal-card button.euthanize-btn { background-color: #dc3545; color: white; } /* Red */
     /* Optional: Add a 'Prioritize' button style if implemented in JS */
     /* .animal-card button.prioritize-btn { background-color: #ffc107; color: #212529; } */

    .animal-card button:hover {
        opacity: 0.9;
        transform: translateY(-1px);
    }

    .decisions-panel {
        flex-basis: 100%; /* Button takes full width */
        text-align: center;
        order: 3; /* Place it after panels-container */
    }

    button#nextDayBtn {
        display: block;
        width: 100%;
        padding: 12px 20px; /* Larger button */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2em;
        margin-top: 10px;
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.2);
        transition: background-color 0.2s ease, transform 0.1s ease;
    }
     button#nextDayBtn:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
     }
     button#nextDayBtn:active {
         background-color: #004085;
         transform: translateY(0);
     }


    .messages-panel {
         flex: 1; /* Takes remaining space */
         order: 4; /* Place it after the next day button */
    }

    #messages {
        max-height: 200px; /* Slightly taller messages panel */
        overflow-y: auto;
        padding-top: 5px;
         display: flex; /* Use flex for message animation */
         flex-direction: column-reverse; /* New messages appear at top */
    }

    #messages p {
        margin: 5px 0;
        padding: 8px;
        border-radius: 4px;
        font-size: 0.95em;
        line-height: 1.4;
        opacity: 0; /* Start invisible for fade-in animation */
        animation: fadeInMessage 0.5s ease-out forwards;
    }

     @keyframes fadeInMessage {
         to { opacity: 1; }
     }

     .message.system {
         color: #007bff; /* Blue for system messages */
         background-color: #e9f5ff;
         border: 1px solid #cfe2ff;
     }
    .message.animal-event {
        color: #28a745; /* Green for positive outcomes */
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
    }
     .message.negative-event {
         color: #dc3545; /* Red for negative outcomes */
         background-color: #f8d7da;
         border: 1px solid #f5c6cb;
     }
     .message.warning {
         color: #ffc107; /* Yellow for warnings */
         background-color: #fff3cd;
         border: 1px solid #ffeeba;
     }


    /* Explanation Button */
     #toggleExplanation {
         display: block;
         width: fit-content;
         margin: 20px auto;
         padding: 10px 15px;
         background-color: #6c757d;
         color: white;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         font-size: 1em;
         transition: background-color 0.2s ease;
     }
     #toggleExplanation:hover {
         background-color: #5a6268;
     }

    /* Explanation Section */
    #explanation {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #d3e0ea;
        border-radius: 8px;
        background-color: #f0f4f8;
        color: #333;
    }

    #explanation h2 {
        color: #0056b3;
        margin-top: 0;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }

    #explanation p {
        line-height: 1.6;
        margin-bottom: 15px;
        font-size: 1em;
    }
     #explanation strong {
         color: #0056b3;
     }


    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .game-area {
            flex-direction: column; /* Stack panels vertically on smaller screens */
        }

        .panels-container {
            grid-template-columns: 1fr; /* Single column grid */
            gap: 15px;
        }

        .animal-card {
            flex-direction: column;
            align-items: stretch;
        }

        .animal-card > div:first-child {
            flex-basis: auto;
        }
        .animal-card .actions {
            flex-basis: auto;
            justify-content: center; /* Center buttons when stacked */
            margin-top: 10px;
             gap: 10px; /* More space between stacked buttons */
        }

        .resources-grid {
             grid-template-columns: 1fr; /* Stack resources vertically */
        }
    }

</style>

<button id="toggleExplanation">הצגת הסבר / הסתרת הסבר</button>

<div id="explanation" style="display: none;">
    <h2>על מרכזי שיקום והצלה לחיות בר</h2>
    <p><strong>מהו מרכז הצלה לחיות בר?</strong> זהו מקום שבו מעניקים טיפול רפואי ושיקומי לחיות בר שנפגעו בטבע, במטרה העליונה להחזיר אותן בריאות וחזקות ככל האפשר לביתן הטבעי. כל חיה שמצליחה לחזור לטבע היא ניצחון קטן ותרומה חשובה לשמירה על המגוון הביולוגי המקומי.</p>
    <p><strong>מסע ההחלמה:</strong> חיה שמגיעה למרכז עוברת תהליך מורכב: בדיקה רפואית מהירה (טריאז'), אבחון מדויק, טיפול רפואי (לפעמים מדובר בניתוחים מורכבים!), שלב שיקום והתאוששות בכלובים מותאמים, ולבסוף הכנה לקראת חזרה לטבע – בה החיה לומדת ומזכירה לעצמה איך לשרוד לבד, לצוד, לחפש מזון ולהימנע מסכנות. רק חיה כשירה לחלוטין משוחררת בחזרה, לרוב בסביבה שבה נמצאה.</p>
    <p><strong>ממה נפגעות חיות הבר?</strong> למרבה הצער, פעילות האדם היא גורם מרכזי. פגיעות רכב, התנגשות בחלונות או קווי חשמל, פגיעה מציד לא חוקי, מלכודות או חומרי הדברה - כל אלה מביאים חיות רבות למרכזים. גם מחלות טבעיות, פציעות מטורפים או יתמות בגיל קריטי דורשים לעיתים התערבות אדם.</p>
    <p><strong>אומנות ניהול המשאבים:</strong> מרכזי הצלה פועלים לרוב עם תקציב דחוק, מסתמכים על תרומות ופועלים בזכות מסירותם של וטרינרים, מטפלים ומתנדבים. כל שקל, כל שעת טיפול, כל כלוב פנוי - הם משאבים יקרים. יש צורך בציוד רפואי, מזון מיוחד, ותשתיות מתאימות. ניהול נכון של המשאבים הוא קריטי להצלת כמה שיותר חיות, וכל החלטה על קבלת חיה לטיפול או ויתור עליה משפיעה על יכולת המרכז לטפל באחרות.</p>
    <p><strong>דילמות קשות בדרך:</strong> לא תמיד אפשר לעזור לכולם. עם משאבים מוגבלים, עלולות להתעורר דילמות: האם להשקיע מאמץ רב בחיה עם סיכויי החלמה נמוכים על חשבון חיות רבות יותר עם סיכויים טובים? מתי, אם בכלל, נכון לקבל את ההחלטה הכואבת לשקול המתת חסד לחיה סובלת שאין לה סיכוי סביר לחזור לטבע או שאיכות חייה תהיה ירודה ביותר? אלו הן החלטות יומיומיות שדורשות איזון בין חמלה למציאות.</p>
    <p><strong>הדרך חזרה הביתה:</strong> שחרור לטבע הוא רגע מרגש אך גם מחייב. החיה חייבת לעמוד בקריטריונים מחמירים: החלמה פיזית מלאה, משקל תקין, יכולת תנועה, ראייה ושמיעה, וכישורי הישרדות. יש למצוא לה גם אתר שחרור מתאים. האתגר הגדול הוא לוודא שהיא לא תפתח תלות בבני אדם במהלך הטיפול, דבר שיפגע בסיכויי שרידותה בטבע.</p>
    <p><strong>למה זה כל כך חשוב?</strong> מרכזי הצלה עושים יותר מלהציל פרטים בודדים. הם אוספים מידע חיוני על מצב הטבע, מזהים סכנות סביבתיות (כמו מחלות או זיהומים מתפשטים), ותורמים ישירות לחיזוק אוכלוסיות של מינים מקומיים, כולל נדירים. הצלת חיות בר היא חלק בלתי נפרד משמירה על בריאות המערכת האקולוגית שלנו.</p>
</div>

<script>
    // Game Configuration
    const initialResources = {
        vetTime: 15, // Increased initial resources slightly
        specialFood: 10,
        specialCages: 5,
        budget: 2000
    };

     const dailyResourceReplenishment = {
         vetTime: 10,
         specialFood: 5,
         specialCages: 0, // Cages are static
         budget: 500
     };

     const dailyAnimalMaintenanceCost = {
         vetTime: 0.5, // Small daily vet check/observation time
         specialFood: 0.2, // Basic food cost per day
         specialCages: 0, // Cage cost is initial placement, not daily
         budget: 10 // Basic daily cost (cleaning, utilities etc.)
     };

    let resources = { ...initialResources }; // Clone initial resources

    let incomingAnimals = [];
    let activeAnimals = [];
    let releasedCount = 0;
    let criticalCount = 0;
    let diedCount = 0; // Track animals that died
    let euthanizedCount = 0; // Track animals euthanized

    const maxActiveAnimals = 12; // Limit the total number of animals in active care + critical - slightly lower limit for challenge
    let animalIdCounter = 0;
    let gameDay = 0;

    const animalTypes = [
        { species: "ציפור שיר (פצועה)", icon: "🐦", condition: "כנף שבורה", requiredResources: { vetTime: 2, specialFood: 1, specialCages: 0, budget: 50 }, dailyCost: { ...dailyAnimalMaintenanceCost, vetTime: 0.5, budget: 10 }, recoveryChance: 0.7, recoveryTime: 3, critical: false },
        { species: "דורס לילה (תשוש)", icon: "🦉", condition: "תשישות/רזון", requiredResources: { vetTime: 1, specialFood: 2, specialCages: 1, budget: 70 }, dailyCost: { ...dailyAnimalMaintenanceCost, specialFood: 0.5, budget: 15 }, recoveryChance: 0.8, recoveryTime: 4, critical: false },
        { species: "צב יבשה (התנגשות)", icon: "🐢", condition: "שבר שריון קשה", requiredResources: { vetTime: 3, specialFood: 0, specialCages: 1, budget: 150 }, dailyCost: { ...dailyAnimalMaintenanceCost, vetTime: 1, budget: 20 }, recoveryChance: 0.4, recoveryTime: 7, critical: true },
        { species: "גור שועל (יתום)", icon: "🦊", condition: "יתמות בגיל צעיר", requiredResources: { vetTime: 1, specialFood: 3, specialCages: 1, budget: 100 }, dailyCost: { ...dailyAnimalMaintenanceCost, specialFood: 1, budget: 25 }, recoveryChance: 0.9, recoveryTime: 5, critical: false },
        { species: "עטלף (פגיעת חלון)", icon: "🦇", condition: "טראומה ראש/שבר קל", requiredResources: { vetTime: 1, specialFood: 1, specialCages: 0, budget: 40 }, dailyCost: { ...dailyAnimalMaintenanceCost, budget: 8 }, recoveryChance: 0.75, recoveryTime: 3, critical: false },
         { species: "נחש (פצוע)", icon: "🐍", condition: "פצע פתוח", requiredResources: { vetTime: 1, specialFood: 0, specialCages: 0, budget: 60 }, dailyCost: { ...dailyAnimalMaintenanceCost, budget: 12 }, recoveryChance: 0.6, recoveryTime: 4, critical: false },
          { species: "ציפור שיר (חולה)", icon: "🐦", condition: "מחלה ויראלית", requiredResources: { vetTime: 1, specialFood: 1, specialCages: 0, budget: 50 }, dailyCost: { ...dailyAnimalMaintenanceCost, vetTime: 0.7, specialFood: 0.3, budget: 15 }, recoveryChance: 0.5, recoveryTime: 5, critical: true },
          { species: "צבי (התנגשות)", icon: "🦌", condition: "שבר רגל", requiredResources: { vetTime: 4, specialFood: 2, specialCages: 1, budget: 200 }, dailyCost: { ...dailyAnimalMaintenanceCost, vetTime: 1.5, specialFood: 0.5, budget: 30 }, recoveryChance: 0.65, recoveryTime: 8, critical: true },
          { species: "קיפוד (נפילה)", icon: "🦔", condition: "שברים קטנים", requiredResources: { vetTime: 1, specialFood: 1, specialCages: 0, budget: 60 }, dailyCost: { ...dailyAnimalMaintenanceCost, specialFood: 0.3, budget: 10 }, recoveryChance: 0.7, recoveryTime: 4, critical: false },
           { species: "בז (תשישות/הרעלה)", icon: "🦅", condition: "חשד להרעלה", requiredResources: { vetTime: 3, specialFood: 2, specialCages: 1, budget: 180 }, dailyCost: { ...dailyAnimalMaintenanceCost, vetTime: 1.2, specialFood: 0.7, budget: 25 }, recoveryChance: 0.55, recoveryTime: 6, critical: true },
    ];

    const messagesElement = document.getElementById('messages');
    const incomingAnimalsElement = document.getElementById('incomingAnimals');
    const activeAnimalsElement = document.getElementById('activeAnimals');
    const resourcesElement = document.getElementById('resources');
    const releasedCountElement = document.getElementById('releasedCount');
    const activeCountElement = document.getElementById('activeCount');
    const criticalCountElement = document.getElementById('criticalCount');
    const incomingCountElement = document.getElementById('incomingCount');

    document.getElementById('nextDayBtn').addEventListener('click', processNextDay);
    document.getElementById('toggleExplanation').addEventListener('click', toggleExplanation);

     function addMessage(text, type = 'system') {
        const p = document.createElement('p');
        p.textContent = text;
         p.classList.add('message', type); // Add class for styling/animation
        messagesElement.prepend(p); // Add to top

        // Optional: limit number of messages
        while (messagesElement.children.length > 50) { // Keep more messages history
            messagesElement.removeChild(messagesElement.lastChild);
        }
         // Animate new message
         setTimeout(() => { p.style.opacity = 1; }, 50);
    }


    function updateResourcesDisplay() {
        document.getElementById('vetTime').textContent = resources.vetTime.toFixed(1); // Show decimal for partial units
        document.getElementById('specialFood').textContent = resources.specialFood.toFixed(1);
        document.getElementById('specialCages').textContent = resources.specialCages; // Cages are integers
        document.getElementById('budget').textContent = resources.budget.toFixed(0); // Budget is integer
    }

    function updateStatusDisplay() {
         releasedCountElement.textContent = releasedCount;
         activeCountElement.textContent = activeAnimals.filter(a => !a.critical && !['released', 'died', 'euthanized'].includes(a.status)).length;
         criticalCountElement.textContent = activeAnimals.filter(a => a.critical && !['released', 'died', 'euthanized'].includes(a.status)).length;
         incomingCountElement.textContent = `(${incomingAnimals.length})`;
         document.getElementById('activeTreatmentCount').textContent = `(${activeAnimals.filter(a => !['released', 'died', 'euthanized'].includes(a.status)).length})`; // Count only active/critical
    }


    function renderIncomingAnimals() {
        incomingAnimalsElement.innerHTML = ''; // Clear current list
        if (incomingAnimals.length === 0) {
            incomingAnimalsElement.innerHTML = '<p class="empty-state">אין מקרים חדשים כרגע.</p>';
        } else {
             // Sort incoming by critical status
            incomingAnimals.sort((a, b) => (b.critical ? 1 : 0) - (a.critical ? 1 : 0));

            incomingAnimals.forEach(animal => {
                const card = document.createElement('div');
                card.classList.add('animal-card', 'incoming'); // Add incoming class
                 if (animal.critical) card.classList.add('status-critical'); // Highlight critical incoming
                card.dataset.id = animal.id; // Store ID on the card
                card.innerHTML = `
                    <div>
                        <h4>${animal.icon} ${animal.species} (ID: ${animal.id})</h4>
                        <p><strong>מצב:</strong> ${animal.condition}</p>
                        <p><strong>סיכוי החלמה (משוער):</strong> ${(animal.recoveryChance * 100).toFixed(0)}%</p>
                         ${animal.critical ? '<p style="color: #dc3545; font-weight: bold;"> 🚨 במצב קשה מאוד - דורש החלטה דחופה!</p>' : ''}
                        <p><strong>משאבים נדרשים לקבלה וטיפול ראשוני:</strong></p>
                        <ul>
                             ${animal.requiredResources.vetTime > 0 ? `<li>👩‍⚕️ זמן וטרינר: ${animal.requiredResources.vetTime} יח'</li>` : ''}
                             ${animal.requiredResources.specialFood > 0 ? `<li>🐛 מזון מיוחד: ${animal.requiredResources.specialFood} יח'</li>` : ''}
                             ${animal.requiredResources.specialCages > 0 ? `<li>🏠 כלוב ייעודי: ${animal.requiredResources.specialCages} יח'</li>` : ''}
                             ${animal.requiredResources.budget > 0 ? `<li>💵 תקציב: ${animal.requiredResources.budget} ש"ח</li>` : ''}
                        </ul>
                    </div>
                    <div class="actions">
                        <button class="treat-btn" data-id="${animal.id}">קבל וטפל</button>
                        <button class="euthanize-btn" data-id="${animal.id}">שקול המתת חסד</button>
                    </div>
                `;
                 // Animate card appearance
                 card.style.opacity = 0;
                 card.style.transform = 'translateY(20px)';
                 incomingAnimalsElement.appendChild(card);
                 setTimeout(() => {
                    card.style.opacity = 1;
                    card.style.transform = 'translateY(0)';
                 }, 50 + incomingAnimals.indexOf(animal) * 50); // Stagger animation
            });
        }


        // Add event listeners *after* rendering
        incomingAnimalsElement.querySelectorAll('.treat-btn').forEach(button => {
            button.addEventListener('click', handleTreatDecision);
        });
        incomingAnimalsElement.querySelectorAll('.euthanize-btn').forEach(button => {
            button.addEventListener('click', handleEuthanizeDecision);
        });
    }

     function renderActiveAnimals() {
        activeAnimalsElement.innerHTML = '';
         if (activeAnimals.length === 0) {
            activeAnimalsElement.innerHTML = '<p class="empty-state">אין חיות בטיפול כרגע.</p>';
            return;
        }

        // Sort active animals (e.g., critical first, then by days in care)
        activeAnimals.sort((a, b) => {
            if (a.critical !== b.critical) return (b.critical ? 1 : 0) - (a.critical ? 1 : 0); // Critical first
             if (a.daysInCare !== b.daysInCare) return a.daysInCare - b.daysInCare; // Then by days in care
            return 0;
        });


        activeAnimals.forEach(animal => {
             const card = document.createElement('div');
            card.classList.add('animal-card', 'active');
            card.classList.add(`status-${animal.status}`); // Add status class for styling
            card.dataset.id = animal.id; // Store ID on the card

            let statusDisplay = animal.statusText;
             if (animal.status === 'active' || animal.status === 'critical') {
                 statusDisplay += ` (יום ${animal.daysInCare}/${animal.recoveryTime})`;
             }

            card.innerHTML = `
                <div>
                    <h4>${animal.icon} ${animal.species} (ID: ${animal.id})</h4>
                    <p><strong>מצב התחלתי:</strong> ${animal.condition}</p>
                    <p><strong>סטטוס נוכחי:</strong> ${statusDisplay}</p>
                     ${animal.critical && (animal.status === 'active' || animal.status === 'critical') ? '<p style="color: #dc3545; font-weight: bold;"> 🚨 במצב קשה</p>' : ''}
                      ${animal.status === 'released' ? '<p style="color: #28a745; font-weight: bold;"> 🌿 שוחרר בהצלחה</p>' : ''}
                       ${animal.status === 'died' ? '<p style="color: #dc3545; font-weight: bold;"> 😔 נפטר בטיפול</p>' : ''}
                        ${animal.status === 'euthanized' ? '<p style="color: #dc3545; font-weight: bold;"> 💔 הומת בחסד</p>' : ''}
                </div>
            `;
             // No actions needed for active animals in this simple model beyond displaying status
             activeAnimalsElement.appendChild(card);
        });
    }


    function canAfford(cost) {
        return resources.vetTime >= (cost.vetTime || 0) &&
               resources.specialFood >= (cost.specialFood || 0) &&
               resources.specialCages >= (cost.specialCages || 0) &&
               resources.budget >= (cost.budget || 0);
    }

    function deductResources(cost) {
        resources.vetTime = Math.max(0, resources.vetTime - (cost.vetTime || 0));
        resources.specialFood = Math.max(0, resources.specialFood - (cost.specialFood || 0));
        resources.specialCages = Math.max(0, resources.specialCages - (cost.specialCages || 0));
        resources.budget = Math.max(0, resources.budget - (cost.budget || 0));
    }

    function addResources(amount) {
         resources.vetTime += (amount.vetTime || 0);
        resources.specialFood += (amount.specialFood || 0);
        resources.specialCages += (amount.specialCages || 0);
        resources.budget += (amount.budget || 0);
    }

    function handleTreatDecision(event) {
        const animalId = parseInt(event.target.dataset.id);
        const animalIndex = incomingAnimals.findIndex(a => a.id === animalId);
        if (animalIndex === -1) return;

        const animal = incomingAnimals[animalIndex];

        if (activeAnimals.filter(a => !['released', 'died', 'euthanized'].includes(a.status)).length >= maxActiveAnimals) {
             addMessage(`לא ניתן לקבל את ${animal.species} (ID: ${animal.id}) - הגעת למגבלת החיות בטיפול (${maxActiveAnimals}).`, 'warning');
             return;
        }

        if (canAfford(animal.requiredResources)) {
            deductResources(animal.requiredResources);
            animal.status = animal.critical ? 'critical' : 'active';
            animal.statusText = animal.critical ? 'בבחינה וטיפול ראשוני' : 'בטיפול פעיל';
            animal.daysInCare = 0; // Start tracking days
             // Add daily cost property to animal object for easier access
            animal.dailyCost = animalTypes.find(type => type.species === animal.species && type.condition === animal.condition).dailyCost;

            activeAnimals.push(animal);
            incomingAnimals.splice(animalIndex, 1); // Remove from incoming
            addMessage(`✅ קיבלת את ${animal.species} (ID: ${animal.id}) לטיפול. נדרשים: וטרינר ${animal.requiredResources.vetTime}, מזון ${animal.requiredResources.specialFood}, כלוב ${animal.requiredResources.specialCages}, תקציב ${animal.requiredResources.budget} ש"ח.`, 'animal-event');
            updateUI();
        } else {
             let missing = [];
             if (resources.vetTime < animal.requiredResources.vetTime) missing.push(`👩‍⚕️ וטרינר (${animal.requiredResources.vetTime - resources.vetTime.toFixed(1)} יח')`);
             if (resources.specialFood < animal.requiredResources.specialFood) missing.push(`🐛 מזון (${animal.requiredResources.specialFood - resources.specialFood.toFixed(1)} יח')`);
             if (resources.specialCages < animal.requiredResources.specialCages) missing.push(`🏠 כלובים (${animal.requiredResources.specialCages - resources.specialCages} יח')`);
             if (resources.budget < animal.requiredResources.budget) missing.push(`💵 תקציב (${animal.requiredResources.budget - resources.budget.toFixed(0)} ש"ח)`);

            addMessage(`אין מספיק משאבים לקבל את ${animal.species} (ID: ${animal.id}). חסר: ${missing.join(', ')}.`, 'warning');
        }
    }

    function handleEuthanizeDecision(event) {
        const animalId = parseInt(event.target.dataset.id);
        const animalIndex = incomingAnimals.findIndex(a => a.id === animalId);
         if (animalIndex === -1) return;

        const animal = incomingAnimals[animalIndex];

        // Deduct a small cost for the procedure.
        const euthanasiaCost = 50; // Cost slightly increased

         if (resources.budget >= euthanasiaCost) {
            resources.budget -= euthanasiaCost;
             animal.status = 'euthanized';
             animal.statusText = 'הומת בחסד';
             animal.daysInCare = 0; // Start countdown for removal from list
             activeAnimals.push(animal); // Move to active list to show outcome briefly
             incomingAnimals.splice(animalIndex, 1);
             euthanizedCount++;
            addMessage(`💔 הוחלט לשקול המתת חסד עבור ${animal.species} (ID: ${animal.id}).`, 'negative-event');
             updateUI();
         } else {
             addMessage(`אין מספיק תקציב לביצוע המתת חסד עבור ${animal.species} (ID: ${animal.id}). נדרש: ${euthanasiaCost} ש"ח.`, 'warning');
         }
    }


    function addNewAnimal() {
        // Randomly add 0, 1, or 2 new animals per day, maybe weighted towards 1
        const rand = Math.random();
        let numNew;
        if (rand < 0.4) numNew = 0; // 40% chance of 0
        else if (rand < 0.85) numNew = 1; // 45% chance of 1
        else numNew = 2; // 15% chance of 2


        for (let i = 0; i < numNew; i++) {
             // Simple cap to prevent overwhelming the game
             if (incomingAnimals.length + activeAnimals.filter(a => !['released', 'died', 'euthanized'].includes(a.status)).length >= maxActiveAnimals + 5) {
                // addMessage("עומס גבוה במרכז, מקרים חדשים מופנים למרכז אחר או לא מקבלים טיפול..."); // Muted to avoid spam
                 break;
             }
            const animalType = animalTypes[Math.floor(Math.random() * animalTypes.length)];
            const newAnimal = {
                id: ++animalIdCounter,
                species: animalType.species,
                 icon: animalType.icon, // Add icon
                condition: animalType.condition,
                requiredResources: {...animalType.requiredResources}, // Clone resources
                dailyCost: {...animalType.dailyCost}, // Clone daily cost
                recoveryChance: animalType.recoveryChance,
                recoveryTime: animalType.recoveryTime, // Days needed for treatment
                critical: animalType.critical,
                status: 'incoming',
                statusText: 'ממתין לקליטה',
                daysInCare: 0
            };
            incomingAnimals.push(newAnimal);
            addMessage(`📬 מקרה חדש הגיע: ${newAnimal.species} (ID: ${newAnimal.id}) עם ${newAnimal.condition}.`, 'system');
        }
        if(numNew === 0 && incomingAnimals.length === 0 && activeAnimals.length < maxActiveAnimals / 2) {
             // Add a message on quiet days, but not every time
             if (Math.random() < 0.3) addMessage("יום שקט יחסית במרכז. הזדמנות להתארגן.", 'system');
        }
    }

    function processActiveAnimals() {
        const releasedToday = [];
        const diedToday = [];
        const stillActive = [];
        const removedFromList = []; // For animals that finished their display time (euthanized/died)

        // Shuffle active animals slightly each day to vary processing order (or prioritize critical)
        activeAnimals.sort((a, b) => (b.critical ? 1 : 0) - (a.critical ? 1 : 0)); // Critical first processing


        let dailyResourcesAvailable = { // Track resources *actually* consumed for daily maintenance
             vetTime: 0,
             specialFood: 0,
             specialCages: 0, // Not consumed daily
             budget: 0
        };

        activeAnimals.forEach(animal => {
             // Handle animals marked for removal after status display
             if (['euthanized', 'died'].includes(animal.status)) {
                 animal.daysInCare++; // Use daysInCare to count display time
                 if (animal.daysInCare > 2) { // Show for 2 days after status change
                     removedFromList.push(animal.id);
                 } else {
                     stillActive.push(animal); // Keep for display
                 }
                 return; // Skip processing for removed/dying animals
             }


             // --- Daily Maintenance & Recovery Progress ---
             animal.daysInCare++;

             // Check if daily maintenance resources are sufficient
             let maintenanceMet = true;
             let cost = animal.dailyCost;
             if (resources.vetTime < cost.vetTime || resources.specialFood < cost.specialFood || resources.budget < cost.budget) {
                 maintenanceMet = false;
                 // Penalize recovery chance or increase time if daily resources are lacking
                 // Simplification: just slightly reduce recovery chance if maintenance isn't met *on that day*
                 animal.currentDayRecoveryChance = animal.recoveryChance * 0.8; // Reduced chance
                  addMessage(`⚠️ אין מספיק משאבים לתחזוקה שוטפת עבור ${animal.species} (ID: ${animal.id}). ייתכן שההחלמה תיפגע.`, 'warning');
             } else {
                 // Deduct daily maintenance cost *if* resources are available globally (simplified)
                  // This model implies global pool vs per-animal check
                  // Let's refine: deduct if global is available. If not, maintenance isn't met.
                  // This requires checking aggregate daily cost *before* deducting.
                  // Okay, let's stick to simpler per-animal check for now, deducting immediately if available.
                 deductResources(cost);
                 dailyResourcesAvailable.vetTime += cost.vetTime;
                 dailyResourcesAvailable.specialFood += cost.specialFood;
                 dailyResourcesAvailable.budget += cost.budget;
                 animal.currentDayRecoveryChance = animal.recoveryChance; // Full chance
             }


            // Check for recovery completion
            if (animal.daysInCare >= animal.recoveryTime) {
                // Treatment period finished, check for recovery success based on overall chance
                 // Note: A more complex model could average 'currentDayRecoveryChance'

                if (Math.random() < animal.recoveryChance) { // Using initial chance for simplicity
                    animal.status = 'released';
                    animal.statusText = 'שוחרר בהצלחה';
                    releasedToday.push(animal);
                    releasedCount++;
                     // Free up resources like cages?
                      if(animal.requiredResources.specialCages > 0) resources.specialCages += animal.requiredResources.specialCages;
                     addMessage(`🌿 ${animal.species} (ID: ${animal.id}) החלים ושוחרר לטבע בהצלחה!`, 'animal-event');
                } else {
                    animal.status = 'died'; // Could also be "died during treatment"
                    animal.statusText = 'נפטר במהלך השיקום';
                    diedToday.push(animal);
                     diedCount++;
                     // Free up resources
                     if(animal.requiredResources.specialCages > 0) resources.specialCages += animal.requiredResources.specialCages;
                    addMessage(`😔 ${animal.species} (ID: ${animal.id}) נפטר במהלך השיקום.`, 'negative-event');
                }
            } else {
                // Still needs care
                 stillActive.push(animal);
            }
        });

        // Filter out animals that were released, died, or are marked for removal
        activeAnimals = stillActive.filter(animal => !removedFromList.includes(animal.id));

        // Messages for daily resource consumption (optional, can be too chatty)
        // if(dailyResourcesAvailable.vetTime > 0 || dailyResourcesAvailable.specialFood > 0 || dailyResourcesAvailable.budget > 0) {
        //      addMessage(`משאבים שנוצלו היום לתחזוקת חיות בטיפול: וטרינר ${dailyResourcesAvailable.vetTime.toFixed(1)}, מזון ${dailyResourcesAvailable.specialFood.toFixed(1)}, תקציב ${dailyResourcesAvailable.budget.toFixed(0)} ש"ח.`);
        // }
    }


    function replenishResources() {
         // Simple daily replenishment + potential random bonus
        resources.vetTime += dailyResourceReplenishment.vetTime;
        resources.specialFood += dailyResourceReplenishment.specialFood;
        // Cages are not replenished daily
        resources.budget += dailyResourceReplenishment.budget;

         // Random event: Donation!
         if (Math.random() < 0.15) { // 15% chance of a donation
             const donationAmount = Math.floor(Math.random() * 300) + 100; // Between 100 and 400
             resources.budget += donationAmount;
             addMessage(`🎁 קיבלנו תרומה נדיבה בסך ${donationAmount} ש"ח!`, 'animal-event');
         }
          // Random event: Vet on leave!
          if (Math.random() < 0.05) { // 5% chance of vet time reduction
              const reduction = Math.floor(resources.vetTime * 0.3); // Reduce by 30%
              resources.vetTime = Math.max(0, resources.vetTime - reduction);
              addMessage(`⏰ הווטרינר הראשי בחופשה קצרה, זמן הוטרינר היומי מוגבל יותר היום (-${reduction} יח').`, 'warning');
          }
    }


    function processNextDay() {
        gameDay++;
        addMessage(`--- מתחיל יום ${gameDay} במרכז ההצלה ---`, 'system');
        replenishResources(); // Get resources for the new day
        processActiveAnimals(); // Animals in care either heal, die, or continue, consuming resources
        addNewAnimal(); // New cases might arrive
        updateUI(); // Update display

         // Check for lose condition (optional)
         // if (resources.budget < -1000 || activeAnimals.filter(a => !['released', 'euthanized'].includes(a.status)).length > maxActiveAnimals + 10) {
         //     addMessage("❌ המרכז קרס תחת העומס והחובות. סוף המשחק.", 'negative-event');
         //     document.getElementById('nextDayBtn').disabled = true;
         // }
    }

    function updateUI() {
        updateResourcesDisplay();
        updateStatusDisplay();
        renderIncomingAnimals();
        renderActiveAnimals();
    }

     function toggleExplanation() {
        const explanationDiv = document.getElementById('explanation');
        const button = document.getElementById('toggleExplanation');
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            button.textContent = 'הסתרת הסבר';
        } else {
            explanationDiv.style.display = 'none';
            button.textContent = 'הצגת הסבר / הסתרת הסבר';
        }
    }

    // Initial setup
     gameDay = 1; // Start on Day 1
    addMessage(`--- ברוכים הבאים ליום הראשון במרכז ההצלה! ---`, 'system');
    addNewAnimal(); // Add initial animals
    addNewAnimal(); // Add a second initial animal for variety
    updateUI(); // Render initial state

</script>
```