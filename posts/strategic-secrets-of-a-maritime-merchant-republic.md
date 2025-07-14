---
title: "האימפריה הנסתרת: אסטרטגיית ההצלחה של רפובליקת סוחרים ימית"
english_slug: strategic-secrets-of-a-maritime-merchant-republic
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - רפובליקה מסחרית
  - ונציה
  - ג'נובה
  - מסחר
  - אסטרטגיה
  - היסטוריה כלכלית
  - סימולציה
  - ימי הביניים
  - רנסנס
---

# האימפריה הנסתרת: אסטרטגיית ההצלחה של רפובליקת סוחרים ימית

מערי-מדינה קטנות וצנועות בחוף הים האדריאטי או הליגורי, צמחו ישויות אדירות כונציה וג'נובה. כיצד הצליחו רפובליקות סוחרים אלו לצבור עושר אגדי, לבסס שליטה ימית חסרת תקדים ולהפוך לשחקניות מפתח בזירה הבינלאומית של ימי הביניים והרנסנס? האם הכוח נבע רק מעוצמת הצי, או שמא סוד ההצלחה טמון באסטרטגיות ניהול פיננסיות, דיפלומטיות וצבאיות מתוחכמות?

היכנסו לנעלי הדוג'ה (ראש הרפובליקה) וגלו בעצמכם את האתגרים וההזדמנויות!

<div id="app">
    <div class="game-container">
        <div class="status-panel card">
            <h2>מצב הרפובליקה</h2>
            <p>שנה: <span id="current-year" class="status-value">1</span></p>
            <p>קופה: <span id="money" class="status-value">10000</span> דוקאטים</p>
            <p>אוניות סוחר זמינות: <span id="merchant-ships" class="status-value">10</span></p>
            <p>אוניות מלחמה זמינות: <span id="war-ships" class="status-value">2</span></p>
            <p>סיכון ימי ממוצע: <span id="risk-level" class="status-value">נמוכה</span></p>
        </div>

        <div class="map-area card">
            <h2>מפת הים התיכון</h2>
            <div class="map-representation">
                <p class="map-title">מרכזי סחר ונתיבים עיקריים:</p>
                <ul>
                    <li><span class="city-name">ונציה</span> (הבסיס שלך)</li>
                    <li><span class="city-name">אלכסנדריה</span> (מצרים - תבלינים, משי)</li>
                    <li><span class="city-name">קונסטנטינופול</span> (האימפריה הביזנטית - משי, זהב)</li>
                    <li><span class="city-name">עכו</span> (ממלכת ירושלים/ערי סהר פורה - תבלינים, אבני חן)</li>
                    <li class="rival"><span class="city-name">ג'נובה</span> (מתחרה קשוחה!)</li>
                </ul>
                 <p class="map-info">נתיבים פעילים:</p>
                 <ul id="active-routes">
                    <li>ונציה ➔ אלכסנדריה</li>
                    <li>ונציה ➔ קונסטנטינופול</li>
                    <li>ונציה ➔ עכו</li>
                 </ul>
                 <p class="map-info">סחורות מאירופה (ייצוא): זכוכית מוראנו, בדי צמר/פשתן איכותיים.</p>
                 <p class="map-info">סחורות מהמזרח (ייבוא): תבלינים אקזוטיים, משי יוקרתי.</p>
                 <p class="map-info">**מטרתך:** להפוך את הרפובליקה שלך לעשירה והחזקה בים התיכון!</p>
                 <div id="map-visual-feedback">
                     <!-- Dynamic visual feedback will be added here -->
                 </div>
            </div>
        </div>

        <div class="controls-panel card">
            <h2>החלטות לשנה זו</h2>
            <div class="decision-block">
                <h3>ניהול צי הסוחר</h3>
                <p>בחר יעד למסע סחר יחיד (הכי משתלם? הכי בטוח?):</p>
                <select id="trade-route" class="styled-select">
                    <option value="venice-alexandria">ונציה ➔ אלכסנדריה</option>
                    <option value="venice-constantinople">ונציה ➔ קונסטנטינופול</option>
                    <option value="venice-acre">ונציה ➔ עכו</option>
                </select>
                 <p>קנה בונציה (הוצאה): <span id="buy-goods-price"></span> דוקאטים ליחידה</p>
                 <select id="buy-goods" class="styled-select">
                    <option value="glass">זכוכית (ייצוא)</option>
                    <option value="textiles">בדים (ייצוא)</option>
                </select>
                 <p>מכור ביעד (הכנסה פוטנציאלית): <span id="sell-goods-price"></span> דוקאטים ליחידה</p>
                 <select id="sell-goods" class="styled-select">
                    <option value="spices">תבלינים (ייבוא)</option>
                    <option value="silk">משי (ייבוא)</option>
                </select>
                <p>מספר אוניות סוחר להקצאה לנתיב זה (מתוך <span id="available-merchant-ships">10</span>):</p>
                <input type="number" id="allocate-merchant-ships" value="0" min="0" class="styled-input">
                <p class="allocation-feedback" id="merchant-allocation-feedback"></p>
            </div>

             <div class="decision-block">
                <h3>הגנה ימית (אופציונלי)</h3>
                 <p>הקצא אוניות מלחמה להגנה על הנתיב הנבחר (מתוך <span id="available-war-ships">2</span>):</p>
                <input type="number" id="allocate-war-ships" value="0" min="0" class="styled-input">
                 <p class="allocation-feedback" id="war-allocation-feedback"></p>
            </div>

            <div class="decision-block">
                <h3>השקעות עתידיות</h3>
                 <p>כל השקעה עולה <span class="investment-cost">1000</span> דוקאטים.</p>
                <button id="invest-merchant-ship" class="styled-button invest-button">בנה אוניית סוחר (+1)</button>
                <button id="invest-war-ship" class="styled-button invest-button">בנה אוניית מלחמה (+1)</button>
            </div>

            <button id="next-round-button" class="styled-button primary-button">סיום שנה והתקדמות</button>
        </div>

        <div class="feedback-area card">
            <h2>יומן אירועים ימי</h2>
            <ul id="event-log">
                <li class="event-item initial">השנה החלה. קבל החלטות אסטרטגיות ראשונות!</li>
            </ul>
        </div>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Hebrew:wght@400;700&display=swap');

    #app {
        font-family: 'Noto Sans Hebrew', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 1100px; /* Slightly wider */
        margin: 20px auto;
        background-color: #f4f0e8; /* Parchment background */
        color: #333;
        border: 1px solid #c0b29e; /* Earthy border */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        padding: 20px;
        border-radius: 12px;
        overflow: hidden; /* For potential animations */
    }

    .game-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto 1fr; /* Status, Controls, Log */
        gap: 25px; /* Increased gap */
    }

    .card {
        background-color: #ffffff; /* White card background */
        border: 1px solid #ddd; /* Light grey border */
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Soft card shadow */
    }

    .status-panel {
        grid-column: 1 / 2;
        grid-row: 1 / 2;
        background-color: #e9f5ee; /* Light green for status */
        border-color: #d0e9c6;
    }

    .status-panel h2 {
        color: #2a7a47; /* Dark green */
        border-bottom: 2px solid #4CAF50; /* Green border */
        padding-bottom: 8px;
        margin-top: 0;
    }

    .status-panel p {
        margin-bottom: 8px;
        font-size: 1.1em;
    }

    .status-value {
        font-weight: bold;
        color: #0056b3; /* Blue for values */
         transition: color 0.5s ease, transform 0.3s ease; /* Smooth transition */
         display: inline-block; /* Allow transform */
    }

    .map-area {
        grid-column: 2 / 3;
        grid-row: 1 / 3; /* Map spans status and controls rows */
        background-color: #eef7ff; /* Light blue for map */
        border-color: #cce7ff;
        display: flex;
        flex-direction: column; /* Arrange map content vertically */
    }

    .map-area h2 {
        color: #0056b3; /* Dark blue */
        border-bottom: 2px solid #007bff; /* Blue border */
        padding-bottom: 8px;
        margin-top: 0;
    }

    .map-representation {
        margin-top: 15px;
        padding: 15px;
        border: 2px dashed #a0c0d0; /* Dashed blue border */
        background-color: #f8ffff; /* Very light blue */
        border-radius: 5px;
        flex-grow: 1; /* Allow map content to fill space */
        position: relative; /* For absolute positioning of feedback */
    }

     .map-representation ul {
         list-style: none;
         padding: 0;
         margin-bottom: 10px;
     }

    .map-representation li {
        margin-bottom: 5px;
    }

    .map-title {
        font-weight: bold;
        margin-bottom: 10px;
        color: #555;
    }

    .map-info {
         font-size: 0.95em;
         color: #666;
         margin-bottom: 5px;
    }

    .city-name {
        font-weight: bold;
        color: #007bff; /* Blue for city names */
    }

     .city-name.rival {
         color: #dc3545; /* Red for rival */
     }

     #map-visual-feedback {
         position: absolute;
         bottom: 15px;
         left: 15px;
         right: 15px;
         padding: 10px;
         background-color: rgba(255, 255, 255, 0.8);
         border: 1px solid #ccc;
         border-radius: 5px;
         font-size: 0.9em;
         color: #333;
         display: none; /* Hidden by default */
     }


    .controls-panel {
        grid-column: 1 / 2;
        grid-row: 2 / 3;
        background-color: #fdf8e1; /* Light yellow for controls */
        border-color: #faeec8;
    }

    .controls-panel h2 {
        color: #b38f00; /* Dark yellow/brown */
        border-bottom: 2px solid #ffc107; /* Yellow border */
        padding-bottom: 8px;
        margin-top: 0;
    }

    .decision-block {
        margin-bottom: 20px; /* Increased space */
        padding: 15px;
        border: 1px solid #ffeeba; /* Light yellow border */
        border-radius: 8px;
        background-color: #fffaf0; /* Very light yellow */
    }

    .decision-block h3 {
        margin-top: 0;
        margin-bottom: 12px;
        border-bottom: 1px dashed #ffda6a; /* Dashed yellow */
        padding-bottom: 6px;
        color: #a16e00; /* Brown */
    }

    .styled-select, .styled-input {
        margin-top: 8px; /* More space */
        padding: 10px; /* More padding */
        border: 1px solid #ccc;
        border-radius: 5px; /* Rounded corners */
        font-size: 1em;
        width: calc(100% - 22px); /* Adjust for padding/border */
        box-sizing: border-box; /* Include padding/border in width */
        background-color: #fff;
    }

    .styled-button {
        margin-top: 10px;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

     .styled-button:hover {
         transform: translateY(-1px); /* Slight lift on hover */
     }
     .styled-button:active {
         transform: translateY(0); /* Press effect */
     }

    .invest-button {
        background-color: #28a745; /* Green */
        color: white;
        margin-left: 10px;
    }
     .invest-button:hover {
         background-color: #218838;
     }


     .primary-button {
        display: block;
        width: 100%;
        padding: 15px; /* Larger padding */
        margin-top: 25px; /* More space */
        font-size: 1.2em; /* Larger text */
        background-color: #007bff; /* Blue */
        color: white;
        font-weight: bold;
     }
     .primary-button:hover {
         background-color: #0056b3;
     }
      .primary-button:disabled {
          background-color: #cccccc;
          cursor: not-allowed;
      }

    .allocation-feedback {
        font-size: 0.9em;
        color: #666;
        margin-top: 5px;
    }


    .feedback-area {
        grid-column: 1 / 3; /* Spans both columns */
        grid-row: 3 / 4;
        background-color: #fff0f0; /* Light red/pink for events */
        border-color: #ffe5e5;
        max-height: 250px; /* Increased height */
        overflow-y: auto; /* Add scroll */
         display: flex;
         flex-direction: column;
    }
    .feedback-area h2 {
         color: #cc0000; /* Red */
         border-bottom: 2px solid #dc3545; /* Red border */
         padding-bottom: 8px;
         margin-top: 0;
    }

    #event-log {
        list-style: none;
        padding: 0;
        margin: 0;
        flex-grow: 1;
    }
    .event-item { /* Class for log items */
        margin-bottom: 8px;
        padding: 8px;
        border-bottom: 1px dashed #ffc0c0; /* Light red dashed */
        background-color: #fff; /* White background for items */
        border-radius: 4px;
        font-size: 0.95em;
         opacity: 0; /* Start hidden for animation */
         transform: translateY(10px); /* Start slightly lower */
         animation: fadeInLog 0.5s ease-out forwards; /* Animation */
    }
     .event-item.initial { /* Style for the first item */
         opacity: 1;
         transform: none;
         animation: none;
         background-color: #e9f5ee;
         border-color: #d0e9c6;
     }

    @keyframes fadeInLog {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

     /* Specific log entry styles (optional, based on content) */
     .event-item.profit { color: #28a745; font-weight: bold; }
     .event-item.loss { color: #dc3545; font-weight: bold; }
     .event-item.investment { color: #007bff; }
     .event-item.neutral { color: #333; }


    #showExplanationButton {
        display: block;
        margin: 25px auto; /* Centered below game */
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #6c757d; /* Grey */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Noto Sans Hebrew', sans-serif; /* Match game font */
    }
    #showExplanationButton:hover {
        background-color: #5a6268;
         transform: translateY(-1px);
    }

    #explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #c0b29e;
        border-radius: 12px;
        background-color: #fdfbf6; /* Lighter parchment */
        direction: rtl;
        text-align: right;
        color: #333;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    #explanation h2 {
        color: #8a6a4f; /* Brownish */
        border-bottom: 2px solid #d4c0a9;
        padding-bottom: 8px;
        margin-top: 20px;
    }
     #explanation h3 {
        color: #a16e00; /* Darker yellow/brown */
        margin-top: 15px;
        margin-bottom: 10px;
     }
    #explanation p {
        line-height: 1.7; /* Improved readability */
        margin-bottom: 15px;
        color: #444;
    }
</style>

<button id="showExplanationButton">הצג הסבר על רפובליקות הסוחרים וסודותיהן</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מורחב: עולמן של רפובליקות הסוחרים הימיות</h2>

    <h3>מי היו ערי-המדינה ששלטו בים התיכון?</h3>
    <p>במאות העשירית עד החמש עשרה לספירה, ערי חוף איטלקיות כמו ונציה, ג'נובה, פיזה ואמאלפי פרחו והפכו למרכזים כלכליים ופוליטיים עצמאיים - הן "הרפובליקות הימיות" (Repubbliche Marinare). הן לא היו ממלכות שנשלטו על ידי אצולה פיאודלית, אלא ישויות ייחודיות שנשלטו לרוב על ידי אוליגרכיות של סוחרים ואנשי צי. ערי-מדינה אלו ניצלו בחוכמה את מיקומן הגאוגרפי המצוין, כגשר בין אירופה התוססת לשווקים העשירים של המזרח (האימפריה הביזנטית, העולם המוסלמי והלבנט הצלבני/ממלוכי).</p>

    <h3>עושר מן הים: סחר, נתיבים, ומונופולים.</h3>
    <p>הבסיס הכלכלי לכוחן היה טמון בשליטתן בנתיבי הסחר הימיים הרווחיים ביותר. אוניותיהן הובילו סחורות יוקרתיות מהמזרח - תבלינים כמו פלפל, קינמון וג'ינג'ר ששימשו לתיבול מזון, רפואה ובשמים; משי יקר ערך; אבני חן; ואף סוכר - אל השווקים באירופה, שם נמכרו במחירים מופקעים. בכיוון ההפוך, הן ייצאו מאירופה מוצרים כמו בדי צמר ופשתן, מתכות, עץ לבנייה, וכלי זכוכית מפוארים שנוצרו בבתי המלאכה שלהן (ונציה התפרסמה במיוחד בזכוכית מוראנו). כדי להבטיח את רווחיותם, הן שאפו להשיג מונופולים וזכויות סחר בלעדיות באמצעות הסכמים דיפלומטיים ולעיתים קרובות בכוח הזרוע, תוך דיכוי מתחרים (כמו המלחמות הארוכות בין ונציה לג'נובה על השליטה בנתיבי הים השחור והמזרח התיכון).</p>

    <h3>לא רק אוניות: יזמות פיננסית וארגונית.</h3>
    <p>הרפובליקות הימיות היו חממות לפיתוחים כלכליים ופיננסיים שקדמו לבנקאות המודרנית. הן פיתחו שיטות בנקאות (פיקדונות, הלוואות, העברות כספים בין סניפים), השתמשו בשטרות חליפין שהקטינו את הסיכון שבהובלת מטבעות פיזיים, ושכללו את הנהלת החשבונות (שיטת הרישום הכפול). מבנים ארגוניים כמו ה-"commenda" (הסכם השקעה קצר מועד) וה-"maona" (חברת מניות ארוכת טווח בג'נובה) אפשרו גיוס הון בקנה מידה גדול ופיזור סיכונים. הן בנו מספנות ענק (כמו הארסנלה בונציה) שיכלו לבנות ולהצטייד אוניות בקצב מסחרר, מה שאפשר להן לתחזק ציים מסחריים וצבאיים כאחד.</p>

    <h3>אסטרטגיה רב-שכבתית: דיפלומטיה, צבא, וניהול סיכונים.</h3>
    <p>הצלחתן של הרפובליקות נשענה על אסטרטגיה מורכבת שחרגה מעבר למסחר גרידא. היא כללה:
    <ul>
        <li>**דיפלומטיה ערמומית:** כריתת בריתות משתנות עם מעצמות אזוריות (האימפריה הביזנטית, המمالוכים במצרים, הח'ליפויות בצפון אפריקה, הממלכות הצלבניות, האימפריה המונגולית) כדי להשיג זכויות סחר והגנה. הקמת רשת של קונסוליות ונציגויות סחר בערים זרות.</li>
        <li>**עוצמה צבאית ימית:** החזקת ציי מלחמה חזקים לא רק להגנה מפני פיראטים (בעיה אקוטית בים התיכון), אלא גם כאמצעי כפייה דיפלומטי וכוח תקיפה לכיבוש נקודות אסטרטגיות. ה"גליאה" (Galley) המהירה והחמושה הייתה עמוד השדרה של ציים אלו.</li>
        <li>**ניהול סיכונים:** פיזור השקעות על פני מספר אוניות ונתיבים, פיתוח מנגנונים דמויי ביטוח ימי, ותחזוקת מלאי סחורות.</li>
        <li>**השקעה בתשתיות:** שיפור נמלים, מספנות, ובניית אוניות גדולות ויעילות יותר.</li>
    </ul>
    היכולת לשלב את כל אלו - מסחר, פיננסים, דיפלומטיה וכוח צבאי - היא שהפכה אותן למעצמות זעירות אך אדירות.</p>

    <h3>אתגרים ודעיכה: סערות היסטוריות.</h3>
    <p>לצד ההצלחות, הרפובליקות התמודדו עם אתגרים אדירים: מלחמות בלתי פוסקות ביניהן לבין עצמן ועם כוחות ימיים אחרים, פיראטיות שמעולם לא נעלמה לגמרי, מגפות קשות (המוות השחור במאה ה-14 קטל חלק ניכר מהאוכלוסייה ושיבש את הסחר), ושינויים גאו-פוליטיים דרמטיים. עליית האימפריה העות'מאנית ושליטתה ההולכת וגוברת במזרח הים התיכון במאות ה-14 וה-15 חסמה בהדרגה נתיבי סחר מסורתיים. לבסוף, "עידן התגליות" בסוף המאה ה-15, שהוביל לגילוי אמריקה ולפתיחת נתיב ימי ישיר להודו דרך כף התקווה הטובה (על ידי פורטוגל), הסטה את מרכז הכובד של הסחר העולמי מהים התיכון לאוקיינוס האטלנטי, וגרם לשקיעתן ההדרגתית ככוחות מובילים, אם כי ונציה המשיכה להיות מרכז תרבותי וכלכלי חשוב עוד מאות שנים.</p>

    <h3>מורשת לעולם המודרני.</h3>
    <p>מורשתן של רפובליקות הסוחרים חיה וקיימת. הן היו חלוצות בקפיטליזם, בבנקאות, בביטוח, בדיני ים, ובניהול עסקאות בינלאומיות מורכבות. סיפורן מדגים את הכוח הטמון בשילוב של יזמות כלכלית, חדשנות פיננסית, אסטרטגיה רב-כיוונית, ויכולת הסתגלות מול אתגרים.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const state = {
            year: 1,
            money: 10000,
            merchantShips: 10,
            warShips: 2,
            baseRisk: 0.1, // Overall economic/political climate risk
            routeDetails: {
                'venice-alexandria': { risk: 0.15, travelTime: 2, destination: 'אלכסנדריה' },
                'venice-constantinople': { risk: 0.1, travelTime: 3, destination: 'קונסטנטינופול' },
                'venice-acre': { risk: 0.2, travelTime: 2, destination: 'עכו' },
            },
             // Initial prices (can fluctuate)
            prices: {
                venice: { glass: 100, textiles: 80 },
                alexandria: { spices: 200, silk: 250 },
                constantinople: { spices: 180, silk: 230 },
                acre: { spices: 190, silk: 240 },
            },
            investmentCost: 1000,
            allocatedMerchantShips: 0,
            allocatedWarShips: 0,
            selectedRoute: 'venice-alexandria',
            buyGoods: 'glass',
            sellGoods: 'spices',
        };

        const els = {
            year: document.getElementById('current-year'),
            money: document.getElementById('money'),
            merchantShips: document.getElementById('merchant-ships'),
            warShips: document.getElementById('war-ships'),
            riskLevel: document.getElementById('risk-level'),
            tradeRouteSelect: document.getElementById('trade-route'),
            buyGoodsSelect: document.getElementById('buy-goods'),
            sellGoodsSelect: document.getElementById('sell-goods'),
            buyGoodsPriceSpan: document.getElementById('buy-goods-price'),
            sellGoodsPriceSpan: document.getElementById('sell-goods-price'),
            allocateMerchantInput: document.getElementById('allocate-merchant-ships'),
            allocateWarInput: document.getElementById('allocate-war-ships'),
            availableMerchantShipsSpan: document.getElementById('available-merchant-ships'),
            availableWarShipsSpan: document.getElementById('available-war-ships'),
            merchantAllocationFeedback: document.getElementById('merchant-allocation-feedback'),
            warAllocationFeedback: document.getElementById('war-allocation-feedback'),
            investMerchantBtn: document.getElementById('invest-merchant-ship'),
            investWarBtn: document.getElementById('invest-war-ship'),
            nextRoundBtn: document.getElementById('next-round-button'),
            eventLog: document.getElementById('event-log'),
            showExplanationBtn: document.getElementById('showExplanationButton'),
            explanationDiv: document.getElementById('explanation'),
             mapVisualFeedback: document.getElementById('map-visual-feedback'),
        };

         // --- Helper Functions ---
        function formatMoney(amount) {
             // Add a class for positive/negative numbers
             const span = document.createElement('span');
             span.textContent = Math.round(amount).toLocaleString(); // Format with commas
             if (amount > 0) span.classList.add('profit-value');
             else if (amount < 0) span.classList.add('loss-value');
             return span.outerHTML;
         }


         function getRiskText(risk) {
            if (risk < 0.15) return 'נמוכה';
            if (risk < 0.25) return 'בינונית';
            return 'גבוהה';
        }

        function updateUI() {
            els.year.textContent = state.year;
            els.money.innerHTML = formatMoney(state.money); // Use innerHTML for formatting
            els.merchantShips.textContent = state.merchantShips - state.allocatedMerchantShips; // Show available
            els.warShips.textContent = state.warShips - state.allocatedWarShips; // Show available
            els.availableMerchantShipsSpan.textContent = state.merchantShips; // Show total
            els.availableWarShipsSpan.textContent = state.warShips; // Show total
            els.riskLevel.textContent = getRiskText(state.baseRisk + state.routeDetails[state.selectedRoute].risk);

            // Update input max values based on available ships
            els.allocateMerchantInput.max = state.merchantShips;
            els.allocateWarInput.max = state.warShips;

            // Update price displays
             els.buyGoodsPriceSpan.textContent = Math.round(state.prices.venice[state.buyGoods]);
             const destination = state.selectedRoute.split('-')[1];
             els.sellGoodsPriceSpan.textContent = Math.round(state.prices[destination][state.sellGoods]);

            // Allocation feedback
            els.merchantAllocationFeedback.textContent = `(נותרו: ${state.merchantShips - state.allocatedMerchantShips})`;
            els.warAllocationFeedback.textContent = `(נותרו: ${state.warShips - state.allocatedWarShips})`;

             // Disable invest buttons if not enough money
             els.investMerchantBtn.disabled = state.money < state.investmentCost;
             els.investWarBtn.disabled = state.money < state.investmentCost;

             // Disable next round button if no merchant ships allocated
             els.nextRoundBtn.disabled = state.allocatedMerchantShips === 0;
        }

        function addEvent(text, type = 'neutral') {
            const li = document.createElement('li');
            li.textContent = `[שנה ${state.year}] ${text}`;
             li.classList.add('event-item', type); // Add base class and type class
            els.eventLog.prepend(li); // Add to the top

             // Optional: limit log size
             while (els.eventLog.children.length > 25) { // Keep more history
                 els.eventLog.removeChild(els.eventLog.lastChild);
             }
             // Trigger CSS animation for the new item
             setTimeout(() => {
                 li.style.opacity = 1;
                 li.style.transform = 'translateY(0)';
             }, 10); // Small delay to allow display property update
        }

        function calculateTradeOutcome() {
            const routeKey = state.selectedRoute;
            const route = state.routeDetails[routeKey];
            const numShips = state.allocatedMerchantShips;
            const numWarShips = state.allocatedWarShips;

            if (numShips === 0) {
                addEvent("לא הוקצו אוניות סוחר למסע השנה.", 'neutral');
                return 0;
            }
             if (numShips > state.merchantShips) {
                 addEvent("שגיאה: הוקצו יותר אוניות סוחר מזמינות.", 'loss');
                 return 0; // Should be prevented by max attribute, but good fallback
             }
              if (numWarShips > state.warShips) {
                 addEvent("שגיאה: הוקצו יותר אוניות מלחמה מזמינות.", 'loss');
                 return 0; // Should be prevented by max attribute
             }


            // Simplified: Each ship carries 1 unit of buy goods and 1 unit of sell goods
            const unitsTraded = numShips;
            const buyPrice = state.prices.venice[state.buyGoods];
            const destination = routeKey.split('-')[1];
            const sellPrice = state.prices[destination][state.sellGoods];

            const cost = unitsTraded * buyPrice;
            let potentialRevenue = unitsTraded * sellPrice;
            let revenue = potentialRevenue;
            let profit = 0;

            // --- Risk Calculation ---
            let effectiveRisk = state.baseRisk + route.risk;
            const protectionBonus = numWarShips * 0.08; // Each war ship provides protection
             effectiveRisk = Math.max(0, effectiveRisk - protectionBonus); // Risk is reduced by war ships

             const randomRiskFactor = Math.random(); // 0 to 1

             // Simulate different risk events based on effective risk
             let eventText = "מסע הסחר עבר בשלום.";
             let eventType = 'neutral';

             if (randomRiskFactor < effectiveRisk) { // Risk event occurs
                 const eventSeverity = Math.random(); // How bad is the event?

                 if (eventSeverity < 0.4) { // Minor event (Storm, petty pirates)
                     const lossFactor = Math.random() * 0.2 + 0.05; // Lose 5% to 25% of potential revenue
                     const lossAmount = potentialRevenue * lossFactor;
                     revenue -= lossAmount;
                     revenue = Math.max(0, revenue);
                     eventText = `נתיב הים סוער! סערה או פיראטים קטנים גרמו נזק. הפסד של כ-${Math.round(lossAmount)} דוקאטים.`;
                     eventType = 'loss';
                 } else if (eventSeverity < 0.8) { // Moderate event (Attack by rival, larger pirate fleet)
                      // War ships can mitigate this
                      if (numWarShips > 0 && Math.random() > (numWarShips * 0.3)) { // War ships might fight them off
                           const lossFactor = Math.random() * 0.3 + 0.1; // Reduced loss
                           const lossAmount = potentialRevenue * lossFactor;
                           revenue -= lossAmount;
                           revenue = Math.max(0, revenue);
                           eventText = `נתקלת בצי מתחרה/פיראטים! אוניות המלחמה סייעו בהגנה, אך נגרמו הפסדים. הפסד של כ-${Math.round(lossAmount)} דוקאטים.`;
                           eventType = 'loss';
                      } else if (numWarShips === 0 || Math.random() < (0.7 / numWarShips)) { // No war ships or defense failed
                           const lossFactor = Math.random() * 0.5 + 0.2; // Significant loss
                           const lossAmount = potentialRevenue * lossFactor;
                           revenue -= lossAmount;
                           revenue = Math.max(0, revenue);
                           eventText = `צי שלך הותקף בנתיב! ללא הגנה מספקת, נגרם נזק כבד. הפסד של כ-${Math.round(lossAmount)} דוקאטים.`;
                           eventType = 'loss';
                      } else { // War ships successfully defended
                           eventText = `נתקלת באיום ימי! אוניות המלחמה שלך הדפו את התוקפים והמסע נמשך ללא הפסד כספי ישיר (אך עם עיכוב).`;
                           eventType = 'neutral'; // No monetary loss, maybe add a small cost later
                      }
                 } else { // Severe event (Plague outbreak, major political upheaval, route closure)
                     // These events are harder to mitigate with just war ships
                      const lossFactor = Math.random() * 0.7 + 0.3; // Very significant loss
                      const lossAmount = potentialRevenue * lossFactor;
                      revenue -= lossAmount;
                      revenue = Math.max(0, revenue);
                      eventText = `אסון ב${route.destination}! מגפה או אירוע פוליטי דרמטי פגע קשות במסחר. הפסד עצום של כ-${Math.round(lossAmount)} דוקאטים.`;
                      eventType = 'loss';
                      // Severe events could also impact future state, but simplified for now.
                 }
             }


            profit = revenue - cost;
            state.money += profit;

            addEvent(`מסע סחר ל${route.destination}: קנית ${unitsTraded} יחידות ${state.buyGoods} ב-${Math.round(buyPrice)} ליחידה, מכרת ${unitsTraded} יחידות ${state.sellGoods} ב-${Math.round(sellPrice)} ליחידה (מחיר בפועל). הוצאה: ${Math.round(cost)}, הכנסה פוטנציאלית: ${Math.round(potentialRevenue)}. ${eventText} רווח/הפסד נקי: ${Math.round(profit)}.`, profit >= 0 ? 'profit' : 'loss');

             // Simple visual feedback on map
             els.mapVisualFeedback.innerHTML = `<p><strong>תוצאת המסע ל${route.destination}:</strong></p><p>${eventText}</p><p>רווח/הפסד: ${Math.round(profit)} דוקאטים.</p>`;
             els.mapVisualFeedback.style.display = 'block';


            return profit;
        }

        function nextRound() {
            // Hide map feedback
             els.mapVisualFeedback.style.display = 'none';
             els.mapVisualFeedback.innerHTML = '';

            // Calculate trade outcomes
            const tradeProfit = calculateTradeOutcome();
            // Money update is now inside calculateTradeOutcome


            // --- Advance Year and Update State ---
            state.year++;

            // Reset allocations
            state.merchantShips -= state.allocatedMerchantShips; // Ships that went on the voyage return (simplification)
            state.warShips -= state.allocatedWarShips; // War ships return
            state.allocatedMerchantShips = 0;
            state.allocatedWarShips = 0;

            // Simulate price changes for next year (more volatile)
            const priceFluctuationFactor = 0.15; // Prices can change by +/- 15%
            for (const city in state.prices) {
                for (const goods in state.prices[city]) {
                    state.prices[city][goods] = Math.max(
                        goods === 'glass' || goods === 'textiles' ? 50 : 100, // Minimum price
                        state.prices[city][goods] + (Math.random() - 0.5) * (state.prices[city][goods] * priceFluctuationFactor * 2) // Larger fluctuations
                    );
                }
            }

            // Simulate overall risk changes (e.g., due to political climate)
            state.baseRisk = Math.max(0.05, state.baseRisk + (Math.random() - 0.5) * 0.03); // Base risk slightly fluctuates

            // Simulate random events affecting the republic (separate from trade route event)
            const republicEventChance = 0.2; // 20% chance of a general event
            if (Math.random() < republicEventChance) {
                const eventType = Math.random();
                if (eventType < 0.3) {
                    const shipLoss = Math.floor(Math.random() * (state.merchantShips * 0.1) + 1); // Lose 1-10% of ships
                    state.merchantShips = Math.max(0, state.merchantShips - shipLoss);
                    addEvent(`אסון בנמל! סערה חזקה או שריפה פגעו בצי. איבדת ${shipLoss} אוניות סוחר.`, 'loss');
                } else if (eventType < 0.6) {
                    const incomeBoost = Math.floor(Math.random() * 1500 + 500); // Gain 500-2000
                    state.money += incomeBoost;
                    addEvent(`הסכם סחר חדש נחתם! שערים נוחים יותר הובילו לרווח בלתי צפוי של ${incomeBoost} דוקאטים.`, 'profit');
                } else {
                     const upkeepCost = Math.floor(Math.random() * 1000 + 200); // Cost 200-1200
                     state.money -= upkeepCost;
                     addEvent(`עלויות תחזוקה ותיקונים גבוהות מהצפוי עקב בלאי בצי. הוצאה של ${upkeepCost} דוקאטים.`, 'loss');
                }
            }


            // 5. Update UI for the next year
            updateUI();
            addEvent(`שנה ${state.year} החלה. קופה נוכחית: ${Math.round(state.money).toLocaleString()} דוקאטים. קבל החלטות!`, 'neutral');

             // Check for game end conditions (optional, e.g., bankruptcy)
             if (state.money < -5000) { // Significant debt
                 addEvent("קופת הרפובליקה ריקה והחובות נערמו. ימי הזוהר הסתיימו. המשחק נגמר.", 'loss');
                 els.nextRoundBtn.disabled = true;
                  els.investMerchantBtn.disabled = true;
                 els.investWarBtn.disabled = true;
                  els.allocateMerchantInput.disabled = true;
                  els.allocateWarInput.disabled = true;
             } else if (state.money > 100000 && state.year > 10) { // Arbitrary win condition
                  addEvent(`ברכות, הדוג'ה! לאחר ${state.year} שנים, הרפובליקה שלך היא המעצמה הכלכלית והימית העשירה ביותר בים התיכון, עם קופה של ${Math.round(state.money).toLocaleString()} דוקאטים. ניהולך האסטרטגי הוביל אותנו לתור הזהב! המשחק הסתיים בהצלחה.`, 'profit');
                   els.nextRoundBtn.disabled = true;
                  els.investMerchantBtn.disabled = true;
                 els.investWarBtn.disabled = true;
                  els.allocateMerchantInput.disabled = true;
                  els.allocateWarInput.disabled = true;
             }

             // Animate money/ship changes (simple version - could be more complex)
             animateValue(els.money, state.money); // Needs a separate animation function if not using innerHTML method
             animateValue(els.merchantShips, state.merchantShips - state.allocatedMerchantShips);
             animateValue(els.warShips, state.warShips - state.allocatedWarShips);


        }

        // Simple animation placeholder (more complex animation would track actual changes)
        function animateValue(element, newValue) {
             // This is a placeholder. Real animation would involve setting a target value
             // and smoothly transitioning the displayed text/number over time.
             // For now, we just update the text and let CSS handle visual cues via classes.
             // If using innerHTML for money, the class is handled there.
             if(element !== els.money) { // Only animate non-money elements for now
                 element.textContent = newValue;
                 element.classList.add('status-value-changed');
                 setTimeout(() => {
                     element.classList.remove('status-value-changed');
                 }, 500); // Remove class after animation
             }
        }


        function handleInvestment(type) {
            if (state.money >= state.investmentCost) {
                state.money -= state.investmentCost;
                if (type === 'merchant') {
                    state.merchantShips++;
                    addEvent(`השקעה: נבנתה אוניית סוחר חדשה הצטרפה לצי.`, 'investment');
                } else if (type === 'war') {
                    state.warShips++;
                     addEvent(`השקעה: נבנתה אוניית מלחמה חדשה הצטרפה לצי.`, 'investment');
                }
                updateUI();
            } else {
                addEvent("אין מספיק דוקאטים בקופה להשקעה זו.", 'loss');
            }
        }

        // --- Event Listeners ---
        els.tradeRouteSelect.addEventListener('change', (e) => { state.selectedRoute = e.target.value; updateUI(); });
        els.buyGoodsSelect.addEventListener('change', (e) => { state.buyGoods = e.target.value; updateUI(); });
        els.sellGoodsSelect.addEventListener('change', (e) => { state.sellGoods = e.target.value; updateUI(); });

         // Update state and UI immediately when allocation changes
        els.allocateMerchantInput.addEventListener('input', (e) => {
             let value = parseInt(e.target.value, 10) || 0;
             value = Math.max(0, Math.min(value, state.merchantShips)); // Clamp value
             e.target.value = value; // Update input field value
             state.allocatedMerchantShips = value;
             updateUI(); // Update UI including feedback and button state
         });
        els.allocateWarInput.addEventListener('input', (e) => {
             let value = parseInt(e.target.value, 10) || 0;
             value = Math.max(0, Math.min(value, state.warShips)); // Clamp value
             e.target.value = value; // Update input field value
             state.allocatedWarShips = value;
             updateUI(); // Update UI including feedback
         });

        els.investMerchantBtn.addEventListener('click', () => handleInvestment('merchant'));
        els.investWarBtn.addEventListener('click', () => handleInvestment('war'));
        els.nextRoundBtn.addEventListener('click', nextRound);

        els.showExplanationBtn.addEventListener('click', () => {
            const isHidden = els.explanationDiv.style.display === 'none';
            els.explanationDiv.style.display = isHidden ? 'block' : 'none';
            els.showExplanationBtn.textContent = isHidden ? 'הסתר הסבר על רפובליקות הסוחרים' : 'הצג הסבר על רפובליקות הסוחרים וסודותיהן';
        });


        // Initialize the game
        updateUI(); // Initial UI render
         // Ensure initial prices are displayed
         els.buyGoodsPriceSpan.textContent = Math.round(state.prices.venice[state.buyGoods]);
         const destination = state.selectedRoute.split('-')[1];
         els.sellGoodsPriceSpan.textContent = Math.round(state.prices[destination][state.sellGoods]);
    });
</script>
```