---
title: "מפגש עם עוצמת הטבע: סוגי התפרצויות געשיות"
english_slug: meeting-with-natures-power-volcanic-eruption-types
category: "מדעי הסביבה / כדור הארץ"
tags: ["געש", "התפרצות געשית", "וולקנולוגיה", "סוגי הרי געש", "לבה", "אפר געשי", "זרם פירוקלסטי"]
---

# מפגש עם עוצמת הטבע: סוגי התפרצויות געשיות

האם דמיינתם פעם לעמוד מול הר געש פעיל? חלק מההתפרצויות מרתקות בצפייה שקטה יחסית, עם נהרות לבה זוהרים. אחרות משחררות כוח אדיר בפיצוצים מחרישי אוזניים וענני אפר שמגיעים לגובה הטיסה של מטוסים. מה הופך כל התפרצות לייחודית כל כך, וכיצד ההבדלים הללו מעצבים את פני כדור הארץ?

התנסו בסימולציה הקצרה שלפניכם כדי לגלות את ההבדלים בין סוגי ההתפרצויות העיקריים!

<div class="volcano-simulator-container">
    <h2 class="interaction-prompt">בחרו את עוצמת הטבע שברצונכם לפגוש:</h2>
    <div class="controls">
        <button data-type="hawaiian" class="control-button">הוואית</button>
        <button data-type="strombolian" class="control-button">סטרומבוליאנית</button>
        <button data-type="plinian" class="control-button">פליניאנית</button>
    </div>

    <div class="eruption-display">
        <div class="sky"></div>
        <div class="ground"></div>
        <div class="volcano-cone"></div>
        <div class="eruption-area">
            <!-- Animation elements will be added here by JS -->
            <div class="vent"></div> <!-- Representing the opening -->
        </div>
        <div class="stats-display">
            <h3>מאפיינים עיקריים:</h3>
            <p><strong>סוג התפרצות:</strong> <span id="eruption-type-name">-- בחר התפרצות --</span></p>
            <p><strong>טמפרטורת לבה אופיינית:</strong> <span id="lava-temp">--</span></p>
            <p><strong>אופי הפליטה:</strong> <span id="flow-speed">--</span></p>
            <p><strong>גובה עמוד התפרצות:</strong> <span id="column-height">--</span></p>
        </div>
        <div class="eruption-message"></div> <!-- Area for short messages -->
    </div>

    <div class="animation-controls">
        <button id="play-reset-button" disabled>התחל התפרצות</button>
    </div>
</div>

<style>
/* General Styles */
.volcano-simulator-container {
    font-family: 'Arial', sans-serif; /* Use a common, clean sans-serif */
    direction: rtl;
    text-align: center;
    margin: 30px auto;
    max-width: 800px;
    border: 1px solid #dcdcdc;
    padding: 20px;
    border-radius: 12px; /* Softer corners */
    background-color: #ffffff; /* Clean white background */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

.volcano-simulator-container h2.interaction-prompt {
    color: #2c3e50; /* Dark blue-grey */
    margin-bottom: 20px;
    font-size: 1.6rem;
}

/* Controls */
.controls {
    margin-bottom: 25px;
}

.control-button {
    padding: 12px 25px;
    margin: 5px;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    background-color: #3498db; /* Bright blue */
    color: white;
    font-size: 1.1rem;
    transition: background-color 0.3s ease, transform 0.1s ease;
    min-width: 120px; /* Ensure consistent size */
}

.control-button:hover {
    background-color: #2980b9; /* Darker blue */
    transform: translateY(-2px); /* Subtle lift effect */
}

.control-button.active {
    background-color: #2ecc71; /* Emerald green when active */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    pointer-events: none; /* Cannot click while active */
}

/* Eruption Display */
.eruption-display {
    position: relative;
    width: 100%;
    height: 450px; /* Increased height for more drama */
    border: 1px solid #bdc3c7; /* Light grey border */
    margin-top: 20px;
    overflow: hidden;
    border-radius: 8px; /* Match container border-radius */
    background: linear-gradient(to bottom, #a6e7ff 0%, #e0f6ff 100%); /* Brighter initial sky */
    box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
}

.sky {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, #a6e7ff 0%, #e0f6ff 100%); /* Default sky */
    transition: background 2s ease; /* Smooth transition for sky color */
    z-index: 0;
}

.ground {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 120px; /* Taller ground */
    background-color: #7f8c8d; /* Darker greyish-brown for ground */
    z-index: 1;
}

.volcano-cone {
    position: absolute;
    bottom: 119px; /* Just above the ground */
    left: 50%;
    transform: translateX(-50%);
    width: 200px; /* Wider base */
    height: 180px; /* Taller cone */
    background-color: #34495e; /* Dark volcanic rock color */
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
    z-index: 2;
}

.eruption-area {
    position: absolute;
    /* Positioned relative to the bottom of eruption-display, just above the cone tip */
    bottom: calc(120px + 180px - 10px); /* Ground height + Cone height - slight overlap */
    left: 50%;
    transform: translateX(-50%);
    width: 80px; /* Wider vent area */
    height: 80px;
    z-index: 3; /* Above cone */
    overflow: visible; /* Allow particles to go beyond bounds initially */
    pointer-events: none; /* Don't block clicks */
}

.vent {
     position: absolute;
     bottom: 0;
     left: 50%;
     transform: translateX(-50%);
     width: 30px;
     height: 10px;
     background-color: #4a2b1b; /* Dark vent opening color */
     border-radius: 5px 5px 0 0;
     z-index: 1; /* Ensure it's above some particles if needed */
}


.stats-display {
    position: absolute;
    top: 15px;
    right: 15px; /* Position on the right in RTL */
    background-color: rgba(255, 255, 255, 0.9); /* More opaque */
    padding: 15px;
    border-radius: 8px;
    text-align: right;
    z-index: 5;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.stats-display h3 {
    margin-top: 0;
    font-size: 1.2rem;
    color: #2c3e50;
    border-bottom: 1px solid #ecf0f1; /* Light separator */
    padding-bottom: 8px;
    margin-bottom: 8px;
}

.stats-display p {
    margin: 6px 0;
    font-size: 1rem;
    color: #34495e;
}

.stats-display strong {
    color: #c0392b; /* Reddish accent for labels */
}

.eruption-message {
    position: absolute;
    bottom: 10px; /* Positioned above ground */
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(0, 0, 0, 0.6);
    color: white;
    padding: 8px 15px;
    border-radius: 5px;
    font-size: 0.9rem;
    opacity: 0;
    transition: opacity 0.5s ease;
    z-index: 5;
    pointer-events: none;
}

.eruption-message.visible {
    opacity: 1;
}

/* --- Animation Styles (Dynamic elements added by JS) --- */

/* Hawaiian Lava Flow */
.lava-stream {
    position: absolute;
    bottom: 0; /* Starts from eruptionArea bottom */
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 0;
    background: linear-gradient(to bottom, #ff8c00, #ff4500); /* Gradient for depth */
    border-radius: 5px 5px 20px 20px; /* Rounded base */
    z-index: 4; /* Above cone, below stats */
    opacity: 0.9;
    will-change: height, width, transform; /* Optimize animation */
}

/* Strombolian Ejecta (Bombs) */
.ejecta-bomb {
    position: absolute;
    bottom: 0; /* Starts from eruptionArea bottom */
    left: 50%;
    transform: translate(-50%, 0); /* Initial positioning */
    width: 10px; /* Slightly larger */
    height: 10px;
    background-color: #a0522d; /* Sienna */
    border-radius: 50%;
    z-index: 4;
    opacity: 1;
     box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
    will-change: transform, opacity;
}

/* Small smoke puff for Strombolian */
.strombolian-puff {
    position: absolute;
    bottom: 0; /* Starts at vent */
    left: 50%;
    transform: translateX(-50%);
    width: 15px;
    height: 15px;
    background-color: rgba(128, 128, 128, 0.5); /* Grey semi-transparent */
    border-radius: 50%;
    z-index: 3; /* Below bomb, above cone */
    opacity: 0;
    animation: puff-and-fade 1s ease-out forwards; /* CSS animation for simple effect */
    pointer-events: none;
}

@keyframes puff-and-fade {
    0% { transform: translate(-50%, 0) scale(1); opacity: 0.5; }
    100% { transform: translate(-50%, -30px) scale(2); opacity: 0; }
}


/* Plinian Ash Column */
.ash-column {
    position: absolute;
    bottom: 0; /* Starts from eruptionArea bottom */
    left: 50%;
    transform: translateX(-50%);
    width: 100px; /* Wider initial width */
    height: 0;
    background: linear-gradient(to top, rgba(108, 122, 137, 0.8), rgba(169, 169, 169, 0.7), rgba(220, 220, 220, 0.6)); /* Grey gradient */
    z-index: 4;
    opacity: 1;
    will-change: height, width, transform, opacity;
}

.plinian-pyroclastic {
     position: absolute;
     bottom: 119px; /* Positioned just above the ground level */
     left: 0;
     width: 100%;
     height: 40px; /* Taller initial height */
     background: linear-gradient(to right, rgba(139, 69, 19, 0), rgba(139, 69, 19, 0.8), rgba(139, 69, 19, 0.8), rgba(139, 69, 19, 0)); /* Transparent edges */
     z-index: 3; /* Below ash, above ground/cone base */
     opacity: 0; /* Initially hidden */
     pointer-events: none;
     will-change: transform, opacity;
}


/* Animation Controls */
.animation-controls {
    margin-top: 20px;
    min-height: 40px; /* Reserve space to prevent layout shift */
}

#play-reset-button {
    padding: 12px 30px;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    background-color: #f1c40f; /* Sunflower yellow */
    color: #2c3e50; /* Dark text */
    font-size: 1.2rem;
    transition: background-color 0.3s ease, transform 0.1s ease;
    min-width: 180px;
}

#play-reset-button:hover:not(:disabled) {
    background-color: #f39c12; /* Orange-yellow */
    transform: translateY(-2px);
}

#play-reset-button:disabled {
    background-color: #bdc3c7; /* Light grey when disabled */
    color: #7f8c8d;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
}


/* Explanation Toggle */
#toggle-explanation {
    display: block;
    margin: 30px auto;
    padding: 10px 20px;
    border: none;
    border-radius: 20px; /* Softer pill */
    cursor: pointer;
    background-color: #9b59b6; /* Amethyst */
    color: white;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #8e44ad; /* Darker amethyst */
}

/* Explanation Section */
.explanation {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    background-color: #ecf0f1; /* Light background for explanation */
    text-align: justify;
    line-height: 1.7; /* More comfortable reading */
    color: #34495e;
    display: none; /* Initially hidden */
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.explanation h3 {
    color: #c0392b; /* Reddish accent for headings */
    margin-top: 25px;
    margin-bottom: 12px;
    border-bottom: 2px solid #bdc3c7; /* Thicker separator */
    padding-bottom: 8px;
    font-size: 1.4rem;
}

.explanation h3:first-child {
    margin-top: 0;
}

.explanation p {
    margin-bottom: 18px;
}

.explanation ul {
    margin-bottom: 18px;
    padding-right: 25px; /* Increased padding */
    list-style: disc outside; /* Use disc, outside padding */
}

.explanation li {
    margin-bottom: 10px;
}

/* Small screens adjustments */
@media (max-width: 600px) {
    .control-button {
        font-size: 1rem;
        padding: 10px 15px;
        min-width: inherit; /* Allow buttons to shrink */
    }
    #play-reset-button {
         font-size: 1rem;
         padding: 10px 15px;
         min-width: inherit;
    }
    .stats-display {
        position: static; /* Stack on small screens */
        margin-top: 15px;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.95);
    }
    .eruption-display {
        height: 350px; /* Reduce height */
    }
     .ground {
         height: 80px;
     }
    .volcano-cone {
         bottom: 79px;
         height: 120px;
         width: 150px;
    }
     .eruption-area {
         bottom: calc(80px + 120px - 10px);
         width: 60px;
         height: 60px;
     }
}

</style>

<button id="toggle-explanation">הצג הסבר מעמיק על סוגי ההתפרצויות</button>

<div class="explanation">
    <h3>מבוא קצר: מה גורם להר געש להתפרץ?</h3>
    <p>דמיינו מעמקי אדמה רותחים! עמוק מתחת לפני השטח, קיים סלע מותך בטמפרטורות קיצוניות - **מאגמה**. כשהמאגמה עולה כלפי מעלה, בועות גז לכודות בתוכה מתחילות להשתחרר, בדומה לפתיחת בקבוק שמפניה מנוער. לחץ הגזים הזה דוחף את המאגמה ואת חומרים נוספים דרך סדקים ופתחים בקרום כדור הארץ, במה שאנו מכנים **התפרצות געשית**. החומרים המשתחררים יכולים להיות לבה (מאגמה שהגיעה לפני השטח), גזים (בעיקר אדי מים, פחמן דו-חמצני, גופרית), וחלקיקי סלע בגדלים שונים הנקראים **חומר פירוקלסטי** (אפר, לפיל, פצצות געשיות).</p>

    <h3>סוד הכוח: צמיגות וגזים</h3>
    <p>מדוע התפרצויות שונות כל כך? ההבדלים הדרמטיים נובעים בעיקר משני מאפיינים של המאגמה:</p>
    <ul>
        <li>**צמיגות (Viscosity):** זוהי מידת ה"סמיכות" או ההתנגדות לזרימה של המאגמה. חשבו על דבש לעומת מים - הדבש צמיג יותר. מאגמה בעלת תכולת סיליקה גבוהה וטמפרטורה נמוכה יותר נוטה להיות צמיגה (סמיכה) מאוד, בעוד מאגמה עם תכולת סיליקה נמוכה וטמפרטורה גבוהה דלילה יותר.</li>
        <li>**תכולת גזים (Gas Content):** כמות הגזים המומסים במאגמה. גזים הם המנוע מאחורי התפרצות מתפוצצת. אם המאגמה צמיגה, הגזים נכלאים בה ומצטבר לחץ עצום. כשהלחץ משתחרר בפתאומיות, מתרחש פיצוץ אלים. אם המאגמה דלילה, הגזים משתחררים בקלות יחסית ובשקט, מה שמוביל לזרימות לבה.</li>
    </ul>
    <p>השילוב בין צמיגות המאגמה וכמות הגזים הלכודים בה קובע את אופי ההתפרצות: שקטה וזורמת, או אלימה ומתפוצצת.</p>

    <h3>1. התפרצות הוואית: נהרות של אש (Hawaiian Eruption)</h3>
    <p>אלו הן לרוב ההתפרצויות העדינות ביותר, האופייניות לאיי הוואי (ומכאן שמן). הן מתרחשות כאשר מאגמה בעלת **צמיגות נמוכה** מאוד (דלילה) ו**תכולת גזים נמוכה** יחסית עולה אל פני השטח. הגזים משתחררים בקלות ובשקט יחסי מהלבה, ומונעים הצטברות לחץ מסוכנת. התוצאה היא זרימות לבה דלילה שיכולה לנוע במהירות משתנה (עד עשרות קמ"ש במדרונות תלולים) ולכסות שטחים נרחבים. לעיתים נדירות יותר נראות "מזרקות לבה" קצרות ויפות בפתח ההר. התפרצויות מסוג זה בונות הרי געש שטוחים ונרחבים הנקראים הרי געש מגן (shield volcanoes), בעלי צורה הדומה למגן של אביר המונח על הקרקע.</p>
    <ul>
        <li>מאפיינים: מאגמה דלילה (צמיגות נמוכה), מעט גזים.</li>
        <li>אופי ההתפרצות: שקטה יחסית, בעיקר זרימות לבה.</li>
        <li>דוגמאות: הרי הגעש הפעילים בהוואי (קילוואה, מאונה לואה).</li>
    </ul>

    <h3>2. התפרצות סטרומבוליאנית: זיקוקים מהר הגעש (Strombolian Eruption)</h3>
    <p>סוג זה, הקרוי על שם הר הגעש סטרומבולי באיטליה, אלים יותר מהוואיות אך פחות הרסני מהסוג הפליניאני. כאן נפגוש מאגמה בעלת **צמיגות בינונית** ו**תכולת גזים בינונית**. הגזים מצליחים להשתחרר, אך לא בקלות כמו בהתפרצות הוואית. הם נכלאים במאגמה לזמן קצר, ואז משתחררים בפיצוצים קצובים (מדי כמה דקות עד שעות). כל פיצוץ משגר לגובה נמוך עד בינוני חומרים פירוקלסטיים בגודל של סלעים קטנים עד גדולים (לפיל ופצצות געשיות). זרמי לבה יכולים להופיע גם כן, אך הם לרוב קצרים יותר וצמיגים יותר מאשר בהתפרצות הוואית. התפרצויות אלו בונות לרוב הרי געש חרוטיים קטנים יחסית (cinder cones).</p>
     <ul>
        <li>מאפיינים: מאגמה בצמיגות בינונית, כמות גזים בינונית.</li>
        <li>אופי ההתפרצות: פיצוצים קצובים, ירי סלעים וחומרים לגובה נמוך-בינוני.</li>
        <li>דוגמאות: הר הגעש סטרומבולי (איטליה).</li>
    </ul>

    <h3>3. התפרצות פליניאנית: עמוד אפר ענק ואסון (Plinian Eruption)</h3>
    <p>אלו הן ההתפרצויות המרהיבות, אך גם האלימות וההרסניות ביותר שידועות. הן קרויות על שם פליניוס הצעיר שתיעד את התפרצות הר וזוב שהחריבה את פומפיי בשנת 79 לספירה. התפרצויות אלו מתרחשות כאשר מאגמה בעלת **צמיגות גבוהה** מאוד ו**תכולת גזים גבוהה מאוד** מגיעה לפני השטח. הגזים נכלאים בצמיגות המאגמה ומצטבר לחץ עצום. כשהלחץ משתחרר בפתאומיות דרך פתח ההר, נוצר פיצוץ מסיבי המשגר עמוד התפרצות אדיר של אפר געשי, גזים וסלעים קטנים לגובה קיצוני - לעיתים 20, 30, ואף 50 קילומטרים לתוך האטמוספרה! עמוד זה, הנראה לרוב כפטריית עשן ענקית, עלול לקרוס חזרה במורד ההר וליצור **זרמים פירוקלסטיים** - תערובת קטלנית ולוהטת במיוחד של גזים, אפר וסלעים, הנעה במהירות של מאות קמ"ש. זרמים אלו הורסים כל מה שעומד בדרכם. התפרצויות פליניאניות יכולות להשפיע על האקלים העולמי (עקב חלקיקי האפר באטמוספרה) ולהרוס אזורים שלמים.</p>
     <ul>
        <li>מאפיינים: מאגמה סמיכה (צמיגות גבוהה), כמות גזים גבוהה מאוד.</li>
        <li>אופי ההתפרצות: פיצוץ עצום, עמוד אפר ענק ומהיר לגובה רב, לעיתים מלווה בזרמים פירוקלסטיים קטלניים.</li>
        <li>דוגמאות: וזוב (איטליה, 79 לספירה), סנט הלנס (ארה"ב, 1980), פינטובו (הפיליפינים, 1991).</li>
    </ul>

    <h3>לסיכום: מופע הטבע המדהים והמגוון</h3>
    <p>מהזרימה השקטה של לבה הוואית, דרך "זיקוקי" הסטרומבולי, ועד לעוצמה האדירה של התפרצות פליניאנית - הרי געש מספקים מופע מגוון של עוצמת הטבע, הנשלטת על ידי הפיזיקה הפשוטה יחסית של צמיגות וגזים. הבנת ההבדלים הללו חיונית למדע הגיאולוגיה, לניטור הרי געש, ולהערכת הסיכונים הטמונים בהם לאוכלוסיות החיות בקרבתם.</p>

</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const eruptionTypes = {
        hawaiian: {
            name: 'הוואית',
            stats: {
                temp: '~1100-1200°C',
                speed: 'זרימות לבה דלילה (עד עשרות קמ"ש)',
                columnHeight: 'מזרקות קצרות (עד 2 ק"מ)',
            },
            animation: 'hawaiian',
            skyColor: 'linear-gradient(to bottom, #a6e7ff 0%, #e0f6ff 100%)' // Sunny sky
        },
        strombolian: {
            name: 'סטרומבוליאנית',
            stats: {
                temp: '~1000-1100°C',
                speed: 'פיצוצים קצובים (ירי חומרים)',
                columnHeight: 'כמה מאות מטרים עד 2 ק"מ',
            },
            animation: 'strombolian',
             skyColor: 'linear-gradient(to bottom, #87ceeb 0%, #b0d8f0 100%)' // Slightly cloudier sky
        },
        plinian: {
            name: 'פליניאנית',
            stats: {
                temp: '~700-900°C (מאגמה צמיגה)',
                speed: 'עמוד אפר במהירות קול, זרמים פירוקלסטיים (עד מאות קמ"ש)',
                columnHeight: '10-50+ ק"מ (לתוך הסטרטוספרה)',
            },
            animation: 'plinian',
             skyColor: 'linear-gradient(to bottom, #34495e 0%, #7f8c8d 60%, #bdc3c7 100%)' // Dark, ash-filled sky
        }
    };

    const typeButtons = document.querySelectorAll('.control-button');
    const eruptionDisplayName = document.getElementById('eruption-type-name');
    const lavaTempSpan = document.getElementById('lava-temp');
    const flowSpeedSpan = document.getElementById('flow-speed');
    const columnHeightSpan = document.getElementById('column-height');
    const eruptionDisplay = document.querySelector('.eruption-display'); // Parent of eruption-area
    const eruptionArea = document.querySelector('.eruption-area');
    const playResetButton = document.getElementById('play-reset-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.querySelector('.explanation');
    const skyDiv = document.querySelector('.sky');
    const groundDiv = document.querySelector('.ground');
     const volcanoCone = document.querySelector('.volcano-cone');
     const eruptionMessageDiv = document.querySelector('.eruption-message');


    let activeType = null;
    let animationInterval = null; // For Strombolian bomb scheduling
    let animationRunning = false; // Flag to check if animation is in progress
    let animationCleanupTimeout = null; // To manage cleanups after animations finish

    // Calculate eruption point position dynamically
     const getEruptionPointBaseY = () => {
         const eruptionAreaRect = eruptionArea.getBoundingClientRect();
         const eruptionDisplayRect = eruptionDisplay.getBoundingClientRect();
         // Calculate bottom position of eruptionArea relative to eruptionDisplay's *height*
         // This is the distance from the bottom of eruptionDisplay to the bottom of eruptionArea
         const bottomRelativeToDisplay = eruptionDisplayRect.bottom - eruptionAreaRect.bottom;
         // The Y position within the eruptionDisplay from its bottom
         return bottomRelativeToDisplay;
     };


    function resetDisplay() {
        // Clear previous animation elements from eruption area and eruption display
        eruptionArea.innerHTML = '<div class="vent"></div>'; // Keep the vent
        const oldLava = eruptionDisplay.querySelector('.lava-stream');
         if(oldLava) oldLava.remove();
        const oldPyro = eruptionDisplay.querySelector('.plinian-pyroclastic');
         if(oldPyro) oldPyro.remove();
         const oldAsh = eruptionArea.querySelector('.ash-column'); // Ash is appended to eruptionArea in this logic
         if(oldAsh) oldAsh.remove();


        // Clear intervals and animation frames
        clearInterval(animationInterval);
        animationInterval = null;

        // Stop Web Animations API animations
        eruptionDisplay.getAnimations().forEach(anim => anim.cancel());
        eruptionArea.getAnimations().forEach(anim => anim.cancel());


        animationRunning = false;
        playResetButton.textContent = 'התחל התפרצות';
        playResetButton.disabled = !activeType; // Re-enable if a type is selected

        // Reset sky color to default (or currently selected type's sky if applicable)
         if (activeType && eruptionTypes[activeType]) {
             skyDiv.style.background = eruptionTypes[activeType].skyColor;
         } else {
             skyDiv.style.background = 'linear-gradient(to bottom, #a6e7ff 0%, #e0f6ff 100%)';
         }

        // Hide message
        hideMessage();
    }

    function updateStats(typeData) {
        eruptionDisplayName.textContent = typeData.name;
        lavaTempSpan.textContent = typeData.stats.temp;
        flowSpeedSpan.textContent = typeData.stats.speed;
        columnHeightSpan.textContent = typeData.stats.columnHeight;
    }

    function selectEruptionType(type) {
        // Always reset any ongoing animation when selecting a new type
        resetDisplay();

        activeType = type;
        updateStats(eruptionTypes[type]);

        // Highlight the selected button
        typeButtons.forEach(btn => btn.classList.remove('active'));
        document.querySelector(`.control-button[data-type="${type}"]`).classList.add('active');

        // Enable the play button once a type is selected
        playResetButton.disabled = false;

        // Set initial sky color based on selected type
        skyDiv.style.background = eruptionTypes[type].skyColor;

        showMessage(`סוג נבחר: התפרצות ${eruptionTypes[type].name}`);
    }

    function showMessage(text, duration = 2000) {
        eruptionMessageDiv.textContent = text;
        eruptionMessageDiv.classList.add('visible');
        if (animationCleanupTimeout) clearTimeout(animationCleanupTimeout); // Clear previous timeouts
        animationCleanupTimeout = setTimeout(() => {
            hideMessage();
        }, duration);
    }

    function hideMessage() {
        eruptionMessageDiv.classList.remove('visible');
         if (animationCleanupTimeout) clearTimeout(animationCleanupTimeout);
         animationCleanupTimeout = null;
    }


     function startAnimation(type) {
         if (animationRunning) return; // Prevent multiple animations

         animationRunning = true;
         playResetButton.textContent = 'אפס התפרצות';
         playResetButton.disabled = false; // Always enabled when playing for reset

         // Ensure display is clean before starting
         resetDisplay();

         // Set the sky color immediately for the animation
         skyDiv.style.background = eruptionTypes[type].skyColor;

         showMessage(`מתחילה התפרצות ${eruptionTypes[type].name}!`);


         const eruptionAreaRect = eruptionArea.getBoundingClientRect();
         const eruptionDisplayRect = eruptionDisplay.getBoundingClientRect();
         const coneRect = volcanoCone.getBoundingClientRect();

         // Y coordinate of the top of the cone (relative to the bottom of eruption-display)
         const coneTipBottomY_Display = eruptionDisplayRect.bottom - coneRect.top;


         if (type === 'hawaiian') {
             // Simulate lava flow starting from eruptionArea center, flowing down
             const lavaStream = document.createElement('div');
             lavaStream.classList.add('lava-stream');
             // Positioning relative to eruptionArea
             lavaStream.style.bottom = '0px';
             lavaStream.style.left = '50%';
             lavaStream.style.transform = 'translateX(-50%)';
             lavaStream.style.width = '10px';
             lavaStream.style.height = '0px';
             // Append lava stream to the main eruptionDisplay so it can flow past eruptionArea bounds
             eruptionDisplay.appendChild(lavaStream);


             // Target height for the lava stream, relative to eruptionArea bottom
             // Should reach the level of the ground base
             const eruptionAreaBottomY_Display = getEruptionPointBaseY();
             const groundHeight = groundDiv.clientHeight;
             const maxFlowHeightFromEruptionAreaBottom = eruptionAreaBottomY_Display - groundHeight;


             lavaStream.animate([
                 { height: '0px', width: '10px', transform: 'translateX(-50%)' },
                 { height: `${maxFlowHeightFromEruptionAreaBottom}px`, width: '150px', transform: 'translateX(-50%)' } // Widens as it flows down
             ], {
                 duration: 6000, // 6 seconds for flow
                 easing: 'linear',
                 fill: 'forwards'
             }).onfinish = () => {
                 // Animation finished
                 animationRunning = false;
                 playResetButton.textContent = 'התחל התפרצות';
                 showMessage('התפרצות הוואית הסתיימה.', 3000);
             };


         } else if (type === 'strombolian') {
             // Simulate bombs/ejecta with puffs
             const bombInterval = 400; // ms between bomb launches
             const bombDurationMin = 1200; // ms
             const bombDurationMax = 1800; // ms
             const numBombs = 15;
             let bombsLaunched = 0;

              // Eruption area height defines max upward space relative to its bottom
             const eruptionAreaHeightPx = eruptionArea.clientHeight;


             animationInterval = setInterval(() => {
                 if (bombsLaunched >= numBombs) {
                     clearInterval(animationInterval);
                     animationInterval = null;
                     // Wait for the last bomb animation to potentially finish before setting state
                      setTimeout(() => {
                          if (animationRunning) { // Check if reset hasn't happened
                              animationRunning = false;
                              playResetButton.textContent = 'התחל התפרצות';
                               showMessage('התפרצות סטרומבוליאנית הסתיימה.', 3000);
                          }
                      }, bombDurationMax + 200); // Wait a bit longer than the max bomb duration
                     return;
                 }

                 // Create bomb element
                 const bomb = document.createElement('div');
                 bomb.classList.add('ejecta-bomb');
                 // Start at the bottom center of the eruptionArea
                 bomb.style.bottom = '0px';
                 bomb.style.left = '50%';
                 bomb.style.transform = 'translate(-50%, 0)';
                 eruptionArea.appendChild(bomb); // Append to eruptionArea

                 // Create puff element
                 const puff = document.createElement('div');
                 puff.classList.add('strombolian-puff');
                 // Start at the bottom center of the eruptionArea (at the vent)
                 puff.style.bottom = '0px';
                 puff.style.left = '50%';
                 puff.style.transform = 'translate(-50%, 0)';
                 eruptionArea.appendChild(puff); // Append puff to eruptionArea


                 // Randomize trajectory
                 const duration = bombDurationMin + Math.random() * (bombDurationMax - bombDurationMin);
                 // Max vertical height relative to eruptionArea bottom. Should go significantly above eruptionArea
                 // Let's use a height relative to the total display height above the cone tip.
                 const maxApexY_Display = (eruptionDisplayRect.bottom - coneRect.top) * (0.4 + Math.random() * 0.4); // Apex 40-80% above cone tip level
                 // Convert maxApexY_Display to be relative to eruptionArea bottom
                  const maxApexY_EruptionArea = maxApexY_Display - (eruptionDisplayRect.bottom - eruptionAreaRect.bottom);


                 const endX_EruptionArea = (Math.random() - 0.5) * 2 * 150; // Land up to 150px left/right of eruptionArea center

                 // Animate bomb position using Web Animations API
                 bomb.animate([
                     { transform: 'translate(-50%, 0px) scale(1)', opacity: 1 }, // Start at bottom, centered, full size
                     { transform: `translate(calc(-50% + ${endX_EruptionArea / 2}px), -${maxApexY_EruptionArea}px) scale(0.8)`, opacity: 1, offset: 0.5 }, // Peak height, slightly smaller
                     { transform: `translate(calc(-50% + ${endX_EruptionArea}px), 0px) scale(0.6)`, opacity: 0 } // End at eruptionArea bottom level, horizontal shift, fades out
                 ], {
                     duration: duration,
                     easing: 'cubic-bezier(0.4, 0, 0.6, 1)', // Simulate parabolic trajectory
                     fill: 'forwards'
                 }).onfinish = () => {
                     bomb.remove(); // Clean up
                 };

                 bombsLaunched++;

             }, bombInterval);


         } else if (type === 'plinian') {
             // Simulate ash column and pyroclastic flow
             const ashColumn = document.createElement('div');
             ashColumn.classList.add('ash-column');
              // Position relative to eruptionArea bottom
             ashColumn.style.bottom = '0px';
             ashColumn.style.left = '50%';
             ashColumn.style.transform = 'translateX(-50%)';
             ashColumn.style.width = '100px'; // Initial width
             ashColumn.style.height = '0px';
             eruptionArea.appendChild(ashColumn); // Append ash column to eruptionArea

             const pyroclasticFlow = document.createElement('div');
             pyroclasticFlow.classList.add('plinian-pyroclastic');
             // Position relative to the eruptionDisplay container, just above the ground
             pyroclasticFlow.style.bottom = `${groundDiv.clientHeight -1}px`; // Position slightly above ground
             pyroclasticFlow.style.left = '0%';
             pyroclasticFlow.style.width = '0%'; // Starts invisible horizontally
             pyroclasticFlow.style.opacity = '0'; // Starts transparent
             eruptionDisplay.appendChild(pyroclasticFlow);


             // Ash column animation - rapid vertical growth and horizontal spread
             const eruptionAreaBottomY_Display = getEruptionPointBaseY();
             const totalDisplayHeight = eruptionDisplay.clientHeight;
             // Max column height (can go far beyond display bounds) - set a large value for animation
             const maxColumnHeight_EruptionArea = totalDisplayHeight * 2; // Go high above the display


             ashColumn.animate([
                 { height: '0px', width: '100px', transform: 'translateX(-50%) scaleY(0)', opacity: 1 },
                 { height: `${maxColumnHeight_EruptionArea}px`, width: '300px', transform: 'translateX(-50%) scaleY(1)', opacity: 0.7 }
             ], {
                 duration: 8000, // 8 seconds to reach max height and spread
                 easing: 'ease-out',
                 fill: 'forwards'
             });


             // Pyroclastic flow animation - triggered slightly after ash starts
             const pyroclasticDelay = 1500; // ms delay before flow starts

             setTimeout(() => {
                 pyroclasticFlow.animate([
                     { width: '0%', opacity: 0.8, offset: 0 },
                     { width: '100%', opacity: 0.8, offset: 0.1 }, // Rapid horizontal spread
                     { width: '100%', opacity: 0, offset: 1 } // Fade out over time
                 ], {
                     duration: 4000, // 4 seconds for the flow duration
                     easing: 'linear',
                     fill: 'forwards'
                 }).onfinish = () => {
                      // Flow animation finished (can remove the element if desired, but fade is okay)
                 };

                 // Animate height change for flow (briefly taller)
                 pyroclasticFlow.animate([
                     { height: '40px', offset: 0 },
                      { height: '60px', offset: 0.2 },
                      { height: '40px', offset: 0.5 },
                      { height: '30px', offset: 1 }
                 ], {
                     duration: 4000,
                     easing: 'ease-out',
                      fill: 'forwards'
                 });

                  showMessage('זרם פירוקלסטי קטלני!');

             }, pyroclasticDelay);

             // Set general animation duration for the Plinian event
              const totalPlinianDuration = 10000; // 10 seconds for the whole event to feel complete

              animationCleanupTimeout = setTimeout(() => {
                  // Check if reset didn't happen
                   if (animationRunning) {
                       animationRunning = false;
                       playResetButton.textContent = 'התחל התפרצות';
                       showMessage('התפרצות פליניאנית הסתיימה.', 3000);
                   }
              }, totalPlinianDuration);


         }
     }


    // Event Listeners
    typeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const type = button.dataset.type;
            selectEruptionType(type);
        });
    });

    playResetButton.addEventListener('click', () => {
        if (!activeType) {
            // This case should be prevented by the disabled state
            return;
        }

        if (!animationRunning) {
            startAnimation(activeType);
        } else { // If state is playing (animationRunning is true)
            resetDisplay();
            showMessage(`הסימולציה אותחלה. בחר סוג התפרצות או התחל שוב.`, 3000);
        }
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק על סוגי ההתפרצויות';
        // Optional: Scroll to explanation if showing
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial state: No type selected, stats are placeholders, play button disabled.
    resetDisplay(); // Ensure initial state is clean and button disabled
    updateStats({ name: '-- בחר התפרצות --', stats: { temp: '--', speed: '--', columnHeight: '--' }}); // Set initial stats text

});

</script>
```