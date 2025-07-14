---
title: "מגן סייבר: קרב המוחות נגד איומים מתקדמים"
english_slug: cyber-guardian-advanced-defense-simulation
category: "סייבר ואבטחת מידע"
tags: [סייבר, אבטחת מידע, הגנת סייבר, ניהול סיכונים, סימולציה, משחק לימודי]
---
# מגן סייבר: קרב המוחות נגד איומים מתקדמים

הגורל הדיגיטלי של החברה בידיים שלך! בעולם שבו התקפות סייבר הופכות מתוחכמות מיום ליום, האם תצליח לנווט בסערת האיומים המתפתחים, לקבל את ההחלטות הנכונות תחת לחץ ולהקצות משאבים מוגבלים בצורה האפקטיבית ביותר? התמודד עם האתגר וצא לקרב המוחות במשחק ניהול סייבר דינמי.

<div id="game-container">
    <div id="game-stats" class="game-section">
        <h2><i class="icon shield"></i> סטטוס הגנה עדכני</h2>
        <div class="stats-grid">
            <p>סיבוב (חודש): <span id="round" class="stat-value">1</span></p>
            <p>תקציב חודשי זמין: $<span id="budget" class="stat-value colored">50000</span></p>
            <p>רמת סיכון כוללת: <span id="risk-level" class="stat-text colored">נמוך</span> (<span id="risk-value" class="stat-value">10</span>)</p>
            <p>רמת הגנה כוללת: <span id="defense-level" class="stat-text colored">בסיסית</span> (<span id="defense-value" class="stat-value">20</span>)</p>
            <p>נזק מצטבר: $<span id="damage" class="stat-value colored">0</span></p>
        </div>
         <div id="defense-breakdown">
            <h3>פירוט השקעות הגנה (אפקטיביות מצטברת)</h3>
             <p>טכנולוגיה: <span id="defense-tech" class="defense-level-value">0</span></p>
             <p>הכשרה: <span id="defense-training" class="defense-level-value">0</span></p>
             <p>עדכונים: <span id="defense-updates" class="defense-level-value">0</span></p>
             <p>גיבויים: <span id="defense-backup" class="defense-level-value">0</span></p>
             <p>תגובה לאירועים: <span id="defense-response" class="defense-level-value">0</span></p>
         </div>
    </div>

    <div id="game-controls" class="game-section">
        <h2><i class="icon budget"></i> הקצאת תקציב חודשי ($<span id="monthly-budget">50000</span>)</h2>
        <p class="control-description">הקצה את התקציב החודשי בין קטגוריות ההגנה השונות. השקעה נכונה תשפר את יכולת ההגנה שלך מול איומים.</p>
        <div class="budget-allocation-grid">
            <div class="budget-category">
                <label for="tech-budget"><i class="icon tech"></i> טכנולוגיות הגנה:</label>
                <input type="number" id="tech-budget" value="0" min="0" step="1000">
            </div>
            <div class="budget-category">
                <label for="training-budget"><i class="icon training"></i> הכשרת עובדים ומודעות:</label>
                <input type="number" id="training-budget" value="0" min="0" step="1000">
            </div>
            <div class="budget-category">
                <label for="updates-budget"><i class="icon updates"></i> עדכונים ותחזוקה שוטפת:</label>
                <input type="number" id="updates-budget" value="0" min="0" step="1000">
            </div>
             <div class="budget-category">
                <label for="backup-budget"><i class="icon backup"></i> גיבויים והתאוששות מאסון:</label>
                <input type="number" id="backup-budget" value="0" min="0" step="1000">
            </div>
            <div class="budget-category">
                <label for="response-budget"><i class="icon response"></i> מוכנות ותגובה לאירועים:</label>
                <input type="number" id="response-budget" value="0" min="0" step="1000">
            </div>
        </div>
        <button id="next-round-button"><i class="icon play"></i> סיום חודש והתמודדות עם איומים</button>
        <p id="budget-error" class="error-message"><i class="icon warning"></i> שגיאה בהקצאת תקציב: סך ההקצאה חורג מהתקציב החודשי.</p>
    </div>

    <div id="game-reports" class="game-section">
        <h2><i class="icon reports"></i> יומן אירועים ודיווחים</h2>
        <div id="reports-log">
            <p class="report-info"><i class="icon info"></i> [חודש 1] ברוכים הבאים לתפקיד מנהל אבטחת הסייבר. עליכם להגן על החברה מפני איומים מתקדמים. הקצו את התקציב החודשי בחוכמה ולחצו על "סיום חודש".</p>
        </div>
    </div>
    <div id="game-over-message" class="game-section" style="display: none;">
        <h2 id="game-over-title">הסימולציה הסתיימה!</h2>
        <p id="final-score"></p>
        <button onclick="location.reload()"><i class="icon restart"></i> התחלה מחדש</button>
    </div>
</div>

<style>
/* General Styles & Typography */
#game-container {
    font-family: 'Arial', sans-serif;
    max-width: 900px;
    margin: 30px auto;
    padding: 25px;
    border: 1px solid #ddd;
    border-radius: 12px;
    background-color: #f4f7f6;
    direction: rtl; /* Right-to-left for Hebrew */
    text-align: right;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    color: #333;
    line-height: 1.6;
}

.game-section {
    margin-bottom: 25px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
}

h2 {
    color: #2c3e50; /* Dark Blue-Grey */
    border-bottom: 3px solid #3498db; /* Bright Blue */
    padding-bottom: 8px;
    margin-top: 0;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    font-size: 1.6em;
}

h2 .icon {
    margin-left: 10px; /* Space after icon in RTL */
    font-size: 1.2em;
}

h3 {
    color: #555;
    margin-top: 15px;
    margin-bottom: 10px;
    font-size: 1.2em;
}

p {
    margin-bottom: 10px;
}

/* Icons (placeholders, could be replaced with actual icon font/SVG) */
.icon {
    display: inline-block;
    width: 1em;
    height: 1em;
    background-size: contain;
    background-repeat: no-repeat;
    vertical-align: middle;
    margin-left: 5px;
     /* Basic visual cues for placeholder icons */
     background-color: #3498db; /* Default icon color */
     border-radius: 3px;
}
.icon.shield { background-color: #27ae60; } /* Green */
.icon.budget { background-color: #f39c12; } /* Orange */
.icon.reports { background-color: #9b59b6; } /* Purple */
.icon.warning { background-color: #e74c3c; } /* Red */
.icon.play { background-color: #27ae60; } /* Green */
.icon.restart { background-color: #e74c3c; } /* Red */
.icon.info { background-color: #3498db; } /* Blue */

/* Specific Icons for Budget Categories (placeholders) */
.icon.tech { background-color: #3498db; } /* Blue */
.icon.training { background-color: #e67e22; } /* Dark Orange */
.icon.updates { background-color: #2ecc71; } /* Emerald Green */
.icon.backup { background-color: #f1c40f; } /* Yellow */
.icon.response { background-color: #c0392b; } /* Dark Red */


/* Stats Section */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
    margin-bottom: 20px;
}

#game-stats p {
    margin: 0;
    padding: 8px;
    background-color: #ecf0f1; /* Light grey */
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.stat-value {
    font-weight: bold;
    font-size: 1.1em;
     transition: color 0.3s ease, transform 0.3s ease; /* Animation for value changes */
}

.stat-value.highlight {
     transform: scale(1.1);
     color: #e74c3c; /* Pulse red */
}
.stat-value.colored#budget { color: green; }
.stat-value.colored#damage { color: red; }

#risk-level { transition: color 0.3s ease; }
#defense-level { transition: color 0.3s ease; }

#risk-level[data-level="נמוך"] { color: #2ecc71; } /* Green */
#risk-level[data-level="בינוני"] { color: #f39c12; } /* Orange */
#risk-level[data-level="גבוה"] { color: #e74c3c; } /* Red */

#defense-level[data-level="בסיסית"] { color: #e74c3c; } /* Red */
#defense-level[data-level="טובה"] { color: #f39c12; } /* Orange */
#defense-level[data-level="מתקדמת"] { color: #2ecc71; } /* Green */

#defense-breakdown {
    margin-top: 20px;
    padding-top: 15px;
    border-top: 1px dashed #ccc;
}
#defense-breakdown p {
    margin: 5px 0;
    padding: 0;
    background: none;
    justify-content: flex-start; /* Align items to the right in RTL */
}
#defense-breakdown span {
    font-weight: normal;
    margin-right: 5px;
    font-size: 1em;
    color: #555;
}


/* Controls Section */
.control-description {
    font-style: italic;
    color: #555;
    margin-bottom: 20px;
}

.budget-allocation-grid {
     display: grid;
     grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
     gap: 15px;
}

.budget-category {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ecf0f1; /* Light grey */
    padding: 10px;
    border-radius: 4px;
}

.budget-category label {
    flex-grow: 1;
    margin-left: 10px; /* Space between label and input */
    display: flex;
    align-items: center;
    font-weight: bold;
}

.budget-category input[type="number"] {
    width: 100px; /* Fixed width for input */
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    text-align: left; /* Numbers should be left-aligned */
    font-size: 1em;
}

button {
    display: block;
    width: 100%;
    padding: 12px;
    background-color: #2ecc71; /* Emerald Green */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    margin-top: 20px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}

button:hover {
    background-color: #27ae60; /* Darker Green */
}
button:active {
     transform: scale(0.98);
}
button:disabled {
    background-color: #bdc3c7; /* Grey */
    cursor: not-allowed;
}

button .icon {
    margin-left: 8px;
    font-size: 1em;
}


.error-message {
    color: #e74c3c; /* Red */
    font-weight: bold;
    margin-top: 10px;
    display: flex;
    align-items: center;
}
.error-message .icon {
    margin-left: 5px;
}


/* Reports Section */
#reports-log {
    max-height: 250px; /* Increased height */
    overflow-y: auto;
    border: 1px solid #e0e0e0;
    padding: 15px;
    background-color: #fefefe;
    border-radius: 4px;
    display: flex;
    flex-direction: column-reverse; /* Newest reports at the top */
    gap: 10px; /* Space between report entries */
}

#reports-log p {
    margin: 0;
    padding: 10px;
    border-bottom: 1px dashed #eee;
    line-height: 1.5;
    background-color: #fff;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: flex-start;
}

#reports-log p:first-child { /* Target the newest report */
    border-bottom: none;
}

#reports-log p .icon {
     margin-left: 8px;
     flex-shrink: 0; /* Prevent icon from shrinking */
     font-size: 1.1em;
     position: relative;
     top: 3px; /* Adjust vertical alignment */
}

/* Report specific styles */
.report-info { color: #3498db; } /* Blue */
.report-success { color: #27ae60; font-weight: bold; } /* Green */
.report-warning { color: #f39c12; font-weight: bold; } /* Orange */
.report-critical { color: #e74c3c; font-weight: bold; background-color: #fdeded; } /* Red with light red background */


/* Explanation Section */
#explanation-button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #3498db; /* Bright Blue */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 25px;
    font-weight: bold;
}

#explanation-button:hover {
     background-color: #2980b9; /* Darker Blue */
}

#explanation-content {
    margin-top: 25px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
}

#explanation-content h2 {
     border-bottom-color: #3498db; /* Match button color */
}

#explanation-content ul {
    list-style-type: disc;
    margin-right: 25px; /* Adjust for RTL */
    padding-right: 0;
}

#explanation-content li {
    margin-bottom: 10px;
    line-height: 1.6;
}

/* Game Over Message */
#game-over-message {
    text-align: center;
    padding: 30px;
    border: 3px solid #e74c3c; /* Red border */
    border-radius: 12px;
    background-color: #fff5f5; /* Light red background */
    margin-top: 30px;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

#game-over-title {
    color: #e74c3c; /* Red */
    border-bottom-color: #e74c3c;
    justify-content: center;
}

#final-score {
    font-size: 1.3em;
    margin-bottom: 20px;
    color: #333;
}

#game-over-message button {
    width: auto;
    margin-top: 15px;
    background-color: #e74c3c; /* Red */
    padding: 10px 20px; /* Smaller padding for inline button */
    display: inline-flex; /* Center button */
}
#game-over-message button:hover {
    background-color: #c0392b; /* Dark Red */
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .stats-grid {
        grid-template-columns: 1fr; /* Stack stats on small screens */
    }
    .budget-allocation-grid {
         grid-template-columns: 1fr; /* Stack budget categories */
    }
    .budget-category {
        flex-direction: column; /* Stack label and input */
        align-items: flex-end; /* Align to the right in RTL */
    }
    .budget-category label {
         margin-left: 0;
         margin-bottom: 5px;
    }
    .budget-category input[type="number"] {
        width: 100%; /* Full width input on small screens */
        text-align: right; /* Keep text right aligned */
    }
}

</style>

<button id="explanation-button">הצג הסבר תיאורטי על הגנת סייבר</button>

<div id="explanation-content" style="display: none;">
    <h2><i class="icon info"></i> הסבר תיאורטי: מאחורי הקלעים של הגנת הסייבר</h2>
    <p>הסימולציה ששיחקתם מדגימה היבטים מרכזיים בניהול הגנת סייבר בארגון. אלו הנושאים העיקריים שהיא נוגעת בהם:</p>
    <ul>
        <li><strong>אנטומיה של התקפת סייבר מתקדמת (Advanced Persistent Threat - APT):</strong> התקפות אלו אינן אקראיות או פשטניות. הן מתוכננות היטב, ממוקדות בארגון ספציפי, ונמשכות זמן רב (persistent) על מנת להשיג את יעדיהן בחשאי. התוקפים משתמשים בטקטיקות מגוונות כדי לחדור, להישאר בלתי מזוהים, לאסוף מידע רגיש או לבצע נזק אסטרטגי, לעיתים קרובות תוך התאמה להגנות שהם מגלים. הן עוקבות לעיתים קרובות אחר שרשרת הרג (Kill Chain) הכוללת שלבים כמו סיור, חימוש (פיתוח נוזקה מותאמת), מסירה (החדרת הנוזקה לארגון), ניצול (הפעלת הנוזקה), התקנה (התבססות), פקודה ושליטה (C2), וביצוע הפעולות על היעד.</li>
        <li><strong>ההבדל בין איומים רגילים לאיומים מתקדמים:</strong> בעוד שאיומים רגילים (כמו סריקות פורטים המוניות או וירוסים גנריים) מנצלים חולשות ידועות ופגיעות המונית, איומים מתקדמים (כמו אלו שמדמה הסימולציה) משתמשים לעיתים קרובות בשיטות מתוחכמות יותר, קשות לזיהוי, ובהתאמה אישית לארגון המטרה. הם עשויים לכלול שימוש ב-Zero-Days (ניצול חולשות אבטחה שאינן ידועות ליצרן או לציבור), Phishing ממוקד ביותר (Spear Phishing) נגד עובדים ספציפיים, או גרסאות חדישות של Ransomware שעוקפות הגנות סטנדרטיות. הם פחות "רעשניים" ויותר חמקמקים.</li>
        <li><strong>עקרונות מודלי הגנה קריטיים:</strong>
            <ul>
                <li><strong>Defense in Depth (הגנה לעומק):</strong> העיקרון המנחה הוא לבנות שכבות מרובות של הגנה, כך שאם שכבה אחת נכשלת, שכבה אחרת תוכל לעצור או לבלום את התוקף. מדובר באסטרטגיה רב-שכבתית שמכסה את כלל נכסי הארגון: הגנה ברמת הרשת, המערכת, האפליקציה, הנתונים ואף ברמה הפיזית והאנושית. הסימולציה מדגימה זאת דרך הצורך להשקיע בתחומים שונים ומשלימים (טכנולוגיה, הכשרה, גיבויים וכו').</li>
                <li><strong>Cyber Kill Chain:</strong> מודל שמפרק התקפת סייבר לשלבים לינאריים. הבנה של שלבים אלו מאפשרת לארגונים לזהות נקודות התערבות פוטנציאליות (Indicators of Compromise - IOCs) ולפתח הגנות ספציפיות לכל שלב כדי "לשבור את השרשרת" ולעצור את ההתקפה לפני שהיא מגיעה ליעדה הסופי.</li>
            </ul>
        </li>
         <li><strong>קטגוריות מרכזיות של אסטרטגיות הגנה (השקעות בסימולציה):</strong> הסימולציה מחלקת את ההגנה לקטגוריות שונות, המשקפות תחומים חשובים שדורשים השקעה תקציבית וניהולית:
            <ul>
                <li><strong>טכנולוגיות (חומות אש, IDS/IPS, EDR):</strong> כלים אוטומטיים המהווים את עמוד השדרה הטכני של ההגנה. הם מסייעים בחסימת תעבורה זדונית, זיהוי חדירות, ובקרה על נקודות קצה.</li>
                <li><strong>הכשרת עובדים (מודעות סייבר):</strong> הגורם האנושי הוא לעיתים קרובות החוליה החלשה בשרשרת האבטחה, אך גם קו ההגנה הראשון. הכשרה מתאימה יכולה למנוע התקפות רבות המבוססות על הנדסה חברתית (כמו פישינג).</li>
                <li><strong>עדכונים ותחזוקה (Patch Management):</strong> איומים רבים מנצלים חולשות אבטחה בתוכנות ומערכות מיושנות. תחזוקה שוטפת ועדכונים בזמן סוגרים פרצות אבטחה קריטיות.</li>
                <li><strong>גיבויים והתאוששות (Backup & Disaster Recovery):</strong> במקרה של מתקפות שגורמות לנזק או אובדן מידע (כמו Ransomware), גיבויים עדכניים ותוכנית התאוששות מאפשרים לחברה להתאושש במהירות ולמזער את הנזק הכספי והתפעולי.</li>
                <li><strong>מוכנות ותגובה לאירועים (Incident Response):</strong> גם עם ההגנות הטובות ביותר, חדירות עלולות להתרחש. היכולת לנטר, לזהות אירועי אבטחה בזמן אמת, להגיב עליהם במהירות וביעילות (לבודד מערכות, לחקור את האירוע, לשקם) היא קריטית לצמצום הנזק והחזרה לפעילות תקינה.</li>
            </ul>
            הגנה אפקטיבית דורשת שילוב והשקעה מתאימה בכל התחומים הללו, תוך התחשבות באופי האיומים.</li>
        <li><strong>אתגרי ניהול סיכוני סייבר ותעדוף משאבים מוגבלים:</strong> בארגונים אמיתיים, כמו בסימולציה, תקציבי אבטחת סייבר הם לרוב מוגבלים. על מנהל אבטחת המידע להעריך את הסיכונים השונים (מהם האיומים הסבירים ביותר נגד הארגון הספציפי? מהם הנכסים הדיגיטליים הקריטיים ביותר שדורשים את ההגנה הגבוהה ביותר?) ולהחליט היכן להשקיע את המשאבים המוגבלים בצורה שתניב את ההגנה המקסימלית לאור המצב. זהו תהליך מתמיד של ניהול סיכונים ותעדוף אסטרטגי.</li>
        <li><strong>הצורך בהתאמה מתמדת לנוף איומים משתנה:</strong> עולם הסייבר דינמי מאוד. תוקפים מפתחים כל הזמן שיטות חדשות ומתוחכמות יותר. הגנות שהיו אפקטיביות אתמול עשויות להיות מיושנות מחר. לכן, ניהול אבטחת סייבר הוא תהליך מתמשך הדורש ניטור שוטף של נוף האיומים, הערכה מחדש של הסיכונים, ועדכון מתמיד של אסטרטגיות ההגנה, הטכנולוגיות, התהליכים וההכשרות. יש ללמוד מכל אירוע ולהשתפר ללא הפסקה.</li>
    </ul>
    <p>דרך הסימולציה, התנסיתם בצורך לאזן בין השקעות שונות, להתמודד עם תוצאות ההחלטות שלכם תחת לחץ, ולהבין שהגנה אפקטיבית היא תמונה רחבה יותר מסתם התקנת אנטי-וירוס או חומת אש בודדת.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const budgetEl = document.getElementById('budget');
    const monthlyBudgetEl = document.getElementById('monthly-budget');
    const roundEl = document.getElementById('round');
    const riskValueEl = document.getElementById('risk-value');
    const riskLevelEl = document.getElementById('risk-level');
    const defenseValueEl = document.getElementById('defense-value');
    const defenseLevelEl = document.getElementById('defense-level');
    const damageEl = document.getElementById('damage');
    const reportsLogEl = document.getElementById('reports-log');
    const budgetErrorEl = document.getElementById('budget-error');
    const nextRoundButton = document.getElementById('next-round-button');
    const explanationButton = document.getElementById('explanation-button');
    const explanationContentEl = document.getElementById('explanation-content');
    const gameContainerEl = document.getElementById('game-container');
    const gameOverMessageEl = document.getElementById('game-over-message');
    const finalScoreEl = document.getElementById('final-score');
    const gameOverTitleEl = document.getElementById('game-over-title');

    const defenseBreakdownEls = {
        tech: document.getElementById('defense-tech'),
        training: document.getElementById('defense-training'),
        updates: document.getElementById('defense-updates'),
        backup: document.getElementById('defense-backup'),
        response: document.getElementById('defense-response')
    };


    const budgetInputs = {
        tech: document.getElementById('tech-budget'),
        training: document.getElementById('training-budget'),
        updates: document.getElementById('updates-budget'),
        backup: document.getElementById('backup-budget'),
        response: document.getElementById('response-budget')
    };

    // Game State
    let state = {
        round: 1,
        monthlyBudget: 75000, // Increased initial budget slightly for more flexibility
        currentBudget: 75000,
        totalSpending: 0,
        defenseLevels: { // Represents cumulative investment effectiveness (decays)
            tech: 0,
            training: 0,
            updates: 0,
            backup: 0,
            response: 0
        },
        risk: 15, // Starts slightly higher
        defense: 15, // Starts slightly lower
        damage: 0,
        gameOver: false,
        maxRounds: 18, // Simulation runs for 18 months/rounds
        maxDamage: 750000 // Game over if damage exceeds this
    };

    // Configuration
    const defenseEffectiveness = { // How much 1 unit of spending adds to defense level
        tech: 0.0006, // Increased tech effectiveness slightly
        training: 0.0012,
        updates: 0.0009,
        backup: 0.0005,
        response: 0.0008
    };
     const defenseDecayRate = 0.08; // Defense levels decay slightly each round

    // Attack definitions (tuned for difficulty and impact)
    const attackTypes = [
        { name: 'ניסיון פישינג', type: 'phishing', baseRiskImpact: 5, baseDefenseNegation: 10, potentialDamage: 30000, affectedDefenses: ['training', 'tech'], defenseEffect: { training: 0.7, tech: 0.3 }, messages: { success: 'משתמש לחץ על קישור זדוני! נזק קטן נגרם, רמת הסיכון האנושי עולה.', failure: 'העובדים זיהו את הפישינג ודיווחו! המערכות חסמו את הגישה.' } },
        { name: 'התקפת נוזקה גנרית', type: 'malware', baseRiskImpact: 10, baseDefenseNegation: 15, potentialDamage: 60000, affectedDefenses: ['tech', 'updates'], defenseEffect: { tech: 0.6, updates: 0.4 }, messages: { success: 'נוזקה חמקה מהגנות! קבצים הוצפנו בחלק מהמערכות.', failure: 'האנטי-וירוס זיהה את הנוזקה ונטרל אותה בזמן.' } },
        { name: 'ניצול חולשת אבטחה ידועה', type: 'exploit', baseRiskImpact: 15, baseDefenseNegation: 20, potentialDamage: 90000, affectedDefenses: ['updates', 'tech'], defenseEffect: { updates: 0.7, tech: 0.3 }, messages: { success: 'חולשה במערכת נוצלה! התוקפים השיגו גישה למערכות פנימיות.', failure: 'העדכונים האחרונים חסמו את ניסיון הניצול.' } },
        { name: 'התקפת כופר', type: 'ransomware', baseRiskImpact: 25, baseDefenseNegation: 30, potentialDamage: 250000, affectedDefenses: ['backup', 'tech', 'response'], defenseEffect: { backup: 0.4, tech: 0.3, response: 0.3 }, messages: { success: 'התקפת כופר הצליחה! מערכות קריטיות מוצפנות, נדרש תשלום (או שחזור מגיבוי).', failure: 'תוכנית התגובה פעלה במהירות! המתקפה נעצרה לפני גרימת נזק נרחב.' } },
        { name: 'APT: סיור והתבססות ראשונית', type: 'apt-recon', baseRiskImpact: 8, baseDefenseNegation: 12, potentialDamage: 15000, affectedDefenses: ['tech', 'training'], defenseEffect: { tech: 0.5, training: 0.5 }, hidden: true, messages: { success: 'גורמים זדוניים מבצעים סיור שקט ברשת. הם התבססו בנקודת קצה בודדת.', failure: 'ניסיונות סיור זוהו ונחסמו! המערכת נשארה בטוחה.' } },
        { name: 'APT: הרחבת גישה ותנועה רוחבית', type: 'apt-lateral', baseRiskImpact: 18, baseDefenseNegation: 25, potentialDamage: 80000, affectedDefenses: ['tech', 'response'], defenseEffect: { tech: 0.6, response: 0.4 }, messages: { success: 'התוקפים התקדמו בתוך הרשת! הם השיגו גישה למערכות נוספות.', failure: 'פעילות חשודה זוהתה על ידי ה-SOC! הגישה הוגבלה במהירות.' } },
        { name: 'APT: איסוף מידע וגניבה', type: 'apt-exfil', baseRiskImpact: 22, baseDefenseNegation: 35, potentialDamage: 150000, affectedDefenses: ['tech', 'response', 'training'], defenseEffect: { tech: 0.4, response: 0.4, training: 0.2 }, messages: { success: 'מידע רגיש נגנב מהארגון! הפרצת מידע משמעותית.', failure: 'ניסיון גניבת מידע סוכל! ההגנות מנעו את הוצאת הנתונים.' } },
         { name: 'DDoS ממוקד', type: 'ddos', baseRiskImpact: 12, baseDefenseNegation: 18, potentialDamage: 40000, affectedDefenses: ['tech'], defenseEffect: { tech: 1.0 }, messages: { success: 'השרתים הופלו עקב מתקפת מניעת שירות! האתר אינו זמין.', failure: 'מערכות ה-DDoS Mitigation עמדו במבחן! התעבורה הזדונית סוננה.' } },
    ];

    // Game Functions
    function updateStatsDisplay() {
        budgetEl.textContent = state.currentBudget.toLocaleString(); // Format with commas
        roundEl.textContent = state.round;
        riskValueEl.textContent = state.risk.toFixed(0);
        defenseValueEl.textContent = state.defense.toFixed(0);
        damageEl.textContent = state.damage.toLocaleString(); // Format with commas

        // Update risk level text and color
        if (state.risk < 35) { riskLevelEl.textContent = 'נמוך'; riskLevelEl.setAttribute('data-level', 'נמוך'); }
        else if (state.risk < 70) { riskLevelEl.textContent = 'בינוני'; riskLevelEl.setAttribute('data-level', 'בינוני'); }
        else { riskLevelEl.textContent = 'גבוה'; riskLevelEl.setAttribute('data-level', 'גבוה'); }

        // Update defense level text and color
        if (state.defense < 30) { defenseLevelEl.textContent = 'חלשה'; defenseLevelEl.setAttribute('data-level', 'בסיסית'); }
        else if (state.defense < 65) { defenseLevelEl.textContent = 'סבירה'; defenseLevelEl.setAttribute('data-level', 'טובה'); }
        else { defenseLevelEl.textContent = 'מתקדמת'; defenseLevelEl.setAttribute('data-level', 'מתקדמת'); }

        // Update defense breakdown levels
         for(const category in defenseBreakdownEls) {
             defenseBreakdownEls[category].textContent = state.defenseLevels[category].toFixed(1);
         }

         // Add animation class to stats that changed significantly (optional)
         // This requires storing previous state and comparing
    }

    function logReport(message, type = 'info') { // type can be 'info', 'success', 'warning', 'critical'
        const p = document.createElement('p');
        let iconClass = 'info';
        switch(type) {
            case 'success': iconClass = 'shield'; break;
            case 'warning': iconClass = 'warning'; break;
            case 'critical': iconClass = 'warning'; break; // Using warning icon for critical
            default: iconClass = 'info';
        }
        p.innerHTML = `<i class="icon ${iconClass}"></i> [חודש ${state.round}] ${message}`;
        p.className = `report-${type}`; // Add class for styling
        reportsLogEl.prepend(p); // Add to top

        // Clean up old logs
        while (reportsLogEl.children.length > 100) { // Keep a reasonable number of logs
            reportsLogEl.removeChild(reportsLogEl.lastChild);
        }
    }

    function calculateTotalAllocated() {
        let total = 0;
        for (const category in budgetInputs) {
            total += parseInt(budgetInputs[category].value) || 0;
        }
        return total;
    }

    function applyBudgetAllocation(allocation) {
        let totalDefenseChange = 0;

        for (const category in allocation) {
            // Apply decay *before* adding new investment
            state.defenseLevels[category] *= (1 - defenseDecayRate);

             // Apply new investment
            const investment = allocation[category];
            const defenseIncrease = investment * defenseEffectiveness[category];
            state.defenseLevels[category] += defenseIncrease;
            totalDefenseChange += defenseIncrease;
        }

        // Calculate overall defense (weighted sum or average)
        // Let's use a weighted sum based on how critical each area is for overall defense feeling
         const weights = { tech: 0.3, training: 0.15, updates: 0.2, backup: 0.1, response: 0.25 };
         state.defense = Object.keys(state.defenseLevels).reduce((sum, category) => sum + (state.defenseLevels[category] * weights[category] * 2), 0); // Multiply by 2 to make levels grow faster

         // Cap defense level for display
        state.defense = Math.min(state.defense, 100);

        // Risk slightly decreases with investment in defense, but mostly increases from attacks
        // state.risk = Math.max(5, state.risk - (totalDefenseChange * 0.01)); // Minimal risk decrease from spending
    }

    function simulateAttack() {
        // --- Attack Selection ---
        // Attacks become more likely and advanced as risk and rounds increase
        let possibleAttacks = attackTypes.filter(attack => {
             // Filter based on minimum risk and round required for advanced attacks
             const minRiskForAdvanced = (attack.type === 'ransomware' || attack.type.startsWith('apt')) ? 40 : 0;
             const minRoundForAdvanced = (attack.type === 'ransomware' || attack.type.startsWith('apt')) ? 6 : 1;
             const minRoundForMid = (attack.type === 'exploit' || attack.type === 'malware') ? 3 : 1;
             const minRiskForMid = (attack.type === 'exploit' || attack.type === 'malware') ? 20 : 0;

             return state.risk >= minRiskForAdvanced && state.round >= minRoundForAdvanced ||
                    state.risk >= minRiskForMid && state.round >= minRoundForMid ||
                    (attack.type === 'phishing' || attack.type === 'malware' || attack.type === 'ddos') && state.round >= 1;
        });

        // If no advanced attacks qualify, ensure there's always a basic one
        if (possibleAttacks.length === 0) {
            possibleAttacks = attackTypes.filter(attack => !attack.hidden); // Only show non-hidden basic attacks
        }

        // Select attack probabilistically based on risk level and available types
        // Higher risk makes more severe attacks more likely
        const totalAttackWeight = possibleAttacks.reduce((sum, attack) => {
            let weight = 1; // Base weight
            if (attack.type === 'ransomware') weight = 1.5;
            if (attack.type.startsWith('apt')) weight = 1.2;
            // Increase weight significantly at higher risk
            weight += (state.risk / 100) * (attack.baseRiskImpact / 10); // Attacks with higher impact are more likely at high risk
            return sum + weight;
        }, 0);

        let randomWeight = Math.random() * totalAttackWeight;
        let selectedAttack = possibleAttacks[0]; // Default
        for(const attack of possibleAttacks) {
            let weight = 1;
            if (attack.type === 'ransomware') weight = 1.5;
            if (attack.type.startsWith('apt')) weight = 1.2;
            weight += (state.risk / 100) * (attack.baseRiskImpact / 10);
            randomWeight -= weight;
            if (randomWeight <= 0) {
                selectedAttack = attack;
                break;
            }
        }

        const attack = selectedAttack; // The chosen attack for this round

        // Don't log hidden APT recon attack if it doesn't succeed significantly
        if (!attack.hidden) {
             logReport(`איום זוהה: ${attack.name}.`, 'warning');
        }


        // --- Calculate Effective Defense vs. This Attack ---
        let effectiveDefenseAgainstAttack = 0;
        let defenseEffectivenessSum = 0;
         for(const defenseCategory of attack.affectedDefenses) {
             const effectWeight = attack.defenseEffect[defenseCategory] || 0;
             effectiveDefenseAgainstAttack += state.defenseLevels[defenseCategory] * effectWeight;
             defenseEffectivenessSum += effectWeight;
         }
         // Normalize effective defense based on weights
         effectiveDefenseAgainstAttack = defenseEffectivenessSum > 0 ? effectiveDefenseAgainstAttack / defenseEffectivenessSum : 0;


        // --- Calculate Attack Success Chance ---
        // Higher risk increases success chance
        // Higher effective defense decreases success chance
        // Attack type's base negation slightly reduces effective defense
        const riskInfluence = (state.risk / 100) * 0.4; // Risk adds up to 40% chance influence
        const defenseInfluence = (effectiveDefenseAgainstAttack / 100) * 0.6; // Defense subtracts up to 60% chance influence
        const attackNegationInfluence = (attack.baseDefenseNegation / 100) * 0.2; // Attack type negates defense slightly

        let successChance = 0.5 + riskInfluence - defenseInfluence + attackNegationInfluence; // Base 50% chance
        successChance = Math.max(0.05, Math.min(0.95, successChance)); // Clamp between 5% and 95%


        const attackSuccessful = Math.random() < successChance;

        let damageTaken = 0;
        let reportMessage = `התקפת ${attack.name}: `;
        let reportType = 'info'; // Default report type


        if (attackSuccessful) {
            // Damage calculation: based on potential damage, modified by risk and *lack* of effective defense
            damageTaken = attack.potentialDamage * (1 + (state.risk / 100) - (effectiveDefenseAgainstAttack / 100));
            damageTaken = Math.max(attack.potentialDamage * 0.3, damageTaken); // Minimum damage on a successful hit
            damageTaken = Math.round(damageTaken * (1 + (Math.random() - 0.5) * 0.3)); // Add some randomness

            state.damage += damageTaken;
            reportMessage = attack.messages.success; // Use specific success message
            reportType = (damageTaken >= attack.potentialDamage * 0.8 || attack.type.startsWith('apt')) ? 'critical' : 'warning';

            // Successful attacks significantly increase risk
            state.risk = Math.min(100, state.risk + attack.baseRiskImpact * (1 + (state.round / state.maxRounds))); // Risk increases more in later rounds
             // APT successful attacks have a larger, persistent risk increase
             if(attack.type.startsWith('apt')) {
                 state.risk = Math.min(100, state.risk + attack.baseRiskImpact * 2);
             }


        } else {
            reportMessage = attack.messages.failure; // Use specific failure message
             reportType = 'success';

            // Successfully defending slightly reduces risk and increases overall defense feeling
             state.risk = Math.max(5, state.risk - attack.baseRiskImpact * 0.3); // Small risk decrease
             state.defense = Math.min(100, state.defense + 1); // Very small bonus for successful defense
        }

         // Log report only if it's not a hidden attack or if a hidden attack was successful
        if (!attack.hidden || (attack.hidden && attackSuccessful)) {
            logReport(reportMessage + (attackSuccessful ? ` נזק מוערך: $${damageTaken.toLocaleString()}.` : ''), reportType);
        }

    }

    function checkGameOver() {
        if (state.damage >= state.maxDamage) {
            state.gameOver = true;
            gameOverTitleEl.textContent = "הסימולציה הסתיימה - כישלון!";
            finalScoreEl.textContent = `נגרם נזק מצטבר של $${state.damage.toLocaleString()}, החברה קרסה תחת הנטל הכלכלי והתדמיתי. נכשלת במשימה לאחר ${state.round} חודשים. נסה שוב והגן טוב יותר!`;
            return true;
        }
         if (state.round > state.maxRounds) {
            state.gameOver = true;
            // Calculate final score based on damage minimized and final defense/risk levels
            const damagePenalty = state.damage;
            const riskPenalty = state.risk * 8000; // Higher penalty for high final risk
            const defenseBonus = state.defense * 5000; // Higher bonus for high final defense
            const baseValue = state.maxDamage * state.maxRounds * 0.2; // Base value for completing all rounds

            const finalScore = Math.max(0, baseValue - damagePenalty - riskPenalty + defenseBonus); // Simplified score calculation

            gameOverTitleEl.textContent = "הסימולציה הסתיימה - הצלחה!";
            finalScoreEl.textContent = `עברת בהצלחה 18 חודשים! נזק מצטבר: $${state.damage.toLocaleString()}. רמת סיכון סופית: ${state.risk.toFixed(0)}. רמת הגנה סופית: ${state.defense.toFixed(0)}. ציון ההצלחה שלך: ${finalScore.toFixed(0)}$. מזל טוב, הצלת את החברה!`;
             // Change game over message style for win state
             gameOverMessageEl.style.borderColor = '#27ae60'; // Green border
             gameOverMessageEl.style.backgroundColor = '#f0fff0'; // Light green background
             gameOverTitleEl.style.color = '#27ae60'; // Green title
             gameOverMessageEl.querySelector('button').style.backgroundColor = '#2ecc71';
             gameOverMessageEl.querySelector('button').style.borderColor = '#2ecc71';

             return true;
         }
        return false;
    }

    function endRound() {
        if (state.gameOver) return;

        const allocated = calculateTotalAllocated();

        if (allocated > state.monthlyBudget) {
            budgetErrorEl.style.display = 'block';
            logReport("שגיאה בהקצאת תקציב: סך ההקצאה חורג מהתקציב החודשי הזמין.", 'critical');
            return;
        } else {
            budgetErrorEl.style.display = 'none';
        }

        // Apply allocated budget
        const allocation = {};
        for (const category in budgetInputs) {
             allocation[category] = parseInt(budgetInputs[category].value) || 0;
             // Reset input fields for next round
             budgetInputs[category].value = 0;
        }
        applyBudgetAllocation(allocation);

        // Simulate attack for the round
        simulateAttack();

        // Advance round
        state.round++;
        state.currentBudget = state.monthlyBudget; // Refresh budget for next month

        // Update display
        updateStatsDisplay();

        // Check game over conditions
        if (checkGameOver()) {
             gameContainerEl.style.display = 'none';
             gameOverMessageEl.style.display = 'block';
        } else {
            // Log start of next round
             if (state.round <= state.maxRounds) {
                logReport("מתחיל חודש חדש. נתח את הדוחות, הקצה תקציב בחוכמה והגן על החברה!", 'info');
             }
        }
    }

    // Event Listeners
    nextRoundButton.addEventListener('click', endRound);

     // Update remaining budget display as user types
     Object.values(budgetInputs).forEach(input => {
        input.addEventListener('input', () => {
            const allocated = calculateTotalAllocated();
            const remaining = state.monthlyBudget - allocated;
            budgetEl.textContent = remaining.toLocaleString(); // Format remaining budget

            if (remaining < 0) {
                budgetEl.style.color = 'red';
                budgetErrorEl.style.display = 'block';
                nextRoundButton.disabled = true;
                nextRoundButton.textContent = "תקציב חורג!";
            } else {
                 budgetEl.style.color = remaining < state.monthlyBudget * 0.2 ? 'orange' : 'green'; // Color changes based on remaining budget
                 budgetErrorEl.style.display = 'none';
                 nextRoundButton.disabled = false;
                 nextRoundButton.innerHTML = '<i class="icon play"></i> סיום חודש והתמודדות עם איומים';
            }
        });
     });


    explanationButton.addEventListener('click', () => {
        const isHidden = explanationContentEl.style.display === 'none';
        explanationContentEl.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר הסבר תיאורטי' : 'הצג הסבר תיאורטי על הגנת סייבר';
    });

    // Initial setup
     monthlyBudgetEl.textContent = state.monthlyBudget.toLocaleString();
    updateStatsDisplay();
});
</script>
```