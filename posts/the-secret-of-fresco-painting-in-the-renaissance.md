---
title: "סוד הפרסקו: לצייר על טיח רטוב בזמן הרנסאנס"
english_slug: the-secret-of-fresco-painting-in-the-renaissance
category: "תולדות האמנות"
tags:
  - פרסקו
  - רנסאנס
  - ציור קיר
  - טכניקות אמנות
  - מיכלאנג'לו
---
# סוד הפרסקו: לצייר על טיח רטוב בזמן הרנסאנס

דמיינו את עצמכם באטלייה רומנטי בפירנצה, עומדים מול קטע קיר ענק המכוסה בטיח טרי. ריח הסיד באוויר, ובידכם מברשת ספוגה בפיגמנט טבעי. השמש שוקעת, ואתם יודעים שיש לכם רק שעות ספורות להשלים את החלק הזה של הציור לפני שהטיח יתייבש וההזדמנות תאבד. כך נולדו יצירות המופת עוצרות הנשימה של הרנסאנס.

<div id="fresco-app" class="fresco-container">
    <div id="canvas-container" class="art-frame">
        <canvas id="fresco-canvas" width="600" height="400"></canvas>
        <div id="drying-overlay" class="overlay"></div>
        <div id="dry-message" class="overlay-message hidden">הטיח התייבש! הצבע לא ייטמע.</div>
        <div id="timer" class="info-box">זמן נותר: <span id="time-left">60</span> שניות</div>
        <div id="status" class="info-box">הטיח רטוב! ציירו בחופשיות.</div>
    </div>
    <div id="color-palette" class="palette">
        <div class="color-swatch selected" data-color="#B03A2E" style="background-color: #B03A2E;"></div> <!-- Muted Red -->
        <div class="color-swatch" data-color="#2874A6" style="background-color: #2874A6;"></div> <!-- Muted Blue -->
        <div class="color-swatch" data-color="#1E8449" style="background-color: #1E8449;"></div> <!-- Muted Green -->
        <div class="color-swatch" data-color="#F4D03F" style="background-color: #F4D03F;"></div> <!-- Earthy Yellow -->
        <div class="color-swatch" data-color="#7D3C98" style="background-color: #7D3C98;"></div> <!-- Muted Purple -->
        <div class="color-swatch" data-color="#0E0E0E" style="background-color: #0E0E0E;"></div> <!-- Near Black -->
    </div>
    <p class="instruction-text">בחרו צבע מהפלטה וציירו על הטיח הלח. שימו לב לשעון החול - הזמן שלכם מוגבל!</p>
    <button id="start-new-giornata" class="action-button">התחילו 'ג'ורנאטה' חדשה</button>
</div>

<button id="toggle-explanation" class="toggle-button">הצגת מסמך ההסבר על טכניקת הפרסקו</button>

<div id="explanation" class="explanation-section hidden">
    <h2>הסודות העתיקים של הפרסקו בואונו (Fresco Buono)</h2>
    טכניקת ה"פרסקו" (שפירושה באיטלקית: "טרי") היא שיטת ציור קיר ייחודית שבה האמן עובד ישירות על שכבת טיח רטוב וטרייה. הצבעים, שהם פיגמנטים טבעיים טחונים דק מעורבבים עם מים בלבד, חודרים עמוק לתוך הטיח הלח. כאשר הטיח מתייבש, מתרחש תהליך כימי מופלא הנקרא קרבוניזציה: הסידן ההידרוקסידי שבטיח הופך לגבישי סידן פחמתי קשיחים (כמו אבן גיר). הפיגמנטים נלכדים בתוך רשת גבישים זו, והופכים למעשה לחלק בלתי נפרד מהקיר עצמו – לא רק יושבים על פני השטח.

    <h3>מסע בזמן: שורשי הטכניקה</h3>
    פרסקו אינה המצאה של הרנסאנס; היא הייתה בשימוש כבר בתרבויות עתיקות, החל מיוון המינואית (קנוסוס) ועד לרומא העתיקה (פומפיי, הרקולנאום). אך הפריחה המחודשת והכניסה לפנתיאון האמנות העולמית אירעו ברנסאנס האיטלקי (מאות 14-16). שמות כמו ג'וטו, מזאצ'ו, רפאל, וכמובן מיכלאנג'לו, הפכו לשם נרדף ליצירות מופת שנוצרו בטכניקה תובענית זו.

    <h3>בניית הקיר: יסודות הפרסקו</h3>
    הכנה קפדנית היא סוד ההצלחה. הקיר מטופל במספר שכבות טיח, לכל אחת תפקיד:
    <ul>
        <li>**ארצ'יצ'ו (Arriccio):** השכבה הראשונה, מחוספסת ועבה, מונחת ישירות על המבנה האבן או הלבנים. היא מספקת בסיס אחיד ומאפשרת לאמן לשרטט עליה את הקומפוזיציה הכללית בקווים גדולים (ה"סינופיה").</li>
        <li>**אינטונאקו (Intonaco):** השכבה העליונה, חלקה ועדינה יותר, המכילה לרוב אבקת שיש דקה בנוסף לסיד וחול. שכבה זו מונחת רק על השטח שבו האמן מתכוון לעבוד באותו יום. זהו המשטח ה"טרי" שעליו מתבצע הציור בפועל.</li>
    </ul>

    <h3>חומרי הקסם: פיגמנטים וסיד</h3>
    *   **סיד כבוי (Slaked Lime):** המרכיב הקושר, סידן הידרוקסידי (Ca(OH)₂), המעניק לטיח את תכונותיו הכימיות המיוחדות.
    *   **אגרגטים:** חול או אבקת שיש בגדלים שונים, המעורבבים עם הסיד ליצירת הטיח.
    *   **פיגמנטים טבעיים:** אבקות צבע המופקות ממינרלים ואדמות (למשל, אדמה אדומה לאדום, אזוריט לכחול, מלכיט לירוק). פיגמנטים מסוימים שרגישים לבסיסיות של הסיד אינם מתאימים לפרסקו בואונו (כמו חלק מהכחולים והירוקים, מה שהגביל במקצת את פלטת הצבעים). הם מעורבבים במים בלבד, ללא חומר קשר נוסף.

    <h3>ריקוד עם הזמן: תהליך העבודה היומי</h3>
    תהליך יצירת פרסקו הוא מרוץ נגד הזמן, המחייב תכנון וביצוע קפדניים:
    1.  **הכנת הקיר והשרטוט הראשוני (סינופיה):** לאחר יישום הארצ'יצ'ו ויבושו, שורטטה הקומפוזיציה הכללית (לרוב באדמה אדומה) ישירות על הטיח היבש.
    2.  **תכנון ה'ג'ורנאטה':** האמן חילק את היצירה כולה לקטעים קטנים שניתן לצייר ולהשלים ביום עבודה אחד – כל קטע כזה נקרא 'ג'ורנאטה' ("יום" באיטלקית). גודל הג'ורנאטה נקבע לפי מורכבות החלק וקצב העבודה המשוער.
    3.  **יישום האינטונאקו:** ממש לפני תחילת הציור היומי, מניחים שכבה טרייה של אינטונאקו רק על שטח הג'ורנאטה המתוכנן. שכבה זו חייבת להישאר לחה מספיק לאורך כל שעות הציור.
    4.  **העברת השרטוט המדויק:** השרטוט המפורט של הג'ורנאטה הועבר לטיח הלח. שיטות נפוצות כללו: ניקוב קווי השרטוט בסינופיה והטפת אבקת פחם דרך החורים (spolvero), או חריטה עדינה של הקווים מתוך רישום על נייר שהוצמד לקיר.
    5.  **הציור בזמן אמת:** האמן וצוותו ציירו במהירות ובדיוק על האינטונאקו הרטוב. הצבעים נספגו לתוך הטיח הלח. עבודה על טיח שהתייבש חלקית (Fresco Secco) הייתה אפשרית אך פחות עמידה.
    6.  **התייבשות והטמעה (קרבוניזציה):** כשהטיח מתייבש, הסידן ההידרוקסידי מגיב עם הפחמן הדו-חמצני שבאוויר והופך לסידן פחמתי קשה. הפיגמנטים נלכדים במבנה הגבישי החדש. תהליך זה מפסיק כשהטיח יבש לחלוטין.

    <h3>ה'ג'ורנאטה' - יום עבודה של אמן</h3>
    ה'ג'ורנאטה' היא לא רק קטע פיזי בציור, אלא גם יחידת זמן ותכנון. הצורך להשלים את כל הג'ורנאטה לפני שהטיח מתייבש דרש מהאמן תכנון מראש, מיומנות גבוהה ומהירות ביצוע. קווי החיבור העדינים בין ג'ורנאטות שונות ניתנים לעיתים לזיהוי על יצירות פרסקו גדולות, ומהווים עדות לתהליך העבודה.

    <h3>מדוע הזמן כה קריטי? הכימיה שבקיר</h3>
    תהליך הקרבוניזציה, המקנה לפרסקו את עמידותו האגדית, תלוי בנוכחות מים. הסידן ההידרוקסידי (Ca(OH)₂) בטיח הלח סופח CO₂ מהאוויר והופך ל-CaCO₃ (סידן פחמתי). המים משמשים כתווך הכרחי לתגובה זו. הפיגמנטים שחודרים לטיח בזמן שהוא לח נלכדים בתוך גבישי ה-CaCO₃ הנוצרים. ברגע שהטיח יבש לחלוטין, התגובה נפסקת. ציור על טיח יבש ('פרסקו סקו') לא יאפשר לצבעים להיטמע באותה צורה – הם יישארו על פני השטח, יהיו פחות עמידים ויינטו לדהות או להתקלף.

    <h3>מאזן הכוחות: יתרונות וחסרונות</h3>
    *   **יתרונות מדהימים:** עמידות חסרת תקדים לאורך מאות ואלפי שנים, צבעים עזים וזוהרים כשהם נטמעים בטיח הבהיר, חסינות יחסית ללחות ושינויי טמפרטורה.
    *   **אתגרים משמעותיים:** מחייב מהירות, דיוק ותכנון מושלם; קושי רב בתיקונים (לרוב יש להסיר את הטיח ולצייר מחדש את כל הג'ורנאטה); דורש מומחיות רבה לא רק בציור אלא גם בהבנת תהליך הכנת הטיח והכימיה שלו.

    <h3>מופעי ראווה על קירות הזמן</h3>
    יצירות פרסקו מפורסמות כוללות את התקרה האייקונית וה"דין האחרון" בקפלה הסיסטינית (מיכלאנג'לו), ציורי הקיר המרשימים בחדר החתן והכלה במנטובה (אנדראה מנטניה), והפרסקאות המהפכניות בקפלת בראנקאצ'י בפירנצה (מזאצ'ו), ועוד רבות מהעת העתיקה.

    <h3>פרסקו סקו: האלטרנטיבה ה"קלה" יותר?</h3>
    "פרסקו סקו" (Secco - "יבש") היא טכניקה שבה צובעים על טיח שכבר התייבש. בשיטה זו, מערבבים את הפיגמנטים עם חומר מקשר (כמו דבק ביצים, דבק חיות או שמנים) כדי שידבקו לקיר. היתרון הוא האפשרות לעבוד לאט יותר, לתקן בקלות, ולהשתמש בפלטת צבעים רחבה יותר (כולל פיגמנטים שאינם עמידים בפני בסיסיות הסיד). החיסרון הגדול הוא העמידות הנמוכה לאין ערוך לעומת פרסקו בואונו – הצבע נוטה להתקלף ולהתפורר עם הזמן. לכן, פרסקו בואונו נחשב לטכניקה הנעלה והיוקרתית יותר.

    <h3>מאחורי הקלעים: צוות האמנים</h3>
    יצירת ציור פרסקו מונומנטלי לא הייתה עבודה של אדם אחד בלבד. המאסטר היה אמנם אחראי על התפיסה האמנותית, התכנון, השרטוטים הראשיים, ולרוב צייר את החלקים המרכזיים והחשובים בג'ורנאטות. אך לצדו עמד צוות מומחים: גבסנים (intonacatori) מומחים בהכנת הטיח ויישומו בזמן הנכון, עוזרים לערבוב פיגמנטים, ולעיתים גם ציירים שהיו אחראים על רקעים וחלקים פשוטים יותר. שיתוף הפעולה, התיאום והתזמון המדויק של הצוות כולו היו קריטיים להצלחה.
</div>

<style>
    :root {
        --plaster-color: #EDECE4;
        --wet-overlay-color: rgba(174, 214, 241, 0.1); /* Subtle blue hint for wet */
        --dry-overlay-color-start: rgba(250, 240, 230, 0.0); /* Starts transparent */
        --dry-overlay-color-end: rgba(250, 240, 230, 0.7); /* Ends opaque beige */
        --earthy-red: #B03A2E;
        --earthy-blue: #2874A6;
        --highlight-color: #007bff;
        --text-color: #333;
        --subtle-border-color: #ccc;
        --box-shadow-color: rgba(0, 0, 0, 0.15);
        --font-sans: 'Arial', sans-serif;
        --font-serif: 'Georgia', serif; /* Using standard fonts for simplicity */
    }

    body {
        font-family: var(--font-sans);
        line-height: 1.6;
        color: var(--text-color);
        padding-bottom: 40px; /* Add space for sticky elements or just general footer space */
    }

    h1, h2, h3 {
        font-family: var(--font-serif);
        color: #555; /* Slightly darker or different shade */
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
    }

    #fresco-app {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
        padding: 20px;
        background-color: #f8f8f8; /* Light background for the interactive section */
        border-radius: 8px;
        box-shadow: 0 4px 10px var(--box-shadow-color);
    }

    .art-frame {
        position: relative;
        width: 100%;
        max-width: 600px;
        border: 10px solid #ddd; /* Frame border */
        box-shadow: 4px 4px 12px var(--box-shadow-color);
        margin-bottom: 20px;
        background-color: var(--plaster-color); /* Background behind canvas */
        overflow: hidden; /* Ensure overlays stay within bounds */
    }

    #fresco-canvas {
        display: block;
        background-color: var(--plaster-color);
        cursor: crosshair;
        touch-action: none; /* Prevent default touch actions like scrolling/zooming */
    }

    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* Allow clicks/touches to pass through */
        transition: background-color 1s ease; /* Smooth transition for drying effect */
    }

    .overlay-message {
         position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: var(--earthy-red);
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        pointer-events: none;
        z-index: 10; /* Ensure it's above the overlay */
        background-color: rgba(255, 255, 255, 0.85);
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 2px 5px var(--box-shadow-color);
        animation: pulse 1.5s infinite ease-in-out; /* Subtle animation */
    }

    @keyframes pulse {
        0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        50% { transform: translate(-50%, -50%) scale(1.05); opacity: 0.9; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    }


    .info-box {
        position: absolute;
        padding: 8px 12px;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
        font-size: 0.9em;
        font-weight: bold;
        box-shadow: 0 1px 3px var(--box-shadow-color);
    }

    #timer {
        top: 10px;
        right: 10px;
        color: var(--earthy-red);
    }

    #status {
        bottom: 10px;
        left: 10px;
        color: var(--earthy-blue);
    }

    #status.dry {
        color: var(--earthy-red);
        font-weight: bold;
    }


    .palette {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
        padding: 10px;
        background-color: #eee; /* Palette background */
        border-radius: 5px;
        box-shadow: inset 0 1px 3px var(--box-shadow-color);
    }

    .color-swatch {
        width: 35px;
        height: 35px;
        margin: 0 8px;
        cursor: pointer;
        border: 3px solid transparent; /* Border for selection */
        box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, border-color 0.2s ease;
        border-radius: 50%; /* Make them round */
    }

    .color-swatch:hover {
        transform: scale(1.15);
    }

    .color-swatch.selected {
        border-color: var(--highlight-color);
        box-shadow: 0 0 6px var(--highlight-color);
        transform: scale(1.1); /* Keep selected slightly larger */
    }

    .instruction-text {
        font-size: 1em;
        color: #555;
        margin-bottom: 20px;
        text-align: center;
    }

    .action-button, .toggle-button {
        display: block;
        margin: 15px auto;
        padding: 12px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: var(--highlight-color);
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    .action-button:hover, .toggle-button:hover {
        background-color: #0056b3;
    }
     .action-button:active, .toggle-button:active {
        transform: scale(0.98);
     }


    .explanation-section {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid var(--subtle-border-color);
        background-color: #f9f9f9;
        border-radius: 8px;
        line-height: 1.7;
    }

    .explanation-section h2, .explanation-section h3 {
        color: #444;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        font-family: var(--font-serif);
    }

     .explanation-section h2:first-child {
         margin-top: 0;
     }

    .explanation-section ul {
        padding-left: 25px;
    }

    .explanation-section li {
        margin-bottom: 0.8em;
    }

     .explanation-section strong {
         color: #555;
     }


    .hidden {
        display: none;
    }

    /* Improve drawing look - maybe add subtle texture or varying opacity via JS */
    /* For simplicity, basic line drawing is kept in JS, but CSS influences the container/background */

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('fresco-canvas');
        const ctx = canvas.getContext('2d');
        const timerDisplay = document.getElementById('time-left');
        const statusDisplay = document.getElementById('status');
        const dryOverlay = document.getElementById('drying-overlay');
        const dryMessage = document.getElementById('dry-message');
        const colorPalette = document.getElementById('color-palette');
        const colorSwatches = colorPalette.querySelectorAll('.color-swatch');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const startNewGiornataButton = document.getElementById('start-new-giornata');

        let isDrawing = false;
        let isWet = true;
        let totalTime = 60; // Seconds for one giornata
        let timeLeft = totalTime;
        let timerInterval;
        let lastX = 0;
        let lastY = 0;
        let selectedColor = '#B03A2E'; // Default color
        const dryingStartsAt = 20; // Seconds remaining when drying effect begins
        const dryThreshold = 0; // Seconds remaining when it's considered fully dry

        // Set canvas size based on container
        function resizeCanvas() {
             const container = canvas.parentElement;
             // Maintain aspect ratio or set fixed height - fixed height for now
             canvas.width = container.clientWidth;
             canvas.height = 400;
             // Note: Resizing canvas clears it. In a real app, save/restore content.
             // For this simulation, we start fresh or assume the user redraws.
             // Let's add a simple visual cue to the canvas being fresh.
             // Maybe fill with plaster color? It's already background.
        }

        // Initial resize and add resize listener
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        // Drawing functions
        function getEventPos(e) {
            const rect = canvas.getBoundingClientRect();
            let clientX, clientY;

            if (e.touches && e.touches.length > 0) { // Handle touch events
                clientX = e.touches[0].clientX;
                clientY = e.touches[0].clientY;
            } else { // Handle mouse events
                clientX = e.clientX;
                clientY = e.clientY;
            }

            return [
                clientX - rect.left,
                clientY - rect.top
            ];
        }

        function startDrawing(e) {
            if (!isWet) {
                showDryMessage();
                return;
            }
            e.preventDefault(); // Prevent scrolling on touch devices
            isDrawing = true;
            [lastX, lastY] = getEventPos(e);
            // Start drawing a new path
             ctx.beginPath();
             ctx.moveTo(lastX, lastY);
        }

        function draw(e) {
            if (!isDrawing || !isWet) return;
            e.preventDefault();

            const [x, y] = getEventPos(e);

            // Adjust stroke opacity as it dries
            let opacity = 1;
            if (timeLeft <= dryingStartsAt && timeLeft > dryThreshold) {
                // Fade opacity linearly from 1 to 0 in the drying phase
                opacity = timeLeft / dryingStartsAt; // Simple linear fade
                opacity = Math.max(0.1, opacity); // Minimum opacity so stroke is visible
            } else if (timeLeft <= dryThreshold) {
                 opacity = 0; // Should not draw, but as backup
                 isWet = false; // Ensure isWet is false if timer ran out mid-stroke
                 return; // Stop drawing if fully dry
            }

            const [r, g, b] = hexToRgb(selectedColor);
            ctx.strokeStyle = `rgba(${r}, ${g}, ${b}, ${opacity})`;
            ctx.lineWidth = 4; // Slightly thicker for brush effect
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round'; // Smooth corners

            ctx.lineTo(x, y);
            ctx.stroke();

            [lastX, lastY] = [x, y];
        }

        function stopDrawing() {
            if (isDrawing) {
                 isDrawing = false;
                 ctx.closePath(); // Close the current path
            }
        }

         function hexToRgb(hex) {
            const bigint = parseInt(hex.slice(1), 16);
            const r = (bigint >> 16) & 255;
            const g = (bigint >> 8) & 255;
            const b = bigint & 255;
            return [r, g, b];
        }


        // Timer and Drying functions
        function updateTimer() {
            timeLeft--;
            timerDisplay.textContent = timeLeft;

            // Update drying overlay opacity
            if (timeLeft <= dryingStartsAt && timeLeft >= dryThreshold) {
                 const dryProgress = 1 - (timeLeft / dryingStartsAt); // 0 at start, 1 at end
                 const opacity = dryProgress * (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--dry-overlay-color-end').split(',')[3]) || 0.7); // Fade to the end opacity
                 dryOverlay.style.backgroundColor = `rgba(250, 240, 230, ${opacity})`;
                 statusDisplay.textContent = "הטיח מתייבש...";
                 statusDisplay.classList.add('drying'); // Add class for potential styling
            } else if (timeLeft < dryThreshold) {
                // Ensure fully dry state is set
                timeLeft = dryThreshold; // Prevent negative time
                timerDisplay.textContent = timeLeft;
            }


            if (timeLeft <= dryThreshold) {
                clearInterval(timerInterval);
                isWet = false;
                statusDisplay.textContent = "הטיח יבש! אי אפשר לצייר.";
                statusDisplay.classList.remove('drying');
                statusDisplay.classList.add('dry');
                dryOverlay.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue('--dry-overlay-color-end');
                canvas.style.cursor = 'not-allowed';
                showDryMessage();
            }
        }

        function startTimer() {
             if (timerInterval) clearInterval(timerInterval); // Clear any existing timer
             timerInterval = setInterval(updateTimer, 1000);
        }

        function showDryMessage() {
             dryMessage.classList.remove('hidden');
             // Hide message after a few seconds
             setTimeout(() => {
                 dryMessage.classList.add('hidden');
             }, 3000); // Show for 3 seconds
        }

        // Color palette functions
        function selectColor(color) {
            selectedColor = color;
            colorSwatches.forEach(swatch => swatch.classList.remove('selected'));
            document.querySelector(`.color-swatch[data-color="${color}"]`).classList.add('selected');
        }

        colorSwatches.forEach(swatch => {
            swatch.addEventListener('click', () => {
                selectColor(swatch.getAttribute('data-color'));
            });
        });

        // Explanation toggle
        toggleExplanationButton.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            if (!explanationDiv.classList.contains('hidden')) {
                toggleExplanationButton.textContent = 'הסתר מסמך הסבר';
            } else {
                toggleExplanationButton.textContent = 'הצגת מסמך ההסבר על טכניקת הפרסקו';
            }
        });

        // Start New Giornata button
        startNewGiornataButton.addEventListener('click', () => {
            resetGiornata();
        });

        function resetGiornata() {
            clearInterval(timerInterval); // Stop current timer
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
            timeLeft = totalTime; // Reset time
            isWet = true; // Set back to wet
            timerDisplay.textContent = timeLeft; // Update timer display
            statusDisplay.textContent = "הטיח רטוב! ציירו בחופשיות."; // Reset status
            statusDisplay.classList.remove('dry', 'drying'); // Remove dry classes
            dryOverlay.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue('--wet-overlay-color'); // Reset overlay
            dryMessage.classList.add('hidden'); // Hide dry message
            canvas.style.cursor = 'crosshair'; // Reset cursor
            startTimer(); // Start timer again
        }


        // Add event listeners for drawing (both mouse and touch)
        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mouseout', stopDrawing); // Stop drawing if mouse leaves canvas
        canvas.addEventListener('mousemove', draw);

        canvas.addEventListener('touchstart', startDrawing, { passive: false });
        canvas.addEventListener('touchend', stopDrawing);
        canvas.addEventListener('touchcancel', stopDrawing);
        canvas.addEventListener('touchmove', draw, { passive: false });


        // Initialize
        resetGiornata(); // Start the first giornata
        selectColor(selectedColor); // Select initial color visually
    });
</script>
---