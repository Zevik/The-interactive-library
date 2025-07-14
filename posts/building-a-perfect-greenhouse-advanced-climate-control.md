---
title: "לבנות חממה מושלמת: בקרת אקלים מתקדמת"
english_slug: building-a-perfect-greenhouse-advanced-climate-control
category: "מדעי החקלאות / אגרוטכנולוגיה"
tags:
  - חממה
  - בקרת אקלים
  - חקלאות מדויקת
  - הנדסה חקלאית
  - אגרוטק
  - סימולציה
---
<h1>לבנות חממה מושלמת: בקרת אקלים מתקדמת</h1>

<p>דמיינו שיש לכם את היכולת לגדל את הגידולים הרגישים והרווחיים ביותר בעולם, בלי קשר למזג האוויר בחוץ. נשמע כמו קסם? זו המציאות בחממות מתקדמות, שמשתמשות במערכות בקרת אקלים חכמות. אבל מה באמת עומד מאחורי הקסם הזה? איך מנגנונים שונים פועלים יחד כדי לשמור על התנאים המושלמים? לפני שנקפוץ להסברים, בואו נתנסה בעצמנו! גררו רכיבים, התחילו את הסימולציה וראו אם תצליחו לייצב את האקלים בחממה שלכם.</p>

<div class="app-container">
    <div class="greenhouse-area" id="greenhouse">
        <h2>החממה הווירטואלית שלך</h2>
        <p class="drag-prompt">גרור ושחרר רכיבי בקרת אקלים לכאן כדי להוסיף אותם לחממה. לחץ על רכיב בחממה כדי להסירו.</p>
        <div id="greenhouse-components">
            <!-- Dropped components will appear here -->
        </div>
        <div class="climate-data-container">
            <div class="climate-display">
                <h3>אקלים פנימי נוכחי:</h3>
                <p class="climate-value-row">טמפרטורה: <span id="current-temp" class="climate-value">--</span> °C <span class="target-range">(יעד: <span id="target-temp">20-25</span>°C)</span></p>
                <p class="climate-value-row">לחות יחסית: <span id="current-humidity" class="climate-value">--</span> % <span class="target-range">(יעד: <span id="target-humidity">60-75</span>%)</span></p>
                <p class="climate-value-row">עוצמת אור: <span id="current-light" class="climate-value">--</span>% <span class="target-range">(יעד: <span id="target-light">70-90</span>%)</span></p>
                <p class="climate-status">מצב: <span id="climate-status">--</span></p>
            </div>
            <div class="external-weather-display">
                <h3>מזג אוויר חיצוני:</h3>
                <p class="climate-value-row">טמפרטורה: <span id="external-temp" class="climate-value">--</span> °C</p>
                <p class="climate-value-row">לחות יחסית: <span id="external-humidity" class="climate-value">--</span> %</p>
                <p class="climate-value-row">עוצמת אור: <span id="external-light" class="climate-value">--</span>%</p>
            </div>
        </div>
         <div class="sim-info">
             <p>זמן סימולציה: <span id="sim-time">00:00</span> | זמן יציב: <span id="stable-time">00:00</span></p>
         </div>
        <div class="controls">
             <button id="start-sim">התחל סימולציה</button>
             <button id="stop-sim" disabled>עצור סימולציה</button>
             <button id="reset-sim">אפס חממה</button>
        </div>
    </div>

    <div class="tool-palette">
        <h2>ארגז כלים</h2>
        <div class="tool-item" draggable="true" data-type="heater">
            <div class="tool-icon">🔥</div>
            <div class="tool-label">מחמם</div>
        </div>
        <div class="tool-item" draggable="true" data-type="cooler">
             <div class="tool-icon">❄️</div>
            <div class="tool-label">מקרר</div>
        </div>
        <div class="tool-item" draggable="true" data-type="fan">
             <div class="tool-icon">💨</div>
            <div class="tool-label">מאוורר (פנימי)</div>
        </div>
        <div class="tool-item" draggable="true" data-type="vent">
             <div class="tool-icon">🌬️</div>
            <div class="tool-label">פתח אוורור</div>
        </div>
        <div class="tool-item" draggable="true" data-type="humidifier">
             <div class="tool-icon">💧</div>
            <div class="tool-label">מכשיר אדים</div>
        </div>
        <div class="tool-item" draggable="true" data-type="dehumidifier">
             <div class="tool-icon"> sécheresse</div>
            <div class="tool-label">מסיר לחות</div>
        </div>
        <div class="tool-item" draggable="true" data-type="grow-light">
             <div class="tool-icon">💡</div>
            <div class="tool-label">גוף תאורה (צמיחה)</div>
        </div>
        <div class="tool-item" draggable="true" data-type="shade-screen">
             <div class="tool-icon">🕶️</div>
            <div class="tool-label">מסך הצללה</div>
        </div>
    </div>
</div>

<button id="toggle-explanation">רוצים להבין לעומק? לחצו כאן להסבר מקיף!</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: בקרת אקלים בחממות מתקדמות</h2>

    <p>ראיתם בסימולציה כמה גורמים משפיעים על האקלים בחממה, וכמה רכיבים שונים נדרשים כדי לאזן אותו. עכשיו בואו נצלול פנימה ונבין את העקרונות.</p>

    <h3>מדוע בקרת אקלים ממוחשבת היא ליבת החממה המודרנית?</h3>
    <p>גידולי פרימיום, זנים נדירים או כאלו הדורשים תנאים מדויקים (כמו קנאביס רפואי, סחלבים, או ירקות עלית מחוץ לעונה), אינם סובלים פשרות בתנאי הסביבה. טמפרטורה, לחות, אור וזרימת אוויר חייבים להיות בטווחים אופטימליים כדי להבטיח צמיחה מקסימלית, איכות בלתי מתפשרת ומניעת מחלות ומזיקים. בעוד חממה מספקת מחסה פיזי, מערכת בקרה חכמה היא המוח והשרירים שמוודאים שהתנאים הפנימיים תמיד יהיו אידיאליים, גם כשבחוץ משתוללת סערה או שורר גל חום.</p>

    <h3>חמשת עמודי התווך של אקלים החממה האידיאלי:</h3>
    <ul>
        <li><strong>טמפרטורה:</strong> המנוע של תהליכים פיזיולוגיים בצמח (פוטוסינתזה, נשימה, טרנסלוקציה של סוכרים). לכל צמח טווח טמפרטורות אופטימלי, וחריגה ממנו פוגעת קשות בצמיחה וביבול.</li>
        <li><strong>לחות יחסית (RH):</strong> שולטת בקצב הדיות (אידוי מים מהצמח דרך הפיוניות). הדיות חיוני לקליטת מים ומינרלים מהקרקע ולוויסות טמפרטורת הצמח. לחות נמוכה מדי = עקה (סטרס) יובש, סגירת פיוניות, האטת קליטת מינרלים. לחות גבוהה מדי = סיכון מוגבר למחלות פטרייתיות וחיידקיות, ירידה בדיות ופגיעה בקליטת מינרלים.</li>
        <li><strong>עוצמת ואיכות אור:</strong> האנרגיה לפוטוסינתזה. גם משך החשיפה לאור (פוטופריודיזם) קריטי לצמחים רבים למעבר משלב וגטטיבי לפריחה/הנבה. עוצמת אור חלשה מגבילה צמיחה; עוצמה חזקה מדי עלולה לגרום לנזק ("כוויות שמש").</li>
        <li><strong>זרימת אוויר ואוורור:</strong> זרימת אוויר *בתוך* החממה מבטיחה פיזור אחיד של טמפרטורה, לחות ו-CO2 סביב העלים, ומפחיתה סיכון למחלות. אוורור (החלפת אוויר *עם החוץ*) חיוני לוויסות טמפרטורה ולחות וחידוש מאגרי CO2.</li>
        <li><strong>ריכוז CO2:</strong> פחמן דו-חמצני הוא חומר הגלם העיקרי לפוטוסינתזה. בחממות סגורות, רמת CO2 יכולה לצנוח במהירות ולהפוך לגורם מגביל. העשרת CO2 (לרוב לא מיושמת בסימולציות בסיסיות) מגבירה דרמטית את קצב הפוטוסינתזה והצמיחה.</li>
    </ul>

    <h3>מבט מקרוב על רכיבי הבקרה שפגשתם בסימולציה:</h3>
    <ul>
        <li><strong>מחמם (Heater):</strong> מספק חום אקטיבי. נחוץ במיוחד בחורף, בלילה, או באזורים קרים. יעילותו פוחתת כשפתחי האוורור פתוחים.</li>
        <li><strong>מקרר (Cooler) / פאדים וונטות:</strong> מוריד טמפרטורה. לרוב נעשה באמצעות אידוי (Evaporative Cooling), בו מאווררים שואבים אוויר דרך פאדים רטובים. יעיל במיוחד באקלים יבש.</li>
        <li><strong>מאוורר פנימי (Fan):</strong> יוצר תנועת אוויר רציפה בתוך החממה. מונע הצטברות אוויר לח סביב העלים, מסייע בחידוש CO2 מקומי, ומשפר את אחידות האקלים הפנימי. הוא אינו מחליף אוויר עם החוץ.</li>
        <li><strong>פתח אוורור (Vent):</strong> פתחים (לרוב בגג או בצדדים) הנפתחים אוטומטית. מאפשרים החלפה פסיבית או אקטיבית (עם עזרת מאווררים) של האוויר הפנימי באוויר חיצוני. הדרך העיקרית לוויסות טמפרטורה ולחות ברוב החממות. פתיחתם מפחיתה את יעילות החימום/קירור/הלחה/היבוש הפנימיים.</li>
        <li><strong>מכשיר אדים (Humidifier):</strong> מוסיף לחות לאוויר הפנימי, נחוץ באקלים יבש או כשהחימום מייבש את האוויר. יעילותו פוחתת כשפתחי האוורור פתוחים.</li>
        <li><strong>מסיר לחות (Dehumidifier):</strong> מוציא לחות מהאוויר הפנימי. קריטי בחממות סגורות (למשל, כדי לחסוך אנרגיה על חימום בחורף) בהן לא ניתן לפתוח ונטות לאוורור טבעי. יעילותו פוחתת כשפתחי האוורור פתוחים.</li>
        <li><strong>גוף תאורה (Grow Light):</strong> משלים או מחליף אור שמש טבעי כשהעוצמה בחוץ נמוכה מדי (חורף, ימים מעוננים, גידולים הדורשים שעות אור רבות). התאורה משפיעה בעיקר על האור הפנימי, פחות על טמפרטורה/לחות בסימולציה זו.</li>
        <li><strong>מסך הצללה (Shade Screen):</strong> מפחית את עוצמת אור השמש הנכנס. עוזר גם להפחית את החום הנכנס מהשמש. ישנם מסכים המשמשים גם כמסכים טרמיים לשמירת חום בלילה. בסימולציה זו הוא מפחית את עוצמת האור הפנימי ביחס לאור החיצוני.</li>
    </ul>

    <h3>איך מערכת הבקרה מתפקדת כל הזמן? זו לולאה סגורה!</h3>
    <ol>
        <li><strong>איסוף נתונים:</strong> חיישנים מתקדמים (טמפרטורה, לחות, קרינה, CO2, מהירות רוח, כיוון רוח, גשם ועוד) מפוזרים בחממה ומחוצה לה ומספקים נתונים בזמן אמת.</li>
        <li><strong>ניתוח והחלטה:</strong> בקר ממוחשב (ה"מוח") מקבל את נתוני החיישנים, משווה אותם ליעדים (Set Points) שהוגדרו מראש ע"י המגדל לכל פרמטר, ומפעיל אלגוריתמים מורכמים (לעיתים מבוססי AI) כדי לחשב את הפעולה האופטימלית.</li>
        <li><strong>ביצוע:</strong> הבקר שולח פקודות למבצעים (Actuators) - מנועים הפותחים וסוגרים ונטות, מפעילים מחממים/מקררים/מאווררים/תאורה/מערכות השקיה/הדברה וכו'.</li>
        <li><strong>חזרה לשלב 1:</strong> החיישנים מודדים שוב את התנאים המתוקנים, והלולאה נמשכת באופן רציף 24/7.</li>
    </ol>

    <h3>אתגרים ופתרונות בעולם האמיתי:</h3>
    האתגר המרכזי הוא לשמור על יציבות מקסימלית באקלים הפנימי למרות שינויים חיצוניים מהירים וקיצוניים, תוך כדי מזעור צריכת האנרגיה העצומה של מערכות הבקרה. תכנון חממה אקלים-אקטיבית (שליטה מלאה, סגורה יחסית) לעומת חממה אקלים-פסיבית (שימוש בעיקר באוורור טבעי) תלוי בגידול, באקלים החיצוני ובתקציב. מערכות בקרה חכמות מייעלות את השימוש ברכיבים השונים, למשל, העדפת אוורור טבעי על פני קירור/חימום מכאני ככל הניתן.

    <p>הסימולציה בה התנסיתם היא מודל פשוט של המציאות המורכבת הזו. היא נועדה להמחיש את העקרונות הבסיסיים של איזון כוחות שונים (טבעיים ואקטיביים) כדי להגיע לתנאי הסביבה הרצויים לגידולים שלכם.</p>
</div>

<script>
    const greenhouse = document.getElementById('greenhouse-components');
    const toolPalette = document.querySelector('.tool-palette');
    const tools = toolPalette.querySelectorAll('.tool-item');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const startSimButton = document.getElementById('start-sim');
    const stopSimButton = document.getElementById('stop-sim');
    const resetButton = document.getElementById('reset-sim');

    // Climate display elements
    const currentTempSpan = document.getElementById('current-temp');
    const currentHumiditySpan = document.getElementById('current-humidity');
    const currentLightSpan = document.getElementById('current-light');
    const climateStatusSpan = document.getElementById('climate-status');
    const externalTempSpan = document.getElementById('external-temp');
    const externalHumiditySpan = document.getElementById('external-humidity');
    const externalLightSpan = document.getElementById('external-light');
    const simTimeSpan = document.getElementById('sim-time');
    const stableTimeSpan = document.getElementById('stable-time');

    // Target climate (example for a specific crop)
    const targetTempRange = [20, 25];
    const targetHumidityRange = [60, 75];
    const targetLightRange = [70, 90]; // As percentage of potential max light (relative to a max 100% external)

    // Initial state & Variables
    let internalTemp = 22;
    let internalHumidity = 65;
    let internalLight = 80; // Start within range
    let externalTemp = 15;
    let externalHumidity = 50;
    let externalLight = 60; // Example starting external light
    let simulationInterval = null;
    let simTime = 0; // in seconds
    let stableTime = 0; // in seconds

    // Component effects (simplified per tick, interaction with external/vents added in logic)
    const componentEffects = {
        heater: { temp: +0.3, cost: 1 }, // Adds temp per tick
        cooler: { temp: -0.3, cost: 1 }, // Removes temp per tick
        fan: { air_flow: +1, cost: 0.1 }, // Adds air flow factor
        vent: { air_exchange_factor: +1, cost: 0 }, // Adds air exchange factor
        humidifier: { humidity: +0.5, cost: 0.5 }, // Adds humidity
        dehumidifier: { humidity: -0.5, cost: 0.5 }, // Removes humidity
        'grow-light': { light: +5, cost: 0.8 }, // Adds light % directly
        'shade-screen': { shade_factor: -0.05, cost: 0 } // Reduces incoming light percentage
    };

    let activeComponents = []; // Array to hold types of dropped components


    // --- Drag and Drop functionality ---
    tools.forEach(tool => {
        tool.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', e.target.dataset.type);
            e.dataTransfer.effectAllowed = 'copy';
            e.target.classList.add('dragging');
        });
         tool.addEventListener('dragend', (e) => {
            e.target.classList.remove('dragging');
        });
    });

    greenhouse.addEventListener('dragover', (e) => {
        e.preventDefault(); // Necessary to allow dropping
        e.dataTransfer.dropEffect = 'copy';
        greenhouse.classList.add('drag-over');
    });

     greenhouse.addEventListener('dragleave', (e) => {
        greenhouse.classList.remove('drag-over');
    });


    greenhouse.addEventListener('drop', (e) => {
        e.preventDefault();
        greenhouse.classList.remove('drag-over');
        const dataType = e.dataTransfer.getData('text/plain');

        // Limit placing the same type multiple times? (Optional, depending on simulation complexity)
        // For now, allow multiple for simplicity in this model.

        const component = document.createElement('div');
        component.classList.add('placed-component');
        component.dataset.type = dataType;

        // Get icon and label from tool palette
        const toolTemplate = toolPalette.querySelector(`.tool-item[data-type="${dataType}"]`);
        if (toolTemplate) {
            component.innerHTML = toolTemplate.innerHTML; // Copy icon and label structure
        } else {
             component.textContent = dataType.replace('-', ' '); // Fallback
        }


        // Simple placement - just add to the list, ignore exact position
        greenhouse.querySelector('#greenhouse-components').appendChild(component);

        // Add to active components for simulation
        activeComponents.push(dataType);

        // Add click listener for removal
        component.addEventListener('click', removeComponent);

        console.log('Component dropped:', dataType);
        console.log('Active components:', activeComponents);

        // Ensure simulation can start if components are added
        if (!simulationInterval) {
             startSimButton.disabled = false;
        }
    });

    function removeComponent(event) {
        const componentElement = event.target.closest('.placed-component');
        if (!componentElement) return;

        const dataType = componentElement.dataset.type;

        // Remove from active components array
        const index = activeComponents.indexOf(dataType);
        if (index > -1) {
            activeComponents.splice(index, 1);
        }

        // Remove from DOM
        componentElement.remove();

        console.log('Component removed:', dataType);
        console.log('Active components:', activeComponents);
    }


    // --- Simulation Logic ---
    function updateClimate() {
        simTime++; // Increment simulation time

        // Simulate external weather changes (more dynamic)
        externalTemp += (Math.random() - 0.5) * 0.8; // Fluctuates by +/- 0.4
        externalHumidity += (Math.random() - 0.5) * 1.5; // Fluctuates by +/- 0.75
        externalLight += (Math.random() - 0.5) * 3; // Fluctuates by +/- 1.5

        // Add a slight diurnal trend (simplistic sine wave based on time)
        const hour = (simTime / 60) % 24; // Simulate hours passing (1 sim sec = 1 real min?)
        externalTemp += Math.sin(hour / 12 * Math.PI) * 0.1;
        externalLight = Math.max(0, externalLight + Math.sin((hour + 6) / 12 * Math.PI) * 0.5); // Light peaks around 'noon' (hour 6-18 sim)

        externalTemp = Math.max(-10, Math.min(40, externalTemp));
        externalHumidity = Math.max(10, Math.min(100, externalHumidity));
        externalLight = Math.max(0, Math.min(100, externalLight)); // External light max 100%

        // Natural tendency towards external climate (passive transfer)
        let tempChangeNatural = (externalTemp - internalTemp) * 0.05; // Slower passive heat exchange
        let humidityChangeNatural = (externalHumidity - internalHumidity) * 0.03; // Slower passive moisture exchange
        // Natural light influence is direct before component effects

        // Calculate combined component effects and factors
        let totalComponentTempEffect = 0;
        let totalComponentHumidityEffect = 0;
        let totalAddedLight = 0;
        let airExchangeFactor = 1; // Base factor
        let shadeFactor = 0; // Sum of shade factors

        activeComponents.forEach(type => {
            const effects = componentEffects[type];
            if (effects) {
                totalComponentTempEffect += effects.temp || 0;
                totalComponentHumidityEffect += effects.humidity || 0;
                totalAddedLight += effects.light || 0;
                airExchangeFactor += effects.air_exchange_factor || 0; // Vents increase exchange
                 airExchangeFactor += (effects.air_flow || 0) * 0.5; // Fans also increase exchange rate implicitly
                shadeFactor += effects.shade_factor || 0;
            }
        });

        // Vents increase exchange rate, making internal climate follow external faster
        // This means passive transfer is amplified by airExchangeFactor
        let tempChange = tempChangeNatural * airExchangeFactor;
        let humidityChange = humidityChangeNatural * airExchangeFactor;

        // Vents also reduce the effectiveness of internal components (heater, cooler, humi, de-humi)
        const ventPenalty = airExchangeFactor > 1 ? (airExchangeFactor - 1) * 0.4 : 0; // Penalty increases with more venting/airflow
        totalComponentTempEffect *= (1 - ventPenalty);
        totalComponentHumidityEffect *= (1 - ventPenalty);

        // Apply active component effects
        internalTemp += totalComponentTempEffect + tempChange;
        internalHumidity += totalComponentHumidityEffect + humidityChange;

        // Light: influenced by external, grow lights, and shade
        let incomingLight = externalLight;
         // Apply shade screen effect to incoming external light
        incomingLight = Math.max(0, incomingLight * (1 + shadeFactor)); // shadeFactor is negative, so 1 + shadeFactor < 1

        internalLight = (internalLight * 0.9) + (incomingLight * 0.1); // Blend with external/incoming light
        internalLight += totalAddedLight; // Add light from grow lamps

        // Clamp values within reasonable bounds
        internalTemp = Math.max(-5, Math.min(45, internalTemp));
        internalHumidity = Math.max(10, Math.min(99, internalHumidity));
        internalLight = Math.max(0, Math.min(200, internalLight)); // Can exceed 100% with grow lights

        // Check if climate is stable
        const isStable = internalTemp >= targetTempRange[0] && internalTemp <= targetTempRange[1] &&
                         internalHumidity >= targetHumidityRange[0] && internalHumidity <= targetHumidityRange[1] &&
                         internalLight >= targetLightRange[0] && internalLight <= targetLightRange[1];

        if (isStable) {
            stableTime++;
        }

        updateDisplay(isStable);
    }

    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        const paddedMinutes = String(minutes).padStart(2, '0');
        const paddedSeconds = String(remainingSeconds).padStart(2, '0');
        return `${paddedMinutes}:${paddedSeconds}`;
    }

    function updateDisplay(isStable = false) {
        currentTempSpan.textContent = internalTemp.toFixed(1);
        currentHumiditySpan.textContent = internalHumidity.toFixed(1);
        currentLightSpan.textContent = internalLight.toFixed(1);

         // Add visual feedback (color) to climate values
         updateValueColor(currentTempSpan, internalTemp, targetTempRange);
         updateValueColor(currentHumiditySpan, internalHumidity, targetHumidityRange);
         updateValueColor(currentLightSpan, internalLight, targetLightRange);


        externalTempSpan.textContent = externalTemp.toFixed(1);
        externalHumiditySpan.textContent = externalHumidity.toFixed(1);
        externalLightSpan.textContent = externalLight.toFixed(1);

        simTimeSpan.textContent = formatTime(simTime);
        stableTimeSpan.textContent = formatTime(stableTime);


        // Determine climate status message
        let status = "";
        let isOffTarget = false;

        if (internalTemp < targetTempRange[0]) { status += " קר מדי;"; isOffTarget = true; }
        else if (internalTemp > targetTempRange[1]) { status += " חם מדי;"; isOffTarget = true; }

        if (internalHumidity < targetHumidityRange[0]) { status += " יבש מדי;"; isOffTarget = true; }
        else if (internalHumidity > targetHumidityRange[1]) { status += " לח מדי;"; isOffTarget = true; }

        if (internalLight < targetLightRange[0]) { status += " אור חלש מדי;"; isOffTarget = true; }
        else if (internalLight > targetLightRange[1]) { status += " אור חזק מדי;"; isOffTarget = true; }

        if (!isOffTarget) {
            status = " האקלים יציב ויעיל! "; // More positive message
        } else {
             // Remove trailing semicolon if present
             status = status.slice(0, -1);
             if (status === "") status = "נא הוסף רכיבים..."; // Case before sim starts
        }


        climateStatusSpan.textContent = status;
        climateStatusSpan.className = 'climate-status'; // Reset class
        if (!isOffTarget && simTime > 0) {
             climateStatusSpan.classList.add('status-stable');
        } else if (isOffTarget) {
             climateStatusSpan.classList.add('status-off-target');
        } else {
             climateStatusSpan.classList.add('status-initial');
        }

        // Add visual feedback to placed components (simple pulse if simulation is running)
         if (simulationInterval) {
              greenhouse.querySelectorAll('.placed-component').forEach(comp => {
                   comp.classList.add('simulating');
              });
         } else {
              greenhouse.querySelectorAll('.placed-component').forEach(comp => {
                   comp.classList.remove('simulating');
              });
         }
    }

     function updateValueColor(element, value, range) {
          element.classList.remove('value-low', 'value-ok', 'value-high');
          if (value < range[0]) {
              element.classList.add('value-low');
          } else if (value > range[1]) {
              element.classList.add('value-high');
          } else {
               element.classList.add('value-ok');
          }
     }


    function startSimulation() {
        if (!simulationInterval) {
             if (activeComponents.length === 0) {
                 alert("הוסף רכיבים לחממה מסדנת הכלים לפני התחלת הסימולציה!");
                 return;
             }
            simulationInterval = setInterval(updateClimate, 100); // Run simulation tick every 100ms (10 ticks per second)
            startSimButton.disabled = true;
            stopSimButton.disabled = false;
             resetButton.disabled = true; // Disable reset during sim
             greenhouse.classList.add('sim-active'); // Add visual indicator to greenhouse area
        }
    }

    function stopSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;
            startSimButton.disabled = false;
            stopSimButton.disabled = true;
            resetButton.disabled = false; // Enable reset after stopping
             greenhouse.classList.remove('sim-active'); // Remove visual indicator
             updateDisplay(false); // Update display state without advancing time/stability
        }
    }

     function resetSimulation() {
        stopSimulation();
        internalTemp = 22;
        internalHumidity = 65;
        internalLight = 80;
        externalTemp = 15;
        externalHumidity = 50;
        externalLight = 60;
        simTime = 0;
        stableTime = 0;
        activeComponents = [];
        const placedComponents = greenhouse.querySelectorAll('#greenhouse-components .placed-component');
         placedComponents.forEach(comp => comp.removeEventListener('click', removeComponent)); // Clean up listeners
        greenhouse.querySelector('#greenhouse-components').innerHTML = ''; // Clear placed components
        updateDisplay(); // Update display to reset values
        climateStatusSpan.style.color = ""; // Reset status color
        startSimButton.disabled = false; // Re-enable start button
     }


    // --- Event Listeners ---
    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'רוצים להבין לעומק? לחצו כאן להסבר מקיף!';
         // Scroll to explanation if shown
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

    startSimButton.addEventListener('click', startSimulation);
    stopSimButton.addEventListener('click', stopSimulation);
    resetButton.addEventListener('click', resetSimulation);


    // Initial display update
    updateDisplay();

</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap'); /* Optional: Use a modern Hebrew-friendly font */

    body {
        font-family: 'Heebo', 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        direction: rtl;
        text-align: right;
        background-color: #f8f8f8; /* Light grey background */
        color: #333;
    }

    h1, h2, h3 {
        color: #2c3e50; /* Dark blue-grey */
        text-align: center; /* Center headings for better visual balance */
        margin-bottom: 15px;
    }

    h1 {
        color: #1a5276;
        margin-bottom: 25px;
    }

    p {
         text-align: right;
         margin-bottom: 10px;
    }

    .app-container {
        display: flex;
        flex-direction: row;
        gap: 30px; /* Increased gap */
        margin-top: 20px;
        flex-wrap: wrap-reverse; /* Palette on the left on small screens */
        background-color: #ecf0f1; /* Very light blue-grey */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .greenhouse-area {
        flex: 3; /* Take up more space */
        border: 2px dashed #aed6f1; /* Lighter blue dashed border */
        padding: 20px; /* Increased padding */
        min-height: 500px; /* Increased min height */
        position: relative;
        background: linear-gradient(to bottom, #e0ffe0, #c8e6c9); /* Gentle green gradient */
        border-radius: 8px;
        overflow: hidden; /* Clip potential overflow from components */
    }

     .greenhouse-area.drag-over {
          background-color: #d4edda; /* Highlight when dragging over */
     }

     .greenhouse-area.sim-active {
         border-color: #4CAF50; /* Green border when simulation is active */
         box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
     }

     .greenhouse-area h2 {
         margin-top: 0;
         color: #28a745; /* Green color for greenhouse title */
         text-align: center;
     }

     .drag-prompt {
         text-align: center;
         color: #555;
         font-style: italic;
         margin-bottom: 20px;
     }


    #greenhouse-components {
         min-height: 180px; /* Give more space for components */
         border: 1px solid #c8e6c9; /* Lighter border */
         padding: 15px; /* Increased padding */
         margin-bottom: 20px;
         background-color: rgba(255, 255, 255, 0.6); /* More transparent background */
         border-radius: 6px;
         display: flex;
         flex-wrap: wrap;
         gap: 10px; /* Increased gap between components */
         align-items: flex-start; /* Align items to the top */
         align-content: flex-start; /* Distribute lines to the top */
    }

    .placed-component {
        background-color: #5cb85c; /* Bootstrap-like success green */
        color: white;
        padding: 8px 12px; /* Increased padding */
        border-radius: 20px; /* Pill shape */
        margin: 3px; /* Margin around pills */
        font-size: 0.9em;
        cursor: pointer; /* Indicate clickable for removal */
        text-align: center;
        display: flex; /* Align icon and label */
        align-items: center;
        gap: 5px;
        transition: background-color 0.2s ease, transform 0.2s ease;
         box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

     .placed-component .tool-icon {
         font-size: 1.2em;
     }
     .placed-component .tool-label {
          white-space: nowrap; /* Prevent label wrapping */
     }


    .placed-component:hover {
        background-color: #d9534f; /* Indicate it can be removed (red on hover) */
        transform: scale(1.05); /* Slightly enlarge on hover */
    }

     .placed-component.simulating {
         animation: pulse 1.5s infinite ease-in-out; /* Add pulse animation when simulating */
     }

     @keyframes pulse {
         0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7); }
         70% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
         100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
     }


    .climate-data-container {
        display: flex;
        gap: 20px;
        margin-bottom: 15px;
         flex-wrap: wrap; /* Wrap on smaller screens */
    }

    .climate-display, .external-weather-display {
        flex: 1; /* Take equal space */
        border: 1px solid #bdc3c7; /* Light grey border */
        padding: 15px; /* Increased padding */
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

     .climate-display h3, .external-weather-display h3 {
         margin-top: 0;
         font-size: 1.1em;
         color: #34495e; /* Darker blue-grey */
         border-bottom: 1px solid #eee;
         padding-bottom: 5px;
         margin-bottom: 10px;
         text-align: right; /* Align display titles to the right */
     }

     .climate-value-row {
         margin-bottom: 8px; /* Space out value rows */
         display: flex; /* Use flex to align value and target */
         justify-content: space-between; /* Push target to the left */
         align-items: center;
     }

     .climate-value {
         font-weight: bold;
         font-size: 1.2em;
         transition: color 0.3s ease; /* Smooth color transition */
     }

     .target-range {
         font-size: 0.9em;
         color: #555;
     }

     /* Climate value color feedback */
     .value-low { color: #e74c3c; } /* Red */
     .value-ok { color: #28a745; } /* Green */
     .value-high { color: #f39c12; } /* Orange */

    .climate-status {
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px solid #eee;
        font-weight: bold;
        text-align: center; /* Center status text */
        min-height: 1.2em; /* Reserve space */
    }

     .status-initial { color: #888; }
     .status-stable { color: #28a745; animation: pulse-green 1.5s infinite ease-in-out; }
     .status-off-target { color: #e74c3c; }

     @keyframes pulse-green {
         0% { color: #28a745; }
         50% { color: #4ade80; }
         100% { color: #28a745; }
     }

     .sim-info {
         text-align: center;
         margin-bottom: 15px;
         font-size: 1em;
         color: #555;
     }

     .sim-info span {
         font-weight: bold;
         color: #333;
     }


    .controls {
        margin-top: 20px; /* Increased margin */
        text-align: center;
    }

    .controls button {
        margin: 0 8px; /* Increased margin */
        padding: 10px 20px; /* Increased padding */
        cursor: pointer;
        border: none;
        border-radius: 5px; /* Slightly more rounded */
        font-size: 1em;
        transition: background-color 0.2s ease, opacity 0.2s ease;
         font-weight: bold;
    }

    #start-sim { background-color: #28a745; color: white; } /* Green */
    #start-sim:hover:not(:disabled) { background-color: #218838; }
    #start-sim:disabled { background-color: #a5d6a7; cursor: not-allowed; opacity: 0.7; }

    #stop-sim { background-color: #dc3545; color: white; } /* Red */
    #stop-sim:hover:not(:disabled) { background-color: #c82333; }
     #stop-sim:disabled { background-color: #ef9a9a; cursor: not-allowed; opacity: 0.7; }

    #reset-sim { background-color: #007bff; color: white; } /* Blue */
    #reset-sim:hover:not(:disabled) { background-color: #0056b3; }
     #reset-sim:disabled { background-color: #90CAF9; cursor: not-allowed; opacity: 0.7; }


    .tool-palette {
        flex: 1;
        border: 1px solid #bdc3c7;
        padding: 20px; /* Increased padding */
        min-width: 200px; /* Increased minimum width */
        background-color: #ecf0f1; /* Same as container background */
        border-radius: 8px;
         align-self: flex-start; /* Align palette to the top */
    }

    .tool-palette h2 {
        margin-top: 0;
        color: #34495e;
        text-align: center;
        margin-bottom: 20px;
    }

    .tool-item {
        border: 1px solid #dcdcdc; /* Lighter border */
        padding: 12px; /* Increased padding */
        margin-bottom: 12px; /* Increased margin */
        background-color: #ffffff; /* White background */
        cursor: grab;
        text-align: center;
        border-radius: 6px; /* Slightly more rounded */
        box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        display: flex; /* Align icon and label */
        align-items: center;
        justify-content: center; /* Center content */
        gap: 10px;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

     .tool-item .tool-icon {
         font-size: 1.5em; /* Larger icons */
     }
     .tool-item .tool-label {
         font-weight: bold;
         color: #333;
     }


    .tool-item:hover:not(.dragging) {
        background-color: #f0f0f0;
        transform: translateY(-2px); /* Slight lift on hover */
    }

     .tool-item.dragging {
         opacity: 0.5; /* Reduce opacity while dragging */
         transform: scale(0.95); /* Slightly shrink while dragging */
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* Center the button and add space */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none; /* Remove border */
        border-radius: 5px;
        background-color: #bdc3c7; /* Light grey-blue */
        color: #34495e; /* Dark text */
        transition: background-color 0.2s ease;
         font-weight: bold;
    }

     #toggle-explanation:hover {
         background-color: #95a5a6; /* Darker grey-blue on hover */
     }


    #explanation {
        margin-top: 20px;
        padding: 20px; /* Increased padding */
        border: 1px solid #bdc3c7;
        background-color: #ecf0f1; /* Same as container */
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }

    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 8px;
        color: #34495e;
        border-bottom: 1px dashed #bdc3c7;
        padding-bottom: 5px;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Indent list */
    }

    #explanation li {
        margin-bottom: 8px; /* More space between list items */
        line-height: 1.8; /* Improved readability */
    }

     @media (max-width: 768px) {
         .app-container {
             flex-direction: column; /* Stack vertically on small screens */
             gap: 20px;
             padding: 15px;
         }
         .greenhouse-area, .tool-palette {
             flex: none;
             width: 100%;
             min-width: auto;
             min-height: 300px; /* Adjust minimum height for smaller screens */
         }
         .tool-palette {
              order: 1; /* Place palette first on small screens */
         }
         .greenhouse-area {
              order: 2; /* Place greenhouse second */
              padding: 15px;
         }
         .climate-data-container {
              flex-direction: column;
              gap: 15px;
         }
         .controls button {
             margin-bottom: 10px; /* Add space below buttons */
         }
         #toggle-explanation {
              font-size: 1em;
              padding: 10px 20px;
         }
     }

</style>
```