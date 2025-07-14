---
title: "מסע הריפוי המדהים: כך העור שלכם מתקן את עצמו"
english_slug: the-miraculous-healing-journey-how-your-skin-repairs-itself
category: "מדעי החיים / פיזיולוגיה"
tags: [ריפוי פצעים, עור, קרישת דם, התחדשות רקמות, דלקת, פיזיולוגיה, אינטראקטיבי]
---
# מסע הריפוי המדהים: כך העור שלכם מתקן את עצמו

רגע אחד של חוסר תשומת לב, ושריטה קטנה כבר כאן. אבל אל דאגה! עמוק מתחת לפני השטח, מתחיל מיד מסע מדהים, אוטומטי ומורכב שמטרתו לסגור את הפצע, למנוע זיהום ולבנות מחדש את הרקמה הפגועה כאילו לא קרה דבר. איך בדיוק הקסם הביולוגי הזה קורה, ומהם השלבים המדויקים שמבטיחים שהעור יחזור לעצמו? הצטרפו לסימולציה וגלו!

<div id="healing-simulation-container">
    <div id="simulation-area">
        <div class="skin-layer epidermis">אפידרמיס</div>
        <div class="skin-layer dermis">דרמיס</div>
        <div class="wound-cut"></div>

        <!-- Simulation elements -->
        <div id="blood" class="sim-element"></div>
        <div id="platelets" class="sim-element"></div>
        <div id="clot" class="sim-element"></div>
        <div id="neutrophils" class="sim-element"></div>
        <div id="macrophages" class="sim-element"></div>
        <div id="fibroblasts" class="sim-element"></div>
        <div id="blood-vessels" class="sim-element"></div>
        <div id="epithelial-cells" class="sim-element"></div>
        <div id="scar-tissue" class="sim-element"></div>

        <!-- Pop-up explanations -->
        <div class="popup" id="popup-platelets">טסיות דם: חיילי העזרה הראשונה! מגיעות ראשונות לעצור דימום ולגשר על הפער.</div>
        <div class="popup" id="popup-clot">קריש דם (פקק פיברין): רשת סיבים חזקה שעוצרת סופית את הדימום ואוטמת את הפצע.</div>
        <div class="popup" id="popup-neutrophils">נויטרופילים: השוטרים הראשונים של מערכת החיסון. מגיעים לבלוע ולנקות חיידקים ופסולת קטנה.</div>
        <div class="popup" id="popup-macrophages">מקרופאגים: "האוכפים" הגדולים. מנקים פסולת גדולה יותר, "אוכלים" נויטרופילים מותשים, ומפעילים את שלב התיקון.</div>
        <div class="popup" id="popup-fibroblasts">פיברובלסטים: בנאי הגוף! מייצרים את סיבי הקולגן שמרכיבים את הרקמה החדשה וממלאים את הפצע.</div>
        <div class="popup" id="popup-blood-vessels">כלי דם חדשים (אנגיוגנזה): נובטים כדי לספק חמצן וחומרי בניין לאזור הריפוי הפעיל.</div>
        <div class="popup" id="popup-epithelial-cells">תאי אפידרמיס: נודדים מהשוליים ומכסים את הפצע מלמעלה כמו שמיכה דקה, כדי לסגור את העור החיצוני.</div>

    </div>
    <div id="simulation-text">
        <p id="current-step-description">לחצו על 'השלב הבא' כדי להתחיל את מסע הריפוי!</p>
    </div>
    <button id="next-step-button">השלב הבא</button>
</div>

<style>
#healing-simulation-container {
    font-family: 'Heebo', sans-serif; /* Added Hebrew-friendly font */
    direction: rtl;
    text-align: right;
    margin-top: 20px;
    border: 1px solid #e0e0e0; /* Lighter border */
    padding: 20px; /* Increased padding */
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* White background */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Subtle shadow */
    max-width: 700px; /* Max width for better readability */
    margin-left: auto;
    margin-right: auto;
}

#simulation-area {
    position: relative;
    width: 100%;
    height: 280px; /* Slightly increased height */
    border: 1px solid #d3d3d3; /* Softer border */
    margin-bottom: 20px; /* Increased margin */
    background: linear-gradient(to bottom, #fafafa 0%, #f0f0f0 100%); /* Subtle gradient background */
    overflow: hidden;
    border-radius: 8px; /* Rounded corners */
}

.skin-layer {
    position: absolute;
    left: 0;
    width: 100%;
    height: 50%;
    text-align: center;
    line-height: 140px; /* Vertically center text */
    font-weight: bold;
    color: #444;
    box-sizing: border-box;
    user-select: none; /* Prevent text selection */
    font-size: 1.1em;
}

.epidermis {
    top: 0;
    background-color: #f5e1d3; /* Warmer skin tone */
    border-bottom: 2px solid #d4c0b2; /* More defined border */
}

.dermis {
    top: 50%;
    background-color: #ebcea7; /* Deeper skin tone */
    border-top: none;
}

.wound-cut {
    position: absolute;
    top: 0;
    left: 50%;
    width: 15px; /* Slightly wider cut */
    height: 100%;
    background: linear-gradient(to bottom, #c0392b 0%, #e74c3c 30%, #c0392b 70%, #a93226 100%); /* Richer red gradient */
    z-index: 10;
    filter: drop-shadow(0 0 5px rgba(192, 57, 43, 0.5)); /* Subtle glow/shadow */
}

/* Simulation Elements - Initially hidden and styled for animation */
.sim-element {
    position: absolute;
    opacity: 0; /* Start invisible */
    transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Smooth transitions */
    z-index: 20;
    cursor: pointer; /* Default cursor */
}

.sim-element.active {
    opacity: 1; /* Fade in */
    transform: none; /* Reset transform if any initial scale/translate */
}

/* Specific Element Styles & Initial/Active States */

#blood {
    top: 0;
    left: calc(50% - 7.5px); /* Align with wider cut */
    width: 15px;
    height: 100%;
    background-color: rgba(231, 76, 60, 0.6); /* Brighter red */
    z-index: 15;
    transition: opacity 1s ease-in, height 1s ease-in; /* Blood might recede */
}
#blood.active {
    opacity: 1;
    height: 100%; /* Stays full height initially */
}


#platelets {
    width: 60px; /* Larger area for swarm */
    height: 60px;
    top: 50px;
    left: calc(50% - 30px);
    background: radial-gradient(circle, #3498db 10%, transparent 15%),
                radial-gradient(circle, #3498db 10%, transparent 15%) 25px 25px,
                radial-gradient(circle, #3498db 10%, transparent 15%) 5px 40px,
                radial-gradient(circle, #3498db 10%, transparent 15%) 40px 5px;
    background-size: 30px 30px; /* Tighter pattern */
    transform: scale(0.8); /* Appear slightly smaller initially */
}

#clot {
    top: 0;
    left: calc(50% - 20px); /* Wider than the cut */
    width: 40px;
    height: 100%;
    background-color: rgba(120, 60, 60, 0.8); /* Deeper reddish-brown */
    z-index: 18; /* Covers blood/platelets */
    transform: scaleY(0.5); /* Appear to "fill" or grow vertically */
}
#clot.active {
    opacity: 1;
    transform: scaleY(1);
}

#neutrophils, #macrophages {
    width: 100px; /* Wider area for swarm */
    height: 100px;
    top: 40px;
    left: calc(50% - 50px);
    transform: scale(0.7); /* Appear smaller initially */
}

#neutrophils {
     background: radial-gradient(circle, #f1c40f 10%, transparent 15%),
                radial-gradient(circle, #f1c40f 10%, transparent 15%) 20px 20px,
                radial-gradient(circle, #f1c40f 10%, transparent 15%) 0px 30px,
                radial-gradient(circle, #f1c40f 10%, transparent 15%) 30px 10px,
                 radial-gradient(circle, #f1c40f 10%, transparent 15%) 10px 0px,
                radial-gradient(circle, #f1c40f 10%, transparent 15%) 40px 30px;
    background-size: 40px 40px;
}

#macrophages {
     background: radial-gradient(circle, #2ecc71 12%, transparent 18%),
                radial-gradient(circle, #2ecc71 12%, transparent 18%) 25px 25px,
                radial-gradient(circle, #2ecc71 12%, transparent 18%) 5px 40px,
                radial-gradient(circle, #2ecc71 12%, transparent 18%) 40px 5px,
                 radial-gradient(circle, #2ecc71 12%, transparent 18%) 15px 15px,
                radial-gradient(circle, #2ecc71 12%, transparent 18%) 35px 35px;
    background-size: 50px 50px;
}


#fibroblasts {
     width: 80px; /* Wider area */
     height: 100px;
     top: 50px;
     left: calc(50% - 40px);
     /* More complex gradient for spindle shape appearance */
     background:
         linear-gradient(to bottom right, transparent 45%, #e67e22 45%, #e67e22 55%, transparent 55%) 0px 0px,
         linear-gradient(to top left, transparent 45%, #e67e22 45%, #e67e22 55%, transparent 55%) 40px 0px,
         linear-gradient(to bottom right, transparent 45%, #e67e22 45%, #e67e22 55%, transparent 55%) 0px 50px,
         linear-gradient(to top left, transparent 45%, #e67e22 45%, #e67e22 55%, transparent 55%) 40px 50px;
     background-size: 40px 50px; /* Size of each gradient shape */
     background-repeat: no-repeat;
     transform: scale(0.9); /* Appear slightly smaller */
}

#blood-vessels {
    width: 50px; /* Wider area for vessels */
    height: 120px; /* Longer */
    top: 50px;
    left: calc(50% - 25px);
    background: linear-gradient(to bottom, transparent 0%, #e74c3c 10%, transparent 20%, #e74c3c 30%, transparent 40%, #e74c3c 50%, transparent 60%, #e74c3c 70%, transparent 80%, #e74c3c 90%, transparent 100%); /* More defined vessels */
    background-size: 100% 30px; /* Spacing of vessel segments */
    animation: vessel-grow 2s linear infinite; /* Simple animation for blood flow/growth feel */
    transform: scaleY(0.5); /* Appear to grow vertically */
}
#blood-vessels.active {
    opacity: 1;
    transform: scaleY(1);
}

@keyframes vessel-grow {
    0% { background-position-y: 0; }
    100% { background-position-y: 30px; } /* Adjust based on background-size */
}


#epithelial-cells {
    position: absolute;
    top: 48%; /* Just below epidermis line */
    left: 50%; /* Start centered */
    width: 0; /* Start as if closing from sides */
    height: 12px; /* Slightly thicker */
    background-color: #f5e1d3; /* Match epidermis color */
    border: 1px solid #d4c0b2; /* Outline */
    box-sizing: border-box;
    z-index: 19; /* Above clot/scar, below popups */
    transform: translateX(-50%); /* Keep centered while width grows */
    transition: opacity 0.8s ease-in, width 2s ease-out; /* Animate width */
}
#epithelial-cells.active {
    opacity: 1;
    width: 100%; /* Grow to full width */
}


#scar-tissue {
    top: 0;
    left: calc(50% - 20px); /* Align with clot */
    width: 40px;
    height: 100%;
    background-color: #d0b9a5; /* Paler scar color */
    z-index: 18; /* Below epithelial */
    transition: opacity 1s ease-in;
}
#scar-tissue.active {
    opacity: 1;
}


/* Popup styles */
.popup {
    position: absolute;
    background-color: #333;
    color: white;
    padding: 8px 15px; /* More padding */
    border-radius: 6px; /* More rounded */
    font-size: 0.9em; /* Slightly larger font */
    bottom: 20px; /* Position higher from bottom */
    left: 50%;
    transform: translateX(-50%) translateY(10px); /* Initial slightly lower */
    white-space: nowrap;
    z-index: 100;
    display: none; /* Initially hidden */
    opacity: 0; /* Start invisible */
    transition: opacity 0.3s ease-out, transform 0.3s ease-out; /* Smooth fade/slide */
}

.popup.active {
    display: block; /* Show for transition */
    opacity: 1;
    transform: translateX(-50%) translateY(0); /* Slide up */
}

#simulation-text {
    min-height: 50px; /* More space for text */
    border-top: 1px solid #eee;
    padding-top: 15px; /* More padding */
    font-size: 1.1em; /* Larger font */
    color: #444; /* Darker text */
    text-align: center; /* Center the text */
}

#next-step-button {
    display: block;
    margin: 20px auto 0; /* More margin */
    padding: 12px 25px; /* Larger button */
    font-size: 1.2em; /* Larger font */
    cursor: pointer;
    background-color: #007bff; /* Primary blue */
    color: white;
    border: none;
    border-radius: 6px; /* Rounded corners */
    transition: background-color 0.3s ease, transform 0.1s ease; /* Add subtle press effect */
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Button shadow */
}

#next-step-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    box-shadow: 0 4px 10px rgba(0, 123, 255, 0.4);
}
#next-step-button:active {
     transform: scale(0.98); /* Slightly shrink on click */
}


#show-explanation-button {
    display: block;
    margin: 25px auto 10px; /* More margin */
    padding: 10px 20px; /* Larger button */
    font-size: 1em;
    cursor: pointer;
    background-color: #6c757d; /* Secondary grey */
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
     box-shadow: 0 2px 5px rgba(108, 117, 125, 0.3);
}

#show-explanation-button:hover {
     background-color: #5a6268;
     box-shadow: 0 2px 7px rgba(108, 117, 125, 0.4);
}
#show-explanation-button:active {
     transform: scale(0.98);
}

#full-explanation {
    display: none; /* Initially hidden */
    margin-top: 20px;
    padding: 20px;
    border: 1px dashed #b0b0b0; /* Softer dashed border */
    background-color: #f8f8f8; /* Light grey background */
    border-radius: 8px;
    direction: rtl;
    text-align: right;
}

#full-explanation h2 {
    text-align: center;
    margin-bottom: 20px; /* More space */
    color: #333;
    font-size: 1.6em;
    border-bottom: 1px solid #eee; /* Separator */
    padding-bottom: 10px;
}

#full-explanation h3 {
    margin-top: 20px; /* More space above */
    margin-bottom: 8px; /* More space below */
    color: #555;
    font-size: 1.3em;
}

#full-explanation p, #full-explanation ul {
    margin-bottom: 12px; /* More space */
    line-height: 1.7; /* Improved line spacing */
    color: #444;
    font-size: 1em;
}

#full-explanation ul {
    padding-right: 25px; /* More padding */
    list-style-type: disc;
}

#full-explanation li {
    margin-bottom: 6px; /* More space */
}

/* General Body styles for better look */
body {
    font-family: 'Heebo', sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 20px;
    background-color: #f4f7f6; /* Light background color for the page */
}

h1 {
    text-align: center;
    color: #2c3e50; /* Darker heading color */
    margin-bottom: 30px; /* More space below title */
}

</style>

<button id="show-explanation-button">הצג הסבר מפורט</button>

<div id="full-explanation">
    <h2>המסע המדהים של ריפוי פצעים בעור</h2>

    <p>תהליך ריפוי פצע בעור הוא רצף ביולוגי מדהים, מדויק ומתואם שנועד להחזיר את העור לקדמותו ולהגן על הגוף מפני פולשים חיצוניים. הוא מתרחש במספר שלבים עיקריים, שחלקם חופפים זה לזה. בואו נצלול לעומק:</p>

    <h3>1. שלב ההמוסטאזיס (עצירת הדימום המיידית)</h3>
    <p>ברגע שהעור נחתך וכלי דם זעירים נפגעים, מתחיל מרוץ נגד הזמן לעצור את הדימום. כלי הדם מתכווצים במהירות כדי להאט את זרימת הדם, וטסיות הדם (חלקים זעירים של תאים בדם) נדבקות לאזור הפגוע ויוצרות "פקק" ראשוני. במקביל, מופעל מפל הקרישה המורכב, שבסופו נוצרת רשת של חלבון שנקרא פיברין. רשת הפיברין לוכדת כדוריות דם לבנות ואדומות ומתמצקת מעל הפצע, ויוצרת את קריש הדם היציב שכולנו מכירים, שאוטם את הפצע ומונע דימום נוסף.</p>

    <h3>2. שלב הדלקת (ניקוי והגנה)</h3>
    <p>מיד לאחר עצירת הדימום, מתחיל שלב קריטי של ניקוי והגנה. זהו שלב ה"דלקת" - תגובה טבעית וחיונית של הגוף לפציעה (ולא בהכרח סימן לזיהום, למרות שזיהום יכול להתרחש). תאי מערכת החיסון, בראשם הנויטרופילים ואחריהם המקרופאגים, נודדים במהירות לאזור הפצע. הנויטרופילים בולעים ומנטרלים חיידקים ופסולת קטנה, בעוד המקרופאגים, שהם "אוכלי כל" גדולים יותר, מפנים רקמה פגועה, שאריות קריש דם וגם נויטרופילים שמילאו את תפקידם. המקרופאגים משחקים תפקיד כפול: הם לא רק מנקים אלא גם מפרישים חומרים מיוחדים (גורמי גדילה וציטוקינים) שנותנים "אות" לתאים אחרים להתחיל את שלב התיקון והבנייה.</p>

    <h3>3. שלב הפרוליפרציה (בנייה והתחדשות)</h3>
    <p>כשהפצע נקי ומצב החירום חלף, מתחיל שלב הבנייה המסיבית. פיברובלסטים - תאים מיוחדים של רקמת החיבור - מגיעים לאזור הפצע ומתחילים לייצר כמויות גדולות של קולגן (בעיקר סוג III) וחלבונים אחרים. חומרים אלו ממלאים את חלל הפצע ויוצרים רקמה חדשה ועשירה בכלי דם זעירים, שנקראת "רקמת גרעון" (Granulation Tissue). במקביל, כלי דם חדשים נובטים וצומחים לתוך רקמת הגרעון (תהליך הנקרא אנגיוגנזה) כדי להבטיח אספקה סדירה של חמצן וחומרי מזון חיוניים לתאים הפעילים. ולבסוף, תאי האפידרמיס (השכבה החיצונית של העור) משולי הפצע מתחילים להתחלק ולנדוד לאט ובזהירות מעל רקמת הגרעון, מכסים את הפצע מלמעלה עד שהם נפגשים ויוצרים שכבת עור חיצונית רציפה.</p>

    <h3>4. שלב ההבשלה (חיזוק ועיצוב מחדש)</h3>
    <p>זהו השלב הארוך ביותר, שיכול להימשך חודשים ואף שנים. מטרתו לשפר את האיכות והחוזק של הרקמה המתוקנת. הקולגן הרך יותר (סוג III) שהופקד בשלב הקודם מוחלף בהדרגה בקולגן חזק ומסודר יותר (סוג I). סיבי הקולגן מסתדרים מחדש לאורך קווי המתח המופעלים על העור, מה שמגביר את חוזק הצלקת. צפיפות כלי הדם באזור פוחתת (ולכן הצלקת הופכת פחות אדומה), וגם מספר התאים הדלקתיים יורד. חשוב לזכור שהרקמה החדשה שנוצרה - הצלקת - לעולם לא תהיה זהה לחלוטין לעור המקורי. היא בדרך כלל פחות גמישה, אין בה זקיקי שיער או בלוטות זיעה, ויש לה מראה ומרקם שונים. תהליך ההבשלה גורם לצלקת להיות פחות בולטת וקשה עם הזמן.</p>

    <p>מסע הריפוי הוא עדות מדהימה ליכולות הגוף שלנו לתקן את עצמו ולהישאר מוגן.</p>

</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const simulationArea = document.getElementById('simulation-area');
    const descriptionText = document.getElementById('current-step-description');
    const nextButton = document.getElementById('next-step-button');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const fullExplanation = document.getElementById('full-explanation');

    // Simulation elements
    const bloodElement = document.getElementById('blood');
    const plateletsElement = document.getElementById('platelets');
    const clotElement = document.getElementById('clot');
    const neutrophilsElement = document.getElementById('neutrophils');
    const macrophagesElement = document.getElementById('macrophages');
    const fibroblastsElement = document.getElementById('fibroblasts');
    const bloodVesselsElement = document.getElementById('blood-vessels');
    const epithelialCellsElement = document.getElementById('epithelial-cells');
    const scarTissueElement = document.getElementById('scar-tissue');

    // Popups
    const plateletPopup = document.getElementById('popup-platelets');
    const clotPopup = document.getElementById('popup-clot');
    const neutrophilPopup = document.getElementById('popup-neutrophils');
    const macrophagePopup = document.getElementById('popup-macrophages');
    const fibroblastPopup = document.getElementById('popup-fibroblasts');
    const bvPopup = document.getElementById('popup-blood-vessels');
    const epPopup = document.getElementById('popup-epithelial-cells');

    let currentStepIndex = 0;

    // Define simulation steps with elements visible and clickable popups
    const steps = [
        {
            description: "שלב 1: רגע הפציעה! העור נחתך, כלי דם זעירים נקרעים ומתחיל דימום.",
            elements: [bloodElement], // Elements to show and make active
            clickable: {} // Elements that trigger popups
        },
        {
            description: "שלב 2: עוצרים את הדימום! כלי הדם מתכווצים, וטסיות הדם מגיעות במהירות ליצור פקק ראשוני.",
            elements: [bloodElement, plateletsElement],
            clickable: { platelets: plateletPopup }
        },
        {
            description: "שלב 3: פקק הקרישה נוצר! רשת סיבי פיברין אוטמת את הפצע ועוצרת סופית את הדימום.",
            elements: [clotElement], // Clot visually replaces blood/platelets in the cut
             clickable: { clot: clotPopup }
        },
        {
            description: "שלב 4: מתחיל הניקוי! נויטרופילים - השוטרים הראשונים - מגיעים לבלוע חיידקים ופסולת.",
            elements: [clotElement, neutrophilsElement],
            clickable: { clot: clotPopup, neutrophils: neutrophilPopup }
        },
         {
            description: "שלב 5: המקרופאגים מגיעים! הם ממשיכים את הניקוי ומפעילים את שלבי הבנייה הבאים.",
            elements: [clotElement, macrophagesElement], // Macrophages arrive, neutrophils might still be there but macrophages are key
            clickable: { clot: clotPopup, macrophages: macrophagePopup }
        },
        {
            description: "שלב 6: בנאי הגוף נכנסים לפעולה! פיברובלסטים מגיעים ליצור רקמת גרעון חדשה וקולגן.",
            elements: [clotElement, macrophagesElement, fibroblastsElement],
            clickable: { clot: clotPopup, macrophages: macrophagePopup, fibroblasts: fibroblastPopup }
        },
        {
            description: "שלב 7: אספקת הדם מתחדשת! כלי דם חדשים נובטים לתוך הרקמה המתרפאת כדי להביא חמצן ומזון.",
            elements: [clotElement, macrophagesElement, fibroblastsElement, bloodVesselsElement],
            clickable: { clot: clotPopup, macrophages: macrophagePopup, fibroblasts: fibroblastPopup, bloodVessels: bvPopup }
        },
         {
            description: "שלב 8: העור החיצוני נסגר! תאי אפידרמיס נודדים מעל הפצע כדי לכסות את השטח החשוף.",
            elements: [clotElement, macrophagesElement, fibroblastsElement, bloodVesselsElement, epithelialCellsElement],
            clickable: { clot: clotPopup, macrophages: macrophagePopup, fibroblasts: fibroblastPopup, bloodVessels: bvPopup, epithelialCells: epPopup }
        },
         {
            description: "שלב 9: הרקמה מתבגרת! הקריש מתכווץ ומתחיל להפוך לרקמת צלקת חזקה ומסודרת יותר.",
            elements: [scarTissueElement, epithelialCellsElement], // Scar tissue replaces clot visually, others fade/reduce
            clickable: { epithelialCells: epPopup } // Scar tissue itself isn't 'clickable' for info in this simple model
        },
        {
            description: "תהליך הריפוי הושלם! הפצע סגור, נותרה רקמת צלקת שתשתנה ותתבהר עם הזמן.",
            elements: [scarTissueElement, epithelialCellsElement], // Final state elements
            clickable: {} // End state, no clickable elements
        }
    ];

    // Map element IDs to element objects for easier lookup
    const elementMap = {
        blood: bloodElement,
        platelets: plateletsElement,
        clot: clotElement,
        neutrophils: neutrophilsElement,
        macrophages: macrophagesElement,
        fibroblasts: fibroblastsElement,
        bloodVessels: bloodVesselsElement,
        epithelialCells: epithelialCellsElement,
        scarTissue: scarTissueElement
    };

    const allSimElements = Object.values(elementMap);
    const allPopups = [plateletPopup, clotPopup, neutrophilPopup, macrophagePopup, fibroblastPopup, bvPopup, epPopup];


    function updateSimulation(stepIndex) {
        const currentStep = steps[stepIndex];
        const prevStepElements = stepIndex > 0 ? steps[stepIndex - 1].elements : [];

        descriptionText.textContent = currentStep.description;

        // Determine which elements should be active (visible and animated)
        const elementsToShow = currentStep.elements;

        // --- Animation Logic ---

        // 1. Hide elements that were active but are not in the current step
        prevStepElements.forEach(el => {
            if (!elementsToShow.includes(el)) {
                 el.classList.remove('active');
                 // Use setTimeout to set display: none *after* the transition
                 const transitionDuration = parseFloat(getComputedStyle(el).transitionDuration) * 1000;
                 setTimeout(() => {
                     if (!el.classList.contains('active')) { // Only hide if class wasn't re-added
                         el.style.display = 'none';
                     }
                 }, transitionDuration);
            }
        });

        // 2. Show and activate elements that should be in the current step
        elementsToShow.forEach(el => {
             if (!prevStepElements.includes(el)) {
                // If element was hidden, make it block first, then activate for transition
                el.style.display = 'block';
                 // Use requestAnimationFrame or setTimeout for next paint cycle before adding 'active' class
                 requestAnimationFrame(() => {
                     requestAnimationFrame(() => { // Double rAF is a common trick
                        el.classList.add('active');
                     });
                 });
             } else {
                 // If element was already active, ensure display is block and active class is present
                 el.style.display = 'block';
                 el.classList.add('active');
             }
        });


        // --- Interaction Logic (Popups) ---

        // Remove all previous click listeners and hide popups
        allSimElements.forEach(el => {
            el.onclick = null;
            el.style.cursor = 'default'; // Reset cursor
        });
        allPopups.forEach(p => {
            p.classList.remove('active');
            p.style.display = 'none'; // Ensure hidden after removing active
        });


        // Add new click listeners for elements specified in this step's 'clickable' list
        for (const elementId in currentStep.clickable) {
            const element = elementMap[elementId];
            const popup = currentStep.clickable[elementId];
            if (element && popup) {
                 element.style.cursor = 'pointer'; // Indicate clickable
                 element.onclick = (event) => {
                    event.stopPropagation(); // Prevent click from bubbling to simulationArea
                    // Hide all popups first
                     allPopups.forEach(p => {
                         p.classList.remove('active');
                         const transitionDuration = parseFloat(getComputedStyle(p).transitionDuration) * 1000;
                         setTimeout(() => {
                             if (!p.classList.contains('active')) {
                                 p.style.display = 'none';
                             }
                         }, transitionDuration);
                     });
                    // Show the specific popup
                    popup.style.display = 'block';
                     requestAnimationFrame(() => {
                        requestAnimationFrame(() => {
                           popup.classList.add('active');
                        });
                     });
                 };
            }
        }

        // Hide popups when clicking inside simulationArea but not on a clickable element
         simulationArea.onclick = () => {
             allPopups.forEach(p => {
                p.classList.remove('active');
                 const transitionDuration = parseFloat(getComputedStyle(p).transitionDuration) * 1000;
                 setTimeout(() => {
                     if (!p.classList.contains('active')) {
                         p.style.display = 'none';
                     }
                 }, transitionDuration);
            });
         };


        // Handle end of simulation
        if (stepIndex === steps.length - 1) {
            nextButton.textContent = "התחל מחדש";
        } else {
            nextButton.textContent = "השלב הבא";
        }
    }

    nextButton.addEventListener('click', () => {
        if (currentStepIndex < steps.length - 1) {
            currentStepIndex++;
        } else {
            // Restart simulation
            currentStepIndex = 0;
             // Ensure all elements are properly reset/hidden at start
             allSimElements.forEach(el => {
                el.classList.remove('active');
                 // Use a small delay to ensure classes are removed before hiding
                 setTimeout(() => {
                    el.style.display = 'none';
                 }, 50); // Small delay just in case
                el.onclick = null;
                el.style.cursor = 'default';
            });
             allPopups.forEach(p => {
                 p.classList.remove('active');
                 setTimeout(() => { p.style.display = 'none'; }, 50);
             });
        }
        updateSimulation(currentStepIndex);
    });

     showExplanationButton.addEventListener('click', () => {
        const isHidden = fullExplanation.style.display === 'none' || fullExplanation.style.display === '';
        fullExplanation.style.display = isHidden ? 'block' : 'none';
        showExplanationButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
    });

    // Initialize the simulation to the first step
    updateSimulation(currentStepIndex);
});
</script>
---