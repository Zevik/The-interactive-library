---
title: "המסע המרתק להגנת המצאה: סימולטור הפטנטים הגדול"
english_slug: patent-application-simulator-process-v2
category: "משפטים"
tags: ["פטנט", "קניין רוחני", "המצאה", "חדשנות", "תהליך משפטי", "סימולטור", "למידה חווייתית"]
---
<h1>המסע המרתק להגנת המצאה: סימולטור הפטנטים הגדול</h1>

<p>יש לכם רעיון פורץ דרך שיכול לשנות את העולם? אתם חולמים להבטיח שההמצאה שלכם תהיה רק שלכם? תהליך רישום פטנט הוא הרפתקה מרתקת, אך גם מורכבת ורצופת שלבים מפתיעים. הסימולטור הזה מזמין אתכם לצלול אל תוך התהליך, לחוות את האתגרים וההצלחות, ולהבין טוב יותר מה באמת קורה מאחורי הקלעים בדרך לפטנט המיוחל.</p>

<div id="app">
    <div id="progress-bar">
        <div id="progress-fill"></div>
    </div>
    <div id="current-status">
        <h3><span id="status-emoji">💡</span> סטטוס המסע: <span id="status-text">התחלה חדשה</span></h3>
        <p>זמן מצטבר במסע: <span id="timeline">0 חודשים</span> | עלות מצטברת: <span id="cost">0 ש"ח</span></p>
    </div>

    <div id="stage-idea" class="stage">
        <h2>שלב 1: ניצוץ של גאונות - הרעיון הראשוני ✨</h2>
        <p>כל מסע מתחיל ברעיון. חשבו על ההמצאה שלכם - מה היא פותרת? למה היא חדשנית? תנו לנו תיאור קצר ומלהיב שיעזור לנו להתחיל את התהליך:</p>
        <textarea id="idea-description" rows="5" placeholder="תארו כאן את ההמצאה שלכם... כמה שיותר ברור ומפורט, כך ייטב!"></textarea><br>
        <button onclick="startSearch()">צאו לדרך: בצעו חיפוש חדשנות מקדים!</button>
    </div>

    <div id="stage-search" class="stage" style="display: none;">
        <h2>שלב 2: מחט בערימת שחת - חיפוש חדשנות מקדים 🕵️‍♀️</h2>
        <p>האם הרעיון שלכם באמת חדש? זה השלב הקריטי לבדיקה. אנחנו צוללים לתוך מאגרי פטנטים ופרסומים עולמיים כדי לוודא שהמצאה דומה לא קיימת כבר. תהליך זה עוזר לנו להבין את סיכויי ההמצאה לעבור את שלב הבחינה המאתגר.</p>
        <div id="search-process">
             <p id="search-status" class="process-text">...צוללים למאגרי המידע העולמיים, מחפשים אחר פטנטים ופרסומים רלוונטיים...</p>
             <div class="loading-dots"><span>.</span><span>.</span><span>.</span></div>
        </div>
        <div id="search-result" style="display: none;" class="result-message"></div>
        <button id="continue-drafting-btn" onclick="startDrafting()" style="display: none;">הממצאים בידינו! המשיכו לניסוח הבקשה המקצועי</button>
    </div>

    <div id="stage-drafting" class="stage" style="display: none;">
        <h2>שלב 3: אמנות המילים המגנות - ניסוח בקשת הפטנט ✍️</h2>
        <p>בקשת פטנט היא מסמך טכני ומשפטי מורכב ביותר. עלינו לנסח אותה בקפידה, לכלול תיאורים מפורטים, שרטוטים מדויקים, ובעיקר - "תביעות" שיגדירו בדיוק מה אתם ממציאים ועל מה אתם מבקשים הגנה. ניסוח טוב הוא המפתח להגנה רחבה ויעילה.</p>
        <div id="drafting-process">
            <p class="process-text">...צוות עורכי הפטנטים שלכם עובד במרץ על ניסוח מדויק ומקיף של בקשת הפטנט, כולל התביעות הקריטיות...</p>
             <div class="loading-dots"><span>.</span><span>.</span><span>.</span></div>
        </div>
        <button onclick="startFiling()">הבקשה מוכנה! הגישו אותה רשמית לרשות הפטנטים</button>
    </div>

    <div id="stage-filing" class="stage" style="display: none;">
        <h2>שלב 4: רגע האמת - הגשת הבקשה הרשמית ✉️</h2>
        <p>הבקשה סוף סוף הוגשה לרשות הפטנטים! תאריך ההגשה הזה קובע את "זכות הקדימה" שלכם - מהיום, העולם לא יכול לטעון שהמצאה דומה כבר קיימת אם לא הייתה ידועה לפני רגע זה. עכשיו מתחיל תהליך הבחינה הרשמי.</p>
        <button onclick="startExamination()">הבקשה על שולחן הבוחן: המשיכו לשלב הבחינה!</button>
    </div>

    <div id="stage-examination" class="stage" style="display: none;">
        <h2>שלב 5: מבחן המציאות - בחינת הפטנט ע'י הבוחן 🧐</h2>
        <p>בקשת הפטנט שלכם נמצאת עכשיו אצל בוחן פטנטים מומחה מטעם הרשות. הבוחן יבצע בחינה מעמיקה וישווה את ההמצאה לידע הקיים בעולם (Prior Art). הוא יבדוק האם היא עומדת בדרישות החוק: חדשנות מוחלטת, התקדמות המצאתית (היא לא מובנת מאליה) וישימות תעשייתית. שלב זה הוא לרוב הארוך והמאתגר ביותר.</p>
        <div id="examination-process">
             <p id="examination-status" class="process-text">...בוחן הפטנטים צולל לפרטי בקשתכם, עורך חיפושים נוספים, ומגבש את החלטתו הראשונית...</p>
              <div class="loading-dots"><span>.</span><span>.</span><span>.</span></div>
        </div>
        <div id="office-action" style="display: none;" class="result-message"></div>
        <button id="respond-action-btn" onclick="startResponse()" style="display: none;">הגיעה הודעה מהבוחן! עליכם להגיב!</button>
         <button id="continue-to-outcome-btn" onclick="finalizeOutcome()" style="display: none;">אין התנגדויות? המשיכו להחלטה הסופית!</button>

    </div>

    <div id="stage-response" class="stage" style="display: none;">
        <h2>שלב 6: דו-שיח עם הרשות - תגובה להודעת הבוחן ⚖️</h2>
        <p>קיבלתם "הודעה מהמשרד" (Office Action) - הבוחן העלה שאלות, התנגדויות או בקשות לתיקונים. זה נורמלי ולרוב דורש תגובה מקצועית ומנומקת. עליכם לשכנע את הבוחן שההמצאה שלכם אכן כשירה לפטנט, לעיתים באמצעות תיקונים או הבהרות לבקשה.</p>
        <div id="response-process">
            <p class="process-text">...מנסחים תגובה מפורטת ומנומקת לבוחן, אולי בצירוף תיקונים נדרשים...</p>
             <div class="loading-dots"><span>.</span><span>.</span><span>.</span></div>
        </div>
        <button onclick="finalizeOutcome()">שלחו את התגובה והמתינו להחלטה הסופית!</button>
    </div>

    <div id="stage-outcome" class="stage" style="display: none;">
        <h2>שלב 7: סוף המסע - ההחלטה הסופית 🏆/❌</h2>
        <p>הגיע רגע האמת! לאחר כל השלבים, הבחינה, והתקשורת עם הרשות, הבוחן גיבש החלטה סופית לגבי בקשת הפטנט שלכם.</p>
        <div id="final-outcome-message" class="result-message">
             <p id="final-outcome-text"></p>
        </div>

        <button onclick="resetSimulation()">התחילו סימולציה חדשה עם רעיון אחר!</button>
    </div>
</div>

<button id="explanation-toggle-btn" aria-expanded="false">הצג מידע נוסף והסבר מפורט 📚</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: עולם הפטנטים</h2>

    <h3>מהו פטנט ומדוע הוא חיוני?</h3>
    <p>פטנט הוא לא סתם תעודה; זו זכות חוקית בלעדית שמעניקה לממציא הגנה מפני שימוש בלתי מורשה בהמצאתו לתקופה מוגבלת (בדרך כלל 20 שנה). ההגנה הזו חיונית כדי לעודד חדשנות, לאפשר לממציאים להחזיר את ההשקעה האדירה בפיתוח, ולהוות תמריץ לשיתוף ידע טכנולוגי במקום להסתיר אותו כסוד מסחרי.</p>

    <h3>התנאים המרכזיים לקבלת פטנט (וכפי שהם מיוצגים בסימולטור):</h3>
    <ul>
        <li>**חדשנות מוחלטת (Novelty):** הרעיון או ההמצאה לא היו ידועים לציבור בשום מקום בעולם לפני שהגשתם את הבקשה. <strong>(מיוצג בשלב החיפוש המקדים ובבחינה)</strong></li>
        <li>**התקדמות המצאתית (Inventive Step / Non-Obviousness):** ההמצאה אינה "מובנת מאליה" לאדם מומחה בתחום, בהתחשב בכל הידע הקיים. היא צריכה לכלול אלמנט של יצירתיות או פתרון בלתי צפוי. <strong>(מיוצג בעיקר בשלב הבחינה ובתגובה להתנגדויות)</strong></li>
        <li>**יישום תעשייתי (Industrial Applicability):** ההמצאה צריכה להיות פרקטית וניתנת לייצור או שימוש מעשי. <strong>(נבדק כחלק מהבחינה)</strong></li>
    </ul>

    <h3>פירוט השלבים בסימולטור והמקבילה במציאות:</h3>
    <ul>
        <li>**שלב 1 (הרעיון):** שלב הרעיון והפיתוח הראשוני של ההמצאה.</li>
        <li>**שלב 2 (חיפוש מקדים):** בדיקה וולונטרית (אך מומלצת ביותר!) של מאגרי פטנטים קיימים. כלי חיוני להערכת סיכויי הבקשה.</li>
        <li>**שלב 3 (ניסוח הבקשה):** מלאכת הניסוח המקצועי של מסמכי הבקשה, הכוללים תיאור, סרטוטים ותביעות. זהו אחד השלבים המורכבים והקריטיים ביותר, הדורש מומחיות טכנית ומשפטית (כאן נכנס לתמונה עורך פטנטים).</li>
        <li>**שלב 4 (הגשה):** הגשת המסמכים באופן רשמי לרשות הפטנטים במדינה/ות הרלוונטית. תאריך זה הוא "תאריך הבקשה".</li>
        <li>**שלב 5 (בחינה):** רשות הפטנטים ממנה בוחן לבדיקת עמידת הבקשה בדרישות החוק (חדשנות, התקדמות, יישום). שלב זה יכול לארוך שנים.</li>
        <li>**שלב 6 (תגובה לבוחן):** מענה רשמי להתנגדויות, שאלות או בקשות לתיקונים מצד הבוחן. זהו "דו-שיח" כתוב שמטרתו לשכנע את הבוחן. לעיתים יש צורך במספר סבבי תגובה.</li>
        <li>**שלב 7 (החלטה סופית):** קבלת פטנט (Allowance) או דחיית הבקשה (Rejection). במקרה של קבלה, יש לרוב צורך בתשלום אגרת הנפקה.</li>
    </ul>

     <h3>לא לשכוח את העלויות והזמן:</h3>
     <p>כפי שראיתם בסימולטור, תהליך רישום פטנט הוא ארוך ויקר. הוא כולל אגרות לרשות הפטנטים (משתנות לפי שלב וסוג הבקשה) ובעיקר שכר טרחה לעורך פטנטים, שבלעדיו קשה ביותר לצלוח את התהליך בהצלחה. משך התהליך יכול לנוע בין שנתיים לכמה שנים טובות, תלוי במדינה, מורכבות ההמצאה, ועומס העבודה ברשות.</p>

     <h3>למה ליווי מקצועי קריטי?</h3>
     <p>ניסוח שגוי של התביעות, מענה לא מדויק לבוחן, או אי-הבנה של הפרוצדורות עלולים להכשיל את הבקשה לחלוטין, או לגרום לקבלת פטנט עם הגנה צרה וחסרת ערך. עורך פטנטים מוסמך הוא המומחה שיודע לנווט במבוך החוקים והתקנות, לנסח את הבקשה בצורה אופטימלית, ולהתמודד מול רשויות הפטנטים בעולם, ולכן ליוויו הוא השקעה חיונית.</p>
</div>

<style>
    :root {
        --primary-color: #0056b3;
        --secondary-color: #007bff;
        --accent-color: #28a745;
        --danger-color: #dc3545;
        --warning-color: #ffc107;
        --background-color: #f8f9fa;
        --card-background: #ffffff;
        --text-color: #343a40;
        --border-color: #e9ecef;
        --shadow-color: rgba(0, 0, 0, 0.08);
        --animation-duration: 0.3s;
    }

    body {
        font-family: 'Arial', sans-serif; /* Adjusted to a common sans-serif */
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background-color: var(--background-color);
        color: var(--text-color);
        direction: rtl; /* Ensure Right-to-Left */
        text-align: right; /* Ensure Right-to-Left */
    }

    h1, h2, h3 {
        color: var(--primary-color);
        margin-bottom: 15px;
        line-height: 1.4;
    }

     h1 {
        text-align: center;
        color: var(--secondary-color);
        margin-bottom: 25px;
     }

    #app, #explanation {
        background-color: var(--card-background);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 15px var(--shadow-color);
        max-width: 800px;
        margin: 20px auto;
        transition: all var(--animation-duration) ease-in-out;
    }

     #explanation {
         margin-top: 30px;
         border-top: 3px dashed var(--border-color);
     }
     #explanation h2 {
         text-align: center;
         margin-bottom: 20px;
     }
      #explanation h3 {
          color: var(--secondary-color);
          margin-top: 25px;
          margin-bottom: 10px;
      }
     #explanation ul {
         list-style: disc inside;
         padding-left: 0;
     }
     #explanation li {
         margin-bottom: 8px;
     }


    #progress-bar {
        width: 100%;
        height: 8px;
        background-color: var(--border-color);
        border-radius: 4px;
        margin-bottom: 20px;
        overflow: hidden;
    }

    #progress-fill {
        height: 100%;
        width: 0%; /* Will be updated by JS */
        background-color: var(--accent-color);
        border-radius: 4px;
        transition: width 0.6s ease-in-out;
    }


    #current-status {
        background-color: var(--border-color);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 30px;
        border: 1px solid #dee2e6;
    }
    #current-status h3 {
        margin: 0 0 10px 0;
        color: var(--text-color);
        font-size: 1.2rem;
    }
     #current-status p {
         margin: 0;
         font-size: 1rem;
         color: #555;
     }
      #status-emoji {
          margin-left: 8px;
          font-size: 1.4rem;
          vertical-align: middle;
      }
     #timeline, #cost {
         font-weight: bold;
         color: var(--secondary-color);
     }
      /* Animation for status numbers */
     @keyframes countup {
         from { opacity: 0.5; }
         to { opacity: 1; }
     }
      #timeline span, #cost span {
          animation: countup 0.5s ease-out;
      }


    .stage {
        border-top: 1px solid #eee;
        padding-top: 30px;
        margin-top: 30px;
        opacity: 0; /* Start hidden */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity var(--animation-duration) ease-out, transform var(--animation-duration) ease-out;
    }
     .stage.active {
        opacity: 1;
        transform: translateY(0);
     }

    .stage h2 {
        color: var(--primary-color);
         font-size: 1.8rem;
         margin-bottom: 10px;
    }
     .stage p {
         margin-bottom: 20px;
         color: #555;
     }

    textarea {
        width: calc(100% - 24px); /* Adjust for padding and border */
        padding: 12px;
        margin-bottom: 20px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 1rem;
        box-sizing: border-box; /* Include padding in width */
        resize: vertical; /* Allow vertical resize only */
        min-height: 120px;
        transition: border-color var(--animation-duration) ease-in-out;
    }
     textarea:focus {
         border-color: var(--secondary-color);
         outline: none;
     }

    button {
        display: inline-block;
        background-color: var(--secondary-color);
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1rem;
        margin-left: 10px; /* Adjusted from margin-right for RTL */
        transition: background-color var(--animation-duration) ease-in-out, transform 0.1s ease-in-out;
        font-weight: bold;
    }
     button:last-child {
        margin-left: 0; /* Adjusted for RTL */
     }

    button:hover {
        background-color: var(--primary-color);
    }
    button:active {
        transform: scale(0.98);
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        transform: none;
    }

    #explanation-toggle-btn {
        display: block; /* Make it a block element */
        margin: 20px auto; /* Center the button */
        background-color: var(--primary-color); /* Different color */
        font-weight: normal;
    }
    #explanation-toggle-btn:hover {
        background-color: #003f80;
    }


    /* Simulation process indicators */
    .process-text {
        font-style: italic;
        color: #6c757d;
        margin-bottom: 10px;
    }

    .loading-dots {
        display: inline-block;
        color: #6c757d;
        font-size: 1.5rem;
        height: 1.5em; /* Reserve space */
    }

    .loading-dots span {
        animation: blink 1.4s infinite both;
    }

    .loading-dots span:nth-child(2) {
        animation-delay: 0.2s;
    }

    .loading-dots span:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes blink {
        0% { opacity: 0.2; }
        20% { opacity: 1; }
        100% { opacity: 0.2; }
    }

     /* Result Messages */
    .result-message {
        padding: 15px;
        margin-top: 15px;
        border-radius: 6px;
        font-weight: bold;
        line-height: 1.5;
        transition: opacity var(--animation-duration) ease-in-out;
    }

    .result-message p { /* Style paragraphs inside result messages */
        margin: 0;
         color: inherit; /* Inherit text color from parent div */
    }

    /* Specific result message styles */
    #search-result.positive, #office-action.positive, #final-outcome-message.positive {
        background-color: #d4edda;
        color: var(--accent-color);
        border: 1px solid #c3e6cb;
    }

    #search-result.negative, #office-action.negative, #final-outcome-message.negative {
        background-color: #f8d7da;
        color: var(--danger-color);
        border: 1px solid #f5c6cb;
    }

     #office-action.warning {
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeeba;
     }

     /* Emojis for result messages */
    .result-message::before {
         margin-left: 10px;
         font-size: 1.3em;
         vertical-align: middle;
    }
    #search-result.positive::before { content: '🟢'; }
    #search-result.negative::before { content: '🔴'; }
    #office-action.positive::before { content: '✅'; } /* Should not happen for office action, but good to have */
    #office-action.negative::before { content: '❌'; }
     #office-action.warning::before { content: '⚠️'; }
    #final-outcome-message.positive::before { content: '🎉'; }
    #final-outcome-message.negative::before { content: '💔'; }


     /* Basic responsiveness */
    @media (max-width: 600px) {
        #app, #explanation {
            padding: 20px;
        }
         button {
             width: 100%;
             margin-left: 0;
             margin-top: 10px;
         }
         button:first-of-type {
             margin-top: 0;
         }
          #explanation-toggle-btn {
              width: auto; /* Auto width for centering */
          }
    }


</style>

<script>
    let currentStage = 'idea';
    let totalStages = 7; // Total number of distinct stages in the simulation
    let currentTime = 0; // in months
    let currentCost = 0; // in NIS

    // Simulation variables to influence outcomes based on prior steps
    let searchOutcome = 'unknown'; // 'novel', 'similar', 'very-similar'
    let officeActionType = 'none'; // 'none', 'inventiveStep', 'clarification', 'multiple'


    const stageElements = {
        idea: document.getElementById('stage-idea'),
        search: document.getElementById('stage-search'),
        drafting: document.getElementById('stage-drafting'),
        filing: document.getElementById('stage-filing'),
        examination: document.getElementById('stage-examination'),
        response: document.getElementById('stage-response'),
        outcome: document.getElementById('stage-outcome')
    };

    const statusText = document.getElementById('status-text');
    const statusEmoji = document.getElementById('status-emoji');
    const timelineText = document.getElementById('timeline');
    const costText = document.getElementById('cost');
    const progressBarFill = document.getElementById('progress-fill');

    const ideaDescriptionTextarea = document.getElementById('idea-description');

    const searchProcessDiv = document.getElementById('search-process');
    const searchStatusText = document.getElementById('search-status');
    const searchResultDiv = document.getElementById('search-result');
    const continueDraftingBtn = document.getElementById('continue-drafting-btn');

    const draftingProcessDiv = document.getElementById('drafting-process');

    const examinationProcessDiv = document.getElementById('examination-process');
    const examinationStatusText = document.getElementById('examination-status');
    const officeActionDiv = document.getElementById('office-action');
    const respondActionBtn = document.getElementById('respond-action-btn');
    const continueToOutcomeBtn = document.getElementById('continue-to-outcome-btn');

    const responseProcessDiv = document.getElementById('response-process');

    const finalOutcomeText = document.getElementById('final-outcome-text');
     const finalOutcomeMessageDiv = document.getElementById('final-outcome-message');


    const explanationDiv = document.getElementById('explanation');
    const explanationToggleBtn = document.getElementById('explanation-toggle-btn');

     // Helper to get stage index for progress bar
     const stageIndex = {
        idea: 1,
        search: 2,
        drafting: 3,
        filing: 4,
        examination: 5,
        response: 6,
        outcome: 7 // Outcome stage might be considered the final step visually
     };


    function updateUI() {
        // Hide all stages and remove active class
        Object.values(stageElements).forEach(el => {
             el.style.display = 'none';
             el.classList.remove('active');
        });

        // Show current stage and add active class
        const activeStageElement = stageElements[currentStage];
        if (activeStageElement) {
            activeStageElement.style.display = 'block';
            // Use a small delay before adding 'active' class to allow display:block to register for transition
            setTimeout(() => {
                activeStageElement.classList.add('active');
            }, 10);
        }


        // Update status bar
        const statusMap = {
            idea: { text: 'רעיון ראשוני', emoji: '✨' },
            search: { text: 'חיפוש חדשנות', emoji: '🕵️‍♀️' },
            drafting: { text: 'ניסוח בקשה', emoji: '✍️' },
            filing: { text: 'הגשת בקשה רשמית', emoji: '✉️' },
            examination: { text: 'בחינת פטנט ע"י הבוחן', emoji: '🧐' },
            response: { text: 'תגובה להודעת הבוחן', emoji: '⚖️' },
            outcome: { text: 'החלטה סופית', emoji: '🏆' } // Emoji updated based on outcome later
        };

        statusText.textContent = statusMap[currentStage].text;
        statusEmoji.textContent = statusMap[currentStage].emoji;


        // Update progress bar
        const currentStageIndex = stageIndex[currentStage] || 1;
        // Calculate progress excluding the final outcome stage as an intermediate step
        const progress = (currentStageIndex / (totalStages)) * 100;
        progressBarFill.style.width = `${progress}%`;


        // Update status display immediately
         updateStatus();
    }

     function updateStatus() {
         // Trigger reflow to restart animation
         timelineText.classList.remove('count-up');
         costText.classList.remove('count-up');
         void timelineText.offsetWidth; // Trigger reflow
         void costText.offsetWidth; // Trigger reflow
         timelineText.classList.add('count-up');
         costText.classList.add('count-up');


         timelineText.textContent = `${currentTime} חודשים`;
         costText.textContent = `${currentCost.toLocaleString()} ש"ח`;
     }


     function showProcessing(element) {
         element.style.display = 'block';
     }

     function hideProcessing(element) {
         element.style.display = 'none';
     }

     function showResult(element, type, message) {
         element.className = 'result-message'; // Reset classes
         element.classList.add(type);
         element.innerHTML = `<p>${message}</p>`; // Use innerHTML to allow for emojis/tags
         element.style.display = 'block';
         // Add a slight delay before making it fully visible if needed for transition
         setTimeout(() => element.style.opacity = '1', 10);
     }


    function simulateDelay(ms, onProcessingStart = () => {}, onProcessingEnd = () => {}) {
        onProcessingStart();
        return new Promise(resolve => setTimeout(() => {
            onProcessingEnd();
            resolve();
        }, ms));
    }

    function startSearch() {
        currentStage = 'search';
        updateUI();

        hideResult(searchResultDiv);
        continueDraftingBtn.style.display = 'none';
         showProcessing(searchProcessDiv);

        // Simulate search time and cost (approximate ranges)
        const searchTime = Math.floor(Math.random() * 2) + 1; // 1-2 months
        const searchCost = Math.floor(Math.random() * 2000) + 1000; // 1000-3000 ש"ח
        currentTime += searchTime;
        currentCost += searchCost;

        // Simulate search outcome
        // Influence outcome slightly by description length (heuristic)
        const descriptionLength = ideaDescriptionTextarea.value.trim().length;
        let noveltyChance = 0.6; // Base chance of novel
        if (descriptionLength < 50) { // Short description -> harder to search effectively?
             noveltyChance -= 0.1;
        } else if (descriptionLength > 200) { // More detailed -> easier to find prior art?
             noveltyChance -= 0.1; // Can also increase chance of finding 'similar'
        }


        const random = Math.random();
        if (random < noveltyChance) {
            searchOutcome = 'novel';
        } else if (random < noveltyChance + 0.3) { // 30% chance of similar
            searchOutcome = 'similar';
        } else { // 10% chance of very similar
             searchOutcome = 'very-similar';
        }


        simulateDelay(2500,
             () => {}, // No specific start processing visual beyond the block itself
             () => { hideProcessing(searchProcessDiv); }
        ).then(() => {
            let message = "";
            let type = "";
            if (searchOutcome === 'novel') {
                message = 'תוצאות החיפוש מבטיחות! נראה שהרעיון שלכם חדשני באופן יחסי ביחס לידע הקיים. סיכוי טוב לעבור את דרישת החדשנות!';
                type = 'positive';
            } else if (searchOutcome === 'similar') {
                message = 'שימו לב: נמצאו מספר פטנטים/פרסומים דומים. ייתכן שיהיה צורך להתאים או לצמצם את היקף ההגנה המבוקש כדי לעבור את שלב הבחינה הרשמי.';
                type = 'warning';
            } else { // very-similar
                 message = 'אזהרה חמורה: נמצאו פטנטים דומים מאוד להמצאה שלכם. ייתכן שהרעיון אינו חדש מספיק לקבלת פטנט. כדאי לשקול שינויים משמעותיים או להעריך מחדש את הכדאיות.';
                 type = 'negative';
            }
            showResult(searchResultDiv, type, message);
            continueDraftingBtn.style.display = 'block';
             updateStatus(); // Update status bar after step completion
        });
    }

    function startDrafting() {
        currentStage = 'drafting';
        updateUI();

        hideProcessing(draftingProcessDiv); // Ensure it's hidden initially if coming back
         showProcessing(draftingProcessDiv);

        // Simulate drafting time and cost (significant cost for professional work)
        const draftingTime = Math.floor(Math.random() * 4) + 1; // 1-4 months
        const draftingCost = Math.floor(Math.random() * 10000) + 10000; // 10000-20000 ש"ח
        currentTime += draftingTime;
        currentCost += draftingCost;

        simulateDelay(2000,
            () => {},
            () => { hideProcessing(draftingProcessDiv); }
        ).then(() => {
             updateStatus();
        });
    }

    function startFiling() {
        currentStage = 'filing';
        updateUI();

        // Simulate filing cost (government fee)
        const filingCost = Math.floor(Math.random() * 500) + 1000; // 1000-1500 ש"ח (initial fee)
        currentCost += filingCost;

        // Simulate a very short administrative delay
        simulateDelay(1000).then(() => {
             updateStatus();
        });
    }

    function startExamination() {
        currentStage = 'examination';
        updateUI();
        hideProcessing(examinationProcessDiv); // Ensure hidden
         showProcessing(examinationProcessDiv);

        officeActionDiv.style.display = 'none'; // Hide previous office action
        respondActionBtn.style.display = 'none';
         continueToOutcomeBtn.style.display = 'none';


        // Simulate examination time and cost (main examination fee)
        const examinationTime = Math.floor(Math.random() * 36) + 12; // 12-48 months (1-4 years)
        const examinationCost = Math.floor(Math.random() * 2000) + 3000; // 3000-5000 ש"ח (examination fee)
        currentTime += examinationTime;
        currentCost += examinationCost;

        // Simulate office action based on previous search outcome
        let objectionChance = 0.8; // Base chance of getting an objection
        if (searchOutcome === 'novel') {
            objectionChance -= 0.2; // Lower chance if search was very positive
        } else if (searchOutcome === 'very-similar') {
            objectionChance += 0.1; // Higher chance if search was negative
        }

        const hasOfficeAction = Math.random() < objectionChance;


        simulateDelay(examinationTime * 100 + 2000, // Simulate longer delay corresponding to time
             () => { examinationStatusText.textContent = `...בקשת הפטנט נבחנת ביסודיות על ידי הבוחן (${examinationTime} חודשים סימולציה)...`; },
            () => { hideProcessing(examinationProcessDiv); examinationStatusText.textContent = 'תוצאות הבחינה הראשונית:'; }
        ).then(() => {
            if (hasOfficeAction) {
                 const randomAction = Math.random();
                 if (randomAction < 0.5) {
                    officeActionType = 'inventiveStep'; // 50% inventive step
                    showResult(officeActionDiv, 'negative', '🔴 התנגדות מהבוחן: חוסר התקדמות המצאתית! הבוחן טוען שהמצאתכם מובנת מאליה לאור הידע הקיים. זהו אתגר משפטי וטכני משמעותי.');
                } else if (randomAction < 0.8) {
                    officeActionType = 'clarification'; // 30% clarification
                    showResult(officeActionDiv, 'warning', '⚠️ בקשה להבהרות/תיקונים: הבוחן מבקש הבהרות ניסוח או תיקונים קלים לבקשה. זהו שלב שגרתי יחסית.');
                } else {
                     officeActionType = 'multiple'; // 20% multiple issues
                     showResult(officeActionDiv, 'negative', '🔴 התנגדויות מרובות מהבוחן! שילוב של חוסר התקדמות המצאתית ובעיות ניסוח/תיאור. תגובה מורכבת נדרשת.');
                }
                respondActionBtn.style.display = 'block';
            } else {
                 officeActionType = 'none';
                 showResult(officeActionDiv, 'positive', '🟢 הבחינה הראשונית הסתיימה ללא התנגדויות מהותיות! זהו סימן מצוין. כנראה שהבקשה בדרך לאישור.');
                 continueToOutcomeBtn.style.display = 'block'; // Skip response stage if no objection
            }
            updateStatus();
        });
    }

    function startResponse() {
         currentStage = 'response';
         updateUI();

         hideProcessing(responseProcessDiv); // Ensure hidden
         showProcessing(responseProcessDiv);

         // Simulate response time and cost
         const responseTime = Math.floor(Math.random() * 3) + 1; // 1-3 months
         const responseCost = Math.floor(Math.random() * 7000) + 4000; // 4000-11000 ש"ח (cost depends on complexity of objection)
         currentTime += responseTime;
         currentCost += responseCost;

         simulateDelay(2000,
             () => {},
            () => { hideProcessing(responseProcessDiv); }
         ).then(() => {
              updateStatus();
         });
    }

    function finalizeOutcome() {
        currentStage = 'outcome';
        updateUI();

        hideResult(finalOutcomeMessageDiv); // Hide previous result if any
         // Show processing if outcome calculation takes a moment (optional, can be instant)
         // simulateDelay(500).then(() => { ... }); // Example delay


        // Simulate final outcome based on previous steps and randomness
        let successChance = 0.7; // Base chance of approval if reached this stage

        // Adjust chance based on search outcome
        if (searchOutcome === 'similar') {
            successChance -= 0.1;
        } else if (searchOutcome === 'very-similar') {
            successChance -= 0.3; // Much harder if search was bad
        }

        // Adjust chance based on office action type
        if (officeActionType === 'inventiveStep') {
            successChance -= 0.2; // Inventive step objections are hard
        } else if (officeActionType === 'multiple') {
             successChance -= 0.3; // Multiple objections are very hard
        } else if (officeActionType === 'clarification') {
             successChance += 0.1; // Clarifications are usually overcome
        } else if (officeActionType === 'none') {
             successChance += 0.15; // If no objection, high chance of approval
        }


        // Ensure chance is within 0-1 range
        successChance = Math.max(0.1, Math.min(0.9, successChance)); // Don't make it impossible or guaranteed


        const random = Math.random();
        let message = "";
        let type = "";
        let finalTimeCost = 0; // Final small administrative costs

        if (random < successChance) {
            // APPROVED
            message = `🎉 מזל טוב! בקשת הפטנט שלכם אושרה בהצלחה! ההמצאה שלכם מוגנת כעת.`;
            type = 'positive';
            statusEmoji.textContent = '🏆'; // Update emoji for success
            finalTimeCost = Math.floor(Math.random() * 500) + 1000; // Final issue fee and admin
             currentTime += Math.floor(Math.random() * 2) + 1; // 1-2 months final admin
        } else {
            // REJECTED
             let rejectionReason = "";
             if (officeActionType === 'inventiveStep' || officeActionType === 'multiple') {
                 rejectionReason = "הבקשה נדחתה סופית עקב חוסר התקדמות המצאתית (Obviousness).";
             } else if (searchOutcome === 'very-similar') {
                 rejectionReason = "הבקשה נדחתה סופית עקב חוסר חדשנות (Lack of Novelty) לאור ידע קודם שנמצא.";
             } else if (officeActionType === 'clarification') {
                  rejectionReason = "הבקשה נדחתה. הבהרות/תיקונים שנדרשו לא היו מספקים.";
             }
            else {
                 rejectionReason = "הבקשה נדחתה סופית מסיבה הקשורה לדרישות החוק. לעיתים ניתן לערער.";
            }

            message = `💔 הבקשה לפטנט נדחתה. ${rejectionReason}`;
            type = 'negative';
            statusEmoji.textContent = '❌'; // Update emoji for rejection
             currentTime += Math.floor(Math.random() * 2) + 1; // 1-2 months for final notice
        }

        showResult(finalOutcomeMessageDiv, type, message);

        currentCost += finalTimeCost; // Add final costs if any
         updateStatus();

         // Reset simulation variables for next round
         searchOutcome = 'unknown';
         officeActionType = 'none';

    }

    function resetSimulation() {
        currentStage = 'idea';
        currentTime = 0;
        currentCost = 0;

        // Reset variables
         searchOutcome = 'unknown';
         officeActionType = 'none';

        // Reset UI elements
        ideaDescriptionTextarea.value = '';
        hideResult(searchResultDiv);
         hideProcessing(searchProcessDiv);
         hideProcessing(draftingProcessDiv);
         hideProcessing(examinationProcessDiv);
         hideProcessing(responseProcessDiv);
        officeActionDiv.style.display = 'none';
        continueDraftingBtn.style.display = 'none';
        respondActionBtn.style.display = 'none';
        continueToOutcomeBtn.style.display = 'none';
         hideResult(finalOutcomeMessageDiv);


        updateUI(); // This will show the first stage and update status
         progressBarFill.style.width = '0%'; // Reset progress bar
         explanationDiv.style.display = 'none'; // Hide explanation
         explanationToggleBtn.textContent = 'הצג מידע נוסף והסבר מפורט 📚';
         explanationToggleBtn.setAttribute('aria-expanded', 'false');

    }

    // Initial UI setup
    resetSimulation(); // Use reset to set initial state

    // Explanation toggle
    explanationToggleBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggleBtn.textContent = isHidden ? 'הסתר מידע נוסף והסבר מפורט 📖' : 'הצג מידע נוסף והסבר מפורט 📚';
        explanationToggleBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
    });

     // Make stages respond to forward clicks where applicable
     // This adds a layer of interaction, clicking the stage title moves forward IF a button is visible
     Object.keys(stageElements).forEach(key => {
         const stageEl = stageElements[key];
         const heading = stageEl.querySelector('h2');
         if (heading) {
             heading.style.cursor = 'pointer';
             heading.addEventListener('click', () => {
                 // Only advance if the current visible stage matches this heading's stage key
                 // AND a button allowing advancement is currently displayed
                 if (currentStage === key) {
                      let canAdvance = false;
                      // Check for specific buttons that advance the stage
                      if (key === 'idea' && stageEl.querySelector('button[onclick="startSearch()"]:not(:disabled)')) canAdvance = true;
                      if (key === 'search' && stageEl.querySelector('button[onclick="startDrafting()"]:not(:disabled)')) canAdvance = true;
                      if (key === 'drafting' && stageEl.querySelector('button[onclick="startFiling()"]:not(:disabled)')) canAdvance = true;
                      if (key === 'filing' && stageEl.querySelector('button[onclick="startExamination()"]:not(:disabled)')) canAdvance = true;
                       // For examination, allow advancing if either response or outcome button is visible
                      if (key === 'examination') {
                           if (stageEl.querySelector('button[onclick="startResponse()"]:not(:disabled):not([style*="display: none"])')) canAdvance = true;
                           if (stageEl.querySelector('button[onclick="finalizeOutcome()"]:not(:disabled):not([style*="display: none"])')) canAdvance = true;
                      }
                      if (key === 'response' && stageEl.querySelector('button[onclick="finalizeOutcome()"]:not(:disabled)')) canAdvance = true;
                      if (key === 'outcome' && stageEl.querySelector('button[onclick="resetSimulation()"]:not(:disabled)')) canAdvance = true;


                      if (canAdvance) {
                          // Find the first visible, enabled button and trigger its click
                           const visibleButton = stageEl.querySelector('button:not(:disabled):not([style*="display: none"])');
                           if (visibleButton) {
                               visibleButton.click();
                           }
                      } else {
                           // Optional: Add feedback if clicking doesn't do anything
                           console.log(`Cannot advance from stage ${key} yet.`);
                           // Could add a temporary visual shake or message
                      }
                 }
             });
              // Add visual cue for clickable headings
             heading.style.textDecoration = 'underline dotted';
         }
     });


</script>
---