---
title: "מפקד הצוללת: החלטה בעומק"
english_slug: nuclear-submarine-commander-decision-simulator
category: "מדעי החברה / פסיכולוגיה"
tags: ["קבלת החלטות", "לחץ קיצוני", "ניהול סיכונים", "סימולציה", "פסיכולוגיה צבאית", "מדעי ההתנהגות"]
---
# מפקד הצוללת: החלטה בעומק הים

אתה נמצא בעומק האוקיינוס השחור, מפקד על צוללת גרעינית מתקדמת במשימה חשאית. שקט מתוח שורר בבטן הברזל העצומה. לפתע, מידע קריטי מתפרץ מחדר הסונאר, נשמע כמו הד של גורל. הזמן אוזל בטירוף. האם תצליח לנווט בין אי-ודאות, רעשים ואיומים סמויים ולקבל את ההחלטה שתבטיח את הצלחת המשימה ואת חיי הצוות שלך, תחת לחץ בלתי נתפס?

<div class="submarine-simulator" id="submarine-simulator">
    <div class="sonar-animation"></div> <!-- Visual element for animation -->
    <div id="scenario" class="screen-text"></div>
    <div id="timer-container" class="screen-timer"><span id="timer"></span></div>
    <div id="options" class="options-panel"></div>
    <div id="results" class="screen-results"></div>
    <button id="start-button" class="control-button">התחל משימה / אתחל סימולציה</button>
</div>

<style>
    /* --- כללי ורקע --- */
    .submarine-simulator {
        direction: rtl;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Slightly more modern/techy font */
        max-width: 750px;
        margin: 20px auto;
        padding: 30px;
        border: 2px solid #0a4f82; /* Darker, richer blue border */
        border-radius: 12px;
        background: linear-gradient(180deg, #020f1f 0%, #011a35 100%); /* Deep sea gradient */
        color: #00ff00; /* Classic submarine green */
        box-shadow: 0 0 25px rgba(0, 255, 0, 0.4), inset 0 0 10px rgba(0, 255, 0, 0.2); /* More prominent glow */
        text-align: center;
        position: relative; /* Needed for absolute positioning of animations */
        overflow: hidden; /* Hide overflow from animations */
    }

    .submarine-simulator::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(0, 255, 0, 0.05) 0%, transparent 70%); /* Subtle center glow */
        pointer-events: none; /* Allow clicks through */
        z-index: 0;
    }

    /* --- אלמנטים תצוגה --- */
    .screen-text {
        margin-bottom: 25px;
        font-size: 1.2em; /* Slightly larger text */
        min-height: 90px; /* Reserve slightly more space */
        display: flex;
        align-items: center;
        justify-content: center;
        color: #e0e0e0; /* Lighter color for main text */
        line-height: 1.6;
        text-shadow: 0 0 5px rgba(0, 255, 0, 0.2);
    }

    .screen-timer {
        font-size: 1.8em; /* Larger timer */
        margin-bottom: 25px;
        color: #ffff00; /* Yellow for warning */
        min-height: 1.8em; /* Reserve space */
        font-weight: bold;
        text-shadow: 0 0 8px rgba(255, 255, 0, 0.4);
        transition: color 0.3s ease-in-out, text-shadow 0.3s ease-in-out;
    }

     .screen-timer.pulse-danger {
        color: #ff4500; /* OrangeRed for critical */
        text-shadow: 0 0 15px rgba(255, 69, 0, 0.8), 0 0 25px rgba(255, 69, 0, 0.6);
        animation: pulse 1s infinite step-end; /* Pulsing animation */
    }

     @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
     }

    .options-panel {
        margin-top: 20px;
        min-height: 120px; /* Reserve more space */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .option-button {
        display: block;
        width: 100%; /* Full width */
        max-width: 400px; /* Limit max width */
        margin: 10px auto;
        padding: 14px; /* More padding */
        background-color: #0a4f82; /* Blue-ish button */
        color: white;
        border: 1px solid #1f6cb0;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em; /* Slightly larger font */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    .option-button:hover:not(:disabled) {
        background-color: #1f6cb0;
        box-shadow: 0 0 10px rgba(31, 108, 176, 0.6);
        transform: translateY(-2px); /* Lift effect */
    }
     .option-button:active:not(:disabled) {
        background-color: #073a63; /* Darker on click */
        transform: translateY(0);
     }

     .option-button:disabled {
        background-color: #333;
        color: #999;
        border-color: #555;
        cursor: not-allowed;
        opacity: 0.7;
        text-shadow: none;
     }

    .screen-results {
        margin-top: 30px;
        font-size: 1.3em; /* Larger result text */
        font-weight: bold;
        min-height: 60px; /* Reserve space */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        line-height: 1.5;
    }

    .outcome.success {
        color: #32cd32; /* Lime green */
        text-shadow: 0 0 10px rgba(50, 205, 50, 0.6);
    }

    .outcome.failure_detected,
    .outcome.failure_catastrophic,
    .outcome.failure_timed_out {
        color: #dc143c; /* Crimson */
        text-shadow: 0 0 10px rgba(220, 20, 60, 0.6);
    }

     .outcome.mixed {
        color: #ffff00; /* Yellow */
        text-shadow: 0 0 10px rgba(255, 255, 0, 0.6);
    }

    .control-button {
        margin-top: 30px;
        padding: 12px 25px; /* More padding */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em; /* Slightly larger */
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    .control-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
     .control-button:active {
        background-color: #004080;
        transform: translateY(0);
     }


    /* --- אנימציית סונאר רקע (אופציונלי וויזואלי) --- */
    .sonar-animation {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: rgba(0, 255, 0, 0.2);
        transform: translate(-50%, -50%);
        pointer-events: none;
        z-index: 1; /* Below text/buttons */
        animation: sonarPulse 4s infinite ease-out; /* Adjust timing as needed */
    }

     @keyframes sonarPulse {
        0% {
            width: 10px;
            height: 10px;
            opacity: 0.7;
            margin-top: 0; margin-left: 0; /* Reset margins from translate */
            transform: translate(-50%, -50%) scale(1);
        }
         25% { opacity: 0.2; } /* Fade out slightly */
        100% {
             width: 300%; /* Expand */
            height: 300%; /* Expand */
            opacity: 0;
            margin-top: -150%; margin-left: -150%; /* Adjust margins for expansion from center */
            transform: translate(-50%, -50%) scale(1); /* Keep initial translate */
        }
     }

    /* --- הסבר תיאורטי --- */
    .explanation {
        margin-top: 50px; /* More space */
        padding: 25px;
        border-top: 2px solid #0a4f82;
        text-align: right;
        color: #cee; /* Slightly lighter color */
        background-color: #01101f; /* Very dark blue */
        border-radius: 10px;
        box-shadow: inset 0 0 8px rgba(0, 255, 0, 0.1);
    }

    .explanation h2 {
        color: #00ff00;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 0 0 8px rgba(0, 255, 0, 0.4);
    }

    .explanation h3 {
         color: #90ee90; /* Light green for subheadings */
         margin-top: 15px;
         margin-bottom: 8px;
    }

    .explanation p {
        margin-bottom: 15px;
        line-height: 1.7;
    }

    .explanation ul {
        list-style: disc inside;
        padding-right: 20px;
    }

    .explanation li {
        margin-bottom: 12px; /* More space between list items */
        line-height: 1.6;
    }

    /* Added style for the toggle button */
    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 10px 20px;
        background-color: #333; /* Dark grey */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-size: 1em;
    }
    #toggle-explanation:hover {
        background-color: #555;
        transform: translateY(-2px);
    }
     #toggle-explanation:active {
        background-color: #222;
        transform: translateY(0);
     }

    .hidden {
        display: none;
    }

    /* --- אנימציות כניסה לתוכן --- */
     /* Example: Fade in effect for scenario/results - requires JS to manage classes */
     /* .fade-in {
         animation: fadeIn 0.5s ease-out;
     }

     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     } */


</style>

<button id="toggle-explanation">הצג/הסתר הסבר תיאורטי ומעמיק</button>

<div id="explanation" class="explanation hidden">
    <h2>מאחורי ההחלטות: פסיכולוגיה של קבלת החלטות בלחץ קיצוני</h2>
    <p>הסימולציה שבה התנסית נועדה לדמות סיטואציה קריטית בתנאים של אי-ודאות גבוהה, לחץ זמן אדיר, ועומס פסיכולוגי כבד. מצבים כאלה דורשים קבלת החלטות מהירה ויעילה, והם שכיחים לא רק בזירות צבאיות, אלא גם בתחומים כמו רפואת חירום, שווקים פיננסיים תנודתיים, ניהול משברי אסון, ואף הכרעות חשובות בחיים האישיים והמקצועיים.</p>
    <p>כיצד המוח האנושי מתפקד תחת אש? אילו מנגנונים פסיכולוגיים נכנסים לפעולה, וכיצד ניתן לשפר את יכולת ההחלטה במצבי קיצון? הנה כמה מושגי מפתח:</p>

    <h3>מושגי יסוד בהבנת קבלת החלטות בלחץ:</h3>
    <ul>
        <li><strong>קבלת החלטות בתנאי אי-ודאות ולחץ קיצוני:</strong> תהליך בחירה תחת מגבלות קשות של מידע חלקי או סותר, זמן דחוק, ומשאבים מוגבלים, כאשר לתוצאות יש השפעה דרמטית. הלחץ הפיזיולוגי והפסיכולוגי משבשים יכולות קוגניטיביות חיוניות כמו קשב, זיכרון ושיקול דעת.</li>
        <li><strong>מודלים שונים של קבלת החלטות: רציונלי לעומת טבעי (NDM - Naturalistic Decision Making).</strong> בעוד המודל הרציונלי הקלאסי מניח עיבוד אינפורמציה מלא והערכת כל האפשרויות באופן שיטתי, NDM מתמקד באופן שבו אנשים מנוסים (כמו מפקדי צוללות, כבאים או מנתחים) מקבלים החלטות מהירות ויעילות בעולם האמיתי - לעיתים קרובות על בסיס זיהוי דפוסים מוכרים מהניסיון (Recognition-Primed Decision - RPD).</li>
        <li><strong>השפעת הלחץ הפסיכולוגי (סטרס) והפחד:</strong> לחץ חריף מפעיל את מערכת "הילחם או ברח" (Fight or Flight), המובילה לשחרור הורמונים המשפיעים על המוח. הדבר עלול לצמצם את טווח הקשב ("ראיית מנהרה"), לפגוע בזיכרון העבודה, להאט עיבוד מידע מורכב, ולעודד תגובות אימפולסיביות או לחלופין - שיתוק והיסוס.</li>
        <li><strong>עומס קוגניטיבי והקשבה סלקטיבית:</strong> כשהסביבה מוצפת במידע (רעשי סונאר, התרעות שונות), המוח עלול להגיע לעומס קוגניטיבי. בתנאי לחץ, יש נטייה לא מודעת להתמקד רק בגירויים הדומיננטיים ביותר או באלה שתואמים השערה ראשונית, תוך התעלמות ממידע חיוני אחר (Inattentional Blindness / Selective Attention).</li>
        <li><strong>הטיות קוגניטיביות והשפעתן:</strong> בתרחישים קריטיים, הטיות מנטליות נפוצות עלולות להוביל לשגיאות. לדוגמה: <strong>הטיית אישור (Confirmation Bias)</strong> - חיפוש מידע שמאשר את ההשערה הראשונית והתעלמות ממידע סותר; <strong>הטיית זמינות (Availability Heuristic)</strong> - הערכת סיכון לפי הקלות שבה עולים בזיכרון מקרים דומים (למשל, היזכרות באסון צוללות מהעבר).</li>
        <li><strong>התפקיד המכריע של ניסיון, אינטואיציה ואימון:</strong> ניסיון מעשיר את בנק הדפוסים המוכרים, מאפשר זיהוי מהיר של המצב ותגובה מותאמת (NDM). אינטואיציה במקרה זה אינה "תחושת בטן" בלבד, אלא תוצר של עיבוד תת-מודע מהיר של שנים של ניסיון וידע. אימון, ובמיוחד סימולציות ריאליסטיות כמו זו, בונה את היכולת לתפקד תחת לחץ, מקבע תגובות אוטומטיות נכונות, ומאפשר לזהות דפוסים חדשים במהירות.</li>
        <li><strong>קבלת החלטות בצוות:</strong> בסביבה כמו צוללת, החלטות הן לרוב צוותיות. תקשורת אפקטיבית, שיתוף מידע ברור ותמציתי (גם תחת עומס), הקשבה הדדית ויכולת לערער על הנחות - כל אלה קריטיים למניעת שגיאות ולהגעה להחלטה מיטבית.</li>
        <li><strong>יישום בחיי היומיום:</strong> עקרונות אלה רלוונטיים גם מחוץ לקוקפיט או לחדר הסונאר. הבנה כיצד לחץ משפיע עליך, מודעות להטיות קוגניטיביות נפוצות, פיתוח היכולת לעבד מידע מורכב במהירות, והבנת חשיבות הניסיון וההכנה (מנטלית ומעשית) - כל אלה יכולים לשפר משמעותית את יכולתך לקבל החלטות מושכלות ויעילות יותר גם במצבי אי-ודאות בחייך האישיים והמקצועיים.</li>
    </ul>
</div>

<script>
    const gameStages = {
        start: {
            scenario: "מוכן למשימה, מפקד? אנחנו מתקרבים לאזור הוכושל (נקודת המשימה). הסונאר מזהה קשר עמום במגזר 045, טווח בינוני. לא ניתן לזהות בוודאות את סוג הקשר. עומק נוכחי 200 מטר.",
            timer: 70, // Start with slightly more time
            options: [
                { text: "שנה נתיב מעט מזרחה לכיוון 045, בדוק האם הקשר סטטי.", nextStage: "stg_change_course" },
                { text: "הגבר מהירות ל-8 קשר כדי לחלוף מהר יותר על האזור.", nextStage: "stg_increase_speed" },
                { text: "צלול עמוק יותר ל-300 מטר, השתמש בשכבות טמפרטורה להסתתרות.", nextStage: "stg_dive_deeper" }, // Potential success path
                { text: "שלח פינג סונאר אקטיבי קצר לכיוון 045 לקבלת זיהוי ודאי.", nextStage: "end_active_ping_fail" } // Dangerous option
            ]
        },
        stg_change_course: {
            scenario: "שינית נתיב. הקשר במגזר 045 נשאר יחסית קבוע, טווח מתקצר. נראה גדול יותר כעת. האם הוא עוקב אחרינו או שהיה סטטי?",
            timer: 55,
            options: [
                { text: "התכונן להתחמקות חירום, כנראה מעקב.", nextStage: "stg_evade_prep" },
                { text: "שמור מהירות ונתיב נוכחיים, עקוב בדריכות אחר התפתחות הקשר.", nextStage: "stg_observe" },
                { text: "נסה לצלול עמוק יותר שוב, אולי יש עוד שכבת הסתרה.", nextStage: "stg_dive_deeper_2" } // Leads to new threat
            ]
        },
        stg_increase_speed: {
            scenario: "המהירות עולה ל-8 קשר. רעש המדחפים שלנו גובר משמעותית. קשר הסונאר האבוד ב-045 לא שב. האם בטוח להמשיך ברעש?",
            timer: 45,
            options: [
                { text: "האט מיד למהירות שקטה ונסה לאתר מחדש את הקשרים.", nextStage: "stg_slow_down" }, // Leads to new threat
                { text: "המשך במהירות גבוהה לנקודת הוכושל, בהנחה שהקשר היה לא רלוונטי.", nextStage: "end_risky_advance_fail" } // High risk fail
            ]
        },
        stg_dive_deeper: {
            scenario: "צללת לעומק 300 מטר. הלחץ על הגוף גובר, אך שכבות טמפרטורה עוזרות להסתרה. קשר הסונאר ב-045 דעך לגמרי, אבל נשמע רעש מכני חלש מאוד מהתחתית שאינו שלנו.",
            timer: 60, // More time if successful move
            options: [
                { text: "המשך לצלול בזהירות, אולי זה רעש טבעי או תקלה בצוללת שלנו שטרם איתרנו.", nextStage: "end_malfunction_fail" }, // Leads to disaster
                { text: "עלה מעט ל-250 מטר, בדוק קריאות סונאר נוספות ונסה לזהות את רעש התחתית.", nextStage: "stg_ascend_slight" } // Success path continues
            ]
        },
         stg_dive_deeper_2: { // Variation from stg_change_course
            scenario: "צללת שוב לעומק. הקשר ב-045 כמעט נעלם, כנראה התחמקת. אך... קשר חדש, קרוב מאוד ומאחור, הופיע לפתע בסונאר!",
            timer: 40,
            options: [
                { text: "שגר נגד סונאר (Decoy) והתחמק במהירות בכיוון ההפוך מהקשר.", nextStage: "end_deploy_decoy_outcome" }, // Potential outcome
                { text: "הגבר מהירות מקסימלית ונסה לברוח בקו ישר קדימה.", nextStage: "end_run_away_fail" } // Fail
            ]
         },
        stg_evade_prep: {
             scenario: "אתה מוכן להתחמקות. קשר האויב מתקרב במהירות, נראה שזיהה אותנו. טווח קצר! זו בהחלט צוללת עוינת.",
             timer: 25,
             options: [
                 { text: "בצע תמרון התחמקות חד ומפתיע - עכשיו!", nextStage: "end_evade_now_outcome" }, // Potential outcome based on time
                 { text: "חכה לרגע האחרון כדי לבצע תמרון מקסימלי.", nextStage: "end_evade_late_fail" } // High risk fail
             ]
        },
         stg_observe: {
             scenario: "אתה עוקב. הקשר הוא בהחלט צוללת זרה, ועוקבת אחריך במדויק! המשימה בסכנה, והזמן אוזל.",
             timer: 35,
             options: [
                 { text: "דווח מיד למטה את מיקומך המדויק ובקש פקודות דחופות.", nextStage: "end_report_under_fire_fail" }, // Fail - reporting under fire
                 { text: "נסה לשבור מגע בעומק רדוד יותר תוך שימוש בתנאי הים.", nextStage: "stg_break_contact_shallow" } // Leads to check
             ]
         },
         stg_slow_down: {
             scenario: "האטת למהירות שקטה. הסונאר סורק שוב. הקשר האבוד ב-045 לא נמצא, אבל... קשר חדש, חזק וקרוב, הופיע מאחור!",
             timer: 30,
             options: [
                 { text: "הגבר מהירות מקסימלית ונסה לברוח מהר.", nextStage: "end_run_away_fail" }, // Fail
                 { text: "פרוס מצוף הטעיה וצלול עמוק לשבירת מגע.", nextStage: "end_deploy_decoy_outcome" } // Potential outcome
             ]
         },
         stg_ascend_slight: {
             scenario: "עלית מעט ל-250 מטר. רעש התחתית הפסיק. הסונאר נקי מקשרים קרובים, נראה שהאיום התרחק או לא היה רלוונטי. אך זמן המשימה המוקצב אוזל. נקודת הוכושל קרובה.",
             timer: 40, // Sufficient time left for success if reached correctly
             options: [
                 { text: "המשך בזהירות במהירות שקטה לנקודת הוכושל. כנראה בטוח.", nextStage: "end_success_ontime" }, // Primary success path
                 { text: "שלח דוח מצב וקטורי מיקום מקוצר (חשיפה נמוכה) לבקשת אישור להמשיך.", nextStage: "end_report_position_fail" } // Fail - unnecessary risk
             ]
         },
         stg_break_contact_shallow: {
             scenario: "ניסית לשבור מגע בעומק רדוד יותר - תמרון מסוכן מאוד, אך אולי הפתיע את האויב. קריאות סונאר מבולבלות. האם הצלחת להתחמק סופית?",
             timer: 20,
             options: [
                 { text: "בצע בדיקת סונאר יסודית לעומק בכל המגזרים.", nextStage: "end_check_sonar_outcome" }, // Potential outcome based on time
                 { text: "שנה נתיב אקראי במהירות גבוהה להקשות על מעקב אקוסטי.", nextStage: "end_evade_random_fail" } // High risk fail
             ]
         },
        // Intermediate Outcomes needing a final check or leading to end state
         end_deploy_decoy_outcome: {
            scenario: "שיגרת מצוף הטעיה. האם האויב הוטעה? קשה לדעת בוודאות מיידית, אך פעולתך חשפה את כוונותיך. עליך לנתק מגע במהירות ובנחישות.",
            timer: 20,
            options: [
                { text: "צלול במהירות לעומק מרבי וברח לכיוון אקראי.", nextStage: "end_dive_escape_outcome" }, // Potential outcome based on time
                { text: "הגבר מהירות מקסימלית וברח קדימה, הרחק מההטעיה.", nextStage: "end_speed_escape_fail" } // Fail - predictable escape
            ]
         },
          end_dive_escape_outcome: {
            scenario: "צללת במהירות וברחת אחרי שיגור ההטעיה. ביצעת תמרון נכון תיאורטית. נותר מספיק זמן לביצועו ולהשלמת ההתחמקות? (ההצלחה תלויה בזמן שנותר ובניהול הסיכון שלך עד כה).",
            timer: 15, // Time left after decision + action
            options: [], // End point, check time
             checkTimeForSuccess: true // Trigger time check
         },
          end_evade_now_outcome: {
            scenario: "ביצעת תמרון התחמקות חד ומיידי. זה היה סיכון מחושב כדי להפתיע את האויב. האם הצלחת לשבור מגע סופית? (ההצלחה תלויה בזמן שנותר ליכולת ההתאוששות והניתוק שלך).",
            timer: 20, // Time left after decision + action
            options: [], // End point, check time
             checkTimeForSuccess: true // Trigger time check
         },
         end_check_sonar_outcome: {
            scenario: "ביצעת בדיקת סונאר יסודית אחרי התמרון המסוכן. הסונאר נקי מקשרים קרובים - נראה שהתחמקת בהצלחה! אך הבדיקה גזלה זמן יקר. (ההצלחה תלויה בזמן שנותר להגיע לנקודת המשימה).",
            timer: 15, // Time left after decision + action
             options: [], // End point, check time
             checkTimeForSuccess: true // Trigger time check
         },

        // Final End States - Time Independent Failures
        end_active_ping_fail: {
            scenario: "פינג אקטיבי... זו היתה טעות טקטית קטלנית! מיקומך נחשף באופן חד וברור, והאויב בטווח ירי קצר. שמעת טורפדו נורה לעברך... הצוללת שלך נפגעה קשות. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
        },
        end_risky_advance_fail: {
            scenario: "ההתקדמות במהירות גבוהה אמנם קידמה אותך לכאורה, אך רעש המדחפים העצום שלך הגביר אותך לכל האויבים שבאזור. צוללת אויב איתרה ותקפה ללא אזהרה נוספת. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
        },
        end_malfunction_fail: {
            scenario: "המשכת לצלול עמוק מדי, מתוך הנחה מוטעית שמדובר בתקלה בצוללת. הרעש לא היה תקלה פנימית אלא רעש חיצוני שזיהית מאוחר מדי! גוף הצוללת הגיע לעומק ריסוק. שמעת את הברזל קורס לתוך עצמו... המשימה נכשלה באסון קטסטרופלי.",
            timer: 0, options: [], outcome: "failure_catastrophic"
        },
         end_run_away_fail: {
            scenario: "ניסית לברוח במהירות מקסימלית אחרי שנתפסת, אך בים עמוק, מהירות גבוהה הופכת אותך למטרה קלה. צוללת האויב, כנראה מהירה ומתקדמת יותר, הדביקה אותך במהירות. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
         },
         end_report_under_fire_fail: {
            scenario: "שידור דוח מצב בזמן שאתה במעקב פעיל היה חשיפה מיותרת וקטלנית. האויב איתר את מקור השידור שלך ותקף באופן מיידי ומדויק. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
         },
         end_evade_late_fail: {
            scenario: "המתנת לרגע האחרון לביצוע התמרון... והמתנת יותר מדי. לא הספקת להגיב בזמן לאיום המתקרב. האירועים עקפו אותך, הצוללת נתפסה והמשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_timed_out" /* Classified as timed out because reaction was too late */
         },
         end_report_position_fail: {
            scenario: "הדיווח המקוצר אמנם נשלח בהצלחה, אך גם הוא גילה את מיקומך המדויק לאויב שהאזין לכל התקשורת. החשיפה הקלה הספיקה כדי לאפשר התקפה ממוקדת. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
         },
          end_evade_random_fail: {
            scenario: "תמרון אקראי ומהיר בזמן לחוץ, בעומק מסוכן, הוא מתכון לאסון עצמי. איבדת שליטה רגעית בצוללת, והאויב ניצל זאת מיד לתקוף. המשימה נכשלה באסון קטסטרופלי.",
            timer: 0, options: [], outcome: "failure_catastrophic"
         },
         end_speed_escape_fail: {
            scenario: "ניסית לברוח במהירות קדימה אחרי שיגור ההטעיה, אך כיוון הבריחה היה צפוי והאויב, שזוהה כמתוחכם, לא התקשה להבין את התכסיס ולהדביק אותך. המשימה נכשלה.",
            timer: 0, options: [], outcome: "failure_detected"
         },
        // Final End States - Time Dependent Outcomes
        end_success_ontime: {
            scenario: "סדרת החלטות מבריקה תחת אי-ודאות ולחץ! ניווטת בהצלחה בין איומים פוטנציאליים, קיבלת את ההחלטות הנכונות בזמן, והגעת לאזור המשימה המתוכנן עם מספיק זמן פנוי לביצועה. כל הכבוד, מפקד!",
            timer: 0, options: [], outcome: "success"
        },
         end_time_based_success: {
            scenario: "התמרון או הפעולה שביצעת הצליחו! הצלחת להתחמק או לשבור מגע עם האיום. וחשוב לא פחות - נותר לך מספיק זמן יקר כדי להתאושש ולהמשיך בבטחה לעבר נקודת המשימה. ניהול הזמן וההחלטה הנכונה היו קריטיים. המשימה ממשיכה כמתוכנן. ברכות, מפקד!",
            timer: 0, options: [], outcome: "success"
        },
        end_timer_fail: {
            scenario: "הזמן המוקצב לקבלת ההחלטה אזל לחלוטין! אי-קבלת החלטה בזמן או תגובה מאוחרת מדי פירושה שהאירועים עקפו אותך והאויב, או הסכנה, הגיע ראשון. המשימה נכשלה עקב תגובה איטית מדי.",
            timer: 0, options: [], outcome: "failure_timed_out"
        },
         end_time_based_fail: {
            scenario: "ביצעת את הפעולה הנכונה תיאורטית כדי להתחמק או לשבור מגע, אך... לא נותר מספיק זמן כדי להשלים אותה במלואה או להתאושש מהתמרון ולהגיע לנקודת המשימה. האירועים עקפו אותך עקב ניהול זמן לקוי בשלבים קודמים. המשימה נכשלה עקב מחסור בזמן.",
            timer: 0, options: [], outcome: "failure_timed_out"
        }
    };

    let currentGameStageKey = 'start';
    let timeRemaining = 0;
    let timerInterval = null;
    const timeSuccessThreshold = 10; // Minimum time remaining required for time-based success stages

    const scenarioEl = document.getElementById('scenario');
    const timerContainerEl = document.getElementById('timer-container'); // Get the container
    const timerEl = document.getElementById('timer');
    const optionsEl = document.getElementById('options');
    const resultsEl = document.getElementById('results');
    const startButton = document.getElementById('start-button');
    const explanationEl = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const simulatorEl = document.getElementById('submarine-simulator'); // Get the main container

    function updateDisplay() {
        const currentStage = gameStages[currentGameStageKey];

        // Clear previous state
        scenarioEl.textContent = '';
        optionsEl.innerHTML = '';
        resultsEl.textContent = '';
        resultsEl.className = 'screen-results'; // Reset class

        // Set scenario text with a slight delay/animation feel (CSS transition on content not possible, direct update)
        scenarioEl.textContent = currentStage.scenario;


        if (currentStage.timer > 0) {
             timerEl.textContent = `זמן נותר: ${timeRemaining} שניות`;
             timerContainerEl.style.visibility = 'visible'; // Show timer
        } else {
            timerEl.textContent = ''; // Hide timer text
            timerContainerEl.style.visibility = 'hidden'; // Hide timer container completely
        }

        // Handle options or end state
        if (currentStage.options.length > 0) {
            currentStage.options.forEach(option => {
                const button = document.createElement('button');
                button.classList.add('option-button');
                button.textContent = option.text;
                button.onclick = () => handleDecision(option.nextStage);
                optionsEl.appendChild(button);
            });
             startButton.style.display = 'none'; // Hide start button when options are shown

        } else {
             // Game is over or waiting to start
            startButton.style.display = 'block';
            clearInterval(timerInterval); // Stop timer if game ended

            // Display final outcome if any
            if (currentStage.outcome) {
                // Use scenario text for final outcome display in results area
                 resultsEl.textContent = currentStage.scenario;
                 let outcomeClass = '';
                switch(currentStage.outcome) {
                    case 'success': outcomeClass = 'success'; break;
                    case 'failure_detected': outcomeClass = 'failure_detected'; break;
                    case 'failure_catastrophic': outcomeClass = 'failure_catastrophic'; break;
                    case 'failure_timed_out': outcomeClass = 'failure_timed_out'; break;
                    case 'mixed': outcomeClass = 'mixed'; break;
                }
                 resultsEl.className = 'screen-results outcome ' + outcomeClass; // Set class for styling
                 scenarioEl.textContent = ''; // Clear scenario text on final outcome
                 timerEl.textContent = ''; // Ensure timer is empty on final screen
                 timerContainerEl.style.visibility = 'hidden';
            } else if (currentStage.checkTimeForSuccess) {
                // Handle time-based success/failure logic
                if (timeRemaining >= timeSuccessThreshold) {
                    handleDecision('end_time_based_success');
                } else {
                    handleDecision('end_time_based_fail');
                }
            } else {
                 // Initial state before game starts
                 resultsEl.textContent = "לחץ 'התחל משימה' כדי להתחיל את הסימולציה.";
                 scenarioEl.textContent = '';
                 timerEl.textContent = '';
                 timerContainerEl.style.visibility = 'hidden';
            }
        }
    }

    function startTimer() {
        clearInterval(timerInterval); // Clear any existing timer
        const currentStage = gameStages[currentGameStageKey];
        timerContainerEl.classList.remove('pulse-danger'); // Reset pulse class

        if (currentStage.timer > 0) {
            timeRemaining = currentStage.timer;
            timerEl.textContent = `זמן נותר: ${timeRemaining} שניות`; // Initial display
            timerContainerEl.style.visibility = 'visible'; // Make sure timer is visible

            timerInterval = setInterval(() => {
                timeRemaining--;
                timerEl.textContent = `זמן נותר: ${timeRemaining} שניות`;

                // Change color and potentially pulse as time runs out
                if (timeRemaining <= 10) {
                     timerContainerEl.style.color = '#ff4500'; // OrangeRed
                } else if (timeRemaining <= 20) {
                     timerContainerEl.style.color = '#ffff00'; // Yellow
                } else {
                     timerContainerEl.style.color = '#00ff00'; // Green
                }

                 if (timeRemaining <= 5) { // Start pulsing below 5 seconds
                     timerContainerEl.classList.add('pulse-danger');
                 } else {
                      timerContainerEl.classList.remove('pulse-danger');
                 }


                if (timeRemaining <= 0) {
                    clearInterval(timerInterval);
                     timerContainerEl.classList.remove('pulse-danger'); // Stop pulsing
                    handleDecision('end_timer_fail'); // Handle timer running out
                }
            }, 1000);
        } else {
             timerContainerEl.style.visibility = 'hidden'; // Hide timer if stage has 0 timer
             timerContainerEl.classList.remove('pulse-danger');
        }
    }

    function handleDecision(nextStageKey) {
        clearInterval(timerInterval); // Stop timer immediately after decision
        timerContainerEl.classList.remove('pulse-danger'); // Stop pulsing on decision

         // Disable options after selection
        optionsEl.querySelectorAll('.option-button').forEach(button => {
            button.disabled = true;
        });

        // Process consequence or move to next stage
        currentGameStageKey = nextStageKey;
        // Add a slight delay before showing the next stage to simulate processing/transition
        setTimeout(() => {
            updateDisplay();
            startTimer(); // Start timer for the next stage if it has one
        }, 500); // 500ms delay
    }

    function startGame() {
        currentGameStageKey = 'start';
        updateDisplay();
        startTimer();
    }

    startButton.onclick = startGame;

    toggleExplanationButton.onclick = () => {
        explanationEl.classList.toggle('hidden');
        // Optional: Change button text based on state
        if (explanationEl.classList.contains('hidden')) {
             toggleExplanationButton.textContent = 'הצג הסבר תיאורטי ומעמיק';
        } else {
             toggleExplanationButton.textContent = 'הסתר הסבר תיאורטי ומעמיק';
        }
    };

    // Initial display state
    startButton.style.display = 'block';
    updateDisplay(); // Set initial text

</script>
```