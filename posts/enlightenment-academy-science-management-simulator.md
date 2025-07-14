---
title: "אקדמיית הנאורות: סימולטור ניהול מדעי"
english_slug: enlightenment-academy-science-management-simulator
category: "היסטוריה של המדע"
tags: ["היסטוריה", "מדע", "מאה 18", "ניהול", "אקדמיה", "סימולציה"]
---
# אקדמיית הנאורות: סימולטור ניהול מדעי

שנת 1700. אתם עומדים בראש אקדמיה חדשה למדעים, מוסד פורץ דרך בעידן של תגליות מסעירות. הצלחתה תלויה ביכולתכם לבחור את המוחות המבריקים ביותר, לממן את המחקרים המבטיחים ביותר, ולנווט את האקדמיה בנבכי הפוליטיקה והכלכלה של המאה ה-18. האם תוכלו להוביל את אקדמייתכם לתהילה ולהשאיר חותם בהיסטוריה של המדע?

<div id="academy-simulator" class="simulation-container">
    <h2 class="simulation-title">סימולטור מנהל האקדמיה</h2>

    <div id="game-stats" class="stats-panel">
        <p><strong>שנה:</strong> <span id="current-year">1700</span></p>
        <p><strong>מוניטין האקדמיה:</strong> <span id="reputation" class="stat-value">0</span></p>
        <p><strong>תקציב:</strong> <span id="budget" class="stat-value">1000</span> מטבעות</p>
        <p><strong>חוקרים נוכחיים:</strong> <span id="current-researchers" class="stat-value count-stat">0</span></p>
        <p><strong>פרסומים מדעיים:</strong> <span id="publications" class="stat-value count-stat">0</span></p>
    </div>

    <div id="recruitment-area" class="area-panel">
        <h3 class="area-title">מועמדים נבחרים לחברות באקדמיה</h3>
        <ul id="candidate-list" class="item-list">
            <!-- Candidates will be listed here by JavaScript -->
            <li class="loading-item">טוען מועמדים מבטיחים...</li>
        </ul>
    </div>

    <div id="projects-area" class="area-panel">
        <h3 class="area-title">הצעות למחקרי פורצי דרך</h3>
        <ul id="project-list" class="item-list">
             <!-- Projects will be listed here by JavaScript -->
             <li class="loading-item">ממתין להצעות מחקר...</li>
        </ul>
    </div>

    <div id="active-projects-area" class="area-panel">
         <h3 class="area-title">מחקרי אקדמיה פעילים</h3>
         <ul id="active-project-list" class="item-list">
              <li class="info-item">אין פרויקטים פעילים כרגע.</li>
         </ul>
    </div>

    <div id="management-area" class="area-panel">
        <h3 class="area-title">ענייני ניהול שוטפים</h3>
        <p class="info-text">אירועים בלתי צפויים ופעולות ניהול נוספות יופיעו כאן.</p>
        <div id="random-event" class="event-display">
             <!-- Random events will be displayed here -->
        </div>
    </div>

    <div id="actions" class="area-panel">
        <h3 class="area-title">פעולות מרכזיות</h3>
        <button id="advance-turn" class="action-button primary-button">התקדם לשנה הבאה</button>
    </div>

    <div id="game-log" class="area-panel log-panel">
        <h3 class="area-title">יומן האקדמיה</h3>
        <ul id="log-entries" class="log-list">
            <!-- Game events will be logged here -->
            <li><span class="log-year">[1700]</span> 📜 האקדמיה הוקמה! יצאנו לדרך בשנה הראשונה.</li>
        </ul>
    </div>
</div>

<button id="toggle-explanation" class="explanation-button">הצג רקע היסטורי: האקדמיות במאה ה-18</button>

<div id="explanation" class="explanation-content" style="display: none;">
    <h2>רקע היסטורי: האקדמיות למדעים במאה ה-18</h2>

    <h3>הולדת האקדמיות למדעים: הרקע ההיסטורי</h3>
    <p>במהלך המאה ה-17 וה-18, חלה תמורה משמעותית באופן שבו מדענים התארגנו ופעלו. במקום לעבוד לרוב באופן פרטי או תחת פטרונות של אצילים יחידים, החלו לקום מוסדות רשמיים שהוקדשו למדע - האקדמיות למדעים. מוסדות אלו, כמו הרויאל סוסייטי בלונדון (נוסדה 1660) והאקדמיה הצרפתית למדעים בפריז (נוסדה 1666), סיפקו מסגרת פורמלית לשיתוף ידע, ויכוחים מלומדים וקידום מחקר. הן נתמכו לרוב על ידי מלכים או ממשלות, שהבינו את הפוטנציאל הטכנולוגי והיוקרתי של המדע.</p>

    <h3>מבנה ותפקוד האקדמיות</h3>
    <p>האקדמיות פעלו כחברות של חוקרים מובילים. הן קיימו פגישות סדירות (לרוב שבועיות או דו-שבועיות) בהן הוצגו ניסויים חדשים, תצפיות, ותוצאות מחקר. דיונים ערים התנהלו סביב תגליות אלו. אחד התפקידים המרכזיים של האקדמיות היה פרסום. כתבי עת כמו ה-Philosophical Transactions של הרויאל סוסייטי הפכו לפלטפורמה מרכזית להפצת ידע מדעי חדש ברחבי אירופה, והיוו את הבסיס למערכת הפרסום המדעי המודרנית.</p>

    <h3>כלכלת המדע במאה ה-18</h3>
    <p>מחקר מדעי, במיוחד ניסויי, דרש משאבים. האקדמיות התקיימו ממקורות מימון מגוונים: פטרונות מלכותית (שבדרך כלל סיפקה את התקציב המרכזי והכרה רשמית), תרומות מנדבנים עשירים ומעמד האצולה, ולעיתים גם ממנויים על כתבי העת המדעיים. הכסף שימש לרכישת מכשירים, הקמת מעבדות (לרוב קטנות יחסית), תשלום למזכירים ופקידים, ותמיכה חלקית בחוקרים מסוימים (אם כי רבים עבדו ללא שכר מהאקדמיה עצמה). זמינות המשאבים השפיעה ישירות על סוג וכמות המחקר שיכול היה להתבצע.</p>

    <h3>מי היה מדען? תהליך הקבלה והתפקידים</h3>
    <p>חברות באקדמיה נחשבה לאות הכרה יוקרתי. תהליך הקבלה היה לעיתים קרובות ארוך וכלל הצגת עבודות בפני החברים הקיימים, המלצות, ולעיתים גם שיקולים של מעמד חברתי וקשרים אישיים, לא רק כישרון מדעי טהור. הקריטריונים לבחירה כללו מוניטין קיים (גם אם נרכש מחוץ לאקדמיה), יכולת לבצע ולהציג מחקר, ולעיתים גם יכולת לתרום כספית או חברתית לאקדמיה. תפקיד המדענים באקדמיה היה להציג את עבודתם, לבקר את עבודת עמיתיהם, לשתף פעולה בפרויקטים משותפים (כמו משלחות למדידת קו רוחב), ולתרום לפרסומים של האקדמיה.</p>

    <h3>מחקרי מפתח ותחומי עניין</h3>
    <p>המאה ה-18 הייתה תקופה של התקדמות אדירה בתחומי מדע רבים. באקדמיות נחקרו נושאים כמו אסטרונומיה (בעקבות התגליות של ניוטון והצורך בלוחות אסטרונומיים מדויקים לניווט), פיזיקה ניוטונית (אופטיקה, מכניקה, תנועת גרמי שמיים), בוטניקה וזואולוגיה (איסוף וקטלוג מינים חדשים מרחבי העולם), כימיה (תחילת המעבר מ"אלכימיה" למדע מודרני עם עבודות כמו של לבואזיה), חשמל (ניסויים פורצי דרך של פרנקלין ואחרים), רפואה ואנטומיה, ומתמטיקה. האקדמיות סיפקו את הפלטפורמה לשיתוף התגליות הללו ופיתוחן.</p>

    <h3>אתגרים ניהוליים</h3>
    <p>ניהול אקדמיה לא היה משימה פשוטה. מנהלים נאלצו להתמודד עם יריבויות אישיות ואקדמיות בין חוקרים בעלי אגו גדול, מחסור כרוני במשאבים כספיים ופיזיים, קושי באבטחת ציוד מתאים, והצורך להכריע בין נושאי מחקר שונים המתחרים על אותם משאבים. בנוסף, אימות תוצאות מחקר דרש לעיתים שכנוע של עמיתים וקבלת אישור מסמכות אקדמית או אפילו מלכותית, מה שהאט תהליכים. ניהול נכון היה קריטי לקידום המחקר ולשמירה על יוקרת המוסד.</p>

    <h3>השפעת הארגון על תוכן וקצב המחקר</h3>
    <p>האופן שבו האקדמיות היו מאורגנות - הדגש על פגישות סדירות, הצגת ניסויים חיים, תהליך ביקורת עמיתים בלתי רשמי בפגישות, והצורך בפרסום רשמי - עיצב במידה רבה את סדר היום המדעי. נושאים שניתן היה להדגים בקלות או לדון בהם בפומבי זכו לעיתים קרובות לתשומת לב רבה יותר. החלטות ניהוליות לגבי מימון, גיוס חוקרים והכרה בתגליות השפיעו ישירות על אילו תחומים שגשגו ועל קצב ההתקדמות המדעית הכוללת. האקדמיות לא היו רק אוסף של גאונים, אלא מוסדות חברתיים וכלכליים מורכבים שהיו להם תפקיד מכריע במהפכה המדעית ובעיצוב עידן הנאורות.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר רקע היסטורי: האקדמיות במאה ה-18' : 'הצג רקע היסטורי: האקדמיות במאה ה-18';
            explanationDiv.classList.toggle('visible', isHidden); // Add class for potential transitions
        });

        // --- Simulation Core Logic ---
        let gameState = {
            reputation: 0,
            budget: 1000,
            researchers: [],
            publications: 0,
            year: 1700,
            activeProjects: []
        };

        const stats = {
            year: document.getElementById('current-year'),
            reputation: document.getElementById('reputation'),
            budget: document.getElementById('budget'),
            currentResearchers: document.getElementById('current-researchers'),
            publications: document.getElementById('publications')
        };

        const candidateList = document.getElementById('candidate-list');
        const projectList = document.getElementById('project-list');
        const activeProjectList = document.getElementById('active-project-list');
        const gameLog = document.getElementById('log-entries');
        const advanceTurnButton = document.getElementById('advance-turn');
        const randomEventDisplay = document.getElementById('random-event');

        // Game Data
        const initialCandidates = [
            { id: 'c1', name: 'ד"ר אליזבת בויד', field: 'בוטניקה', cost: 100, annual_cost: 20, reputation_gain: 5, publish_chance: 0.6, description: 'מומחית לצמחי מרפא אקזוטיים, בעלת קשרים עם גנים בוטניים.' },
            { id: 'c2', name: 'מר תומאס קלרק', field: 'אסטרונומיה', cost: 150, annual_cost: 30, reputation_gain: 8, publish_chance: 0.5, description: 'צופה כוכבים מסור, בעל טלסקופ חדיש יחסית.' },
            { id: 'c3', name: 'פרופ\' ג'וזף ווטסון', field: 'כימיה', cost: 200, annual_cost: 40, reputation_gain: 10, publish_chance: 0.7, description: 'חוקר נועז המנסה לפענח את סודות היסודות, נחשב פורץ דרך.' },
            { id: 'c4', name: 'הלורד ריצ\'רד סטנפורד', field: 'פיזיקה', cost: 120, annual_cost: 25, reputation_gain: 6, publish_chance: 0.55, description: 'עוקב אחר עבודתו של ניוטון, מתעניין במכניקה ואופטיקה.' },
             { id: 'c5', name: 'הגברת אן פטרסון', field: 'מתמטיקה', cost: 90, annual_cost: 15, reputation_gain: 4, publish_chance: 0.75, description: 'מתמטיקאית מוכשרת, עוסקת בחישובים מורכבים ואלגוריתמים.' }
        ];

        let potentialCandidates = [...initialCandidates]; // Copy for dynamic changes

        const initialProjects = [
            { id: 'p1', name: 'קטלוג צמחים מקומיים', field: 'בוטניקה', cost: 50, potential_reputation: 10, success_chance: 0.8, turns_required: 1, description: 'מיפוי וקטלוג הצומח באזור. יניב פרסום שימושי.' },
            { id: 'p2', name: 'מדידת תנועת ירחי צדק', field: 'אסטרונומיה', cost: 100, potential_reputation: 20, success_chance: 0.6, turns_required: 2, description: 'דרושות תצפיות מדויקות לאורך זמן. עשוי לחשוף סודות שמימיים.' },
            { id: 'p3', name: 'ניסויים בחומצות ובסיסים', field: 'כימיה', cost: 150, potential_reputation: 30, success_chance: 0.4, turns_required: 3, description: 'מחקר מסוכן אך עשוי להוביל לגילויים כימיים חשובים.' },
             { id: 'p4', name: 'פיתוח טלסקופ משופר', field: 'פיזיקה', cost: 200, potential_reputation: 25, success_chance: 0.5, turns_required: 2, description: 'דורש משאבים רבים ותיאוריה פיזיקלית איתנה. יגדיל את יכולות התצפית שלנו.'}
        ];

        let availableProjects = [...initialProjects]; // Copy for dynamic changes

        const events = [
            { type: 'positive', text: 'פטרון עשיר תרם לאקדמיה! התקציב גדל ב-', effect: (gs) => { const amount = Math.floor(Math.random() * 100) + 50; gs.budget += amount; return amount + ' מטבעות.'; } },
            { type: 'negative', text: 'מכשיר יקר התקלקל במעבדה. עלות תיקון:', effect: (gs) => { const amount = Math.floor(Math.random() * 50) + 30; gs.budget -= amount; return amount + ' מטבעות.'; } },
            { type: 'positive', text: 'חוקר שלנו גילה תגלית קטנה אך מעניינת! המוניטין עלה ב-', effect: (gs) => { const amount = Math.floor(Math.random() * 5) + 1; gs.reputation += amount; return amount + ' נקודות.'; } },
            { type: 'negative', text: 'שמועה לא נעימה על האקדמיה הגיעה לציבור. המוניטין ירד ב-', effect: (gs) => { const amount = Math.floor(Math.random() * 5) + 1; gs.reputation = Math.max(0, gs.reputation - amount); return amount + ' נקודות.'; } },
             { type: 'neutral', text: 'נשלח אלינו מכתב מאקדמיה אחרת, המציע שיתוף פעולה עתידי.'}
        ];


        function updateStats() {
            stats.year.textContent = gameState.year;
            stats.reputation.textContent = gameState.reputation;
            stats.budget.textContent = gameState.budget;
            stats.currentResearchers.textContent = gameState.researchers.length;
            stats.publications.textContent = gameState.publications;
             advanceTurnButton.textContent = `התקדם לשנת ${gameState.year + 1}`;

             // Visual feedback for stats (simple pulse animation)
             document.querySelectorAll('.stat-value').forEach(statElement => {
                 statElement.classList.add('pulse-effect');
                 setTimeout(() => {
                     statElement.classList.remove('pulse-effect');
                 }, 500);
             });
        }

        function addLogEntry(text, type = 'info') {
            const li = document.createElement('li');
            li.innerHTML = `<span class="log-year">[${gameState.year}]</span> ${text}`;
            li.classList.add(`log-${type}`); // Add class for styling (e.g., log-success, log-failure, log-info)
            gameLog.prepend(li); // Add to the top
            // Keep log concise - show max 15 entries
            while (gameLog.children.length > 15) {
                gameLog.removeChild(gameLog.lastChild);
            }
             // Optional: scroll log to top to show latest entry
             gameLog.parentElement.scrollTop = 0;
        }

        function renderCandidates() {
            candidateList.innerHTML = ''; // Clear list
            if (potentialCandidates.length === 0) {
                 candidateList.innerHTML = '<li class="info-item">אין מועמדים חדשים כרגע.</li>';
                 return;
            }
            potentialCandidates.forEach(candidate => {
                const li = document.createElement('li');
                const canRecruit = gameState.budget >= candidate.cost;
                li.innerHTML = `
                    <strong>${candidate.name}</strong> (${candidate.field})
                    <p class="item-description">${candidate.description}</p>
                    <span class="item-cost">עלות גיוס: ${candidate.cost} מטבעות</span> |
                    <span class="item-cost">עלות שנתית: ${candidate.annual_cost} מטבעות</span>
                    <button data-id="${candidate.id}" class="recruit-button action-button" ${canRecruit ? '' : 'disabled'}>גייס</button>
                `;
                 li.classList.add('list-item', 'candidate-item');
                candidateList.appendChild(li);
            });

            document.querySelectorAll('.recruit-button').forEach(button => {
                button.addEventListener('click', (e) => {
                    const candidateId = e.target.dataset.id;
                    recruitScientist(candidateId);
                });
            });
        }

        function renderProjects() {
             projectList.innerHTML = ''; // Clear list
             if (availableProjects.length === 0) {
                  projectList.innerHTML = '<li class="info-item">אין הצעות מחקר חדשות כרגע.</li>';
                  return;
             }

             availableProjects.forEach(project => {
                 const li = document.createElement('li');
                 // Check if we have any researchers to assign AND budget
                 const canStart = gameState.researchers.length > 0 && gameState.budget >= project.cost;
                 li.innerHTML = `
                    <strong>${project.name}</strong> (${project.field})
                    <p class="item-description">${project.description}</p>
                    <span class="item-cost">עלות התחלה: ${project.cost} מטבעות</span> |
                    <span class="item-cost">סיכוי הצלחה: ${Math.floor(project.success_chance * 100)}%</span> |
                    <span class="item-cost">ימשך: ${project.turns_required} שנה/שנים</span> |
                    <span class="item-cost">מוניטין פוטנציאלי: ${project.potential_reputation}</span>
                    <button data-id="${project.id}" class="start-project-button action-button" ${canStart ? '' : 'disabled'}>התחל פרויקט</button>
                 `;
                 li.classList.add('list-item', 'project-item');
                 projectList.appendChild(li);
             });

             document.querySelectorAll('.start-project-button').forEach(button => {
                button.addEventListener('click', (e) => {
                    const projectId = e.target.dataset.id;
                    startProject(projectId);
                });
            });
        }

        function renderActiveProjects() {
            activeProjectList.innerHTML = '';
            if (gameState.activeProjects.length === 0) {
                 activeProjectList.innerHTML = '<li class="info-item">אין פרויקטים פעילים כרגע.</li>';
                 return;
            }
            gameState.activeProjects.forEach(project => {
                 const li = document.createElement('li');
                 li.innerHTML = `
                    <strong>${project.name}</strong> (${project.field})
                    <p class="item-description">נותר: ${project.turns_remaining} שנה/שנים</p>
                 `;
                 li.classList.add('list-item', 'active-project-item');
                 activeProjectList.appendChild(li);
            });
        }


        function recruitScientist(candidateId) {
            const candidateIndex = potentialCandidates.findIndex(c => c.id === candidateId);
            const candidate = potentialCandidates[candidateIndex];

            if (candidate && gameState.budget >= candidate.cost) {
                gameState.budget -= candidate.cost;
                gameState.researchers.push(candidate);
                // Remove from potential list
                potentialCandidates.splice(candidateIndex, 1);
                gameState.reputation += candidate.reputation_gain; // Instant small rep gain upon joining
                addLogEntry(`🎉 הצטרפות חדשה! ד"ר/מר/פרופ' ${candidate.name} בתחום ${candidate.field} הצטרפ/ה לאקדמיה. עלות גיוס: ${candidate.cost} מטבעות.`, 'success');
                updateStats();
                renderCandidates(); // Refresh list
                renderProjects(); // Projects might become available
            } else if (!candidate) {
                 addLogEntry(`🧐 ניסיון לגייס מועמד לא קיים.`, 'warning');
            } else {
                addLogEntry(`💰 אין מספיק תקציב כדי לגייס את ${candidate.name}. נדרשים עוד ${candidate.cost - gameState.budget} מטבעות.`, 'warning');
            }
        }

        function startProject(projectId) {
             const projectIndex = availableProjects.findIndex(p => p.id === projectId);
             const project = availableProjects[projectIndex];

             if (project && gameState.budget >= project.cost && gameState.researchers.length > 0) {
                 gameState.budget -= project.cost;
                 gameState.activeProjects.push({ ...project, turns_remaining: project.turns_required });
                 // Remove from available list
                 availableProjects.splice(projectIndex, 1);
                 addLogEntry(`🧪 פרויקט "${project.name}" יצא לדרך! עלות התחלה: ${project.cost} מטבעות. מצפים לתוצאות בעוד ${project.turns_required} שנה/שנים.`, 'info');
                 updateStats();
                 renderProjects(); // Refresh available list
                 renderActiveProjects(); // Refresh active list
             } else if (!project) {
                  addLogEntry(`🧐 ניסיון להתחיל פרויקט לא קיים.`, 'warning');
             } else if (gameState.budget < project.cost) {
                 addLogEntry(`💰 אין מספיק תקציב כדי להתחיל את פרויקט "${project.name}". נדרשים עוד ${project.cost - gameState.budget} מטבעות.`, 'warning');
             } else if (gameState.researchers.length === 0) {
                 addLogEntry(`🧍 גיוס חוקרים הכרחי לפני שניתן להתחיל פרויקט מחקר!`, 'warning');
             }
        }

        function resolveActiveProjects() {
             const completedProjects = [];
             const remainingProjects = [];

             gameState.activeProjects.forEach(project => {
                 project.turns_remaining--;
                 if (project.turns_remaining <= 0) {
                     // Project complete, check for success
                     const success = Math.random() < project.success_chance;
                     if (success) {
                         gameState.reputation += project.potential_reputation;
                         gameState.publications++;
                         addLogEntry(`✅ פרויקט "${project.name}" הושלם בהצלחה מזהירה! המוניטין עלה ב-${project.potential_reputation} נקודות. פורסם מאמר חדש!`, 'success');
                     } else {
                         // Maybe a small rep loss or just no gain or negative outcome
                         gameState.reputation = Math.max(0, gameState.reputation - Math.floor(project.potential_reputation / 4)); // Small penalty on failure
                          addLogEntry(`❌ פרויקט "${project.name}" נתקל בקשיים ולא הניב את התוצאות המקוות. ייתכן שהמוניטין נפגע קלות.`, 'failure');
                     }
                     completedProjects.push(project); // Add to completed list (optional, if we want to show history)
                 } else {
                     remainingProjects.push(project);
                 }
             });
             gameState.activeProjects = remainingProjects;
        }

        function handleResearcherActivities() {
             let totalAnnualCost = 0;
             gameState.researchers.forEach(researcher => {
                  totalAnnualCost += researcher.annual_cost;

                 // Chance for individual researcher publication/contribution
                 if (Math.random() < researcher.publish_chance / 5) { // Reduced chance per year
                     gameState.publications++;
                     const repGain = Math.floor(researcher.reputation_gain / 3); // Smaller gain than project
                     gameState.reputation += repGain;
                     addLogEntry(`📝 ד"ר/מר/פרופ' ${researcher.name} פרסם/ה מאמר עצמאי קצר בתחום ${researcher.field}. המוניטין עלה ב-${repGain} נקודות.`, 'info');
                 }
             });

             gameState.budget -= totalAnnualCost;
             if (totalAnnualCost > 0) {
                 addLogEntry(`💸 שולם שכר ועלויות תחזוקה לחוקרים בסך ${totalAnnualCost} מטבעות.`, 'info');
             }

             if (gameState.budget < 0) {
                  // Handle bankruptcy or severe financial issues
                  addLogEntry(`🚨 תקציב האקדמיה אזל ואף ירד מתחת לאפס! יש להפחית הוצאות או לגייס מימון דחוף!`, 'critical');
                  gameState.reputation = Math.max(0, gameState.reputation - 10); // Reputation hit for bankruptcy
                  // Maybe add mechanics like researchers leaving if budget is negative for too long
             }
        }

        function generateNewOpportunities() {
             // Randomly add new candidates
             if (Math.random() < 0.6) { // 60% chance
                 const newCandidate = {
                      id: `c${Date.now() + Math.random()}`,
                      name: `מועמד/ת חדש/ה מסקרנ/ת`,
                      field: ['פיזיקה', 'ביולוגיה', 'מתמטיקה', 'גאולוגיה', 'כימיה', 'אסטרונומיה', 'רפואה'][Math.floor(Math.random() * 7)],
                      cost: 80 + Math.floor(Math.random() * 150),
                      annual_cost: 10 + Math.floor(Math.random() * 30),
                      reputation_gain: 3 + Math.floor(Math.random() * 8),
                      publish_chance: 0.3 + Math.random() * 0.4,
                      description: 'עשוי/ה להיות תוספת בעלת ערך לאקדמיה.'
                 };
                  // Avoid duplicates by ID (unlikely with Date.now() + random, but good practice)
                  if (!potentialCandidates.find(c => c.id === newCandidate.id) && !gameState.researchers.find(r => r.id === newCandidate.id)) {
                       potentialCandidates.push(newCandidate);
                       addLogEntry(`🔍 מועמד/ת פוטנציאל/ית חדש/ה הופיע/ה ברשימה.`, 'info');
                  }
             }

            // Randomly add new projects
            if (Math.random() < 0.7) { // 70% chance
                 const newProject = {
                     id: `p${Date.now() + Math.random()}`,
                     name: `מחקר בנושא ${['אופטיקה מתקדמת', 'מגנטיות ואלקטרוסטטיקה', 'סיווג מיני חיות חדשים', 'גאומטריה אנליטית', 'תגובות בעירה', 'מפות כוכבים מדויקות'][Math.floor(Math.random() * 6)]}`,
                     field: ['פיזיקה', 'כימיה', 'ביולוגיה', 'מתמטיקה', 'אסטרונומיה'][Math.floor(Math.random() * 5)], // simplified field matching
                     cost: 40 + Math.floor(Math.random() * 150),
                     potential_reputation: 10 + Math.floor(Math.random() * 30),
                     success_chance: 0.3 + Math.random() * 0.5,
                     turns_required: 1 + Math.floor(Math.random() * 2), // 1 to 3 turns
                     description: 'פרויקט מאתגר שעשוי לקדם את הידע בתחום זה.'
                 };
                 if (!availableProjects.find(p => p.id === newProject.id) && !gameState.activeProjects.find(p => p.id === newProject.id)) {
                      availableProjects.push(newProject);
                      addLogEntry(`✨ הצעת פרויקט מחקר חדשה ומסקרנת התקבלה.`, 'info');
                 }
            }
        }

        function triggerRandomEvent() {
             if (Math.random() < 0.4) { // 40% chance each turn
                 const event = events[Math.floor(Math.random() * events.length)];
                 let logText = event.text;
                 let eventClass = event.type;
                 if (event.effect) {
                      logText += event.effect(gameState); // Apply effect and append details to text
                 }
                 addLogEntry(`📢 אירוע אקדמי: ${logText}`, eventClass);
                 randomEventDisplay.textContent = logText; // Display the event prominently for one turn
                 randomEventDisplay.className = `event-display event-${eventClass}`; // Apply class for styling
             } else {
                  randomEventDisplay.textContent = ''; // Clear previous event if no new one
                  randomEventDisplay.className = 'event-display';
             }
        }


        function advanceTurn() {
            // 1. Resolve current year's activities
            resolveActiveProjects(); // Projects tick down or complete
            handleResearcherActivities(); // Pay salaries, chance for passive research
            triggerRandomEvent(); // Potential random event

            // 2. Advance year
            gameState.year++;

            // 3. Receive annual funding (simplified)
            const annualFunding = 250 + Math.floor(gameState.reputation * 0.8); // Base + reputation bonus
            gameState.budget += annualFunding;
            addLogEntry(`👑 התקבל מימון שנתי מפטרון האקדמיה בסך ${annualFunding} מטבעות.`, 'info');


            // 4. Generate new opportunities (candidates, projects)
             generateNewOpportunities();

            // 5. Update UI
            updateStats();
            renderCandidates();
            renderProjects();
            renderActiveProjects();

            // Check for game over conditions (e.g., negative budget for too long, 0 reputation)
            // Or check for win conditions (e.g., high reputation, many publications by certain year)
            // Implement game over/win screens here if desired (beyond scope of this refactor)
        }

        advanceTurnButton.addEventListener('click', advanceTurn);

        // Initial Render
        updateStats();
        renderCandidates();
        renderProjects();
        renderActiveProjects(); // Ensure active projects area is rendered initially (even if empty)
    });
</script>

<style>
    :root {
        --primary-color: #0056b3; /* Darker blue */
        --secondary-color: #5cb85c; /* Green */
        --accent-color: #f0ad4e; /* Orange/Gold */
        --background-color: #f4f7f6; /* Light gray */
        --card-background: #ffffff; /* White */
        --border-color: #dcdcdc; /* Light gray border */
        --text-color: #333; /* Dark gray text */
        --heading-color: #013220; /* Dark green */
        --log-info: #5bc0de; /* Light blue */
        --log-success: #5cb85c; /* Green */
        --log-warning: #f0ad4e; /* Orange */
        --log-failure: #d9534f; /* Red */
        --log-critical: #c9302c; /* Dark red */
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        margin: 0;
        padding: 20px;
    }

    h1 {
        color: var(--heading-color);
        text-align: center;
        margin-bottom: 30px;
    }

    .simulation-container {
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

    .simulation-title, .area-title {
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: bold;
    }

    .stats-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Responsive grid */
        gap: 15px;
        background-color: #e9ecef; /* Lighter background for stats */
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .stats-panel p {
        margin: 0;
        font-size: 1em;
        color: #333;
    }

     .stat-value {
         font-weight: bold;
         color: var(--heading-color); /* Different color for values */
         font-size: 1.1em;
     }

     .pulse-effect {
        animation: pulse 0.5s ease-in-out;
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.05); }
         100% { transform: scale(1); }
     }


    .area-panel {
        margin-top: 20px;
        padding: 15px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: var(--card-background);
    }

    .item-list, .log-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .list-item {
        background-color: var(--background-color);
        padding: 12px 15px;
        margin-bottom: 10px;
        border-radius: 6px;
        border-right: 4px solid var(--accent-color); /* Border on the right for RTL */
        font-size: 0.95em;
        transition: background-color 0.2s ease, transform 0.1s ease;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .list-item:hover {
        background-color: #e0e4e7; /* Slightly darker on hover */
    }

    .candidate-item { border-right-color: var(--secondary-color); }
    .project-item { border-right-color: var(--primary-color); }
    .active-project-item { border-right-color: var(--accent-color); }
    .info-item { border-right-color: var(--log-info); font-style: italic; color: #555; }
     .loading-item { border-right-color: var(--border-color); font-style: italic; color: #555; }


    .item-description {
        font-size: 0.85em;
        color: #555;
        margin: 5px 0;
    }

    .item-cost {
        font-size: 0.8em;
        color: #666;
        margin-top: 5px;
    }


    .action-button {
        padding: 8px 15px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.9em;
        margin-right: 10px; /* Margin on the right for RTL */
        margin-top: 8px;
        transition: background-color 0.3s ease, opacity 0.3s ease;
         align-self: flex-end; /* Align button to the left (visual effect in RTL) */
    }

    .action-button:hover:not(:disabled) {
        background-color: #004085;
    }

    .action-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.6;
    }

    .primary-button {
         background-color: var(--secondary-color); /* Green button for main action */
         margin-right: 0; /* No right margin for the main button */
         width: auto; /* Auto width */
         align-self: flex-start; /* Align to the right in RTL */
    }
     .primary-button:hover:not(:disabled) {
         background-color: #4cae4c;
     }


    .log-panel {
         max-height: 250px; /* Fixed height for log */
         overflow-y: auto; /* Scroll for logs */
         direction: rtl; /* RTL direction for log entries */
         text-align: right;
    }

    .log-list li {
         padding: 8px 12px;
         margin-bottom: 6px;
         border-radius: 4px;
         border-right: 4px solid; /* Border color set by class */
         font-size: 0.9em;
         line-height: 1.5;
         background-color: #f9f9f9;
    }

    .log-year {
        font-weight: bold;
        margin-left: 5px; /* Space after year */
        color: #555;
    }

    .log-info { border-right-color: var(--log-info); color: #222; }
    .log-success { border-right-color: var(--log-success); color: #222; }
    .log-warning { border-right-color: var(--log-warning); color: #222; }
    .log-failure { border-right-color: var(--log-failure); color: #222; }
    .log-critical { border-right-color: var(--log-critical); font-weight: bold; color: var(--log-critical); }


    .event-display {
        margin-top: 15px;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        transition: background-color 0.5s ease;
        min-height: 1.5em; /* Reserve space even when empty */
    }
     .event-positive { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
     .event-negative { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
     .event-neutral { background-color: #e9ecef; color: #333; border: 1px solid #dee2e6; }


    .explanation-button {
        display: block; /* Make the button a block element */
        margin: 30px auto; /* Center the button */
        padding: 12px 25px;
        background-color: var(--accent-color);
        color: var(--heading-color); /* Dark green text */
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
        font-weight: bold;
    }

    .explanation-button:hover:not(:disabled) {
         background-color: #ec971f;
    }

    .explanation-content {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--card-background);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        /* Optional: Add a subtle fade-in transition */
        opacity: 0;
        transform: translateY(10px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }
     .explanation-content.visible {
         opacity: 1;
         transform: translateY(0);
     }


    .explanation-content h2, .explanation-content h3 {
         color: var(--heading-color);
         border-bottom: 1px solid var(--border-color);
         padding-bottom: 5px;
         margin-top: 15px;
    }

     /* Basic responsiveness */
     @media (max-width: 600px) {
         .stats-panel {
             grid-template-columns: 1fr; /* Stack stats on small screens */
         }
         .list-item {
             align-items: stretch; /* Stretch items in flex column */
         }
         .action-button {
             align-self: flex-start; /* Keep buttons aligned left visually (right in RTL) */
             margin-right: 0; /* Remove extra margin */
             width: 100%; /* Full width buttons on small screens */
             text-align: center;
             margin-top: 10px;
         }
         .primary-button {
              align-self: stretch; /* Main button full width */
         }
         .simulation-container, .explanation-content {
              padding: 15px;
         }
     }

</style>
---