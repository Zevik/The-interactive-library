---
title: "בניית מצודה צלבנית: סודות הבנאים העתיקים"
english_slug: building-a-crusader-castle-secrets-of-ancient-builders
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [מסעי הצלב, מצודות, אדריכלות ימי הביניים, ביצורים, ארכיאולוגיה]
---
<p>הצטרפו למסע בזמן ותגלו את הפלא ההנדסי של ימי הביניים! איך נבנו המצודות הצלבניות האדירות, אותם ענקי אבן בלתי ניתנים לחדירה (כמעט)? בואו נבנה מצודה בעצמנו, שלב אחר שלב, ונגלה את הסודות והטריקים שהפכו אותן למבצרי מגן אימתניים.</p>

<div id="castle-app">
    <div id="castle-container">
        <!-- Base layer: Ground/Site -->
        <div class="castle-layer" id="stage-0-ground"></div>

        <!-- Building stages - initially hidden -->
        <!-- Add meaningful animations and visuals -->
        <div class="castle-layer buildable" id="stage-1-foundations" data-info="היסודות: עמוד השדרה הנסתר! נחפרו עמוק בסלע האם כדי לעגן את המבנה האדיר ולמנוע חפירת מנהרות מתחתיו. ללא יסודות חזקים, המצודה כולה בסכנה."></div>
        <div class="castle-layer buildable" id="stage-2-lower-walls" data-info="החומות התחתונות: המחסום הראשון! נבנו מאבנים ענקיות, לעיתים כפולות, בעובי שיכול להגיע למטרים רבים. עוצרות התקפות ישירות ומגינות על הנמצאים בפנים."></div>
        <div class="castle-layer buildable" id="stage-3-towers" data-info="המגדלים: העיניים והאגרופים של המצודה! מאפשרים תצפית מרחוק וירי הגנתי לכל הכיוונים. צורתם העגולה עמידה יותר בפני בליסטראות; צורתם המרובעת סיפקה שטח פנימי גדול יותר."></div>
        <div class="castle-layer buildable" id="stage-4-upper-walls" data-info="חומות עליונות ושינות (קרנולציות): עמדות ירי טקטיות! חלק זה של החומה הגבוהה סיפק מחסה ליורים מאחורי השינות, ומעבר נוח לתנועת מגנים. ה'שיניים' הללו הן סמל מיידי למצודה."></div>
        <div class="castle-layer buildable" id="stage-5-gatehouse" data-info="שער הכניסה: נקודת התורפה המוגנת ביותר! מכלול מתוחכם של מגדלי שמירה, גשר מתרומם, שערים כפולים, סורגים כבדים ואף 'משפכי מוות' אפשרו לנטרל תוקפים שניסו לפרוץ פנימה."></div>
        <div class="castle-layer buildable" id="stage-6-inner-buildings" data-info="מבני הפנים: הלב הפועם של המצודה! מגורים, מחסנים, מטבחים, אורוות, באר מים, ואף כנסייה או קפלה - כל מה שנדרש כדי שמאות ואף אלפי אנשים יוכלו לשרוד מצור ממושך בביטחון יחסי."></div>
        <div class="castle-layer buildable" id="stage-7-details" data-info="פרטים הגנתיים קטלניים: שפרו את היכולת להתגונן מקרוב. חרכי ירי צרים אפשרו ירי חיצים החוצה במינימום חשיפה. מרפסות ירי (משקפים) איפשרו להטיל אבנים או לשפוך חומרים רותחים על תוקפים למרגלות החומה. צריחים קטנים הגנו על נקודות תורפה."></div>

        <!-- Info Popup -->
        <div id="info-popup"></div> <!-- Initially hidden via CSS -->

    </div>
    <button id="next-stage-button">נתחיל בבנייה (שלב 1)</button>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;700&display=swap');

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f4f1eb; /* Light earthy background */
    }

    h1 {
        color: #5a4a3a; /* Dark earthy color */
        text-align: center;
        margin-top: 20px;
        font-size: 2em;
    }

    p {
        text-align: center;
        max-width: 800px;
        margin: 15px auto;
    }

    #castle-app {
        direction: rtl;
        text-align: center;
        margin: 20px auto;
        padding: 20px;
        background-color: #ffffff; /* Clean white background for the app area */
        border-radius: 12px; /* More rounded corners */
        max-width: 800px;
        position: relative;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        overflow: hidden; /* To contain transformations */
    }

    #castle-container {
        position: relative;
        width: 100%;
        padding-top: 70%; /* Maintain aspect ratio, slightly taller */
        overflow: hidden;
        background: linear-gradient(to bottom, #87CEEB 0%, #E0F6FF 60%, #D2B48C 60%, #D2B48C 100%); /* Simple sky and ground gradient */
        border-bottom: none; /* Remove stark line */
        margin-bottom: 20px;
        border-radius: 8px; /* Match app container */
    }

    .castle-layer {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: 100% auto; /* Cover width, auto height */
        background-position: center bottom;
        opacity: 0; /* Initially hidden */
        transition: opacity 1s ease-out, transform 1s ease-out; /* Added transform transition */
        transform: translateY(20px) scale(0.98); /* Start slightly down and smaller */
        transform-origin: bottom center; /* Transform from the bottom */
        /* Use basic colors with hints of texture via CSS */
        box-sizing: border-box; /* Include padding/border in element's total width and height */
    }

    /* Base Ground layer - always visible */
    #stage-0-ground {
        opacity: 1;
        height: 40%; /* Ground occupies lower part */
        background: #c1a58c; /* Earth tone */
        /* Subtle texture hint */
        background-image: linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%, rgba(0,0,0,0.05)), linear-gradient(-45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%, rgba(0,0,0,0.05));
        background-size: 20px 20px;
        transform: none; /* Ground doesn't animate in */
    }

    /* Specific layer styling for visual progression */
    #stage-1-foundations {
        height: 15%;
        background-color: #7d6b5e; /* Darker stone */
        bottom: 0%;
        z-index: 1;
    }

    #stage-2-lower-walls {
        height: 35%; /* Taller */
        background-color: #9b8a7c; /* Medium stone */
        bottom: 15%;
        z-index: 2;
        /* Add a subtle top border to suggest stones */
        border-top: 3px solid rgba(0,0,0,0.1);
    }

    #stage-3-towers {
        height: 60%; /* Tallest layer conceptually */
        background-color: #8a7a6c; /* Slightly different stone */
        bottom: 15%; /* Base on foundations */
        z-index: 3;
         /* Suggest tower shapes - this is an abstraction */
        /* In a real app, this would be separate tower elements */
    }

    #stage-4-upper-walls {
        height: 10%;
        background-color: #a9988b; /* Lighter stone */
        bottom: 50%; /* Stack on lower walls (15+35=50) */
        z-index: 4;
         border-top: 2px solid rgba(0,0,0,0.1);
         /* Add crenellation visual hint - very simplified */
        background-image: linear-gradient(to right, transparent 10%, rgba(0,0,0,0.1) 10%, rgba(0,0,0,0.1) 15%, transparent 15%, transparent 25%, rgba(0,0,0,0.1) 25%, rgba(0,0,0,0.1) 30%, transparent 30%, transparent 40%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.1) 45%, transparent 45%, transparent 55%, rgba(0,0,0,0.1) 55%, rgba(0,0,0,0.1) 60%, transparent 60%, transparent 70%, rgba(0,0,0,0.1) 70%, rgba(0,0,0,0.1) 75%, transparent 75%, transparent 85%, rgba(0,0,0,0.1) 85%, rgba(0,0,0,0.1) 90%, transparent 90%);
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }

    #stage-5-gatehouse {
        height: 45%; /* Taller than lower walls */
        width: 30%; /* Wider */
        left: 35%; /* Centered */
        background-color: #b8a79a; /* Gatehouse stone */
        bottom: 15%; /* Base on foundations */
        z-index: 5; /* Above walls */
        border: 2px solid rgba(0,0,0,0.1);
        border-bottom: none;
        /* Suggest gate opening - abstraction */
        background-image: linear-gradient(to bottom, transparent 60%, rgba(0,0,0,0.2) 60%, rgba(0,0,0,0.2) 100%), radial-gradient(circle at 50% 100%, transparent 60%, rgba(0,0,0,0.2) 60%);
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }

    #stage-6-inner-buildings {
        height: 30%;
        width: 70%; /* Wider area */
        left: 15%; /* Positioned inside */
        background-color: #d4c3b6; /* Lighter inner color */
        bottom: 16%; /* Slightly above foundations */
        z-index: 0; /* Below outer walls and gatehouse */
         border: 2px solid rgba(0,0,0,0.08);
         border-bottom: none;
    }

    #stage-7-details {
        /* This layer acts as an invisible overlay to capture clicks on the whole visible castle structure */
        height: calc(100% - 15%); /* Covers area above foundations */
        bottom: 15%;
        width: 100%;
        left: 0;
        z-index: 6; /* Above most things but below popup */
        opacity: 0; /* Still invisible, only there for click detection */
        background: none; /* No visual */
         pointer-events: none; /* Initially no clicks */
    }


    .buildable {
         cursor: pointer;
    }

    .buildable:hover {
        filter: brightness(1.1); /* Subtle highlight on hover */
        transition: filter 0.2s ease;
    }

    .built {
         pointer-events: auto !important; /* Enable clicks after built */
    }


    #next-stage-button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        margin-top: 15px;
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #next-stage-button:hover:not(:disabled) {
        background-color: #45a049;
        transform: translateY(-2px); /* Lift effect on hover */
    }

     #next-stage-button:active:not(:disabled) {
        transform: translateY(0); /* Press effect */
    }

    #next-stage-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    #info-popup {
        position: fixed; /* Fixed to viewport */
        background-color: rgba(44, 62, 80, 0.9); /* Darker, semi-transparent */
        color: white;
        padding: 15px;
        border-radius: 8px;
        z-index: 10;
        pointer-events: none; /* Allows clicking through to layers below */
        white-space: normal; /* Allow text wrapping */
        font-size: 0.95em;
        line-height: 1.5;
        max-width: 250px; /* Limit width */
        text-align: right;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        opacity: 0; /* Initially hidden */
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
        transform: translate(-50%, -100%); /* Position relative to calculated point */
    }

    #info-popup.visible {
        opacity: 1;
        visibility: visible;
    }

    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #008CBA; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #toggle-explanation:hover {
        background-color: #007b9e;
        transform: translateY(-2px);
    }

     #toggle-explanation:active {
        transform: translateY(0);
    }


    #full-explanation {
        margin-top: 20px;
        padding: 20px; /* More padding */
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 12px; /* Match app container */
        text-align: right;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        display: none; /* Hidden by default */
    }

    #full-explanation h2 {
        color: #5a4a3a;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
        font-size: 1.4em;
    }

    #full-explanation h2:first-child {
         margin-top: 0;
    }

    #full-explanation p {
        margin-bottom: 15px; /* More space between paragraphs */
        line-height: 1.7;
        text-align: right; /* Ensure text aligns right */
    }

     #full-explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
     }

     #full-explanation li {
        margin-bottom: 8px;
        line-height: 1.6;
     }

    /* Style for popup when it's positioned */
    #info-popup.visible {
        transform: translate(-50%, -100%); /* Reset transform after calculation if needed, or keep it */
    }


</style>

<button id="toggle-explanation">רוצים לדעת עוד? הצגת/הסתרת הסבר מלא</button>

<div id="full-explanation">
    <h2>מבוא: לב ליבה של השליטה הצלבנית</h2>
    <p>מצודות לא היו רק מבנים גדולים; הן היו אגרופי ברזל שהחזיקו את השליטה הצלבנית במזרח התיכון. לאחר הצלחת מסע הצלב הראשון בסוף המאה ה-11, נדרשו הצלבנים לבסס את שלטונם באזור עוין. המצודות שצצו בנוף שימשו כבסיסי צבא, מרכזי מינהל ואספקה, מקלטים לאוכלוסייה בעת סכנה, ונקודות אסטרטגיות לשליטה על דרכים ומעברים חיוניים. הן אפשרו לגרעין קטן יחסית של לוחמים לשלוט בשטחים נרחבים.</p>

    <h2>האתר קובע הכל: בחירת המיקום המושלם</h2>
    <p>הסוד הראשון למצודה בלתי חדירה טמון בבחירת המקום. אדריכלים צלבנים חיפשו יתרונות טבעיים מקסימליים: פסגות הרים נישאות, צוקים תלולים שהגנו על אחד האגפים, עיקולי נהרות שיצרו 'חפיר' טבעי, או נקודות ששלטו על עמקי מפתח ודרכים ראשיות. קרבה למקור מים יציב (באר, מעיין) הייתה הכרחית להישרדות במצור. האתר המושלם הפך את עבודת התוקפים לקשה פי כמה.</p>

    <h2>תכנון גאוני: עקרונות הגנה לעומק</h2>
    <p>התכנון האדריכלי שיקף הבנה מעמיקה של טקטיקות מצור והגנה. המטרה הייתה ליצור סדרה של מכשולים שייבשו את כוחו של התוקף. חומות חיצוניות עבות נתמכו בחומות פנימיות גבוהות יותר ('קונצנטריות'), כך שגם אם נפרצה החומה הראשונה, התוקפים נחשפו לירי מהחומה הפנימית הגבוהה. שערים הפכו למלכודות מתוחכמות, ומגדלים רבים אפשרו לירות חיצים (ואחר כך גם קליעים) מהאגף על מי שניסה לפרוץ את החומה או השער. כל פינה תוכננה כדי ליצור 'שטח הריגה'.</p>

    <h2>אבן, מלט ועץ: חומרי הבנייה של ענקי האבן</h2>
    <p>רוב המצודות נבנו מאבן מקומית, שנחצבה בסמוך כדי לחסוך בשינוע היקר והמסוכן. חוצבים מיומנים שלפו גושי ענק מהאדמה או הצוק, וסתתים עיצבו אותם לגודל ולצורה המתאימים. לחיבור האבנים השתמשו במלט איכותי וחזק, לעיתים על בסיס סיד, שהקשה את המבנה כולו והפך אותו לעמיד בפני כלי מצור. עץ היה חיוני לבניית פיגומים, גגות, רצפות, שערים וגשרים מתרוממים, ולעיתים היה צורך לייבא אותו ממרחקים.</p>

    <h2>בנייה אפית: התהליך המורכב</h2>
    <ul>
        <li>**חציבה ושינוע:** זה התחיל בחציבה מסיבית. אבנים ענקיות שונעו לאתר הבנייה בשיטות פרימיטיביות אך יעילות - מריצות, עגלות, מנופים פשוטים המבוססים על כוח אדם ובהמות, ושימוש בגלילים ומשטחי עפר לבניית רמפות.</li>
        <li>**יסודות על הסלע האם:** לפני שהונחה אבן אחת מעל פני הקרקע, נחפרו תעלות יסוד עמוקות מאוד, לרוב עד שהגיעו לסלע האם היציב. יסודות אלו מולאו באבנים גדולות ומלט ויצרו את הבסיס האיתן שיכול היה לשאת את משקל עשרות אלפי טונות של אבן מעליהם.</li>
        <li>**קירות שצמחו השמיימה:** הבנייה עצמה התקדמה בשלבים, עם פיגומים מעץ שתמכו בבנאים ובסתתים. קירות חיצוניים נבנו לרוב כמעטפת כפולה עם חלל פנימי שמולא באבנים קטנות יותר ומלט ('אופוס רטילאטום' או דומיו), טכניקה שחסכה זמן וחומרים ועדיין סיפקה חוזק עצום.</li>
        <li>**שערים, גשרים ומלכודות:** בניית השער הייתה שיא מורכבות ההנדסה הצלבנית. שילוב של מגדלי שמירה, גשרים מתרוממים (שיכולים גם ליצור מחסום אנכי כשהורמו), דלתות עץ ענקיות מחוזקות בברזל, וסורגי מתכת כבדים (Portcullis) שיכלו ליפול ברגע ולאטום את הכניסה - הפכו את הפריצה לשער למשימת התאבדות.</li>
        <li>**חיים בתוך האבן:** לאחר הקמת קווי ההגנה, נבנו בתוך חצר המצודה מבנים שאיפשרו חיים וניהול יומיומי: מגורי המפקדים, החיילים ואנשי המנהלה, מחסני מזון וציוד (חשובים במיוחד למצור), מטבחים, אורוות, ובאר מרכזית שהייתה לעיתים קרובה סיבת חיים או מוות במצור ממושך.</li>
    </ul>

    <h2>צבא של בנאים: כוח אדם ומיומנויות</h2>
    <p>בניית מצודה דרשה גיוס וארגון של אלפי עובדים. בבסיס הפירמידה היו אלפי פועלים לא מיומנים, לרוב איכרים או שבויי מלחמה, שביצעו את העבודות הפיזיות הקשות - חפירה, שינוע אבנים, ועירבוב מלט. מעליהם פעלו בעלי מלאכה מיומנים: חוצבים, סתתים מומחים שעיצבו אבני פינה ואלמנטים מורכבים, בנאים שהניחו את האבנים בקירות, נפחים שיצרו כלי עבודה, מסמרים וסורגים, ונגרים שבנו פיגומים, תקרות ושערים. כל הפרויקט נוהל על ידי מנהלי עבודה ובראשם אדריכל או מהנדס צבאי, לרוב איש צבא או נזיר מלומד.</p>

    <h2>טקטיקות הגנה פעילה: לא רק חומות עבות</h2>
    <p>המצודות לא היו רק מבנים פסיביים. הן היו פלטפורמות להגנה אקטיבית ויצירת אזורי ירי קטלניים. חרכי ירי (Arrow Slits) היו חריצים צרים בקירות המצודה, לעיתים בצורת צלב או מפתח, שאיפשרו ליורים מבפנים לירות חיצים לעבר תוקפים בחוץ, תוך חשיפה מינימלית של גופם. מרפסות ירי (Machicolations) היו בליטות בחומות או מעל שערים עם פתחים ברצפתן, שאיפשרו להפיל אבנים, לשפוך שמן רותח או מים רותחים, ולירות ישר למטה על תוקפים שניסו לחתור תחת החומה או לשבור את השער. צריחים קטנים (Turrets) בפינות או בקצות חומות הרחיבו את שדה הראייה ואפשרו ירי מנקודות נוספות.</p>

    <h2>מורשת אבן: מצודות צלבניות מפורסמות</h2>
    <p>ברחבי המזרח התיכון ובאירופה ניצבות עד היום מצודות צלבניות מרשימות המעידות על עוצמתן וכושר ההנדסה של בוניהן. בישראל בולטות מצודות כמו כוכב הירדן (בלבואר), מבצר מונפור בגליל, שרידי מבצר עתלית על החוף, ומבצר נמרוד ברמת הגולן (אם כי בחלקו מאוחר יותר). בעולם, קראק דה שבלייה ומרגט בסוריה נחשבות מהמפוארות והשמורות ביותר, לצד מבצר בודרום בטורקיה ורבות אחרות באירופה שהושפעו מהטכניקות הצלבניות.</p>

    <h2>עלות בלתי נתפסת וזמן בניה אין סופי</h2>
    <p>בניית מצודה הייתה מיזם עצום, יקר בטירוף, ודרש שנים רבות ואף עשרות שנים להשלמתו. עלויות העבודה, החומרים, והשינוע היו אדירות, והן מומנו לרוב על ידי המלכים, האצילים העשירים, או המסדרים הצבאיים האביריים כמו הטמפלרים וההוספיטלרים, שהיו בעלי משאבים כלכליים אדירים. משך הבנייה היה תלוי בגודל המצודה, קשיי האתר, זמינות חומרי הגלם וכוח האדם, וכמובן - היציבות הפוליטית באזור שאיפשרה פרויקט כה ארוך טווח.</p>
</div>

<script>
    const castleContainer = document.getElementById('castle-container');
    const stages = document.querySelectorAll('.castle-layer');
    const nextStageButton = document.getElementById('next-stage-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const fullExplanationDiv = document.getElementById('full-explanation');
    const infoPopup = document.getElementById('info-popup');
    const buildableElements = document.querySelectorAll('.buildable');

    let currentStage = 0;
    const totalStages = stages.length -1; // Subtract 1 for the ground layer

    // Ensure ground layer is visible initially
    document.getElementById('stage-0-ground').style.opacity = 1;

    // Set initial button text correctly
    nextStageButton.textContent = `נתחיל בבנייה (שלב ${currentStage + 1})`;


    nextStageButton.addEventListener('click', function() {
        if (currentStage < totalStages) {
            currentStage++;
            const stageElement = document.getElementById(`stage-${currentStage}-${getStageName(currentStage)}`);
            if (stageElement) {
                // Add 'visible' class to trigger CSS transition
                stageElement.style.opacity = 1;
                stageElement.style.transform = 'translateY(0) scale(1)';

                // Add 'built' class to enable pointer events and hover effect
                stageElement.classList.add('built');
            }

            if (currentStage === totalStages) {
                nextStageButton.textContent = 'המצודה הושלמה!';
                nextStageButton.disabled = true;
            } else {
                 nextStageButton.textContent = `השלב הבא (${currentStage + 1}/${totalStages})`;
            }

             // Hide popup when building next stage
             hideInfoPopup();
        }
    });

    // Function to get stage name for ID (simplified lookup)
    function getStageName(stageNum) {
        switch (stageNum) {
            case 1: return 'foundations';
            case 2: return 'lower-walls';
            case 3: return 'towers';
            case 4: return 'upper-walls';
            case 5: return 'gatehouse';
            case 6: return 'inner-buildings';
            case 7: return 'details';
            default: return '';
        }
    }

    // Add click listeners to buildable elements
    buildableElements.forEach(element => {
        element.addEventListener('click', function(event) {
            // Check if the element is currently visible (opacity > 0) to prevent clicking hidden layers
            const style = window.getComputedStyle(element);
            if (parseFloat(style.opacity) > 0) {
                 const infoText = element.getAttribute('data-info');
                 if (infoText) {
                    showInfoPopup(infoText, event.clientX, event.clientY);
                 }
            }
        });
        // Initially disable clicks via CSS class, will be enabled on 'built' class
    });

    // Handle clicks anywhere on the body to hide popup, except clicks on the popup itself or buildable elements
    document.body.addEventListener('click', function(event) {
        let target = event.target;
        let isClickInsidePopup = false;
        while (target) {
            if (target.id === 'info-popup') {
                isClickInsidePopup = true;
                break;
            }
            target = target.parentElement;
        }

        // Hide popup if click is not on a buildable element AND not inside the popup
        // Also check if the clicked element is one of the "built" layers that triggered the popup initially
        const isClickOnBuiltLayer = event.target.classList.contains('built');


        if (!isClickInsidePopup && !isClickOnBuiltLayer) {
             hideInfoPopup();
        }
    });


    // Function to display and position the info popup near the click location
    function showInfoPopup(text, x, y) {
        infoPopup.textContent = text;
        // Position the popup initially near the click but use transforms for final placement
        // This helps with calculating dimensions before final position
        infoPopup.style.left = `${x}px`;
        infoPopup.style.top = `${y}px`;
        infoPopup.classList.add('visible'); // Trigger CSS transition

        // Use setTimeout to allow visibility/opacity to apply before calculating size
        setTimeout(() => {
            const popupRect = infoPopup.getBoundingClientRect();
            const margin = 15; // Margin from viewport edges

            let finalX = x;
            let finalY = y;

            // Default positioning is centered above the click (handled by transform)
            // Now adjust if it goes off-screen

            // Check horizontal bounds
            if (finalX - popupRect.width / 2 < margin) {
                 finalX = margin + popupRect.width / 2;
            } else if (finalX + popupRect.width / 2 > window.innerWidth - margin) {
                 finalX = window.innerWidth - margin - popupRect.width / 2;
            }

            // Check vertical bounds
            // Default is above click (y - height - space)
            const spaceAbove = y - popupRect.height - 10;
            const spaceBelow = y + 10;

            if (spaceAbove < margin) {
                // No space above, position below
                finalY = spaceBelow;
                // Adjust transform origin if positioning below
                infoPopup.style.transform = 'translate(-50%, 0)'; // Position centered below
            } else {
                // Enough space above, position above
                finalY = spaceAbove;
                infoPopup.style.transform = 'translate(-50%, -100%)'; // Position centered above (default)
            }

             if (finalY + popupRect.height > window.innerHeight - margin) {
                // If still too low even positioned below, clamp to bottom
                finalY = window.innerHeight - popupRect.height - margin;
                 infoPopup.style.transform = 'translate(-50%, 0)'; // Ensure transform is for 'below' base point
            }

            infoPopup.style.left = `${finalX}px`;
            infoPopup.style.top = `${finalY}px`;


        }, 0); // Use minimal timeout to allow DOM update
    }

    function hideInfoPopup() {
        infoPopup.classList.remove('visible'); // Hide using CSS transition
    }

    // Toggle explanation section visibility
    toggleExplanationButton.addEventListener('click', function() {
        const isHidden = fullExplanationDiv.style.display === 'none';
        if (isHidden) {
             fullExplanationDiv.style.display = 'block';
             toggleExplanationButton.textContent = 'הסתר הסבר מלא';
        } else {
             fullExplanationDiv.style.display = 'none';
             toggleExplanationButton.textContent = 'רוצים לדעת עוד? הצגת/הסתרת הסבר מלא';
        }
    });

    // Hide popup on window resize to prevent mispositioning
    window.addEventListener('resize', hideInfoPopup);

    // Optional: Add a subtle initial animation on the ground/sky or app container
    // castleContainer.style.transform = 'scale(0.95)';
    // setTimeout(() => {
    //     castleContainer.style.transition = 'transform 1s ease-out';
    //     castleContainer.style.transform = 'scale(1)';
    // }, 100);


</script>