---
title: "הקסם של שעון הקוורץ: איך זמן נמדד בגביש?"
english_slug: how-does-quartz-measure-time
category: "פיזיקה"
tags:
  - קוורץ
  - שעון
  - גבישים
  - תנודות
  - פיאזואלקטריות
  - דיוק
---
# הקסם של שעון הקוורץ: איך זמן נמדד בגביש?

שעוני קוורץ מקיפים אותנו, מהשעון האלגנטי על פרק היד ועד למוח האלקטרוני שבסמארטפון. הדיוק שלהם נראה כמעט קסם, אבל הסוד טמון בגביש צנוע למראה – הקוורץ. בואו נצלול לתוך הגביש הזוהר הזה ונראה איך הוא הופך תנודות זעירות למדידת זמן אולטימטיבית!

<div class="quartz-app-container">
    <div class="app-area">
        <h2>גלו את ליבת שעון הקוורץ</h2>
        <p class="intro-text">הפעילו את המתח וצפו כיצד גביש הקוורץ האנרגטי יוצר אות חשמלי מדויק!</p>

        <div class="simulation-area">
            <div class="crystal-model interactive-panel">
                <h3>גביש הקוורץ הפועם</h3>
                <div class="lattice-container">
                     <!-- More abstract, stylized representation -->
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                    <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                     <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                     <div class="atom si-atom"></div>
                    <div class="atom o-atom"></div>
                </div>
                <div class="electric-field-overlay" id="electricField"></div>
                <p class="panel-hint" id="crystalHint">כשהמתח מופעל, הגביש מתעוות ורוטט בתדר קבוע.</p>
            </div>
            <div class="circuit-elements interactive-panel">
                <h3>המעגל האלקטרוני</h3>
                 <div class="circuit-diagram">
                    <span class="component battery" title="מקור מתח">🔋</span>
                    <span class="wire w1"></span>
                    <span class="component crystal-symbol" title="גביש קוורץ">💎</span>
                    <span class="wire w2"></span>
                    <span class="component oscillator" title="אוסצילטור - שומר על הרטט">🔄</span>
                     <span class="wire w3"></span>
                    <span class="component counter" title="מונה - סופר את התנודות">🔢</span>
                     <span class="wire w4"></span>
                    <span class="component display" title="תצוגת זמן">⏱️</span>
                </div>
                 <button id="activateButton" class="action-button">🔌 הפעל מתח! ⚡</button>
                 <p class="panel-hint" id="circuitHint">המעגל מפעיל את הגביש ומשתמש באות שלו.</p>
            </div>
        </div>
        <div class="graph-area interactive-panel">
            <h3>האות החשמלי: פעימות הזמן</h3>
            <canvas id="voltageGraph"></canvas>
            <p class="panel-hint" id="graphHint">גרף המתח החשמלי היציב שנוצר ע"י הגביש.</p>
        </div>
         <div class="control-area">

         </div>
    </div>
</div>

<button id="toggleExplanation" class="explanation-toggle-button">הצג לי את הסודות! (הסבר מפורט)</button>

<div id="explanation" style="display: none;">
    <h2>הסבר עמוק: מאחורי הקלעים של הדיוק</h2>
    <p>שעוני קוורץ הם פלא טכנולוגי קטן שמבוסס על תכונה יוצאת דופן של גביש הקוורץ הטבעי (סיליקון דו-חמצני, SiO2).</p>

    <h3>מבנה קסום ויציב</h3>
    <p>קוורץ אינו סתם אבן. זהו גביש בעל מבנה אטומי פנימי מסודר להפליא, בו אטומי סיליקון וחמצן קשורים זה לזה בתבנית קבועה וחוזרת. הסדר הזה הוא המפתח ליציבות שלו.</p>

    <h3>האפקט הפיאזואלקטרי: הלב הפועם</h3>
    <p>זו התכונה הגאונית של הקוורץ: הוא פיאזואלקטרי. זה אומר שהוא יכול להמיר אנרגיה חשמלית לאנרגיה מכנית, ולהפך:</p>
    <ul>
        <li>**חשמל לתנועה:** כשמפעילים מתח חשמלי על הגביש, הקשרים האטומיים נדחסים או נמתחים קלות, וגורמים לגביש כולו לשנות את צורתו באופן זעיר.</li>
        <li>**תנועה לחשמל:** כשמפעילים לחץ מכני על הגביש (מעוותים אותו), זה משנה את פיזור המטענים החשמליים בתוכו ויוצר מתח חשמלי קטן בקצותיו.</li>
    </ul>
    <p>האפקט הזה הוא דו-כיווני, וזו הנקודה הקריטית!</p>

    <h3>רטט ברזוננס: התדר המושלם</h3>
    <p>שעון הקוורץ מנצל את האפקט הפיאזואלקטרי ליצירת "פעימה" אלקטרונית יציבה להפליא. מחברים את הגביש למעגל אלקטרוני שמפעיל עליו מתח. המתח גורם לגביש להתכווץ. כשהוא מתכווץ, הוא מייצר מתח חשמלי משלו, שמתנגש במתח של המעגל. המעגל מתוכנן כך שהאינטראקציה הזו גורמת לגביש להיכנס למצב של רטט מכני קבוע ומהיר מאוד - בתדר הרזוננס הטבעי שלו. זה דומה לדחיפת נדנדה בדיוק בזמן הנכון כדי לשמור על התנועה. התדר הזה נקבע על ידי גודלו, צורתו ואופן החיתוך של הגביש, והוא יציב להפליא.</p>

    <h3>ספירת הפעימות: איך הופכים רטט לזמן</h3>
    <p>כל רטט מכני של הגביש יוצר, דרך האפקט הפיאזואלקטרי, פעימה חשמלית זעירה בתדר זהה. האות החשמלי המחזורי הזה מועבר למעגל אלקטרוני אחר שנקרא "מונה". המונה פשוט סופר את הפעימות. כל מספר קבוע וידוע מראש של פעימות (בשעוני יד רבים זה 32,768, או 2 בחזקת 15) נחשב ליחידת זמן אחת - למשל, שנייה אחת. המונה מעביר את המידע הזה למנגנון שמזיז את המחוגים או מציג את השעה בצג דיגיטלי.</p>

    <h3>למה זה כל כך מדויק?</h3>
    <p>הדיוק הפנומנלי של שעוני קוורץ נובע מהיציבות המדהימה של תדר הרטט של הגביש. מבנה הקוורץ כמעט אינו מושפע משינויים קטנים בטמפרטורה או בלחץ, בניגוד למנגנונים מכניים שמושפעים מקפיצים וגלגלי שיניים. התדר היציב הזה מספק בסיס מדידה אמין שאינו סוטה בקלות, ולכן שעון הקוורץ הפשוט מדויק בהרבה משעונים מכניים מורכבים ויקרים.</p>
</div>

<script>
    const activateButton = document.getElementById('activateButton');
    const latticeContainer = document.querySelector('.lattice-container');
    const electricFieldOverlay = document.getElementById('electricField');
    const crystalHint = document.getElementById('crystalHint');
    const circuitHint = document.getElementById('circuitHint');
    const graphHint = document.getElementById('graphHint');
    const voltageGraphCanvas = document.getElementById('voltageGraph');
    const toggleExplanationButton = document.getElementById('toggleExplanation');
    const explanationDiv = document.getElementById('explanation');
    const ctx = voltageGraphCanvas.getContext('2d');
    const circuitWires = document.querySelectorAll('.circuit-diagram .wire');
    const circuitCrystalSymbol = document.querySelector('.circuit-diagram .crystal-symbol');

    let isVibrating = false;
    let graphAnimationFrame = null;
    let graphStartTime = null;
    const graphDuration = 2000; // Duration for one cycle of the wave animation in ms

    // Set initial canvas size - make it responsive
    const resizeCanvas = () => {
        voltageGraphCanvas.width = voltageGraphCanvas.parentElement.clientWidth - 30; // Adjust for padding
        voltageGraphCanvas.height = 120;
        if (!isVibrating) {
             drawStaticGraph(); // Redraw initial state if not vibrating
        }
    };
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas(); // Initial call

    // Function to draw a static baseline
    function drawStaticGraph() {
        ctx.clearRect(0, 0, voltageGraphCanvas.width, voltageGraphCanvas.height);
        ctx.strokeStyle = '#a0a0a0'; // Lighter gray for static
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, voltageGraphCanvas.height / 2);
        ctx.lineTo(voltageGraphCanvas.width, voltageGraphCanvas.height / 2);
        ctx.stroke();
    }

    // Function to draw a sine wave
    function drawSineWave(elapsedTime) {
        ctx.clearRect(0, 0, voltageGraphCanvas.width, voltageGraphCanvas.height);
        ctx.strokeStyle = '#1e88e5'; // Blue color for active signal
        ctx.lineWidth = 2;

        ctx.beginPath();
        ctx.moveTo(0, voltageGraphCanvas.height / 2);

        const frequency = 8; // Cycles visible on screen
        const amplitude = voltageGraphCanvas.height / 3; // Amplitude
        const phaseShift = (elapsedTime / graphDuration) * Math.PI * 2; // Shift phase over time for animation

        for (let x = 0; x < voltageGraphCanvas.width; x++) {
            const angle = (x / voltageGraphCanvas.width) * Math.PI * 2 * frequency + phaseShift;
            const y = voltageGraphCanvas.height / 2 - Math.sin(angle) * amplitude; // Y-axis is inverted in canvas
            ctx.lineTo(x, y);
        }
        ctx.stroke();

         // Draw axis line
        ctx.strokeStyle = '#a0a0a0';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, voltageGraphCanvas.height / 2);
        ctx.lineTo(voltageGraphCanvas.width, voltageGraphCanvas.height / 2);
        ctx.stroke();
    }

    // Animation loop for the graph
    function animateGraph(timestamp) {
        if (!graphStartTime) graphStartTime = timestamp;
        const timeElapsed = timestamp - graphStartTime;

        if (isVibrating) {
             drawSineWave(timeElapsed);
        } else {
            // If stopped, clear the graph or draw static line after a brief moment
            // We stop the animation loop explicitly now, so this else might not be strictly needed here
        }

        if(isVibrating) { // Keep animating only if still vibrating
            graphAnimationFrame = requestAnimationFrame(animateGraph);
        }
    }

    // Circuit animation function
    function animateCircuit(active) {
        if (active) {
            circuitWires.forEach(wire => wire.classList.add('active'));
            circuitCrystalSymbol.classList.add('active');
        } else {
             circuitWires.forEach(wire => wire.classList.remove('active'));
             circuitCrystalSymbol.classList.remove('active');
        }
    }


    activateButton.addEventListener('click', () => {
        isVibrating = !isVibrating;
        if (isVibrating) {
            activateButton.textContent = '🛑 עצור שעון';
            activateButton.classList.remove('action-button');
            activateButton.classList.add('stop-button');

            latticeContainer.classList.add('vibrating');
            electricFieldOverlay.classList.add('active');

            animateCircuit(true);

            crystalHint.textContent = 'צפו באטומים רוטטים בתדר מדהים!';
            circuitHint.textContent = 'המעגל מפעיל את הגביש ושומע את פעימותיו!';
            graphHint.textContent = 'הנה האות החשמלי היציב שהגביש מייצר!';

            // Start animation loop if not already running
            if (!graphAnimationFrame) {
                 graphStartTime = null; // Reset start time for smooth start
                 animateGraph(performance.now()); // Use performance.now() for high precision time
            }

        } else {
            activateButton.textContent = '🔌 הפעל מתח! ⚡';
             activateButton.classList.remove('stop-button');
            activateButton.classList.add('action-button');

            latticeContainer.classList.remove('vibrating');
            electricFieldOverlay.classList.remove('active');

            animateCircuit(false);

            crystalHint.textContent = "כשהמתח מופעל, הגביש מתעוות ורוטט בתדר קבוע.";
            circuitHint.textContent = 'המעגל מפעיל את הגביש ומשתמש באות שלו.';
            graphHint.textContent = 'גרף המתח החשמלי היציב שנוצר ע"י הגביש.';

            // Stop the animation loop and clear/reset graph
             cancelAnimationFrame(graphAnimationFrame);
             graphAnimationFrame = null;
             graphStartTime = null;
             drawStaticGraph(); // Draw static line when stopped
        }
    });

    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'צמצם הסבר' : 'הצג לי את הסודות! (הסבר מפורט)';
         toggleExplanationButton.classList.toggle('active-explanation', isHidden);
    });

     // Initial state drawing
    drawStaticGraph();

</script>

<style>
    /* General Styles */
    .quartz-app-container {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        max-width: 750px;
        background-color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        color: #333;
        overflow: hidden; /* Ensure things stay inside */
    }

    .app-area h2 {
        text-align: center;
        color: #0d47a1; /* Dark Blue */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
    }

    .intro-text {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
        font-size: 1.1em;
        line-height: 1.6;
    }

    .simulation-area {
        display: flex;
        justify-content: space-between;
        align-items: stretch; /* Align items to stretch vertically */
        margin-bottom: 20px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
        gap: 20px; /* Space between flex items */
    }

    .interactive-panel {
        background-color: #e3f2fd; /* Lightest Blue */
        border: 1px solid #bbdefb; /* Lighter Blue */
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        flex: 1; /* Allow panels to grow */
        min-width: 280px; /* Ensure minimum width before wrapping */
        display: flex; /* Use flex for inner layout */
        flex-direction: column;
        align-items: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
         position: relative; /* Needed for electric field overlay */
         overflow: hidden;
    }

     .interactive-panel h3 {
        color: #1565c0; /* Medium Blue */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.3em;
     }

    .panel-hint {
        font-size: 0.95em;
        color: #5e35b1; /* Deep Purple */
        margin-top: auto; /* Push hint to the bottom */
        min-height: 1.5em; /* Reserve space */
        line-height: 1.4;
    }

    /* Crystal Model Specifics */
    .crystal-model {
        justify-content: space-between; /* Space between h3, lattice, and hint */
    }

    .lattice-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr); /* More grid columns */
        gap: 8px; /* Increase gap */
        width: 100%;
        max-width: 220px; /* Limit grid size */
        margin: 15px auto;
        background-color: #ffffff;
        border: 2px solid #0288d1; /* Cyan border */
        padding: 12px;
        border-radius: 8px;
        position: relative; /* Needed for atom positioning/animation */
         box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.05);
         overflow: hidden; /* Hide potential overflow */
    }

    .atom {
        width: 22px; /* Larger atoms */
        height: 22px;
        border-radius: 50%;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        font-weight: bold;
        color: white;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        transition: transform 0.08s ease-in-out; /* Fast transition for subtle movement */
         cursor: pointer; /* Indicate interactivity */
    }

    .si-atom {
        background: linear-gradient(to bottom right, #4fc3f7, #039be5); /* Light Blue gradient */
        border: 1px solid #0277bd;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

     .o-atom {
        background: linear-gradient(to bottom right, #ffb74d, #fb8c00); /* Orange gradient */
        border: 1px solid #f57f17;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .lattice-container.vibrating .atom {
         /* More complex vibration */
         animation: subtle-vibrate 0.05s infinite alternate ease-in-out; /* Faster, smoother vibration */
    }

     @keyframes subtle-vibrate {
        0% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(0.5px, 0.5px) rotate(0.5deg); }
        100% { transform: translate(-0.5px, -0.5px) rotate(-0.5deg); }
    }

    .electric-field-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(33,150,243,0.2) 0%, rgba(255,255,255,0) 70%); /* Fading blue glow */
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
         z-index: 1; /* Above atoms */
    }

     .electric-field-overlay.active {
        opacity: 1;
        animation: field-pulse 1.5s infinite ease-out;
     }

     @keyframes field-pulse {
         0% { transform: scale(0.9); opacity: 0.7; }
         50% { transform: scale(1); opacity: 1; }
         100% { transform: scale(0.9); opacity: 0.7; }
     }


    /* Circuit Elements Specifics */
    .circuit-elements {
        justify-content: space-between;
    }

    .circuit-diagram {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 15px 0;
        font-size: 2em; /* Larger emojis */
        color: #333;
         flex-wrap: wrap; /* Allow circuit line to wrap */
         gap: 5px; /* space between circuit components */
    }

    .component {
        padding: 0 5px; /* Space around components */
         transition: transform 0.3s ease-in-out;
    }

    .crystal-symbol {
         color: #0288d1; /* Cyan color for crystal */
         font-size: 1.8em;
         transition: transform 0.2s ease-in-out, color 0.2s ease-in-out;
    }

    .crystal-symbol.active {
        animation: pulse-scale 0.8s infinite ease-in-out alternate;
         color: #ff6f00; /* Orange when active */
    }

     @keyframes pulse-scale {
         0% { transform: scale(1); }
         100% { transform: scale(1.1); }
     }

     .wire {
         display: inline-block;
         width: 30px; /* Length of wire segments */
         height: 2px;
         background-color: #90a4ae; /* Gray wire */
         margin: 0 2px;
         position: relative;
         overflow: hidden;
     }

    .wire.active {
        background: linear-gradient(to right, #90a4ae 0%, #4caf50 50%, #90a4ae 100%); /* Green pulse effect */
        animation: flow 1s infinite linear;
         background-size: 200% 100%; /* Make gradient wider than wire */
    }

     @keyframes flow {
         0% { background-position: 200% 0; }
         100% { background-position: -200% 0; }
     }


    .action-button, .stop-button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
        margin-top: 15px;
        min-height: 50px; /* Prevent size changes on text change */
    }

    .action-button:hover {
        background-color: #45a049;
        transform: translateY(-1px);
    }

    .action-button:active {
         transform: translateY(1px);
         box-shadow: 0 1px 5px rgba(0,0,0,0.3);
    }

     .stop-button {
         background-color: #e53935; /* Red */
     }
      .stop-button:hover {
        background-color: #d32f2f;
        transform: translateY(-1px);
    }

    .stop-button:active {
         transform: translateY(1px);
         box-shadow: 0 1px 5px rgba(0,0,0,0.3);
    }

    /* Graph Area Specifics */
    .graph-area {
        margin-top: 20px;
        padding: 20px;
        background-color: #e8f5e9; /* Lightest Green */
        border: 1px solid #c8e6c9; /* Lighter Green */
        border-radius: 10px;
        text-align: center;
        width: calc(100% - 40px); /* Adjust width for padding */
         box-sizing: border-box; /* Include padding in width */
    }

    #voltageGraph {
        border: 1px solid #a5d6a7; /* Medium Green border */
        margin-top: 10px;
        background-color: #ffffff; /* White background for graph area */
        border-radius: 5px;
    }


    /* Explanation Toggle Button */
    .explanation-toggle-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        background-color: #007bff; /* Blue */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }

    .explanation-toggle-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
      .explanation-toggle-button:active {
         transform: translateY(1px);
         box-shadow: 0 1px 5px rgba(0,0,0,0.3);
    }

    .explanation-toggle-button.active-explanation {
        background-color: #673ab7; /* Purple when explanation is open */
    }
     .explanation-toggle-button.active-explanation:hover {
         background-color: #512da8;
     }


    /* Explanation Area Styles */
    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: #f5f5f5; /* Light gray */
        max-width: 750px;
        margin-left: auto;
        margin-right: auto;
        direction: rtl;
        text-align: right;
        line-height: 1.7;
         box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    #explanation h2 {
        color: #0d47a1;
        text-align: right;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.6em;
    }

     #explanation h3 {
        color: #1565c0;
        text-align: right;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.3em;
         border-bottom: 1px solid #bbdefb;
         padding-bottom: 5px;
    }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px;
        margin-bottom: 15px;
         padding-right: 0;
    }

    #explanation li {
        margin-bottom: 8px;
        line-height: 1.5;
    }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .simulation-area {
            flex-direction: column;
            align-items: center;
        }

        .interactive-panel {
            min-width: 95%; /* Allow panels to take more width on small screens */
        }

        .lattice-container {
            grid-template-columns: repeat(6, 1fr); /* More columns for smaller atoms */
            gap: 4px;
            max-width: none; /* No max width */
            width: 100%;
             padding: 8px;
        }

        .atom {
            width: 18px;
            height: 18px;
        }

        .circuit-diagram {
             font-size: 1.5em; /* Smaller emojis */
             flex-direction: column; /* Stack components vertically */
             gap: 8px;
        }

         .wire {
             width: 2px; /* Vertical wires */
             height: 20px; /* Height of vertical wire segments */
         }

         .wire.active {
            background: linear-gradient(to bottom, #90a4ae 0%, #4caf50 50%, #90a4ae 100%); /* Green pulse effect */
             background-size: 100% 200%;
             animation: flow-vertical 1s infinite linear;
         }
         @keyframes flow-vertical {
            0% { background-position: 0 200%; }
            100% { background-position: 0 -200%; }
        }


        .graph-area {
             width: 100%; /* Take full width on small screens */
             padding: 15px;
             box-sizing: border-box;
        }

        #voltageGraph {
            width: 100%;
        }
    }
</style>
---