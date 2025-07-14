---
title: "קסם ההתססה: המסע המופלא מפולי סויה לטמפה ומיסו"
english_slug: fermentation-magic-soy-tempeh-miso
category: "מדעי המזון"
tags:
  - סויה
  - התססה
  - טמפה
  - מיסו
  - פטריות
  - ביולוגיה
  - מזון מותסס
---
# קסם ההתססה: המסע המופלא מפולי סויה לטמפה ומיסו
האם תהיתם פעם איך פולי סויה צנועים הופכים למזונות-על עשירים בטעם, במרקם ובבריאות כמו טמפה מוצקה או מיסו עמוק? הסוד טמון בקסם מיקרוסקופי עתיק יומין. הצטרפו למעבדה הווירטואלית שלנו וגלו כיצד יצורים זעירים עושים את העבודה הקסומה, ואיך שליטה בתנאים הנכונים הופכת אתכם למאסטרים של התססת סויה! התנסו בסימולציה לפני שצוללים להסבר המלא.

<div id="fermentation-simulator">
    <div class="process-selection">
        <h2>בחרו אתגר התססה:</h2>
        <button id="tempeh-btn" class="process-btn">טמפה</button>
        <button id="miso-btn" class="process-btn">מיסו</button>
    </div>

    <div id="simulation-area" style="display: none;">
        <div class="controls">
            <h2>כוונו את קסם המיקרובים</h2>
            <div class="param-control">
                <label for="temp">טמפרטורה (°C):</label>
                <input type="range" id="temp" min="15" max="45" value="30">
                <span id="temp-value">30</span>
                <span class="condition-indicator" id="temp-indicator"></span>
            </div>
            <div class="param-control">
                <label for="humidity">לחות (%):</label>
                <input type="range" id="humidity" min="40" max="100" value="85">
                <span id="humidity-value">85</span>
                <span class="condition-indicator" id="humidity-indicator"></span>
            </div>
             <div class="param-control">
                <label for="salt">מלח (%):</label>
                <input type="range" id="salt" min="0" max="20" value="0" disabled>
                <span id="salt-value">0</span>
                 <span class="condition-indicator" id="salt-indicator"></span>
            </div>
            <div class="param-control">
                <label>השחקן המרכזי:</label>
                <span id="microbe-value"></span>
            </div>


            <button id="start-sim-btn">שגרו את המיקרובים!</button>
        </div>

        <div class="simulation-display">
            <h2>מעקב אחר ההתפתחות</h2>
            <div id="soy-display">
                <div class="soy-content">
                     <p>בחרו אתגר והתחילו לכייל את התנאים...</p>
                </div>
                 <div class="progress-bar"></div>
            </div>
            <div id="feedback">
                <p class="message"></p>
                <p class="details"></p>
            </div>
             <div id="sim-time">
                <span id="sim-time-label">זמן סימולציה:</span> <span id="sim-time-value">0</span> <span id="sim-time-unit">שעות</span>
            </div>
        </div>
    </div>
     <button id="reset-sim-btn" style="display: none; margin-top: 20px;">התחילו מחדש את הניסוי</button>
</div>

<button id="toggle-explanation" style="margin-top: 20px;">הצגת הסבר המאסטר-שף למיקרוביולוגיה</button>

<div id="explanation" style="display: none; margin-top: 20px;">
    <h2>הצלילה העמוקה לקסם ההתססה של סויה</h2>

    <h3>אמנות ההתססה: לא רק שימור, אלא יצירת טעם וחיים!</h3>
    <p>התססה היא תהליך ביוכימי פלאי שבו צבא זעיר של מיקרואורגניזמים (חיידקים, שמרים, פטריות) מפרק חומרים מורכבים למרכיבים פשוטים יותר, לרוב בהיעדר חמצן. מעבר לשימור מזון (על ידי יצירת סביבה חומצית או אלכוהולית שמפריעה למזיקים), התססה מעניקה למזון עומק טעם, מרקם ייחודי, ולעיתים אף מעלה את ערכו התזונתי והופכת אותו קל יותר לעיכול. חשבו על גבינות, יוגורט, לחם מחמצת, ואפילו שוקולד וקפה – כולם תוצרי קסם התססה!</p>

    <h3>השחקנים המרכזיים בזירת התססת הסויה</h3>
    <ul>
        <li><strong>צבא קורי הפלא: פטריות Rhizopus (לדוגמה R. oligosporus) עבור טמפה:</strong> דמיינו רשת עדינה וחזקה של קורים לבנים (מיצלה) שעוטפת כל פול סויה ומחברת את כולם לגוש אחד מוצק כמו "עוגת סויה". זו העבודה של פטריות ה-Rhizopus! הן אלופות בפירוק חלבונים ושומנים, הופכות את הסויה לזמינה יותר מבחינה תזונתית ומוסיפות טעם אגוזי עשיר. הן עובדות בזריזות יחסית ודורשות סביבה חמה ולחה אך מאווררת היטב.</li>
        <li><strong>מהנדסי הטעם המורכב: פטריית Aspergillus oryzae ("קוֹג'י") בשילוב חיידקים ושמרים עבור מיסו:</strong> Koji היא לא פטרייה אחת, אלא שם לתערובת דגנים (לרוב אורז או שעורה) שעליה גודלה פטריית Aspergillus oryzae. פטרייה זו היא מפעל אנזימים מהלך! היא מייצרת אנזימים שמפרקים עמילנים לסוכרים וחלבונים לחומצות אמינו – אבני הבניין של טעם האומאמי. לאחר שקוג'י עשה את עבודתו הראשונית, התערובת מעורבבת עם פולי סויה מבושלים, מלח (המלח הוא שומר הסף, רק עמידים נשארים) ונבחרת של חיידקי חומצה לקטית ושמרים. אלה ממשיכים את ההתססה לאורך חודשים ואפילו שנים, ויוצרים את קשת הטעמים והניחוחות המורכבת והאינסופית של המיסו.</li>
    </ul>

    <h3>טמפה: המהפך המהיר (1-2 ימים)</h3>
    <p>המטרה: לגרום לפטריית Rhizopus לגדול וללכוד את הפולים ברשת לבנה מוצקה.</p>
    <ol>
        <li>**הכנת שדה הקרב:** פולי סויה עוברים בישול, קילוף (כדי שהפטרייה תחדור בקלות) וחצייה. ייבוש עדין לאחר הבישול קריטי למניעת עובשים רעים.</li>
        <li>**שילוח הכוחות:** הפולים מצוננים ומעורבבים עם "סטארטר" - נבגי הפטרייה. כל פול צריך להיות מצופה היטב.</li>
        <li>**שליטה באקלים:** הפטרייה זקוקה לסאונה מבוקרת: חום יציב (30°C-31°C זהב!) ולחות גבוהה בסביבה, אך לא מים עומדים על הפולים.</li>
        <li>**נשימה עמוקה:** ה-Rhizopus חובבת חמצן (אירובית). לכן, אורזים את הפולים בשקיות או מכלים עם חורים קטנים לאוורור.</li>
        <li>**הפלא הלבן:** כשהתנאים מושלמים, הפטרייה גדלה במהירות, יוצרת את המיצלה הלבנה הצפופה שהופכת את הפולים לגוש אחד. זה הסימן לטמפה איכותית!</li>
        <li>**הזמן הנכון:** בדרך כלל 24-48 שעות. אם התהליך נמשך מדי או התנאים לא טובים, עלולים להופיע כתמים שחורים (נבגים, פחות רצויים) או, גרוע מכך, עובשים מזיקים אחרים.</li>
    </ol>

    <h3>מיסו: מסע ההתבגרות הארוך (חודשים עד שנים)</h3>
    <p>המטרה: פירוק איטי ועמוק של הסויה והדגן ויצירת טעמים מורכבים על ידי מגוון מיקרובים.</p>
    <ol>
        <li>**בניית הבסיס:** מבשלים את פולי הסויה עד לרכות קיצונית ומועכים למשחה. במקביל, מכינים את הקוג'י – מצע שעליו גודלה פטריית Aspergillus oryzae בתנאים מבוקרים.</li>
        <li>**האיחוד הגדול:** משחת הסויה והקוג'י מערבבים יחד.</li>
        <li>**צוות העילית + שומר הסף:** מוסיפים כמות נדיבה של מלח (5%-20%!) – הוא המגן מפני מיקרובים רעים ומאפשר רק לצוות המועדף (חיידקי חומצה לקטית ושמרים עמידים למלח) לשגשג. מוסיפים גם את התרביות הנכונות של החיידקים והשמרים.</li>
        <li>**תרדמת החורף (או הקיץ...):** התערובת מהודקת היטב בכלי התססה (להרחקת אוויר - תהליך אנאירובי) ועליה מונחת משקולת. עכשיו מתחיל החלק הארוך – התבגרות איטית בטמפרטורת החדר (או קרירה יותר) למשך חודשים, שנה, ואף יותר. במהלך זמן זה, אנזימי הקוג'י והמיקרובים ממשיכים את הפירוק והופכים את התערובת הגולמית למשחת מיסו עשירה ומלאת אומאמי.</li>
        <li>**המלח כמאסטרו:** ריכוז המלח שולט בקצב ובסוג ההתססה. מעט מדי מלח = סכנת קלקול. יותר מדי מלח = התססה איטית מדי או עצירה.</li>
    </ol>

    <h3>מה מניע (או עוצר) את הקסם? גורמים קריטיים להצלחה</h3>
    <ul>
        <li>**טמפרטורה:** כל מיקרוב הוא בררן! יש לו טווח טמפרטורות אידיאלי. סטייה גדולה מדי והתהליך יתקע, ישנה כיוון, או יזמין שחקנים לא רצויים.</li>
        <li>**לחות ואוורור:** מיקרובים צריכים מים, אבל יותר מדי מים חופשיים על פני השטח זה מתכון לקלקול. אוורור נכון (בטמפה) או היעדרו (במיסו) קריטי לסוג המיקרובים שישגשגו.</li>
        <li>**זמן:** סבלנות מפתח במיסו, זריזות בטמפה. יותר מדי זמן בטמפה = נבגים שחורים וטעם מריר. פחות מדי זמן במיסו = טעם לא מפותח.</li>
        <li>**איכות הסטארטר:** "זרע" מיקרוביאלי טרי, חי ונכון למוצר הוא חובה. מיקרובים חלשים או לא נכונים לא יעשו את העבודה.</li>
        <li>**היגיינה:** סביבת עבודה נקייה מונעת תחרות לא רצויה של חיידקי קלקול ועובשים רעים.</li>
    </ul>

    <h3>טמפה מול מיסו: קרב המיקרובים (והתנאים)</h3>
    <ul>
        <li>**הצוות:** טמפה – בעיקר פטריית Rhizopus אחת, פשוט ויעיל. מיסו – קוג'י (Aspergillus oryzae) ואחריו נבחרת מגוונת של חיידקי חומצה לקטית ושמרים, מורכב ועשיר.</li>
        <li>**הקצב:** טמפה – מהיר (1-2 ימים), תוצאות תוך שעות! מיסו – סבלני (חודשים-שנים), מסע ארוך לטעם.</li>
        <li>**הטמפרטורה:** טמפה – חם ויציב (סביב 30°C) כל הזמן. מיסו – שלב קוג'י חם, ואחריו התבגרות בטמפרטורת חדר או קרירה יותר.</li>
        <li>**האוויר:** טמפה – דורש חמצן (אירובי), נושם דרך חורים. מיסו – לא דורש חמצן (אנאירובי בעיקרו), מהודק היטב.</li>
        <li>**המלח:** טמפה – כמעט בלי מלח (או ממש מעט). מיסו – הרבה מלח (שומר ומכוון).</li>
        <li>**התוצר:** טמפה – גוש מוצק, לבן ויפה של פולים מחוברים. מיסו – משחה סמיכה, לרוב בצבעים שונים.</li>
    </ul>
</div>

<script>
    const tempehBtn = document.getElementById('tempeh-btn');
    const misoBtn = document.getElementById('miso-btn');
    const simulationArea = document.getElementById('simulation-area');
    const tempControl = document.getElementById('temp');
    const humidityControl = document.getElementById('humidity');
    const saltControl = document.getElementById('salt');
    const tempValueSpan = document.getElementById('temp-value');
    const humidityValueSpan = document.getElementById('humidity-value');
    const saltValueSpan = document.getElementById('salt-value');
    const tempIndicator = document.getElementById('temp-indicator');
    const humidityIndicator = document.getElementById('humidity-indicator');
    const saltIndicator = document.getElementById('salt-indicator');
    const microbeValueSpan = document.getElementById('microbe-value');
    const startSimBtn = document.getElementById('start-sim-btn');
    const resetSimBtn = document.getElementById('reset-sim-btn');
    const soyDisplay = document.getElementById('soy-display');
    const soyContent = soyDisplay.querySelector('.soy-content');
    const progressBar = soyDisplay.querySelector('.progress-bar');
    const feedbackArea = document.getElementById('feedback').querySelector('.message');
     const feedbackDetails = document.getElementById('feedback').querySelector('.details');
    const simTimeLabelSpan = document.getElementById('sim-time-label');
    const simTimeValueSpan = document.getElementById('sim-time-value');
     const simTimeUnitSpan = document.getElementById('sim-time-unit');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let currentProcess = null;
    let simulationInterval = null;
    let simulationTime = 0; // Represents a conceptual progression step, not literal time.
    let maxSimSteps = 100; // Total steps for simulation
    let currentSimProgress = 0; // Percentage 0-100

    const optimalConditions = {
        tempeh: {
            temp: { min: 28, max: 32 },
            humidity: { min: 80, max: 95 },
            salt: { min: 0, max: 1 }, // Very low salt inhibits Rhizopus
            microbe: 'Rhizopus (פטרייה)',
            timeUnit: 'שעות סימולציה',
            colors: { start: '#f8f8f8', progress: '#ffffff', optimal: '#f0f0f0', fail: '#ffcccc' }
        },
        miso: {
            temp: { min: 20, max: 25 }, // Focus on aging temp
            humidity: { min: 60, max: 80 }, // As a paste consistency
            salt: { min: 10, max: 15 }, // High salt concentration
            microbe: 'Aspergillus oryzae + חיידקים ושמרים',
            timeUnit: 'שלבי התבגרות',
            colors: { start: '#f8f8f8', progress: '#ffeebb', optimal: '#d4b991', fail: '#ffcccc' }
        }
    };

    function updateControlValues() {
        tempValueSpan.textContent = tempControl.value;
        humidityValueSpan.textContent = humidityControl.value;
        saltValueSpan.textContent = saltControl.value;
        updateConditionIndicators();
    }

     function updateConditionIndicators() {
        if (!currentProcess) return;
        const conditions = optimalConditions[currentProcess];
        const currentTemp = parseInt(tempControl.value);
        const currentHumidity = parseInt(humidityControl.value);
        const currentSalt = parseInt(saltControl.value);

        setIndicator(tempIndicator, currentTemp, conditions.temp);
        setIndicator(humidityIndicator, currentHumidity, conditions.humidity);

         // Salt indicator logic is process-dependent
         if (currentProcess === 'miso') {
              setIndicator(saltIndicator, currentSalt, conditions.salt);
         } else { // tempeh
              // Tempeh needs LOW salt. Treat high salt as failure condition range.
              // Optimal is within the min/max (0-1). Suboptimal is slightly above. Failure is high.
              if (currentSalt >= conditions.salt.min && currentSalt <= conditions.salt.max) {
                  saltIndicator.className = 'condition-indicator optimal'; // Low salt is good
              } else if (currentSalt > conditions.salt.max && currentSalt <= conditions.salt.max + 3) { // Small buffer
                  saltIndicator.className = 'condition-indicator suboptimal'; // Slightly high salt is suboptimal
              }
              else {
                   saltIndicator.className = 'condition-indicator failing'; // High salt is failing
              }
         }
     }

    function setIndicator(element, currentValue, optimalRange) {
        if (currentValue >= optimalRange.min && currentValue <= optimalRange.max) {
            element.className = 'condition-indicator optimal';
        } else if ((currentValue >= optimalRange.min - 5 && currentValue < optimalRange.min) || (currentValue > optimalRange.max && currentValue <= optimalRange.max + 5)) { // +/- 5 degree buffer
             element.className = 'condition-indicator suboptimal';
        }
        else {
            element.className = 'condition-indicator failing';
        }
    }


    function selectProcess(processType) {
        if (simulationInterval) {
            resetSimulation(); // Reset if a simulation was running
        }
        currentProcess = processType;
        simulationArea.style.display = 'flex';
        resetSimBtn.style.display = 'none';
        startSimBtn.style.display = 'block';
        soyContent.innerHTML = '<p>מכין פולי סויה לתהליך...</p>';
         feedbackArea.textContent = 'כוונו את התנאים להתססה מושלמת!';
        feedbackDetails.textContent = '';
        currentSimProgress = 0;
        simulationTime = 0;
        simTimeValueSpan.textContent = 0;
        progressBar.style.width = '0%';
         progressBar.style.backgroundColor = '#4CAF50'; // Default green progress

        // Set default values and ranges based on process
        const conditions = optimalConditions[processType];
        tempControl.value = Math.round((conditions.temp.min + conditions.temp.max) / 2);
        humidityControl.value = Math.round((conditions.humidity.min + conditions.humidity.max) / 2);

        if (processType === 'tempeh') {
             saltControl.value = 0;
             saltControl.disabled = true;
             saltControl.style.opacity = 0.5; // Visually indicate disabled
             tempControl.min = 25; tempControl.max = 35; // Narrower range for Tempeh sim
             humidityControl.min = 70; humidityControl.max = 100;
             saltControl.min = 0; saltControl.max = 5; // Max useful range for Tempeh sim salt check
             simTimeLabelSpan.textContent = `זמן סימולציה: `;
             simTimeUnitSpan.textContent = conditions.timeUnit;
             // Initial Tempeh display
             soyDisplay.style.backgroundColor = optimalConditions.tempeh.colors.start;
              soyDisplay.style.borderColor = '#ccc';
              soyDisplay.classList.remove('miso-style', 'failed');
              soyDisplay.classList.add('tempeh-style');

        } else { // miso
             saltControl.value = Math.round((conditions.salt.min + conditions.salt.max) / 2);
             saltControl.disabled = false;
             saltControl.style.opacity = 1;
             tempControl.min = 15; tempControl.max = 30; // Wider range, lower default for Miso sim
             humidityControl.min = 50; humidityControl.max = 90;
             saltControl.min = 0; saltControl.max = 20; // Full range for Miso sim salt check
             simTimeLabelSpan.textContent = `שלב התבגרות: `;
             simTimeUnitSpan.textContent = conditions.timeUnit;
              // Initial Miso display
             soyDisplay.style.backgroundColor = optimalConditions.miso.colors.start;
              soyDisplay.style.borderColor = '#ccc';
              soyDisplay.classList.remove('tempeh-style', 'failed');
              soyDisplay.classList.add('miso-style');
        }

        microbeValueSpan.textContent = conditions.microbe;
        updateControlValues();
    }

    function calculateConditionScore() {
        if (!currentProcess) return 0;
        const conditions = optimalConditions[currentProcess];
        const currentTemp = parseInt(tempControl.value);
        const currentHumidity = parseInt(humidityControl.value);
        const currentSalt = parseInt(saltControl.value);

        let score = 0;
        const maxScorePerParam = 1;

        // Temperature score
        if (currentTemp >= conditions.temp.min && currentTemp <= conditions.temp.max) {
            score += maxScorePerParam;
        } else {
            // Penalize further away
            const dist = Math.min(Math.abs(currentTemp - conditions.temp.min), Math.abs(currentTemp - conditions.temp.max));
             // Simple linear decrease: 0 score when 10 units away from range
            score += Math.max(0, maxScorePerParam - dist / 10);
        }

        // Humidity score
        if (currentHumidity >= conditions.humidity.min && currentHumidity <= conditions.humidity.max) {
            score += maxScorePerParam;
        } else {
             const dist = Math.min(Math.abs(currentHumidity - conditions.humidity.min), Math.abs(currentHumidity - conditions.humidity.max));
             score += Math.max(0, maxScorePerParam - dist / 20); // Humidity might be less sensitive, larger divisor
        }

         // Salt score - Process dependent
         if (currentProcess === 'miso') {
              if (currentSalt >= conditions.salt.min && currentSalt <= conditions.salt.max) {
                  score += maxScorePerParam;
              } else {
                   const dist = Math.min(Math.abs(currentSalt - conditions.salt.min), Math.abs(currentSalt - conditions.salt.max));
                    score += Math.max(0, maxScorePerParam - dist / 5); // Salt is quite sensitive
              }
         } else { // tempeh - penalize high salt
              if (currentSalt >= conditions.salt.min && currentSalt <= conditions.salt.max) { // 0-1% is optimal
                  score += maxScorePerParam;
              } else {
                  // Linear decrease based on how much salt is present above optimal max (1)
                   const saltAboveOptimal = Math.max(0, currentSalt - conditions.salt.max);
                   score += Math.max(0, maxScorePerParam - saltAboveOptimal / 3); // Even small amounts hurt tempeh
              }
         }


        // Normalize score to 0-1 range
        return score / (maxScorePerParam * 3); // 3 parameters total
    }


    function startSimulation() {
        if (!currentProcess) {
            feedbackArea.textContent = 'בחרו תהליך (טמפה או מיסו) כדי להתחיל.';
            return;
        }

        // Disable controls and start button
        tempControl.disabled = true;
        humidityControl.disabled = true;
        saltControl.disabled = true; // Salt is enabled/disabled by process selection anyway
        startSimBtn.style.display = 'none';
        resetSimBtn.style.display = 'block';

        soyContent.innerHTML = '<p>התססה יוצאת לדרך...</p>';
         feedbackArea.textContent = 'מעקב אחר קצב ההתפתחות...';
         feedbackDetails.textContent = '';


        simulationInterval = setInterval(() => {
            const conditionsScore = calculateConditionScore(); // 0 to 1
            let progressThisStep = conditionsScore * 1; // How much progress per interval (can be adjusted)
            let timeProgressThisStep = conditionsScore * (currentProcess === 'tempeh' ? 2 : 0.5); // Simulate time passing faster/slower based on conditions

            currentSimProgress += progressThisStep;
            simulationTime += timeProgressThisStep;


            const displayTime = currentProcess === 'tempeh' ? Math.round(simulationTime) : Math.round(simulationTime);
             simTimeValueSpan.textContent = displayTime;

            // Update progress bar
            const clampedProgress = Math.min(100, Math.max(0, currentSimProgress));
             progressBar.style.width = clampedProgress + '%';

            // Update visual display based on progress and score
            const conditions = optimalConditions[currentProcess];
             const baseColor = conditions.colors.start;
             const progressColor = conditions.colors.progress;
             const failColor = conditions.colors.fail;


             let backgroundColor;
             let feedbackMsg = '';
             let detailsMsg = '';

            if (conditionsScore >= 0.8) {
                // Optimal or near-optimal
                 const progressMix = clampedProgress / 100;
                 backgroundColor = mixColors(progressColor, conditions.colors.optimal, progressMix);
                 feedbackMsg = `תנאים מצוינים! הקסם קורה כמתוכנן.`;
                 soyContent.innerHTML = `<p>התפתחות מעולה!</p><p>${currentProcess === 'tempeh' ? 'המיצלה גדלה במהירות...' : 'הטעמים מתפתחים בעומק...'}</p><p>התקדמות: ${Math.round(clampedProgress)}%</p>`;
                  soyDisplay.classList.remove('suboptimal', 'failing');
                 soyDisplay.classList.add('optimal');

            } else if (conditionsScore >= 0.4) {
                // Suboptimal
                 const progressMix = clampedProgress / 100;
                 backgroundColor = mixColors(baseColor, progressColor, progressMix * 0.8); // Slower color change
                 feedbackMsg = `התנאים לא מושלמים... הקצב איטי יותר.`;
                 detailsMsg = getConditionFeedback(currentProcess);
                 soyContent.innerHTML = `<p>התפתחות איטית...</p><p>${detailsMsg}</p><p>התקדמות: ${Math.round(clampedProgress)}%</p>`;
                 soyDisplay.classList.remove('optimal', 'failing');
                  soyDisplay.classList.add('suboptimal');

            } else {
                // Failing
                 const progressMix = clampedProgress / 100; // Still show some initial color change
                 backgroundColor = mixColors(baseColor, failColor, progressMix * 0.5 + 0.3); // Move towards fail color faster
                 feedbackMsg = `בעיה! התנאים גורמים לכישלון התהליך.`;
                 detailsMsg = getConditionFeedback(currentProcess);
                  soyContent.innerHTML = `<p>התססה נכשלת...</p><p>${detailsMsg}</p><p>התקדמות: ${Math.round(clampedProgress)}%</p>`;
                  soyDisplay.classList.remove('optimal', 'suboptimal');
                 soyDisplay.classList.add('failing');
                 progressBar.style.backgroundColor = '#dc3545'; // Red progress bar on failure
            }

             soyDisplay.style.backgroundColor = backgroundColor;
             feedbackArea.textContent = feedbackMsg;
             feedbackDetails.textContent = detailsMsg;


            // Check for end conditions
            if (currentSimProgress >= maxSimSteps || (conditionsScore < 0.3 && simulationTime > 10)) { // Finish on progress or fail early if bad
                 clearInterval(simulationInterval);
                 simulationInterval = null;

                 let finalMessage = "";
                 if (currentSimProgress >= maxSimSteps && conditionsScore >= 0.5) { // Successful completion requires sufficient progress and score
                     finalMessage = currentProcess === 'tempeh' ? "התססה הושלמה בהצלחה! טמפה מוכנה ואיכותית." : "ההתבגרות הסתיימה בהצלחה! מיסו מוכן ובעל טעם עמוק.";
                      soyContent.innerHTML = `<p>🎉 הצלחה! 🎉</p><p>${finalMessage}</p>`;
                       soyDisplay.style.backgroundColor = conditions.colors.optimal; // Final success color
                       soyDisplay.classList.remove('suboptimal', 'failing');
                       soyDisplay.classList.add('optimal');

                 } else {
                     finalMessage = currentProcess === 'tempeh' ? "התססה נכשלה." : "ההתבגרות נכשלה.";
                     feedbackArea.textContent = `${finalMessage}`;
                      feedbackDetails.textContent = `תנאים לא מתאימים מנעו את השלמת התהליך. הסיבה: ${getConditionFeedback(currentProcess, true)}`;
                     soyContent.innerHTML = `<p>💔 כישלון... 💔</p><p>${finalMessage}</p><p>${getConditionFeedback(currentProcess, true)}</p>`;
                      soyDisplay.style.backgroundColor = conditions.colors.fail; // Final failure color
                      soyDisplay.classList.remove('optimal', 'suboptimal');
                      soyDisplay.classList.add('failing');
                      progressBar.style.backgroundColor = '#dc3545'; // Ensure red bar on failure
                 }

                 // Enable controls for reset/new simulation
                 tempControl.disabled = false;
                 humidityControl.disabled = false;
                 if (currentProcess === 'miso') saltControl.disabled = false;
            }

        }, 150); // Update more frequently for smoother simulation feel
    }

     // Helper function to mix two hex/rgb colors
     function mixColors(color1, color2, weight) {
         // weight is 0 to 1, where 0 is 100% color1 and 1 is 100% color2
         const rgb1 = parseColor(color1);
         const rgb2 = parseColor(color2);

         const r = Math.round(rgb1[0] * (1 - weight) + rgb2[0] * weight);
         const g = Math.round(rgb1[1] * (1 - weight) + rgb2[1] * weight);
         const b = Math.round(rgb1[2] * (1 - weight) + rgb2[2] * weight);

         return `rgb(${r}, ${g}, ${b})`;
     }

     // Helper function to parse hex or rgb color string into [r, g, b] array
     function parseColor(color) {
         if (color.startsWith('#')) {
             const hex = color.slice(1);
             const r = parseInt(hex.substring(0, 2), 16);
             const g = parseInt(hex.substring(2, 4), 16);
             const b = parseInt(hex.substring(4, 6), 16);
             return [r, g, b];
         } else if (color.startsWith('rgb(')) {
             return color.slice(4, -1).split(',').map(Number);
         }
          // Add more color types if needed (e.g., rgba)
         return [0, 0, 0]; // Default to black on parse failure
     }


     function getConditionFeedback(processType, isFinal = false) {
        if (!processType) return '';
        const conditions = optimalConditions[processType];
        const currentTemp = parseInt(tempControl.value);
        const currentHumidity = parseInt(humidityControl.value);
        const currentSalt = parseInt(saltControl.value);

        let feedback = [];

        // Temperature feedback
        if (currentTemp < conditions.temp.min) feedback.push(`טמפרטורה נמוכה מדי (${currentTemp}°C). קצב התססה איטי או נעצר.`);
        else if (currentTemp > conditions.temp.max) feedback.push(`טמפרטורה גבוהה מדי (${currentTemp}°C). סיכון לקלקול או עובש לא רצוי.`);

        // Humidity feedback
        if (currentHumidity < conditions.humidity.min) feedback.push(`לחות נמוכה מדי (${currentHumidity}%). המיקרובים מתייבשים ולא פועלים.`);
        else if (currentHumidity > conditions.humidity.max) feedback.push(`לחות גבוהה מדי (${currentHumidity}%). סיכון לצמיחת בקטריות רעות.`);

        // Salt feedback
        if (processType === 'miso') {
             if (currentSalt < conditions.salt.min) feedback.push(`מלח נמוך מדי (${currentSalt}%). סיכון גבוה לקלקול ע"י חיידקים לא רצויים.`);
             else if (currentSalt > conditions.salt.max) feedback.push(`מלח גבוה מדי (${currentSalt}%). מעכב את פעילות המיקרובים הרצויים.`);
        } else { // tempeh
             if (currentSalt > conditions.salt.max) feedback.push(`מלח גבוה מדי (${currentSalt}%). מעכב את צמיחת פטריית הטמפה.`);
             // No specific feedback for salt < min as min is 0, and 0 salt is generally good for tempeh
        }

        if (feedback.length === 0) {
             if (isFinal) return 'התנאים היו אופטימליים אך אולי היה כשל אחר (הדמיה מפושטת).'; // Should ideally not happen with optimal conditions in this sim
             return 'התנאים בטווח טוב, אך אולי לא מושלמים.'; // Should not happen if score is < 0.8
        }

        return feedback.join(', ');
    }


    function resetSimulation() {
        clearInterval(simulationInterval);
        simulationInterval = null;
        currentSimProgress = 0;
        simulationTime = 0;

         if (currentProcess) {
             simTimeValueSpan.textContent = 0;
              simTimeLabelSpan.textContent = currentProcess === 'tempeh' ? `זמן סימולציה: ` : `שלב התבגרות: `;
             simTimeUnitSpan.textContent = optimalConditions[currentProcess].timeUnit;

         } else {
             simTimeValueSpan.textContent = 0;
             simTimeLabelSpan.textContent = `זמן סימולציה: `;
             simTimeUnitSpan.textContent = 'שעות';
         }

        // Reset controls to initial values for the selected process, or defaults if none selected yet
         if (currentProcess) {
            const conditions = optimalConditions[currentProcess];
            tempControl.value = Math.round((conditions.temp.min + conditions.temp.max) / 2);
            humidityControl.value = Math.round((conditions.humidity.min + conditions.humidity.max) / 2);
            if (currentProcess === 'miso') {
                saltControl.value = Math.round((conditions.salt.min + conditions.salt.max) / 2);
                saltControl.disabled = false;
                 saltControl.style.opacity = 1;
            } else { // tempeh
                 saltControl.value = 0;
                 saltControl.disabled = true;
                 saltControl.style.opacity = 0.5;
            }
             tempControl.min = currentProcess === 'tempeh' ? 25 : 15;
             tempControl.max = currentProcess === 'tempeh' ? 35 : 30;
             humidityControl.min = currentProcess === 'tempeh' ? 70 : 50;
             humidityControl.max = currentProcess === 'tempeh' ? 100 : 90;
             saltControl.min = currentProcess === 'tempeh' ? 0 : 0;
             saltControl.max = currentProcess === 'tempeh' ? 5 : 20;

         } else { // Default state before process selection
             tempControl.value = 30; tempControl.min = 15; tempControl.max = 45;
             humidityControl.value = 85; humidityControl.min = 40; humidityControl.max = 100;
              saltControl.value = 0; saltControl.min = 0; saltControl.max = 20;
              saltControl.disabled = true; saltControl.style.opacity = 0.5;
         }
         updateControlValues();


        // Enable controls
        tempControl.disabled = false;
        humidityControl.disabled = false;
        if (currentProcess === 'miso') saltControl.disabled = false; // Only re-enable salt if miso was selected

        // Reset display and feedback
        soyContent.innerHTML = currentProcess ? '<p>מוכן לכיוון תנאים...</p>' : '<p>בחרו תהליך והתחילו סימולציה...</p>';
         soyDisplay.style.backgroundColor = currentProcess ? optimalConditions[currentProcess].colors.start : '#f8f8f8';
        soyDisplay.style.borderColor = '#ccc';
         soyDisplay.classList.remove('optimal', 'suboptimal', 'failing', 'tempeh-style', 'miso-style');
         if (currentProcess) soyDisplay.classList.add(currentProcess + '-style');


        feedbackArea.textContent = currentProcess ? 'בחרו תנאים והתחילו סימולציה.' : '';
        feedbackDetails.textContent = '';

         progressBar.style.width = '0%';
         progressBar.style.backgroundColor = '#4CAF50'; // Reset to green


        // Show start button, hide reset
        startSimBtn.style.display = 'block';
        resetSimBtn.style.display = 'none';
    }

    // Event Listeners
    tempehBtn.addEventListener('click', () => selectProcess('tempeh'));
    misoBtn.addEventListener('click', () => selectProcess('miso'));

    tempControl.addEventListener('input', updateControlValues);
    humidityControl.addEventListener('input', updateControlValues);
    saltControl.addEventListener('input', updateControlValues);

    startSimBtn.addEventListener('click', startSimulation);
    resetSimBtn.addEventListener('click', resetSimulation);

    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצגת הסבר המאסטר-שף למיקרוביולוגיה';
    });

    // Initial state setup
     resetSimulation(); // Set initial state correctly including disabled controls and text
     simulationArea.style.display = 'none'; // Hide sim area until process selected
     resetSimBtn.style.display = 'none';


</script>

<style>
    #fermentation-simulator {
        font-family: 'Rubik', sans-serif; /* Use a more modern font */
        border: 1px solid #e0e0e0; /* Lighter border */
        padding: 25px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        background-color: #ffffff; /* White background */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Subtle shadow */
    }

    #fermentation-simulator h1, #fermentation-simulator h2 {
        color: #2c3e50; /* Darker, modern heading color */
        text-align: center;
        margin-bottom: 20px;
    }

    .process-selection {
        text-align: center;
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid #f0f0f0; /* Light border */
    }

    .process-btn {
        padding: 12px 25px;
        margin: 0 10px;
        font-size: 17px;
        cursor: pointer;
        border: none; /* No border */
        border-radius: 30px; /* Pill shape */
        background-color: #3498db; /* Muted blue */
        color: white;
        transition: all 0.3s ease; /* Smooth transitions */
        font-weight: bold;
        outline: none;
    }

    .process-btn:hover {
        background-color: #2980b9; /* Darker blue on hover */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    .process-btn:active {
         transform: scale(0.98); /* Press effect */
    }


    #simulation-area {
        display: flex;
        gap: 30px; /* More space between sections */
        flex-wrap: wrap;
    }

    .controls, .simulation-display {
        flex: 1;
        min-width: 300px;
        padding: 20px;
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        background-color: #fdfdfd; /* Slightly off-white */
        box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05); /* Inner shadow */
    }

     .controls {
         display: flex;
         flex-direction: column;
         gap: 20px; /* More space between controls */
     }

    .param-control {
        display: flex;
        align-items: center;
        gap: 15px; /* Space for indicator */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .param-control label {
        flex-shrink: 0;
        width: 120px; /* Slightly wider label */
        font-weight: bold;
        color: #555;
    }

     .param-control input[type="range"] {
         flex-grow: 1;
         -webkit-appearance: none;
         appearance: none;
         height: 8px; /* Thicker slider */
         background: #ddd;
         outline: none;
         opacity: 0.7;
         transition: opacity .2s;
         border-radius: 5px;
         margin: 0; /* Remove default margin */
     }

     .param-control input[type="range"]:hover {
        opacity: 1;
     }

     .param-control input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        background: #3498db; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }

      .param-control input[type="range"]::-moz-range-thumb {
        width: 18px;
        height: 18px;
        background: #3498db; /* Blue thumb */
        cursor: pointer;
        border-radius: 50%;
         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
     }


    .param-control span {
        width: 35px; /* Wider for value + indicator space */
        text-align: center;
        font-weight: bold;
        color: #333;
    }

     .condition-indicator {
         display: inline-block;
         width: 12px;
         height: 12px;
         border-radius: 50%;
         margin-left: 5px;
         transition: background-color 0.3s ease;
     }

     .condition-indicator.optimal { background-color: #2ecc71; } /* Green */
     .condition-indicator.suboptimal { background-color: #f39c12; } /* Orange */
     .condition-indicator.failing { background-color: #e74c3c; } /* Red */


    #start-sim-btn, #reset-sim-btn {
        padding: 14px 30px; /* Larger buttons */
        font-size: 19px;
        cursor: pointer;
        border: none;
        border-radius: 8px; /* Rounded corners */
        color: white;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.1s ease;
        width: 100%;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
         outline: none;
    }

    #start-sim-btn {
        background-color: #2ecc71; /* Green */
    }
    #reset-sim-btn {
        background-color: #e74c3c; /* Red for reset/stop */
     }

    #start-sim-btn:hover { background-color: #27ae60; }
    #reset-sim-btn:hover { background-color: #c0392b; }

     #start-sim-btn:active, #reset-sim-btn:active {
         transform: scale(0.98);
     }


    .simulation-display {
         display: flex;
         flex-direction: column;
         justify-content: space-between;
         position: relative; /* For progress bar positioning */
    }

    #soy-display {
        width: 100%;
        height: 180px; /* Taller display area */
        background-color: #f8f8f8;
        border: 2px solid #ccc;
        border-radius: 8px;
        margin-bottom: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 1em;
        color: #555;
        transition: background-color 0.8s ease, border-color 0.5s ease; /* Smooth visual changes */
        padding: 15px;
         box-sizing: border-box;
         overflow: hidden; /* Hide overflowing pseudo-elements */
         position: relative; /* Needed for pseudo-elements */
    }

     /* Pseudo-elements for visual texture/animation */
     #soy-display::before {
         content: '';
         position: absolute;
         top: 0; left: 0; right: 0; bottom: 0;
         pointer-events: none;
         z-index: 1; /* Above background color */
         opacity: 0; /* Starts hidden */
         transition: opacity 0.8s ease;
     }

     /* Tempeh specific animation */
     #soy-display.tempeh-style.optimal::before {
        /* Simulate mycelium growth */
        background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 70%),
                    url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxjaXJjbGUgY3g9IjEwIiBjY1k9IjEwIiByPSIxMCIgZmlsbD0iI2ZmZiIvPgogICAgcGF0aCBkPSJNMTAgMEExMCAxMCAwIDAgMSAxMCAyMGExMCAxMCAwIDAgMSAwLTIwWm0wIDVhNSA1IDAgMSAwIDAgMTBhNSA1IDAgMSAwIDAtMTBaIiBmaWxsPSIjZTRlNGU0Ii8+Cjwvc3ZnPg=='); /* Simple textured pattern */
        background-size: 30px 30px;
        animation: mycelium-grow 2s infinite linear; /* Subtle animation */
        opacity: 1; /* Fully visible when optimal */
     }

      /* Miso specific animation */
      #soy-display.miso-style.optimal::before {
          /* Simulate color deepening/texture change */
          background: linear-gradient(to bottom right, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0) 50%);
           opacity: 1;
      }

      @keyframes mycelium-grow {
          from { background-position: 0 0; }
          to { background-position: 60px 60px; }
      }

      /* Failure visual cue */
      #soy-display.failing {
          animation: shake 0.5s ease-in-out infinite alternate;
          border-color: #e74c3c;
      }

      @keyframes shake {
          0% { transform: translateX(0); }
          100% { transform: translateX(5px); }
      }


     .soy-content {
         position: relative;
         z-index: 2; /* Ensure text is above pseudo-elements */
         padding: 10px;
     }


    #feedback {
        min-height: 3em; /* Give space for two lines */
         margin-bottom: 10px;
    }

     #feedback .message {
         font-weight: bold;
         color: #333;
         margin-bottom: 5px;
     }
      #feedback .details {
          font-size: 0.9em;
          color: #666;
      }


     #sim-time {
         margin-top: auto; /* Push to bottom */
         font-weight: bold;
         text-align: right;
         color: #555;
     }

     .progress-bar {
         height: 8px; /* Height of the bar */
         width: 0%; /* Starts empty */
         background-color: #4CAF50; /* Green */
         position: absolute;
         bottom: 0;
         left: 0;
         border-bottom-left-radius: 8px;
         transition: width 0.3s ease; /* Smooth progress */
     }

    #explanation {
        border: 1px solid #e0e0e0;
        padding: 25px;
        border-radius: 12px;
        max-width: 850px;
        margin: 20px auto;
        background-color: #ffffff;
         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
         line-height: 1.6; /* Improve readability */
    }

    #explanation h2, #explanation h3 {
        color: #2c3e50;
        margin-bottom: 15px;
    }

    #explanation h3 {
        margin-top: 20px;
        border-bottom: 1px dotted #ccc; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation ul, #explanation ol {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent lists */
    }
     #explanation li {
         margin-bottom: 8px;
     }
     #explanation strong {
         color: #3498db; /* Highlight key terms */
     }


     #toggle-explanation {
         display: block;
         margin: 20px auto;
         padding: 12px 25px;
         font-size: 17px;
         cursor: pointer;
         border: none;
         border-radius: 30px;
         background-color: #95a5a6; /* Gray */
         color: white;
         transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
         outline: none;
         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
     }
      #toggle-explanation:hover {
          background-color: #7f8c8d;
           box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
      }
       #toggle-explanation:active {
         transform: scale(0.98);
     }


     /* Responsive adjustments */
     @media (max-width: 600px) {
         #simulation-area {
             flex-direction: column;
             gap: 20px;
         }

         .controls, .simulation-display {
             min-width: unset;
             width: 100%;
         }

         .process-btn {
             margin: 5px;
             width: calc(50% - 20px); /* Two buttons per line */
             box-sizing: border-box;
         }

         .param-control {
             flex-direction: column;
             align-items: flex-start;
             gap: 5px;
         }
         .param-control label {
             width: auto;
         }
         .param-control input[type="range"] {
             width: 100%;
         }
         .param-control span {
            align-self: flex-end; /* Align value to the right */
         }

         #soy-display {
             height: 150px;
         }
     }

</style>
```