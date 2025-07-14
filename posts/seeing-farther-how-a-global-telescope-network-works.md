---
title: "העין הגדולה ביותר: איך רשת טלסקופים עולמית חושפת את סודות היקום?"
english_slug: seeing-farther-how-a-global-telescope-network-works
category: "פיזיקה"
tags:
- אסטרונומיה
- טלסקופים
- אינטרפרומטריה
- רזולוציה
- EHT
---
# העין הגדולה ביותר: איך רשת טלסקופים עולמית חושפת את סודות היקום?

הטלסקופים הבודדים הגדולים בעולם מגיעים לקוטר של עשרות מטרים, אבל יש גבול לגודל הפיזי שניתן לבנות. אז איך מצליחים אסטרונומים להשיג את הרזולוציה הגבוהה ביותר שאי פעם הושגה, כדי "לצלם" עצמים זעירים על השמיים (מנקודת מבטנו) כמו חורים שחורים עצומי-מסה במרחק מיליוני שנות אור? התשובה טמונה בטכנולוגיה גאונית בשם אינטרפרומטריה. בואו נחקור איך זה עובד!

<div class="app-container">
    <div class="app-description">
        <h3>בנה את "העין הגדולה ביותר"</h3>
        <p>כדי לשפר את יכולת ההפרדה (רזולוציה) של הרשת, עליך להציב טלסקופים. המרחק בין הטלסקופים הוא המפתח!</p>
         <p>לחץ בכל מקום על המפה כדי להוסיף טלסקופ, או גרור טלסקופ קיים למיקום חדש. לחץ לחיצה כפולה על טלסקופ כדי להסירו.</p>
        <div class="controls">
            <button id="add-telescope-btn">✨ הוסף טלסקופ</button>
            <button id="reset-telescopes-btn">🗑️ נקה רשת</button>
        </div>
        <div class="info">
            <p>מספר טלסקופים ברשת: <span id="num-telescopes">0</span></p>
            <p>הבסיס המקסימלי (המרחק הגדול ביותר בין 2 טלסקופים): <span id="max-baseline">0</span> יחידות</p>
        </div>
    </div>
    <div class="simulation-area">
        <div class="map-area" id="map-area">
            <!-- Telescopes and baselines will be drawn here -->
            <canvas id="baseline-canvas"></canvas>
             <div class="map-overlay">לחץ כאן להוספת טלסקופ ראשון</div>
        </div>
        <div class="image-area">
            <h4>התמונה ש'רואה' הרשת</h4>
            <img id="result-image" src="https://via.placeholder.com/300x300?text=%D7%94%D7%95%D7%A1%D7%A3+%D7%98%D7%9C%D7%A1%D7%A7%D7%95%D7%A4%D7%99%D7%9D+%D7%95%D7%AA%D7%A8%D7%90%D7%94+%D7%AA%D7%95%D7%A6%D7%90%D7%94" alt="Resulting image from telescope network">
            <div class="resolution-level">רמת רזולוציה: <span id="resolution-level">0</span>/3</div>
        </div>
    </div>
</div>

<style>
:root {
    --bg-color: #1a1a2e; /* Dark background */
    --card-color: #16213e; /* Slightly lighter card background */
    --text-color: #e94560; /* Accent color for text/highlights */
    --secondary-text-color: #c1c1c1; /* Lighter text */
    --border-color: #0f3460; /* Border color */
    --button-bg: #e94560; /* Button background */
    --button-text: #1a1a2e; /* Button text color */
    --button-hover-bg: #ff6d80; /* Button hover color */
    --telescope-color: #0f3460; /* Telescope dot color */
    --baseline-color: rgba(233, 69, 96, 0.7); /* Baseline line color with opacity */
    --max-baseline-color: #ffef00; /* Highlight for max baseline */
    --overlay-color: rgba(22, 33, 62, 0.9); /* Overlay for map */
}

body {
    font-family: 'Arial Hebrew', sans-serif;
    background-color: var(--bg-color);
    color: var(--secondary-text-color);
    line-height: 1.6;
    padding: 20px;
    direction: rtl;
}

h1, h3, h4 {
    color: var(--text-color);
}

.app-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-top: 30px;
    border: 1px solid var(--border-color);
    padding: 25px;
    border-radius: 12px;
    background-color: var(--card-color);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.app-description {
    flex: 1;
    min-width: 280px;
}

.app-description p {
    margin-bottom: 15px;
    font-size: 1.1em;
}

.simulation-area {
    flex: 2;
    min-width: 350px;
    display: flex;
    flex-direction: column;
    gap: 25px;
    align-items: center;
}

.map-area {
    position: relative;
    width: 100%;
    max-width: 500px; /* Limit max width for map */
    height: 350px; /* Adjust height */
    border: 2px dashed var(--border-color); /* Dashed border suggests the "effective" area */
    background-color: var(--bg-color);
    cursor: crosshair;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

#baseline-canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 5; /* Below the dots */
    pointer-events: none; /* Clicks go through to map-area */
}


.map-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--overlay-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.4em;
    color: var(--secondary-text-color);
    pointer-events: none;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
    transition: opacity 0.5s ease;
    z-index: 15; /* Above canvas */
}

.map-overlay.hidden {
    opacity: 0;
}


.telescope-dot {
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: var(--telescope-color);
    border: 3px solid var(--text-color);
    border-radius: 50%;
    cursor: grab;
    transform: translate(-50%, -50%); /* Center the dot */
    z-index: 10;
    transition: background-color 0.2s ease, border-color 0.2s ease, transform 0.1s ease;
}

.telescope-dot:hover {
    background-color: var(--text-color);
    border-color: var(--secondary-text-color);
    transform: translate(-50%, -50%) scale(1.1); /* Slight scale on hover */
}

.telescope-dot:active {
    cursor: grabbing;
    background-color: var(--button-bg);
    border-color: var(--button-text);
    transform: translate(-50%, -50%) scale(1.2); /* Larger scale when dragging */
    box-shadow: 0 0 15px rgba(233, 69, 96, 0.7); /* Glow effect */
}

.image-area {
    width: 100%;
    max-width: 300px; /* Control image size */
    text-align: center;
    background-color: var(--bg-color);
    padding: 15px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

#result-image {
    width: 100%;
    height: auto;
    border: 1px solid var(--border-color);
    display: block;
    margin: 0 auto 15px auto;
    border-radius: 4px;
     transition: opacity 0.5s ease; /* Smooth image change */
}

.controls {
    margin-bottom: 20px;
    display: flex;
    gap: 15px;
    flex-wrap: wrap; /* Allow buttons to wrap on small screens */
}

.controls button, #show-explanation-btn {
    padding: 12px 20px;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: var(--button-bg);
    color: var(--button-text);
    font-size: 1em;
    font-weight: bold;
    transition: background-color 0.2s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.controls button:hover, #show-explanation-btn:hover {
    background-color: var(--button-hover-bg);
    transform: translateY(-2px); /* Lift effect on hover */
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.4);
}

.controls button:active, #show-explanation-btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.info, .resolution-level {
    font-size: 1em;
    color: var(--secondary-text-color);
    margin-bottom: 10px;
}

.info span, .resolution-level span {
     color: var(--text-color);
     font-weight: bold;
}


#show-explanation-btn {
    display: block;
    width: fit-content;
    margin: 30px auto;
}


#explanation-area {
    margin-top: 30px;
    padding: 25px;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background-color: var(--card-color);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
     /* Add animation for display toggle */
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    transition: opacity 0.5s ease-out, max-height 0.7s ease-out;
}

#explanation-area.visible {
    opacity: 1;
    max-height: 2000px; /* Sufficiently large value */
}


#explanation-area h3 {
    margin-top: 0;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
    margin-bottom: 20px;
    color: var(--text-color);
}

#explanation-area p {
    margin-bottom: 15px;
    color: var(--secondary-text-color);
}

#explanation-area ul {
    list-style-type: disc;
    margin-right: 25px; /* For RTL */
    padding-right: 0;
    color: var(--secondary-text-color);
}

#explanation-area li {
    margin-bottom: 8px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .app-container {
        flex-direction: column;
    }
    .app-description, .simulation-area {
        min-width: 100%;
    }
    .simulation-area {
        order: -1; /* Simulation first on small screens */
    }
     .map-area {
        height: 300px;
    }
    .controls {
        flex-direction: column;
        gap: 10px;
    }
     .controls button, #show-explanation-btn {
        width: 100%;
        text-align: center;
    }
}

</style>

<button id="show-explanation-btn">הצג הסבר מורחב 📖</button>

<div id="explanation-area">
    <h3>איך "העין הגדולה ביותר" עובדת? (אינטרפרומטריה אסטרונומית)</h3>

    <p>דמיין שאתה מנסה לקרוא טקסט קטן במיוחד הנמצא במרחק עצום. ככל שעדשת המצלמה או העין שלך גדולה יותר, כך תוכל להבחין בפרטים קטנים יותר ולהגיע לרזולוציה (יכולת הפרדה) גבוהה יותר. באסטרונומיה, כדי לראות עצמים רחוקים כמו כוכבים או גלקסיות בחדות מקסימלית, טלסקופים צריכים להיות גדולים ככל האפשר.</p>

    <ul>
        <li><strong>האתגר: גודל מוגבל ויכולת הפרדה (רזולוציה):</strong> היכולת של טלסקופ להבחין בין שתי נקודות קרובות בשמיים מוגבלת על ידי תופעת הדיפרקציה (עקיפה) של גלי האור/רדיו. כאשר אור עובר דרך פתח (הקוטר של צלחת הטלסקופ - האפרטורה), הוא מתפזר מעט. כתוצאה מכך, נקודה בשמיים אינה נראית כנקודה חדה, אלא כדיסקה מטושטשת. ככל שקוטר הצלחת גדול יותר, הדיסקה הזו קטנה יותר והרזולוציה גבוהה יותר. אבל... בניית צלחת טלסקופ בקוטר של קילומטרים או עשרות קילומטרים היא פשוט בלתי אפשרית פיזית וכלכלית.</li>
        <li><strong>הפתרון: אינטרפרומטריה!</strong> במקום טלסקופ יחיד ענק, אסטרונומים משתמשים ברשת של טלסקופים קטנים יותר המפוזרים על שטח גדול. הטכניקה הזו נקראת אינטרפרומטריה אסטרונומית. הרעיון הוא לאסוף את האור (או גלי הרדיו) באמצעות מספר "עיניים" קטנות במקומות שונים, ולשלב את המידע החכם הזה.</li>
        <li><strong>איך משלבים את האותות? הקלטה מדויקת ועיבוד חישובי:</strong> כל טלסקופ ברשת קולט את גל האור/רדיו ומתעד אותו במדויק, כולל מידע על זמן ההגעה וה"פאזה" של הגל (היכן הוא נמצא במחזור התנודה שלו). המידע הזה נרשם עם חותמת זמן מדויקת להפליא (דורש שעונים אטומיים!) ונשלח למרכז עיבוד נתונים. שם, מחשבי-על משלבים את כל הנתונים מכל הטלסקופים. הם עושים זאת בצורה כזו שזה מדמה קליטה של אות על ידי טלסקופ דמיוני שגודלו כגודל השטח המכוסה על ידי כל הרשת!</li>
        <li><strong>"האפרטורה האפקטיבית" והבייסליין:</strong> רשת הטלסקופים אינה אוספת *כמות* אור כמו טלסקופ ענק באותו קוטר (היא אוספת רק את כמות האור שנקלטת על ידי צלחות הטלסקופים הבודדים יחד), אבל היא משיגה את אותה *יכולת הפרדה*! הרזולוציה של רשת אינטרפרומטרית נקבעת לא על פי גודל הטלסקופים הבודדים, אלא על פי המרחק המקסימלי בין כל שני טלסקופים ברשת. מרחק זה נקרא 'בייסליין'. ככל שהבייסליין גדול יותר, כך הרזולוציה גבוהה יותר – כאילו היה לנו טלסקופ ענק בגודל הבייסליין הזה! הנוסחה הבסיסית לרזולוציה (θ) היא בערך λ/D, כאשר λ הוא אורך הגל ו-D הוא קוטר הטלסקופ. ברשת, D מוחלף ב-B, הבייסליין המקסימלי: θ ≈ λ/B.</li>
        <li><strong>רשתות ענק ברחבי העולם:</strong> רשתות כמו VLBI (Very Long Baseline Interferometry) וה-EHT (Event Horizon Telescope) משתמשות בטלסקופים הממוקמים ביבשות שונות, במרחק של אלפי קילומטרים זה מזה. זה מאפשר להן להשיג בייסליין אפקטיבי בגודל כמעט כדור הארץ כולו! התוצאה? רזולוציה מדהימה, גבוהה פי מיליוני מונים מזו של טלסקופ אופטי רגיל!</li>
        <li><strong>אתגרים וניצחונות טכנולוגיים:</strong> בניית ותפעול רשת כזו דורשת התגברות על אתגרים עצומים: סינכרון שעונים בדיוק ננו-שנייה, טיפול בכמויות מידע אדירות (פטה-בייט של נתונים נאספים בלילה אחד!), ופיתוח אלגוריתמים סבוכים לשילוב וניתוח הנתונים ליצירת תמונה. למרות הקשיים, ההישגים מדהימים – המפורסם ביותר הוא צילום "הצל" והטבעת הבוהקת סביב חורים שחורים סופר-מאסיביים בליבת גלקסיות שונות, הישג פורץ דרך שהיה בלתי אפשרי ללא אינטרפרומטריה עולמית.</li>
        <li><strong>מעבר לתמונות:</strong> אינטרפרומטריה מאפשרת לא רק ליצור תמונות מפורטות, אלא גם למדוד תכונות נוספות של מקורות קרינה, כמו תנועות זעירות, שינויים בזמן, ואפילו הרכב כימי, ובכך לחשוף עוד ועוד סודות על הפיזיקה הקיצונית ביקום.</li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const mapArea = document.getElementById('map-area');
    const canvas = document.getElementById('baseline-canvas');
    const ctx = canvas.getContext('2d');
    const addTelescopeBtn = document.getElementById('add-telescope-btn');
    const resetTelescopesBtn = document.getElementById('reset-telescopes-btn');
    const numTelescopesSpan = document.getElementById('num-telescopes');
    const maxBaselineSpan = document.getElementById('max-baseline');
    const resultImage = document.getElementById('result-image');
    const resolutionLevelSpan = document.getElementById('resolution-level');
    const mapOverlay = mapArea.querySelector('.map-overlay');

    const showExplanationBtn = document.getElementById('show-explanation-btn');
    const explanationArea = document.getElementById('explanation-area');

    let telescopes = []; // Array to store {x, y, element} for telescope centers relative to map top-left
    let isDragging = false;
    let draggedTelescopeIndex = -1;
    let dragOffsetX, dragOffsetY; // Offset from the element's center to the mouse click point

    // Image levels for demonstration (simulating increasing sharpness)
    // Using placeholder URLs with text to convey resolution increase
    const imageLevels = [
        'https://via.placeholder.com/300x300/1a1a2e/e94560?text=%D7%94%D7%95%D7%A1%D7%A3+%D7%98%D7%9C%D7%A1%D7%A7%D7%95%D7%A4%D7%99%D7%9D+%D7%95%D7%AA%D7%A8%D7%90%D7%94+%D7%AA%D7%95%D7%A6%D7%90%D7%94', // Level 0
        'https://via.placeholder.com/300x300/1a1a2e/e94560?text=%D7%A8%D7%96%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94+%D7%A0%D7%9E%D7%95%D7%9B%D7%94+%7C+%D7%9E%D7%98%D7%95%D7%A9%D7%98%D7%A9%D7%AA', // Level 1 (2+ telescopes, small baseline)
        'https://via.placeholder.com/300x300/1a1a2e/e94560?text=%D7%A8%D7%96%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94+%D7%91%D7%99%D7%A0%D7%95%D7%A0%D7%99%D7%AA+%7C+%D7%A4%D7%A8%D7%98%D7%99%D7%9D+%D7%9E%D7%AA%D7%97%D7%99%D7%9C%D7%99%D7%9D+%D7%9C%D7%94%D7%95%D7%A4%D7%99%D7%A2', // Level 2 (medium baseline)
        'https://via.placeholder.com/300x300/1a1a2e/ffef00?text=%D7%A8%D7%96%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94+%D7%92%D7%91%D7%95%D7%94!+%7C+%D7%AA%D7%9E%D7%95%D7%A0%D7%94+%D7%97%D7%93%D7%94+%F0%9F%9A%80' // Level 3 (large baseline)
    ];

    // Thresholds for switching image levels based on max baseline (in pixels)
    const baselineThresholds = [
        mapArea.offsetHeight * 0.2, // 20% of map height/width (approx)
        mapArea.offsetHeight * 0.5, // 50%
        mapArea.offsetHeight * 0.9  // 90%
    ];

    // Resize canvas to match mapArea
    function resizeCanvas() {
        const rect = mapArea.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;
        // Redraw everything after resize
        updateSimulation();
    }

    // Draw baseline lines between telescopes
    function drawBaselines() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous drawings

        if (telescopes.length < 2) {
            return; // Need at least two telescopes for a baseline
        }

        let maxDist = 0;
        let maxPair = null;

        // Find max baseline
        for (let i = 0; i < telescopes.length; i++) {
            for (let j = i + 1; j < telescopes.length; j++) {
                const dx = telescopes[i].x - telescopes[j].x;
                const dy = telescopes[i].y - telescopes[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist > maxDist) {
                    maxDist = dist;
                    maxPair = [telescopes[i], telescopes[j]];
                }
            }
        }

        // Draw all baselines (lighter color)
        ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--baseline-color').trim();
        ctx.lineWidth = 1.5;
        for (let i = 0; i < telescopes.length; i++) {
            for (let j = i + 1; j < telescopes.length; j++) {
                ctx.beginPath();
                ctx.moveTo(telescopes[i].x, telescopes[i].y);
                ctx.lineTo(telescopes[j].x, telescopes[j].y);
                ctx.stroke();
            }
        }

        // Draw the max baseline (highlighted color)
        if (maxPair) {
             ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--max-baseline-color').trim();
             ctx.lineWidth = 3;
             ctx.beginPath();
             ctx.moveTo(maxPair[0].x, maxPair[0].y);
             ctx.lineTo(maxPair[1].x, maxPair[1].y);
             ctx.stroke();
        }
    }


    function addTelescope(x, y) { // x, y are desired center coordinates relative to map top-left
        if (telescopes.length >= 10) { // Limit number of telescopes for performance/clarity
            // alert("מספר הטלסקופים המקסימלי (10) הושג."); // Maybe better UI feedback?
            return;
        }

        const dot = document.createElement('div');
        dot.classList.add('telescope-dot');
        // Set left/top to the desired center coordinates. CSS transform centers the dot based on these.
        dot.style.left = `${x}px`;
        dot.style.top = `${y}px`;
        mapArea.appendChild(dot);

        const newTelescope = { x: x, y: y, element: dot };
        telescopes.push(newTelescope);
        const index = telescopes.length - 1;

        updateSimulation();

        // Make the dot draggable
        makeDraggable(dot, index);
        // Add remove on dblclick
        addRemoveListener(dot, index);

        // Add subtle creation animation
        dot.style.opacity = 0;
        dot.style.transform = 'translate(-50%, -50%) scale(0.5)';
        setTimeout(() => {
            dot.style.transition = 'opacity 0.3s ease, transform 0.3s ease, background-color 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease';
            dot.style.opacity = 1;
            dot.style.transform = 'translate(-50%, -50%) scale(1)';
        }, 10); // Small delay to allow css transition
    }

     function removeTelescope(index) {
        if (index === -1 || index >= telescopes.length) return;

        const tel = telescopes[index];
        tel.element.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        tel.element.style.opacity = 0;
        tel.element.style.transform = 'translate(-50%, -50%) scale(0.5)';

        tel.element.addEventListener('transitionend', () => {
             if (tel.element.parentNode) {
                tel.element.parentNode.removeChild(tel.element);
            }
        });


        telesc.splice(index, 1); // Remove from array
        // Need to re-index draggable/remove listeners? No, better to just remove and let new ones be added if needed, or manage indices carefully.
        // Re-assign listeners isn't practical. The current setup relies on the index at creation.
        // A better approach for drag/remove with splice would be to use the element itself or a unique ID rather than array index.
        // Let's simplify: when removing, update simulation. Drag/remove will work for remaining items as their listeners don't rely on static indices.
         // For simplicity in this context, removing just needs to update the simulation display.
         // The drag/dblclick handlers attached to the *elements* will still work for the elements that remain.
         // If an element is removed, its handler won't fire again. This approach is okay given the scope.


        // Need to update indices for remaining elements if we were relying on index-based lookups in drag/remove, but currently not.
        // The makeDraggable and addRemoveListener use the index *at the time of creation*. If we remove an element, subsequent indices shift.
        // This is a limitation of using array index. Using a unique ID would be more robust.
        // For this simulation, with limited telescopes and likely no complex drag interactions happening concurrently with removal, the current simple splice+update should be acceptable visually. If needed, I'd refactor to use element references or unique IDs.
        // Let's re-implement drag/remove using element reference lookup in the array instead of index.

        updateSimulation();
    }

     // Refactored drag listener logic to not rely on index
     function makeDraggable(element) {
        let isDragging = false;
        let offsetX, offsetY; // Offset from the element's center to the mouse click point

        element.addEventListener('mousedown', (e) => {
            // Find the index of the element in the current telescopes array
            const index = telescopes.findIndex(tel => tel.element === element);
            if (index === -1) return; // Should not happen

            isDragging = true;
            draggedTelescopeIndex = index; // Store index of the currently dragged element
            const rect = element.getBoundingClientRect();
            // Calculate offset from the center of the dot to the mouse click point
            offsetX = e.clientX - (rect.left + rect.width / 2);
            offsetY = e.clientY - (rect.top + rect.height / 2);

            element.style.cursor = 'grabbing';
            element.style.zIndex = 30; // Bring dragged element to front
            e.stopPropagation(); // Prevent map click event from adding a new telescope
        });

         element.ondragstart = function() { return false; }; // Prevent default drag behavior
    }

    // Refactored remove listener logic to not rely on index
     function addRemoveListener(element) {
         element.addEventListener('dblclick', (e) => {
            // Find the index of the element in the current telescopes array
            const index = telescopes.findIndex(tel => tel.element === element);
            if (index !== -1) {
                removeTelescope(index);
            }
             e.stopPropagation(); // Prevent map click event
         });
     }


    // Global mousemove and mouseup listeners for dragging
    document.addEventListener('mousemove', (e) => {
        if (!isDragging || draggedTelescopeIndex === -1) return;

        const mapRect = mapArea.getBoundingClientRect();
        const element = telescopes[draggedTelescopeIndex].element;

        // Calculate the desired center position of the dot relative to the map's top-left
        let newCenterX = e.clientX - mapRect.left - offsetX;
        let newCenterY = e.clientY - mapRect.top - offsetY;

        const dotHalfWidth = element.offsetWidth / 2;
        const dotHalfHeight = element.offsetHeight / 2;

        // Clamp the center position to keep the whole dot within map boundaries
        const clampedCenterX = Math.max(dotHalfWidth, Math.min(newCenterX, mapRect.width - dotHalfWidth));
        const clampedCenterY = Math.max(dotHalfHeight, Math.min(newCenterY, mapRect.height - dotHalfHeight));

        // Apply the clamped center position
        element.style.left = `${clampedCenterX}px`;
        element.style.top = `${clampedCenterY}px`;

        // Store the clamped center coordinates
        telescopes[draggedTelescopeIndex].x = clampedCenterX;
        telescopes[draggedTelescopeIndex].y = clampedCenterY;

        // Update simulation display in real-time during drag
        updateSimulation();
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            if (draggedTelescopeIndex !== -1) {
                const element = telescopes[draggedTelescopeIndex].element;
                element.style.cursor = 'grab';
                element.style.zIndex = 10; // Reset z-index
                 // Ensure final update happens
                updateSimulation();
            }
            draggedTelescopeIndex = -1;
        }
    });


    function calculateMaxBaseline() {
        let maxDist = 0;
        if (telescopes.length < 2) {
            return 0;
        }
        for (let i = 0; i < telescopes.length; i++) {
            for (let j = i + 1; j < telescopes.length; j++) {
                // Use stored coordinates which are the center position relative to map's top-left
                const dx = telescopes[i].x - telescopes[j].x;
                const dy = telescopes[i].y - telescopes[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist > maxDist) {
                    maxDist = dist;
                }
            }
        }
        return maxDist;
    }

    function updateSimulation() {
        const num = telescopes.length;
        numTelescopesSpan.textContent = num;

        // Hide overlay when there are telescopes
        if (num > 0) {
             mapOverlay.classList.add('hidden');
        } else {
             mapOverlay.classList.remove('hidden');
        }

        const maxBaseline = calculateMaxBaseline(); // Always calculate max baseline
        maxBaselineSpan.textContent = maxBaseline.toFixed(1);

        drawBaselines(); // Redraw baselines

        let resolutionLevel = 0; // Default to Level 0

        if (num >= 2) { // If we have at least 2 telescopes, we can calculate resolution based on baseline
             if (maxBaseline > baselineThresholds[2]) {
                 resolutionLevel = 3; // Sharpest
             } else if (maxBaseline > baselineThresholds[1]) {
                 resolutionLevel = 2; // Less Blurred
             } else if (maxBaseline > baselineThresholds[0]) {
                 resolutionLevel = 1; // Blurred
             } else {
                 // Baseline > 0 but <= threshold[0], and num >= 2
                 resolutionLevel = 1; // Show at least the first blurred image
             }
        }
        // If num < 2, resolutionLevel remains 0.

        // Update image only if level changes to avoid unnecessary reloads
        if (resultImage.src !== imageLevels[resolutionLevel]) {
            resultImage.style.opacity = 0.5; // Start fade out
             // Use a small timeout before changing src to allow fade out to start
            setTimeout(() => {
                resultImage.src = imageLevels[resolutionLevel];
                 // Add load listener to fade in image once loaded
                resultImage.onload = () => {
                    resultImage.style.opacity = 1;
                };
                // Handle potential error if image doesn't load (e.g., broken placeholder URL)
                resultImage.onerror = () => {
                     resultImage.style.opacity = 1; // Still fade in even on error
                     console.error("Failed to load image for resolution level", resolutionLevel);
                };
            }, 100); // Small delay
        }


        resolutionLevelSpan.textContent = resolutionLevel;
    }

    function resetSimulation() {
        // Remove all telescope elements from the DOM
        telescopes.forEach(tel => tel.element.remove());
        telesc = []; // Clear the array
        updateSimulation(); // Update display and redraw canvas
         // Initial state update will set the image to level 0 which is the "Add Telescopes" image
    }

    // Event Listeners
    mapArea.addEventListener('click', (e) => {
        // Ensure it's a left click and not a drag (check if a telescope is being dragged)
        if (e.button === 0 && !isDragging) {
             // Calculate click position relative to mapArea. This will be the desired center.
            const rect = mapArea.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Add telescope at the clicked position
            addTelescope(x, y);
        }
    });


    addTelescopeBtn.addEventListener('click', () => {
         // Add a telescope at a random position when the button is clicked
         const mapRect = mapArea.getBoundingClientRect();
         const dotSize = 20; // As defined in CSS telescope-dot width/height
         // Calculate random coordinates for the center of the dot, staying within bounds
         // Ensure random position is at least dotSize/2 away from edges
         const randomCenterX = Math.random() * (mapRect.width - dotSize) + dotSize / 2;
         const randomCenterY = Math.random() * (mapRect.height - dotSize) + dotSize / 2;
         addTelescope(randomCenterX, randomCenterY); // These are the desired center coordinates
    });


    resetTelescopesBtn.addEventListener('click', resetSimulation);


    // Explanation button logic
    showExplanationBtn.addEventListener('click', () => {
        const isVisible = explanationArea.classList.contains('visible');
        if (isVisible) {
            explanationArea.classList.remove('visible');
            showExplanationBtn.textContent = 'הצג הסבר מורחב 📖';
        } else {
            explanationArea.classList.add('visible');
            showExplanationBtn.textContent = 'הסתר הסבר 📕';
        }
    });

    // Initialize canvas size and simulation state
    resizeCanvas();
    updateSimulation();

    // Listen for window resize to adjust canvas and redraw
    window.addEventListener('resize', resizeCanvas);

});
</script>
```