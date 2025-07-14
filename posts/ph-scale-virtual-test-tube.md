---
title: "מסע ה-pH: מבחנה אינטראקטיבית"
english_slug: ph-scale-virtual-test-tube
category: "כימיה"
tags: [סימולציה, אינטראקטיבי, ניסוי, חומצות ובסיסים, pH]
---
# גלו את קסם ה-pH!

מוכנים לחקור את עולם החומצות והבסיסים? הצטרפו למעבדה הווירטואלית שלנו! בחרו חומר יומיומי מהרשימה, הוסיפו אותו למבחנה וצפו כיצד הוא משנה את צבע התמיסה ואת ערך ה-pH. איזו הפתעה מצפה לכם בכל לחיצה?

<div class="container">
    <div class="test-tube-container">
        <div class="test-tube">
            <div class="liquid"></div>
             <div class="drop-animation"></div> <!-- Placeholder for drop animation -->
            <div class="ph-indicator"></div>
        </div>
        <div class="ph-scale">
            <!-- Scale labels are positioned dynamically by JS for better alignment -->
             <div class="scale-label" data-ph="14">14</div>
             <div class="scale-label" data-ph="13">13</div>
             <div class="scale-label" data-ph="12">12</div>
             <div class="scale-label" data-ph="11">11</div>
             <div class="scale-label" data-ph="10">10</div>
             <div class="scale-label" data-ph="9">9</div>
             <div class="scale-label" data-ph="8">8</div>
             <div class="scale-label" data-ph="7">7</div>
             <div class="scale-label" data-ph="6">6</div>
             <div class="scale-label" data-ph="5">5</div>
             <div class="scale-label" data-ph="4">4</div>
             <div class="scale-label" data-ph="3">3</div>
             <div class="scale-label" data-ph="2">2</div>
             <div class="scale-label" data-ph="1">1</div>
             <div class="scale-label" data-ph="0">0</div>
        </div>
    </div>

    <div class="controls">
        <div class="ph-display">pH: 7.0</div>
        <label for="substance-select">איזה חומר נוסיף היום?</label>
        <select id="substance-select">
            <option value="7.0">💦 מים מזוקקים</option>
            <option value="2.0">🍋 מיץ לימון</option>
            <option value="3.0">🍷 חומץ</option>
            <option value="6.0">☕ קפה שחור</option>
            <option value="8.0">NaHCO₃ סודה לשתייה (תמיסה)</option>
            <option value="11.0">🧼 אמוניה ביתית</option>
            <option value="13.0">🪠 מנקה ניקוזים (תמיסה)</option>
            <option value="1.0">🔋 חומצת בטריות</option>
            <option value="14.0">NaOH סודה קאוסטית (תמיסה)</option>
        </select>
        <button id="add-substance-btn">הוסף למבחנה ושנה צבע!</button>
    </div>
</div>

<button id="toggle-explanation-btn" class="info-button">מה זה בכלל pH? לחצו להסבר קצר!</button>

<div id="explanation" class="explanation-box" style="display: none;">
    <h2>סולם ה-pH בפשטות</h2>
    <p>סולם ה-pH הוא דרך קסומה למדוד עד כמה תמיסה מימית חומצית או בסיסית. הוא נע בין 0 ל-14:</p>
    <ul>
        <li>**pH נמוך מ-7:** מזכיר חומצות! (כמו מיץ לימון). הן אוהבות לשחרר יוני מימן (H⁺).</li>
        <li>**pH שווה ל-7:** זה ניטרלי, כמו מים נקיים! איזון מושלם בין יוני H⁺ ליוני OH⁻.</li>
        <li>**pH גבוה מ-7:** ברוכים הבאים לעולם הבסיסים (או אלקליות)! (למשל, סודה לשתייה). הם אוהבים לקלוט יוני H⁺ או לשחרר יוני OH⁻.</li>
    </ul>
    <p>הסולם הזה הוא לוגריתמי - כל יחידה אחת למעלה או למטה פירושה שינוי ענק פי 10 בריכוז יוני המימן! דמיינו את זה!</p>
    <p>בסימולציה הזו, שינוי הצבע במבחנה מדמה "אינדיקטור pH" - חומר שמשנה את צבעו בהתאם לרמת החומציות, ומד ה-pH הווירטואלי מראה לנו את הערך המדויק. איזה כיף לראות כימיה קורית מול העיניים!</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

    body {
        font-family: 'Varela Round', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        background: linear-gradient(to bottom right, #e0f7fa, #e1bee7); /* Softer, educational gradient */
        color: #2c3e50; /* Darker, readable text */
        min-height: 100vh;
        margin: 0;
        line-height: 1.6;
    }

    h1 {
        color: #00796b; /* Teal/Green */
        margin-bottom: 15px;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    p {
        text-align: center;
        max-width: 700px;
        margin-bottom: 25px;
        font-size: 1.1em;
    }

    .container {
        display: flex;
        align-items: flex-end;
        margin-top: 40px;
        margin-bottom: 30px;
        background-color: #ffffff;
        padding: 30px 40px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        justify-content: center;
    }

    .test-tube-container {
        display: flex;
        align-items: flex-end;
        position: relative;
        height: 300px; /* Increased height */
        margin-right: 60px; /* Increased margin */
        margin-left: 20px;
        flex-shrink: 0;
    }

    .test-tube {
        width: 60px; /* Increased width */
        height: 250px; /* Increased height */
        border: 4px solid #34495e; /* Darker border */
        border-top: none;
        border-radius: 0 0 30px 30px; /* More rounded base */
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.4) 50%, rgba(255, 255, 255, 0.2) 100%); /* Glossy effect */
        box-shadow: inset 0 -5px 5px rgba(0,0,0,0.2);
    }

    .liquid {
        width: 100%;
        /* height: 100%; Removed fixed height */
        position: absolute;
        bottom: 0;
        left: 0;
        background-color: #b2dfdb; /* Initial neutral color (light teal) */
        transition: background-color 1.5s ease-in-out; /* Slower, smoother transition */
        /* Animation for initial fill */
        animation: initial-fill 1s ease-out forwards;
        height: 100%; /* Fill initially */
    }

     @keyframes initial-fill {
         0% { height: 0; }
         100% { height: 100%; }
     }

    .drop-animation {
        position: absolute;
        top: 0;
        left: 50%;
        width: 15px; /* Size of the drop */
        height: 15px;
        background-color: rgba(0, 123, 255, 0.8); /* Example drop color */
        border-radius: 50%;
        transform: translate(-50%, -20px); /* Start above the tube */
        opacity: 0;
        z-index: 3; /* Above liquid */
    }

    .ph-scale {
        width: 50px; /* Wider scale */
        height: 250px; /* Match test tube liquid height */
        border-left: 2px solid #34495e;
        position: relative;
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        padding: 0 10px; /* More padding */
        box-sizing: border-box;
    }

    .scale-label {
        position: absolute;
        left: 60px; /* Position relative to the scale */
        width: 30px; /* Ensure space for label */
        text-align: left;
        font-size: 0.9em;
        color: #555;
        pointer-events: none; /* Do not interfere with clicks */
        transition: color 0.3s ease;
    }

    .ph-indicator {
        width: 35px; /* Wider indicator */
        height: 8px; /* Thicker indicator */
        background-color: #e74c3c; /* Default red */
        position: absolute;
        right: -5px; /* Position relative to test tube */
        border-radius: 4px;
        transition: bottom 1.5s ease-in-out, background-color 0.5s ease; /* Smooth movement */
        z-index: 2; /* Ensure indicator is above liquid */
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .controls {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-top: 20px; /* Add margin if flex-wrapped */
    }

    .ph-display {
        font-size: 2em; /* Larger display */
        font-weight: bold;
        margin-bottom: 25px;
        color: #00796b; /* Teal */
        min-width: 150px; /* Reserve space */
        text-align: center;
        padding: 10px;
        border: 2px solid #b2dfdb;
        border-radius: 8px;
        background-color: #e0f2f7; /* Light blue background */
    }

    label {
        margin-bottom: 8px; /* More space */
        font-weight: bold;
        color: #34495e;
    }

    select, button {
        padding: 12px 15px; /* More padding */
        margin-bottom: 15px; /* More space */
        border: 1px solid #bdc3c7; /* Light gray border */
        border-radius: 8px; /* More rounded */
        font-size: 1em;
        font-family: 'Varela Round', sans-serif;
        outline: none; /* Remove outline on focus */
    }

    select {
         background-color: #ecf0f1; /* Light background */
         cursor: pointer;
         min-width: 200px; /* Ensure minimum width */
    }

    button {
        background-color: #3498db; /* Blue */
        color: white;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    button:hover {
        background-color: #2980b9; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    }

    button:active {
        transform: scale(0.98); /* Slight press effect */
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .info-button {
        margin-top: 25px;
        background-color: #95a5a6; /* Gray */
    }

    .info-button:hover {
         background-color: #7f8c8d; /* Darker gray */
    }

    .explanation-box {
        margin-top: 30px;
        padding: 25px;
        background-color: #ecf0f1; /* Light gray */
        border-radius: 12px;
        border: 1px solid #bdc3c7;
        width: 90%;
        max-width: 700px;
        line-height: 1.7;
        color: #34495e;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .explanation-box h2 {
        color: #00796b; /* Teal */
        margin-top: 0;
        border-bottom: 2px solid #b2dfdb;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .explanation-box ul {
        list-style-type: disc;
        padding-left: 25px;
        margin-bottom: 15px;
    }

    .explanation-box li {
        margin-bottom: 8px;
    }

    .explanation-box strong {
        color: #00796b; /* Teal */
    }

     /* Responsive adjustments */
    @media (max-width: 768px) {
        .container {
            flex-direction: column;
            align-items: center;
        }

        .test-tube-container {
            margin-right: 0;
            margin-bottom: 30px;
            margin-left: 0;
        }

        .ph-scale {
            margin-left: 20px; /* Add space between tube and scale */
        }

        .controls {
            align-items: center;
            width: 100%;
        }

        select, button {
            width: 80%;
            box-sizing: border-box;
            text-align: center; /* Center text in select/button */
        }

         label {
             align-self: center; /* Center label above controls */
         }

        .ph-display {
             width: 80%;
             box-sizing: border-box;
        }
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const substanceSelect = document.getElementById('substance-select');
        const addSubstanceBtn = document.getElementById('add-substance-btn');
        const liquidElement = document.querySelector('.liquid');
        const phDisplay = document.querySelector('.ph-display');
        const phIndicator = document.querySelector('.ph-indicator');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
        const explanationDiv = document.getElementById('explanation');
        const scaleLabels = document.querySelectorAll('.scale-label');
        const testTubeHeight = 250; // px, matches .test-tube height
        const scaleHeight = 250; // px, matches .ph-scale height
        const dropAnimationElement = document.querySelector('.drop-animation');


        // Define a more granular pH color map
        const phColors = [
            { ph: 0, color: '#FF0000' }, // Red
            { ph: 1, color: '#FF4500' }, // OrangeRed
            { ph: 2, color: '#FFA500' }, // Orange
            { ph: 3, color: '#FFD700' }, // Gold
            { ph: 4, color: '#FFFF00' }, // Yellow
            { ph: 5, color: '#9ACD32' }, // YellowGreen
            { ph: 6, color: '#ADFF2F' }, // GreenYellow
            { ph: 7, color: '#008000' }, // Green (Neutral)
            { ph: 8, color: '#00CED1' }, // DarkTurquoise
            { ph: 9, color: '#4682B4' }, // SteelBlue
            { ph: 10, color: '#1E90FF' }, // DodgerBlue
            { ph: 11, color: '#0000FF' }, // Blue
            { ph: 12, color: '#4B0082' }, // Indigo
            { ph: 13, color: '#8A2BE2' }, // BlueViolet
            { ph: 14, color: '#9400D3'  // DarkViolet
        ];

         // Helper to convert hex to RGB
        function hexToRgb(hex) {
            const bigint = parseInt(hex.slice(1), 16);
            const r = (bigint >> 16) & 255;
            const g = (bigint >> 8) & 255;
            const b = bigint & 255;
            return { r, g, b };
        }

        // Function to interpolate color based on pH
        function getPhColor(ph) {
            ph = Math.max(0, Math.min(14, parseFloat(ph))); // Clamp pH

            for (let i = 0; i < phColors.length - 1; i++) {
                const p1 = phColors[i];
                const p2 = phColors[i + 1];

                if (ph >= p1.ph && ph <= p2.ph) {
                    const ratio = (ph - p1.ph) / (p2.ph - p1.ph);
                    const color1 = hexToRgb(p1.color);
                    const color2 = hexToRgb(p2.color);

                    const r = Math.round(color1.r + (color2.r - color1.r) * ratio);
                    const g = Math.round(color1.g + (color2.g - color1.g) * ratio);
                    const b = Math.round(color1.b + (color2.b - color1.b) * ratio);

                    return `rgb(${r},${g},${b})`;
                }
            }
            // Should not reach here if pH is clamped, but return end colors just in case
            if (ph < phColors[0].ph) return phColors[0].color;
            return phColors[phColors.length - 1].color;
        }

         // Position scale labels dynamically
        function positionScaleLabels() {
             scaleLabels.forEach(label => {
                 const phValue = parseFloat(label.getAttribute('data-ph'));
                 // pH 14 is at bottom (0% from bottom of scale), pH 0 is at top (100% from bottom of scale)
                 const bottomPercentage = (14 - phValue) / 14 * 100;
                 label.style.bottom = `${bottomPercentage}%`;
                 label.style.transform = 'translateY(50%)'; // Vertically center text on the tick
            });
        }

        // Function to update the simulation based on pH
        function updateSimulation(ph) {
            const safePh = Math.max(0, Math.min(14, parseFloat(ph))); // Ensure pH is within 0-14

             // Animate a drop falling
             dropAnimationElement.style.cssText = `
                 top: 0;
                 left: 50%;
                 width: 15px;
                 height: 15px;
                 background-color: ${getPhColor(safePh)}; /* Drop color matches target pH */
                 border-radius: 50%;
                 transform: translate(-50%, -20px);
                 opacity: 1;
                 z-index: 3;
                 transition: none; /* Reset transition */
             `;

             // Trigger reflow to restart animation
             void dropAnimationElement.offsetWidth;

            dropAnimationElement.style.cssText += `
                 transition: transform 1s ease-in, opacity 0.8s linear;
                 transform: translate(-50%, ${testTubeHeight - 20}px); /* Animate down to near the bottom */
                 opacity: 0;
             `;


             // Update pH display, liquid color, and indicator position after a short delay
            setTimeout(() => {
                 phDisplay.textContent = `pH: ${safePh.toFixed(1)}`;

                 const color = getPhColor(safePh);
                 liquidElement.style.backgroundColor = color;
                 phIndicator.style.backgroundColor = color; // Indicator color can match liquid

                 // Calculate indicator position: pH 14 at bottom (0% from bottom), pH 0 at top (100% from bottom)
                 const bottomPercentage = (14 - safePh) / 14 * 100;
                 phIndicator.style.bottom = `${bottomPercentage}%`; // Use percentage relative to scale/tube height


            }, 800); // Delay matches drop animation duration
        }

        // Event listener for button click
        addSubstanceBtn.addEventListener('click', () => {
            const selectedPh = substanceSelect.value;
            updateSimulation(selectedPh);
        });

        // Position labels initially
        positionScaleLabels();

        // Initial state (Water)
        updateSimulation(substanceSelect.value);

        // Toggle explanation visibility
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'מה זה בכלל pH? לחצו להסבר קצר!';
        });
    });
</script>