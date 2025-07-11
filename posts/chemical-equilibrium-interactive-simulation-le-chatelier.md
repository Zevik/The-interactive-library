---
title: "מסע לשיווי משקל כימי: סימולציה אינטראקטיבית של ריאקציה הפיכה ותגובת מערכת לשינויים (עקרון לה-שטלייה)"
english_slug: chemical-equilibrium-interactive-simulation-le-chatelier
category: "כימיה"
tags: ["כימיה", "שיווי משקל כימי", "לה-שטלייה", "סימולציה", "אינטראקטיבי", "ריכוזים", "טמפרטורה", "הדמיה מדעית"]
---
# מסע לשיווי משקל כימי: חקר ריאקציה הפיכה

צאו למסע מרתק אל עולם שיווי המשקל הכימי! בסימולציה האינטראקטיבית הזו, תוכלו לצפות בזמן אמת כיצד ריאקציה הפיכה שואפת להגיע לאיזון דינמי, וחשוב מכך - כיצד היא מגיבה ל"הפרעות" חיצוניות. נסו לשנות את ריכוזי המגיבים או התוצרים, שחקו עם הטמפרטורה, וגלו בעצמכם כיצד המערכת מתאימה את עצמה כדי למזער את השפעת השינוי, בהתאם לעקרון לה-שטלייה.

<div class="simulation-wrapper">
    <div class="simulation-container">
        <div class="controls-panel">
            <h2>מעבדת השליטה</h2>
            <div class="control-group reaction-info">
                <h3>הריאקציה שלנו:</h3>
                <p>A ⇌ B</p>
                <p class="reaction-type">ריאקציה אקסותרמית (פולטת חום): ΔH &lt; 0</p>
                <p class="equilibrium-const">בשיווי משקל: [B] / [A] = K<sub>eq</sub></p>
            </div>

            <div class="control-group initial-settings">
                <h3>הגדרות התחלה:</h3>
                 <div class="input-pair">
                    <label for="initialA">[A] התחלתי:</label>
                    <input type="number" id="initialA" value="10" min="0" step="0.1">
                 </div>
                 <div class="input-pair">
                    <label for="initialB">[B] התחלתי:</label>
                    <input type="number" id="initialB" value="1" min="0" step="0.1">
                 </div>
            </div>

            <div class="control-group simulation-actions">
                 <h3>פעולות סימולציה:</h3>
                <button id="startBtn" class="action-button start">התחל ניסוי!</button>
                <button id="stopBtn" class="action-button stop" disabled>עצור</button>
                <button id="resetBtn" class="action-button reset">אפס הכל</button>
            </div>

            <div class="control-group concentration-changes">
                <h3>הפרעת ריכוזים:</h3>
                <p class="instruction">הוסף או הסר חומרים תוך כדי ריצה:</p>
                <div class="button-pair">
                    <button id="addA" class="change-button">+A</button>
                    <button id="removeA" class="change-button">-A</button>
                </div>
                 <div class="button-pair">
                    <button id="addB" class="change-button">+B</button>
                    <button id="removeB" class="change-button">-B</button>
                 </div>
            </div>

            <div class="control-group temperature-changes">
                <h3>הפרעת טמפרטורה:</h3>
                 <p class="instruction">שנה את הטמפרטורה תוך כדי ריצה:</p>
                 <div class="button-pair">
                    <button id="tempLowBtn" class="temp-button low-temp">טמפ' נמוכה</button>
                    <button id="tempMediumBtn" class="temp-button medium-temp">טמפ' רגילה</button>
                    <button id="tempHighBtn" class="temp-button high-temp">טמפ' גבוהה</button>
                 </div>
            </div>
        </div>
        <div class="graph-area">
            <h2>גרף ריכוזים בזמן</h2>
            <canvas id="equilibriumCanvas"></canvas>
            <div class="graph-legend">
                <span class="legend-item"><span class="legend-color a-color"></span>[A] ריכוז מגיב A</span>
                <span class="legend-item"><span class="legend-color b-color"></span>[B] ריכוז תוצר B</span>
            </div>
        </div>
    </div>

    <button id="toggleExplanationBtn" class="toggle-button">הצג/הסתר הסבר מדעי</button>

    <div id="explanation" class="explanation-panel" style="display: none;">
        <h2>הבסיס המדעי: שיווי משקל כימי ועקרון לה-שטלייה</h2>
        <p><strong>שיווי משקל כימי:</strong> דמיינו תגובה כימית שפועלת כמו רחוב דו-סטרי. מגיבים הופכים לתוצרים בכיוון אחד, ותוצרים הופכים למגיבים בכיוון ההפוך. בריאקציה הפיכה, שני התהליכים מתרחשים בו זמנית. שיווי משקל כימי מושג כשהקצב שבו מגיבים הופכים לתוצרים <strong>שווה בדיוק</strong> לקצב שבו תוצרים הופכים למגיבים. במצב הזה, הריכוזים הכוללים של כל החומרים נשארים קבועים, למרות שהתגובות ממשיכות להתקיים ללא הפסקה (זהו שיווי משקל <strong>דינמי</strong>!).</p>
        <p><strong>עקרון לה-שטלייה:</strong> מה קורה כשמערכת הנמצאת בשיווי משקל "מותקפת" על ידי שינוי חיצוני? עקרון לה-שטלייה מנבא זאת: "כאשר משנים תנאים במערכת הנמצאת בשיווי משקל (כמו ריכוז, טמפרטורה או לחץ), המערכת תגיב בכיוון שימזער את השפעת השינוי ותגיע למצב שיווי משקל חדש".</p>
        <ul>
            <li><strong>הפרעת ריכוזים:</strong> הוספת חומר (מגיב או תוצר) למערכת בשיווי משקל תגרום לתגובה "לברוח" מהחומר שהוסף - כלומר, להתרחש בכיוון שצורך את החומר העודף. אם מוציאים חומר, המערכת תגיב בכיוון שמייצר אותו מחדש. למשל, בסימולציה שלנו (A ⇌ B), אם תוסיפו A, המערכת תגיב ביצירת יותר B (תנועה ימינה) כדי להשתמש ב-A שהוסף. אם תוציאו A, המערכת תגיב בפירוק B ליצירת A (תנועה שמאלה).</li>
            <li><strong>הפרעת טמפרטורה:</strong> טמפרטורה משפיעה על קבוע שיווי המשקל עצמו, K<sub>eq</sub>. הריאקציה בסימולציה (A ⇌ B) היא אקסותרמית (ΔH < 0), כלומר היא "מייצרת" חום. הגדלת הטמפרטורה היא כמו "הוספת" חום למערכת. לפי לה-שטלייה, המערכת תגיב בכיוון שצורך חום - הכיוון האנדותרמי (ההפוך). לכן, העלאת טמפרטורה בריאקציה אקסותרמית תזיז את שיווי המשקל לכיוון המגיבים (שמאלה, יצירת יותר A ופחות B), ותקטין את K<sub>eq</sub>. הורדת טמפרטורה תגרום לתגובה להתרחש בכיוון האקסותרמי (הישר) כדי "לפצות" על החום שנגרע, ותזיז את שיווי המשקל לכיוון התוצרים (ימינה, יצירת יותר B ופחות A), ותגדיל את K<sub>eq</sub>.</li>
        </ul>
        <p><strong>חקר הסימולציה:</strong> הסימולציה מציגה ויזואלית את השינויים בריכוזי A ו-B לאורך זמן. צפו כיצד הם משתנים במהירות בתחילת הניסוי עד להגעה לשיווי משקל, וכיצד הם מגיבים בחדות לכל שינוי שאתם מבצעים, ואז שוב מתייצבים במצב שיווי משקל חדש. שימו לב במיוחד כיצד הטמפרטורה משפיעה על הריכוזים הסופיים בשיווי המשקל - הוכחה חיה להשפעתה על K<sub>eq</sub>!</p>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 30px;
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
        color: #333;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: #007bff; /* Primary blue */
        margin-bottom: 15px;
        font-weight: 700; /* Bold */
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #0056b3; /* Darker blue */
    }

    p {
        margin-bottom: 15px;
    }

    .simulation-wrapper {
        max-width: 1000px;
        margin: 0 auto;
        padding: 0 15px;
    }

    .simulation-container {
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 30px; /* Space between panels */
        margin-bottom: 30px;
        background-color: #ffffff; /* White background */
        padding: 30px;
        border-radius: 12px; /* Rounded corners */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        border: 1px solid #e0e0e0; /* Light border */
    }

    .controls-panel {
        flex: 1 1 350px; /* Flex properties */
        min-width: 300px; /* Minimum width */
    }

    .graph-area {
        flex: 2 1 500px; /* Flex properties */
        min-width: 350px; /* Minimum width */
        background-color: #f8f9fa; /* Light gray background */
        border-radius: 8px;
        padding: 20px;
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* Inner shadow */
        display: flex;
        flex-direction: column; /* Stack header, canvas, legend */
        justify-content: space-between; /* Space out elements */
    }

    .graph-area h2 {
        margin-top: 0;
        margin-bottom: 20px;
        text-align: center;
        color: #0056b3;
    }

    canvas {
        width: 100% !important; /* Make canvas responsive */
        height: 350px !important; /* Fixed height for clarity */
        background-color: #ffffff; /* White canvas background */
        border-radius: 6px;
        border: 1px solid #d0d0d0;
    }

    .graph-legend {
        margin-top: 15px;
        text-align: center;
        font-size: 0.9em;
        color: #555;
    }

    .legend-item {
        display: inline-block;
        margin: 0 15px;
    }

    .legend-color {
        display: inline-block;
        width: 15px;
        height: 15px;
        margin-left: 5px; /* Space between color box and text in RTL */
        vertical-align: middle;
        border-radius: 3px;
    }

    .a-color { background-color: #007bff; } /* Blue for A */
    .b-color { background-color: #28a745; } /* Green for B */


    .control-group {
        margin-bottom: 25px;
        padding-bottom: 20px;
        border-bottom: 1px solid #eeeeee; /* Light separator */
    }

    .control-group:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

     .control-group h3 {
         margin-top: 0;
         margin-bottom: 10px;
         color: #0056b3;
         font-size: 1.1em;
     }

    .instruction {
        font-size: 0.95em;
        color: #555;
        margin-bottom: 10px;
    }

    .input-pair, .button-pair {
        display: flex;
        align-items: center; /* Vertically align items */
        margin-bottom: 10px;
        flex-wrap: wrap; /* Allow wrapping */
    }

    .input-pair label {
        display: inline-block;
        margin-bottom: 5px;
        font-weight: 700;
        width: 150px; /* Fixed width for labels for alignment */
        min-width: 100px; /* Allow shrinking */
        flex-shrink: 0; /* Prevent shrinking below min-width */
        text-align: right; /* Align label text */
        padding-left: 10px; /* Space between label and input */
    }

    input[type="number"] {
        flex-grow: 1; /* Allow input to fill space */
        max-width: 150px; /* Max width for input */
        padding: 10px;
        border: 1px solid #cccccc;
        border-radius: 5px;
        box-sizing: border-box;
        font-size: 1em;
        text-align: left; /* Align input value left */
    }

    .action-button, .change-button, .temp-button {
        padding: 12px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        font-weight: 700;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        text-align: center;
        display: inline-block; /* Ensure buttons are inline */
    }

    .action-button.start {
        background-color: #28a745; /* Green */
        color: white;
    }
    .action-button.start:hover:not(:disabled) {
        background-color: #218838;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }

     .action-button.stop {
        background-color: #ffc107; /* Yellow */
        color: #212529;
    }
     .action-button.stop:hover:not(:disabled) {
        background-color: #e0a800;
        transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(255, 193, 7, 0.3);
    }

    .action-button.reset {
        background-color: #dc3545; /* Red */
        color: white;
    }
    .action-button.reset:hover:not(:disabled) {
        background-color: #c82333;
        transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3);
    }

    .change-button {
        background-color: #007bff; /* Blue */
        color: white;
        flex-grow: 1; /* Allow change buttons to fill space */
        max-width: 120px;
    }
    .change-button:hover:not(:disabled) {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }


    .temp-button {
         flex-grow: 1; /* Allow temp buttons to fill space */
         max-width: 150px;
         color: white;
    }
    .temp-button.low-temp { background-color: #28a745; } /* Green */
    .temp-button.low-temp:hover:not(:disabled) { background-color: #218838; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3); }
    .temp-button.medium-temp { background-color: #ffc107; color: #212529;} /* Yellow */
    .temp-button.medium-temp:hover:not(:disabled) { background-color: #e0a800; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(255, 193, 7, 0.3); }
    .temp-button.high-temp { background-color: #dc3545; } /* Red */
    .temp-button.high-temp:hover:not(:disabled) { background-color: #c82333; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3); }


    button:disabled {
        background-color: #cccccc !important;
        cursor: not-allowed;
        transform: none !important;
        box-shadow: none !important;
        opacity: 0.7;
    }

    .toggle-button {
         display: block;
         width: 250px;
         margin: 30px auto;
         background-color: #6c757d; /* Gray */
         color: white;
         padding: 15px 25px;
         font-size: 1.1em;
         border: none;
         border-radius: 5px;
         cursor: pointer;
         transition: background-color 0.3s ease, transform 0.1s ease;
         text-align: center;
    }

    .toggle-button:hover {
         background-color: #5a6268;
         transform: translateY(-2px);
         box-shadow: 0 4px 8px rgba(108, 117, 125, 0.3);
    }


    .explanation-panel {
        margin-top: 30px;
        padding: 30px;
        background-color: #e9ecef; /* Light blue-gray */
        border-radius: 12px;
        border-right: 6px solid #007bff; /* Primary blue border on the right in RTL */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    .explanation-panel h2 {
        margin-top: 0;
        color: #0056b3;
        font-size: 1.4em;
    }

    .explanation-panel p {
        margin-bottom: 20px;
        font-size: 1em;
        color: #444;
    }

    .explanation-panel strong {
        color: #0056b3;
    }

    .explanation-panel ul {
        margin-bottom: 20px;
        padding-right: 25px; /* Padding on the right for RTL list */
        list-style: disc inside; /* Disc bullets */
        color: #444;
    }

    .explanation-panel li {
        margin-bottom: 10px;
        font-size: 1em;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .simulation-container {
            flex-direction: column; /* Stack controls and graph vertically */
            padding: 20px;
        }

        .controls-panel, .graph-area {
            flex: 1 1 100%; /* Take full width */
            min-width: auto;
        }

        body {
            padding: 15px;
        }

        .toggle-button {
            width: 100%;
            max-width: 250px; /* Keep max width for larger screens */
        }

        .input-pair {
            flex-direction: column; /* Stack label and input */
            align-items: flex-end; /* Align stacked items to the right */
        }

        .input-pair label {
             width: auto; /* Auto width for stacked labels */
             text-align: right;
             padding-left: 0;
             margin-bottom: 5px;
        }

        input[type="number"] {
             width: 100%; /* Full width input */
             max-width: none;
             text-align: right;
        }

         .button-pair {
             flex-direction: column; /* Stack buttons */
             align-items: stretch; /* Stretch buttons */
         }

         .action-button, .change-button, .temp-button {
             margin: 5px 0; /* Adjust margin for stacked buttons */
             max-width: none; /* Allow buttons to take full width */
         }

          .graph-area h2 {
             font-size: 1.2em;
          }
           .graph-legend {
             font-size: 0.8em;
         }
    }


     @media (max-width: 480px) {
         .simulation-container {
            padding: 15px;
         }
          body {
             padding: 10px;
         }
         h1 { font-size: 1.8em; }
         h2 { font-size: 1.4em; }
         h3 { font-size: 1.1em; }
          .action-button, .change-button, .temp-button {
             padding: 10px 15px;
             font-size: 0.9em;
          }
         .toggle-button {
             padding: 10px 15px;
             font-size: 1em;
         }

     }


</style>

<script>
    const canvas = document.getElementById('equilibriumCanvas');
    const ctx = canvas.getContext('2d');
    const initialAInput = document.getElementById('initialA');
    const initialBInput = document.getElementById('initialB');
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const resetBtn = document.getElementById('resetBtn');
    const addABtn = document.getElementById('addA');
    const removeABtn = document.getElementById('removeA');
    const addBBtn = document.getElementById('addB');
    const removeBBtn = document.getElementById('removeB');
    const tempLowBtn = document.getElementById('tempLowBtn');
    const tempMediumBtn = document.getElementById('tempMediumBtn');
    const tempHighBtn = document.getElementById('tempHighBtn');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');

    let state = {
        A: parseFloat(initialAInput.value),
        B: parseFloat(initialBInput.value),
        time: 0,
        history: [],
        isRunning: false,
        intervalId: null,
        kf: 0.1, // Forward rate constant (A -> B)
        kr: 0.05 // Reverse rate constant (B -> A)
    };

    // Temperature affects K = kf/kr. Reaction A ⇌ B is EXOTHERMIC (ΔH < 0).
    // Increasing T decreases K (shifts left, A increases, B decreases). Decreasing T increases K (shifts right, A decreases, B increases).
    // We'll adjust kf and kr slightly differently to simulate the shift and changed rates.
    const baseKf = 0.08; // Reduced base rate slightly for smoother start
    const tempSettings = {
        // K_eq = kf/kr
        low: { kf: baseKf * 1.5, kr: baseKf * 0.5 }, // K = 3 -> More B at equilibrium
        medium: { kf: baseKf, kr: baseKf * 0.8 },    // K = 1.25 -> Medium B
        high: { kf: baseKf * 0.6, kr: baseKf * 1.0 }  // K = 0.6 -> Less B at equilibrium
    };
    let currentTemp = 'medium'; // Default temperature

    function applyTemperature(tempKey) {
        currentTemp = tempKey;
        state.kf = tempSettings[tempKey].kf;
        state.kr = tempSettings[tempKey].kr;
        // Optional: Small concentration step to nudge system towards new equilibrium faster after temp change
         if (state.isRunning) {
             // This "nudge" is more illustrative of the expected *direction* of change on the graph edge,
             // letting the simulation then handle the actual curve.
             // Recalculate theoretical equilibrium for the *current total concentration* at the *new temperature*
             const totalConc = state.A + state.B;
             const K = state.kf / state.kr;
             // Solve total = A + B and K = B/A for A and B
             // total = A + KA => total = A(1+K) => A_eq = total / (1+K)
             // B_eq = K * A_eq
             const targetA = totalConc / (1 + K);
             const targetB = K * targetA;

             // Nudge concentrations slightly towards the new equilibrium point
             const nudgeFactor = 0.03; // Adjust this value for desired nudge strength (smaller means less jump)
             state.A = state.A * (1 - nudgeFactor) + targetA * nudgeFactor;
             state.B = state.B * (1 - nudgeFactor) + targetB * nudgeFactor;
         }
         // Visually highlight current temp button
         document.querySelectorAll('.temp-button').forEach(btn => btn.classList.remove('active-temp'));
         document.getElementById('temp' + tempKey.charAt(0).toUpperCase() + tempKey.slice(1) + 'Btn').classList.add('active-temp');
    }

    // Add a CSS class for the active temp button
    const styleSheet = document.styleSheets[0]; // Get the first stylesheet
    styleSheet.insertRule(`
        .temp-button.active-temp {
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5); /* Blue ring shadow */
            border: 2px solid white; /* White border */
        }
    `, styleSheet.cssRules.length); // Add the rule

    // Initial temperature setting
    applyTemperature(currentTemp);

    function drawGraph() {
        const width = canvas.width;
        const height = canvas.height;
        ctx.clearRect(0, 0, width, height);

        // Graph padding
        const padding = 45; // Increased padding for labels
        const graphWidth = width - 2 * padding;
        const graphHeight = height - 2 * padding;

        // Find max concentration and max time for scaling
        let maxConc = 0;
        let maxTime = 0;

         // Include initial values and current values in maxConc calculation
        const currentValues = [state.A, state.B];
        const initialValues = [parseFloat(initialAInput.value), parseFloat(initialBInput.value)];
        const allConcs = state.history.flatMap(p => [p.A, p.B]).concat(currentValues).concat(initialValues);

        if (allConcs.length > 0) {
             maxConc = Math.max(...allConcs);
        } else {
             maxConc = 10; // Default
        }

        if (state.history.length > 0) {
             maxTime = state.history[state.history.length - 1].time;
        } else {
             maxTime = 10; // Default time scale
        }

        maxConc = Math.max(maxConc, 5) * 1.2; // Ensure enough padding, minimum 5
        maxTime = Math.max(maxTime, 5) * 1.5; // Ensure enough padding, minimum 5


        // Draw Axes
        ctx.strokeStyle = '#aaa'; // Lighter axes
        ctx.lineWidth = 1.5;
        ctx.lineCap = 'round';

        // Y-axis
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.stroke();
        // X-axis
        ctx.beginPath();
        ctx.moveTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();

         // Draw grid lines (lighter)
        ctx.strokeStyle = '#eee';
        ctx.lineWidth = 1;
         const yTicks = 5;
         for (let i = 0; i <= yTicks; i++) {
             const y = height - padding - ((maxConc / yTicks) * i / maxConc) * graphHeight;
             ctx.beginPath();
             ctx.moveTo(padding, y);
             ctx.lineTo(width - padding, y);
             ctx.stroke();
         }
         const xTicks = 10; // More X ticks for better grid
         for (let i = 0; i <= xTicks; i++) {
              const x = padding + ((maxTime / xTicks) * i / maxTime) * graphWidth;
              ctx.beginPath();
              ctx.moveTo(x, padding);
              ctx.lineTo(x, height - padding);
              ctx.stroke();
         }


        // Draw Labels and Ticks (darker text)
        ctx.fillStyle = '#555';
        ctx.font = '14px Heebo, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        ctx.fillText('זמן', width / 2, height - padding + 15); // Time label
        ctx.textAlign = 'right';
        ctx.textBaseline = 'middle';
        ctx.save();
        ctx.translate(padding - 30, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('ריכוז', 0, 0); // Concentration label
        ctx.restore();

         // Y-axis ticks
         ctx.fillStyle = '#333';
         ctx.font = '12px Heebo, sans-serif';
         for (let i = 0; i <= yTicks; i++) {
             const conc = (maxConc / yTicks) * i;
             const y = height - padding - (conc / maxConc) * graphHeight;
             ctx.textAlign = 'right';
             ctx.fillText(conc.toFixed(1), padding - 10, y);
         }

         // X-axis ticks
         for (let i = 0; i <= xTicks; i++) {
              const time = (maxTime / xTicks) * i;
              const x = padding + (time / maxTime) * graphWidth;
              ctx.textAlign = 'center';
              ctx.textBaseline = 'top';
              ctx.fillText(time.toFixed(1), x, height - padding + 8);
         }


        // Draw Data Lines with potential jump indicators
        if (state.history.length >= 1) { // Need at least one point to start
            ctx.lineWidth = 3; // Thicker lines
            ctx.lineJoin = 'round'; // Smooth line joins

            // Helper to draw a line from history
            function drawLine(history, color, key) {
                ctx.strokeStyle = color;
                ctx.beginPath();
                let firstPoint = true;
                for (let i = 0; i < history.length; i++) {
                     const x = padding + (history[i].time / maxTime) * graphWidth;
                     const y = height - padding - (history[i][key] / maxConc) * graphHeight;

                     if (firstPoint) {
                         ctx.moveTo(x, y);
                         firstPoint = false;
                     } else {
                         // Detect sudden jumps (e.g., from concentration change)
                         const prevX = padding + (history[i-1].time / maxTime) * graphWidth;
                         const prevY = height - padding - (history[i-1][key] / maxConc) * graphHeight;
                         const timeDiff = history[i].time - history[i-1].time;

                         // If time difference is very small but concentration difference is large, it's a jump
                         if (timeDiff < 0.01 && Math.abs(history[i][key] - history[i-1][key]) > 0.01) {
                             // Draw a vertical line for the jump
                             ctx.stroke(); // Finish previous segment
                             ctx.beginPath();
                             ctx.strokeStyle = color; // Ensure color is correct
                             ctx.lineWidth = 3;
                             ctx.moveTo(x, prevY); // Start at the old Y at the new X
                             ctx.lineTo(x, y); // Draw to the new Y
                             ctx.stroke(); // Draw the jump segment
                             ctx.beginPath(); // Start new segment
                             ctx.strokeStyle = color;
                             ctx.lineWidth = 3;
                             ctx.moveTo(x, y); // Start new segment from the new point
                         } else {
                             ctx.lineTo(x, y);
                         }
                     }
                }
                ctx.stroke();
            }

             drawLine(state.history, '#007bff', 'A'); // Blue for A
             drawLine(state.history, '#28a745', 'B'); // Green for B
        }
         // If simulation is running, draw a small circle at the current point
         if (state.isRunning && state.history.length > 0) {
             const lastPoint = state.history[state.history.length - 1];
             const x = padding + (lastPoint.time / maxTime) * graphWidth;
             const yA = height - padding - (lastPoint.A / maxConc) * graphHeight;
             const yB = height - padding - (lastPoint.B / maxConc) * graphHeight;

             ctx.fillStyle = '#007bff';
             ctx.beginPath();
             ctx.arc(x, yA, 4, 0, Math.PI * 2); // Circle radius 4
             ctx.fill();

             ctx.fillStyle = '#28a745';
             ctx.beginPath();
             ctx.arc(x, yB, 4, 0, Math.PI * 2); // Circle radius 4
             ctx.fill();
         }

    }


    function updateSimulation() {
        if (!state.isRunning) return;

        const dt = 0.1; // Time step

        // Calculate rates (ensure non-negative concentrations for rate calculation)
        const currentA = Math.max(0, state.A);
        const currentB = Math.max(0, state.B);

        const rateForward = state.kf * currentA;
        const rateReverse = state.kr * currentB;

        // Calculate change in concentrations
        const dA = (-rateForward + rateReverse) * dt;
        const dB = (rateForward - rateReverse) * dt;

        // Update concentrations
        state.A += dA;
        state.B += dB;
        state.time += dt;

        // Prevent negative concentrations (shouldn't happen often but good safeguard)
        state.A = Math.max(0, state.A);
        state.B = Math.max(0, state.B);


        // Store history (reduce frequency for performance if needed, but 50ms interval with dt=0.1 is okay)
        // Ensure we don't add points too close in time if the interval is faster than dt
        if (state.history.length === 0 || state.time - state.history[state.history.length - 1].time >= dt/2) { // Store approximately every dt/2 seconds
             state.history.push({ time: state.time, A: state.A, B: state.B });
        }


        // Update graph periodically (not necessarily every simulation step)
        drawGraph();

        // Optional: stop condition (e.g., concentrations barely changing)
        // Not implementing auto-stop to allow continuous interaction
    }

    function startSimulation() {
        // Validate initial inputs
        const initialA = parseFloat(initialAInput.value);
        const initialB = parseFloat(initialBInput.value);
        if (isNaN(initialA) || initialA < 0 || isNaN(initialB) || initialB < 0) {
             alert("אנא הזינו ריכוזים התחלתיים חוקיים (מספרים אי שליליים).");
             return;
        }

        state.A = initialA;
        state.B = initialB;
        state.time = 0;
        state.history = [{ time: 0, A: state.A, B: state.B }];
        state.isRunning = true;

        startBtn.disabled = true;
        stopBtn.disabled = false;
        resetBtn.disabled = false;
        initialAInput.disabled = true;
        initialBInput.disabled = true;
        addABtn.disabled = false;
        removeABtn.disabled = false;
        addBBtn.disabled = false;
        removeBBtn.disabled = false;
        tempLowBtn.disabled = false;
        tempMediumBtn.disabled = false;
        tempHighBtn.disabled = false;


        // Ensure current temp settings are applied
        applyTemperature(currentTemp);

        state.intervalId = setInterval(updateSimulation, 50); // Run updateSimulation every 50ms (drawing happens inside)
        drawGraph(); // Initial draw
    }

    function stopSimulation() {
        state.isRunning = false;
        clearInterval(state.intervalId);
        state.intervalId = null;
        startBtn.disabled = false;
        stopBtn.disabled = true;
        // resetBtn remains enabled
        // Interaction buttons remain enabled after stop allowing changes before restart
    }

    function resetSimulation() {
         stopSimulation(); // Stop if running
         initialAInput.disabled = false;
         initialBInput.disabled = false;

         state.A = parseFloat(initialAInput.value); // Reset to values in input fields
         state.B = parseFloat(initialBInput.value);
         state.time = 0;
         state.history = [{ time: 0, A: state.A, B: state.B }];
         state.isRunning = false; // Ensure isRunning is false

         startBtn.disabled = false;
         stopBtn.disabled = true;
         resetBtn.disabled = true; // Can only reset if stopped after starting

         // Disable interaction buttons until simulation starts
         addABtn.disabled = true;
         removeABtn.disabled = true;
         addBBtn.disabled = true;
         removeBBtn.disabled = true;
         tempLowBtn.disabled = true;
         tempMediumBtn.disabled = true;
         tempHighBtn.disabled = true;


         // Reset to medium temperature on full reset and apply visually
         currentTemp = 'medium';
         applyTemperature(currentTemp);


         drawGraph(); // Draw initial state
    }

    function changeConcentration(species, amount) {
        // Allow concentration changes even if simulation is stopped, but only apply if simulation started once
        if (startBtn.disabled === false && stopBtn.disabled === true && resetBtn.disabled === true) {
             // Simulation hasn't started yet or was fully reset.
             // Maybe update the initial values directly? Let's keep it simple and only allow mid-sim changes.
             // Or, allow changes but only update the graph visualization, not the simulation state.
             // Sticking to mid-sim changes as per instructions "במהלך הסימולציה".
             console.log("Please start the simulation first.");
             return;
        }
         if (!state.isRunning && state.history.length > 0) {
             // Allow changes while stopped, but only if sim ran previously
         } else if (!state.isRunning) {
            return; // If sim never ran, don't allow changes
         }


        // Add a point to history *before* the sudden change
         state.history.push({ time: state.time, A: state.A, B: state.B });


        if (species === 'A') {
            state.A = Math.max(0, state.A + amount);
        } else if (species === 'B') {
            state.B = Math.max(0, state.B + amount);
        }

        // Add a point to history *after* the sudden change
         state.history.push({ time: state.time, A: state.A, B: state.B });

        drawGraph(); // Redraw immediately after change
        // If stopped, restart the interval briefly to show the new equilibrium forming?
        // Or just let the user click Start again? Let's stick to requiring user to click Start again if stopped.
    }

    function handleTemperatureChange(tempKey) {
         // Allow temperature changes even if simulation is stopped, but only apply if simulation started once
         if (startBtn.disabled === false && stopBtn.disabled === true && resetBtn.disabled === true) {
              console.log("Please start the simulation first.");
              return;
         }
          if (!state.isRunning && state.history.length > 0) {
             // Allow changes while stopped, but only if sim ran previously
         } else if (!state.isRunning) {
            return; // If sim never ran, don't allow changes
         }


         // Add a point to history *before* the change
         state.history.push({ time: state.time, A: state.A, B: state.B });

         applyTemperature(tempKey); // This updates kf and kr and nudges state

         // Add a point to history *after* the change
         state.history.push({ time: state.time, A: state.A, B: state.B });


        drawGraph(); // Redraw immediately after change
         // If stopped, restart the interval briefly? Same logic as concentration change.
    }


    // Event Listeners
    startBtn.addEventListener('click', startSimulation);
    stopBtn.addEventListener('click', stopSimulation);
    resetBtn.addEventListener('click', resetSimulation);

    // Change concentration by adding/removing a fixed amount (e.g., 3 units)
    addABtn.addEventListener('click', () => changeConcentration('A', 3));
    removeABtn.addEventListener('click', () => changeConcentration('A', -3));
    addBBtn.addEventListener('click', () => changeConcentration('B', 3));
    removeBBtn.addEventListener('click', () => changeConcentration('B', -3));

    tempLowBtn.addEventListener('click', () => handleTemperatureChange('low'));
    tempMediumBtn.addEventListener('click', () => handleTemperatureChange('medium'));
    tempHighBtn.addEventListener('click', () => handleTemperatureChange('high'));

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הצג הסבר מדעי';
        // Scroll to the explanation if showing it? Optional.
        // if (isHidden) { explanationDiv.scrollIntoView({ behavior: 'smooth' }); }
    });


    // Initialize canvas size based on container and handle resize
    function resizeCanvas() {
        const graphArea = canvas.parentElement;
        // Set canvas display size via CSS, then internal drawing buffer size
        canvas.style.width = '100%';
        canvas.style.height = '350px'; // Keep fixed height or calculate dynamically
        canvas.width = graphArea.clientWidth;
        canvas.height = 350; // Match CSS height for drawing buffer

        drawGraph(); // Redraw after resize
    }

    window.addEventListener('resize', resizeCanvas);

    // Initial setup
    resizeCanvas(); // Set initial size and draw
    resetSimulation(); // Set initial state and button states


</script>