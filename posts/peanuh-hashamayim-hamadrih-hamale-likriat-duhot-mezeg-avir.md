---
title: "פענוח השמיים: המדריך האינטראקטיבי לקריאת דוחות מזג אוויר"
english_slug: peanuh-hashamayim-hamadrih-hamale-likriat-duhot-mezeg-avir
category: "מדעי האטמוספרה"
tags: [מטאורולוגיה, מזג אוויר, חיזוי, דוחות מזג אוויר, אטמוספירה, אינטראקטיבי, סימולציה]
---
# פענוח השמיים: המדריך האינטראקטיבי לקריאת דוחות מזג אוויר

אי פעם הסתכלתם על תחזית מזג אוויר וקיבלתם רק אייקון פשוט? האייקון הזה מספר רק חלק קטן מהסיפור האמיתי. מטאורולוגים, טייסים וימאים משתמשים בדוחות מזג אוויר מקודדים ועשירים בפרטים מדויקים. מוכנים לפענח את השפה הסודית של השמיים? בואו נצלול פנימה ונתרגל!

<div class="weather-app">
    <div class="app-header">פענוח דוח מזג אוויר - תרגול</div>
    <div id="weather-report-display" class="report-display">
        <p>טוען את דוח מזג האוויר...</p>
    </div>
     <div class="icon-representation">
         <!-- Visual representation will be added here by JS -->
     </div>
    <div id="question-area" class="question-area">
        <p>טוען שאלה...</p>
    </div>
    <div id="options-area" class="options-area">
        <!-- Answer buttons will be added here by JS -->
    </div>
    <div id="feedback-area" class="feedback-area">
        <!-- Feedback and explanation will appear here -->
    </div>
</div>

<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #28a745;
        --background-color: #e0f7fa; /* Light cyan */
        --container-bg: #ffffff;
        --border-color: #b3e5fc; /* Light blue */
        --correct-color: #28a745;
        --incorrect-color: #dc3545;
        --text-color: #333;
        --header-bg: #0056b3;
        --header-text: #ffffff;
        --subtle-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        --button-hover-bg: #0056b3;
        --button-hover-text: #ffffff;
    }

    .weather-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 650px;
        margin: 30px auto;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background: linear-gradient(to bottom right, var(--container-bg), #e1f5fe); /* Soft gradient */
        box-shadow: var(--subtle-shadow);
        color: var(--text-color);
        position: relative; /* For potential animations */
        overflow: hidden; /* Keep animations inside */
    }

    .app-header {
        background-color: var(--header-bg);
        color: var(--header-text);
        padding: 12px 20px;
        margin: -25px -25px 25px -25px; /* Extend header to edges */
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        font-size: 1.4em;
        font-weight: bold;
        text-align: center;
        box-shadow: var(--subtle-shadow);
    }


    .report-display {
        font-family: 'Courier New', monospace; /* Monospaced font for report */
        font-size: 1.2em;
        margin-bottom: 20px;
        padding: 15px;
        background-color: #eef; /* Light blue tint */
        border: 1px dashed var(--border-color);
        border-radius: 6px;
        white-space: pre-wrap; /* Preserves formatting */
        overflow-x: auto; /* Scroll if report is too wide */
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
        opacity: 0; /* Start hidden for animation */
        transform: translateY(-10px);
        animation: fadeInSlideDown 0.6s ease-out forwards;
    }

     .icon-representation {
         text-align: center;
         margin-bottom: 20px;
         min-height: 50px; /* Reserve space */
     }

     .weather-icon {
         font-size: 2.5em;
         margin: 0 10px;
         display: inline-block;
         opacity: 0;
         animation: fadeInPop 0.5s ease-out forwards;
     }

     .weather-icon.wind { animation-delay: 0.2s; }
     .weather-icon.temp { animation-delay: 0.4s; }
     .weather-icon.pressure { animation-delay: 0.6s; }


    .question-area {
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 20px;
        color: var(--header-bg);
        opacity: 0; /* Start hidden */
        transform: translateY(-10px);
        animation: fadeInSlideDown 0.6s ease-out forwards;
        animation-delay: 0.3s; /* Delay after report */
    }

    .options-area {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
        opacity: 0; /* Start hidden */
        animation: fadeIn 0.6s ease-out forwards;
        animation-delay: 0.6s; /* Delay after question */
    }

    .option-button {
        padding: 12px 20px;
        border: 2px solid var(--primary-color);
        border-radius: 8px;
        background-color: var(--container-bg);
        color: var(--primary-color);
        cursor: pointer;
        font-size: 1.1em;
        text-align: right;
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.1s ease;
        box-shadow: var(--subtle-shadow);
        width: 100%; /* Make buttons full width */
    }

    .option-button:hover:not([disabled]) {
        background-color: var(--button-hover-bg);
        color: var(--button-hover-text);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .option-button:active:not([disabled]) {
         transform: translateY(0);
         box-shadow: var(--subtle-shadow);
    }

     .option-button[disabled] {
         opacity: 0.7;
         cursor: not-allowed;
         box-shadow: none;
     }

    .feedback-area {
        margin-top: 20px;
        padding: 15px;
        border-radius: 8px;
        opacity: 0; /* Start hidden */
        transform: translateY(10px);
        animation: fadeInSlideUp 0.5s ease-out forwards;
    }

    .feedback.correct {
        background-color: #d4edda; /* Light green */
        color: var(--correct-color);
        border: 1px solid #c3e6cb;
    }

    .feedback.incorrect {
        background-color: #f8d7da; /* Light red */
        color: var(--incorrect-color);
        border: 1px solid #f5c6cb;
    }

    .feedback p {
        margin-bottom: 10px;
        font-weight: bold;
    }

    .explanation {
        margin-top: 10px;
        font-size: 1em;
        line-height: 1.6;
        color: var(--text-color);
        border-top: 1px dashed rgba(0,0,0,0.1);
        padding-top: 10px;
    }

    .next-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.2em;
        cursor: pointer;
        margin-top: 15px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: var(--subtle-shadow);
    }

    .next-button:hover {
        background-color: #218838;
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
     .next-button:active {
         transform: translateY(0);
         box-shadow: var(--subtle-shadow);
     }

    .toggle-explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: var(--subtle-shadow);
    }

    .toggle-explanation-button:hover {
        background-color: #5a6268;
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
     .toggle-explanation-button:active {
         transform: translateY(0);
         box-shadow: var(--subtle-shadow);
     }

    #full-explanation {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
        box-shadow: var(--subtle-shadow);
    }

    #full-explanation h2, #full-explanation h3 {
        color: var(--header-bg);
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 5px;
    }

    #full-explanation p, #full-explanation ul {
        line-height: 1.7;
        margin-bottom: 15px;
        font-size: 1em;
        color: var(--text-color);
    }

    #full-explanation ul {
        padding-right: 25px;
        list-style-type: disc;
    }

     #full-explanation ul ul {
         padding-right: 15px;
         margin-bottom: 8px;
     }

    /* Animations */
     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }

    @keyframes fadeInSlideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInSlideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInPop {
         from { opacity: 0; transform: scale(0.8); }
         to { opacity: 1; transform: scale(1); }
    }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.02); }
         100% { transform: scale(1); }
     }

     .feedback.correct p { animation: pulse 0.8s ease-in-out 2; /* Pulse twice */ }

</style>

<button class="toggle-explanation-button" id="toggle-explanation">הצגת מדריך הפענוח המלא</button>

<div id="full-explanation" style="display: none;">
    <h2>מדריך מורחב לפענוח דוחות מזג אוויר</h2>

    <p>דוחות מטאורולוגיים, כמו METAR (Meteorological Aerodrome Report), הם כלי קריטי להבנת תנאי מזג אוויר מדויקים בזמן אמת. הם משמשים לא רק טייסים, אלא גם כל מי שעוסק בתכנון רגיש למזג אוויר. בואו נפרוט את הרכיבים העיקריים שתפגשו:</p>

    <h3>מבנה כללי ורכיבים עיקריים</h3>
    <p>דוח METAR מלא מכיל רכיבים רבים, אך בגרסה המפושטת שלנו, נתמקד באלה:</p>
    <ul>
        <li>**סמלים ותיאור כללי:** סמלים ויזואליים המייצגים מצב בסיסי (שמש, ענן, גשם, ערפל).</li>
        <li>**קוד מצב שמיים/ראות:** לדוגמה, SKC (שמיים נקיים), OVC (מעונן לחלוטין), או קודים המציינים ראות ירודה כמו FG (ערפל).</li>
        <li>**נתוני רוח:** כיוון ומהירות.</li>
        <li>**טמפרטורה ונקודת טל:** טמפרטורת האוויר והטמפרטורה בה האוויר יגיע לרוויה.</li>
        <li>**לחץ ברומטרי (QNH):** לחץ האוויר המותאם לגובה פני הים.</li>
    </ul>

    <h3>פענוח רכיבים: פירוט מעמיק</h3>

    <h4>עננות וראות</h4>
    <ul>
        <li>**ראות (Visibility):** המרחק המרבי בו ניתן לראות אובייקטים.
            <ul>
                <li>`CAVOK` (Ceiling and Visibility OK): ראות מעל 10 ק"מ, ללא עננים משמעותיים מתחת ל-1500 מטר וללא תופעות מזג אוויר.</li>
                <li>`9999`: ראות 10 ק"מ ומעלה.</li>
                <li>מספרים כמו `0800` או `5000`: מציינים ראות ב מטרים (800 מטר, 5 ק"מ). ראות נמוכה יכולה להיגרם מ:
                    <ul>
                        <li>`FG` (Fog): ערפל (ראות < 1000 מטר).</li>
                        <li>`BR` (Mist): אד/ערפילי ים (ראות 1000-5000 מטר).</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li>**עננות (Cloud Cover):** מציינת כמה מהשמיים מכוסים בעננים ובאיזה גובה. הכיסוי נמדד בשמיניות (אוקטות), והגובה במאות רגל.
            <ul>
                <li>`SKC` (Sky Clear) / `CLR` (Clear): 0/8 כיסוי - שמיים בהירים.</li>
                <li>`FEW` (Few): 1-2/8 כיסוי - מעט עננים.</li>
                <li>`SCT` (Scattered): 3-4/8 כיסוי - עננות מפוזרת.</li>
                <li>`BKN` (Broken): 5-7/8 כיסוי - מעונן חלקית עד כמעט מלא ("שמיים שבורים").</li>
                <li>`OVC` (Overcast): 8/8 כיסוי - שמיים מכוסים לחלוטין.</li>
                <li>המספר שאחרי הקוד (לדוגמה, `SCT030`) הוא הגובה במאות רגל (3000 רגל).</li>
            </ul>
        </li>
    </ul>

    <h4>משקעים ותופעות מזג אוויר</h4>
    <p>קודים דו- או תלת-אותיים מתארים תופעות משמעותיות (Present Weather):</p>
    <ul>
        <li>עוצמה: `-` (קל), `+` (כבד), אין סימון (בינוני).</li>
        <li>סוג: `RA` (גשם), `SN` (שלג), `DZ` (גשם קל), `GR` (ברד).</li>
        <li>תיאור/מאפיין: `TS` (סופת רעמים), `FG` (ערפל), `BR` (אד), `SS` (סופת חול), `SQ` (סקווול).</li>
    </ul>
    <p>**דוגמאות נפוצות:** `-RA` (גשם קל), `+TSRA` (סופת רעמים עם גשם כבד), `FG` (ערפל), `BR` (אד), `VCSH` (גשם קל בסביבה הקרובה).</p>

    <h4>נתוני רוח</h4>
    <p>הפורמט הוא DDDVVVKT, לעיתים עם GFFFKT:</p>
    <ul>
        <li>`DDD`: כיוון הרוח במעלות מתוך הצפון האמיתי (000-360). `VRB` מציין רוח משתנה כיוון.</li>
        <li>`VVV`: מהירות הרוח בקשרים (KT - Knots). 1 קשר ≈ 1.85 קמ"ש.</li>
        <li>`GFFF`: מופיע אם יש משבים (Gusts) - FFF היא מהירות המשב המקסימלית.</li>
        <li>**דוגמה:** `27015KT` (רוח ממערב, 270°, 15 קשר). `36020G35KT` (רוח מצפון, 360°, 20 קשר, משבים עד 35 קשר). `VRB05KT` (רוח משתנה, 5 קשר).</li>
    </ul>

    <h4>טמפרטורה ונקודת טל</h4>
    <p>הפורמט TT/TD:</p>
    <ul>
        <li>`TT`: טמפרטורת האוויר בצלזיוס. `M` לפני מספר מציינת מינוס. (לדוגמה, `18` = 18°C, `M03` = -3°C).</li>
        <li>`TD`: טמפרטורת נקודת הטל בצלזיוס (גם כאן, `M` למינוס). נקודת הטל היא הטמפרטורה בה האוויר מתחיל להתעבות. ככל שהטמפרטורה קרובה יותר לנקודת הטל, כך האוויר לח יותר והסיכוי לערפל או משקעים גבוה יותר.</li>
        <li>**דוגמה:** `20/15` (טמפרטורה 20°C, נקודת טל 15°C). `M05/M06` (טמפרטורה -5°C, נקודת טל -6°C).</li>
    </ul>

    <h4>לחץ ברומטרי</h4>
    <p>הפורמט QPPPP:</p>
    <ul>
        <li>`Q`: קוד המציין שמדובר בלחץ ברומטרי המותאם לגובה פני הים (QNH).</li>
        <li>`PPPP`: ערך הלחץ בהקטו-פסקל (hPa).</li>
        <li>**דוגמה:** `Q1018` (לחץ 1018 hPa). לחץ גבוה לרוב מצביע על מזג אוויר יציב, ולחץ נמוך על מערכת לא יציבה.</li>
    </ul>

    <p>הדוחות בתרגול זה הם גרסאות מפושטות המכילות את הרכיבים העיקריים כדי לאפשר לכם להתמקד בלמידה.</p>
</div>

<script>
    const weatherData = [
        {
            report: "☀️ SKC 💨 05010KT 🌡️ 25°C/10°C 📊 1020hPa",
            question: "מתכננים טיול רגלי בהרים מחר. מה ניתן להסיק מדוח מזג האוויר הזה?",
            options: [
                "צפוי גשם חזק וערפל, כדאי לבטל.",
                "מזג אוויר בהיר ויבש, מתאים לטיול, אך שימו לב להפרש הטמפרטורות (יובש).",
                "רוחות עזות שיקשו על ההליכה בשטח פתוח.",
                "צפוי שלג וטמפרטורות מתחת לאפס."
            ],
            correctAnswerIndex: 1,
            explanation: "הדוח מצביע על: SKC (שמיים בהירים), רוח קלה יחסית (10 קשר) מכיוון 050, טמפרטורה נעימה (25°C), נקודת טל נמוכה (10°C) המעידה על אוויר יבש, ולחץ גבוה (1020hPa) המעיד על יציבות אטמוספרית. הפרש גדול בין טמפרטורה לנקודת טל מרמז על לחות נמוכה ויובש. התנאים אידיאליים לטיול רגלי, רק חשוב לזכור שתנאי יובש יכולים להשפיע (למשל, להתייבשות).",
            icons: ["☀️"]
        },
        {
            report: "☁️ OVC ☔ -RA 💨 27015KT 🌡️ 12°C/11°C 📊 1005hPa",
            question: "האם כדאי לתכנן פיקניק בפארק הפתוח היום אחר הצהריים?",
            options: [
                "כן, מזג האוויר מתאים לפעילות בחוץ ויהיה שמשי.",
                "לא, צפוי כיסוי עננים מלא, גשם קל ורוחות בינוניות.",
                "כן, אך רק בשעות הבוקר המוקדמות לפני הגשם.",
                "רק אם הפארק נמצא באזור מדברי יבש וללא עננים."
            ],
            correctAnswerIndex: 1,
            explanation: "הדוח מראה: OVC (כיסוי עננים מלא), -RA (גשם קל), רוח מערבית (270 מעלות) בינונית (15 קשר), טמפרטורה 12°C ונקודת טל 11°C (מעיד על אוויר רווי וסכנת ערפל או גשם מתמשך), ולחץ נמוך (1005hPa) שיכול להצביע על מערכת פעילה. תנאים אלו אינם מתאימים לפיקניק בפארק פתוח.",
            icons: ["☁️", "☔"]
        },
        {
            report: "🌫️ FG 💨 01005KT 🌡️ 8°C/8°C 📊 1012hPa",
            question: "אתם צריכים לנהוג בכביש מהיר בשעת בוקר מוקדמת. מה המשמעות העיקרית של דוח זה?",
            options: [
                "ראות מעולה ורוחות קלות לנסיעה מהירה.",
                "צפויה סופת רעמים, כדאי להימנע מנהיגה.",
                "קיים ערפל כבד שמגביל משמעותית את הראות.",
                "מזג אוויר בהיר וקר, אין בעיה מיוחדת בנהיגה."
            ],
            correctAnswerIndex: 2,
            explanation: "הדוח מציג: FG (ערפל), רוח קלה מאוד (5 קשר), טמפרטורה ונקודת טל זהות (8°C/8°C) מה שמעיד על רוויית אוויר וסבירות גבוהה לערפל. ערפל מגביל מאוד את הראות ומסוכן לנהיגה, במיוחד בכביש מהיר.",
            icons: ["🌫️"]
        },
         {
            report: "☁️ BKN020 💨 VRB03KT 🌡️ 18°C/16°C 📊 1010hPa",
            question: "האם כדאי לצאת לשייט קצר בים הפתוח בספינה קטנה לפי הדוח?",
            options: [
                "כן, הים שקט והראות צפויה להיות מצוינת.",
                "כן, אבל יש סיכוי לרוחות חזקות פתאומיות מהים.",
                "לא, יש כיסוי עננים נמוך, אוויר לח ורוח משתנה קלה שאינם אידיאליים לשייט קטן.",
                "מזג אוויר מושלם לכל סוג שייט, כולל סירות מפרש."
            ],
            correctAnswerIndex: 2,
            explanation: "הדוח מציין: BKN020 (עננות משמעותית בגובה 2000 רגל), VRB03KT (רוח קלה מאוד ומשתנה כיוון), טמפרטורה 18°C ונקודת טל 16°C (אוויר לח למדי). כיסוי עננים נמוך (BKN) ורוח קלה ומשתנה אינם אידיאליים לשייט בספינה קטנה בים פתוח, ונקודת הטל הקרובה לטמפרטורה מגבירה את הסיכוי לגשם קל או אד (BR) שיכול להגביל ראות.",
            icons: ["☁️"]
        },
         {
            report: "☀️ FEW050 💨 32025G40KT 🌡️ 20°C/5°C 📊 1018hPa",
            question: "מתכננים טיול אופניים ביער. מה הסיכון העיקרי לפי דוח זה שכדאי לקחת בחשבון?",
            options: [
                "גשם כבד ובוץ שיקשו על הרכיבה.",
                "טמפרטורות קיצוניות שידרשו לבוש מיוחד.",
                "רוחות חזקות ומשבים שעלולים להפיל ענפים או עצמים.",
                "ראות נמוכה עקב ערפל סמיך בתוך היער."
            ],
            correctAnswerIndex: 2,
            explanation: "הדוח מציין: FEW050 (מעט עננים גבוהים יחסית), 32025G40KT (רוח חזקה יחסית מצפון מערב, 25 קשר, עם משבים חזקים עד 40 קשר), טמפרטורה 20°C ונקודת טל 5°C (אוויר יבש). רוחות ומשבים חזקים ביער יכולים להוות סכנה של נפילת ענפים או עצמים אחרים, ולקשות על השליטה באופניים. זהו הסיכון העיקרי לפי הדוח.",
            icons: ["☀️", "💨"]
        }
    ];

    let currentQuestionIndex = 0;
    const reportDisplay = document.getElementById('weather-report-display');
    const questionArea = document.getElementById('question-area');
    const optionsArea = document.getElementById('options-area');
    const feedbackArea = document.getElementById('feedback-area');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const iconRepresentationArea = document.querySelector('.icon-representation'); // New area for icons

    function displayQuestion(index) {
        // Clear previous elements and animations
        feedbackArea.innerHTML = '';
        feedbackArea.className = 'feedback-area'; // Reset class
        optionsArea.innerHTML = '';
        iconRepresentationArea.innerHTML = ''; // Clear icons

        const data = weatherData[index];

        // Add animations before setting text
        reportDisplay.style.opacity = 0;
        reportDisplay.style.transform = 'translateY(-20px)';
        questionArea.style.opacity = 0;
        questionArea.style.transform = 'translateY(-20px)';
        optionsArea.style.opacity = 0;


        // Set text content
        reportDisplay.innerText = "דוח מזג האוויר:\n" + data.report;
        questionArea.innerText = data.question;

        // Add visual icons with animation delay
        data.icons.forEach((icon, i) => {
             const span = document.createElement('span');
             span.classList.add('weather-icon');
             // Add specific classes for potential different icon animations later
             if (icon === "💨") span.classList.add('wind');
             if (icon === "🌡️") span.classList.add('temp');
             if (icon === "📊") span.classList.add('pressure');
             span.innerText = icon;
             // Apply animation with delay
             span.style.animation = `fadeInPop 0.5s ease-out forwards ${0.1 * i + 0.8}s`; // Staggered animation
             iconRepresentationArea.appendChild(span);
        });


        // Animate in the report and question
        setTimeout(() => {
             reportDisplay.style.opacity = 1;
             reportDisplay.style.transform = 'translateY(0)';
        }, 50); // Small delay to ensure transition fires

        setTimeout(() => {
            questionArea.style.opacity = 1;
            questionArea.style.transform = 'translateY(0)';
        }, 300); // Delay question animation

        // Populate and animate in options
        setTimeout(() => {
            data.options.forEach((option, i) => {
                const button = document.createElement('button');
                button.classList.add('option-button');
                button.innerText = option;
                button.onclick = () => handleAnswer(i);
                // Add animation with delay
                button.style.opacity = 0;
                button.style.transform = 'translateY(20px)';
                button.style.animation = `fadeInSlideUp 0.5s ease-out forwards ${0.1 * i}s`; // Staggered animation
                optionsArea.appendChild(button);
            });
             optionsArea.style.opacity = 1; // This opactiy might be overridden by child animations, reconsider
        }, 600); // Delay option population and animation

    }

    function handleAnswer(selectedIndex) {
        const data = weatherData[currentQuestionIndex];
        const isCorrect = selectedIndex === data.correctAnswerIndex;

        // Disable all option buttons
        optionsArea.querySelectorAll('.option-button').forEach((button, i) => {
            button.disabled = true;
            // Optional: Style correct/incorrect answer button
            if (i === data.correctAnswerIndex) {
                 button.style.borderColor = var(--correct-color);
                 button.style.color = var(--correct-color);
                 button.style.fontWeight = 'bold';
            } else {
                 button.style.opacity = 0.5; // Fade out incorrect options
            }
            if (i === selectedIndex && !isCorrect) {
                 button.style.borderColor = var(--incorrect-color);
                 button.style.color = var(--incorrect-color);
                  button.style.fontWeight = 'bold';
            }
        });

        feedbackArea.innerHTML = ''; // Clear previous feedback

        const feedbackText = document.createElement('p');
        if (isCorrect) {
            feedbackText.innerText = "🔥 נכון מאוד! פענוח מדויק! 🔥";
            feedbackArea.classList.add('correct');
        } else {
            feedbackText.innerText = "🧐 לא מדויק הפעם. בואו נראה למה... 👇";
            feedbackArea.classList.add('incorrect');
        }
        feedbackArea.appendChild(feedbackText);

        const explanationText = document.createElement('p');
        explanationText.classList.add('explanation');
        explanationText.innerText = "הסבר: " + data.explanation;
        feedbackArea.appendChild(explanationText);

        // Add Next button
        const nextButton = document.createElement('button');
        nextButton.classList.add('next-button');
        nextButton.innerText = currentQuestionIndex < weatherData.length - 1 ? 'שאלה הבאה >>' : 'סיימנו! ✨';
        nextButton.onclick = handleNext;
        feedbackArea.appendChild(nextButton);

        // Animate feedback area
        feedbackArea.style.opacity = 0;
        feedbackArea.style.transform = 'translateY(20px)';
        setTimeout(() => {
            feedbackArea.style.opacity = 1;
            feedbackArea.style.transform = 'translateY(0)';
        }, 50); // Small delay
    }

    function handleNext() {
        currentQuestionIndex++;
        if (currentQuestionIndex < weatherData.length) {
            displayQuestion(currentQuestionIndex);
        } else {
            // End of quiz
            reportDisplay.innerText = "✅ סיימתם את כל השאלות והפכתם למפענחי שמיים מתחילים!";
            reportDisplay.style.opacity = 1; reportDisplay.style.transform = 'translateY(0)'; // Ensure final message is visible
            questionArea.innerText = "כל הכבוד על התרגול! מקווים שנהניתם ולמדתם.";
            questionArea.style.opacity = 1; questionArea.style.transform = 'translateY(0)'; // Ensure final message is visible
            optionsArea.innerHTML = '';
             iconRepresentationArea.innerHTML = ''; // Clear icons
            feedbackArea.innerHTML = '';
            feedbackArea.className = 'feedback-area'; // Reset class

            // Add a restart button
            const restartButton = document.createElement('button');
            restartButton.classList.add('next-button');
            restartButton.innerText = '🔄 התחלה מחדש';
            restartButton.onclick = () => {
                currentQuestionIndex = 0;
                displayQuestion(currentQuestionIndex);
            };
             // Animate restart button
             restartButton.style.opacity = 0;
             restartButton.style.transform = 'scale(0.8)';
             setTimeout(() => {
                 restartButton.style.opacity = 1;
                 restartButton.style.transform = 'scale(1)';
             }, 300);
            feedbackArea.appendChild(restartButton);

        }
    }

    function toggleExplanation() {
        if (fullExplanationDiv.style.display === 'none') {
            fullExplanationDiv.style.display = 'block';
            toggleExplanationButton.innerText = 'הסתרת מדריך הפענוח המלא';
             // Optional: smooth scroll to explanation
             fullExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            fullExplanationDiv.style.display = 'none';
            toggleExplanationButton.innerText = 'הצגת מדריך הפענוח המלא';
        }
    }

    // Initialize the app
    displayQuestion(currentQuestionIndex);

    // Add event listener for the toggle button
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Initial check for explanation state on load (optional, but good practice)
    if (fullExplanationDiv.style.display === 'none') {
         toggleExplanationButton.innerText = 'הצגת מדריך הפענוח המלא';
    } else {
         toggleExplanationButton.innerText = 'הסתרת מדריך הפענוח המלא';
    }


</script>