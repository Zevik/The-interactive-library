---
title: "קסם הסלעים המאוזנים: מבנים שוברי שיווי משקל בטבע"
english_slug: secret-of-balancing-rocks-how-they-stand
category: "מדעי הסביבה / כדור הארץ"
tags: ['גיאולוגיה', 'בלייה', 'ארוזיה', 'סלעים', 'גאומורפולוגיה', 'תהליכי נוף']
---
# קסם הסלעים המאוזנים: מבנים שוברי שיווי משקל בטבע

דמיינו סלע ענק, טון של משקל מוצק, מונח באורח פלא על בסיס דקיק, כאילו הוא מרחף על נקודה. המראה המדהים הזה של "סלע מאוזן" נראה לעיתים כאילו הוא מתריס נגד כוח המשיכה וכל מה שלמדנו על יציבות. איך הטבע מצליח לפסל יצירות אמנות גאולוגיות כאלה, ומה מאפשר להן לעמוד איתן כל כך הרבה זמן, דורות על גבי דורות? הצטרפו למסע גאולוגי שיגלה את סודם!

<div class="interactive-app">
    <h2 class="app-title">פסלו את הסלע שלכם: סימולציית בלייה וארוזיה</h2>
    <p class="app-description">צאו למסע בזמן גאולוגי! בחרו את סוג הסלע והשפיעו על תהליכי הבלייה כדי לחזות במו עיניכם איך נוצר סלע מאוזן - צעד אחר צעד.</p>

    <div class="controls">
        <div class="control-group">
            <label for="rock-type">סוג הסלע:</label>
            <select id="rock-type">
                <option value="homogeneous">סלע הומוגני (עמידות אחידה)</option>
                <option value="layered">סלע עם שכבות חלשות יותר</option>
                <option value="weak-base">סלע עם בסיס פגיע במיוחד</option>
            </select>
        </div>

        <div class="control-group">
            <label for="weathering-factors">כוחות הטבע הפועלים:</label>
            <select id="weathering-factors">
                <option value="wind">רוח (סחיפת חול)</option>
                <option value="water">מים (זרימה ובליה כימית)</option>
                <option value="temp-changes">שינויי טמפרטורה (קפיאה/הפשרה, התרחבות)</option>
                <option value="all">שילוב כוחות (רוח, מים, טמפרטורה)</option>
            </select>
        </div>

        <button id="start-sim" class="sim-button primary">התחילו לפסל!</button>
        <button id="reset-sim" class="sim-button secondary">אפסו ונסו שוב</button>
    </div>

    <div class="simulation-area">
        <canvas id="rock-canvas"></canvas>
        <div class="timeline">
             <div class="timeline-progress"></div>
            <div class="time-marker" style="left: 0%;">התחלה</div>
            <div class="time-marker" style="left: 25%;"></div>
            <div class="time-marker" style="left: 50%;"></div>
            <div class="time-marker" style="left: 75%;"></div>
            <div class="time-marker" style="left: 100%;">עידנים גאולוגיים</div>
        </div>
        <div id="sim-time" class="time-display">זמן גאולוגי שעבר: 0%</div>
         <div id="sim-message" class="sim-message">בחרו הגדרות והתחילו בסימולציה</div>
    </div>
</div>

<style>
    /* כללי */
    .interactive-app {
        font-family: 'Arial', sans-serif; /* בחירת פונט נעים לעין */
        background: linear-gradient(to bottom, #e0f2f7, #b3e5fc); /* רקע עדין עם גרדיאנט */
        padding: 30px;
        border-radius: 15px; /* פינות מעוגלות יותר */
        margin: 30px auto; /* מרכוז והוספת מרווח */
        max-width: 800px; /* הגבלת רוחב מקסימלי */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* צל עדין לאפליקציה */
        direction: rtl; /* עברית מימין לשמאל */
        text-align: right; /* יישור טקסט לימין */
    }

    .app-title {
        color: #0277bd; /* כחול כהה */
        text-align: center;
        margin-bottom: 15px;
        font-size: 2em; /* גודל כותרת גדול יותר */
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    .app-description {
        color: #01579b; /* כחול מעט בהיר יותר */
        text-align: center;
        margin-bottom: 25px;
        font-size: 1.1em;
        line-height: 1.6;
    }

    /* בקרות */
    .controls {
        margin-bottom: 25px;
        display: flex;
        gap: 20px; /* מרווח בין אלמנטים */
        align-items: flex-end; /* יישור אלמנטים בתחתית */
        flex-wrap: wrap; /* מעבר שורה במסכים קטנים */
        justify-content: center; /* מרכז את הפקדים */
    }

    .control-group {
         display: flex;
         flex-direction: column;
         align-items: flex-start;
    }

    .controls label {
        display: block; /* כל לייבל בשורה משלו */
        margin-bottom: 8px;
        font-weight: bold;
        color: #01579b;
        font-size: 1em;
    }

    .controls select {
        padding: 10px 15px;
        border: 2px solid #0288d1; /* גבול כחול */
        border-radius: 8px; /* פינות עגולות לselect */
        background-color: #e1f5fe; /* רקע כחול בהיר */
        color: #01579b;
        font-size: 1em;
        cursor: pointer;
        transition: border-color 0.3s ease, box-shadow 0.3s ease; /* אנימציית מעבר */
    }

     .controls select:hover {
         border-color: #0277bd;
         box-shadow: 0 0 8px rgba(2, 119, 189, 0.3);
     }

    .sim-button {
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em; /* גודל כפתור גדול יותר */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease; /* אנימציית מעבר */
        min-width: 150px; /* רוחב מינימלי לכפתורים */
         text-align: center;
    }

    .sim-button.primary {
        background-color: #0288d1; /* כחול ראשי */
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .sim-button.primary:hover {
        background-color: #0277bd;
        transform: translateY(-2px); /* אפקט הרמה קל */
    }

     .sim-button.primary:active {
         transform: translateY(0); /* אפקט לחיצה */
     }

    .sim-button.secondary {
        background-color: #e0e0e0; /* אפור משני */
        color: #333;
        border: 1px solid #ccc;
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .sim-button.secondary:hover {
        background-color: #d5d5d5;
         transform: translateY(-1px);
    }

     .sim-button.secondary:active {
         transform: translateY(0);
     }


    /* אזור סימולציה */
    .simulation-area {
        position: relative;
        width: 100%;
        max-width: 700px; /* הגדלת רוחב מקסימלי לקנבס */
        margin: 20px auto;
        text-align: center;
        background-color: #b2dfdb; /* רקע ירוק מנטה עדין */
        border-radius: 10px;
        padding: 15px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* צל פנימי עדין */
    }

    #rock-canvas {
        border: 2px solid #00796b; /* גבול ירוק כהה */
        background: linear-gradient(to top, #80cbc4, #b2dfdb); /* גרדיאנט עדין ברקע הקנבס */
        width: 100%;
        height: 350px; /* הגדלת גובה הקנבס */
        display: block;
        margin-bottom: 15px;
        border-radius: 8px;
        position: relative; /* לטובת אנימציות */
        overflow: hidden; /* חיתוך אנימציות חלקיקים */
    }

     /* אנימציית חלקיקי בליה (עשוי לדרוש JS או פסאודו-אלמנטים מורכבים - נטפל בזה ב-JS) */


    /* ציר זמן */
    .timeline {
        position: relative;
        width: 95%; /* רוחב כמעט מלא */
        height: 15px; /* גובה קטן יותר */
        background-color: #e0f2f7; /* רקע בהיר */
        border-radius: 8px;
        margin: 10px auto; /* מרכוז */
        overflow: hidden; /* חיתוך פס ההתקדמות */
         box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }

     .timeline-progress {
         position: absolute;
         top: 0;
         left: 0;
         height: 100%;
         width: 0%; /* יתעדכן ב-JS */
         background-color: #00796b; /* צבע התקדמות */
         border-radius: 8px;
         transition: width 0.1s linear; /* אנימציית התקדמות חלקה */
     }

    .time-marker {
        position: absolute;
        top: -5px; /* מיקום מעל הפס */
        /* bottom: 0; */ /* להשאיר רק למעלה */
        width: 2px;
        background-color: #01579b; /* קו כחול כהה */
        font-size: 0.7em; /* גודל פונט קטן יותר */
        color: #01579b;
        text-align: center;
        transform: translateX(-50%); /* מרכז את הקו */
        white-space: nowrap; /* מונע שבירת שורה בטקסט */
        padding-top: 20px; /* מרווח לטקסט מתחת לקו */
    }
     .time-marker:nth-child(2) { transform: translateX(0%); text-align: right;} /* Adjust start marker */
     .time-marker:nth-child(6) { transform: translateX(-100%); text-align: left;} /* Adjust end marker */


    .time-display {
        margin-top: 8px;
        font-weight: bold;
        color: #01579b;
        font-size: 1em;
         min-height: 1.2em; /* כדי למנוע קפיצות כשהטקסט משתנה */
    }

     .sim-message {
         margin-top: 15px;
         font-size: 1.1em;
         color: #004d40; /* צבע הודעה */
         min-height: 1.2em;
     }


    /* הסבר */
    #show-explanation-btn {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #00796b; /* ירוק כהה */
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    #show-explanation-btn:hover {
        background-color: #004d40;
        transform: translateY(-2px);
    }
     #show-explanation-btn:active {
         transform: translateY(0);
     }


    #explanation {
        margin-top: 30px;
        border-top: 2px dashed #0288d1; /* קו הפרדה מסוגנן */
        padding-top: 30px;
        display: none; /* Hidden by default */
        color: #333; /* צבע טקסט כללי */
        line-height: 1.7; /* מרווח שורות */
    }

    #explanation h2 {
        color: #0277bd;
        margin-bottom: 20px;
        font-size: 1.8em;
         text-align: center;
    }

     #explanation h3 {
         color: #01579b;
         margin-top: 25px;
         margin-bottom: 10px;
         font-size: 1.4em;
         border-bottom: 1px solid #b3e5fc; /* קו תחתון לכותרת משנה */
         padding-bottom: 5px;
     }

    #explanation p {
        margin-bottom: 15px;
         text-align: justify; /* יישור לשני הצדדים להסבר */
    }

    #explanation strong {
        color: #004d40; /* ירוק כהה להדגשות */
    }

     /* ריספונסיביות בסיסית */
     @media (max-width: 600px) {
         .controls {
             flex-direction: column;
             align-items: center;
         }
          .control-group {
              width: 100%;
              align-items: center;
          }
         .controls select, .sim-button {
             width: 90%; /* רוחב כמעט מלא לפקדים */
         }
     }

</style>

<button id="show-explanation-btn">גלשו לעומק: מה באמת גורם לסלעים לעמוד?</button>

<div id="explanation">
    <h2>פענוח סוד הסלעים המאוזנים: גאולוגיה בפעולה</h2>

    <h3>מבנים שוברי אינטואיציה: הפלא של סלעים מאוזנים</h3>
    סלעים מאוזנים, או Balanced Rocks, הם פסלים טבעיים מדהימים שנוצרו על ידי כוחות אדירים הפועלים במשך עידנים. אלו הן תצורות סלע בהן גוש סלע עליון, לרוב גדול וכבד, נח על בסיס תמיכה צר במיוחד. המראה הלא ייאמן הזה מעורר תמיהה - איך הם לא נופלים? הוא מדגים בצורה ויזואלית את העוצמה האיטית והמתמדת של תהליכים גאולוגיים המפסלים את פני האדמה.

    <h3>בלייה וארוזיה: צמד דינמי שמעצב נופים</h3>
    כדור הארץ נמצא בתנועה מתמדת, לא רק בלוחות טקטוניים, אלא גם ברמת פני השטח. שני התהליכים העיקריים האחראים לפיסול הנוף הם:
    *   **בלייה (Weathering):** תהליך כימי ופיזי שמפורר ומפורק את הסלע במקומו. זה יכול לקרות מחשיפה למים (המסת מינרלים), שינויי טמפרטורה (סדקים מקפיאה-הפשרה או התרחבות-התכווצות), רוח (סחיפת חלקיקים), ואף פעילות אורגניזמים (שורשים שחודרים לסדקים).
    *   **ארוזיה (Erosion):** תהליך הסחיפה וההובלה של חומרי הסלע המפורקים ממקומם על ידי גורמים ניידים כמו רוח, מים זורמים, קרחונים וכוח המשיכה.
    יחד, בלייה וארוזיה פועלים ללא הרף, שוחקים פסגות הרים, מעמיקים עמקים, ויוצרים את הצורות הייחודיות שאנו רואים בטבע, כולל את הסלעים המאוזנים.

    <h3>הקסם האמיתי: בלייה דיפרנציאלית (Differential Weathering)</h3>
    הסוד ליצירת סלע מאוזן טמון ב**בלייה דיפרנציאלית** – תהליך שבו אזורים שונים באותה תצורת סלע נשחקים ומתבלים בקצבים שונים. ההבדלים בקצב הבלייה יכולים לנבוע ממגוון גורמים:
    *   **הבדלים בהרכב הסלע:** סלע אינו תמיד אחיד. הוא עשוי להכיל שכבות או כיסים של מינרלים רכים יותר או קשים יותר, או להיות סדוק יותר באזורים מסוימים. אזורים חלשים יותר יתבלו מהר יותר.
    *   **חשיפה לגורמי בלייה:** בסיס סלע החשוף יותר לרוח נושאת חול, מים זורמים או שינויי טמפרטורה קיצוניים (כי הוא קרוב יותר לקרקע ופחות מוגן) יתבלה מהר יותר מחלקו העליון.
    *   **צורת הסלע והטופוגרפיה:** צורת הסלע הראשונית והסביבה בה הוא נמצא (למשל, אם מים נוטים להתאסף סביב בסיסו) משפיעים על מידת החשיפה של חלקים שונים לגורמי הבלייה.

    <h3>מפסלים את הצורה: כיצד זה מוביל לסלע מאוזן?</h3>
    רוב הסלעים המאוזנים החלו את דרכם כגושי סלע גדולים יותר, לעיתים קרובות חלק ממצוק או רמה. לאורך אלפי עד מיליוני שנים, גורמי הבלייה והארוזיה החלו לפעול עליהם. בגלל בלייה דיפרנציאלית, לרוב הבסיס של הסלע נשחק בקצב מהיר יותר מחלקו העליון. הרוח סוחפת חול שמכה בעוצמה בבסיס הקרוב לקרקע, המים מחלחלים וקופאים בסדקים תחתונים, ומינרלים נמסים מהחלקים התחתונים הפגיעים יותר. החלק העליון, לרוב גדול יותר, פחות חשוף או עשוי מחומר עמיד יותר, נשחק לאט יותר. התוצאה היא תהליך "פיסול" טבעי איטי ומתמשך, שבו הבסיס הולך ונעשה צר יותר ויותר, בעוד שהמסה העליונה נשמרת יחסית לגודלה המקורי. כך נוצר המראה הדרמטי של "סלע מאוזן".

    <h3>יציבות פלאית: איך הם לא נופלים?</h3>
    למרות המראה הלא יציב לכאורה, סלעים מאוזנים יציבים להפליא כל עוד מרכז הכובד של הגוש העליון נמצא בדיוק מעל נקודת התמיכה הצרה. הטבע "פיסל" אותם כך שהם נמצאים בשיווי משקל עדין. הם עומדים איתן נגד כוחות רגילים כמו רוח. רק כוחות חזקים במיוחד או אירועים קיצוניים (כמו רעידת אדמה חזקה, או המשך בלייה עד נקודת כשל קריטית) יכולים להפר את שיווי המשקל העדין ולגרום לקריסתם. למעשה, הסלעים המאוזנים שאנו רואים היום הם רק "רגע בזמן" בתהליך גאולוגי ארוך הכולל יצירה, פיסול, ובסופו של דבר - קריסה טבעית.

    <h3>סלעים מאוזנים מסביב לעולם: עדויות ויזואליות לתהליך</h3>
    ניתן למצוא סלעים מאוזנים מרהיבים במקומות רבים בעולם, במיוחד באזורים צחיחים או מדבריים בהם בלייה פיזית על ידי רוח ומים עונתית היא דומיננטית. פארק הארצ'ס הלאומי ביוטה, ארה"ב, הוא דוגמה מפורסמת, שם לצד קשתות טבעיות ישנן תצורות סלע מאוזנים רבות ומגוונות. כל אחד מהם מספר את סיפורו הייחודי של מיליוני שנות פיסול טבעי.
</div>

<script>
    const canvas = document.getElementById('rock-canvas');
    const ctx = canvas.getContext('2d');
    const rockTypeSelect = document.getElementById('rock-type');
    const weatheringSelect = document.getElementById('weathering-factors');
    const startButton = document.getElementById('start-sim');
    const resetButton = document.getElementById('reset-sim');
    const timeDisplay = document.getElementById('sim-time');
    const timelineProgress = document.querySelector('.timeline-progress');
    const simMessage = document.getElementById('sim-message');
    const showExplanationBtn = document.getElementById('show-explanation-btn');
    const explanationDiv = document.getElementById('explanation');

    let rockShape;
    let initialRockShape;
    let simTime = 0;
    let animationFrameId = null;
    const totalSimSteps = 600; // Represents thousands/millions of years
    const stepsPerFrame = 2; // How many simulation steps occur per animation frame (speed control)
    let isSimulating = false;

    // Particle system for erosion visualization
    let particles = [];
    const particleCountPerStep = 5;
    const particleMaxLife = 30; // frames
    const particleSize = 2; // pixels
    const particleColor = 'rgba(139, 69, 19, 0.8)'; // Semi-transparent brown

    function createParticle(x, y) {
        particles.push({
            x: x,
            y: y,
            vx: (Math.random() - 0.5) * 2, // velocity x
            vy: Math.random() * -2 - 1, // velocity y (mostly upwards)
            life: particleMaxLife,
            opacity: 1
        });
    }

    function updateParticles() {
        for (let i = particles.length - 1; i >= 0; i--) {
            const p = particles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.05; // Gravity effect
            p.life--;
            p.opacity = p.life / particleMaxLife;

            if (p.life <= 0) {
                particles.splice(i, 1);
            }
        }
    }

    function drawParticles() {
        particles.forEach(p => {
            ctx.fillStyle = particleColor;
            ctx.globalAlpha = p.opacity;
            ctx.beginPath();
            ctx.arc(p.x, p.y, particleSize, 0, Math.PI * 2);
            ctx.fill();
        });
        ctx.globalAlpha = 1; // Reset alpha
    }


    function initializeRock() {
         // Ensure canvas size is set before calculating dimensions
        const simArea = document.querySelector('.simulation-area');
        canvas.width = simArea.offsetWidth - 30; // Adjust for padding
        canvas.height = 350;

        const baseWidthRatio = 0.6;
        const topWidthRatio = 0.8;
        const totalHeightRatio = 0.8;
        const baseHeightRatio = 0.1; // Base height is part of total height calculation

        const totalHeight = canvas.height * totalHeightRatio;
        const baseHeight = canvas.height * baseHeightRatio;
        const topWidth = canvas.width * topWidthRatio;
        const baseWidth = canvas.width * baseWidthRatio;


        // Basic trapezoid shape (wider at top, narrower at base initially)
        // Points: 0=TL, 1=TR, 2=BR, 3=BL
         initialRockShape = [
            { x: (canvas.width - topWidth) / 2, y: canvas.height - totalHeight }, // Top Left
            { x: (canvas.width + topWidth) / 2, y: canvas.height - totalHeight }, // Top Right
            { x: (canvas.width + baseWidth) / 2, y: canvas.height - baseHeight }, // Bottom Right
            { x: (canvas.width - baseWidth) / 2, y: canvas.height - baseHeight }  // Bottom Left
        ];

        // Deep copy the initial shape for the simulation
        rockShape = JSON.parse(JSON.stringify(initialRockShape));

        simTime = 0;
        particles = []; // Clear particles
        updateTimeDisplay();
        updateSimMessage("בחרו הגדרות והתחילו בסימולציה");
        drawRock();
        updateTimelineProgress();
    }

    function drawRock() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw rock with a simple gradient for depth
        const gradient = ctx.createLinearGradient(0, rockShape[0].y, 0, rockShape[2].y);
        gradient.addColorStop(0, '#8B4513'); // Brown top
        gradient.addColorStop(1, '#A0522D'); // Sienna base
        ctx.fillStyle = gradient;

        ctx.beginPath();
        ctx.moveTo(rockShape[0].x, rockShape[0].y);
        for (let i = 1; i < rockShape.length; i++) {
            ctx.lineTo(rockShape[i].x, rockShape[i].y);
        }
        ctx.closePath();
        ctx.fill();

        // Add internal lines/texture for "layered" effect (optional - visual hint)
        if (rockTypeSelect.value === 'layered' && simTime > 50) { // Show lines only after some time
            ctx.strokeStyle = '#5a2d0c';
            ctx.lineWidth = 0.5;
            ctx.beginPath();
            const layerCount = 5;
            const rockHeight = rockShape[2].y - rockShape[0].y;
            for(let i = 1; i < layerCount; i++) {
                const y = rockShape[0].y + rockHeight * (i / layerCount);
                ctx.moveTo(rockShape[0].x + (rockShape[3].x - rockShape[0].x) * (i / layerCount), y);
                ctx.lineTo(rockShape[1].x + (rockShape[2].x - rockShape[1].x) * (i / layerCount), y);
            }
            ctx.stroke();
        }

        // Draw particles on top
        drawParticles();
    }

    function erodeRock() {
        const baseErosionRate = 0.15; // Base erosion rate per step
        const rockType = rockTypeSelect.value;
        const weatheringFactor = weatheringSelect.value;

        let currentBaseErosion = baseErosionRate; // Erosion affecting bottom points
        let currentMidErosion = 0; // Erosion affecting higher points (for layered)

        // Adjust erosion based on rock type and weathering factors
        let baseMultiplier = 1;
        let midMultiplier = 1;

        if (rockType === 'layered') {
             midMultiplier = 1.5; // Mid-section (simulated) erodes faster
        } else if (rockType === 'weak-base') {
             baseMultiplier = 2.5; // Very base erodes significantly faster
        }

         // Adjust erosion based on weathering factors
         if (weatheringFactor === 'wind') {
              baseMultiplier *= 1.5; // Wind hits base hard
              midMultiplier *= 1.1; // Some rounding higher up
         } else if (weatheringFactor === 'water') {
              baseMultiplier *= 1.8; // Water pools and erodes base/undercuts
         } else if (weatheringFactor === 'temp-changes') {
             baseMultiplier *= 1.3; // Cracks form and enlarge, especially at base
             midMultiplier *= 1.3; // Affects the whole rock slightly more
         } else if (weatheringFactor === 'all') {
             baseMultiplier *= 2;
             midMultiplier *= 1.5;
         }

        currentBaseErosion = baseErosionRate * baseMultiplier;
        currentMidErosion = baseErosionRate * midMultiplier;


        // Apply erosion to the shape points (simplified 2D model)
        // Points: 0=TL, 1=TR, 2=BR, 3=BL

        // Erode bottom points (3 and 2) inwards (x-axis) and slightly upwards (y-axis)
        // Ensure base doesn't get too narrow initially relative to its height
        const minBaseWidth = canvas.width * 0.1; // Avoid zero width base
        const baseWidth = rockShape[2].x - rockShape[3].x;

        if (baseWidth > minBaseWidth || currentBaseErosion < baseWidth / 2) {
             rockShape[3].x += currentBaseErosion;
             rockShape[2].x -= currentBaseErosion;
             // Simulate base getting shorter as it erodes upwards
             rockShape[3].y -= currentBaseErosion * 0.3;
             rockShape[2].y -= currentBaseErosion * 0.3;

             // Create particles from the eroding base
             for(let i=0; i < particleCountPerStep; i++) {
                 const erodeX = rockShape[3].x + (rockShape[2].x - rockShape[3].x) * Math.random();
                 const erodeY = rockShape[3].y;
                 createParticle(erodeX, erodeY);
             }

        } else {
            // Base is too narrow, cause collapse slightly faster
             rockShape[3].x += currentBaseErosion * 0.5; // Still erode, but less inwards
             rockShape[2].x -= currentBaseErosion * 0.5;
             rockShape[3].y += currentBaseErosion * 0.8; // Simulate crumbling downwards
             rockShape[2].y += currentBaseErosion * 0.8;
             // Create more particles on collapse
             for(let i=0; i < particleCountPerStep * 2; i++) {
                  const erodeX = rockShape[3].x + (rockShape[2].x - rockShape[3].x) * Math.random();
                  const erodeY = rockShape[3].y;
                  createParticle(erodeX, erodeY);
              }
        }


        // Simulate erosion affecting "mid-section" for layered rock by slightly moving
        // points 0 & 1 inwards relative to their height from base
         if (rockType === 'layered' && currentMidErosion > 0) {
             const erosionHeightFactor = (rockShape[2].y - rockShape[0].y) / (initialRockShape[2].y - initialRockShape[0].y); // How much vertical space is left
             const actualMidErosion = currentMidErosion * (1 - erosionHeightFactor * 0.5); // Erodes more higher up initially

             rockShape[0].x += actualMidErosion * 0.5; // Affect top corners slightly
             rockShape[1].x -= actualMidErosion * 0.5;

             // Simulate erosion from sides affecting points closer to base
             const sideErosion = currentMidErosion * 0.8; // Slightly less than direct base erosion
             // Affect points 3 and 2's x coordinates slightly more based on mid erosion
             rockShape[3].x += sideErosion * 0.2;
             rockShape[2].x -= sideErosion * 0.2;

              // Create particles from sides and mid-sections
              for(let i=0; i < particleCountPerStep * 0.5; i++) {
                   // Left side
                   const erodeX_L = rockShape[0].x + (rockShape[3].x - rockShape[0].x) * Math.random();
                   const erodeY_L = rockShape[0].y + (rockShape[3].y - rockShape[0].y) * Math.random();
                   createParticle(erodeX_L, erodeY_L);
                   // Right side
                    const erodeX_R = rockShape[1].x + (rockShape[2].x - rockShape[1].x) * Math.random();
                    const erodeY_R = rockShape[1].y + (rockShape[2].y - rockShape[1].y) * Math.random();
                   createParticle(erodeX_R, erodeY_R);
               }
         }


        // Check for collapse (base points cross or base becomes too narrow/low)
        const stabilityThreshold = canvas.width * 0.03; // Base minimum width
        const minRockHeight = canvas.height * 0.2; // Prevent rock from disappearing entirely

        if (rockShape[3].x >= rockShape[2].x - stabilityThreshold || (rockShape[3].y > canvas.height - 5) || (rockShape[0].y > canvas.height - minRockHeight)) {
            stopSimulation();
            updateSimMessage("הסימולציה הסתיימה: הסלע קרס!");
            // Optional: Draw broken pieces animation (more complex)
             ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear rock
             // Draw a pile of debris (simplified)
             ctx.fillStyle = '#a0522d'; // Sienna color
             ctx.beginPath();
             const debrisHeight = canvas.height * 0.05;
             const debrisWidth = canvas.width * 0.5;
             ctx.rect((canvas.width - debrisWidth) / 2, canvas.height - debrisHeight, debrisWidth, debrisHeight);
             ctx.fill();

            return false; // Indicate collapse
        }


        return true; // Indicate simulation continues
    }

    function updateTimeDisplay() {
        const percentage = (simTime / totalSimSteps) * 100;
        timeDisplay.textContent = `זמן גאולוגי שעבר: ${percentage.toFixed(0)}%`;
    }

    function updateTimelineProgress() {
         const percentage = (simTime / totalSimSteps) * 100;
         timelineProgress.style.width = `${percentage}%`;
    }

    function updateSimMessage(message) {
        simMessage.textContent = message;
    }

    function gameLoop() {
        if (simTime < totalSimSteps) {
            let collapsed = false;
            // Advance simulation multiple steps per frame for speed
            for(let i = 0; i < stepsPerFrame; i++) {
                 if (!erodeRock()) { // If collapse occurs during any step
                     collapsed = true;
                     break; // Stop processing steps for this frame
                 }
                 simTime++;
                 if (simTime >= totalSimSteps) break;
            }


            updateParticles(); // Update particle positions
            drawRock(); // Draw rock AND particles
            updateTimeDisplay();
            updateTimelineProgress();


            if (!collapsed && simTime < totalSimSteps) {
                 animationFrameId = requestAnimationFrame(gameLoop);
            } else if (!collapsed && simTime >= totalSimSteps) {
                 stopSimulation();
                 updateSimMessage("הסימולציה הסתיימה בהצלחה: נוצר סלע מאוזן!");
            }

        } else {
            stopSimulation();
            updateSimMessage("הסימולציה הסתיימה בהצלחה: נוצר סלע מאוזן!");
        }
    }

    function startSimulation() {
        if (!isSimulating) { // Prevent multiple starts
             isSimulating = true;
            initializeRock(); // Reset before starting
            updateSimMessage("הסימולציה רצה...");
            gameLoop();
        }
    }

    function stopSimulation() {
        if (animationFrameId !== null) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
             isSimulating = false;
        }
    }

    function resetSimulation() {
        stopSimulation();
        initializeRock();
         updateSimMessage("הסימולציה אופסה. בחרו הגדרות חדשות.");
    }

    // Event Listeners
    startButton.addEventListener('click', startSimulation);
    resetButton.addEventListener('click', resetSimulation);

    showExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        showExplanationBtn.textContent = isHidden ? 'הסתירו את ההסבר' : 'גלשו לעומק: מה באמת גורם לסלעים לעמוד?';
    });

    // Initial setup
    initializeRock();

    // Resize canvas and re-initialize rock if window is resized (Debounced is better for performance)
     let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (!isSimulating) { // Only reset if not currently simulating
                 initializeRock();
            } else {
                // If simulating, just resize canvas and redraw current state
                 const simArea = document.querySelector('.simulation-area');
                 canvas.width = simArea.offsetWidth - 30;
                 canvas.height = 350;
                 drawRock(); // Redraw the rock at its current shape
            }
        }, 250); // Wait 250ms after resize finishes
    });

     // Initial canvas size setup
    const simArea = document.querySelector('.simulation-area');
    canvas.width = simArea.offsetWidth - 30;
    canvas.height = 350;


</script>
```