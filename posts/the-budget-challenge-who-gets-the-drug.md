---
title: "ועדת סל התרופות: המשימה הקריטית"
english_slug: the-budget-challenge-who-gets-the-drug
category: "כלכלה התנהגותית"
tags:
  - כלכלה
  - בריאות הציבור
  - אתיקה רפואית
  - קבלת החלטות
  - מדיניות ציבורית
  - תקצוב
---
# ועדת סל התרופות: המשימה הקריטית

ברוכים הבאים לסימולציה שמאתגרת אתכם לקבל את אחת ההחלטות הציבוריות הקשות ביותר: אילו תרופות וטיפולים מצילים או מאריכים חיים ייכללו בסל הבריאות הממלכתי, בהינתן תקציב מוגבל?

בתפקיד חברי ועדת הסל, עליכם לבחון הצעות לטיפולים חדשים ולבחור את אלו שייכנסו לסל, מבלי לחרוג מהמסגרת התקציבית. כל בחירה משפיעה ישירות על חיי מטופלים. האם תצליחו לנווט בין השיקולים הרפואיים, הכלכליים והאתיים?

לחצו על כרטיסיות התרופות הזמינות כדי להעביר אותן לסל שבניתם. לחצו עליהן שוב בסל כדי להסירן.

<div class="app-container" dir="rtl">
    <div class="budget-area">
        <h2>תקציב שנתי: <span id="total-budget"></span> ש"ח</h2>
        <div class="budget-bar-container">
            <div id="budget-bar" class="budget-bar"></div>
        </div>
         <p class="budget-label">יתרה/חריגה:</p>
        <h2><span id="current-budget"></span> ש"ח</h2>
        <p id="budget-status" class="budget-status"></p>
    </div>
    <div class="proposals-and-basket">
        <div class="available-proposals panel">
            <h3>הצעות לדיון <span class="icon">💡</span> (לחצו כדי להוסיף לסל)</h3>
            <div id="proposals-list" class="proposals-list list">
                <!-- Drug proposal cards will be rendered here -->
            </div>
        </div>
        <div class="drug-basket panel">
            <h3>סל התרופות שבניתם <span class="icon">🛒</span> (לחצו כדי להסיר מהסל)</h3>
            <div id="basket-list" class="basket-list list">
                <!-- Selected drug cards will be rendered here -->
            </div>
        </div>
    </div>
    <button id="finish-button" class="action-button">סיימתי את בניית הסל!</button>
    <div id="results-area" class="results-area hidden panel">
        <h3><span class="icon">📊</span> סיכום החלטות הסל שלכם</h3>
        <div id="results-content">
            <!-- Results will be displayed here -->
        </div>
    </div>
</div>

<style>
/* General Styles */
.app-container {
    font-family: 'Arial', sans-serif;
    max-width: 1100px;
    margin: 20px auto;
    padding: 25px;
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    direction: rtl; /* Hebrew support */
    text-align: right;
    overflow: hidden; /* Clear floats/margins */
}

h1 {
    color: #004d40; /* Dark Teal */
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.2em;
    font-weight: bold;
}

h2 {
     color: #006064; /* Cyan-Teal */
     text-align: center;
     margin: 10px 0;
     font-size: 1.8em;
}

h3 {
    color: #00796b; /* Teal */
    margin-top: 0;
    margin-bottom: 15px;
    padding-bottom: 5px;
    border-bottom: 2px solid #b2ebf2; /* Light Cyan */
    display: flex;
    align-items: center;
    justify-content: center; /* Center align headings */
    gap: 8px; /* Space between text and icon */
}

.icon {
    font-size: 1.1em;
}

.panel {
    background-color: #ffffff;
    border: 1px solid #e0f7fa; /* Light border */
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

/* Budget Area */
.budget-area {
    margin-bottom: 30px;
    padding: 20px;
    background-color: #e0f2f7; /* Very Light Blue-Green */
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.budget-label {
     font-size: 1.1em;
     color: #004d40;
     margin-bottom: 5px;
}

.budget-area h2 span {
    font-weight: bold;
    color: #004d40; /* Dark Teal */
}


.budget-bar-container {
    width: 95%;
    margin: 15px auto;
    background-color: #b2dfdb; /* Light Teal */
    border-radius: 12px;
    overflow: hidden;
    height: 30px;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
}

.budget-bar {
    height: 100%;
    width: 100%; /* Starts full */
    background-color: #4CAF50; /* Green */
    transition: width 0.8s ease-in-out, background-color 0.8s ease-in-out; /* Smoother transition */
    border-radius: 12px; /* Match container radius */
}

.budget-bar.over-budget {
    background-color: #e53935; /* Red */
     animation: pulse-red 1s infinite alternate; /* Add pulsing animation for over budget */
}

@keyframes pulse-red {
    from { background-color: #e53935; }
    to { background-color: #ff5252; }
}


.budget-status {
    font-weight: bold;
    margin-top: 15px;
    font-size: 1.1em;
    min-height: 1.5em; /* Prevent layout shift */
}

.budget-status.over-budget {
    color: #e53935; /* Red */
}

/* Proposals and Basket Layout */
.proposals-and-basket {
    display: flex;
    flex-wrap: wrap;
    gap: 25px; /* Increased gap */
    margin-bottom: 30px;
}

.available-proposals, .drug-basket {
    flex: 1;
    min-width: 320px; /* Adjusted min-width */
}

.list {
    min-height: 200px; /* Increased visual space */
    padding: 10px; /* Added padding */
    background-color: #f5f5f5; /* Light grey background for list area */
    border-radius: 8px;
    border: 1px dashed #cfd8dc; /* Dashed border to indicate drop area */
}

.proposals-list .drug-card {
     border-color: #e0f7fa; /* Light border */
     background-color: #e0f7fa; /* Very Light Blue-Green */
}

.basket-list .drug-card {
    border-color: #b2ebf2; /* Light border */
    background-color: #b2ebf2; /* Light Cyan */
}

/* Drug Cards */
.drug-card {
    border: 1px solid; /* Border color set in parent list */
    border-radius: 8px;
    padding: 15px; /* Increased padding */
    margin-bottom: 12px; /* Increased margin */
    cursor: pointer;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out, opacity 0.3s ease; /* Added opacity transition */
    position: relative; /* Needed for potential animations */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.drug-card:hover {
    transform: translateY(-5px) scale(1.02); /* More pronounced hover effect */
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
    background-color: #ffffff; /* White on hover */
}

.drug-card h4 {
    margin-top: 0;
    margin-bottom: 8px; /* Increased margin */
    color: #004d40; /* Dark Teal */
    font-size: 1.1em;
    font-weight: bold;
}

.drug-card p {
    margin: 5px 0; /* Increased margin */
    font-size: 0.95em;
    color: #555;
    line-height: 1.4;
}

.drug-card p strong {
    color: #333;
}

.drug-card .cost {
    font-weight: bold;
    color: #c62828; /* Dark Red */
    font-size: 1.05em;
}

/* Buttons */
button {
    display: block;
    width: 250px; /* Increased width */
    margin: 25px auto; /* Increased margin */
    padding: 12px 25px; /* Increased padding */
    background-color: #00796b; /* Teal */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

button:hover {
    background-color: #004d40; /* Darker Teal */
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

button:active {
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

#toggle-explanation {
    background-color: #546e7a; /* Blue-grey */
     margin-top: 40px; /* More space above explanation toggle */
}
#toggle-explanation:hover {
     background-color: #37474f; /* Darker blue-grey */
}


/* Results Area */
.results-area {
    margin-top: 30px; /* Increased margin */
    background-color: #e0f7fa; /* Light blue-green */
    border-color: #b2ebf2;
}

.results-area h3 {
     color: #00796b; /* Teal */
     border-bottom-color: #b2ebf2;
}

.results-area p {
    font-size: 1.05em;
    margin-bottom: 10px;
    line-height: 1.5;
}

.results-area strong {
    color: #004d40; /* Dark Teal */
}

.results-area ul {
    list-style: none; /* Remove default list style */
    padding: 0;
    margin-top: 20px;
}

.results-area li {
    background-color: #ffffff; /* White background for list items */
    border: 1px solid #b2ebf2; /* Light border */
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.results-area li strong {
    color: #00796b; /* Teal */
}

.results-area .budget-warning {
    color: #c62828; /* Dark Red */
    font-weight: bold;
    margin-top: 20px;
    padding: 15px;
    background-color: #ffebee; /* Very light red */
    border: 1px solid #ef9a9a; /* Light red border */
    border-radius: 8px;
    text-align: center;
}

.results-area .budget-suggestion {
    color: #fbc02d; /* Dark Yellow */
    font-weight: bold;
     margin-top: 20px;
    padding: 15px;
    background-color: #fffde7; /* Very light yellow */
    border: 1px solid #fff59d; /* Light yellow border */
    border-radius: 8px;
    text-align: center;
}


.hidden {
    display: none;
}

/* Explanation Area */
.explanation {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ffcc80; /* Light orange border */
    border-radius: 10px;
    background-color: #fff3e0; /* Light orange */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.explanation h2, .explanation h3 {
    color: #e65100; /* Darker orange */
    border-bottom-color: #ffcc80; /* Light orange border */
}

.explanation p {
    color: #4e342e; /* Brownish text */
    line-height: 1.6;
    margin-bottom: 15px;
}

.explanation ul {
     padding-right: 20px;
     list-style: disc;
     color: #4e342e;
}

.explanation li {
     margin-bottom: 8px;
}

.explanation li strong {
    color: #d84315; /* Orange-Red */
}


/* Responsive adjustments */
@media (max-width: 768px) {
    .proposals-and-basket {
        flex-direction: column;
        gap: 15px;
    }

    .available-proposals, .drug-basket {
        min-width: 95%;
    }

    button {
        width: 90%;
        padding: 10px 20px;
        font-size: 1em;
    }

     h1 { font-size: 1.8em; }
     h2 { font-size: 1.5em; }
     h3 { font-size: 1.2em; }

     .panel { padding: 15px; }
     .drug-card { padding: 12px; }
     .results-area li { padding: 10px; }
}

</style>

<button id="toggle-explanation">רוצים להבין יותר? קראו על ועדת הסל כאן</button>
<div id="explanation" class="explanation hidden">
    <h2>רקע והסבר: ועדת סל התרופות</h2>
    <p>כפי שחוויתם בסימולציה, תהליך ההחלטה אילו תרופות וטכנולוגיות רפואיות ייכנסו לסל הבריאות הממלכתי הוא מורכב, טעון, וכרוך בדילמות קשות. הסימולציה נועדה לדמות את האתגרים העומדים בפני ועדת סל התרופות בישראל.</p>

    <h3>מהי ועדת סל התרופות ותפקידה?</h3>
    <p>ועדת סל שירותי הבריאות היא ועדה ציבורית הממונה על ידי שר הבריאות. תפקידה המרכזי הוא להחליט אילו תרופות, טכנולוגיות וטיפולים רפואיים חדשים ייכללו בסל שירותי הבריאות הממלכתי. הסל הוא רשימה של כל הטיפולים והשירותים שמשרד הבריאות וקופות החולים מחויבים לממן למבוטחים בישראל. מדי שנה מקצה המדינה תקציב נוסף מוגבל להרחבת הסל, והוועדה צריכה לבחור אילו מההצעות הרבות שהוגשו ייכללו בו במסגרת התקציב.</p>

    <h3>הקונפליקט הבסיסי: משאבים מוגבלים מול צרכים בלתי מוגבלים</h3>
    <p>זהו לב הדילמה. הצרכים הרפואיים בחברה הם עצומים ותמיד יהיו חידושים רפואיים יקרים שיכולים לעזור לחולים רבים או מעטים. לעומת זאת, התקציב המוקצה להרחבת הסל מוגבל. עובדה זו יוצרת מצב בו לא ניתן להכניס את כל התרופות והטכנולוגיות המומלצות, ונדרשת בחירה כואבת - מי יקבל טיפול מציל או מאריך חיים ומי לא.</p>

    <h3>הקריטריונים המנחים את הועדה</h3>
    <p>הוועדה מתבססת על קריטריונים מוגדרים, אך אופן יישומם כרוך בפרשנות ובאיזונים:
    <ul>
        <li><strong>עלות-תועלת:</strong> האם התועלת הבריאותית (הארכת חיים, שיפור איכות חיים) שמספקת התרופה מצדיקה את עלותה?</li>
        <li><strong>חומרת המחלה:</strong> האם מדובר במחלה קשה, מסכנת חיים או גורמת סבל רב? ניתנת לרוב עדיפות לטיפול במחלות קשות יותר.</li>
        <li><strong>היקף האוכלוסיה:</strong> כמה מטופלים פוטנציאליים ייהנו מהטיפול? טיפולים למחלות נפוצות משפיעים על רבים, בעוד טיפולים למחלות נדירות משפיעים על קבוצה קטנה.</li>
        <li><strong>היבטים אתיים וחברתיים:</strong> שיקולים כמו טיפול בילדים, חולים סופניים (טיפול פליאטיבי), צדק חברתי (האם התרופה זמינה רק לעשירים בלעדי הסל?), מחלות נדירות ("יתום" תרופתי).</li>
    </ul>
    </p>

    <h3>מושגים מרכזיים כמו QALY</h3>
    <p>אחד הכלים המשמשים להערכת עלות-תועלת הוא ה-QALY (Quality-Adjusted Life Year) - "שנת חיים מותאמת לאיכות". QALY מנסה לכמת את התועלת של טיפול לא רק לפי הארכת חיים, אלא גם לפי איכות החיים בשנים שהתווספו. שנת חיים בבריאות מלאה נחשבת ל-1 QALY, בעוד שנת חיים עם מחלה קשה או מוגבלות מקבלת ציון נמוך יותר (למשל 0.5 QALY). על ידי חישוב עלות לכל QALY שהטיפול מוסיף, ניתן להשוות יחסית בין טיפולים שונים המשפיעים באופן שונה על חיים ואיכות חיים.</p>

    <h3>הדילמות המוסריות והחברתיות</h3>
    <p>ההחלטות בוועדת הסל אינן רק כלכליות או קליניות. הן נוגעות ישירות לחיי אדם, לסבל, לתקווה ולאכזבה. הדילמות כוללות: האם לתעדף הארכת חיים על פני שיפור איכות חיים? האם להשקיע משאבים עצומים במחלה נדירה לעומת טיפול זול ויעיל למחלה נפוצה? כיצד מתייחסים לחולים סופניים? לחולים ש"אשמים" במחלתם (למשל, מעשנים)? זו אחריות ציבורית כבדה.</p>

    <h3>השפעת גורמים חיצוניים</h3>
    <p>הוועדה פועלת תחת לחץ ציבורי ותקשורתי משמעותי. סיפורים אישיים של חולים בתקשורת, קמפיינים ציבוריים, ולעיתים גם לובינג של חברות תרופות, משפיעים על השיח הציבורי ועל האווירה סביב החלטות הוועדה, גם אם ההחלטות הפורמליות מתבססות על הקריטריונים.</p>

    <h3>מדוע התהליך הכרחי, קשה ושקוף</h3>
    <p>על אף הקושי והכאב הכרוכים בו, תהליך קבלת ההחלטות על סל הבריאות הכרחי בחברה מודרנית עם משאבים מוגבלים. השקיפות היחסית של עבודת הוועדה (הדיונים מתועדים, ההחלטות מנומקות) חשובה לאמון הציבור במערכת, גם כשההחלטות קשות ומאכזבות. הסימולציה נועדה להדגיש את המורכבות של התהליך ולהמחיש שאין לו בהכרח "פתרון אחד נכון", אלא הוא תוצר של איזונים ערכיים, כלכליים וקליניים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const totalBudget = 500000000; // 500 million
    let currentSpent = 0;
    const drugs = [
        { id: 1, name: "תרופה לסרטן נדיר", cost_per_patient: 800000, num_patients: 100, total_cost: 80000000, efficacy: "מאריך חיים בשנים רבות, שיפור דרמטי באיכות חיים", severity: "מחלת סרטן נדירה, קטלנית ללא טיפול", ethical_considerations: "טיפול מציל חיים", category: "סרטן", impact_level: "High" },
        { id: 2, name: "תרופה למחלה אוטואימונית קשה", cost_per_patient: 250000, num_patients: 500, total_cost: 125000000, efficacy: "שיפור משמעותי באיכות חיים, הפחתת נכות", severity: "מחלה כרונית קשה, גורמת נכות", ethical_considerations: "", category: "אוטואימוני", impact_level: "Medium-High" },
        { id: 3, name: "טיפול חדשני לסיבוכי סוכרת", cost_per_patient: 30000, num_patients: 5000, total_cost: 150000000, efficacy: "מניעת הידרדרות ותחלואה משנית", severity: "מחלה כרונית נפוצה, בעלת סיבוכים קשים", ethical_considerations: "השפעה על אוכלוסייה גדולה", category: "סוכרת", impact_level: "High-Volume" },
        { id: 4, name: "תרופה למחלה גנטית קטלנית בילדים", cost_per_patient: 1200000, num_patients: 50, total_cost: 60000000, efficacy: "מציל חיים, מאפשר התפתחות תקינה", severity: "מחלה גנטית נדירה וקטלנית בילדים", ethical_considerations: "טיפול בילדים, מחלה נדירה", category: "מחלות נדירות", impact_level: "Critical-Rare" },
        { id: 5, name: "טיפול מונע לאירוע מוחי חוזר", cost_per_patient: 5000, num_patients: 10000, total_cost: 50000000, efficacy: "מניעת אירועים מוחיים בסיכון גבוה", severity: "מניעת תחלואה קשה", ethical_considerations: "טיפול מונע, השפעה רחבה", category: "קרדיו-וסקולרי", impact_level: "Prevention-Volume" },
        { id: 6, name: "טיפול פליאטיבי לחולים סופניים", cost_per_patient: 150000, num_patients: 200, total_cost: 30000000, efficacy: "שיפור דרמטי באיכות החיים והפחתת סבל בחודשי חיים אחרונים", severity: "מחלה סופנית", ethical_considerations: "טיפול בסוף חיים, כבוד האדם", category: "פליאטיבי", impact_level: "Palliative" },
        { id: 7, name: "תרופה למחלת נפש קשה ועמידה לטיפול", cost_per_patient: 200000, num_patients: 300, total_cost: 60000000, efficacy: "מאפשר חזרה לתפקוד מלא, מונע אשפוזים", severity: "מחלת נפש קשה, מגבילה מאוד", ethical_considerations: "בריאות הנפש", category: "פסיכיאטריה", impact_level: "Quality-of-Life" },
        { id: 8, name: "טיפול חדשני בכאב כרוני קשה", cost_per_patient: 10000, num_patients: 8000, total_cost: 80000000, efficacy: "הפחתה משמעותית של כאב כרוני", severity: "מצב כרוני פוגע באיכות החיים", ethical_considerations: "", category: "כאב", impact_level: "Symptom-Relief" }
    ];

    let availableDrugs = [...drugs];
    let selectedDrugs = [];

    const proposalsList = document.getElementById('proposals-list');
    const basketList = document.getElementById('basket-list');
    const currentBudgetSpan = document.getElementById('current-budget');
    const totalBudgetSpan = document.getElementById('total-budget');
    const budgetBar = document.getElementById('budget-bar');
    const budgetStatus = document.getElementById('budget-status');
    const finishButton = document.getElementById('finish-button');
    const resultsArea = document.getElementById('results-area');
    const resultsContent = document.getElementById('results-content');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    totalBudgetSpan.textContent = formatCurrency(totalBudget);

    function formatCurrency(amount) {
         // Use minimumFractionDigits: 0 to avoid decimals for whole numbers
         return amount.toLocaleString('he-IL', { minimumFractionDigits: 0 });
    }

    function updateBudgetDisplay() {
        currentSpent = selectedDrugs.reduce((sum, drug) => sum + drug.total_cost, 0);
        const remainingBudget = totalBudget - currentSpent;
        currentBudgetSpan.textContent = formatCurrency(remainingBudget);

        const budgetPercentage = Math.max(0, (totalBudget - currentSpent) / totalBudget) * 100;
        budgetBar.style.width = budgetPercentage + '%';

        if (remainingBudget < 0) {
            budgetBar.classList.add('over-budget');
            // budgetBar.style.width = '100%'; // Keep width for visual context
            budgetStatus.textContent = `חריגה מהתקציב בסך: ${formatCurrency(Math.abs(remainingBudget))} ש"ח`;
            budgetStatus.classList.add('over-budget');
             budgetStatus.classList.remove('within-budget');
        } else if (remainingBudget === totalBudget) {
             budgetBar.classList.remove('over-budget');
             budgetStatus.textContent = 'הסל ריק, כל התקציב זמין';
             budgetStatus.classList.remove('over-budget', 'within-budget');

        }
        else {
            budgetBar.classList.remove('over-budget');
             budgetStatus.textContent = `${formatCurrency(remainingBudget)} ש"ח נותרו בתקציב`;
             budgetStatus.classList.remove('over-budget');
             budgetStatus.classList.add('within-budget');

             if (budgetPercentage > 50) budgetBar.style.backgroundColor = '#4CAF50'; // Green
             else if (budgetPercentage > 10) budgetBar.style.backgroundColor = '#ffc107'; // Yellow
             else budgetBar.style.backgroundColor = '#ff9800'; // Orange
        }
         // Update button state
        // finishButton.disabled = currentSpent === 0; // Optional: Disable finish if nothing is selected
    }

    function renderDrugs(listElement, drugsArray, inBasket = false) {
        listElement.innerHTML = '';
        if (drugsArray.length === 0) {
             listElement.innerHTML = inBasket
                ? '<p style="text-align:center; color:#777; padding-top: 20px;">הסל ריק. לחצו על הצעות מהרשימה משמאל כדי להוסיף אותן.</p>'
                : '<p style="text-align:center; color:#777; padding-top: 20px;">אין הצעות נוספות לדיון כרגע.</p>';
             listElement.classList.add('empty');
        } else {
             listElement.classList.remove('empty');
             drugsArray.forEach(drug => {
                 const card = document.createElement('div');
                 card.classList.add('drug-card');
                 card.dataset.id = drug.id;
                 card.dataset.inBasket = inBasket; // Mark card source/destination
                 card.innerHTML = `
                    <h4>${drug.name}</h4>
                    <p><strong>עלות כוללת:</strong> <span class="cost">${formatCurrency(drug.total_cost)} ש"ח</span></p>
                    <p><strong>מטופלים:</strong> ${drug.num_patients.toLocaleString('he-IL')}</p>
                    <p><strong>יעילות:</strong> ${drug.efficacy}</p>
                    <p><strong>חומרת מחלה:</strong> ${drug.severity}</p>
                    ${drug.ethical_considerations ? `<p><strong>שיקול נוסף:</strong> ${drug.ethical_considerations}</p>` : ''}
                 `;

                // Add simple animation class before appending
                card.style.opacity = 0; // Start invisible
                listElement.appendChild(card);
                requestAnimationFrame(() => {
                    card.style.opacity = 1; // Fade in
                });
             });
        }
    }

    function moveDrug(drugId) {
        const drugIndexAvailable = availableDrugs.findIndex(d => d.id === drugId);
        const drugIndexSelected = selectedDrugs.findIndex(d => d.id === drugId);

        let drugToMove;
        let sourceList, destList, sourceArray, destArray;

        if (drugIndexAvailable !== -1) { // Drug is in available list, move to basket
            drugToMove = availableDrugs[drugIndexAvailable];
            sourceArray = availableDrugs;
            destArray = selectedDrugs;
            sourceList = proposalsList;
            destList = basketList;
        } else if (drugIndexSelected !== -1) { // Drug is in basket, move back to available
            drugToMove = selectedDrugs[drugIndexSelected];
            sourceArray = selectedDrugs;
            destArray = availableDrugs;
            sourceList = basketList;
            destList = proposalsList;
        } else {
            return; // Drug not found
        }

        // Add animation class before removal
        const cardElement = sourceList.querySelector(`.drug-card[data-id="${drugId}"]`);
        if (cardElement) {
             cardElement.style.opacity = 0; // Fade out
             cardElement.style.transform = 'scale(0.9)'; // Shrink slightly
             cardElement.style.transition = 'transform 0.3s ease, opacity 0.3s ease';


            setTimeout(() => {
                 // Remove from source array and add to destination array
                 const indexInSource = sourceArray.findIndex(d => d.id === drugId);
                 if (indexInSource !== -1) {
                      const [movedDrug] = sourceArray.splice(indexInSource, 1);
                      destArray.push(movedDrug);
                 }

                // Re-render lists
                renderDrugs(proposalsList, availableDrugs, false);
                renderDrugs(basketList, selectedDrugs, true);
                updateBudgetDisplay();
            }, 300); // Match animation duration
        } else {
             // Fallback if element not found (shouldn't happen with delegation)
             const indexInSource = sourceArray.findIndex(d => d.id === drugId);
                 if (indexInSource !== -1) {
                      const [movedDrug] = sourceArray.splice(indexInSource, 1);
                      destArray.push(movedDrug);
                 }
                renderDrugs(proposalsList, availableDrugs, false);
                renderDrugs(basketList, selectedDrugs, true);
                updateBudgetDisplay();
        }
    }

    function calculateResults() {
        const totalSpent = selectedDrugs.reduce((sum, drug) => sum + drug.total_cost, 0);
        const totalPatientsCovered = selectedDrugs.reduce((sum, drug) => sum + drug.num_patients, 0);
        const budgetDifference = totalBudget - totalSpent;

        let resultsHtml = `
            <p><strong>התקציב השנתי המוגדר:</strong> ${formatCurrency(totalBudget)} ש"ח</p>
            <p><strong>סך ההוצאה בסל שבניתם:</strong> ${formatCurrency(totalSpent)} ש"ח</p>
            <p><strong>יתרת/חריגת תקציב:</strong>
                ${budgetDifference >= 0
                    ? `<span style="color: #2e7d32; font-weight: bold;">${formatCurrency(budgetDifference)} ש"ח נותרו</span>`
                    : `<span style="color: #c62828; font-weight: bold;">${formatCurrency(Math.abs(budgetDifference))} ש"ח חריגה</span>`}
            </p>
            <p><strong>מספר המטופלים שיקבלו טיפול מהסל שבניתם (משוער):</strong> ${totalPatientsCovered.toLocaleString('he-IL')}</p>
            <h4><span class="icon">💊</span> רשימת התרופות שנבחרו לסל שלכם:</h4>
            <ul>
        `;

        if (selectedDrugs.length === 0) {
            resultsHtml += '<li>לא נבחרו תרופות לסל. אף מטופל לא יקבל טיפול מהרשימה המוצעת.</li>';
        } else {
             // Sort selected drugs perhaps by cost or category for readability?
            selectedDrugs.sort((a, b) => a.total_cost - b.total_cost); // Example sort
            selectedDrugs.forEach(drug => {
                resultsHtml += `<li><strong>${drug.name}:</strong> (עבור ${drug.num_patients.toLocaleString('he-IL')} מטופלים, עלות: ${formatCurrency(drug.total_cost)} ש"ח). יעילות: ${drug.efficacy}. חומרה: ${drug.severity}. ${drug.ethical_considerations ? `שיקול: ${drug.ethical_considerations}` : ''}</li>`;
            });
        }

        resultsHtml += '</ul>';

        if (Math.abs(budgetDifference) > totalBudget * 0.02 && budgetDifference < 0) { // Significant overspend (more than 2%)
             resultsHtml += `<p class="budget-warning"><span class="icon">⚠️</span> שימו לב: הסל שבניתם חורג משמעותית מהתקציב המוקצה (${formatCurrency(Math.abs(budgetDifference))} ש"ח). במציאות, היה צורך לבצע קיצוצים כואבים נוספים כדי לעמוד במסגרת.</p>`;
        } else if (budgetDifference > totalBudget * 0.05 && budgetDifference >= 0) { // Significant underspend (more than 5%)
             resultsHtml += `<p class="budget-suggestion"><span class="icon">💡</span> שימו לב: נותר חלק משמעותי מהתקציב (${formatCurrency(budgetDifference)} ש"ח). אולי יכולתם להוסיף עוד טיפולים מועילים כדי לסייע ליותר מטופלים?</p>`;
        } else if (budgetDifference >= 0 && budgetDifference <= totalBudget * 0.02) { // Close to budget
             resultsHtml += `<p style="color: #2e7d32; font-weight: bold; text-align: center; margin-top: 20px;"><span class="icon">✅</span> כל הכבוד! עמדתם במסגרת התקציב בהצלחה.</p>`;
        }


        resultsContent.innerHTML = resultsHtml;
        resultsArea.classList.remove('hidden');
         resultsArea.scrollIntoView({ behavior: 'smooth', block: 'start' }); // Scroll to results
    }

    // Event listeners for drug cards (using delegation)
    proposalsList.addEventListener('click', (event) => {
        const card = event.target.closest('.drug-card');
        if (card && card.dataset.inBasket === 'false') {
            const drugId = parseInt(card.dataset.id);
            moveDrug(drugId);
        }
    });

    basketList.addEventListener('click', (event) => {
        const card = event.target.closest('.drug-card');
        if (card && card.dataset.inBasket === 'true') {
            const drugId = parseInt(card.dataset.id);
            moveDrug(drugId);
        }
    });

    finishButton.addEventListener('click', calculateResults);

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
        if (!explanationDiv.classList.contains('hidden')) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial render
    renderDrugs(proposalsList, availableDrugs, false);
    renderDrugs(basketList, selectedDrugs, true); // Render basket list with placeholder if empty
    updateBudgetDisplay();
});
</script>