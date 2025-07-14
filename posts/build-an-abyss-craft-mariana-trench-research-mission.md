---
title: "מסע אל התהום: בנה חללית מחקר לשקע מריאנה"
english_slug: build-an-abyss-craft-mariana-trench-research-mission
category: "אוקיינוגרפיה"
tags:
  - שקע מריאנה
  - חקר ימים
  - אוקיינוס עמוק
  - צוללת
  - לחץ הידרוסטטי
  - הנדסה
---
# מסע אל התהום: בנה חללית מחקר לשקע מריאנה

שקע מריאנה - הנקודה העמוקה ביותר בכדור הארץ, מסתורית ועוינת. בלחץ אדיר, קור מקפיא וחשיכה מוחלטת, רק כלי שיט ייעודיים יכולים להגיע לשם. האם תצליח לתכנן כלי כזה? בנה את צוללת המחקר שלך, בחר את הציוד המתאים ביותר לתנאים הקיצוניים, ותכנן את המשימה האולטימטיבית אל התהום!

<div id="app-container">
    <div id="budget-display">
        <h2>התקציב שלך למשימה: <span id="current-budget" class="budget-value">$5,000,000</span></h2>
        <div class="budget-bar-container">
            <div id="budget-bar" class="budget-bar"></div>
        </div>
    </div>

    <div id="components-selection" class="section-container">
        <h2>בנה את חללית העומק שלך: בחר רכיבים</h2>

        <div class="component-category" id="body-type">
            <h3><i class="icon-body"></i> מבנה הגוף (חובה!)</h3>
            <div class="options">
                <label data-value="titanium" title="הגנה מירבית ללחץ קיצוני">
                    <input type="radio" name="body" value="titanium"> גוף טיטניום <span class="component-stats">(עומק מקס': 11000מ', משקל נשיאה מקס': 1200ק"ג) - עלות: $3,000,000, משקל: 800ק"ג, כוח בסיסי: 500W</span>
                </label>
                <label data-value="ceramic" title="עמיד מאוד ללחץ, קל יותר מטיטניום">
                    <input type="radio" name="body" value="ceramic"> גוף קרמי <span class="component-stats">(עומק מקס': 8000מ', משקל נשיאה מקס': 800ק"ג) - עלות: $1,500,000, משקל: 500ק"ג, כוח בסיסי: 300W</span>
                </label>
                <label data-value="steel" title="חזק אך כבד, לעומקים בינוניים">
                    <input type="radio" name="body" value="steel"> גוף פלדה מחוזקת <span class="component-stats">(עומק מקס': 5000מ', משקל נשיאה מקס': 700ק"ג) - עלות: $800,000, משקל: 700ק"ג, כוח בסיסי: 400W</span>
                </label>
                <label data-value="auv_frame" title="שלד קל לעומקים רדודים יחסית">
                    <input type="radio" name="body" value="auv_frame"> שלדת AUV בסיסית <span class="component-stats">(עומק מקס': 2000מ', משקל נשיאה מקס': 300ק"ג) - עלות: $200,000, משקל: 100ק"ג, כוח בסיסי: 200W</span>
                </label>
            </div>
        </div>

        <div class="component-category" id="power-source">
            <h3><i class="icon-power"></i> מנוע הלב (חובה!)</h3>
            <div class="options">
                <label data-value="large_battery" title="אספקת אנרגיה למשימות ארוכות ועמוקות">
                    <input type="radio" name="power" value="large_battery"> סוללות גדולות <span class="component-stats">(אספקת כוח: 100 קוט"ש) - עלות: $500,000, משקל: 400ק"ג, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="small_battery" title="אנרגיה למשימות קצרות יותר">
                    <input type="radio" name="power" value="small_battery"> סוללות קטנות <span class="component-stats">(אספקת כוח: 30 קוט"ש) - עלות: $200,000, משקל: 150ק"ג, עומק מקס': 11000מ'</span>
                </label>
            </div>
        </div>

        <div class="component-category" id="research-equipment">
            <h3><i class="icon-research"></i> כלי מדע וחישה (בחר אחד או יותר)</h3>
            <div class="options">
                <label data-value="pressure_camera" title="צילום תמונות ווידאו באיכות גבוהה בלחץ עצום">
                    <input type="checkbox" name="research" value="pressure_camera"> מצלמה עמידת לחץ <span class="component-stats">(צילום בעומק קיצוני) - עלות: $400,000, משקל: 50ק"ג, כוח: 50W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="high_res_camera" title="מצלמה איכותית לעומקים בינוניים">
                    <input type="checkbox" name="research" value="high_res_camera"> מצלמה ברזולוציה גבוהה <span class="component-stats">(צילום כללי) - עלות: $250,000, משקל: 30ק"ג, כוח: 40W, עומק מקס': 8000מ'</span>
                </label>
                <label data-value="temp_sensor" title="מדידת הטמפרטורה המדויקת במים העמוקים">
                    <input type="checkbox" name="research" value="temp_sensor"> חיישן טמפרטורה <span class="component-stats">- עלות: $50,000, משקל: 5ק"ג, כוח: 10W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="pressure_sensor" title="מדידת הלחץ ההידרוסטטי לאימות נתונים">
                    <input type="checkbox" name="research" value="pressure_sensor"> חיישן לחץ <span class="component-stats">- עלות: $60,000, משקל: 5ק"ג, כוח: 10W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="chem_sensor" title="ניתוח הרכב כימי של המים, כולל מליחות וחמצן">
                    <input type="checkbox" name="research" value="chem_sensor"> חיישני כימיה <span class="component-stats">(ניתוח הרכב מים) - עלות: $150,000, משקל: 20ק"ג, כוח: 30W, עומק מקס': 10000מ'</span>
                </label>
                <label data-value="sample_arm" title="איסוף דגימות קרקעית, מים ויצורים חיים">
                    <input type="checkbox" name="research" value="sample_arm"> זרוע איסוף דגימות <span class="component-stats">- עלות: $700,000, משקל: 150ק"ג, כוח: 100W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="sonar" title="מיפוי תלת-ממדי של קרקעית הים המורכבת">
                    <input type="checkbox" name="research" value="sonar"> סונאר סריקת צד <span class="component-stats">(מיפוי קרקעית) - עלות: $600,000, משקל: 100ק"ג, כוח: 80W, עומק מקס': 7000מ'</span>
                </label>
            </div>
        </div>

        <div class="component-category" id="lighting">
            <h3><i class="icon-light"></i> עיניים בחשיכה</h3>
            <div class="options">
                <label data-value="powerful_led" title="תאורה חזקה לחשיכה המוחלטת בעומק">
                    <input type="radio" name="lighting" value="powerful_led"> תאורת LED חזקה <span class="component-stats">(לעומק רב) - עלות: $100,000, משקל: 15ק"ג, כוח: 70W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="basic_lights" title="תאורה סטנדרטית לעומקים רדודים יותר">
                    <input type="radio" name="lighting" value="basic_lights"> תאורה בסיסית <span class="component-stats">(לעומק בינוני) - עלות: $40,000, משקל: 8ק"ג, כוח: 30W, עומק מקס': 6000מ'</span>
                </label>
            </div>
        </div>

        <div class="component-category" id="navigation">
            <h3><i class="icon-nav"></i> דרך בחשכה</h3>
            <div class="options">
                <label data-value="acoustic_nav" title="ניווט מדויק ואמין בסביבה אקוסטית מאתגרת">
                    <input type="radio" name="navigation" value="acoustic_nav"> ניווט אקוסטי מתקדם <span class="component-stats">(לעומק רב) - עלות: $300,000, משקל: 25ק"ג, כוח: 20W, עומק מקס': 11000מ'</span>
                </label>
                <label data-value="basic_nav" title="ניווט בסיסי לעומקים רדודים יותר">
                    <input type="radio" name="navigation" value="basic_nav"> ניווט בסיסי <span class="component-stats">(לעומק בינוני) - עלות: $80,000, משקל: 10ק"ג, כוח: 10W, עומק מקס': 5000מ'</span>
                </label>
            </div>
        </div>
    </div>

    <div id="current-build-stats" class="section-container">
        <h2><i class="icon-stats"></i> סיכום הרכבה נוכחית</h2>
        <p>עלות כוללת: <span id="total-cost" class="stat-value">-</span></p>
        <p>משקל כולל (כולל גוף): <span id="total-weight" class="stat-value">-</span></p>
        <p>משקל ציוד (ללא גוף): <span id="payload-weight" class="stat-value">-</span></p>
        <p>צריכת כוח כוללת: <span id="total-power-draw" class="stat-value">-</span></p>
        <p>עומק מקסימלי שכל הרכיבים עומדים בו: <span id="combined-max-depth" class="stat-value">-</span></p>
    </div>

    <div id="mission-planning" class="section-container">
        <h2><i class="icon-mission"></i> הגדר את יעד המשימה</h2>
        <div>
            <label for="mission-depth">עומק יעד (מטר):</label>
            <input type="number" id="mission-depth" min="1" max="11000" value="5000">
        </div>
        <div>
            <label for="mission-duration">משך יעד (שעות):</label>
            <input type="number" id="mission-duration" min="1" max="72" value="12">
        </div>
        <button id="plan-mission-button"><i class="icon-launch"></i> תכנן משימה!</button>
    </div>

    <div id="mission-results" class="section-container">
        <h2><i class="icon-results"></i> סיכום המשימה</h2>
        <p id="results-text">בחר רכיבים והגדר יעד משימה כדי לקבל סיכום.</p>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר על חקר שקע מריאנה והתנאים בתהום</button>
<div id="explanation" style="display: none;">
    <h2>שקע מריאנה - אתגרים וחקר</h2>
    <p>שקע מריאנה הוא התהום האוקיינית העמוקה ביותר הידועה על פני כדור הארץ, הממוקמת במערב האוקיינוס השקט. העומק המרבי הידוע בו, בנקודת הצ'לנג'ר דיפ, מגיע לכ-10,994 מטרים (קרוב ל-11 קילומטרים). זהו עומק שיכול לבלוע את הר האוורסט כולו ועוד להישאר מים מעליו!</p>

    <h3>התנאים הקיצוניים בשקע - מדוע זה כל כך מסובך?</h3>
    <p>הסביבה בשקע מריאנה מתאפיינת בתנאים קיצוניים ביותר המהווים אתגר הנדסי ומדעי:</p>
    <ul>
        <li>**לחץ הידרוסטטי עצום:** בעומק 11 ק"מ, הלחץ גדול פי למעלה מ-1,000 מהלחץ על פני הים (כ-1100 אטמוספרות!). דמיינו משאית כבדה היושבת על כל סנטימטר רבוע של הכלי - זהו הלחץ שמנסה למעוך אותו.</li>
        <li>**טמפרטורה נמוכה:** הטמפרטורה קרובה לנקודת הקיפאון, כ-1-4 מעלות צלזיוס. הקור דורש בידוד והתאמת רכיבים.</li>
        <li>**חשיכה מוחלטת:** אור השמש אינו חודר לעומקים אלה. כדי לראות משהו, נדרשת תאורה מלאכותית חזקה ועמידה ללחץ.</li>
        <li>**תקשורת מסובכת:** גלי רדיו אינם חודרים עמוק למים. תקשורת עם כלי בעומק דורשת שימוש בטכנולוגיות אקוסטיות מורכבות ואיטיות, או כבלי תקשורת מסורבלים (ל-ROVs).</li>
    </ul>

    <h3>כלים לחקר התהום: רובוטים ובני אדם</h3>
    <p>חקר העומק הקיצוני מתאפשר בעיקר באמצעות שני סוגי כלים, שלכל אחד יתרונות וחסרונות:</p>
    <ul>
        <li>**צוללות מאוישות (כמו הטריאסטה והדיפסי צ'לנג'ר):** מאפשרות נוכחות אנושית ותצפית ישירה, אך הן יקרות ומורכבות להנדסה (דורשות תא טייס עמיד במיוחד) ולתפעול. מעטות מאוד נוצרו המסוגלות להגיע לעומק המרבי.</li>
        <li>**כלי רכב תת-ימיים בלתי מאוישים (ROVs ו-AUVs):** רובוטים הנשלטים מרחוק (ROV) או אוטונומיים (AUV). יתרונם הוא שאין סיכון לחיי אדם, הם יכולים לשהות זמן רב יותר בעומק ולשאת מגוון רחב יותר של ציוד. ה-AUVs (כמו זה שאתם בונים) פועלים באופן אוטונומי על בסיס תוכנית שהוגדרה מראש.</li>
    </ul>

    <h3>חיים בעומק: הפתעות באפלה</h3>
    <p>למרות התנאים העוינים, שקע מריאנה אינו ריק מחיים! יצורים חיים בעומק הקיצוני פיתחו הסתגלויות מדהימות כדי לשרוד בסביבה בלתי אפשרית לכאורה:</p>
    <ul>
        <li>**עמידות ללחץ:** מבנה גופם מותאם ללחץ האדיר, לעיתים קרובות על ידי היעדר חללים מלאי גז (כמו שלפוחית ציפה) והרכב כימי מיוחד בתאים המגן על החלבונים.</li>
        <li>**חיים בחשיכה:** רבים עיוורים או מסתמכים על חושים אחרים (כמו חישה כימית או מכנית) כדי למצוא מזון ולהתנייד. חלקם מייצרים אור בעצמם (ביולומינציה) כדי לתקשר או למשוך טרף.</li>
        <li>**מקורות מזון:** רוב המזון מגיע מלמעלה ("שלג ימי" - אורגניזמים מתים ששוקעים). אך קיימות גם מערכות אקולוגיות ייחודיות המבוססות על כימוסינתזה, ניצול אנרגיה כימית הנפלטת מפתחי אוורור בקרקעית.</li>
    </ul>

    <h3>חשיבות חקר שקע מריאנה</h3>
    <p>חקר שקע מריאנה חיוני למספר סיבות:</p>
    <ul>
        <li>**גילויים מדעיים:** גילוי מינים חדשים, הבנת הביולוגיה של סביבות קיצוניות, לימוד תהליכים גיאולוגיים ותנועות לוחות טקטוניים בעומק.</li>
        <li>**פיתוח טכנולוגי:** הצורך ליצור כלים שיכולים לעמוד בתנאים אלה דוחף את גבולות ההנדסה, החומרים והרובוטיקה. טכנולוגיות שפותחו לחקר העומק משמשות גם בתעשיות אחרות.</li>
        <li>**מעקב סביבתי:** הבנת זרמים עמוקים, פיזור חומרים מזהמים (כמו פסולת פלסטיק שכבר נמצאה בעומקים אלה!) ומעקב אחר השפעת שינויי אקלים על המערכות האקולוגיות העמוקות.</li>
    </ul>
    <p>עכשיו תורך לתכנן את המשימה ההיסטורית הבאה אל לב התהום!</p>
</div>

<style>
/* General Styling */
#app-container {
    font-family: 'Arial', sans-serif; /* A common, readable font */
    direction: rtl;
    text-align: right;
    max-width: 900px; /* Slightly wider container */
    margin: 20px auto;
    padding: 30px; /* More padding */
    border-radius: 12px; /* Softer corners */
    background: linear-gradient(to bottom, #e0f7fa, #b2ebf2); /* Light blue gradient */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Softer, deeper shadow */
    color: #333; /* Darker text for readability */
}

h1 {
    color: #004d7a; /* Deep blue */
    text-align: center;
    margin-bottom: 30px;
    font-size: 2em;
}

h2 {
    color: #0077b6; /* Medium blue */
    text-align: right;
    border-bottom: 2px solid #0077b6; /* Underline headings */
    padding-bottom: 10px;
    margin-top: 30px;
    font-size: 1.5em;
}

h3 {
    color: #023e8a; /* Darker blue for category titles */
    margin-top: 0;
    margin-bottom: 15px;
    padding-right: 10px; /* Indent category titles slightly */
    font-size: 1.2em;
}

/* Section Containers */
.section-container {
    margin-bottom: 30px;
    padding: 20px;
    border-radius: 8px;
    background-color: #ffffff; /* White background for sections */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for sections */
}

/* Budget Display */
#budget-display {
    text-align: center; /* Center budget display */
    margin-bottom: 30px;
}

#budget-display h2 {
     color: #1b5e20; /* Dark green */
     text-align: center;
     border-bottom: none;
     margin-bottom: 15px;
}

.budget-value {
    color: #2e7d32; /* Green */
    font-weight: bold;
    font-size: 1.5em;
}

.budget-bar-container {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
    height: 20px;
    margin-top: 10px;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}

.budget-bar {
    height: 100%;
    width: 100%; /* Starts full */
    background-color: #4caf50; /* Green */
    transition: width 0.5s ease-in-out, background-color 0.5s ease-in-out;
    text-align: center;
    line-height: 20px;
    color: white;
    font-size: 0.9em;
}

.budget-bar.warning {
    background-color: #ffc107; /* Amber */
}

.budget-bar.critical {
    background-color: #f44336; /* Red */
}

/* Component Selection */
.component-category .options label {
    display: block;
    margin-bottom: 8px; /* More space between options */
    padding: 12px; /* Padding inside labels */
    border: 1px solid #e0e0e0; /* Light grey border */
    border-radius: 6px;
    background-color: #f8f8f8; /* Off-white background */
    cursor: pointer;
    transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.component-category .options label:hover {
    background-color: #eef; /* Light blue on hover */
    border-color: #c5cae9;
}

.component-category .options label input[type="radio"],
.component-category .options label input[type="checkbox"] {
    margin-left: 10px; /* Space out input */
    vertical-align: middle; /* Align with text */
}

.component-category .options label.selected {
    background-color: #bbdefb; /* Blueish background for selected */
    border-color: #64b5f6; /* Darker blue border */
    box-shadow: 0 0 5px rgba(0, 119, 182, 0.3);
}

.component-stats {
    font-size: 0.9em;
    color: #555;
    margin-right: 10px;
}

/* Icons (simple text-based or unicode) */
.icon-body::before { content: '🛠️ '; }
.icon-power::before { content: '🔋 '; }
.icon-research::before { content: '🔬 '; }
.icon-light::before { content: '💡 '; }
.icon-nav::before { content: '🗺️ '; }
.icon-stats::before { content: '📊 '; }
.icon-mission::before { content: '🎯 '; }
.icon-launch::before { content: '🚀 '; }
.icon-results::before { content: '📋 '; }

/* Current Build Stats */
#current-build-stats p {
    margin-bottom: 8px;
    font-size: 1.1em;
    color: #555;
}

#current-build-stats .stat-value {
    font-weight: bold;
    color: #0056b3;
}

/* Mission Planning */
#mission-planning div {
    margin-bottom: 15px; /* More space between inputs */
}

#mission-planning label {
    display: inline-block;
    margin-left: 15px;
    min-width: 180px; /* Align labels */
    font-size: 1.1em;
    color: #333;
}

#mission-planning input[type="number"] {
    padding: 8px; /* More padding */
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1em;
    width: 100px; /* Fixed width */
    text-align: center;
}

#plan-mission-button {
    display: block;
    width: 100%;
    padding: 12px; /* More padding */
    background-color: #28a745; /* Green */
    color: white;
    border: none;
    border-radius: 6px; /* Rounded corners */
    font-size: 1.3em; /* Larger text */
    cursor: pointer;
    margin-top: 20px;
    transition: background-color 0.3s ease-in-out, transform 0.1s ease;
    font-weight: bold;
}

#plan-mission-button:hover {
    background-color: #218838; /* Darker green on hover */
}

#plan-mission-button:active {
     transform: scale(0.98); /* Button press effect */
}


/* Mission Results */
#mission-results p {
    white-space: pre-wrap; /* Preserve line breaks */
    font-size: 1.1em;
    color: #333;
    line-height: 1.6; /* Better line spacing */
}

#mission-results.success {
    background-color: #e8f5e9; /* Very light green */
    border-color: #4caf50; /* Green border */
    box-shadow: 0 0 8px rgba(76, 175, 80, 0.4); /* Green shadow */
}

#mission-results.failure {
    background-color: #ffebee; /* Very light red */
    border-color: #f44336; /* Red border */
     box-shadow: 0 0 8px rgba(244, 67, 54, 0.4); /* Red shadow */
}

/* Explanation Toggle Button */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* More space above/below */
    padding: 12px 25px;
    background-color: #007bff; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
}

#toggle-explanation:hover {
    background-color: #0056b3; /* Darker blue */
}

/* Explanation Section */
#explanation {
    margin-top: 20px;
    padding: 25px;
    border-radius: 8px;
    background-color: #ffffff; /* White background */
    border: 1px solid #ccc;
    direction: rtl;
    text-align: right;
    line-height: 1.7; /* Improve readability */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

#explanation h2, #explanation h3 {
    color: #0056b3;
    text-align: right;
    border-bottom: 1px dashed #ccc; /* Lighter underline */
    padding-bottom: 5px;
}

#explanation ul {
    list-style-type: disc;
    padding-right: 25px; /* Adjust list padding */
    margin-bottom: 15px;
}

#explanation li {
    margin-bottom: 8px;
}

/* Responsive Adjustments (basic) */
@media (max-width: 768px) {
    #app-container {
        padding: 15px;
    }
    h1 {
        font-size: 1.6em;
    }
    h2 {
        font-size: 1.3em;
    }
    .component-category .options label {
        padding: 10px;
    }
     #mission-planning label {
        display: block;
        margin-left: 0;
        margin-bottom: 5px;
        min-width: auto;
    }
    #mission-planning input[type="number"] {
        width: 100%; /* Full width on small screens */
        box-sizing: border-box; /* Include padding and border in width */
    }
}
</style>

<script>
const componentsData = {
    body: {
        titanium: { name: "גוף טיטניום", cost: 3000000, weight: 800, power: 500, max_depth: 11000, weight_limit: 1200 },
        ceramic: { name: "גוף קרמי", cost: 1500000, weight: 500, power: 300, max_depth: 8000, weight_limit: 800 },
        steel: { name: "גוף פלדה מחוזקת", cost: 800000, weight: 700, power: 400, max_depth: 5000, weight_limit: 700 },
        auv_frame: { name: "שלדת AUV בסיסית", cost: 200000, weight: 100, power: 200, max_depth: 2000, weight_limit: 300 }
    },
    power: {
        large_battery: { name: "סוללות גדולות", cost: 500000, weight: 400, power: 0, max_depth: 11000, capacity_kwh: 100 },
        small_battery: { name: "סוללות קטנות", cost: 200000, weight: 150, power: 0, max_depth: 11000, capacity_kwh: 30 }
    },
    research: { // Checkboxes allow multiple selections
        pressure_camera: { name: "מצלמה עמידת לחץ", cost: 400000, weight: 50, power: 50, max_depth: 11000 },
        high_res_camera: { name: "מצלמה ברזולוציה גבוהה", cost: 250000, weight: 30, power: 40, max_depth: 8000 },
        temp_sensor: { name: "חיישן טמפרטורה", cost: 50000, weight: 5, power: 10, max_depth: 11000 },
        pressure_sensor: { name: "חיישן לחץ", cost: 60000, weight: 5, power: 10, max_depth: 11000 },
        chem_sensor: { name: "חיישני כימיה", cost: 150000, weight: 20, power: 30, max_depth: 10000 },
        sample_arm: { name: "זרוע איסוף דגימות", cost: 700000, weight: 150, power: 100, max_depth: 11000 },
        sonar: { name: "סונאר סריקת צד", cost: 600000, weight: 100, power: 80, max_depth: 7000 }
    },
    lighting: {
        powerful_led: { name: "תאורת LED חזקה", cost: 100000, weight: 15, power: 70, max_depth: 11000 },
        basic_lights: { name: "תאורה בסיסית", cost: 40000, weight: 8, power: 30, max_depth: 6000 }
    },
    navigation: {
        acoustic_nav: { name: "ניווט אקוסטי מתקדם", cost: 300000, weight: 25, power: 20, max_depth: 11000 },
        basic_nav: { name: "ניווט בסיסי", cost: 80000, weight: 10, power: 10, max_depth: 5000 }
    }
};

const startingBudget = 5000000;

function updateStats() {
    let totalCost = 0;
    let totalWeight = 0; // Total weight including body
    let payloadWeight = 0; // Weight of components *excluding* body
    let totalPowerDraw = 0; // in Watts (W)
    let minMaxDepth = 12000; // Start higher than Mariana Trench depth

    const selected = {
        body: null,
        power: null,
        research: [],
        lighting: null,
        navigation: null
    };

    // Clear selection highlights first
    document.querySelectorAll('.component-category .options label').forEach(label => {
        label.classList.remove('selected');
    });


    // Get selected body (radio)
    const selectedBodyInput = document.querySelector('input[name="body"]:checked');
    if (selectedBodyInput) {
        selected.body = componentsData.body[selectedBodyInput.value];
        totalCost += selected.body.cost;
        totalWeight += selected.body.weight;
        totalPowerDraw += selected.body.power;
        minMaxDepth = Math.min(minMaxDepth, selected.body.max_depth);
        // Highlight selected label
        selectedBodyInput.closest('label').classList.add('selected');
    }

    // Get selected power (radio)
    const selectedPowerInput = document.querySelector('input[name="power"]:checked');
    if (selectedPowerInput) {
        selected.power = componentsData.power[selectedPowerInput.value];
        totalCost += selected.power.cost;
        totalWeight += selected.power.weight;
        // Power source itself doesn't draw power from others, it *provides* it.
        // totalPowerDraw += selected.power.power; // This is 0 for power sources in data
        minMaxDepth = Math.min(minMaxDepth, selected.power.max_depth);
        payloadWeight += selected.power.weight; // Power source is part of payload calculation
         // Highlight selected label
        selectedPowerInput.closest('label').classList.add('selected');
    }

    // Get selected research (checkboxes)
    document.querySelectorAll('input[name="research"]:checked').forEach(input => {
        const item = componentsData.research[input.value];
        selected.research.push(item);
        totalCost += item.cost;
        totalWeight += item.weight;
        payloadWeight += item.weight;
        totalPowerDraw += item.power;
        minMaxDepth = Math.min(minMaxDepth, item.max_depth);
         // Highlight selected label
        input.closest('label').classList.add('selected');
    });

    // Get selected lighting (radio)
    const selectedLightingInput = document.querySelector('input[name="lighting"]:checked');
    if (selectedLightingInput) {
        selected.lighting = componentsData.lighting[selectedLightingInput.value];
        totalCost += selected.lighting.cost;
        totalWeight += selected.lighting.weight;
        payloadWeight += selected.lighting.weight;
        totalPowerDraw += selected.lighting.power;
        minMaxDepth = Math.min(minMaxDepth, selected.lighting.max_depth);
         // Highlight selected label
        selectedLightingInput.closest('label').classList.add('selected');
    }

    // Get selected navigation (radio)
    const selectedNavigationInput = document.querySelector('input[name="navigation"]:checked');
    if (selectedNavigationInput) {
        selected.navigation = componentsData.navigation[selectedNavigationInput.value];
        totalCost += selected.navigation.cost;
        totalWeight += selected.navigation.weight;
        payloadWeight += selected.navigation.weight;
        totalPowerDraw += selected.navigation.power;
        minMaxDepth = Math.min(minMaxDepth, selected.navigation.max_depth);
         // Highlight selected label
        selectedNavigationInput.closest('label').classList.add('selected');
    }

    // Update display
    document.getElementById('total-cost').textContent = `$${totalCost.toLocaleString()}`;
    document.getElementById('total-weight').textContent = `${totalWeight.toLocaleString()} ק"ג`;
    document.getElementById('payload-weight').textContent = `${payloadWeight.toLocaleString()} ק"ג`;
    document.getElementById('total-power-draw').textContent = `${totalPowerDraw.toLocaleString()} W`;
    document.getElementById('combined-max-depth').textContent = `${minMaxDepth === 12000 ? 'לא נבחר גוף' : minMaxDepth.toLocaleString() + ' מ\''}`; // Show something if no body selected

    const remainingBudget = startingBudget - totalCost;
    document.getElementById('current-budget').textContent = `$${remainingBudget.toLocaleString()}`;

    // Update budget bar
    const budgetBar = document.getElementById('budget-bar');
    const budgetPercent = Math.max(0, Math.min(100, (remainingBudget / startingBudget) * 100));
    budgetBar.style.width = budgetPercent + '%';

    // Change budget bar color based on remaining budget
    budgetBar.classList.remove('warning', 'critical');
    if (remainingBudget < 0) {
        budgetBar.classList.add('critical');
         budgetBar.textContent = 'חריגה מתקציב!';
         budgetBar.style.width = '100%'; // Show full bar in red on critical
    } else if (remainingBudget < startingBudget * 0.2) { // Less than 20% remaining
         budgetBar.classList.add('warning');
         budgetBar.textContent = `${budgetPercent.toFixed(0)}% נותר`;
    } else {
         budgetBar.style.backgroundColor = '#4caf50'; // Ensure it's green if not warning/critical
         budgetBar.textContent = `${budgetPercent.toFixed(0)}% נותר`;
    }


    // Store current selected components data for mission planning
    document.getElementById('plan-mission-button').dataset.selectedComponents = JSON.stringify(selected);
    document.getElementById('plan-mission-button').dataset.currentStats = JSON.stringify({
        totalCost,
        totalWeight,
        payloadWeight,
        totalPowerDraw,
        minMaxDepth: (minMaxDepth === 12000 ? 0 : minMaxDepth) // Store 0 if no body selected
    });
}

function planMission() {
    const selected = JSON.parse(document.getElementById('plan-mission-button').dataset.selectedComponents || '{}');
    const currentStats = JSON.parse(document.getElementById('plan-mission-button').dataset.currentStats || '{}');

    const missionDepth = parseInt(document.getElementById('mission-depth').value, 10);
    const missionDuration = parseInt(document.getElementById('mission-duration').value, 10);

    const resultsDiv = document.getElementById('mission-results');
    resultsDiv.classList.remove('success', 'failure');
    let resultsText = "";
    let success = true;
    let issues = [];

    // --- Validation Checks ---

    // Basic checks - require body and power source selected
    if (!selected.body) {
        issues.push("- לא נבחר גוף לכלי המחקר. חובה לבחור מבנה גוף!");
        success = false;
    }
    if (!selected.power) {
         issues.push("- לא נבחר מקור כוח לכלי המחקר. חובה לצייד את החללית במנוע לב!");
         success = false;
    }

     // If basic components are missing, report and stop
     if (!selected.body || !selected.power) {
          document.getElementById('results-text').textContent = "🚫 שגיאת הרכבה:\n" + issues.join("\n");
          resultsDiv.classList.add('failure');
          return;
     }


    // 1. Budget check
    if (currentStats.totalCost > startingBudget) {
        issues.push(`- חריגה מהתקציב. עלות ההרכבה: $${currentStats.totalCost.toLocaleString()}, התקציב שלך: $${startingBudget.toLocaleString()}.`);
        success = false;
    }

    // 2. Depth check
    if (missionDepth > currentStats.minMaxDepth) {
         // Find components that limit the depth
         let limitingComponents = [];
         if(selected.body && selected.body.max_depth < missionDepth) limitingComponents.push(selected.body.name);
         if(selected.power && selected.power.max_depth < missionDepth) limitingComponents.push(selected.power.name);
         selected.research.forEach(item => {
             if (item.max_depth < missionDepth) limitingComponents.push(item.name);
         });
         if(selected.lighting && selected.lighting.max_depth < missionDepth) limitingComponents.push(selected.lighting.name);
         if(selected.navigation && selected.navigation.max_depth < missionDepth) limitingComponents.push(selected.navigation.name);

          // Remove duplicates and list them
         limitingComponents = [...new Set(limitingComponents)].join(", ");

         issues.push(`- עומק המשימה המתוכנן (${missionDepth} מ') עמוק מדי! הוא חורג מהעומק המקסימלי שהרכיבים שבחרת עומדים בו (${currentStats.minMaxDepth} מ'). הרכיבים המגבילים הם: ${limitingComponents}.`);
         success = false;
     }


    // 3. Weight check
    const totalPayloadWeight = currentStats.payloadWeight; // Components excluding body
    const bodyWeightLimit = selected.body.weight_limit; // The body has its own weight + capacity for payload

    if (totalPayloadWeight > bodyWeightLimit) {
         issues.push(`- משקל הציוד שהרכבת (${totalPayloadWeight} ק"ג) כבד מדי עבור הגוף הנבחר (${selected.body.name} בעל כושר נשיאה של ${bodyWeightLimit} ק"ג בלבד).`);
        success = false;
    }

    // 4. Power check (energy capacity)
    const totalPowerWatts = currentStats.totalPowerDraw; // in Watts
    const totalPowerKW = totalPowerWatts / 1000; // in Kilowatts
    const requiredEnergyKWH = totalPowerKW * missionDuration; // in Kilowatt-hours

    if (requiredEnergyKWH > selected.power.capacity_kwh) {
        issues.push(`- מקור הכוח הנבחר (${selected.power.name}) אינו מספק אנרגיה מספקת למשך המשימה (${missionDuration} שעות).`);
        issues.push(`  צריכת אנרגיה כוללת להספק הנוכחי: ${requiredEnergyKWH.toFixed(2)} קוט"ש. קיבולת מקור הכוח: ${selected.power.capacity_kwh} קוט"ש.`);
        success = false;
    }

     // --- Results Generation ---

    if (success) {
        let capabilitiesList = selected.research.map(item => item.name);
        if(selected.lighting) capabilitiesList.push(selected.lighting.name);
        if(selected.navigation) capabilitiesList.push(selected.navigation.name);

        let capabilities = capabilitiesList.length > 0 ? capabilitiesList.join(", ") : "ללא ציוד מחקר ייעודי";


        resultsText = "🎉 הצלחה! תכנון המשימה מאושר! 🎉\n\n";
        resultsText += `חללית העומק שלך מוכנה למסע אל הלא נודע!\n`;
        resultsText += `\n**סיכום ההרכבה:**\n`;
        resultsText += `- גוף: ${selected.body.name}\n`;
        resultsText += `- מקור כוח: ${selected.power.name}\n`;
        resultsText += `- ציוד מדעי: ${capabilities}\n`;
        resultsText += `\n**נתונים טכניים של החללית:**\n`;
        resultsText += `- עלות כוללת: $${currentStats.totalCost.toLocaleString()}\n`;
        resultsText += `- משקל כולל: ${currentStats.totalWeight.toLocaleString()} ק"ג\n`;
        resultsText += `- צריכת כוח בהפעלה: ${currentStats.totalPowerDraw.toLocaleString()} W\n`;
        resultsText += `- עומק מקסימלי תיאורטי (לפי רכיבים): ${currentStats.minMaxDepth.toLocaleString()} מ'\n`;
        resultsText += `\n**יעד המשימה:**\n`;
        resultsText += `- עומק מתוכנן: ${missionDepth.toLocaleString()} מ'\n`;
        resultsText += `- משך מתוכנן: ${missionDuration.toLocaleString()} שעות\n`;
        resultsText += `\n**תוכנית הפעלה:**\n`;
        resultsText += `החללית תצלול לעומק ${missionDepth.toLocaleString()} מ' ותבצע מחקרים באמצעות ${capabilities} למשך ${missionDuration.toLocaleString()} שעות. צפו לגילויים מרעישים!\n`;

        resultsDiv.classList.add('success');

    } else {
         resultsText = "😢 המשימה נכשלה בשלב התכנון.\n\n";
         resultsText += "החללית אינה עומדת בדרישות המשימה או התקציב עקב הבעיות הבאות:\n";
         resultsText += issues.join("\n");
         resultsText += "\n\nאנא חזור לבחירת הרכיבים ושנה את ההרכבה או את יעד המשימה כדי לנסות שוב.";

         resultsDiv.classList.add('failure');
    }

    document.getElementById('results-text').textContent = resultsText;
}

// Add event listeners to all relevant inputs
document.querySelectorAll('#components-selection input').forEach(input => {
    input.addEventListener('change', updateStats);
});

// Add event listener to the plan mission button
document.getElementById('plan-mission-button').addEventListener('click', planMission);

// Initial stats update on page load
updateStats();

// Toggle explanation
document.getElementById('toggle-explanation').addEventListener('click', function() {
    const explanationDiv = document.getElementById('explanation');
    const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
    if (isHidden) {
        explanationDiv.style.display = 'block';
        this.textContent = 'הסתר הסבר על חקר שקע מריאנה';
    } else {
        explanationDiv.style.display = 'none';
        this.textContent = 'הצג/הסתר הסבר על חקר שקע מריאנה והתנאים בתהום';
    }
});

</script>
```