---
title: "ניהול משבר: להציל חיים אחרי רעידת אדמה"
english_slug: crisis-management-saving-lives-after-earthquake
category: "ניהול"
tags: [רעידת אדמה, משבר הומניטרי, סיוע בינלאומי, קבלת החלטות, הערכת מצב]
---
# מוקד שליטה: ניהול משבר רעידת אדמה

האדמה רעדה. עיר שלמה הפכה להריסות. אתם ראש צוות ניהול המשבר, וגורל אלפים תלוי בהחלטות שלכם. זמן קצר, משאבים מוגבלים, וים של צרכים דחופים. היכולת שלכם לתעדף ולהקצות את צוותי הסיוע היא ההבדל בין חיים למוות. האם תצליחו לנווט באפלה ולהציל את המירב?

<div class="crisis-simulation-container">
    <div class="simulation-area">
        <div class="info-panel">
            <h3><i class="icon-status"></i> מצב נוכחי (<span id="current-turn">0</span> שעות אחרי האסון)</h3>
            <p><strong>היקף ההרס:</strong> קטסטרופלי, אזורים נרחבים בלתי נגישים.</p>
            <p><strong>נפגעים משוער:</strong> עשרות אלפים, רבים לכודים, פצועים אנוש, או זקוקים לסיוע קיומי מיידי.</p>
            <h4><i class="icon-needs"></i> צרכים דחופים:</h4>
            <ul id="needs-list">
                <li class="need-item need-water">מים נקיים: <span id="need-water"></span> נפשות</li>
                <li class="need-item need-food">מזון בסיסי: <span id="need-food"></span> נפשות</li>
                <li class="need-item need-shelter">מחסה חירום: <span id="need-shelter"></span> נפשות</li>
                <li class="need-item need-medical">טיפול רפואי דחוף: <span id="need-medical"></span> נפשות</li>
                <li class="need-item need-sar">חיפוש והצלה: <span id="need-sar"></span> אתרים לקריסה</li>
            </ul>
            <p><strong>מגבלות לוגיסטיות:</strong> תשתיות קרסו, גישה קשה, תקשורת מקוטעת.</p>
            <h4><i class="icon-score"></i> סיכום תוצאות (עד כה):</h4>
            <p>חיים שניצלו: <span id="score-saved">0</span></p>
            <p>נפשות שקיבלו סיוע חירום: <span id="score-aided">0</span></p>
            <p>משאבי סיוע מבוזבזים: <span id="score-wasted">0</span> (עלות צוותים שלא הוקצו)</p>
        </div>

        <div class="teams-panel">
            <h3><i class="icon-teams"></i> צוותים זמינים</h3>
            <div id="teams-list">
                <!-- Teams will be listed here by JS -->
            </div>
        </div>

        <div class="assignments-panel">
            <h3><i class="icon-assign"></i> הקצאת צוותים (ל-6 שעות הבאות)</h3>
            <div id="assignments-ui">
                <!-- Assignment dropdowns will be here -->
            </div>
            <button id="next-turn-btn"><i class="icon-time"></i> התקדם 6 שעות (סיבוב <span id="turn-counter">1</span>)</button>
        </div>

        <div class="updates-panel">
            <h3><i class="icon-updates"></i> עדכוני שטח ומשוב</h3>
            <div id="updates-log">
                <p>-- קבלת שליטה על מוקד ניהול המשבר --</p>
            </div>
        </div>
    </div>
</div>

<style>
    /* General Styles */
    .crisis-simulation-container {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 1100px; /* Slightly wider */
        margin: 25px auto;
        padding: 25px;
        border: 1px solid #dcdcdc;
        border-radius: 12px; /* Softer corners */
        background-color: #f4f7f6; /* Light, calm background */
        box-shadow: 4px 4px 20px rgba(0,0,0,0.1); /* More prominent shadow */
        color: #333;
    }

    h1, h2, h3 {
        color: #1f3a6a; /* Darker blue for headers */
        text-align: center;
        margin-top: 0;
        font-weight: bold;
    }

    h3 {
        margin-bottom: 12px;
        border-bottom: 2px solid #e0e0e0; /* Clearer separator */
        padding-bottom: 8px;
        color: #3f577c; /* Slightly lighter blue */
        font-size: 1.2em;
        display: flex;
        align-items: center;
        justify-content: center; /* Center icon and text */
    }

    /* Icons - Using simple placeholder text for now, could be SVGs/font icons */
    .icon-status::before { content: "📊 "; font-size: 1.1em; margin-left: 8px; }
    .icon-needs::before { content: "🆘 "; font-size: 1.1em; margin-left: 8px; }
    .icon-score::before { content: "🏅 "; font-size: 1.1em; margin-left: 8px; }
    .icon-teams::before { content: "👥 "; font-size: 1.1em; margin-left: 8px; }
    .icon-assign::before { content: "🎯 "; font-size: 1.1em; margin-left: 8px; }
    .icon-updates::before { content: "📢 "; font-size: 1.1em; margin-left: 8px; }
    .icon-time::before { content: "⏳ "; font-size: 1.1em; margin-left: 8px; }

    /* Layout */
    .simulation-area {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px; /* Increased gap */
        margin-top: 25px;
    }

    .info-panel, .teams-panel, .assignments-panel, .updates-panel {
        background-color: #ffffff;
        padding: 20px; /* Increased padding */
        border-radius: 8px; /* Consistent corners */
        border: 1px solid #e0e0e0;
        box-shadow: inset 1px 1px 5px rgba(0,0,0,0.05); /* Inner shadow for depth */
        display: flex; /* Use flexbox for inner layout */
        flex-direction: column;
    }

     .info-panel, .teams-panel {
         /* Max height for potential scroll if content grows */
         max-height: 450px;
         overflow-y: auto;
     }


    /* Needs List Styling */
    #needs-list {
        list-style: none;
        padding: 0;
        margin-bottom: 15px;
    }

    #needs-list li {
        margin-bottom: 8px;
        padding: 5px 0;
        border-bottom: 1px dotted #eee; /* Subtle separator */
        font-weight: bold; /* Needs are important */
        color: #555;
    }

    #needs-list li span {
        font-weight: normal; /* Value should be normal */
        color: #1f3a6a; /* Highlight numbers */
    }

    /* Team List Styling */
     #teams-list {
        flex-grow: 1; /* Teams panel content grows */
     }

    .team-item {
        border-bottom: 1px dashed #cfd8dc; /* Lighter dashed border */
        padding: 8px 0;
        margin-bottom: 8px;
        color: #555;
    }

    .team-item:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    /* Assignments Styling */
     #assignments-ui {
         flex-grow: 1; /* Assignments panel content grows */
         max-height: 300px; /* Limit height to keep button visible */
         overflow-y: auto; /* Add scroll if many teams */
         margin-bottom: 15px;
     }

    .assignment-item {
        margin-bottom: 12px;
        padding: 10px;
        border: 1px solid #b0bec5; /* Subtle border */
        border-radius: 6px;
        background-color: #eceff1; /* Light grey background */
        display: flex; /* Align items */
        justify-content: space-between; /* Space between team name and select */
        align-items: center;
        flex-wrap: wrap; /* Allow wrap on smaller screens */
    }

    .assignment-item strong {
        flex-grow: 1; /* Team name takes available space */
        margin-inline-end: 10px; /* Space after team name */
    }

    .assignment-item select {
        padding: 8px; /* More padding */
        border: 1px solid #90a4ae; /* Match item border */
        border-radius: 4px;
        background-color: #ffffff;
        font-size: 1em;
        cursor: pointer;
        min-width: 150px; /* Ensure select is wide enough */
    }

    /* Button Styling */
    #next-turn-btn {
        display: flex; /* Use flex to center content */
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 12px 15px; /* More padding */
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px; /* Consistent corners */
        font-size: 1.1em;
        cursor: pointer;
        margin-top: auto; /* Push to bottom of flex container */
        transition: background-color 0.3s ease, opacity 0.3s ease;
        font-weight: bold;
    }

    #next-turn-btn i {
        margin-left: 8px;
    }


    #next-turn-btn:hover:not(:disabled) {
        background-color: #0056b3; /* Darker blue on hover */
    }

    #next-turn-btn:disabled {
        background-color: #cccccc; /* Grey out when disabled */
        cursor: not-allowed;
        opacity: 0.8;
    }

    #restart-btn {
         display: block;
        width: 100%;
        padding: 10px;
        background-color: #6c757d; /* Secondary grey */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        cursor: pointer;
        margin-top: 10px; /* Space below next turn */
        transition: background-color 0.3s ease;
         text-align: center;
    }
    #restart-btn:hover {
        background-color: #5a6268;
    }


    /* Updates Log Styling */
    #updates-log {
        max-height: 250px; /* Increased height */
        overflow-y: auto;
        border: 1px solid #cfd8dc; /* Lighter border */
        padding: 15px; /* Increased padding */
        background-color: #e3f2fd; /* Very light blue background */
        font-size: 0.9em;
        border-radius: 4px;
        flex-grow: 1; /* Allow log to grow */
    }

    #updates-log p {
        margin-bottom: 8px; /* More space between messages */
        line-height: 1.5;
        border-bottom: 1px dotted #bbdefb; /* Subtle separator */
        padding-bottom: 5px;
    }
     #updates-log p:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }


    /* Explanation Section Styling */
    .explanation-button {
        display: block;
        width: max-content;
        margin: 30px auto 20px auto; /* More space above and below */
        padding: 12px 25px; /* More padding */
        background-color: #28a745; /* Success green */
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .explanation-button:hover {
        background-color: #218838; /* Darker green on hover */
    }

    .explanation-content {
        border: 1px solid #b0bec5;
        padding: 25px; /* Increased padding */
        margin-top: 20px;
        border-radius: 8px;
        background-color: #ffffff;
        display: none; /* Initially hidden */
        direction: rtl;
        line-height: 1.6; /* Better readability */
        color: #333;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
    }

    .explanation-content h3 {
        color: #0277bd; /* Darker cyan-blue */
        border-bottom: 2px solid #0277bd;
        margin-top: 15px;
        padding-bottom: 8px;
        font-size: 1.3em;
        text-align: right; /* Align explanation headers right */
        justify-content: flex-start; /* Align icon left in RTL */
    }

    .explanation-content ul {
        margin-top: 10px;
        padding-right: 20px; /* RTL padding */
    }

    .explanation-content li {
        margin-bottom: 8px;
    }

    .explanation-content strong {
        color: #1f3a6a; /* Highlight key terms */
    }

    /* Responsive adjustments */
     @media (max-width: 768px) {
         .simulation-area {
             grid-template-columns: 1fr; /* Stack panels on smaller screens */
         }
         .info-panel, .teams-panel, .assignments-panel, .updates-panel {
             max-height: none; /* Remove fixed height when stacked */
             overflow-y: visible;
         }
          .assignment-item {
              flex-direction: column; /* Stack team name and select */
              align-items: flex-start;
          }
          .assignment-item strong {
              margin-inline-end: 0;
              margin-bottom: 8px;
          }
          .assignment-item select {
               width: 100%; /* Make select full width */
               min-width: auto;
          }
     }

     /* Animations - Basic fading for updates */
     #updates-log p {
         animation: fadeIn 0.5s ease-out;
     }

     @keyframes fadeIn {
         from { opacity: 0; transform: translateY(5px); }
         to { opacity: 1; transform: translateY(0); }
     }

</style>

<button class="explanation-button" id="toggle-explanation">מה עומד מאחורי הסימולציה? (רקע תיאורטי)</button>

<div class="explanation-content" id="explanation">
    <h3><i class="icon-info"></i> מהו משבר הומניטרי ושלבי התגובה</h3>
    <p>משבר הומניטרי הוא אירוע בקנה מידה גדול המאיים על חייהם ורווחתם של אוכלוסיות, לרוב עקב אסונות טבע, סכסוכים או מגפות. התגובה הראשונית מתמקדת בהצלת חיים וסיפוק צרכים בסיסיים (שלב ה-<strong>Relief</strong>). לאחריו מגיעים שלבי ה-<strong>Recovery</strong> (התאוששות מוקדמת, שיקום שירותים) וה-<strong>Reconstruction/Development</strong> (בנייה מחדש וחיזוק חוסן לטווח ארוך).</p>

    <h3><i class="icon-assessment"></i> הערכת צרכים והקצאת משאבים</h3>
    <p>באזורי אסון, המשאבים (צוותים, ציוד, זמן) תמיד מוגבלים אל מול הצרכים האדירים. הערכת מצב מהירה ומדויקת חיונית לזיהוי הצרכים הדחופים ביותר (מים, מזון, מחסה, רפואה, חיפוש והצלה) ולהקצאה אופטימלית של המשאבים המוגבלים כדי להשיג את ההשפעה המרבית על הצלת חיים והפחתת סבל.</p>

    <h3><i class="icon-types"></i> סוגי סיוע הומניטרי</h3>
    <p>הסיוע כולל מגוון תחומים: <strong>מים ותברואה (WASH)</strong> למניעת מחלות, <strong>מזון ותזונה</strong> למניעת רעב, <strong>מחסה</strong> למשפחות שאיבדו את בתיהן, <strong>רפואה ובריאות</strong> לפצועים וחולים, ו<strong>חיפוש והצלה (SAR)</strong> לחילוץ לכודים. לצד אלו קיימים גם צרכים כמו <strong>הגנה</strong> לאוכלוסיות פגיעות ו<strong>לוגיסטיקה</strong> לתיאום והספקת כלל הסיוע.</p>

    <h3><i class="icon-challenges"></i> אתגרי לוגיסטיקה ותיאום</h3>
    <p>דרכים חסומות, קשיי תקשורת, מחסור בתשתיות - כל אלו הופכים את העברת הסיוע למורכבת להחריד. צוותי <strong>לוגיסטיקה</strong> קריטיים לפתיחת נתיבים, הקמת נקודות חלוקה, ותיאום בין הגופים השונים בשטח כדי להבטיח שהסיוע יגיע ליעדו במהירות וביעילות.</p>

    <h3><i class="icon-dilemmas"></i> קבלת החלטות תחת לחץ ואי-ודאות</h3>
    <p>מנהלי משברים פועלים בתנאים של מידע חלקי, לחץ זמן עצום ודילמות מוסריות קשות. כל החלטה כרוכה בפשרות - הקצאת צוות לאזור אחד פירושה מניעת הגעתו לאזור אחר. הצלחתם תלויה ביכולת לתעדף, להסתגל לשינויים ולקבל החלטות אמיצות למען טובת המירב.</p>

     <h3><i class="icon-principles"></i> עקרונות מפתח</h3>
     <p>הסיוע ההומניטרי מונחה על ידי עקרונות: <strong>אנושיות</strong> (הקלה על סבל), <strong>ניטרליות</strong> (אי-לקיחת צד בסכסוך), <strong>חוסר משוא פנים</strong> (סיוע על בסיס צורך בלבד) ו<strong>עצמאות</strong> (חופש מלחצים פוליטיים/צבאיים).</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const needs = {
            water: { initial: 8000, decayRate: 800, meetCapacity: 2000, priority: 4, deathRate: 0.4, name: 'מים נקיים' }, // Higher priority, faster death
            food: { initial: 12000, decayRate: 600, meetCapacity: 3000, priority: 2, deathRate: 0.1, name: 'מזון בסיסי' },
            shelter: { initial: 15000, decayRate: 500, meetCapacity: 4000, priority: 1, deathRate: 0.05, name: 'מחסה חירום' }, // Lowest death rate initially
            medical: { initial: 4000, decayRate: 700, meetCapacity: 1500, priority: 5, deathRate: 0.6, name: 'טיפול רפואי דחוף' }, // Highest priority, highest death rate
            sar: { initial: 10, decayRate: 0, meetCapacity: 2, priority: 3, peoplePerSite: 150, name: 'חיפוש והצלה' } // SAR is different
        };

        const teams = {
            sar1: { name: 'צוות חילוץ והצלה כבד (א)', type: 'sar', capacity: needs.sar.meetCapacity, assigned: false },
            sar2: { name: 'צוות חילוץ והצלה קל (ב)', type: 'sar', capacity: needs.sar.meetCapacity * 0.75, assigned: false }, // Varied capacity
            medical1: { name: 'צוות רפואי שדה (א)', type: 'medical', capacity: needs.medical.meetCapacity, assigned: false },
            medical2: { name: 'צוות רפואי שדה (ב)', type: 'medical', capacity: needs.medical.meetCapacity * 0.8, assigned: false },
            logistics1: { name: 'צוות לוגיסטיקה (א)', type: 'logistics', capacity: null, assigned: false },
            logistics2: { name: 'צוות לוגיסטיקה (ב)', type: 'logistics', capacity: null, assigned: false },
            waterTeam: { name: 'צוות אספקת מים', type: 'water', capacity: needs.water.meetCapacity, assigned: false },
            foodTeam: { name: 'צוות אספקת מזון', type: 'food', capacity: needs.food.meetCapacity, assigned: false },
            shelterTeam: { name: 'צוות הקמת מחסות', type: 'shelter', capacity: needs.shelter.meetCapacity, assigned: false }
        };

        let currentNeeds = {};
        let scores = { saved: 0, aided: 0, wasted: 0 };
        let turn = 0;
        const maxTurns = 12; // More turns for longer simulation
        const turnDuration = 6; // Hours per turn

        const needsListElement = document.getElementById('needs-list');
        const teamsListElement = document.getElementById('teams-list');
        const assignmentsUIElement = document.getElementById('assignments-ui');
        const updatesLogElement = document.getElementById('updates-log');
        const nextTurnButton = document.getElementById('next-turn-btn');
        const scoreSavedElement = document.getElementById('score-saved');
        const scoreAidedElement = document.getElementById('score-aided');
        const scoreWastedElement = document.getElementById('score-wasted');
        const currentTurnElement = document.getElementById('current-turn');
        const turnCounterElement = document.getElementById('turn-counter'); // New element for turn count on button

        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationContent = document.getElementById('explanation');

        function initGame() {
            // Initialize needs
            for (const needType in needs) {
                currentNeeds[needType] = needs[needType].initial;
            }

            // Reset scores and turn
            scores = { saved: 0, aided: 0, wasted: 0 };
            turn = 0;

            // Reset team assignments state
             for (const teamId in teams) {
                teams[teamId].assigned = false;
            }

            // Clear updates log
            updatesLogElement.innerHTML = '<p>-- קבלת שליטה על מוקד ניהול המשבר --</p>';

            renderState();
        }

        function renderState() {
            // Render needs with formatting
            document.getElementById('need-water').innerText = Math.max(0, Math.ceil(currentNeeds.water)).toLocaleString() + ' נפש';
            document.getElementById('need-food').innerText = Math.max(0, Math.ceil(currentNeeds.food)).toLocaleString() + ' נפש';
            document.getElementById('need-shelter').innerText = Math.max(0, Math.ceil(currentNeeds.shelter)).toLocaleString() + ' נפש';
            document.getElementById('need-medical').innerText = Math.max(0, Math.ceil(currentNeeds.medical)).toLocaleString() + ' נפש';
            document.getElementById('need-sar').innerText = Math.max(0, Math.ceil(currentNeeds.sar)).toLocaleString() + ' אתרים';

            // Render scores
            scoreSavedElement.innerText = Math.max(0, scores.saved).toLocaleString(); // Score saved cannot be negative
            scoreAidedElement.innerText = Math.max(0, scores.aided).toLocaleString();
            scoreWastedElement.innerText = Math.max(0, scores.wasted).toLocaleString();
            currentTurnElement.innerText = turn * turnDuration;
            turnCounterElement.innerText = turn + 1;


            // Render available teams and assignment UI
            teamsListElement.innerHTML = '';
            assignmentsUIElement.innerHTML = '';

            const availableNeedsOptions = Object.keys(needs)
                .filter(needType => currentNeeds[needType] > 0.5 || needType === 'sar') // Only show needs that still exist (or SAR which is site-based)
                .sort((a, b) => needs[b].priority - needs[a].priority); // Sort by priority (higher first)

            for (const teamId in teams) {
                const team = teams[teamId];
                const teamDiv = document.createElement('div');
                teamDiv.classList.add('team-item');
                teamDiv.innerText = `${team.name}`; // Simplified capacity display in list
                teamsListElement.appendChild(teamDiv);

                const assignmentDiv = document.createElement('div');
                assignmentDiv.classList.add('assignment-item');
                assignmentDiv.innerHTML = `<strong>${team.name}:</strong> <select id="assign-${teamId}">
                    <option value="none">לא הוקצה (משאבים יבוזבזו)</option>
                </select>`;
                 assignmentsUIElement.appendChild(assignmentDiv);

                 const selectElement = document.getElementById(`assign-${teamId}`);

                 // Add relevant options based on team type and existing needs
                 if (team.type === 'logistics') {
                     const option = document.createElement('option');
                     option.value = 'logistics_support'; // Specific logistics support role
                     option.innerText = `סיוע לוגיסטי כללי`;
                     selectElement.appendChild(option);
                 } else {
                      availableNeedsOptions.forEach(needType => {
                         // Check if team type matches need type
                          if (team.type === needType) {
                             const option = document.createElement('option');
                             option.value = needType;
                             option.innerText = `טיפול בצרכי ${needs[needType].name}`;
                             selectElement.appendChild(option);
                         }
                      });
                 }
            }

            if (turn >= maxTurns) {
                nextTurnButton.disabled = true;
                nextTurnButton.innerText = 'הסימולציה הסתיימה';
                logUpdate(`-- הסימולציה הסתיימה לאחר ${turn * turnDuration} שעות --`);
                logUpdate(`סיכום סופי: חיים שניצלו - ${Math.max(0, scores.saved).toLocaleString()}, נפשות שקיבלו סיוע - ${Math.max(0, scores.aided).toLocaleString()}, עלות משאבים מבוזבזים - ${Math.max(0, scores.wasted).toLocaleString()}`);
                 // Optional: Add a restart button
                 if (!document.getElementById('restart-btn')) {
                     const restartBtn = document.createElement('button');
                     restartBtn.innerText = 'התחל מחדש';
                     restartBtn.id = 'restart-btn';
                     restartBtn.onclick = initGame; // Assign click handler
                     assignmentsUIElement.appendChild(restartBtn); // Add to the assignment panel
                 }

            } else {
                 nextTurnButton.disabled = false;
                 nextTurnButton.querySelector('#turn-counter').innerText = turn + 1; // Update turn counter on button
                 const restartBtn = document.getElementById('restart-btn');
                 if (restartBtn) restartBtn.remove(); // Remove restart button if game is ongoing
            }
        }

        function processTurn() {
            turn++;
            const currentAssignments = {};
            let logisticsSupportCount = 0;

            // 1. Read assignments and identify logistics support
             for (const teamId in teams) {
                 const selectElement = document.getElementById(`assign-${teamId}`);
                 if (selectElement) {
                      const assignmentValue = selectElement.value;
                      currentAssignments[teamId] = assignmentValue;
                      if (assignmentValue === 'none') {
                          scores.wasted += 50; // Increased penalty for unassigned team
                          logUpdate(`⚠️ ${teams[teamId].name} לא הוקצה ומשאביו בוזבזו בסיבוב זה.`);
                      } else if (assignmentValue === 'logistics_support') {
                           logisticsSupportCount++;
                           logUpdate(`🚚 ${teams[teamId].name} מספק תמיכה לוגיסטית חיונית.`);
                      }
                 }
             }

             // Calculate logistics effect
             const logisticsDecayMultiplier = Math.max(0, 1 - (logisticsSupportCount * 0.07)); // 7% decay reduction per logistics team, max 100% reduction (logistics won't increase need decay)
             const logisticsAidBonus = (logisticsSupportCount * 0.1); // 10% aid bonus per logistics team

            // 2. Apply impact based on assignments (excluding logistics support handled above)
            for (const teamId in currentAssignments) {
                const assignmentType = currentAssignments[teamId];
                const team = teams[teamId];

                if (assignmentType === 'none' || assignmentType === 'logistics_support') {
                    continue; // Handled separately
                }

                const needType = assignmentType; // Assignment value matches need key
                const capacity = team.capacity;
                const needInfo = needs[needType];

                if (currentNeeds[needType] > 0.5 && capacity > 0) { // Check against small value due to potential floating point
                    let effectiveCapacity = capacity * (1 + logisticsAidBonus); // Apply logistics bonus to aid capacity

                    let amountAided = Math.min(currentNeeds[needType], effectiveCapacity);


                     if (needType === 'sar') {
                          // SAR is different: saves people from sites
                           const sitesCleared = Math.min(currentNeeds.sar, Math.round(effectiveCapacity / needs.sar.peoplePerSite) ); // How many 'sites' can this team clear?
                           if (sitesCleared > 0) {
                                const peopleSaved = Math.round(sitesCleared * needs.sar.peoplePerSite); // How many people are in these sites?
                                scores.saved += peopleSaved;
                                currentNeeds.sar -= sitesCleared; // Reduce sites
                                logUpdate(`🚨 ${team.name} חילץ ${peopleSaved.toLocaleString()} לכודים מ-${sitesCleared} אתרי קריסה. (+${peopleSaved} חיים)`);
                                scores.aided += peopleSaved; // Count rescued as aided too
                           } else {
                                logUpdate(`⚠️ ${team.name} הוקצה לחיפוש והצלה אך לא הצליח להגיע לאתרים חדשים או שלא נותרו אתרים לחיפוש.`);
                                scores.wasted += 25; // Penalty for ineffective SAR assignment
                           }

                     } else { // Standard aid teams (water, food, shelter, medical)
                         amountAided = Math.min(currentNeeds[needType], effectiveCapacity);
                         let livesPossiblySaved = 0;

                         if (needType === 'medical') {
                             // Medical directly saves lives from those treated
                             livesPossiblySaved = Math.round(amountAided * 0.7); // Assume 70% survival rate for critical cases treated
                             scores.saved += livesPossiblySaved;
                             logUpdate(`🏥 ${team.name} טיפל בצרכים רפואיים דחופים עבור ${Math.round(amountAided).toLocaleString()} נפשות. (+${livesPossiblySaved} חיים ניצלו מטיפול)`);
                         } else {
                              // Water, Food, Shelter aid helps prevent future deaths and alleviates suffering
                               logUpdate(`🤝 ${team.name} סיפק ${needInfo.name} עבור ${Math.round(amountAided).toLocaleString()} נפשות.`);
                         }
                         scores.aided += amountAided;
                         currentNeeds[needType] -= amountAided;
                     }
                 } else if (currentNeeds[needType] <= 0.5) {
                     // Assigned to a need that is already largely met
                      logUpdate(`ℹ️ ${team.name} הוקצה לטפל בצרכי ${needInfo.name} שכבר טופלו ברובם. ייתכן שמשאבים בוזבזו.`);
                      scores.wasted += 10; // Smaller penalty for trying to help met need
                 }
            }

            // 3. Simulate needs decay (people dying, conditions worsening)
            for (const needType in needs) {
                 const needInfo = needs[needType];
                 if (needType !== 'sar') { // SAR 'needs' don't decay in the same way
                      let unmetNeed = Math.max(0, currentNeeds[needType]); // People still needing this resource
                      let potentialLosses = needInfo.decayRate * turnDuration; // Base decay amount
                      potentialLosses *= logisticsDecayMultiplier; // Apply logistics reduction
                      potentialLosses = Math.min(unmetNeed, Math.max(0, potentialLosses)); // Cannot lose more people than need the resource

                      if (potentialLosses > 0.5) { // Only log if actual loss is significant
                          const livesLost = Math.round(potentialLosses * needInfo.deathRate); // Calculate deaths based on decay rate for this need type
                           scores.saved -= livesLost; // Subtract from saved lives score
                           currentNeeds[needType] -= potentialLosses; // The need decreases because people died/condition worsened

                           if (livesLost > 0) {
                                logUpdate(`💔 ${Math.round(potentialLosses).toLocaleString()} נפשות נפגעו קשה או מתו עקב מחסור ב${needInfo.name} (-${livesLost.toLocaleString()} חיים).`);
                           } else {
                                logUpdate(`❗ מצב ${needInfo.name} ממשיך להתדרדר עבור ${Math.round(potentialLosses).toLocaleString()} נפשות, אך ללא אובדן חיים מיידי בסיבוב זה.`);
                           }
                      } else if (unmetNeed > 0.5) {
                           // Need still exists but decay was minimal this turn (perhaps due to logistics or low base rate)
                            logUpdate(`⏳ צרכי ${needInfo.name} עדיין קיימים עבור ${Math.ceil(unmetNeed).toLocaleString()} נפשות. דרושה התייחסות.`);
                      } else {
                          // Need is fully met or negligible
                          logUpdate(`✅ צרכי ${needInfo.name} כמעט טופלו לחלוטין.`);
                      }
                 } else { // SAR needs (sites)
                      // SAR sites don't decay by themselves, but could potentially become unstable/harder to reach over time?
                      // For simplicity, they just remain until cleared.
                      if (currentNeeds.sar > 0.5) {
                           logUpdate(`🏗️ נותרו כ-${Math.ceil(currentNeeds.sar).toLocaleString()} אתרי קריסה הדורשים חיפוש וחילוץ.`);
                      } else {
                           logUpdate(`🎉 כל אתרי הקריסה העיקריים טופלו על ידי צוותי חיפוש והצלה!`);
                      }
                 }
                  // Ensure needs don't go below zero after meeting + decay
                 currentNeeds[needType] = Math.max(0, currentNeeds[needType]);
            }

            // Add some minor new needs appearing as situation unfolds
             if (turn < maxTurns - 2) { // New needs appear mostly in early/mid turns
                const newMedical = Math.round(Math.random() * 300); // New injured found
                if (newMedical > 0) {
                     currentNeeds.medical += newMedical;
                     logUpdate(`🚑 ${newMedical.toLocaleString()} פצועים חדשים אותרו וזקוקים לטיפול רפואי.`);
                }
                 const newShelter = Math.round(Math.random() * 500); // More people displaced
                  if (newShelter > 0) {
                      currentNeeds.shelter += newShelter;
                      logUpdate(`🏘️ ${newShelter.toLocaleString()} נפשות נוספות איבדו את בתיהן וזקוקות למחסה.`);
                  }
             }


            renderState();
        }

         function logUpdate(message) {
             const p = document.createElement('p');
             p.innerHTML = `<span class="log-time">שעה ${turn * turnDuration}:</span> ${message}`;
             updatesLogElement.appendChild(p);
             updatesLogElement.scrollTop = updatesLogElement.scrollHeight; // Auto-scroll to bottom
         }

        nextTurnButton.addEventListener('click', processTurn);

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            // Optional: Change button text
            toggleExplanationButton.innerText = isHidden ? 'הסתר רקע תיאורטי' : 'מה עומד מאחורי הסימולציה? (רקע תיאורטי)';
        });

        // Initial game setup
        initGame();
    });
</script>
```