---
title: "המסע הסטטיסטי: גילוי חוק המספרים הגדולים בקוביית המזל הווירטואלית"
english_slug: statistical-magic-law-of-large-numbers-virtual-dice
category: "מתמטיקה"
tags: [Probability, Statistics, Law of Large Numbers, Simulation, Dice]
---
# המסע הסטטיסטי: גילוי חוק המספרים הגדולים בקוביית המזל הווירטואלית

מה קורה כשמטילים קובייה הוגנת? התוצאה של הטלה בודדת היא הפתעה מוחלטת – כל מספר מ-1 עד 6 יכול להופיע. אבל האם באמת הכל אקראי? הצטרפו אלינו למסע מרתק אל עולם ההסתברות, וגלו איך מתוך כאוס לכאורה, צומחת חוקיות מדהימה כשאנחנו חוזרים על הפעולה שוב ושוב, אלפי ואף רבבות פעמים!

<div class="simulation-container">
    <h2>המגרש הווירטואלי שלכם</h2>
    <div class="dice-display">
        <span id="diceVisual" class="dice-icon">-</span>
    </div>
    <div class="stats">
        <p><strong>תוצאת ההטלה האחרונה:</strong> <span id="lastRoll">-</span></p>
        <p><strong>סה"כ הטלות:</strong> <span id="totalRolls">0</span></p>
        <p><strong>ממוצע מצטבר:</strong> <span id="average">-</span></p>
    </div>
     <div class="graph-container">
        <canvas id="averageGraph"></canvas>
    </div>
    <div class="controls">
        <button id="rollOneBtn">הטל קובייה (x1)</button>
        <button id="roll100Btn">הטל 100 פעמים</button>
        <button id="roll1000Btn">הטל 1000 פעמים</button>
        <button id="roll10000Btn">הטל 10000 פעמים</button>
        <button id="resetBtn" class="secondary">התחילו מחדש</button>
    </div>

</div>

<button id="toggleExplanationBtn" class="explanation-toggle">סקרנים? גלו את הסוד מאחורי הקסם</button>

<div id="explanation" class="hidden-explanation">
    <h2>הסבר: חוק המספרים הגדולים נחשף!</h2>

    <h3>הסתברות ואירועים אקראיים: משחקי מזל ומדע</h3>
    <p>הסתברות היא הכלי המרכזי שלנו להבנת אירועים שהתוצאה שלהם אינה ידועה מראש. מה הסיכוי שיצא 6 בהטלת קובייה? מה הסיכוי לזכות בלוטו? אלו שאלות הסתברותיות. קובייה הוגנת היא הדוגמה הקלאסית לאירוע אקראי "סימטרי", שבו לכל תוצאה (1, 2, 3, 4, 5, 6) יש סיכוי זהה לחלוטין להתרחש – 1 מתוך 6, או בערך 16.7%.</p>

    <h3>התוחלת: מה מצפים שיקרה "בממוצע" לאורך זמן?</h3>
    <p>התוחלת היא ה"ממוצע התיאורטי" של התוצאות אם נחזור על הניסוי מספר אינסופי של פעמים. עבור הקובייה שלנו, היא מחושבת כך:</p>
    <p>תוחלת = (1 * 1/6) + (2 * 1/6) + (3 * 1/6) + (4 * 1/6) + (5 * 1/6) + (6 * 1/6) = 21 / 6 = **3.5**</p>
    <p>שימו לב: 3.5 הוא לא מספר שיכול באמת לצאת בהטלה בודדת! הוא מייצג את הערך המרכזי, "נקודת האיזון", שאליו הממוצע של תוצאות ההטלות שלנו צפוי להתקרב ככל שנאסוף יותר נתונים.</p>

    <h3>מדוע תוצאות בודדות "מקפצות" והממוצע אינו יציב בתחילה?</h3>
    <p>בהטלה הראשונה או במספר קטן של הטלות, לכל תוצאה בודדת יש השפעה דרמטית על הממוצע המצטבר. אם קיבלתם 6 בהטלה הראשונה, הממוצע שלכם הוא 6 - רחוק מאוד מ-3.5! אם אחריה קיבלתם 1, הממוצע קופץ ל-(6+1)/2 = 3.5. התנודתיות הזו אופיינית מאוד למדגמים קטנים – הם אינם מייצגים נאמנה את ההתנהגות ארוכת הטווח של התהליך האקראי.</p>

    <h3>הכוח המאזן של המספרים הגדולים</h3>
    <p>הנה קסם אמיתי: ככל שאוספים יותר ויותר הטלות, ההשפעה של כל הטלה בודדת הולכת ומצטמצמת. התוצאות הנמוכות (1, 2) מתאזנות בהדרגה עם התוצאות הגבוהות (5, 6), וכל התוצאות יחד מתחילות לשקף את ההסתברות התיאורטית שלהן (1/6 כל אחת). התנודתיות ה"מקומית" של ההטלות הבודדות "מתפזרת" בתוך המסה הגדולה של הנתונים, והממוצע הכולל מתחיל להתנהג בצורה צפויה ויציבה יותר.</p>

    <h3>חוק המספרים הגדולים: העיקרון ששולט באקראיות</h3>
    <p>זה בדיוק העיקרון שעומד בבסיס **חוק המספרים הגדולים**: ככל שמספר החזרות על ניסוי אקראי זהה (ובלתי תלוי) גדל, כך הממוצע של התוצאות בפועל (הממוצע האמפירי) מתקרב יותר ויותר לתוחלת התיאורטית של הניסוי. הסימולציה כאן היא הדגמה ויזואלית מרהיבה של החוק הזה: צפו בקו הממוצע המצטבר בגרף - בהתחלה הוא מקפץ בפראות, אבל ככל שהטלות מצטברות, הוא מתייצב ומתכנס באופן ברור אל הקו האדום של התוחלת (3.5).</p>

    <h3>חוק המספרים הגדולים מסביבנו:</h3>
    <ul>
        <li>**חברות ביטוח:** הן לא יודעות מי ייפגע בתאונה מחר, אבל על סמך נתונים היסטוריים עצומים, הן יודעות לחזות את סך התביעות שיצטרכו לשלם לקבוצה גדולה של מבוטחים, ועל סמך זה לקבוע פרמיות.</li>
        <li>**סקרים ודגימות:** ככל שמדגם סקר אקראי גדול יותר, כך התוצאות שלו (כמו אחוז תמיכה במפלגה) קרובות יותר למציאות באוכלוסייה כולה.</li>
        <li>**בתי קזינו ומשחקי מזל:** בעוד שכל סיבוב רולטה או יד פוקר היא אקראית, חוק המספרים הגדולים מבטיח שלבית הקזינו יהיה רווח בטווח הארוך, כי התוחלת התיאורטית בנויה תמיד לטובתו, והיא מתממשת על פני מיליוני משחקים.</li>
    </ul>
    <p>אז בפעם הבאה שתטילו קובייה, זכרו: הטלה בודדת היא מזל טהור, אבל בטווח הארוך, המתמטיקה מנצחת!</p>
</div>

<style>
    /* כל הפונטים וצבעים נבחרו כדי ליצור מראה מודרני ונעים */
    body {
        font-family: 'Heebo', sans-serif; /* או פונט עברי נעים אחר */
        line-height: 1.7;
        direction: rtl;
        text-align: right;
        margin: 0;
        padding: 20px;
        background-color: #f0f4f8; /* רקע בהיר ונעים */
        color: #333;
    }
    h1, h2, h3 {
        color: #1a3f66; /* כותרות בצבע כחול כהה */
        margin-bottom: 15px;
        line-height: 1.4;
    }
    h1 {
        text-align: center;
        color: #0056b3; /* כותרת ראשית בצבע כחול בולט */
        margin-bottom: 30px;
    }
    p {
        margin-bottom: 15px;
    }
    .simulation-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* צל עדין יותר */
        margin-bottom: 30px;
        text-align: center;
        border: 1px solid #e0e0e0; /* מסגרת דקה */
    }
    .dice-display {
        margin-bottom: 25px;
        font-size: 4em; /* אייקון קובייה גדול */
        min-height: 1.2em; /* מונע קפיצות בפריסה */
        line-height: 1;
        color: #28a745; /* צבע ירוק לאייקון */
    }

    .stats {
        margin-bottom: 30px;
        font-size: 1.2rem;
        color: #555; /* צבע אפור כהה */
        display: flex; /* הצגת סטטיסטיקות בשורה */
        justify-content: center; /* מרכז סטטיסטיקות */
        gap: 30px; /* רווח בין פריטי סטטיסטיקה */
        flex-wrap: wrap; /* ירידת שורה במסכים קטנים */
    }
     .stats p {
         margin: 0; /* הסרת מרווח פנימי בפסקאות סטטיסטיקה */
     }
    .stats strong {
        color: #333; /* צבע כהה יותר לכותרות סטטיסטיקה */
    }
    .stats span {
        font-weight: bold;
        color: #007bff; /* צבע בולט לערכי הסטטיסטיקה */
    }

    .graph-container {
        position: relative;
        width: 100%;
        max-width: 900px; /* הגדלת רוחב הגרף */
        margin: 20px auto 30px auto;
        background-color: #f8f9fa; /* רקע בהיר יותר לגרף */
        border-radius: 8px;
        overflow: hidden; /* הסתרת חלקים שחורגים */
        border: 1px solid #d0d0d0;
    }
    canvas {
        display: block;
        width: 100%;
        height: 450px; /* הגדלת גובה הגרף */
    }

    .controls {
        margin-top: 20px;
        display: flex; /* כפתורים בשורה */
        justify-content: center; /* מרכוז כפתורים */
        flex-wrap: wrap; /* ירידת שורה במסכים קטנים */
        gap: 15px; /* רווח בין כפתורים */
    }
    .controls button {
        padding: 12px 25px; /* הגדלת מרווח פנימי */
        border: none;
        border-radius: 6px; /* פינות מעוגלות יותר לכפתורים */
        cursor: pointer;
        font-size: 1.1rem; /* גודל פונט גדול יותר */
        transition: background-color 0.2s ease, transform 0.1s ease; /* אנימציית מעבר ועדיפה בלחיצה */
        background-color: #28a745; /* ירוק - פעולה ראשית */
        color: white;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .controls button:hover:not(:disabled) {
        background-color: #218838; /* ירוק כהה יותר במעבר עכבר */
        transform: translateY(-2px); /* אפקט קל במעבר עכבר */
    }
     .controls button:active:not(:disabled) {
         transform: translateY(0); /* לחיצה חוזרת למקום */
     }
    .controls button.secondary {
        background-color: #ffc107; /* צהוב/כתום - פעולה משנית */
        color: #333;
    }
    .controls button.secondary:hover:not(:disabled) {
        background-color: #e0a800; /* צהוב/כתום כהה יותר */
         transform: translateY(-2px);
    }
     .controls button.secondary:active:not(:disabled) {
         transform: translateY(0);
     }
    .controls button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        box-shadow: none;
        transform: none;
    }


    .explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto; /* מרכז והוספת מרווח גדול יותר */
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1rem;
        background-color: #007bff; /* כחול - פעולה חשובה */
        color: white;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
     .explanation-toggle:hover {
        background-color: #0056b3; /* כחול כהה יותר */
         transform: translateY(-2px);
     }
     .explanation-toggle:active {
         transform: translateY(0);
     }

    .hidden-explanation {
        display: none; /* עדיין נסתר כברירת מחדל */
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        border: 1px solid #e0e0e0;
    }
    .hidden-explanation h3 {
        margin-top: 25px;
        color: #1a3f66;
    }
    .hidden-explanation ul {
        margin-top: 10px;
        padding-right: 20px; /* הזחה לרשימות */
    }
     .hidden-explanation li {
         margin-bottom: 8px;
     }

     /* CSS for potential simple roll animation (example) */
     @keyframes rollSpin {
         0% { transform: rotate(0deg); }
         100% { transform: rotate(360deg); }
     }
      .rolling {
         animation: rollSpin 0.5s linear infinite; /* נניח אנימציה בזמן שהקובייה מתגלגלת */
         opacity: 0.6; /* שקיפות קלה בזמן גלגול */
      }

       @keyframes pulse {
         0% { transform: scale(1); opacity: 1; }
         50% { transform: scale(1.1); opacity: 0.8; }
         100% { transform: scale(1); opacity: 1; }
       }

       .stats span {
           display: inline-block; /* מאפשר אנימציה על span */
           transition: color 0.3s ease;
       }
        .stats span.pulsing {
            animation: pulse 0.5s ease-out;
        }

</style>

<script>
    const canvas = document.getElementById('averageGraph');
    const ctx = canvas.getContext('2d');
    const diceVisualSpan = document.getElementById('diceVisual'); // New element for visual dice
    const lastRollSpan = document.getElementById('lastRoll');
    const totalRollsSpan = document.getElementById('totalRolls');
    const averageSpan = document.getElementById('average');
    const rollOneBtn = document.getElementById('rollOneBtn');
    const roll100Btn = document.getElementById('roll100Btn');
    const roll1000Btn = document.getElementById('roll1000Btn');
    const roll10000Btn = document.getElementById('roll10000Btn');
    const resetBtn = document.getElementById('resetBtn');
    const explanationToggleBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');

    let totalRolls = 0;
    let sumOfRolls = 0;
    let averageHistory = [];
    let rollCountHistory = []; // Store totalRolls at the point each averageHistory entry was added
    const theoreticalAverage = 3.5;
    const diceEmojis = ['-', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅']; // Emoji for dice faces
    let animationFrameId = null; // To manage animation loop
    let isRolling = false; // Flag to prevent multiple roll animations

    // Graph drawing parameters
    const padding = 50; // More padding for labels
    let maxRollsDisplay = 100; // Initial max x-axis value
    const maxY = 6; // Max y-axis value for average
    const minY = 1; // Min y-axis value for average (useful if extending graph down)
    const yRange = maxY - minY;


    function rollDice() {
        return Math.floor(Math.random() * 6) + 1;
    }

    function updateDisplay(lastRollResult) {
        // Update text stats
        lastRollSpan.textContent = lastRollResult !== undefined ? lastRollResult : '-';
        totalRollsSpan.textContent = totalRolls;
        averageSpan.textContent = totalRolls > 0 ? (sumOfRolls / totalRolls).toFixed(4) : '-';

        // Add pulsing animation to updated stats
        [lastRollSpan, totalRollsSpan, averageSpan].forEach(span => {
            span.classList.remove('pulsing');
            // Use setTimeout to re-add the class after a brief moment, forcing re-animation
            setTimeout(() => span.classList.add('pulsing'), 10);
        });

        // Update visual dice (only for single rolls initially, or always?)
        // Let's update for single rolls and show '-' for batches
        if (lastRollResult !== undefined && !isRolling) { // Only update visual dice if not a batch roll
             diceVisualSpan.textContent = diceEmojis[lastRollResult];
        } else if (!isRolling) {
             diceVisualSpan.textContent = '-'; // Reset visual dice for batch display
        }
         diceVisualSpan.classList.remove('rolling'); // Ensure rolling class is off unless active
    }

    function drawGraph() {
        // Adjust canvas size to match display size
        const rect = canvas.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const graphWidth = canvas.width - 2 * padding;
        const graphHeight = canvas.height - 2 * padding;

        // Update maxRollsDisplay dynamically but snap to logical levels
        if (totalRolls > maxRollsDisplay) {
             if (totalRolls > 5000) maxRollsDisplay = 10000;
             else if (totalRolls > 500) maxRollsDisplay = 5000;
             else if (totalRolls > 50) maxRollsDisplay = 500;
             else maxRollsDisplay = Math.max(100, totalRolls * 2); // Double for small rolls, give room, min 100
        } else if (totalRolls === 0) {
             maxRollsDisplay = 100; // Reset display max on clear
        }


        // Draw Axes
        ctx.strokeStyle = '#555'; // Axis color
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, canvas.height - padding); // Y-axis
        ctx.lineTo(canvas.width - padding, canvas.height - padding); // X-axis
        ctx.stroke();

        // Draw Y-axis labels and ticks
        ctx.fillStyle = '#333';
        ctx.font = '14px Heebo, sans-serif';
        ctx.textAlign = 'right';
        ctx.textBaseline = 'middle';
        for (let i = 1; i <= maxY; i++) { // Start from 1 as min possible average is 1
            const y = canvas.height - padding - ((i - minY) / yRange) * graphHeight;
            ctx.fillText(i, padding - 10, y);
            ctx.beginPath();
            ctx.moveTo(padding, y);
            ctx.lineTo(padding - 6, y); // Longer ticks
            ctx.strokeStyle = '#ccc'; // Grid line color
            ctx.lineTo(canvas.width - padding, y); // Horizontal grid line
            ctx.stroke();
            ctx.strokeStyle = '#555'; // Reset stroke color for axis ticks
        }

         // Draw X-axis labels and ticks
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        ctx.fillStyle = '#333';
         const xTicks = [0]; // Always show 0
        // Add logical tick marks based on scale, but only show if distinct and relevant
        if (maxRollsDisplay <= 100) { // Scale up to 100
            xTicks.push(25, 50, 75, 100);
        } else if (maxRollsDisplay <= 500) { // Scale up to 500
             xTicks.push(100, 200, 300, 400, 500);
        } else if (maxRollsDisplay <= 1000) { // Scale up to 1000 (less likely with current jumps)
             xTicks.push(250, 500, 750, 1000);
        }
         else if (maxRollsDisplay <= 5000) { // Scale up to 5000
            xTicks.push(1000, 2000, 3000, 4000, 5000);
         }
         else { // Scale up to 10000+
             xTicks.push(2500, 5000, 7500, 10000);
         }

        xTicks.forEach(tick => {
             const x = padding + (tick / maxRollsDisplay) * graphWidth;
             if (x > padding - 10 && x < canvas.width - padding + 10) { // Avoid drawing ticks outside bounds
                  ctx.fillText(tick.toLocaleString(), x, canvas.height - padding + 10); // Add comma separators
                  ctx.beginPath();
                  ctx.moveTo(x, canvas.height - padding);
                  ctx.lineTo(x, canvas.height - padding + 6);
                  ctx.strokeStyle = '#ccc'; // Vertical grid line color
                  ctx.lineTo(x, padding); // Vertical grid line
                  ctx.stroke();
                  ctx.strokeStyle = '#555'; // Reset stroke color
             }
        });

        // Draw Theoretical Average line (3.5)
        const theoreticalY = canvas.height - padding - ((theoreticalAverage - minY) / yRange) * graphHeight;
        ctx.strokeStyle = '#dc3545'; // Redder red
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 4]); // Slightly adjusted dash
        ctx.beginPath();
        ctx.moveTo(padding, theoreticalY);
        ctx.lineTo(canvas.width - padding, theoreticalY);
        ctx.stroke();
        ctx.setLineDash([]); // Reset dash

        // Label Theoretical Average line
        ctx.fillStyle = '#dc3545';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'bottom'; // Position label below the line
        ctx.font = '14px Heebo, sans-serif';
        ctx.fillText('תוחלת תיאורטית (3.5)', canvas.width - padding + 5, theoreticalY);


        // Draw the Average History line
        if (averageHistory.length > 0) {
            ctx.strokeStyle = '#007bff'; // Bright blue
            ctx.lineWidth = 3; // Thicker line
            ctx.beginPath();

             let firstVisiblePoint = -1;
             // Find the first point that is visible on the graph's X-axis scale
             for(let i=0; i < rollCountHistory.length; i++) {
                 const x = padding + (rollCountHistory[i] / maxRollsDisplay) * graphWidth;
                 if (x >= padding) {
                     firstVisiblePoint = i;
                     const y = canvas.height - padding - ((averageHistory[i] - minY) / yRange) * graphHeight;
                     ctx.moveTo(x, y);
                     break;
                 }
             }

            // Draw line segments for the rest of the points
            if(firstVisiblePoint !== -1) {
                for (let i = firstVisiblePoint + 1; i < averageHistory.length; i++) {
                    const x = padding + (rollCountHistory[i] / maxRollsDisplay) * graphWidth;
                    const y = canvas.height - padding - ((averageHistory[i] - minY) / yRange) * graphHeight;
                    if (x >= padding) { // Only draw points within or entering the visible x range
                        ctx.lineTo(x, y);
                    } else {
                        // If the current point goes off-screen to the left, stop drawing the segment
                         break; // Assume history points are added in increasing order of rollCount
                    }
                }
                ctx.stroke();
            }
        }

         // Draw axes labels
         ctx.fillStyle = '#333';
         ctx.font = '16px Heebo, sans-serif';
         ctx.textAlign = 'center';
         ctx.textBaseline = 'top';
         ctx.fillText('מספר הטלות', canvas.width / 2, canvas.height - padding + 30);

         ctx.save(); // Save current state before rotating
         ctx.translate(padding - 30, canvas.height / 2); // Move origin
         ctx.rotate(-Math.PI / 2); // Rotate 90 degrees counter-clockwise
         ctx.textAlign = 'center';
         ctx.textBaseline = 'bottom';
         ctx.fillText('ממוצע מצטבר', 0, 0);
         ctx.restore(); // Restore state
    }


    function performRolls(num) {
         if (isRolling) return; // Prevent clicking buttons during animation/batch
         isRolling = true;
         disableButtons(); // Disable buttons

        if (num === 1) {
             // Simulate rolling animation
             diceVisualSpan.classList.add('rolling');
             diceVisualSpan.textContent = '?'; // Show question mark during roll
             lastRollSpan.textContent = '?'; // Update last roll display too
              lastRollSpan.classList.remove('pulsing'); // Remove pulse during animation

             setTimeout(() => {
                 const lastRollResult = rollDice();
                 sumOfRolls += lastRollResult;
                 totalRolls++;

                 averageHistory.push(sumOfRolls / totalRolls);
                 rollCountHistory.push(totalRolls);

                 updateDisplay(lastRollResult);
                 drawGraph();

                 diceVisualSpan.classList.remove('rolling');
                 isRolling = false;
                 enableButtons(); // Enable buttons after single roll
             }, 600); // Short delay to show animation
        } else { // Batch rolls
             diceVisualSpan.textContent = '-'; // Clear visual dice for batches
             lastRollSpan.textContent = '...'; // Indicate processing

             // No visual per-roll animation for batches, just perform calculations quickly
             const startRolls = totalRolls;
             let lastRollResult = null;
             for (let i = 0; i < num; i++) {
                 lastRollResult = rollDice(); // Keep track of the very last roll in the batch
                 sumOfRolls += lastRollResult;
                 totalRolls++;
             }

             // Add only the *final* point after the batch to history
             averageHistory.push(sumOfRolls / totalRolls);
             rollCountHistory.push(totalRolls);

             // Update display and draw graph
             updateDisplay(lastRollResult);
             drawGraph(); // Redraw graph completely after batch

             // Optional: could add a very fast sequence of graph draws for batches, but
             // this is simpler and fits constraints better. The main goal is the final convergence.

             isRolling = false;
             enableButtons(); // Enable buttons after batch
        }
    }

    function resetSimulation() {
        totalRolls = 0;
        sumOfRolls = 0;
        averageHistory = [];
        rollCountHistory = [];
        maxRollsDisplay = 100; // Reset graph scale
        updateDisplay();
        drawGraph(); // Clear graph
        diceVisualSpan.textContent = '-'; // Reset visual dice
        diceVisualSpan.classList.remove('rolling');
        isRolling = false;
        enableButtons();
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggleBtn.textContent = isHidden ? 'הסתר את הסוד' : 'סקרנים? גלו את הסוד מאחורי הקסם';
    }

    function disableButtons() {
        rollOneBtn.disabled = true;
        roll100Btn.disabled = true;
        roll1000Btn.disabled = true;
        roll10000Btn.disabled = true;
        resetBtn.disabled = true; // Maybe allow reset? Let's disable for simplicity
    }

    function enableButtons() {
        rollOneBtn.disabled = false;
        roll100Btn.disabled = false;
        roll1000Btn.disabled = false;
        roll10000Btn.disabled = false;
        resetBtn.disabled = false;
    }


    // Event Listeners
    rollOneBtn.addEventListener('click', () => performRolls(1));
    roll100Btn.addEventListener('click', () => performRolls(100));
    roll1000Btn.addEventListener('click', () => performRolls(1000));
    roll10000Btn.addEventListener('click', () => performRolls(10000));
    resetBtn.addEventListener('click', resetSimulation);
    explanationToggleBtn.addEventListener('click', toggleExplanation);

    // Initial setup
    explanationDiv.style.display = 'none'; // Ensure explanation is hidden initially
    updateDisplay();
    drawGraph(); // Draw empty graph with axes and theoretical average

    // Handle window resize to redraw graph correctly
    window.addEventListener('resize', drawGraph);

</script>