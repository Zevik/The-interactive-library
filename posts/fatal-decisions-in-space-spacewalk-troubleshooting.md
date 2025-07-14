---
title: "בין חיים למוות: החלטות קריטיות בהליכת חלל"
english_slug: fatal-decisions-in-space-spacewalk-troubleshooting
category: "פסיכולוגיה"
tags: [קבלת החלטות, פסיכולוגיה קוגניטיבית, חלל, הליכת חלל, לחץ, הישרדות]
---

דמיינו את זה: אתם מרחפים שקט מחוץ לתחנת החלל הבינלאומית, קוסמוס אינסופי פרוש סביבכם, כדור הארץ הכחול מטה. פתאום – אזעקה צורמנית בחליפה! תקלה קריטית. חמצן אוזל. זמן דוחק. אין מקום לטעויות. כל שבריר שנייה, כל החלטה, עלולה לשנות את מסלול חייכם. איך שומרים על קור רוח ומקבלים את ההחלטה הנכונה כשגורלכם תלוי על חוט השערה?

<div id="spacewalk-simulator">
    <div class="status-bar">
        <div class="status-item oxygen-status">חמצן: <span id="oxygen">100%</span></div>
        <div class="status-item time-status">זמן: <span id="time">10:00</span></div>
        <div class="status-item system-status">מערכת: <span id="system-status">תקינה</span></div>
        <div class="status-item overall-status">מצב כללי: <span id="overall-status">רגוע</span></div>
    </div>
     <div id="visual-cue"></div> <!-- Simple visual cue area -->
    <div id="scenario-display">
        <p id="scenario-text"></p>
    </div>
    <div id="action-options">
        <!-- Buttons will be populated by JS -->
    </div>
    <div id="feedback-display">
        <p id="feedback-text"></p>
    </div>
    <button id="restart-button" style="display: none;">התחל משימה מחדש</button>
</div>

<style>
    :root {
        --space-blue: #1a237e;
        --space-dark: #0a1128;
        --space-accent: #0077cc;
        --status-green: #4CAF50;
        --status-orange: #FF9800;
        --status-red: #F44336;
        --text-light: #e3f2fd;
        --text-dark: #333;
        --card-bg: #1e3a5f;
    }

    body {
        background-color: var(--space-dark);
        color: var(--text-light);
        font-family: 'Arial', sans-serif; /* Changed font */
        direction: rtl;
        text-align: right;
        line-height: 1.6;
    }

    #spacewalk-simulator {
        border: 2px solid var(--space-accent);
        padding: 30px; /* More padding */
        margin: 30px auto; /* More margin */
        max-width: 800px; /* Wider */
        background: linear-gradient(145deg, var(--card-bg), #10203a); /* Gradient background */
        border-radius: 12px; /* More rounded corners */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5); /* Deeper shadow */
        overflow: hidden; /* For potential animations */
    }

     #visual-cue {
         min-height: 20px; /* Placeholder for visual cues */
         margin-bottom: 15px;
         text-align: center;
         font-size: 1.2rem;
         color: var(--status-orange); /* Default color for alerts */
     }

    .status-bar {
        display: flex;
        justify-content: space-around;
        margin-bottom: 25px; /* More space */
        padding: 15px; /* More padding */
        background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark */
        border-radius: 8px; /* Rounded */
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .status-item {
        font-weight: bold;
        color: var(--text-light);
        font-size: 1.1rem; /* Larger font */
        display: flex;
        align-items: center;
    }

    .status-item span {
        margin-right: 8px; /* Space between label and value */
    }

     .oxygen-status span, .time-status span, .system-status span, .overall-status span {
        transition: color 0.5s ease; /* Smooth color transition */
     }


    #scenario-display {
        margin-bottom: 25px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.08); /* Semi-transparent white */
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 8px;
        min-height: 100px; /* Taller */
        display: flex; /* Center text vertically */
        align-items: center;
        transition: background-color 0.5s ease;
    }
     #scenario-text {
         margin: 0; /* Remove default margin */
         font-size: 1.1rem;
     }


    #action-options {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* Adjust column size */
        gap: 15px; /* Larger gap */
        margin-bottom: 25px;
    }

    .action-button {
        padding: 12px 15px; /* More padding */
        background: linear-gradient(180deg, var(--space-accent), #0056b3); /* Gradient button */
        color: var(--text-light);
        border: none;
        border-radius: 6px; /* More rounded */
        cursor: pointer;
        font-size: 1.1rem;
        transition: background 0.3s ease, transform 0.1s ease; /* Smooth transition and subtle press effect */
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    .action-button:hover {
        background: linear-gradient(180deg, #0088ff, #0066cc); /* Brighter gradient on hover */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
    }

     .action-button:active {
         transform: scale(0.98); /* Slightly shrink on click */
         box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
     }

     .action-button:disabled {
         background: #5a6268;
         cursor: not-allowed;
         opacity: 0.7;
     }


    #feedback-display {
        margin-top: 25px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 8px;
        min-height: 60px; /* Taller */
        display: flex;
        align-items: center;
        font-style: italic;
        color: var(--text-light);
        transition: background-color 0.5s ease;
    }
     #feedback-text {
         margin: 0;
         font-size: 1rem;
     }

    #restart-button {
        display: block;
        width: 100%;
        padding: 18px; /* More padding */
        background-color: var(--status-green); /* Green for restart */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.2rem; /* Larger font */
        margin-top: 30px; /* More space */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    #restart-button:hover {
        background-color: #388e3c; /* Darker green */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
    }

     #restart-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
     }


    #explanation-button {
        display: block;
        width: 100%;
        padding: 18px;
        background-color: var(--space-blue); /* Space blue for explanation */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.2rem;
        margin-top: 40px; /* More space */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
     #explanation-button:hover {
        background-color: #151c5b; /* Darker blue */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4);
     }
     #explanation-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
     }


    #explanation-section {
        margin-top: 40px;
        padding: 30px;
        background-color: #ffffff; /* White background for readability */
        border: 1px solid var(--space-accent);
        border-radius: 12px;
        display: none; /* Initially hidden */
        color: var(--text-dark); /* Dark text */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
    }
    #explanation-section h2 {
        color: var(--space-accent);
        border-bottom: 2px solid var(--space-accent);
        padding-bottom: 15px;
        margin-bottom: 25px;
        font-size: 1.8rem;
    }
     #explanation-section h3 {
        color: var(--space-blue);
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 1.4rem;
     }
     #explanation-section p, #explanation-section li {
        line-height: 1.8; /* Increased line height */
        color: var(--text-dark);
        margin-bottom: 12px; /* More space between paragraphs/list items */
        font-size: 1.1rem;
     }
    #explanation-section ul {
        padding-right: 20px; /* Indent list */
    }
     #explanation-section li {
         margin-bottom: 8px;
     }

    /* Status Color Classes */
    .status-green { color: var(--status-green); }
    .status-orange { color: var(--status-orange); }
    .status-red { color: var(--status-red); }

    /* Pulse Animation */
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    .pulsing {
        animation: pulse 1s infinite ease-in-out;
    }

    /* Scenario Text Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    #scenario-text {
        animation: fadeIn 0.6s ease-out;
    }
     #feedback-text {
        animation: fadeIn 0.6s ease-out;
     }

</style>

<button id="explanation-button">הצג הסבר והקשר לפסיכולוגיה קוגניטיבית</button>

<div id="explanation-section">
    <h2>הקשר בין החלטות גורליות בחלל לפסיכולוגיה קוגניטיבית</h2>

    <p>הסימולציה שבה התנסית שמה אותך בנעלי אסטרונאוט המתמודד עם סכנה מיידית בסביבת העבודה העוינת ביותר שידועה לאדם: הריק של החלל. הליכת חלל (EVA - Extravehicular Activity) היא פסגת האתגר הטכני והפסיכולוגי. דמיינו את הבידוד, את התלות המוחלטת בחליפה זעירה, ואת ההשלכות הקטסטרופליות של כל תקלה. זהו כר פורה לחקר תהליכי קבלת החלטות תחת לחץ קיצוני.</p>

    <h3>קבלת החלטות תחת לחץ: כשהמוח נכנס למצב הישרדות</h3>
    <p>במצב סכנת חיים, המערכת הלימבית במוח, האחראית על תגובות רגשיות והישרדותיות, משתלטת למעשה על קליפת המוח הקדם-מצחית, האחראית על חשיבה רציונלית, תכנון ושליטה. התגובה הפרימיטיבית של "הילחם או ברח" מציפה את הגוף באדרנלין ובקורטיזול, מחדדת את החושים לאיום המיידי, אך עלולה לפגוע ביכולת לעבד מידע מורכב, לשקול חלופות בנחת, ולראות את התמונה הרחבה. זה בדיוק המצב בו אסטרונאוט עם דליפת חמצן צריך לקבל החלטה.</p>

    <h3>מלכודות קוגניטיביות בלחץ גבוה</h3>
    <p>תחת עומס קוגניטיבי ורגשי, המוח נוטה לפנות לקיצורי דרך מחשבתיים (היוריסטיקות) שעלולים להוביל להטיות קוגניטיביות - טעויות שיטתיות בקבלת החלטות:</p>
    <ul>
        <li><strong>ראיית מנהרה (Tunnel Vision):</strong> התמקדות אובססיבית באספקט אחד של הבעיה (למשל, ניסיון תיקון חוזר ונשנה של אותו רכיב) תוך התעלמות ממידע קריטי אחר (כמו מפלס חמצן צונח) או חלופות חשובות (כמו חזרה מיידית).</li>
        <li><strong>הטיית עיגון (Anchoring Bias):</strong> היצמדות למידע הראשוני שהתקבל (למשל, אבחנה ראשונית של התקלה) או לתוכנית הפעולה המקורית, גם כאשר נתונים חדשים מצביעים על הצורך בשינוי כיוון דרסטי.</li>
        <li><strong>הטיית הסטטוס קוו (Status Quo Bias):</strong> העדפה מובנית להישאר במצב הנוכחי ולהימנע מקבלת החלטה אקטיבית, גם כאשר היעדר פעולה הוא למעשה החלטה מסוכנת בפני עצמה שעלולה להוביל לאובדן זמן קריטי.</li>
         <li><strong>הטיית הזמינות (Availability Bias):</strong> הערכת יתר של סבירותו של אירוע או נקיטת פעולה מסוימת רק כי היא זמינה בקלות בזיכרון או עלתה ראשונה בראש (למשל, ניסיון לתקן כי "תיקון" הוא הפעולה הראשונה שקופצת לראש במקרה של תקלה).</li>
    </ul>

    <h3>אסטרטגיות הישרדות פסיכולוגיות: כיצד אסטרונאוטים מתאמנים?</h3>
    <p>הכשרת אסטרונאוטים כוללת מרכיב פסיכולוגי משמעותי שנועד לנטרל או למזער את ההשפעות המזיקות של לחץ והטיות קוגניטיביות:</p>
    <ul>
        <li><strong>תרגול פרוטוקולי חירום:</strong> שינון וביצוע אוטומטי כמעט של נהלים קריטיים מפחית את הצורך בחשיבה מורכבת בזמן אמת. שימוש בצ'קליסטים (גם אם דיגיטליים בחליפה) מבטיח ששלבים חיוניים לא יישכחו.</li>
        <li><strong>סימולציות מציאותיות:</strong> חשיפה חוזרת ונשנית למצבי חירום מדומים בסימולטורים ריאליסטיים בונה עמידות מנטלית, משפרת את התפקוד הקוגניטיבי תחת לחץ, ומאפשרת זיהוי התגובות האישיות ללחץ.</li>
        <li><strong>ניהול עומס מידע:</strong> אימון בסינון מהיר של מידע, זיהוי המדדים הקריטיים ביותר (כמו מפלס חמצן וזמן שנותר), והתעלמות מרעשי רקע.</li>
        <li><strong>תקשורת תחת לחץ:</strong> שמירה על תקשורת בהירה, תמציתית ויעילה עם בקרת המשימה ו/או חברי צוות אחרים מאפשרת קבלת סיוע, פרספקטיבה חיצונית ואימות החלטות. בקרת המשימה משמשת כ"מוח חיצוני" המסייע בקבלת החלטות רציונליות כשהאסטרונאוט נמצא תחת לחץ עצום.</li>
        <li><strong>מודעות עצמית:</strong> הכרה בתסמינים הפיזיולוגיים והקוגניטיביים של לחץ (דופק מהיר, קושי בריכוז, ראיית מנהרה) ולמידת טכניקות הרגעה בסיסיות.</li>
    </ul>

    <h3>מעבר לחלל: יישומים בחיי היומיום</h3>
    <p>העקרונות של קבלת החלטות תחת לחץ רלוונטיים לא רק לאסטרונאוטים. נהגי מרוצים, כירורגים, טייסים, כבאים, וכל אדם במצבי חירום אישיים או מקצועיים, יכולים להפיק תועלת מהבנת המגבלות הקוגניטיביות בלחץ ומהשימוש באסטרטגיות לשיפור הביצועים: הכנה מראש, הסתמכות על תהליכים, ניהול מידע, והתייעצות. גם במצבים פחות דרמטיים, הבנת ההטיות הקוגניטיביות שלנו יכולה לשפר את איכות ההחלטות היומיומיות.</p>
</div>

<script>
    const oxygenDisplay = document.getElementById('oxygen');
    const timeDisplay = document.getElementById('time');
    const systemStatusDisplay = document.getElementById('system-status');
    const overallStatusDisplay = document.getElementById('overall-status');
    const scenarioTextElement = document.getElementById('scenario-text'); // Renamed to avoid conflict
    const actionOptionsDiv = document.getElementById('action-options'); // Renamed to avoid conflict
    const feedbackTextElement = document.getElementById('feedback-text'); // Renamed to avoid conflict
    const restartButton = document.getElementById('restart-button');
    const explanationButton = document.getElementById('explanation-button');
    const explanationSection = document.getElementById('explanation-section');
    const visualCueElement = document.getElementById('visual-cue'); // Added visual cue element

    let gameState = {
        oxygen: 100,
        time: 600, // seconds, 10 minutes
        systemStatus: 'תקינה',
        overallStatus: 'רגוע',
        currentScenario: 'start',
        isGameOver: false,
        timer: null,
        consultedMissionControl: false, // New state: did they consult?
        checkedManual: false, // New state: did they check the manual?
        stressLevel: 0, // New state: accumulates stress
        proximityToAirlock: 0 // New state: 0 = far, 100 = at airlock
    };

    const scenarios = {
        start: {
            text: 'אתה מבצע תיקון שגרתי מחוץ לתחנה. הנוף עוצר נשימה... אך לפתע, אזעקת תקלה צורמנית מתפרצת בחליפה! "דליפת חמצן קטנה מזוהה במערכת המחזור." מפלס החמצן יורד לאט מהרגיל. מהי תגובתך המיידית?',
            options: ['fix-component', 'return-to-airlock', 'consult-mission-control', 'check-manual'],
            feedback: {
                'fix-component': 'אתה מתעלם מהאזעקה ומנסה לאתר ולתקן את הדליפה באופן מיידי. ריכוז מלא נדרש...',
                'return-to-airlock': 'הישרדות היא בראש סדר העדיפויות! אתה מתחיל לנוע במהירות המרבית האפשרית לעבר מנעל האוויר. התנועה המואצת מגבירה מעט את צריכת החמצן.',
                'consult-mission-control': 'אתה פותח ערוץ תקשורת חירום עם בקרת המשימה בכדור הארץ. אתה מדווח על התקלה וממתין להנחיות. התשובה עשויה לקחת רגעים יקרים.',
                'check-manual': 'אתה ניגש לתצוגה הפנימית של החליפה ומחפש במדריך החירום הפרוצדורה הרלוונטית לדליפת חמצן. זה דורש ניווט מהיר במידע.'
            },
            outcomes: {
                 'fix-component': 'scenario_fix_attempt_1',
                 'return-to-airlock': 'scenario_return_start',
                 'consult-mission-control': 'scenario_consult_start',
                 'check-manual': 'scenario_manual_start'
            }
        },
        scenario_fix_attempt_1: {
            text: 'ניסית לתקן, אך ללא הצלחה. האזעקה ממשיכה, הדליפה לא נעצרה. האם תנסה שוב, או שתשנה גישה?',
            options: ['fix-component', 'return-to-airlock', 'consult-mission-control', 'check-manual'],
             feedback: {
                'fix-component': 'אולי פספסת משהו קודם? אתה מנסה לאתר ולתקן שוב, תחת לחץ גובר.',
                'return-to-airlock': 'די! הגיע הזמן לסגת באופן מבוקר.',
                'consult-mission-control': 'אולי בקרת המשימה כבר מצאה פתרון יעיל יותר?',
                'check-manual': 'חייבים למצוא עכשיו פרוצדורה מאושרת!'
            },
             outcomes: {
                 'fix-component': 'scenario_fix_attempt_2', // Costs more time/oxygen, increases stress
                 'return-to-airlock': 'scenario_return_start',
                 'consult-mission-control': 'scenario_consult_continue',
                 'check-manual': 'scenario_manual_start' // Still first time checking manual in this flow
            },
            effects: { oxygen: -7, time: -75, systemStatus: 'דליפה נמשכת', overallStatus: 'לחוץ' } // Increased drain/time cost
        },
         scenario_fix_attempt_2: {
            text: 'הניסיון השני גם נכשל... התסכול עולה, ובזבזת עוד זמן וחמצן קריטיים. הדליפה נמשכת, המצב מחמיר במהירות.',
            options: ['return-to-airlock', 'consult-mission-control', 'check-manual'], // Removed fix option - too risky alone now
             feedback: {
                'return-to-airlock': 'זה מסוכן מדי להישאר בחוץ. אתה מפנה את כל המשאבים לחזרה מיידית.',
                'consult-mission-control': 'חייבים עזרה מבקרה עכשיו, אין זמן נוסף לניסויים.',
                'check-manual': 'סיכוי אחרון למצוא משהו שיכול לעזור במדריך.'
            },
             outcomes: {
                 'return-component': 'scenario_return_start', // Note: changed from fix-component
                 'return-to-airlock': 'scenario_return_start',
                 'consult-mission-control': 'scenario_consult_critical',
                 'check-manual': 'scenario_manual_start' // Still first time checking manual in this path
            },
            effects: { oxygen: -12, time: -100, systemStatus: 'דליפה מתמשכת ומחמירה', overallStatus: 'מצב קריטי!' } // Higher drain/time cost, more stress
        },
        scenario_return_start: {
            text: 'אתה בדרך חזרה למנעל האוויר. כל שנייה חשובה. הדליפה נמשכת.',
            options: ['consult-mission-control', 'check-manual'], // Cannot fix while returning, already returning
             feedback: {
                 'consult-mission-control': 'אתה יוצר קשר עם בקרת המשימה תוך כדי תנועה מהירה.',
                 'check-manual': 'אתה מנסה לדפדף במדריך תוך כדי חזרה - דורש ריכוז רב ויכול להיות מסוכן.'
             },
             outcomes: {
                 'consult-mission-control': 'scenario_return_consult',
                 'check-manual': 'scenario_return_manual', // Risk of damage if checkedManual is false
             },
             effects: { oxygen: -8, time: -60, systemStatus: 'דליפה נמשכת', overallStatus: 'בדרך למנעל' } // Base cost of returning
        },
         scenario_return_manual: {
            text: 'ניסית לעיין במדריך תוך כדי תנועה מהירה. זה היה קשה ומסוכן. [Outcome depends on luck/stress]', // Outcome determined in handleAction
            options: ['consult-mission-control'], // Only consult left as primary action
             feedback: {
                 'consult-mission-control': 'חייבים עזרה חיצונית עכשיו.'
             },
             outcomes: {
                 'consult-mission-control': 'scenario_return_consult',
                 'fail_damage': 'scenario_minor_damage' // New potential failure state
             },
              effects: { oxygen: -5, time: -30, systemStatus: 'דליפה נמשכת', overallStatus: 'בדרך למנעל, מוסח' }
        },
         scenario_minor_damage: {
             text: 'איבדת לרגע שיווי משקל ופגעת קלות ברכיב חיצוני של המנעל האוויר! לא נזק קריטי לחליפה, אבל איבדת זמן יקר והלחץ גובר. עדיין בדרך חזרה.',
             options: ['consult-mission-control'],
              feedback: {
                 'consult-mission-control': 'חייבים עזרה עכשיו, כל היתר נכשל.'
              },
             outcomes: {
                 'consult-mission-control': 'scenario_return_consult',
             },
             effects: { oxygen: -7, time: -45, systemStatus: 'דליפה נמשכת, נגרם נזק קל לסביבה', overallStatus: 'בדרך למנעל, המצב מסוכן יותר' } // Added penalty
         },
         scenario_return_consult: {
            text: 'אתה מדווח לבקרת המשימה תוך כדי חזרה. הם מקבלים את הנתונים ומנתחים אותם במהירות. הם יכולים להציע פתרון חירום רק אם תצליח להגיע קרוב מספיק בזמן.',
            options: [], // No actions, just waiting/moving
             feedback: {}, // No immediate feedback from action
             outcomes: { // Outcome depends on time/oxygen remaining and proximity
                 'default': 'scenario_return_final_approach'
             },
             effects: { oxygen: -10, time: -90, systemStatus: 'דליפה נמשכת', overallStatus: 'ממתין להוראות בדרך' } // More time/oxygen drain while communicating/moving
        },
        scenario_return_final_approach: {
            text: 'אתה ממש ליד מנעל האוויר. האם הגעת בזמן? האם נשאר לך מספיק חמצן? [Outcome based on stats]',
             options: [], // No actions, this is the final check
             feedback: {},
             outcomes: {
                 'win': 'scenario_safe_return',
                 'lose': 'scenario_ran_out' // Or time out, determined by checkWinLoseConditions
             },
             effects: { oxygen: -5, time: -30, systemStatus: 'קרוב למנעל', overallStatus: 'מתקרב לסוף' }
        },
         scenario_consult_start: {
            text: 'בקרת המשימה מנתחת את הנתונים. הם זקוקים לזמן כדי להעריך את המצב המלא ולהציע פתרון. הדליפה נמשכת.',
            options: ['fix-component', 'return-to-airlock', 'check-manual'], // Player can decide what to do while waiting
             feedback: {
                 'fix-component': 'אתה לא מחכה לבקרה ומנסה לתקן שוב בעצמך.',
                 'return-to-airlock': 'החלטת לא לבזבז זמן נוסף ופשוט לחזור.',
                 'check-manual': 'אולי תמצא מידע שימושי במדריך בזמן ההמתנה?'
             },
             outcomes: {
                 'fix-component': 'scenario_fix_attempt_1',
                 'return-to-airlock': 'scenario_return_start',
                 'check-manual': 'scenario_manual_start',
             },
             effects: { oxygen: -6, time: -70, systemStatus: 'דליפה נמשכת', overallStatus: 'ממתין להוראות' }
        },
         scenario_consult_continue: {
            text: 'בקרת המשימה עדיין מנתחת. הם מבקשים הבהרות או נתונים נוספים ממך. הדליפה ממשיכה.',
             options: ['return-to-airlock', 'check-manual'], // Fix is still risky without guidance or manual knowledge
             feedback: {
                 'return-to-airlock': 'החלטת שהגיע הזמן לחזור, גם ללא פתרון מבקרה.',
                 'check-manual': 'אין זמן לחכות, אתה מחפש מידע במדריך תוך כדי.'
             },
             outcomes: {
                 'return-to-airlock': 'scenario_return_start',
                 'check-manual': 'scenario_manual_start', // Still first time checking manual in this path
             },
             effects: { oxygen: -8, time: -100, systemStatus: 'דליפה נמשכת', overallStatus: 'ממתין בלחץ' } // Increased time/oxygen cost
         },
         scenario_consult_critical: {
            text: 'בקרת המשימה קולטת שהמצב קריטי! הם סוף סוף מצאו פתרון חירום אפשרי! הם מורים לך לבצע סדרת פעולות מסוימות תוך כדי תנועה חזרה למנעל האוויר. עליך לפעול *בדיוק* לפי ההוראות ובמהירות!',
             options: ['perform-procedure', 'return-to-airlock'], // New option based on consult, or just run
              feedback: {
                 'perform-procedure': 'אתה מתחיל לבצע את הפרוצדורה המורכבת לפי הנחיות בקרה.',
                 'return-to-airlock': 'החלטת שלא לקחת סיכון נוסף ולנטוש את התיקון לטובת חזרה מיידית, מקווה שתספיק.'
             },
             outcomes: {
                 'perform-procedure': 'scenario_perform_procedure', // High chance of success with consult
                 'return-to-airlock': 'scenario_return_start', // Might be too late depending on stats
             },
             effects: { oxygen: -10, time: -60, systemStatus: 'דליפה נמשכת, יש הנחיות מבקרה', overallStatus: 'יש סיכוי להצלה!' }
         },
        scenario_manual_start: {
            text: 'חיפשת במדריך החירום ומצאת פרוצדורה המתאימה לדליפות מסוג זה. היא נראית מסובכת לביצוע עצמאי בחלל. האם תנסה לבצע אותה, תחזור, או תתייעץ עם בקרה על מה שמצאת?',
            options: ['perform-procedure', 'return-to-airlock', 'consult-mission-control'], // Option to perform procedure based on manual
            feedback: {
                 'perform-procedure': 'אתה מנסה לבצע את הפרוצדורה שמצאת במדריך, relying on your training.',
                 'return-to-airlock': 'מחליט שגם אם מצאת מידע, עדיף לחזור מיד למנעל האוויר.',
                 'consult-mission-control': 'אתה מתקשר לבקרת המשימה כדי לאשר את הפרוצדורה שמצאת ולקבל עליה הנחיות.'
             },
             outcomes: {
                 'perform-procedure': 'scenario_perform_procedure', // Chance of success depends on if also consulted
                 'return-to-airlock': 'scenario_return_start',
                 'consult-mission-control': 'scenario_manual_consult'
             },
             effects: { oxygen: -6, time: -70, systemStatus: 'דליפה נמשכת', overallStatus: 'יש מידע חלקי' }
        },
         scenario_manual_consult: {
             text: 'אתה מתייעץ עם בקרת המשימה לגבי הפרוצדורה שמצאת במדריך. הם מאשרים שהיא רלוונטית, אך מדגישים שדורשת ביצוע *מדויק ומהיר ביותר*. הם מספקים כמה טיפים קריטיים לביצוע בחלל.',
             options: ['perform-procedure', 'return-to-airlock'],
             feedback: {
                 'perform-procedure': 'מבצע את הפרוצדורה המורכבת, כעת עם אישור וטיפים מבקרה.',
                 'return-to-airlock': 'מחליט שהסיכון גדול מדי גם עם אישור בקרה, ופשוט חוזר במהירות המרבית.'
             },
             outcomes: {
                 'perform-procedure': 'scenario_perform_procedure', // Highest chance of success now
                 'return-to-airlock': 'scenario_return_start',
             },
             effects: { oxygen: -5, time: -60, systemStatus: 'דליפה נמשכת, יש אישור והנחיות מבקרה', overallStatus: 'מוכן לנסות תיקון!' }
         },
        scenario_perform_procedure: {
            text: 'אתה מתחיל לבצע את פרוצדורת התיקון המורכבת. הידיים רועדות קלות מהלחץ, אבל אתה מנסה להתרכז. [Outcome depends on preparation and state]',
            options: [], // Action is performing the procedure - outcome will be calculated
             feedback: {},
             outcomes: {
                 // Outcomes calculated in handleAction based on gameState.consultedMissionControl, gameState.checkedManual, gameState.stressLevel
             },
             effects: { oxygen: -15, time: -120, systemStatus: 'מנסה לתקן', overallStatus: 'מותח ביותר' } // Procedure takes significant time/oxygen
        },
        // End states
        scenario_safe_return: {
            text: 'הגעת בבטחה למנעל האוויר בדיוק בזמן! התקלה נוטרלה או שניתן לטפל בה בפנים. קבלת ההחלטות שלך הצילה את המשימה ואת חייך! כל הכבוד, אסטרונאוט!',
            options: [],
            type: 'win'
        },
         scenario_ran_out: {
            text: 'מפלס החמצן ירד מתחת לסף הקריטי... הנשימה הופכת קשה... העולם מתחיל להחוויר סביבך... סוף המשימה. נכשלת לשרוד את הריק הקטלני.',
            options: [],
            type: 'lose'
        },
         scenario_time_out: {
             text: 'הזמן המוקצב למשימה הסתיים לפני שהשלמת את המשימה או חזרת לבטחה. התחנה התרחקה מדי, או שהתקלה הפכה בלתי הפיכה. סוף המשימה. נכשלת.',
            options: [],
            type: 'lose'
         }
    };

     // Map action names to Hebrew text for buttons
    const actionNameMap = {
        'fix-component': 'נסה לתקן רכיב',
        'return-to-airlock': 'חזור למנעל האוויר',
        'consult-mission-control': 'התייעץ עם בקרה',
        'check-manual': 'עיין במדריך',
        'perform-procedure': 'בצע פרוצדורת תיקון',
        'execute-shutdown': 'בצע כיבוי מערכת' // Example, not used in current scenarios but good to have
    };


    function updateDisplay() {
        // Update values
        oxygenDisplay.textContent = `${Math.max(0, gameState.oxygen)}%`;
        const minutes = Math.floor(gameState.time / 60);
        const seconds = gameState.time % 60;
        timeDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        systemStatusDisplay.textContent = gameState.systemStatus;
        overallStatusDisplay.textContent = gameState.overallStatus;

        // Update colors and pulsing based on thresholds
        oxygenDisplay.style.color = gameState.oxygen <= 20 ? var(--status-red) : (gameState.oxygen <= 50 ? var(--status-orange) : var(--status-green));
        timeDisplay.style.color = gameState.time <= 60 ? var(--status-red) : (gameState.time <= 180 ? var(--status-orange) : var(--status-green));
        systemStatusDisplay.style.color = gameState.systemStatus.includes('חמורה') ? var(--status-red) : (gameState.systemStatus.includes('נמשכת') ? var(--status-orange) : var(--status-green));
        overallStatusDisplay.style.color = gameState.overallStatus.includes('קריטי') || gameState.overallStatus.includes('מסוכן') ? var(--status-red) : (gameState.overallStatus.includes('לחוץ') || gameState.overallStatus.includes('מותח') ? var(--status-orange) : var(--status-green));


        // Add pulsing effect
        const oxygenStatusItem = oxygenDisplay.parentElement;
        const timeStatusItem = timeDisplay.parentElement;
        const overallStatusItem = overallStatusDisplay.parentElement;

        oxygenStatusItem.classList.toggle('pulsing', gameState.oxygen <= 20);
        timeStatusItem.classList.toggle('pulsing', gameState.time <= 60);
         // Pulse overall status if critical
         overallStatusItem.classList.toggle('pulsing', gameState.overallStatus.includes('קריטי') || gameState.overallStatus.includes('מסוכן'));

        // Update visual cue based on overall status
        if (gameState.overallStatus.includes('קריטי') || gameState.overallStatus.includes('מסוכן')) {
             visualCueElement.textContent = "⚠️ מצב חירום קריטי! ⚠️";
             visualCueElement.style.color = var(--status-red);
        } else if (gameState.overallStatus.includes('לחוץ') || gameState.overallStatus.includes('מותח')) {
             visualCueElement.textContent = "❗ לחץ גובר ❗";
             visualCueElement.style.color = var(--status-orange);
        } else if (gameState.overallStatus.includes('בדרך') && !gameState.overallStatus.includes('מוסח')) {
             visualCueElement.textContent = "🚀 חוזר לתחנה...";
             visualCueElement.style.color = var(--status-green);
        } else {
             visualCueElement.textContent = ""; // Clear if calm
        }


        if (gameState.isGameOver) {
            actionOptionsDiv.innerHTML = ''; // Remove action buttons
            restartButton.style.display = 'block';
        } else {
             restartButton.style.display = 'none';
        }
    }

    function endGame(type) {
        gameState.isGameOver = true;
        clearInterval(gameState.timer);
        actionOptionsDiv.innerHTML = ''; // Hide buttons
        scenarioTextElement.textContent = scenarios[gameState.currentScenario].text; // Display final scenario text
        feedbackTextElement.textContent = type === 'win' ? 'כל הכבוד, אסטרונאוט! הצלחת להתמודד עם התקלה הקטלנית ולשרוד!' : 'המשימה הסתיימה באופן טרגי. למד מהטעויות הפסיכולוגיות והטכניות ונסה שוב לשרוד את הריק.';
        feedbackTextElement.style.color = type === 'win' ? var(--status-green) : var(--status-red);
        restartButton.style.display = 'block';
        updateDisplay();
    }

    function checkWinLoseConditions() {
         if (gameState.oxygen <= 0) {
             gameState.currentScenario = 'scenario_ran_out';
             endGame('lose');
             return true;
         }
         if (gameState.time <= 0) {
             gameState.currentScenario = 'scenario_time_out';
             endGame('lose');
             return true;
         }

         // Check for specific win/lose scenarios that are explicit end states
         if (scenarios[gameState.currentScenario].type === 'win') {
             endGame('win');
             return true;
         }
          if (scenarios[gameState.currentScenario].type === 'lose') {
             endGame('lose');
             return true;
         }

         return false;
    }

    function gameLoop() {
        if (gameState.isGameOver) return;

        // Apply passive oxygen/time drain
         // Base drain + extra drain based on system status
        let oxygenDrainPerTick = 1;
        if (gameState.systemStatus.includes('נמשכת')) oxygenDrainPerTick += 0.5; // Small leak
        if (gameState.systemStatus.includes('מחמירה')) oxygenDrainPerTick += 1; // Medium leak
        if (gameState.systemStatus.includes('חמורה')) oxygenDrainPerTick += 2; // Severe leak
        if (gameState.systemStatus.includes('איטית קלות')) oxygenDrainPerTick -= 0.5; // Reduced drain

        gameState.oxygen -= oxygenDrainPerTick;
        gameState.time -= 1; // Time always ticks down

         // Simulate stress increase - increases faster with bad overall status
         gameState.stressLevel += 0.1 * (gameState.overallStatus.includes('קריטי') ? 2 : (gameState.overallStatus.includes('לחוץ') ? 1.5 : 1));


        // Simulate proximity decrease if returning
         if (gameState.overallStatus.includes('בדרך למנעל')) {
             gameState.proximityToAirlock += 2; // Move 2 units closer per second
             gameState.proximityToAirlock = Math.min(100, gameState.proximityToAirlock); // Cap at 100
             // Maybe add visual cue for proximity? Not implemented visually yet, but state exists.
         }


        updateDisplay();

        // Check win/lose conditions
        if (checkWinLoseConditions()) return;

         // Handle automatic transitions after certain states if needed (none defined yet)
         // E.g., if in 'scenario_return_start' for X seconds, auto transition to 'scenario_return_final_approach'
         // For now, handle return final approach check within handleAction for simplicity after specific actions lead there.
    }

    function applyScenarioEffects(effects) {
        if (!effects) return;
        if (effects.oxygen !== undefined) gameState.oxygen += effects.oxygen; // oxygen is negative delta
        if (effects.time !== undefined) gameState.time += effects.time; // time is negative delta
        if (effects.systemStatus !== undefined) gameState.systemStatus = effects.systemStatus;
        if (effects.overallStatus !== undefined) gameState.overallStatus = effects.overallStatus;

        // Ensure oxygen and time don't go below zero before checkWinLoseConditions
        gameState.oxygen = Math.max(0, gameState.oxygen);
        gameState.time = Math.max(0, gameState.time);
    }


    function handleAction(action) {
        if (gameState.isGameOver) return;

        const current = scenarios[gameState.currentScenario];
        feedbackTextElement.textContent = current.feedback[action] || 'פעולה בוצעה.'; // Display action feedback

        // Apply effects immediately upon taking action (represents the cost of the action itself)
        // For this simple sim, let's keep effects linked to the *next* scenario for clarity as designed initially,
        // but add action-specific stress increase.
        gameState.stressLevel += 5; // Base stress per action
        if (action === 'fix-component' && (gameState.overallStatus.includes('קריטי') || gameState.overallStatus.includes('לחוץ'))) gameState.stressLevel += 10; // More stress if fixing under pressure
        if (action === 'return-to-airlock' && gameState.overallStatus.includes('קריטי')) gameState.stressLevel += 5; // Stress from desperate return
         if (action === 'check-manual' && gameState.overallStatus.includes('בדרך למנעל')) gameState.stressLevel += 15; // High stress checking manual while moving

        gameState.stressLevel = Math.min(100, gameState.stressLevel); // Cap stress

        // Update state based on action
        if (action === 'consult-mission-control') gameState.consultedMissionControl = true;
        if (action === 'check-manual') gameState.checkedManual = true;


        // Determine next scenario
        let nextScenarioKey;
        if (current.outcomes[action]) {
            nextScenarioKey = current.outcomes[action];
        } else if (current.outcomes['default']) {
            nextScenarioKey = current.outcomes['default'];
        } else {
             console.error(`No outcome defined for action ${action} in scenario ${gameState.currentScenario}`);
             // Transition to a specific error state or just end? Let's make it a failure for now.
             gameState.currentScenario = 'scenario_time_out'; // Arbitrary failure state
             endGame('lose');
             return;
        }

        // --- Complex Outcome Logic (Game-like) ---
        if (nextScenarioKey === 'scenario_perform_procedure') {
             // Outcome depends on preparation (consulted, manual), current stress, and current resources
             let successChance = 0.2; // Base chance of success

             if (gameState.checkedManual) successChance += 0.2; // Bonus for checking manual
             if (gameState.consultedMissionControl) successChance += 0.3; // Larger bonus for consulting mission control
              if (gameState.checkedManual && gameState.consultedMissionControl) successChance += 0.2; // Synergy bonus

             // Penalty for high stress and low resources
              const resourceMetric = (gameState.oxygen / 100) * (gameState.time / 600); // 0 to 1
              successChance -= (gameState.stressLevel / 100) * 0.3; // Stress penalizes chance
              successChance -= (1 - resourceMetric) * 0.2; // Low resources penalize chance

             successChance = Math.max(0.05, Math.min(0.95, successChance)); // Clamp between 5% and 95%

             console.log(`Perform Procedure Success Chance: ${successChance.toFixed(2)} (Manual: ${gameState.checkedManual}, Consulted: ${gameState.consultedMissionControl}, Stress: ${gameState.stressLevel.toFixed(0)}, Resources: ${resourceMetric.toFixed(2)})`);


             if (Math.random() < successChance) {
                 nextScenarioKey = 'scenario_safe_return_partial'; // Successful fix leads to partial safe return
             } else {
                 // Failure outcome depends on how bad the state is
                 if (resourceMetric < 0.2 || gameState.stressLevel > 70) { // Very low resources or very high stress -> critical failure
                     nextScenarioKey = 'scenario_fix_failed_critical';
                 } else { // Moderate state -> minor failure
                     nextScenarioKey = 'scenario_fix_failed_minor';
                 }
             }
        } else if (nextScenarioKey === 'scenario_return_final_approach') {
            // Outcome depends on remaining oxygen, time, and proximity (which increases passively)
             const survivalChance = (gameState.oxygen / 100) * (gameState.time / 600) * (gameState.proximityToAirlock / 100); // Needs good oxygen, time, AND to be close
             survivalChance = Math.max(0.05, Math.min(0.95, survivalChance)); // Clamp

             console.log(`Final Return Survival Chance: ${survivalChance.toFixed(2)} (Oxygen: ${gameState.oxygen}%, Time: ${gameState.time}s, Proximity: ${gameState.proximityToAirlock}%)`);


             if (Math.random() < survivalChance) {
                 nextScenarioKey = 'scenario_safe_return';
             } else {
                 nextScenarioKey = 'scenario_ran_out'; // Or time out, checkWinLoseConditions will handle time
             }
        } else if (nextScenarioKey === 'scenario_return_manual') {
            // Outcome of reading manual while returning depends on stress/luck
             let successChance = 0.7; // Base chance to avoid damage
             successChance -= (gameState.stressLevel / 100) * 0.5; // High stress makes it much riskier
             successChance = Math.max(0.1, Math.min(0.9, successChance));

             console.log(`Return Manual Avoid Damage Chance: ${successChance.toFixed(2)} (Stress: ${gameState.stressLevel.toFixed(0)})`);

             if (Math.random() < successChance) {
                 // No damage, but wasted time/oxygen and missed crucial manual info probably
                 // This scenario text needs adjustment - currently it says damage was caused.
                 // Let's make 'scenario_return_manual' *mean* you tried and failed slightly (minor damage/distraction).
                 // The text "איבדת לרגע שיווי משקל ופגעת קלות במנעל האוויר" implies failure.
                 // So, let's make the outcome of 'check-manual' *while returning* lead *directly* to the negative 'scenario_return_manual' state with penalties,
                 // UNLESS you had already checked the manual earlier and know exactly where to look (less stress).
                 // Revise scenario_return_start outcomes and scenario_return_manual logic.
                 // Okay, new plan: 'check-manual' while returning always leads to `scenario_return_manual`, which *describes* the difficulty/risk. The effects in `scenario_return_manual` are the *cost* of this risky action. No random chance needed here, the risk is inherent.
                 // This simplifies the outcome logic within handleAction for this specific transition.
                 // The text for `scenario_return_manual` will state the difficulty and potential issues.
             } else {
                 // The current scenario_return_manual already describes the negative outcome.
                 // I'll just apply the negative effects defined in scenario_return_manual's effects.
             }
        }
        // --- End Complex Outcome Logic ---


        // Transition to the determined next scenario
        gameState.currentScenario = nextScenarioKey;
        const next = scenarios[gameState.currentScenario];

         // Apply effects of the new scenario
        applyScenarioEffects(next.effects);


        // Update UI for the new scenario
        scenarioTextElement.textContent = next.text;
        actionOptionsDiv.innerHTML = ''; // Clear old options
        if (next.options && next.options.length > 0) {
            next.options.forEach(opt => {
                const button = document.createElement('button');
                button.classList.add('action-button');
                button.dataset.action = opt;
                button.textContent = actionNameMap[opt] || opt; // Use mapped name
                button.addEventListener('click', () => handleAction(opt));
                actionOptionsDiv.appendChild(button);
            });
        }

        updateDisplay();
        checkWinLoseConditions(); // Check conditions immediately after action, in case an action led directly to a win/lose state or triggered a condition (e.g., oxygen hit zero from effect).
    }


    function startGame() {
         gameState = {
            oxygen: 100,
            time: 600,
            systemStatus: 'תקינה',
            overallStatus: 'רגוע',
            currentScenario: 'start',
            isGameOver: false,
            timer: null,
            consultedMissionControl: false,
            checkedManual: false,
            stressLevel: 0,
            proximityToAirlock: 0
        };

        scenarioTextElement.textContent = scenarios.start.text;
        feedbackTextElement.textContent = 'המשימה החלה! קבל החלטות מהירות וחכמות כדי לשרוד את הליכת החלל.';
        feedbackTextElement.style.color = var(--text-light); // Reset feedback color

        restartButton.style.display = 'none';
        visualCueElement.textContent = ""; // Clear visual cue

        // Set up initial buttons
        actionOptionsDiv.innerHTML = '';
        scenarios.start.options.forEach(opt => {
            const button = document.createElement('button');
            button.classList.add('action-button');
            button.dataset.action = opt;
            button.textContent = actionNameMap[opt] || opt; // Use mapped name
            button.addEventListener('click', () => handleAction(opt));
            actionOptionsDiv.appendChild(button);
        });


        updateDisplay();

        // Start the game timer
        clearInterval(gameState.timer); // Clear any existing timer
        gameState.timer = setInterval(gameLoop, 1000); // Tick every 1 second
    }

    // Initialize the game when the page loads
    startGame();

    // Add event listener for restart button
    restartButton.addEventListener('click', startGame);

    // Add event listener for explanation button
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationSection.style.display === 'none';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר והקשר לפסיכולוגיה קוגניטיבית';
         // Optional: Scroll to the explanation section when shown
        if (!isHidden) {
             explanationSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    // Add a CSS variable helper (needed because CSS variables don't work directly in element.style)
     function getCssVar(name) {
        return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    }
     const var = (name) => getCssVar(`--${name}`);


</script>