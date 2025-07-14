---
title: "מציית או מתנגד? הדילמה האתית של ניסוי מילגרם"
english_slug: obey-or-resist-milgram-experiment-ethical-dilemma
category: "פסיכולוגיה"
tags: [פסיכולוגיה חברתית, ניסוי מילגרם, ציות לסמכות, אתיקה בניסויים, דילמות מוסריות]
---
# מציית או מתנגד? הדילמה המצמררת של ניסוי מילגרם

האם הייתם מסוגלים לגרום כאב לזולת רק כי קיבלתם פקודה? גלו כמה קשה להתנגד לסמכות, גם כשהמצפון זועק. סימולציה זו תבחן את גבולות הציות והמוסר האנושי, בהשראת ניסוי מילגרם המפורסם. האם תצייתו עד הסוף, או שתעצרו בזמן?

<div id="simulation-container" class="milgram-simulation">
    <div class="simulation-header">
        <h2>הסימולציה: התפקיד שלך כ"מורה"</h2>
        <p>עליך להעניק "שוקים חשמליים" ל"לומד" (שחקן) בכל פעם שהוא טועה במשימת זיכרון. דרגת המתח עולה עם כל טעות.</p>
    </div>

    <div class="experiment-area">
        <div id="experimenter-area" class="role-area experimenter">
            <div class="role-label">החוקר</div>
            <div id="experimenter-text" class="role-text">אנא התחל בלחיצה על 'תן שוק' לרמה הראשונה.</div>
        </div>

        <div class="machine-learner-area">
             <div id="shock-machine" class="machine">
                 <div class="machine-label">מכשיר השוק</div>
                 <div id="shock-bar-container">
                     <div id="shock-bar" class="shock-level-0"></div>
                 </div>
                  <div id="shock-display" class="display">רמת שוק: <span id="current-voltage">--</span> וולט</div>
                  <div class="level-markers">
                      <span>15V</span><span>75V</span><span>150V</span><span>250V</span><span>350V</span><span>450V</span>
                  </div>
             </div>

            <div id="learner-area" class="role-area learner">
                <div class="role-label">ה"לומד"</div>
                <div id="learner-icon" class="learner-icon">😟</div>
                <div id="learner-reaction" class="role-text">...ממתין להוראות...</div>
            </div>
        </div>
    </div>

    <div class="controls">
        <button id="deliver-shock-btn" class="action-button primary">תן שוק</button>
        <button id="stop-experiment-btn" class="action-button secondary" disabled>הפסק את הניסוי</button>
    </div>
</div>

<div id="results-area" class="milgram-simulation hidden">
    <div class="results-header">
        <h2>תוצאות ההתנסות שלך</h2>
    </div>
    <div class="results-content">
        <p id="final-shock-level-text"></p>
        <div id="your-level-marker"></div>
        <div class="milgram-comparison-bar">
             <div class="comparison-segment" style="width: 5%">0-150V</div>
             <div class="comparison-segment" style="width: 30%">150-300V</div>
             <div class="comparison-segment" style="width: 30%">300-450V</div>
             <div class="comparison-segment max-level" style="width: 35%;">450V (65%)</div>
             <div class="comparison-label">השוואה לניסוי מילגרם המקורי</div>
        </div>
        <p id="comparison-to-milgram-text"></p>
    </div>
</div>

<div class="explanation-toggle">
    <button id="toggle-explanation-btn">מעוניינים להבין? לחצו לקרוא עוד על ניסוי מילגרם והמסקנות</button>
</div>


<div id="explanation-area" class="milgram-explanation hidden">
    <div class="explanation-content">
        <h2>רקע: כוחו של הציות</h2>
        <p>חברות מתבססות על ציות לסמכות - מהורים, מורים, מנהלים, אנשי חוק. ציות מאפשר סדר ותיאום, אך מה קורה כשהוראות הסמכות מתנגשות עם המצפון? זו השאלה המרכזית שניסוי מילגרם ניסה לבחון, לאחר שאלפים צייתו לפקודות שגרמו סבל בל יתואר בשואה. האם זו הייתה תכונה ייחודית לגרמנים, או כוח סמכות כלל-אנושי?</p>

        <h2>ניסוי מילגרם: המטרה המקורית והממצאים המזעזעים</h2>
        <p>הפסיכולוג סטנלי מילגרם גייס "משתתפים" למחקר לכאורה על למידה. באמצעות הטעיה מתוחכמת, המשתתף האמיתי הוקצה תמיד לתפקיד ה"מורה", ונצטווה להעניק שוקים חשמליים (מדומים!) ל"לומד" (שחקן) בכל טעות. מכשיר השוק כלל 30 מתגים, מ-15 וולט ועד 450 וולט, עם כותרות מדאיגות כמו "סכנה: שוק חמור" ו-"XXX".</p>
        <p>כשה"מורה" היסס, ה"חוקר" (שחקן נוסף) הפעיל לחץ בארבעה "פרודים" (הנחיות כפייה): "בבקשה המשך", "הניסוי דורש שתמשיך", "זה חיוני לחלוטין שתמשיך", ו"אין לך ברירה, עליך להמשיך". התוצאות זעזעו את עולם הפסיכולוגיה: בניגוד לציפיות המומחים, **כ-65% מהמשתתפים המשיכו לתת שוקים עד לרמה המקסימלית של 450 וולט!** אף משתתף לא עצר לפני 300 וולט, השלב בו ה"לומד" הפסיק להגיב כלל.</p>

        <h3>גורמים שהשפיעו על עוצמת הציות:</h3>
        <ul>
            <li>**קירבה לקורבן:** כשה"לומד" היה קרוב יותר, הציות ירד. כשהיה צורך במגע פיזי, הציות ירד דרמטית.</li>
            <li>**קירבה לסמכות:** כשה"חוקר" היה רחוק יותר (בטלפון), הציות ירד.</li>
            <li>**לגיטימציה/יוקרה:** הניסויים בייל זכו לציות גבוה יותר מאשר במשרדים פשוטים, אך ההבדל לא היה דרמטי כפי שניתן היה לחשוב.</li>
            <li>**נוכחות מתנגדים:** כשהיו "מורים" נוספים שהתנגדו, רמת הציות צנחה באופן דרמטי (רק 10% המשיכו עד הסוף).</li>
        </ul>

        <h3>הביקורת האתית והשפעת הניסוי:</h3>
        <p>הניסוי ספג ביקורת קשה על גרימת מצוקה פסיכולוגית למשתתפים (מתח, הזעה, רעד) ועל ההטעיה הנרחבת. למרות זאת, השפעתו עצומה. הוא הדגים באופן כואב את כוחה של הסמכות הסיטואציונית על חשבון המוסר האישי, והוביל לשינויים יסודיים בסטנדרטים האתיים במחקר פסיכולוגי, עם דגש על הסכמה מדעת וזכות פרישה בכל עת.</p>
        <p>תובנות מילגרם רלוונטיות עד היום להבנת ציות עיוור במגוון הקשרים - מצבא ועד מקום עבודה, ומזכירות לנו את החשיבות הקריטית בחשיבה ביקורתית ועמידה על עקרונות מוסריים גם תחת לחץ סמכותי.</p>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    body {
        font-family: 'Heebo', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #f4f7f6;
        color: #333;
    }

    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 700;
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0;
    }

    h2 {
         font-size: 1.8em;
         margin-bottom: 15px;
    }

    h3 {
        font-size: 1.3em;
        margin-top: 25px;
        margin-bottom: 10px;
        color: #34495e;
        border-bottom: 2px solid #bdc3c7;
        padding-bottom: 5px;
    }

    p {
        margin-bottom: 15px;
    }

    ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Adjust for RTL */
    }

    li {
        margin-bottom: 8px;
    }

    .milgram-simulation, .milgram-explanation {
        border: 1px solid #dcdcdc;
        padding: 30px;
        margin-bottom: 30px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        transition: all 0.5s ease-in-out;
    }

    .milgram-simulation {
        background: linear-gradient(to bottom, #ecf0f1, #ffffff);
    }

    .simulation-header p {
        text-align: center;
        font-size: 1.1em;
        color: #555;
    }

    .experiment-area {
        display: flex;
        flex-direction: column;
        gap: 25px;
        margin-top: 20px;
    }

    .role-area {
        border: 1px solid #bdc3c7;
        padding: 15px;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }

    .role-label {
        font-weight: bold;
        margin-bottom: 8px;
        padding-bottom: 5px;
        border-bottom: 1px solid #eee;
    }

    .role-text {
        min-height: 1.5em;
        font-size: 1.1em;
    }

    .experimenter .role-label { color: #2980b9; }
    .experimenter .role-text { color: #3498db; font-weight: 500; }

    .learner .role-label { color: #e67e22; }
    .learner .role-text { color: #d35400; font-style: italic; }
    .learner-icon {
         font-size: 2.5em;
         text-align: center;
         margin-bottom: 10px;
         transition: transform 0.3s ease, color 0.3s ease;
    }

    .machine-learner-area {
        display: flex;
        flex-direction: column; /* Stack on small screens */
        gap: 25px;
    }

    @media (min-width: 768px) {
         .experiment-area {
             flex-direction: row;
             align-items: flex-start;
         }
         .role-area.experimenter {
             flex-basis: 30%;
         }
         .machine-learner-area {
             flex-basis: 70%;
             flex-direction: row; /* Side by side on larger screens */
             align-items: flex-start;
             gap: 25px;
         }
         .machine, .learner {
             flex: 1; /* Distribute space */
         }
    }


    .machine {
        border: 2px solid #34495e;
        padding: 20px;
        border-radius: 10px;
        background-color: #5d6d7e;
        color: #ecf0f1;
        text-align: center;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.3);
        position: relative;
    }

    .machine-label {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    #shock-bar-container {
        width: 80%;
        height: 25px;
        background-color: #bdc3c7;
        margin: 0 auto 15px auto;
        border-radius: 5px;
        overflow: hidden;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
    }

    #shock-bar {
        height: 100%;
        width: 0%;
        background: linear-gradient(to right, #2ecc71, #f1c40f, #e67e22, #e74c3c, #c0392b, #8e44ad);
        transition: width 0.5s ease-out, background-color 0.5s ease;
        position: relative;
    }

    .level-markers {
        display: flex;
        justify-content: space-between;
        width: 80%;
        margin: 0 auto 10px auto;
        font-size: 0.8em;
        color: #eee;
    }
     .level-markers span {
        position: relative;
        width: calc(100% / 5); /* Divide by number of gaps + 1 */
        text-align: left; /* Start text left */
     }
      .level-markers span:last-child {
          text-align: right; /* End text right */
      }


    #shock-display {
        background-color: #34495e;
        color: #e74c3c;
        padding: 10px;
        border-radius: 5px;
        font-size: 1.4em;
        font-weight: bold;
        margin-bottom: 15px;
        box-shadow: 0 0 8px rgba(231, 76, 60, 0.5);
    }
     #current-voltage {
         color: #f1c40f; /* Yellowish for dynamic value */
     }

    .controls {
        text-align: center;
        margin-top: 30px;
    }

    .action-button {
        padding: 12px 25px;
        margin: 0 10px;
        font-size: 1.1em;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: 500;
    }

    .primary {
        background-color: #2ecc71;
        color: white;
    }

    .primary:hover:not(:disabled) {
        background-color: #27ae60;
        transform: translateY(-2px);
    }

    .secondary {
        background-color: #e74c3c;
        color: white;
    }

    .secondary:hover:not(:disabled) {
        background-color: #c0392b;
         transform: translateY(-2px);
    }

    button:disabled {
        background-color: #bdc3c7;
        cursor: not-allowed;
        opacity: 0.7;
        transform: none;
    }

     .results-area {
         text-align: center;
     }

     .results-header h2 {
         color: #27ae60;
     }

     #final-shock-level-text {
         font-size: 1.4em;
         font-weight: bold;
         margin-bottom: 20px;
         color: #34495e;
         position: relative;
     }

     #your-level-marker {
        position: absolute;
        height: 20px; /* Height of marker */
        width: 4px; /* Width of marker line */
        background-color: #3498db; /* Blue marker */
        top: 0;
        right: 0; /* Will be positioned by JS */
        transform: translateX(50%); /* Center the marker on the exact spot */
        transition: right 0.5s ease-out;
        z-index: 10; /* Ensure it's above the bar */
     }

     #your-level-marker::after {
        content: 'אתה';
        position: absolute;
        bottom: -25px;
        left: 50%;
        transform: translateX(-50%);
        color: #3498db;
        font-size: 0.9em;
        font-weight: bold;
     }


     .milgram-comparison-bar {
         width: 90%;
         height: 30px;
         margin: 30px auto 15px auto;
         display: flex;
         border-radius: 8px;
         overflow: hidden;
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
         position: relative; /* Needed for marker positioning */
     }

     .comparison-segment {
         height: 100%;
         display: flex;
         justify-content: center;
         align-items: center;
         color: white;
         font-size: 0.85em;
         font-weight: bold;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
         box-sizing: border-box;
     }

     .comparison-segment:nth-child(1) { background-color: #2ecc71; } /* Low */
     .comparison-segment:nth-child(2) { background-color: #f1c40f; } /* Mid */
     .comparison-segment:nth-child(3) { background-color: #e67e22; } /* High */
     .comparison-segment:nth-child(4) { background-color: #e74c3c; } /* Max */

     .comparison-label {
         position: absolute;
         top: -25px;
         left: 50%;
         transform: translateX(-50%);
         font-size: 0.9em;
         color: #555;
     }

     #comparison-to-milgram-text {
         font-size: 1.1em;
         color: #34495e;
     }


    .explanation-toggle {
        text-align: center;
        margin: 30px 0;
    }

    #toggle-explanation-btn {
         padding: 15px 30px;
         background-color: #7f8c8d;
         color: white;
         border: none;
         border-radius: 8px;
         cursor: pointer;
         font-size: 1.2em;
         transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: 500;
    }

     #toggle-explanation-btn:hover {
         background-color: #95a5a6;
         transform: translateY(-2px);
     }

    .milgram-explanation {
        background-color: #ecf0f1;
        border-color: #bdc3c7;
    }

    .hidden {
        display: none;
    }

    /* Animations (simple fade for now) */
     .hidden.fade-out {
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding-top: 0;
         padding-bottom: 0;
         margin-top: 0;
         margin-bottom: 0;
     }
     .milgram-simulation:not(.hidden), .milgram-explanation:not(.hidden) {
         opacity: 1;
     }

    /* Learner Reaction Animation */
    .role-text.fade-in {
        opacity: 0;
        animation: fadeIn 0.5s ease-in-out forwards;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Learner Icon States */
     .learner-icon.shocked { color: #e74c3c; animation: pulse 0.5s ease-in-out; }
     .learner-icon.distress { color: #e67e22; animation: shake 0.5s ease-in-out infinite alternate; }
     .learner-icon.silent { color: #bdc3c7; opacity: 0.7;} /* Grey out */

     @keyframes pulse {
         0%, 100% { transform: scale(1); }
         50% { transform: scale(1.1); }
     }

     @keyframes shake {
         0%, 100% { transform: translateX(0); }
         20%, 60% { transform: translateX(-5px); }
         40%, 80% { transform: translateX(5px); }
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Defined shock levels and corresponding reactions/icons
        const shockLevels = [15, 75, 150, 250, 350, 450];
        const learnerData = [
            { reaction: "אנחה קלה.", icon: "😐" }, // Initial
            { reaction: "קריאת כאב קלה: 'או!'", icon: "😟" }, // 15V
            { reaction: "קריאות כאב: 'זה כואב!'", icon: "😩" }, // 75V
            { reaction: "דרישה נסערת להפסיק: 'אני דורש שתפסיקו את הניסוי! אני לא עונה יותר!'", icon: "😠" }, // 150V
            { reaction: "צעקות זעם ותסכול: 'שחררו אותי מכאן! תפסיקו!'", icon: "😡" }, // 250V
            { reaction: "צרחות היסטריות ודפיקות על הקיר: 'אני לא יכול יותר! אני לא עונה!!'", icon: "😱" }, // 350V
            { reaction: "דממה דרמטית... אין תגובה. (ייתכן שהלומד חסר הכרה?)", icon: " lifeless? 💀" } // 450V (After final shock)
        ];

        // Experimenter prompts (Milgram's Prods)
        const experimenterPrompts = [
            "אנא התחל בלחיצה על 'תן שוק' לרמה הראשונה.", // 0: Initial prompt
            "המשך לדרגה הבאה.", // 1: Please continue. (Used initially)
            "הניסוי דורש שתמשיך.", // 2: The experiment requires that you continue. (Prod 1)
            "זה חיוני לחלוטין שתמשיך.", // 3: It is absolutely essential that you continue. (Prod 2)
            "אין לך ברירה, עליך להמשיך.", // 4: You have no other choice, you must go on. (Prod 3)
            "למרות שהשוקים עשויים להיות כואבים, אין נזק קבוע לרקמות.", // 5: Added clarification prod
            "השלמת את הניסוי ברמה המקסימלית (450 וולט). תודה על השתתפותך." // 6: End prompt
        ];

        // Get DOM elements
        const simulationContainer = document.getElementById('simulation-container');
        const resultsArea = document.getElementById('results-area');
        const shockDisplay = document.getElementById('current-voltage');
        const shockBar = document.getElementById('shock-bar');
        const learnerReactionElement = document.getElementById('learner-reaction');
        const learnerIconElement = document.getElementById('learner-icon');
        const experimenterTextElement = document.getElementById('experimenter-text');
        const deliverShockBtn = document.getElementById('deliver-shock-btn');
        const stopExperimentBtn = document.getElementById('stop-experiment-btn');
        const finalShockLevelText = document.getElementById('final-shock-level-text');
        const comparisonText = document.getElementById('comparison-to-milgram-text');
        const yourLevelMarker = document.getElementById('your-level-marker');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
        const explanationArea = document.getElementById('explanation-area');

        let currentShockIndex = -1; // -1 means before the first shock
        let promptSequenceIndex = 0; // Index for cycling through main prompts (2, 3, 4)

        // Set initial state
        experimenterTextElement.textContent = experimenterPrompts[0];
        learnerReactionElement.textContent = learnerData[0].reaction;
        learnerIconElement.textContent = learnerData[0].icon;
        shockDisplay.textContent = '--';

        // Helper function to update UI state based on shock level
        function updateSimulationUI(index) {
             const level = shockLevels[index];
             const reaction = learnerData[index + 1]; // +1 because learnerData[0] is initial state
             const percentComplete = (index + 1) / shockLevels.length * 100;

             shockDisplay.textContent = `${level}`;
             shockBar.style.width = `${percentComplete}%`;
             shockBar.className = `shock-level-${index}`; // Add class for potential future styling based on level

             // Remove existing animation classes before adding new ones
             learnerReactionElement.classList.remove('fade-in');
             learnerIconElement.classList.remove('shocked', 'distress', 'silent');

             // Trigger reflow to restart animation
             void learnerReactionElement.offsetWidth;
             void learnerIconElement.offsetWidth;


             learnerReactionElement.textContent = reaction.reaction;
             learnerReactionElement.classList.add('fade-in'); // Add fade-in animation


             learnerIconElement.textContent = reaction.icon;
             if (index >= 0 && index <= 1) learnerIconElement.classList.add('shocked'); // Mild pain
             else if (index >= 2 && index <= 4) learnerIconElement.classList.add('distress'); // Increasing distress
             else if (index === 5) learnerIconElement.classList.add('silent'); // Silence

             // Determine next experimenter prompt
             if (index < shockLevels.length - 1) { // Not yet at max level
                  let nextPrompt;
                   if (index === 0) { // After first shock
                       nextPrompt = experimenterPrompts[1]; // Please continue
                   } else if (index === shockLevels.length - 2) { // Before the last shock (350V to 450V)
                        nextPrompt = `${experimenterPrompts[promptSequenceIndex % 3 + 2]} ${experimenterPrompts[5]}`; // Prod + clarification
                        promptSequenceIndex = (promptSequenceIndex + 1) % 3; // Cycle prods 2,3,4
                   }
                   else { // Standard progression (150V to 350V)
                       nextPrompt = experimenterPrompts[promptSequenceIndex % 3 + 2]; // Cycle prods 2,3,4
                       promptSequenceIndex = (promptSequenceIndex + 1) % 3;
                   }
                  experimenterTextElement.textContent = `החוקר: ${nextPrompt}`;

             } else { // Reached max level
                 experimenterTextElement.textContent = `החוקר: ${experimenterPrompts[6]}`; // End prompt
             }

        }

        // Handle Shock Button Click
        deliverShockBtn.addEventListener('click', () => {
            if (currentShockIndex === -1) {
                currentShockIndex = 0; // Start at the first shock level (15V)
                stopExperimentBtn.disabled = false; // Enable stop button after first interaction
            } else {
                currentShockIndex++;
            }

            if (currentShockIndex < shockLevels.length) {
                updateSimulationUI(currentShockIndex);
            }

            if (currentShockIndex === shockLevels.length - 1) {
                 // Reached max level, disable shock button and auto-end after a moment
                 deliverShockBtn.disabled = true;
                 stopExperimentBtn.disabled = true; // Also disable stop button
                 setTimeout(() => endSimulation(currentShockIndex), 1500); // Allow UI update to show 450V
            }
        });

        // Handle Stop Button Click
        stopExperimentBtn.addEventListener('click', () => {
            endSimulation(currentShockIndex);
        });

        // Toggle Explanation
        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationArea.classList.contains('hidden');
            if (isHidden) {
                 explanationArea.classList.remove('hidden');
                 // Optional: Add fade-in class if you implement JS-based fading
                 // explanationArea.classList.add('fade-in');
                 toggleExplanationBtn.textContent = 'הסתר הסבר';
            } else {
                 explanationArea.classList.add('hidden');
                  // Optional: Add fade-out class if you implement JS-based fading
                 // explanationArea.classList.add('fade-out');
                 toggleExplanationBtn.textContent = 'מעוניינים להבין? לחצו לקרוא עוד על ניסוי מילגרם והמסקנות';
            }
        });

        // End Simulation Function
        function endSimulation(finalIndex) {
            // Hide simulation and show results with a fade effect
            simulationContainer.classList.add('hidden');
             // setTimeout(() => { // Use timeout if you want a longer fade-out effect
             // simulationContainer.style.display = 'none';
             // }, 500); // Match CSS transition duration

            resultsArea.classList.remove('hidden');
             // resultsArea.classList.add('fade-in'); // Optional: Add fade-in animation to results

            const finalLevelReached = finalIndex >= 0 ? shockLevels[Math.min(finalIndex, shockLevels.length -1)] : 0; // Ensure valid index, default to 0 if stopped before first
            const stoppedBeforeFirst = finalIndex === -1;
            const reachedMax = finalIndex === shockLevels.length - 1;

            finalShockLevelText.textContent = `עצרת ברמת שוק של: ${stoppedBeforeFirst ? 0 : finalLevelReached} וולט.`;


             // Position the marker on the comparison bar
             let markerPositionPercentage;
             if (stoppedBeforeFirst) {
                 markerPositionPercentage = 0; // Before the bar starts
             } else {
                // Map finalLevelReached to a percentage of the bar width (0% to 100%)
                // Simple linear mapping for the sake of demonstration on the simplified levels
                // 0V maps to 0%, 450V maps to 100%
                // shockLevels: [15, 75, 150, 250, 350, 450]
                // Mapping to 0-100%: 0V=0%, 15V=~5%, 75V=~17%, 150V=~33%, 250V=~55%, 350V=~77%, 450V=100%
                const maxPossibleLevel = 450; // Based on shockLevels array max
                 // Use the index to position for simplicity based on the segments
                 markerPositionPercentage = (finalIndex + 0.5) / shockLevels.length * 100;
                 if (finalIndex === -1) markerPositionPercentage = 0; // Before the first step

                 // Adjust for the visual segments if needed - simpler to use index+1 / length
                 markerPositionPercentage = (finalIndex + 1) / shockLevels.length * 100;
                 if (stoppedBeforeFirst) markerPositionPercentage = 0; // At the very start
                 if (reachedMax) markerPositionPercentage = 100; // At the very end
             }

             // Adjust positioning for RTL
             // Position from the left edge of the container, not the right
             const containerWidth = yourLevelMarker.parentElement.offsetWidth;
             // markerPositionPercentage is 0-100% of the bar's width
             // Calculate the 'right' position based on the bar's width and marker position
             const barWidth = resultsArea.querySelector('.milgram-comparison-bar').offsetWidth; // Get the bar element dynamically
             const rightPosition = barWidth * (100 - markerPositionPercentage) / 100;

             // Need to adjust for the 90% width and centering margin of the bar
             const barContainer = resultsArea.querySelector('.milgram-comparison-bar');
             const barContainerWidth = barContainer.offsetWidth;
             const parentWidth = barContainer.parentElement.offsetWidth;
             const barRightOffset = (parentWidth - barContainerWidth) / 2; // The right margin of the bar within its parent

             // Position relative to the right edge of the parent, minus the bar's right offset
             yourLevelMarker.style.right = `${barRightOffset + (barContainerWidth * (100 - markerPositionPercentage) / 100)}px`;


            let comparison = "";
            if (reachedMax) {
                 comparison = "בניסוי מילגרם המקורי, כ-65% מהמשתתפים הגיעו לרמה המקסימלית (450 וולט). אתה נמצא בתוך קבוצה זו.";
            } else if (finalLevelReached >= 350) {
                 comparison = `עצרת ברמה גבוהה יחסית (${finalLevelReached} וולט). בניסוי המקורי, רבים המשיכו מעבר לרמה זו, וכ-65% הגיעו עד הסוף (450 וולט).`;
            } else if (finalLevelReached >= 150) {
                 comparison = `עצרת בשלב בו הלומד הביע התנגדות ברורה (${finalLevelReached} וולט). בניסוי המקורי, אחוז משמעותי מהמשתתפים המשיך מעבר לרמה זו.`;
            } else if (finalLevelReached > 0) {
                 comparison = `עצרת בשלב מוקדם יחסית (${finalLevelReached} וולט), בו הלומד רק החל להביע מצוקה משמעותית. רבים בניסוי המקורי המשיכו מעבר לכך. כל הכבוד על ההתנגדות המוקדמת.`;
            } else { // finalLevel is 0 or before first shock (-1 index)
                 comparison = `עצרת לפני מתן שוק כלשהו או ברמה הנמוכה ביותר (0 וולט). הדבר דרש התנגדות לסמכות לפני שנוצר לחץ משמעותי כלל. בניסוי המקורי, אף משתתף לא עצר לפני 300 וולט. ההחלטה שלך להתנגד מוקדם בולטת ביחס לממצאים המקוריים.`;
            }

            comparisonText.textContent = comparison;

            // Disable buttons definitively
            deliverShockBtn.disabled = true;
            stopExperimentBtn.disabled = true;
        }
    });
</script>
```