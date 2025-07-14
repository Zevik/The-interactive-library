---
title: "ועדת פרס ישראל: סימולטור קבלת החלטות"
english_slug: israel-prize-committee-decision-making-simulator
category: "מדעי החברה / כללי"
tags:
  - פרס ישראל
  - קבלת החלטות
  - ועדות
  - ניהול
  - שיפוט קבוצתי
---
# ועדת פרס ישראל: שחק/י אותה שופט/ת!

פסגת ההכרה בישראל. תואר נכסף. אבל מה באמת קורה בחדרי הדיונים הסגורים של ועדת פרס ישראל? איך מחליטים מי האדם או המוסד הראוי ביותר מבין שורה של מועמדים מבריקים? האם הכל עניין של מדדים אובייקטיביים, או שישנם גורמים נוספים, אנושיים יותר, שמשפיעים על הבחירה הגורלית?

הסימולטור הזה מזמין אתכם ללבוש את גלימת השופט. היכנסו לנעלי חבר ועדה וגלו ממקור ראשון את המורכבות, השיקולים השונים, ואת הדינמיקה שמובילה להחלטה הסופית. האם הבחירה שלכם תהיה גם בחירת הוועדה?

<div class="interactive-app">
    <h2>החלטה בוועדה: המבחן שלכם</h2>
    <p>את/ה חבר/ת ועדת פרס ישראל בתחום הספרות. לפנייך סקירה תמציתית של שלושה מועמדים מובילים. הענק/י לכל אחד/ת ציון (1 - הכי נמוך, 5 - הכי גבוה) בכל אחד מהקריטריונים המנחים את הוועדה.</p>

    <div class="candidates">
        <div class="candidate-card" data-candidate="cohen">
            <div class="candidate-info">
                <h3>פרופ' אהרון כהן <span class="subtitle">חוקר ומבקר ספרות</span></h3>
                <p>חוקר ומבקר ספרות בעל שם עולמי. פרסם עשרות מאמרים וספרים פורצי דרך בחקר השירה העברית המודרנית. עבודתו מאופיינת במקוריות רבה ועומק תיאורטי. זוכה בפרסים אקדמיים רבים, אך פחות מוכר לקהל הרחב.</p>
            </div>
            <h4>הערכה (1-5):</h4>
            <div class="criteria">
                <label>מקוריות התרומה:</label>
                <div class="rating-control" data-criterion="originality" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="cohen" data-criterion="originality" value="3">
            </div>
            <div class="criteria">
                <label>השפעה על התחום:</label>
                 <div class="rating-control" data-criterion="impact" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                 <input type="hidden" class="rating" data-candidate="cohen" data-criterion="impact" value="3">
            </div>
             <div class="criteria">
                <label>היקף ורציפות פעילות:</label>
                 <div class="rating-control" data-criterion="scope" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="cohen" data-criterion="scope" value="3">
            </div>
        </div>

        <div class="candidate-card" data-candidate="levi">
             <div class="candidate-info">
                <h3>ד"ר רות לוי <span class="subtitle">סופרת פופולרית</span></h3>
                <p>סופרת מחוננת ופופולרית. ספריה זכו להצלחה ביקורתית ומסחרית גדולה, ותורגמו לשפות רבות. עוסקת בנושאים חברתיים אקטואליים ומעוררת דיון ציבורי. פחות פעילה במחקר אקדמי פורמלי.</p>
             </div>
            <h4>הערכה (1-5):</h4>
             <div class="criteria">
                <label>מקוריות התרומה:</label>
                 <div class="rating-control" data-criterion="originality" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                 <input type="hidden" class="rating" data-candidate="levi" data-criterion="originality" value="3">
            </div>
            <div class="criteria">
                <label>השפעה על התחום/ציבור:</label>
                 <div class="rating-control" data-criterion="impact" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="levi" data-criterion="impact" value="3">
            </div>
             <div class="criteria">
                <label>היקף ורציפות פעילות:</label>
                <div class="rating-control" data-criterion="scope" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="levi" data-criterion="scope" value="3">
            </div>
        </div>

        <div class="candidate-card" data-candidate="shapira">
            <div class="candidate-info">
                <h3>פרופ' דוד שפירא <span class="subtitle">מתרגם ומעורר תרבות</span></h3>
                <p>מתרגם ומעורר תרבות חשוב. תרגומיו ליצירות מופת קנו להם מקום של כבוד. ערך אנתולוגיות רבות ופועל רבות לקידום קריאה ותרבות בספריות ובבתי ספר. פחות מחקר מקורי.</p>
            </div>
            <h4>הערכה (1-5):</h4>
            <div class="criteria">
                <label>מקוריות התרומה:</label>
                <div class="rating-control" data-criterion="originality" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="shapira" data-criterion="originality" value="3">
            </div>
            <div class="criteria">
                <label>השפעה על התחום/ציבור:</label>
                <div class="rating-control" data-criterion="impact" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="shapira" data-criterion="impact" value="3">
            </div>
             <div class="criteria">
                <label>היקף ורציפות פעילות:</label>
                <div class="rating-control" data-criterion="scope" data-rating="3">
                    <span class="rating-star" data-value="1"></span>
                    <span class="rating-star" data-value="2"></span>
                    <span class="rating-star" data-value="3"></span>
                    <span class="rating-star" data-value="4"></span>
                    <span class="rating-star" data-value="5"></span>
                </div>
                <input type="hidden" class="rating" data-candidate="shapira" data-criterion="scope" value="3">
            </div>
        </div>
    </div>

    <button id="simulate-btn">סמולץ את דיון הוועדה וגלה/י מי זכה/תה!</button>
     <div class="loading-spinner hidden"></div>


    <div id="simulation-results" class="hidden">
        <h3>תוצאות דיון הוועדה</h3>
        <p>הסימולציה הבאה משקפת את ממוצע ההערכות של כל חברי הוועדה הווירטואליים (המייצגים פרספקטיבות שונות) יחד עם ההערכות שלך:</p>
        <div id="committee-scores"></div>
        <div id="final-result"></div>
        <div id="tie-message" class="hidden"></div>
    </div>
</div>

<button id="toggle-explanation">רוצה/ה לדעת עוד? הצג/הסתר הסבר על פרס ישראל ותהליך השיפוט</button>

<div id="explanation" class="hidden">
    <h2>הסבר מעמיק: מאחורי הקלעים של פרס ישראל</h2>

    <h3>מהו פרס ישראל ולמה הוא חשוב?</h3>
    <p>פרס ישראל הוא גולת הכותרת של ההוקרה וההערכה בישראל, המוענק בטקס ממלכתי ביום העצמאות. הוא מוענק ליחידים או מוסדות שתרמו תרומה יוצאת דופן למדינה, לחברה או לתחומם המקצועי. הפרס מסמל הכרה בפסגת היצירה, המחקר והפעילות הציבורית בישראל, ומעניק יוקרה עצומה לזוכים בו.</p>

    <h3>קריטריונים והאתגר בשיפוט</h3>
    <p>ועדות הפרס מתבססות על קריטריונים כמו מצוינות אקדמית/אמנותית, מקוריות, השפעה (בתחום המקצועי ו/או על החברה), והיקף הפעילות לאורך שנים. אולם, כיצד משווים תרומה מדעית פורצת דרך להשפעה תרבותית רחבה או לפעילות חינוכית רבת שנים? יישום הקריטריונים הללו בתחומים מגוונים דורש שיקול דעת מעמיק, ולעיתים קרובות אין "נוסחת קסם" אובייקטיבית. חברי הוועדה נדרשים לאזן בין סוגי תרומות שונים ולהגיע להכרעה מורכבת.</p>

    <h3>הדינמיקה הסמויה בוועדה</h3>
    <p>הוועדה היא קבוצה של מומחים, ולכן תהליך קבלת ההחלטות מושפע באופן בלתי נמנע מדינמיקות קבוצתיות. הצורך להגיע לקונצנזוס יכול לעיתים להוביל לפשרות, בהן מועמד "מוסכם" זוכה על חשבון מועמד "שנוי במחלוקת" אך אולי בעל תרומה מקורית יותר. חברים בעלי מוניטין חזק או אישיות דומיננטית יכולים להשפיע יותר על עמדות אחרים. לעיתים, דיון פתוח וכנה יכול לחשוף זוויות ראייה חדשות ולשנות עמדות, בעוד שבמקרים אחרים עמדות נוקשות עלולות להקשות על קבלת החלטה. גם לחצים חיצוניים (פוליטיים, תקשורתיים או ציבוריים) יכולים לחלחל לדיוני הוועדה ולהשפיע בעקיפין על התהליך.</p>

    <h3>על הטיות קוגניטיביות בחדר הסגור</h3>
    <p>גם המומחים הגדולים ביותר אינם חסינים מפני הטיות קוגניטיביות, שיכולות לעצב את תפיסתם ואת שיפוטם:
    <ul>
        <li><b>אפקט ההילה:</b> התרשמות חיובית כללית (למשל, ממוניטין רחב או הופעה כריזמטית) צובעת באור חיובי יותר גם היבטים ספציפיים בפועלו של המועמד.</li>
        <li><b>הטיית אישור (Confirmation Bias):</b> נטייה לחפש מידע ולהתייחס אליו באופן שמחזק עמדה או העדפה קיימת לגבי מועמד מסוים, ולהתעלם ממידע סותר.</li>
        <li><b>אפקט העוגן (Anchoring Effect):</b> התבססות יתר על פיסת מידע ראשונית (כמו ההמלצה הראשונה שנקראה, או הציון הראשון שמישהו העניק) כ"עוגן" שממנו מתבצעות התאמות קטנות בלבד, גם אם מידע מאוחר יותר מצדיק שינוי משמעותי יותר.</li>
        <li><b>הטיית הזמינות (Availability Bias):</b> הערכת יתר למועמדים או להישגים שקלים יותר להיזכר בהם או שקיבלו חשיפה תקשורתית רבה, לעומת תרומות משמעותיות אך פחות "נוצצות" או מוכרות לציבור הרחב.</li>
    </ul>
    המודעות להטיות אלו חיונית כדי לנסות למזער את השפעתן על תהליך השיפוט.</p>

    <h3>חשיבות הגיוון בוועדות שיפוט</h3>
    <p>הרכב ועדת שיפוט מגוון – מבחינת גיל, מגדר, רקע מקצועי ספציפי (גם בתוך תחום רחב כמו ספרות), מוצא, השקפות ועוד – הוא קריטי. גיוון כזה מאפשר להביא מגוון רחב יותר של פרספקטיבות, הבנות ורגישויות לשולחן הדיונים. הוא יכול לסייע בחשיפת הטיות, להבטיח שסוגי תרומות שונים יזכו להערכה נאותה, ולשקף טוב יותר את מורכבות התחום והחברה הישראלית.</p>

    <h3>אובייקטיביות מול סובייקטיביות: האיזון העדין</h3>
    <p>בעוד שבתחומי מדעים מדויקים ישנם לעיתים קרובות מדדים אובייקטיביים יותר (כגון מספר פרסומים בכתבי עת מובילים, ציטוטיות), בתחומי הספרות, אמנות ומדעי הרוח, ההערכה כרוכה במידה רבה בשיפוט איכותני, פרשנות והערכה סובייקטיבית של חשיבות התרומה, מקוריותה ועומקה. תהליך קבלת ההחלטות בפרס ישראל הוא ניסיון לאזן בין הצורך להעריך באופן מקצועי ואובייקטיבי ככל הניתן, לבין ההכרה בכך ששיפוט בתחומים רבים הוא מטבעו סובייקטיבי, ומצריך דיון מעמיק והגעה לקונצנזוס קבוצתי המשקף את הערכים וההבנות של חברי הוועדה.</p>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --primary-dark: #0056b3;
        --secondary-color: #28a745; /* Green for success/winner */
        --background-light: #f4f7f6;
        --card-background: #ffffff;
        --border-color: #ddd;
        --text-color: #333;
        --subtitle-color: #555;
        --star-color-empty: #ccc;
        --star-color-filled: #ffc107; /* Amber/Gold */
        --transition-speed: 0.3s;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-light);
        margin: 0;
        padding: 20px;
        direction: rtl; /* Ensure right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: var(--primary-dark);
        margin-bottom: 15px;
    }

    h1 {
        text-align: center;
        color: var(--primary-dark);
        margin-bottom: 30px;
        font-size: 2em;
    }

    h2 {
         border-bottom: 2px solid var(--primary-color);
         padding-bottom: 5px;
         margin-bottom: 20px;
         color: var(--primary-dark);
    }
     h3 {
        color: var(--text-color);
        margin-top: 20px;
     }

    .interactive-app, #explanation {
        background-color: var(--background-light);
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        padding: 25px;
        margin-bottom: 25px;
        border-radius: 10px;
        transition: all var(--transition-speed) ease-in-out;
    }

     #explanation {
         background-color: #e9ecef; /* Slightly different background for explanation */
         border-color: #ced4da;
     }

    .candidates {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 20px; /* Space between cards */
        margin-top: 20px;
    }

    .candidate-card {
        flex: 1 1 300px; /* Grow, shrink, base width */
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        padding: 20px;
        border-radius: 8px;
        background-color: var(--card-background);
        display: flex;
        flex-direction: column;
        transition: transform var(--transition-speed) ease-in-out;
    }

    .candidate-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .candidate-info h3 {
        margin-top: 0;
        margin-bottom: 5px;
        color: var(--primary-dark);
    }

    .candidate-info .subtitle {
        font-size: 0.9em;
        color: var(--subtitle-color);
        font-weight: normal;
    }

     .candidate-info p {
         font-size: 0.95em;
         margin-bottom: 15px;
     }

    .criteria {
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        flex-wrap: wrap; /* Wrap label and control on small screens */
    }

    .criteria label {
        display: inline-block;
        margin-right: 15px;
        font-weight: bold;
        min-width: 120px; /* Give labels a minimum width */
        text-align: right;
    }

    .rating-control {
        display: inline-flex;
        gap: 3px; /* Space between stars/elements */
        cursor: pointer;
        align-items: center;
        flex-grow: 1; /* Allow rating control to take available space */
    }

    .rating-star {
        width: 25px;
        height: 25px;
        background-color: var(--star-color-empty);
        clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); /* Star shape */
        transition: background-color var(--transition-speed) ease-in-out, transform 0.1s ease-in-out;
    }

     .rating-star:hover {
         transform: scale(1.1);
     }

    .rating-star.filled {
        background-color: var(--star-color-filled);
    }


    button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: var(--primary-color);
        color: white;
        transition: background-color var(--transition-speed) ease-in-out, transform 0.1s ease-in-out;
        font-weight: bold;
    }

     button:hover:not(:disabled) {
        background-color: var(--primary-dark);
        transform: translateY(-2px);
     }

     button:active:not(:disabled) {
         transform: translateY(0);
     }

     button:disabled {
         background-color: #ccc;
         cursor: not-allowed;
     }

    #simulation-results {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
        opacity: 0;
        max-height: 0;
        overflow: hidden;
        transition: opacity var(--transition-speed) ease-in-out, max-height var(--transition-speed) ease-in-out;
    }

    #simulation-results.visible {
        opacity: 1;
        max-height: 500px; /* Adjust based on content height */
    }


    .hidden {
        display: none;
    }

    #committee-scores div {
        margin-bottom: 12px;
        padding: 10px;
        background-color: #e9ecef;
        border-radius: 5px;
        border-right: 4px solid var(--primary-color);
    }

    #committee-scores strong {
        color: var(--primary-dark);
    }

    #final-result {
        margin-top: 25px;
        font-weight: bold;
        font-size: 1.3em;
        color: var(--secondary-color); /* Green for winner */
        text-align: center;
        padding: 15px;
        border: 2px dashed var(--secondary-color);
        border-radius: 8px;
        background-color: #d4edda; /* Light green background */
         opacity: 0;
         transform: translateY(20px);
         transition: opacity var(--transition-speed) ease-in-out var(--transition-speed), transform var(--transition-speed) ease-in-out var(--transition-speed); /* Delay animation */
    }
     #final-result.visible {
         opacity: 1;
         transform: translateY(0);
     }

     #tie-message {
        margin-top: 10px;
        text-align: center;
        font-style: italic;
        color: #ffc107; /* Amber for warning */
     }


    #explanation ul {
        list-style-type: disc;
        margin-right: 20px;
        padding-right: 0; /* Reset default padding */
    }

    #explanation li {
        margin-bottom: 10px;
    }

    /* Loading Spinner Styles */
    .loading-spinner {
        border: 4px solid #f3f3f3; /* Light grey */
        border-top: 4px solid var(--primary-color); /* Blue */
        border-radius: 50%;
        width: 30px;
        height: 30px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .candidates {
            flex-direction: column;
            gap: 15px;
        }
        .candidate-card {
            flex: 1 1 100%;
        }
         .criteria {
             flex-direction: column;
             align-items: flex-end; /* Align items to the right in column layout */
         }
         .criteria label {
             margin-right: 0;
             margin-bottom: 5px;
             text-align: right;
             width: 100%; /* Labels take full width */
         }
         .rating-control {
             justify-content: flex-end; /* Align stars to the right */
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const simulateBtn = document.getElementById('simulate-btn');
        const simulationResultsDiv = document.getElementById('simulation-results');
        const committeeScoresDiv = document.getElementById('committee-scores');
        const finalResultDiv = document.getElementById('final-result');
        const tieMessageDiv = document.getElementById('tie-message');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const loadingSpinner = document.querySelector('.loading-spinner');
        const ratingControls = document.querySelectorAll('.rating-control');

        // Initialize Rating Controls
        ratingControls.forEach(control => {
            const stars = control.querySelectorAll('.rating-star');
            const hiddenInput = control.nextElementSibling; // Assuming hidden input is immediately after

            // Set initial state based on hidden input value
            const initialRating = parseInt(hiddenInput.value) || 3; // Default to 3
            control.dataset.rating = initialRating;
            stars.forEach(star => {
                 if (parseInt(star.dataset.value) <= initialRating) {
                     star.classList.add('filled');
                 }
            });


            stars.forEach(star => {
                star.addEventListener('click', () => {
                    const value = parseInt(star.dataset.value);
                    const currentControl = star.closest('.rating-control');
                    const input = currentControl.nextElementSibling;

                    // Update hidden input and data attribute
                    input.value = value;
                    currentControl.dataset.rating = value;

                    // Update visual state
                    const allStarsInControl = currentControl.querySelectorAll('.rating-star');
                    allStarsInControl.forEach(s => {
                        if (parseInt(s.dataset.value) <= value) {
                            s.classList.add('filled');
                        } else {
                            s.classList.remove('filled');
                        }
                    });
                });

                // Optional: Add hover effect to highlight stars
                star.addEventListener('mouseover', () => {
                     const value = parseInt(star.dataset.value);
                     const currentControl = star.closest('.rating-control');
                     const allStarsInControl = currentControl.querySelectorAll('.rating-star');
                     allStarsInControl.forEach(s => {
                        if (parseInt(s.dataset.value) <= value) {
                             s.classList.add('hover-highlight');
                        } else {
                             s.classList.remove('hover-highlight');
                        }
                     });
                });

                 star.addEventListener('mouseout', () => {
                    const currentControl = star.closest('.rating-control');
                     const allStarsInControl = currentControl.querySelectorAll('.rating-star');
                      allStarsInControl.forEach(s => s.classList.remove('hover-highlight'));
                      // Reapply filled state based on current rating
                     const currentRating = parseInt(currentControl.dataset.rating);
                      allStarsInControl.forEach(s => {
                        if (parseInt(s.dataset.value) <= currentRating) {
                             s.classList.add('filled');
                         } else {
                             s.classList.remove('filled');
                         }
                     });
                });

            });
        });


        // Virtual Committee Members and their predetermined scores (scaled 1-5)
        // Slightly adjust scores for more nuanced outcomes
        const virtualCommittee = {
            sarah_goldman: { // Emphasizes originality/research
                name: "פרופ' שרה גולדמן",
                cohen: { originality: 5, impact: 3, scope: 4 },
                levi: { originality: 2, impact: 4, scope: 3 },
                shapira: { originality: 3, impact: 4, scope: 5 }
            },
            yosef_mizrahi: { // Emphasizes public impact/popularity
                 name: "ד''ר יוסף מזרחי",
                cohen: { originality: 3, impact: 2, scope: 3 },
                levi: { originality: 5, impact: 5, scope: 4 },
                shapira: { originality: 4, impact: 4, scope: 4 }
            },
            miriam_katz: { // Emphasizes cultural/educational contribution and scope
                name: "מרים כץ",
                cohen: { originality: 4, impact: 3, scope: 4 },
                levi: { originality: 4, impact: 5, scope: 4 },
                shapira: { originality: 5, impact: 5, scope: 5 }
            },
            dov_rosen: { // More balanced, slightly favors established figures
                 name: "עו''ד דב רוזן",
                 cohen: { originality: 4, impact: 4, scope: 5 },
                 levi: { originality: 4, impact: 4, scope: 3 },
                 shapira: { originality: 4, impact: 5, scope: 4 }
            }
        };

        const candidateNames = {
            cohen: "פרופ' אהרון כהן",
            levi: "ד\"ר רות לוי",
            shapira: "פרופ' דוד שפירא"
        };

        const criterionNames = {
             originality: "מקוריות התרומה",
             impact: "השפעה (תחום/ציבור)",
             scope: "היקף ורציפות פעילות"
        };


        simulateBtn.addEventListener('click', () => {
            // Disable button and show spinner
            simulateBtn.disabled = true;
            loadingSpinner.classList.remove('hidden');
             simulationResultsDiv.classList.remove('visible'); // Hide previous results smoothly
             finalResultDiv.classList.remove('visible');
             tieMessageDiv.classList.add('hidden');


            // Collect user ratings
            const userRatings = {};
            document.querySelectorAll('.rating').forEach(input => {
                const candidate = input.dataset.candidate;
                const criterion = input.dataset.criterion;
                const rating = parseInt(input.value);

                if (!userRatings[candidate]) {
                    userRatings[candidate] = {};
                }
                 // Ensure rating is within 1-5, default to 3 if invalid
                userRatings[candidate][criterion] = rating >= 1 && rating <= 5 ? rating : 3;
            });

            // Simulate committee discussion delay
            setTimeout(() => {
                const allCommitteeScores = {};
                const candidates = Object.keys(candidateNames);
                const criteria = Object.keys(criterionNames);
                const totalCommitteeMembers = Object.keys(virtualCommittee).length + 1; // User + virtual members

                candidates.forEach(candidateKey => {
                    allCommitteeScores[candidateKey] = {};
                    criteria.forEach(criterionKey => {
                        let totalScore = userRatings[candidateKey][criterionKey];

                        for (const memberKey in virtualCommittee) {
                            // Ensure virtual member has scores for this candidate/criterion
                             if (virtualCommittee[memberKey][candidateKey] && virtualCommittee[memberKey][candidateKey][criterionKey] !== undefined) {
                                 totalScore += virtualCommittee[memberKey][candidateKey][criterionKey];
                             } else {
                                // Fallback or handle missing scores if necessary
                                 totalScore += 3; // Assume average if data missing
                             }
                        }
                        allCommitteeScores[candidateKey][criterionKey] = totalScore / totalCommitteeMembers;
                    });
                });

                // Calculate final average score for each candidate (average across criteria)
                const finalCandidateScores = {};
                candidates.forEach(candidateKey => {
                     let totalCandidateScore = 0;
                     criteria.forEach(criterionKey => {
                         totalCandidateScore += allCommitteeScores[candidateKey][criterionKey];
                     });
                     finalCandidateScores[candidateKey] = totalCandidateScore / criteria.length;
                });


                // Determine the winner(s)
                let winningCandidates = [];
                let highestScore = -1;

                for (const candidateKey in finalCandidateScores) {
                    if (finalCandidateScores[candidateKey] > highestScore) {
                        highestScore = finalCandidateScores[candidateKey];
                        winningCandidates = [candidateKey]; // Start new list with this candidate
                    } else if (finalCandidateScores[candidateKey] === highestScore) {
                        winningCandidates.push(candidateKey); // Add tied candidate
                    }
                }

                // Display results
                committeeScoresDiv.innerHTML = '<h4>ציוני הוועדה הממוצעים (משוקלל, כולל הדירוג שלך):</h4>';
                candidates.forEach(candidateKey => {
                     let scoreHtml = `<strong>${candidateNames[candidateKey]}:</strong> `;
                     criteria.forEach((criterionKey, index) => {
                          scoreHtml += `${criterionNames[criterionKey]}: <span style="color: ${allCommitteeScores[candidateKey][criterionKey] >= 4 ? 'green' : allCommitteeScores[candidateKey][criterionKey] >= 3 ? 'orange' : 'red'}; font-weight: bold;">${allCommitteeScores[candidateKey][criterionKey].toFixed(2)}</span>`;
                          if (index < criteria.length - 1) scoreHtml += ' | ';
                     });
                     scoreHtml += `<br>ציון סופי ממוצע: <span style="font-size: 1.1em; color: ${finalCandidateScores[candidateKey] >= 4 ? 'green' : finalCandidateScores[candidateKey] >= 3 ? 'orange' : 'red'}; font-weight: bold;">${finalCandidateScores[candidateKey].toFixed(2)}</span>`;
                     committeeScoresDiv.innerHTML += `<div>${scoreHtml}</div>`;
                });

                if (winningCandidates.length === 1) {
                    const winnerKey = winningCandidates[0];
                     finalResultDiv.innerHTML = `<h4>הזוכה בפרס ישראל השנה הוא/היא: <span style="color: var(--primary-dark);">${candidateNames[winnerKey]}</span>!</h4>`;
                     finalResultDiv.innerHTML += `<p>בחירה זו משקפת את ממוצע ההערכות של הוועדה כולה, המשלב את העדפותיך עם עמדות חברי הוועדה הווירטואליים.</p>`;
                     tieMessageDiv.classList.add('hidden');

                } else {
                     // Handle Tie
                     const tiedNames = winningCandidates.map(key => candidateNames[key]).join(' ו');
                     finalResultDiv.innerHTML = `<h4>תוצאת תיקו! מספר מועמדים הגיעו לציון הממוצע הגבוה ביותר: <span style="color: var(--primary-dark);">${tiedNames}</span>.</h4>`;
                     finalResultDiv.innerHTML += `<p>במצב כזה, הוועדה לרוב מקיימת דיון נוסף ומצמצמת את האפשרויות עד להגעה להכרעה או פשרה.</p>`;
                      tieMessageDiv.classList.remove('hidden'); // Optional: Add specific tie message if needed
                }


                // Display results with animation
                simulationResultsDiv.classList.add('visible');
                 finalResultDiv.classList.add('visible');

                // Hide spinner and enable button
                loadingSpinner.classList.add('hidden');
                simulateBtn.disabled = false;

            }, 1500); // Simulate a 1.5-second discussion time

        });

        toggleExplanationBtn.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
             // Smooth transition for explanation div
             if (!explanationDiv.classList.contains('hidden')) {
                  // For showing: remove hidden, allow content to dictate height, then transition
                  explanationDiv.style.maxHeight = '0px'; // Start from closed state
                  explanationDiv.classList.remove('hidden');
                   // Use a small delay to allow display:block to apply before transition
                   setTimeout(() => {
                     explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 20 + 'px'; // Set to actual height + some buffer
                   }, 10); // Small delay
             } else {
                  // For hiding: set height to current scroll height, then transition to 0
                  explanationDiv.style.maxHeight = explanationDiv.scrollHeight + 20 + 'px';
                  setTimeout(() => {
                      explanationDiv.style.maxHeight = '0px';
                   }, 10); // Small delay
                  explanationDiv.addEventListener('transitionend', function handler() {
                      explanationDiv.classList.add('hidden');
                       explanationDiv.removeEventListener('transitionend', handler);
                  });
             }

            if (explanationDiv.classList.contains('hidden')) {
                toggleExplanationBtn.textContent = 'רוצה/ה לדעת עוד? הצג/הסתר הסבר על פרס ישראל ותהליך השיפוט';
            } else {
                toggleExplanationBtn.textContent = 'הסתר הסבר';
            }
        });

         // Initial state for explanation (hidden by default)
         explanationDiv.classList.add('hidden');
         explanationDiv.style.maxHeight = '0px'; // Ensure it starts closed for the animation
         explanationDiv.style.overflow = 'hidden';
         explanationDiv.style.transition = 'max-height var(--transition-speed) ease-in-out';

    });
</script>