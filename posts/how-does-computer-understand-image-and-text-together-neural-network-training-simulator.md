---
title: "מסע אימון: איך המחשב לומד לקשר תמונה לטקסט?"
english_slug: how-does-computer-understand-image-and-text-together-neural-network-training-simulator
category: "טכנולוגיה / בינה מלאכותית"
tags: [רשתות עצביות, למידת מכונה, עיבוד תמונה, עיבוד שפה טבעית, למידה עמוקה, AI]
---
# מסע אימון: איך המחשב לומד לקשר תמונה לטקסט?

איך מערכות בינה מלאכותית מצליחות לפענח את העולם הוויזואלי והטקסטואלי בו זמנית? איך הן מקשרות בין מה שנראה בתמונה לבין התיאור המילולי המתאים? בואו נצלול לתוך תהליך ה"הבנה" הזה דרך סימולטור אימון רשת עצבית בסיסי. זה לא רק על לזהות אובייקטים, אלא על בניית גשר משמעותי בין תמונות למילים!

<div class="simulation-container">
    <h2 class="simulation-title">סימולטור קישור תמונה-טקסט</h2>
    <p class="simulation-description">צפו בתהליך הלימוד: הרשת מנסה להתאים תיאורי טקסט לתמונה נתונה ומשפרת את ה"הבנה" שלה צעד אחר צעד.</p>
    <div class="simulation-area">
        <div class="image-section panel">
            <h3>הקלט הוויזואלי: התמונה</h3>
            <div class="image-placeholder">
                <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&auto=format&fit=crop&w=870&q=80" alt="תמונת אוכל פשוטה" title="תמונה של סלט צבעוני">
                <p class="feature-label">מאפיינים ויזואליים (פיצ'רים):</p>
                <div class="features-placeholder image-features">
                    <div class="feature">צבע ירוק</div>
                    <div class="feature">עגול</div>
                    <div class="feature">קטן</div>
                    <div class="feature">טרי</div>
                    <div class="feature">קערה</div>
                    <div class="feature">אדום</div>
                </div>
                 <div class="connection-indicator"></div> <!-- Placeholder for visual link -->
            </div>
        </div>
        <div class="text-section panel">
            <h3>אפשרויות קלט טקסטואלי: תיאורים</h3>
            <div class="text-options">
                <div class="text-option" data-correct="false">
                    <p>חתול שחור יושב על גדר ישנה.</p>
                    <div class="features-placeholder text-features">
                         <div class="feature">חתול</div>
                         <div class="feature">שחור</div>
                         <div class="feature">גדר</div>
                         <div class="feature">ישנה</div>
                     </div>
                    <div class="score-container">
                        <span class="score-label">ציון התאמה: </span>
                        <span class="score-value" data-score="0.00">0.00</span>
                        <div class="score-bar">
                            <div class="score-fill"></div>
                        </div>
                    </div>
                </div>
                <div class="text-option" data-correct="true">
                    <p>סלט בריא ומלא צבעים בקערה.</p> <!-- נניח שהתמונה היא של סלט -->
                    <div class="features-placeholder text-features">
                        <div class="feature">סלט</div>
                        <div class="feature">בריא</div>
                        <div class="feature">צבעים</div>
                        <div class="feature">קערה</div>
                    </div>
                     <div class="score-container">
                        <span class="score-label">ציון התאמה: </span>
                        <span class="score-value" data-score="0.00">0.00</span>
                         <div class="score-bar">
                             <div class="score-fill"></div>
                         </div>
                    </div>
                </div>
                <div class="text-option" data-correct="false">
                    <p>מכונית מהירה נוסעת בכביש.</p>
                     <div class="features-placeholder text-features">
                         <div class="feature">מכונית</div>
                         <div class="feature">מהירה</div>
                         <div class="feature">כביש</div>
                     </div>
                     <div class="score-container">
                        <span class="score-label">ציון התאמה: </span>
                        <span class="score-value" data-score="0.00">0.00</span>
                         <div class="score-bar">
                             <div class="score-fill"></div>
                         </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="controls">
        <div class="status-area">
             <p>שגיאה נוכחית: <span id="error-value">0.00</span> <span class="error-target">(יעד: 0.00)</span></p>
             <p>איטרציות אימון (אפוקים): <span id="epoch-count">0</span></p>
        </div>
        <button id="train-button" class="action-button">אמן את הרשת (צעד 1)</button>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    .simulation-container {
        direction: rtl;
        font-family: 'Heebo', sans-serif;
        background-color: #f8f9fa; /* Light grey background */
        padding: 30px;
        border-radius: 12px;
        max-width: 960px; /* Wider container */
        margin: 30px auto;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08); /* Softer, larger shadow */
        overflow: hidden; /* Clear floats/margins */
    }

    .simulation-title {
        text-align: center;
        color: #343a40; /* Dark grey */
        margin-bottom: 10px;
        font-weight: 700;
    }

    .simulation-description {
        text-align: center;
        color: #6c757d; /* Muted text */
        margin-bottom: 30px;
        font-size: 1.1em;
    }

    .simulation-area {
        display: flex;
        justify-content: center; /* Center content */
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 30px; /* Increased gap */
        margin-bottom: 30px;
    }

    .panel {
        background-color: #ffffff;
        padding: 25px; /* Increased padding */
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06); /* Softer shadow */
        flex-grow: 1; /* Allow panels to grow */
        flex-basis: 0; /* Start with base of 0 */
        min-width: 300px; /* Ensure minimum width */
        display: flex;
        flex-direction: column; /* Stack content vertically */
    }

    .image-section {
        flex-basis: 350px; /* Give image section a bit more space */
        align-items: center; /* Center image content */
    }

     .image-placeholder img {
         max-width: 100%;
         height: auto;
         border: 1px solid #e9ecef; /* Light border */
         border-radius: 6px;
         margin-bottom: 15px; /* Space below image */
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); /* subtle shadow */
         transition: transform 0.3s ease-in-out; /* Animation on hover/interaction */
     }

     .image-section:hover img {
         transform: scale(1.02);
     }

     .image-section h3, .text-section h3 {
         margin-top: 0;
         color: #495057; /* Slightly darker grey */
         text-align: center; /* Center section titles */
         margin-bottom: 20px;
         font-weight: 700;
     }

    .feature-label {
        font-size: 0.9em;
        color: #6c757d;
        margin-bottom: 10px;
        text-align: center;
    }

     .features-placeholder {
         display: flex;
         flex-wrap: wrap;
         justify-content: center; /* Center features */
         gap: 8px; /* Increased gap between features */
         margin-top: 10px;
         padding-top: 15px; /* Increased padding */
         border-top: 1px dashed #dee2e6; /* Lighter border */
         font-size: 0.85em;
         color: #495057;
     }

     .feature {
         background-color: #e9ecef; /* Light grey background */
         padding: 5px 10px; /* Increased padding */
         border-radius: 4px; /* More rounded */
         transition: transform 0.2s ease, background-color 0.2s ease, opacity 0.5s ease; /* Smooth transitions */
         cursor: help; /* Indicate hoverable */
     }

     .feature:hover {
         transform: translateY(-2px); /* Lift slightly on hover */
         background-color: #ced4da; /* Darker on hover */
     }

     .text-features .feature {
         opacity: 0.6; /* Start with lower opacity */
     }

     .text-features .feature.active-feature {
         opacity: 1; /* Full opacity for active features */
         background-color: #cce5ff; /* Light blue for active */
         font-weight: bold;
     }


    .text-section {
        flex-basis: 500px; /* Give text section more space */
    }

    .text-options {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap between options */
    }

    .text-option {
        border: 1px solid #ced4da; /* Light grey border */
        padding: 15px; /* Increased padding */
        border-radius: 8px; /* More rounded */
        background-color: #f8f9fa; /* Slightly darker background than container */
        display: flex;
        flex-direction: column;
        transition: all 0.3s ease; /* Smooth transition for state changes */
    }

     .text-option[data-correct="true"] {
         border-color: #28a745; /* Green border for correct */
     }

     .text-option[data-correct="false"] {
          border-color: #dc3545; /* Red border for incorrect initially */
     }

     .text-option p {
         margin-top: 0;
         margin-bottom: 10px;
         font-weight: 400;
         color: #343a40;
     }

    .score-container {
        margin-top: 15px; /* More space */
        display: flex;
        align-items: center;
        font-size: 0.95em; /* Slightly larger font */
        color: #495057;
    }

    .score-label {
        min-width: 90px; /* Align labels */
        font-weight: 400;
    }

    .score-value {
        font-weight: 700;
        min-width: 50px; /* Align values */
        text-align: left; /* Align value left in RTL context */
        margin-left: 10px; /* Space between label and value */
         transition: color 0.5s ease; /* Smooth color change */
    }

    .score-bar {
        flex-grow: 1;
        height: 12px; /* Thicker bar */
        background-color: #e9ecef; /* Light grey track */
        border-radius: 6px; /* More rounded */
        margin-right: 10px;
        overflow: hidden;
        position: relative;
        direction: ltr; /* Ensure bar grows left-to-right visually */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); /* Inner shadow for depth */
    }

     .score-fill {
         display: block;
         height: 100%;
         width: var(--score-width, 0%); /* Use CSS variable for width */
         background: linear-gradient(to right, #007bff, #0056b3); /* Gradient blue */
         transition: width 0.8s ease-in-out; /* Slower, smoother animation */
         border-radius: 6px;
     }

     .text-option[data-correct="true"] .score-fill {
         background: linear-gradient(to right, #28a745, #218838); /* Gradient green */
     }
     .text-option[data-correct="false"] .score-fill {
         background: linear-gradient(to right, #dc3545, #c82333); /* Gradient red */
     }


    .controls {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 15px; /* Increased gap */
        padding: 20px; /* Increased padding */
        background-color: #e9ecef; /* Light background for controls */
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

     .status-area {
         flex-grow: 1;
         min-width: 250px;
         font-size: 1em;
         color: #343a40;
         line-height: 1.6;
     }

    .status-area p {
        margin: 0;
        margin-bottom: 5px;
    }

    .error-target {
        font-size: 0.9em;
        color: #6c757d;
    }

    #error-value {
         font-weight: bold;
         transition: color 0.5s ease; /* Smooth color change */
    }


    .action-button {
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em; /* Larger font */
        color: #fff;
        background-color: #007bff; /* Primary blue */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
        font-weight: 700;
    }

    .action-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-1px); /* Lift button */
        box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3); /* Subtle shadow */
    }

     .action-button:active {
         transform: translateY(0); /* Press effect */
         box-shadow: none;
     }

     .action-button:disabled {
         background-color: #cccccc;
         cursor: not-allowed;
     }


    .explanation-toggle-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        background-color: #6c757d; /* Secondary grey */
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: 700;
    }

    .explanation-toggle-button:hover {
        background-color: #5a6268;
        transform: translateY(-1px);
        box-shadow: 0 2px 5px rgba(108, 117, 125, 0.3);
    }

     .explanation-toggle-button:active {
         transform: translateY(0);
         box-shadow: none;
     }

    #explanation {
        display: none; /* Initially hidden */
        margin-top: 30px; /* More space above */
        padding: 30px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
        direction: rtl;
        font-family: 'Heebo', sans-serif;
        line-height: 1.7; /* Increased line height */
        color: #343a40;
    }

    #explanation h2 {
         color: #343a40;
         margin-bottom: 20px;
         font-weight: 700;
         text-align: center;
    }

    #explanation h3 {
        color: #495057;
        margin-top: 25px; /* More space above headings */
        margin-bottom: 15px;
        font-weight: 700;
        border-bottom: 2px solid #007bff; /* Accent underline */
        padding-bottom: 5px;
        display: inline-block; /* Underline only the text */
    }

    #explanation p {
        margin-bottom: 15px; /* More space between paragraphs */
    }

     #explanation ul {
         margin-bottom: 15px;
     }

     #explanation li {
         margin-bottom: 8px;
         line-height: 1.5;
     }

     /* Specific animations */
    .feature-pulse {
        animation: pulse 0.8s ease-out forwards;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    .score-update-animation {
        animation: score-pulse 0.5s ease-out;
    }

    @keyframes score-pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

</style>

<button class="explanation-toggle-button" id="toggle-explanation">הסבר לעומק: איך זה עובד מאחורי הקלעים?</button>

<div id="explanation">
    <h2>הסבר מעמיק: מסע הלמידה של המחשב</h2>

    <h3>מהי רשת עצבית בהקשר זה?</h3>
    <p>דמיינו רשת עצבית כמערכת מסועפת שמקבלת מידע משני עולמות שונים – עולם התמונות ועולם הטקסט – ומנסה למצוא ביניהם קשר. היא בנויה מ"נוירונים" דיגיטליים שמעבירים ביניהם אותות דרך קשרים בעלי "משקולות". המשקולות הללו הן למעשה מספרים, והן מייצגות את ה"חשיבות" או ה"חוזק" של הקשר בין נוירון לנוירון אחר. בתהליך האימון, הרשת לומדת לכוונן את המשקולות הללו כדי לבצע מטלה מסוימת – במקרה שלנו, להתאים תמונה לתיאור הטקסטואלי הנכון.</p>

    <h3>ייצוג משותף (Embedding): המפתח ל"הבנה"</h3>
    <p>מחשבים אינם חושבים כמו בני אדם. במקום "להבין" תמונה או טקסט, הם ממירים אותם לייצוג מספרי. המפתח ליכולת של המחשב לקשר בין תמונה לטקסט טמון ביצירת "מרחב משותף" (Shared Embedding Space). במרחב זה, גם תמונות וגם טקסטים מיוצגים כוקטורים (רשימות ארוכות של מספרים). המטרה היא שכאשר תמונה ותיאור טקסטואלי מתאימים זה לזה, הוקטורים המייצגים אותם יהיו קרובים זה לזה מבחינה מתמטית במרחב המשותף. ככל שהם קרובים יותר, כך "ציון ההתאמה" גבוה יותר.</p>
    <p>הסימולטור שלנו ממחיש את זה באמצעות ציוני ההתאמה – אלו למעשה מידת הקרבה במרחב הייצוג המשותף לאחר עיבוד התמונה והטקסט על ידי רכיבי הרשת המתאימים.</p>

    <h3>תהליך האימון: מניחוש לדיוק</h3>
    <p>תהליך האימון הוא סדרה של ניסוי ותיקון, החוזר על עצמו פעמים רבות (נקרא "אפוקים"). הרשת מתחילה עם משקולות אקראיות, ולכן ה"ניחושים" הראשונים שלה (ציוני ההתאמה ההתחלתיים בסימולטור) הם שגויים ברובם. בכל צעד אימון (אפוק), קורים הדברים הבאים:</p>
    <ul>
        <li>**הצגת דוגמה:** הרשת מקבלת זוג (תמונה, תיאורים אפשריים). היא מעבדת את התמונה לוקטור אחד ואת כל התיאורים לוקטורים משלהם במרחב המשותף.</li>
        <li>**חישוב ציונים:** הרשת מחשבת את הקרבה (Similarity Score) בין וקטור התמונה לכל אחד מוקטורי הטקסט. זהו ציון ההתאמה המוצג בסימולטור.</li>
        <li>**חישוב שגיאה (Loss):** הרשת יודעת איזה טקסט הוא התיאור ה"נכון" לתמונה (זהו המידע שהוזן לה במהלך האימון המפוקח). היא משווה את ציוני ההתאמה שחישבה לתוצאה הרצויה (ציון גבוה מאוד לטקסט הנכון, ציון נמוך מאוד לשגויים). ההבדל בין התוצאה המחושבת לתוצאה הרצויה הוא ה"שגיאה" או ה"הפסד" (Loss). המטרה תמיד היא למזער את ההפסד הזה. הסימולטור מציג ערך שגיאה כללי.</li>
        <li>**תיקון (Backpropagation & Optimization):** זהו השלב החשוב ביותר. על בסיס השגיאה שחושבה, הרשת מפעילה אלגוריתם (כמו Gradient Descent) כדי לגלות כיצד עליה לשנות את אלפי או מיליוני המשקולות שלה בצורה מינימלית, כך שבפעם הבאה שהיא תראה את אותה דוגמה (או דוגמה דומה), השגיאה תהיה קטנה יותר. זה כאילו הרשת לומדת מהטעויות שלה ומכווננת את הקשרים הפנימיים שלה.</li>
        <li>**איטרציה:** התהליך חוזר על עצמו עם זוגות תמונה-טקסט נוספים ממאגר האימון. עם כל איטרציה, המשקולות מתעדכנות, והרשת נעשית טובה יותר בהתאמה – ציוני ההתאמה לזוגות הנכונים עולים, וציוני ההתאמה לזוגות השגויים יורדים. הסימולטור מדגים זאת באמצעות לחיצה על "אמן", שמבצעת צעד עדכון אחד כזה.</li>
    </ul>

    <h3>ה"פיצ'רים" מתעוררים לחיים</h3>
    <p>כשמדברים על "פיצ'רים" (מאפיינים) בתמונה או בטקסט, הכוונה היא לרכיבים הבסיסיים או המורכבים שהרשת לומדת לזהות ולהשתמש בהם כדי לקשר בין המידע. בתמונות, זה יכול להתחיל מקווים וצבעים ולהגיע עד לזיהוי אובייקטים שלמים או סצנות. בטקסט, זה יכול להיות מילים בודדות, שילובי מילים, או אפילו משמעויות סמנטיות עמוקות יותר. הרשת לומדת איזה פיצ'רים ויזואליים קשורים לאילו פיצ'רים טקסטואליים במרחב המשותף. בסימולטור, הפיצ'רים המוצגים הם דוגמה מפושטת לרכיבים שהרשת עשויה להתמקד בהם.</p>

    <h3>יישומים בעולם האמיתי</h3>
    <p>היכולת לקשר בין תמונה לטקסט היא בסיס למגוון עצום של יישומי AI מתקדמים:</p>
    <ul>
        <li>**חיפוש ויזואלי:** מציאת תמונות דומות לתמונה קיימת, או חיפוש תמונות באמצעות שאילתות טקסט מורכבות ("כלבים קטנים משחקים בפארק").</li>
        <li>**יצירת כיתוב אוטומטי לתמונות (Image Captioning):** המחשב מייצר תיאור טקסטואלי מדויק של תוכן התמונה.</li>
        <li>**מענה ויזואלי-לשוני (Visual Question Answering - VQA):** הצגת תמונה ושאלת שאלה עליה בטקסט ("מה צבע הקערה?", "האם יש חיות בתמונה?"), והמחשב מספק תשובה טקסטואלית.</li>
        <li>**מודלי יצירה גנרטיביים (DALL-E, Midjourney):** היכולת ליצור תמונות חדשות לגמרי על סמך תיאור טקסטואלי מפורט, דורשת הבנה עמוקה במיוחד של הקשר בין מילים למאפיינים ויזואליים.</li>
        <li>**נגישות:** תיאור תמונות אוטומטי עבור עיוורים וכבדי ראייה.</li>
    </ul>

    <h3>מגבלות</h3>
    <p>חשוב לזכור שמודלים אלו, מרשימים ככל שיהיו, עדיין מוגבלים. הם דורשים כמויות אדירות של נתונים וזמן אימון. לעיתים הם עשויים להיכשל בהבנת ניואנסים, סרקזם, או הקשר מורכב מאוד. ה"הבנה" שלהם היא סטטיסטית ומתבססת על הדפוסים שלמדו מנתוני האימון, והיא אינה זהה להבנה הקונספטואלית וההקשרית של בני אדם.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const trainButton = document.getElementById('train-button');
        const textOptions = document.querySelectorAll('.text-option');
        const errorValueSpan = document.getElementById('error-value');
        const epochCountSpan = document.getElementById('epoch-count');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let scores = [];
        let correctIndex = -1; // To be set based on data-correct="true"
        let epoch = 0;
        const learningRate = 0.15; // How much scores change per epoch (slightly increased for faster demo)
        const targetScoreCorrect = 0.95; // Target not exactly 1 to simulate real-world models
        const targetScoreIncorrect = 0.05; // Target not exactly 0

        // Initialize scores and find correct index
        textOptions.forEach((option, index) => {
            // Initialize with small random scores (simulating random weights)
            scores[index] = parseFloat((Math.random() * 0.1).toFixed(2)); // Start close to 0
            if (option.dataset.correct === 'true') {
                correctIndex = index;
            }
            updateScoreDisplay(index, false); // Don't animate initial display
        });

        // Calculate and display initial error
        updateErrorDisplay();
        updateButtonText();

        function updateScoreDisplay(index, animate = true) {
            const optionElement = textOptions[index];
            const scoreValueSpan = optionElement.querySelector('.score-value');
            const scoreFillBar = optionElement.querySelector('.score-fill');
            const features = optionElement.querySelectorAll('.text-features .feature');
            const score = scores[index];

            scoreValueSpan.textContent = score.toFixed(2);
             if (animate) {
                 scoreValueSpan.classList.add('score-update-animation');
                 // Remove class after animation ends
                 scoreValueSpan.addEventListener('animationend', () => {
                     scoreValueSpan.classList.remove('score-update-animation');
                 }, { once: true });
             }


            // Set CSS variable for bar width (percentage)
            scoreFillBar.style.setProperty('--score-width', `${Math.max(0, Math.min(1, score)) * 100}%`);

             // Update feature opacity based on score (simple simulation)
            features.forEach(feature => {
                // A simple model: features are more 'active' if the score is high
                // For incorrect options, features become less active as score drops
                // For the correct option, features become more active as score rises
                let featureOpacity = 0.3; // Base low opacity
                if (index === correctIndex) {
                    // Correct features become more opaque/prominent as score increases
                    featureOpacity = 0.3 + (score * 0.7); // Scales from 0.3 to 1
                 } else {
                    // Incorrect features become less opaque/prominent as score decreases
                     featureOpacity = score * 0.6; // Scales from 0 to 0.6
                 }
                 feature.style.opacity = Math.max(0.1, Math.min(1, featureOpacity)); // Keep within a reasonable range
                 if (featureOpacity > 0.8) { // Threshold for "active" look
                     feature.classList.add('active-feature');
                 } else {
                     feature.classList.remove('active-feature');
                 }
            });


        }

        function calculateError() {
            let error = 0;
            scores.forEach((score, index) => {
                const target = (index === correctIndex) ? targetScoreCorrect : targetScoreIncorrect;
                // Using squared error for a more standard representation of loss
                error += Math.pow(target - score, 2);
            });
            // Sum of squared errors
            return error;
        }

        function updateErrorDisplay() {
            const currentError = calculateError();
            errorValueSpan.textContent = currentError.toFixed(2);

            // Add color indication for error
            if (currentError < 0.05) { // Example threshold for low error
                errorValueSpan.style.color = '#28a745'; // Green
            } else if (currentError < 0.5) { // Medium error
                 errorValueSpan.style.color = '#ffc107'; // Orange/Yellow
            }
            else { // High error
                errorValueSpan.style.color = '#dc3545'; // Red
            }

             // Check if converged (error is low enough)
             if (currentError < 0.05) {
                 trainButton.textContent = 'הרשת התאמנה בהצלחה!';
                 trainButton.disabled = true;
                 trainButton.style.backgroundColor = '#28a745';
                 trainButton.style.boxShadow = '0 2px 5px rgba(40, 167, 69, 0.3)';
                 textOptions[correctIndex].style.borderColor = '#28a745';
                 textOptions[correctIndex].style.boxShadow = '0 0 15px rgba(40, 167, 69, 0.2)';
             }
        }

        function updateButtonText() {
             if (calculateError() >= 0.05) {
                 trainButton.textContent = `אמן את הרשת (צעד ${epoch + 1})`;
             }
        }

        function trainOneEpoch() {
            if (calculateError() < 0.05) return; // Stop training if converged

            epoch++;
            epochCountSpan.textContent = epoch;

            // Simulate backpropagation and weight update
            // Adjust scores based on the desired outcome (correct score up, incorrect scores down)
            // The "learningRate" controls the step size

            scores.forEach((score, index) => {
                const target = (index === correctIndex) ? targetScoreCorrect : targetScoreIncorrect;
                const error = target - score; // Simple error for gradient calculation
                // Update score by moving towards the target, scaled by learning rate
                let delta = error * learningRate;

                // Add a small random nudge initially to simulate exploration
                if (epoch < 10) { // Make the first few steps feel less linear
                    delta += (Math.random() - 0.5) * learningRate * 0.5;
                }


                scores[index] = score + delta;

                // Ensure scores are within [0, 1] range
                scores[index] = parseFloat(Math.max(0, Math.min(1, scores[index])).toFixed(2));

                updateScoreDisplay(index, true); // Animate display update
            });

             // Animate image features briefly
             document.querySelectorAll('.image-features .feature').forEach(feature => {
                 feature.classList.add('feature-pulse');
                 feature.addEventListener('animationend', () => {
                     feature.classList.remove('feature-pulse');
                 }, { once: true });
             });


            // Update error display after scores are updated
            updateErrorDisplay();
            updateButtonText();
        }

        trainButton.addEventListener('click', trainOneEpoch);

        // Toggle explanation section
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתרת הסבר' : 'הסבר לעומק: איך זה עובד מאחורי הקלעים?';
        });
    });
</script>
```