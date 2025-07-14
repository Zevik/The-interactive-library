---
title: "המסע מהמייה לשיח: סימולטור אבולוציה של תקשורת מורכבת בבעלי חיים"
english_slug: evolution-of-complex-animal-communication-simulator
category: "ביולוגיה"
tags: [אבולוציה, תקשורת בעלי חיים, התנהגות בעלי חיים, סימולציה, מורכבות ביולוגית, אינטראקטיבי]
---
<h1>המסע מהמייה לשיח: סימולטור אבולוציה של תקשורת מורכבת בבעלי חיים</h1>
<p>האם חייתם האהובה מבינה אתכם? האם היא רק מגיבה לסימנים פשוטים, או מסוגלת לתקשורת עשירה יותר? הצטרפו אלינו למסע וירטואלי בזמן האבולוציוני, כדי לגלות כיצד מתוך קריאות וסימנים בסיסיים יכולות להתפתח מערכות תקשורת מורכבות, ממש כמו בטבע.</p>

<div id="simulation-app">
    <h2>הגדר את עולם התקשורת שלך</h2>
    <div class="controls">
        <label for="populationSize">גודל אוכלוסייה:</label>
        <input type="number" id="populationSize" value="200" min="50" max="5000">
        <span class="control-desc">כמה פרטים חיים בעולם זה.</span>

        <label for="initialSignalCount">מספר סימנים התחלתי:</label>
        <input type="number" id="initialSignalCount" value="2" min="1" max="50">
         <span class="control-desc">כמה 'מילים' או סימנים קיימים בשפה של דור האפס.</span>

        <label for="initialComplexity">מורכבות סימן התחלתית:</label>
        <input type="range" id="initialComplexity" value="2" min="0" max="10" step="0.1">
        <span id="initialComplexityValue" class="range-value">2.0</span>
        <span class="control-desc">עד כמה הסימנים הראשוניים מורכבים להבנה או שימוש (0=פשוט ביותר, 10=מורכב).</span>

        <label for="selectionPressure">לחץ סביבתי:</label>
        <input type="range" id="selectionPressure" value="6" min="0" max="10" step="0.1">
        <span id="selectionPressureValue" class="range-value">6.0</span>
        <span class="control-desc">עד כמה תקשורת יעילה חשובה להישרדות והצלחה (0=לא חשוב, 10=קריטי).</span>

        <label for="mutationRate">קצב שינוי גנטי:</label>
        <input type="range" id="mutationRate" value="0.05" min="0" max="0.5" step="0.005">
        <span id="mutationRateValue" class="range-value">0.050</span>
         <span class="control-desc">הסיכוי שיתרחשו שינויים אקראיים ביכולות התקשורת בכל דור.</span>

        <label for="generations">משך האבולוציה (דורות):</label>
        <input type="number" id="generations" value="200" min="50" max="2000">
         <span class="control-desc">כמה דורות הסימולציה תרוץ.</span>

    </div>
     <button id="startSimulation" class="interactive-button">התחל את האבולוציה!</button>


    <div id="simulation-results">
        <h3>התפתחות לאורך דורות</h3>
        <p>דור נוכחי: <span id="currentGeneration">0</span></p>
        <div class="chart-container">
            <h4>מספר סימנים ממוצע</h4>
            <div id="signalCountChart" class="chart"></div>
             <div class="chart-axis-label">דורות</div>
             <div class="chart-axis-label y-axis-label">מספר סימנים</div>
        </div>
        <div class="chart-container">
            <h4>מורכבות סימנים ממוצעת</h4>
            <div id="complexityChart" class="chart"></div>
            <div class="chart-axis-label">דורות</div>
             <div class="chart-axis-label y-axis-label">רמת מורכבות</div>
        </div>
        <div class="chart-container">
            <h4>יעילות תקשורת ממוצעת</h4>
            <div id="efficiencyChart" class="chart"></div>
            <div class="chart-axis-label">דורות</div>
             <div class="chart-axis-label y-axis-label">יעילות (0-1)</div>
        </div>
         <div id="simulation-output"></div> <!-- For simple text output/progress -->
    </div>
</div>

<button id="toggleExplanation" class="interactive-button secondary">מה בעצם קורה פה? (הסבר)</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: האבולוציה הסודית של שפות הטבע</h2>
    <p><strong>תקשורת בטבע: מעבר לציוצים ונהמות</strong></p>
    <p>תקשורת בעלי חיים היא הרבה יותר מסתם קולות. זוהי מערכת מורכבת של העברת מידע – דרך קול, ריח, מראה, מגע – שמשפיעה על האופן שבו פרטים מתנהגים ומגיבים לסביבה ולאחרים. היא חיונית למציאת מזון, הימנעות מטורפים, חיזור, טיפול בצאצאים ושמירה על מבנה חברתי.</p>

    <p><strong>מפשוט למורכב: סימנים ומערכות תקשורת</strong></p>
    <p>התקשורת יכולה להיות פשוטה מאוד – כמו צבע עז המזהיר מטורף, או קריאת אזעקה קצרה. אך היא יכולה להפוך למורכבת ביותר, כמו שירת לווייתנים או ריקוד הדבורה, המצריכים אוסף גדול של סימנים ויכולת לשלב אותם בדרכים שונות.</p>

    <p><strong>הכוח המניע: אבולוציה בשידור חי (כמעט)</strong></p>
    <p>איך נוצרת המורכבות הזו? דרך אבולוציה! פרטים עם יכולות תקשורת מעט יותר טובות (למשל, מפיקים סימנים ברורים יותר, מבינים מורכבות גבוהה יותר) מצליחים יותר בסביבתם - מוצאים יותר בני זוג, נמנעים טוב יותר מסכנה, או משתפים פעולה ביעילות. הם שורדים טוב יותר, מתרבים יותר, ומעבירים את ה'תכונות התקשורתיות' המשופרות האלה לדור הבא. שינויים קטנים אקראיים (מוטציות) מוסיפים שונות למערכת, ולחץ הברירה הטבעית דוחף את המערכת כולה לכיוון של יעילות תקשורת מוגברת, אם זה משתלם בסביבה הנתונה.</p>

    <p><strong>גורמים שמשפיעים על המסע למורכבות</strong></p>
    <p>מה גורם למערכת תקשורת להפוך למורכבת יותר? הנה כמה דוגמאות:
        <ul>
            <li><strong>סביבה מורכבת:</strong> צורך לתקשר על מגוון רחב של דברים (סוגי מזון, סוגי טורפים, מצבים חברתיים).</li>
            <li><strong>מבנה חברתי:</strong> חיים בקבוצות גדולות או בעלות היררכיה מורכבת דורשים דרכים עדינות ומדויקות לתקשר מעמד, כוונות, ואף רגשות.</li>
            <li><strong>יכולות קוגניטיביות:</strong> מוח גדול ומורכב יותר מאפשר ללמוד סימנים חדשים, לזכור שילובי סימנים, ולהבין משמעויות מופשטות יותר.</li>
        </ul>
        בסימולטור שלנו, <strong>'לחץ סביבתי'</strong> מייצג את שקלול כל הגורמים הללו - עד כמה התקשורת היא כלי קריטי להישרדות והצלחה ברבייה בעולם הספציפי שהגדרתם.</p>

    <p><strong>ומה ההבדל הגדול בינינו לבינם?</strong></p>
    <p>למרות המורכבות המדהימה שמערכות תקשורת בבעלי חיים יכולות להגיע אליה, הן עדיין שונות משפה אנושית בכמה היבטים:
        <ul>
            <li><strong>תחביר (Syntax):</strong> אנחנו משלבים מילים לפי חוקים כדי ליצור משמעויות חדשות ("החתול אכל את הדג" לעומת "הדג אכל את החתול"). בטבע, שילובים כאלה נדירים או מוגבלים מאוד.</li>
            <li><strong>יצירתיות (Productivity):</strong> אנחנו יכולים לייצר אינסוף משפטים ורעיונות חדשים. בעלי חיים מוגבלים יותר לאוסף סימנים קיים או לוריאציות מצומצמות.</li>
             <li><strong>עקירה (Displacement):</strong> אנחנו יכולים לדבר על דברים שאינם נמצאים כאן ועכשיו – העבר, העתיד, דמיונות, דברים מופשטים. תקשורת בעלי חיים לרוב צמודה להקשר המיידי.</li>
        </ul></p>

    <p><strong>זכרו: זהו מודל פשטני!</strong></p>
    <p>הסימולטור הוא כלי חזק להדגמת עקרונות, אך הוא מפשט מאוד את המציאות הביולוגית העשירה. הוא לא מדמה פרטים ספציפיים, אינטראקציות מורכבות, או גנטיקה אמיתית. הוא עוקב אחר ממוצעים באוכלוסייה כדי להראות כיצד ברירה טבעית ומוטציה יכולות להניע שינוי הדרגתי בתכונות כמו מספר סימנים ומורכבותם, וכיצד זה קשור ליעילות התקשורת בסביבה מסוימת. השתמשו בו כדי לקבל אינטואיציה על התהליך, לא כייצוג מדויק של מין ספציפי!</p>
</div>

<style>
    /* General Styling */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Slightly more modern font */
        line-height: 1.7;
        margin: 0; /* Remove default margin */
        padding: 20px;
        direction: rtl;
        text-align: right;
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
        color: #333;
        min-height: 100vh; /* Full viewport height */
        box-sizing: border-box;
    }

    h1, h2, h3 {
        color: #004d40; /* Dark teal */
        text-align: center;
        margin-bottom: 15px;
        font-weight: 600;
    }

    h1 {
        color: #00796b; /* Medium teal */
        margin-bottom: 25px;
        font-weight: 700;
    }

    p {
         margin-bottom: 15px;
         color: #555;
    }

    /* App Containers */
    #simulation-app, #explanation {
        background-color: #ffffff;
        border: 1px solid #b2dfdb; /* Light teal border */
        padding: 25px;
        margin: 20px auto; /* Center blocks */
        max-width: 800px; /* Limit width for readability */
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* Softer, larger shadow */
        transition: transform 0.3s ease-in-out;
    }

     #simulation-app:hover, #explanation:hover {
         /*transform: translateY(-5px); /* Subtle hover effect */
     }


    /* Controls Section */
    .controls {
        display: grid;
        grid-template-columns: auto 1fr auto; /* Label, Input, Value/Desc */
        gap: 12px 15px; /* Row and column gap */
        align-items: center;
        margin-bottom: 25px;
        padding: 20px;
        background-color: #e0f2f7; /* Very light blue */
        border-radius: 8px;
        border: 1px dashed #b3e5fc; /* Dashed border for a softer look */
    }

    .controls label {
        font-weight: 600;
        color: #004d40; /* Dark teal */
        text-align: left; /* Align labels to the left in RTL */
        white-space: nowrap; /* Prevent label wrapping */
    }

     .controls input[type="number"],
     .controls input[type="range"] {
         width: calc(100% - 10px);
         padding: 8px;
         border: 1px solid #b2dfdb;
         border-radius: 5px;
         box-sizing: border-box; /* Include padding in width */
         transition: border-color 0.3s ease;
     }
     .controls input:focus {
         outline: none;
         border-color: #00796b; /* Highlight on focus */
         box-shadow: 0 0 5px rgba(0, 121, 107, 0.3);
     }

     .controls .range-value {
         text-align: right;
         min-width: 40px; /* Ensure space for value */
         font-weight: 600;
         color: #004d40;
     }
    .controls .control-desc {
        grid-column: 1 / -1; /* Span across all columns */
        font-size: 0.9em;
        color: #555;
        margin-top: -8px; /* Pull description closer to input */
        margin-bottom: 5px;
        padding-bottom: 5px;
        border-bottom: 1px dotted #cfd8dc; /* Separator */
    }
     .controls .control-desc:last-child {
         border-bottom: none; /* No border for the last one */
     }


    /* Buttons */
    .interactive-button {
        display: block;
        margin: 20px auto;
        padding: 12px 25px;
        font-size: 17px;
        cursor: pointer;
        background-color: #00796b; /* Medium teal */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s active;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .interactive-button:hover {
        background-color: #004d40; /* Darker teal on hover */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }
     .interactive-button:active {
         transform: translateY(1px); /* Pressed effect */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
     }

    .interactive-button.secondary {
         background-color: #78909c; /* Blue-grey */
         margin-top: 0;
         box-shadow: none;
    }
     .interactive-button.secondary:hover {
         background-color: #546e7a; /* Darker blue-grey */
     }
    .interactive-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }


    /* Simulation Results */
    #simulation-results {
        margin-top: 30px;
        border-top: 1px solid #b2dfdb;
        padding-top: 25px;
    }

     #simulation-results h3 {
         margin-bottom: 20px;
         color: #004d40;
     }

    #simulation-results p {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 20px;
        color: #004d40;
    }

    /* Charts */
    .chart-container {
        margin-bottom: 30px;
        position: relative; /* Needed for absolute positioning of axis labels */
        padding: 15px; /* Add some padding around the chart */
        background-color: #e0f2f7; /* Light background for chart area */
        border-radius: 8px;
        border: 1px solid #b3e5fc;
    }
     .chart-container h4 {
         text-align: right; /* Align chart titles */
         margin-bottom: 10px;
         color: #00796b; /* Medium teal */
         font-size: 1.1em;
         font-weight: 600;
     }

    .chart {
        width: 100%;
        height: 180px; /* Slightly taller charts */
        background-color: #ffffff;
        border: 1px solid #cfd8dc; /* Light grey border */
        margin-top: 10px;
        position: relative;
        overflow: hidden; /* Hide bars outside */
        display: flex;
        align-items: flex-end; /* Bars grow from bottom */
        justify-content: flex-start; /* Bars start from the left */
        padding: 0; /* Remove padding */
        box-sizing: border-box;
        background-image: repeating-linear-gradient(to top, #eceff1, #eceff1 1px, transparent 1px, transparent 20px); /* Horizontal grid lines */
         background-size: 100% 20px; /* Adjust grid line spacing */
    }

    .chart .data-point {
        flex-shrink: 0; /* Prevent shrinking */
        width: 4px; /* Width of each bar */
        margin: 0 0.5px; /* Small gap between bars */
        background-color: steelblue; /* Default color - overridden by JS */
        transition: height 0.5s ease-out; /* Animate height changes */
        /* Height set by JS */
    }

    /* Chart Axis Labels (simplified positioning) */
    .chart-axis-label {
        position: absolute;
        font-size: 0.8em;
        color: #555;
        bottom: 5px;
        left: 50%;
        transform: translateX(-50%);
        pointer-events: none; /* Don't interfere with clicks */
    }
     .chart-axis-label.y-axis-label {
         left: 5px; /* Position on the left */
         bottom: 50%;
         transform: translateY(50%) rotate(-90deg); /* Rotate for Y-axis */
         transform-origin: 0 0; /* Rotate around its corner */
         right: auto; /* Disable right positioning */
         text-align: center;
         width: 100px; /* Give it width to center rotated text */
     }


    /* Explanation Section */
    #explanation {
        display: none; /* Initially hidden */
         border-top: 1px solid #b2dfdb;
         padding-top: 25px;
         margin-top: 0; /* No extra margin if toggled */
    }
    #explanation p {
        margin-bottom: 15px;
        text-align: justify;
         line-height: 1.8;
         color: #444;
    }
     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px; /* RTL list padding */
     }
     #explanation li {
         margin-bottom: 8px;
         color: #444;
     }
    #explanation strong {
        display: block;
        margin-bottom: 8px;
        color: #004d40; /* Dark teal */
        font-size: 1.15em;
        font-weight: 600;
        border-bottom: 1px dotted #b2dfdb;
        padding-bottom: 4px;
    }

    /* Simulation Output */
    #simulation-output {
        white-space: pre-wrap; /* Maintain formatting */
        max-height: 120px; /* Slightly smaller output box */
        overflow-y: auto;
        border: 1px solid #b2dfdb;
        padding: 10px;
        background-color: #f0f4c3; /* Light yellow-green for log */
        margin-top: 20px;
        border-radius: 4px;
        font-size: 0.85em;
        color: #333;
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; /* Monospaced font for log */
    }
     #simulation-output::-webkit-scrollbar {
        width: 8px;
     }
     #simulation-output::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
     }
     #simulation-output::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 4px;
     }
     #simulation-output::-webkit-scrollbar-thumb:hover {
        background: #555;
     }


    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .controls {
            grid-template-columns: 1fr; /* Stack controls vertically */
            gap: 15px;
        }
         .controls label, .controls .range-value, .controls .control-desc {
             grid-column: auto; /* Reset column spanning */
             text-align: right; /* Ensure RTL alignment */
             margin-bottom: 0;
         }
         .controls input[type="number"],
         .controls input[type="range"] {
             width: 100%; /* Full width in stacked layout */
         }
         .controls .range-value {
             width: 100%;
             text-align: left; /* Value might look better left aligned below label */
         }
         .controls .control-desc {
            font-size: 0.8em;
             margin-top: 0;
         }
         .chart .data-point {
             width: 3px; /* Thinner bars on smaller screens */
         }
         body {
             padding: 10px;
         }
         #simulation-app, #explanation {
             padding: 15px;
         }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // --- Get Elements ---
        const populationSizeInput = document.getElementById('populationSize');
        const initialSignalCountInput = document.getElementById('initialSignalCount');
        const initialComplexityInput = document.getElementById('initialComplexity');
        const initialComplexityValueSpan = document.getElementById('initialComplexityValue');
        const selectionPressureInput = document.getElementById('selectionPressure');
        const selectionPressureValueSpan = document.getElementById('selectionPressureValue');
        const mutationRateInput = document.getElementById('mutationRate');
        const mutationRateValueSpan = document.getElementById('mutationRateValue');
        const generationsInput = document.getElementById('generations');
        const startSimulationButton = document.getElementById('startSimulation');
        const currentGenerationSpan = document.getElementById('currentGeneration');
        const signalCountChartDiv = document.getElementById('signalCountChart');
        const complexityChartDiv = document.getElementById('complexityChart');
        const efficiencyChartDiv = document.getElementById('efficiencyChart');
        const simulationOutputDiv = document.getElementById('simulation-output');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        // --- Event Listeners ---

        // Update span values when range inputs change
        initialComplexityInput.addEventListener('input', () => {
            initialComplexityValueSpan.textContent = parseFloat(initialComplexityInput.value).toFixed(1);
        });
        selectionPressureInput.addEventListener('input', () => {
            selectionPressureValueSpan.textContent = parseFloat(selectionPressureInput.value).toFixed(1);
        });
         mutationRateInput.addEventListener('input', () => {
            mutationRateValueSpan.textContent = parseFloat(mutationRateInput.value).toFixed(3); // Show 3 decimal places
        });

        // Set initial display values on load
        initialComplexityValueSpan.textContent = parseFloat(initialComplexityInput.value).toFixed(1);
        selectionPressureValueSpan.textContent = parseFloat(selectionPressureInput.value).toFixed(1);
        mutationRateValueSpan.textContent = parseFloat(mutationRateInput.value).toFixed(3);


        // Toggle Explanation Visibility
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'מה בעצם קורה פה? (הסבר)';
        });

        // Start Simulation Button
        startSimulationButton.addEventListener('click', runSimulation);

        // --- Simulation Data & State ---
        let populationAvgSignalCountHistory = [];
        let populationAvgComplexityHistory = [];
        let populationAvgEfficiencyHistory = [];
        let simulationInterval = null; // To hold the interval ID
        let isSimulationRunning = false;

        // --- Simulation Logic ---
        function runSimulation() {
            if (isSimulationRunning) {
                 // If already running, maybe add a stop feature later or just ignore
                 appendOutput('הסימולציה כבר רצה...');
                 return;
            }

            const populationSize = parseInt(populationSizeInput.value);
            let currentAvgSignalCount = parseFloat(initialSignalCountInput.value);
            let currentAvgComplexity = parseFloat(initialComplexityInput.value);
            const selectionPressure = parseFloat(selectionPressureInput.value);
            const mutationRate = parseFloat(mutationRateInput.value);
            const totalGenerations = parseInt(generationsInput.value);

            // Reset data and UI
            populationAvgSignalCountHistory = [];
            populationAvgComplexityHistory = [];
            populationAvgEfficiencyHistory = [];
            simulationOutputDiv.textContent = ''; // Clear output
            currentGenerationSpan.textContent = '0'; // Reset generation counter
            updateCharts(); // Clear charts visually

            // Initial state
            let currentAvgEfficiency = calculateEfficiency(currentAvgSignalCount, currentAvgComplexity, selectionPressure);

            populationAvgSignalCountHistory.push(currentAvgSignalCount);
            populationAvgComplexityHistory.push(currentAvgComplexity);
            populationAvgEfficiencyHistory.push(currentAvgEfficiency);


            appendOutput(`מתחילים את מסע האבולוציה...`);
            appendOutput(`הגדרות עולם: אוכלוסייה=${populationSize}, סימנים התחלתיים=${currentAvgSignalCount.toFixed(1)}, מורכבות התחלתית=${currentAvgComplexity.toFixed(1)}, לחץ סביבתי=${selectionPressure.toFixed(1)}, קצב שינוי=${mutationRate.toFixed(3)}, משך האבולוציה=${totalGenerations} דורות`);


            // Disable controls and button
             setSimulationState(true);

            // Simulation loop using setInterval
            let generation = 0;
            simulationInterval = setInterval(() => {
                 if (generation >= totalGenerations) {
                    clearInterval(simulationInterval);
                    simulationInterval = null;
                    appendOutput('האבולוציה הסתיימה אחרי ' + totalGenerations + ' דורות.');
                    setSimulationState(false); // Re-enable button and controls
                     updateCharts(); // Final chart update
                    return;
                }

                generation++;
                currentGenerationSpan.textContent = generation;

                // 1. Calculate efficiency based on current traits and pressure
                // Efficiency rewards higher relevant complexity/signals, scaled by pressure.
                 // Let's refine the efficiency calculation slightly for more nuanced behavior.
                const efficiencyPotential = Math.log(currentAvgSignalCount + 1) * Math.log(currentAvgComplexity + 1); // Benefit increases with both signals and complexity
                 const scaledPressure = selectionPressure / 10.0; // Pressure scales the actual benefit

                // Use a sigmoid-like function to cap efficiency and make it sensitive to pressure
                currentAvgEfficiency = 1 / (1 + Math.exp(-0.5 * (efficiencyPotential * scaledPressure - (scaledPressure * 5)))); // Adjust sigmoid center based on pressure


                // 2. Apply Selection Effect
                // Selection pushes traits towards values that increase *future* efficiency,
                // but the strength of this push depends on *current* efficiency and pressure.
                 // High pressure + high efficiency = strong positive selection for traits.
                 // High pressure + low efficiency = strong negative/stabilizing pressure (maybe? or just slow evolution).
                 // Low pressure = weak selection.
                 // Let's simplify: Selection favors traits roughly proportional to (Efficiency * Pressure).
                 const selectionInfluence = currentAvgEfficiency * scaledPressure; // 0 to 1 scale

                 // Selection drives traits towards higher values if selectionInfluence is high
                 // Let's assume a max desirable signal count (e.g., 30) and complexity (e.g., 8) in a high-pressure ideal world.
                 // Selection will push towards these, proportional to selectionInfluence.
                 const targetSignalCount = 30;
                 const targetComplexity = 8;

                 // The *direction* of selection effect depends on whether the current value is below the target
                 let selectionEffectOnSignals = (targetSignalCount - currentAvgSignalCount) * selectionInfluence * 0.005; // Small push
                 let selectionEffectOnComplexity = (targetComplexity - currentAvgComplexity) * selectionInfluence * 0.01; // Complexity evolves slower, but maybe larger steps


                // 3. Apply Mutation Effect
                // Random change based on mutation rate
                let mutationEffectOnSignals = (Math.random() - 0.5) * mutationRate * 10; // Larger random steps for signals
                let mutationEffectOnComplexity = (Math.random() - 0.5) * mutationRate * 5; // Smaller random steps for complexity

                // 4. Update Traits
                currentAvgSignalCount += selectionEffectOnSignals + mutationEffectOnSignals;
                currentAvgComplexity += selectionEffectOnComplexity + mutationEffectOnComplexity;

                // 5. Clamp values within reasonable biological bounds
                currentAvgSignalCount = Math.max(0.5, Math.min(50, currentAvgSignalCount)); // Signals must be at least 0.5 (represent having *some* signals)
                currentAvgComplexity = Math.max(0, Math.min(10, currentAvgComplexity)); // Complexity 0-10

                 // Re-calculate efficiency *after* trait update for next generation's starting point (optional, or just use the one calculated at the start of the generation loop)
                 // Let's stick to calculating efficiency at the start of the loop to show its effect *on* the trait evolution in that generation.


                // 6. Store results for the generation
                populationAvgSignalCountHistory.push(currentAvgSignalCount);
                populationAvgComplexityHistory.push(currentAvgComplexity);
                populationAvgEfficiencyHistory.push(currentAvgEfficiency); // Store efficiency calculated based on traits *before* this generation's changes

               // Optional: Log progress occasionally
                if (generation % 50 === 0 || generation === 1) {
                   appendOutput(`דור ${generation}: סימנים=${currentAvgSignalCount.toFixed(2)}, מורכבות=${currentAvgComplexity.toFixed(2)}, יעילות=${currentAvgEfficiency.toFixed(2)}`);
                }

                // 7. Update Charts
                updateCharts(); // Update all charts

            }, 60); // Run a generation every 60ms for smoother animation

        }

        // Function to update the state of simulation controls and button
        function setSimulationState(isRunning) {
            isSimulationRunning = isRunning;
            startSimulationButton.disabled = isRunning;
            startSimulationButton.textContent = isRunning ? 'האבולוציה בעיצומה...' : 'התחל את האבולוציה!';
            // Optionally disable other controls
            populationSizeInput.disabled = isRunning;
            initialSignalCountInput.disabled = isRunning;
            initialComplexityInput.disabled = isRunning;
            selectionPressureInput.disabled = isRunning;
            mutationRateInput.disabled = isRunning;
            generationsInput.disabled = isRunning;
        }


        // Update all charts
        function updateCharts() {
            updateChart(signalCountChartDiv, populationAvgSignalCountHistory, '#1a759f'); // Deep sky blue
            updateChart(complexityChartDiv, populationAvgComplexityHistory, '#f77f00'); // Vivid orange
            updateChart(efficiencyChartDiv, populationAvgEfficiencyHistory, '#4caf50'); // Green
        }

        // Function to draw/update bars in a chart div with animation
        function updateChart(chartDiv, data, color) {
            chartDiv.innerHTML = ''; // Clear previous points - this allows CSS transitions to work on subsequent additions

            if (data.length === 0) return;

            // Determine max visible value for scaling (consider history and input max)
            const maxPossibleSignal = 50;
            const maxPossibleComplexity = 10;
            const maxPossibleEfficiency = 1;

            let maxVal;
            if (chartDiv === signalCountChartDiv) maxVal = maxPossibleSignal;
            else if (chartDiv === complexityChartDiv) maxVal = maxPossibleComplexity;
            else if (chartDiv === efficiencyChartDiv) maxVal = maxPossibleEfficiency;
            else maxVal = Math.max(...data); // Fallback


            const chartHeight = chartDiv.clientHeight; // Get actual height
            const chartWidth = chartDiv.clientWidth; // Get actual width
            const maxBars = Math.floor(chartWidth / 4.5); // Max bars that fit with 4px width + 0.5px margin

            // Show only the last maxBars data points if history is longer
            const dataToDisplay = data.slice(-maxBars);


            // Calculate bar width based on number of bars displayed
            const barWidth = Math.max(1, (chartWidth / dataToDisplay.length) - 1); // Bar width minus gap


            dataToDisplay.forEach(value => {
                const point = document.createElement('div');
                point.classList.add('data-point');
                point.style.backgroundColor = color;

                 // Scale height based on value relative to max possible value
                 // Scale to 0%-100% of container height
                const scaledHeight = (value / maxVal) * 100;

                point.style.height = `${scaledHeight}%`;
                point.style.width = `${barWidth}px`; // Set calculated width
                point.style.marginRight = '1px'; // Small gap
                point.style.marginLeft = '0'; // Ensure no left margin
                point.style.borderRight = 'none'; // Remove potential border used for gap

                chartDiv.appendChild(point);
            });
        }

        // Function to append messages to the output box
        function appendOutput(message) {
             const line = document.createElement('div');
             line.textContent = `[${new Date().toLocaleTimeString()}] ${message}`; // Add timestamp
             simulationOutputDiv.appendChild(line);
            simulationOutputDiv.scrollTop = simulationOutputDiv.scrollHeight; // Auto-scroll to bottom
        }

         // --- Initial Setup ---
         updateCharts(); // Render empty charts on load
         setSimulationState(false); // Ensure controls are enabled initially


    });
</script>
```