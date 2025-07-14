---
title: "איך נוצר בולען? סימולציה של מערות מלח"
english_slug: how-a-sinkhole-forms-salt-cave-simulation
category: "מדעי הסביבה / כדור הארץ"
tags:
  - בולענים
  - מערות מלח
  - תהליכי התמוטטות
  - גיאולוגיה
  - הידרולוגיה
---
# גלו את הסוד מתחת לרגליים: איך בולען נפער פתאום?

הם מופיעים ללא אזהרה, בולעים כבישים, מבנים ולעיתים קרובות מעוררים תדהמה. בולענים – הפתחים המסתוריים באדמה – לרוב מתחילים את דרכם בתהליך שקט וסבלני עמוק עמוק מתחת לפני השטח. הצטרפו למסע ויזואלי אל תוך האדמה כדי לראות איך אינטראקציה פשוטה בין מים למלח יכולה ליצור תופעה דרמטית כל כך.

<div id="simulation-container">
    <div class="layer" id="surface-layer">
        <span class="layer-label">פני השטח</span>
        <div id="sinkhole" class="hidden"></div>
    </div>
    <div class="layer" id="soil-layer">
        <span class="layer-label">שכבת קרקע לא מלוכדת</span>
         <div id="water-flow" class="hidden"></div>
    </div>
    <div class="layer" id="salt-layer">
        <span class="layer-label">שכבת מלח (הליט)</span>
        <div id="cave" class="hidden"></div>
    </div>
    <div class="layer" id="base-layer">
        <span class="layer-label">תשתית אטומה</span>
    </div>
    <div id="status-message">לחצו "התחילו להוסיף מים" כדי לצאת למסע התת-קרקעי</div>
</div>

<div id="controls">
    <button id="add-water-btn">התחילו להוסיף מים</button>
    <button id="trigger-collapse-btn" disabled>זרזו את ההתמוטטות</button>
    <button id="reset-btn">התחילו מחדש</button>
</div>

<button id="toggle-explanation-btn" class="explanation-button">רוצים להבין יותר? קראו את ההסבר המדעי</button>

<div id="explanation-section" style="display: none;">
    <h2>הסבר מעמיק: מאחורי הקלעים של היווצרות בולען מעל מערת מלח</h2>
    <p>בולענים, או דולינות, הם שקעים טופוגרפיים הנוצרים לרוב באזורים בעלי סלע מסיס קרוב לפני השטח. כשהסלע (כמו אבן גיר, גבס, או במקרה שלנו - מלח) נמס על ידי מים תת-קרקעיים, נוצרים חללים שעלולים להתמוטט. בולענים מעל שכבות מלח הם מאפיין בולט, למשל, באזור ים המלח.</p>

    <h3>בולעני התמוטטות: הפתעה גיאולוגית</h3>
    <p>הסימולציה שלפניכם מדגימה היווצרות של <b>בולען התמוטטות (Cover-collapse sinkhole)</b>. זהו הסוג המסוכן ביותר בשל הפתאומיות שלו. הוא נוצר כאשר מעל שכבת הסלע המומסת נמצאת שכבה עבה יחסית של קרקע לא מלוכדת (חול, חרסית, טין). המסה תת-קרקעית של הסלע יוצרת חלל הולך וגדל, מעין 'מערה', מתחת לשכבת הקרקע הזו. במשך הזמן, ככל שהמערה גדלה והתקרה הטבעית שלה (הקרקע שמעליה) הופכת דקה וחלשה יותר, היא מאבדת את יכולתה לתמוך במשקל העצמי שלה ובמשקל המצטבר מעליה. בסופו של דבר, התקרה קורסת בפתאומיות לתוך החלל, גוררת איתה את הקרקע העליונה ויוצרת את הבולען הגלוי לעין.</p>

    <h3>הגורמים להמסת מלח תת-קרקעי</h3>
    <p>שכבות מלח עבות (הליט) נוצרות כתוצאה מהתאדות של ימות או אגמים מלוחים קדומים. שכבות אלו יכולות להיקבר תחת משקעים אחרים לאורך מיליוני שנים. מלח הוא מסיס מאוד במים. כאשר מים (מי גשמים מחלחלים, מי תהום) מגיעים במגע עם שכבת המלח, הם מתחילים להמיס אותה בהדרגה, תהליך המכונה המסה (Dissolution). קצב ההמסה תלוי בגורמים כמו כמות המים הזמינה, קצב זרימת המים, טמפרטורת המים, וריכוז המלח שכבר קיים במים.</p>

    <h3>טריגרים חיצוניים: מה יכול להקפיץ את התהליך?</h3>
    <p>בעוד שהמסת המלח היא תהליך איטי וארוך טווח, הקריסה הסופית של שכבת הקרקע מעל החלל התת-קרקעי יכולה להיגרם או לואץ על ידי גורמים חיצוניים המכונים 'טריגרים'. אלו יכולים להיות:
        <ul>
            <li><b>שינויים במפלס מי התהום:</b> עלייה פתאומית יכולה להציף חללים ולהגדיל את הלחץ על התקרה; ירידה במפלס (למשל עקב שאיבה) יכולה להסיר תמיכה הידרוסטטית שהייתה קיימת.</li>
            <li><b>גשמים עזים:</b> מגדילים את כמות המים המחלחלים ומאיצים את ההמסה, וכן מוסיפים משקל לשכבות העליונות.</li>
            <li><b>עומסים חדשים על פני השטח:</b> בנייה, תנועת כלי רכב כבדים, או אפילו שלולית מים גדולה, יכולים להוסיף עומס על התקרה המוחלשת ולגרום לקריסתה.</li>
            <li><b>שינויים בטמפרטורה:</b> יכולים להשפיע על מסיסות המלח או על תנועת המים.</li>
        </ul>
    </p>

    <h3>בולענים בים המלח: מקרה מבחן כואב</h3>
    <p>אזור חופי ים המלח מהווה דוגמה דרמטית ועדכנית לתופעת בולענים מעל שכבות מלח. ירידת מפלס ים המלח, המואצת על ידי פעילות אנושית ואקלים, גורמת לירידה מקבילה במפלס מי התהום. בעבר, מי התהום היו גבוהים יותר ותמכו בחלק משכבות המלח. כעת, כאשר המפלס יורד, מים מתוקים יחסית (שאינם רוויים במלח) יכולים להגיע לשכבות המלח, להמיס אותן בקצב מהיר יחסית וליצור חללים. כשהחללים הללו מגיעים לגודל קריטי מתחת לשכבת הקרקע הלא יציבה, הם קורסים ויוצרים את אלפי הבולענים הנפערים כיום לאורך החופים, מסכנים תשתיות ומונעים גישה לאזורים שהיו פופולריים בעבר.</p>
</div>

<style>
    /* --- General Styling --- */
    body {
        font-family: 'Arial', sans-serif; /* Use a common, clean font */
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #0056b3; /* Theme color */
        text-align: center;
        margin-bottom: 20px;
    }

    p {
        margin-bottom: 15px;
        text-align: justify;
    }

    button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 12px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
    }

    button:hover {
        background-color: #0056b3;
    }

    button:active {
        transform: scale(0.98);
    }

    button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        opacity: 0.7;
        transform: none;
    }

    .explanation-button {
        display: block;
        margin: 30px auto 10px auto; /* More space around the button */
        background-color: #6c757d;
    }

    .explanation-button:hover {
        background-color: #5a6268;
    }


    /* --- Simulation Container --- */
    #simulation-container {
        width: 95%; /* Use more width */
        max-width: 500px; /* Slightly smaller max-width */
        height: 450px; /* Taller simulation area */
        margin: 30px auto; /* More vertical margin */
        border: 2px solid #8d6e63; /* Earthy border */
        border-radius: 8px; /* Rounded corners */
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, #e0f7fa 0%, #b3e5fc 20%, #e0f2f7 100%); /* Gradient sky/air */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        display: flex;
        flex-direction: column;
        align-items: center; /* Center layers horizontally */
        justify-content: flex-end; /* Stack layers from bottom */
    }

    .layer {
        width: 100%;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9em;
        color: #333;
        position: relative; /* For absolute positioning of children/labels */
        z-index: 1; /* Default z-index */
        border-bottom: 1px dashed rgba(0,0,0,0.2); /* Subtle layer separation */
        text-shadow: 0 0 3px rgba(255,255,255,0.5); /* Make labels readable */
    }

    .layer-label {
         background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent background for text */
         padding: 3px 8px;
         border-radius: 4px;
         font-weight: bold;
    }

    #surface-layer {
        background-color: #8b4513; /* Soil/Brown color */
        height: 15%; /* Allocate more space for surface */
        color: white;
        z-index: 4; /* Highest layer */
         border-bottom: none; /* No border on top layer */
    }

    #soil-layer {
        background-color: #a0522d; /* Darker soil */
        height: 30%; /* Thicker soil layer */
        z-index: 3;
        transition: transform 0.6s ease-out, opacity 0.6s ease-out; /* Animation for collapse */
         overflow: hidden; /* Hide water flow initially */
    }

     #water-flow {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 5px; /* Width of water flow */
        height: 100%; /* Flow through the soil layer */
        background: linear-gradient(to bottom, rgba(0,100,255,0.8) 0%, rgba(0,100,255,0) 100%);
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
        z-index: 1; /* Below the layer label */
        animation: flow-down 1.5s infinite linear; /* Animation for water flow */
     }

     @keyframes flow-down {
         0% { transform: translate(-50%, 0); opacity: 0.8; }
         50% { opacity: 1; }
         100% { transform: translate(-50%, 100%); opacity: 0.8; }
     }


    #salt-layer {
        background-color: #eeeeee; /* Light grey for salt */
        height: 35%; /* Salt layer size */
        z-index: 2;
         background-image: linear-gradient(45deg, rgba(255,255,255,0.2) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.2) 75%, transparent 75%, transparent);
         background-size: 20px 20px; /* Add a subtle crystal texture */
    }

    #base-layer {
        background-color: #607d8b; /* Blue-grey for base */
        height: 20%;
        border-bottom: none;
        z-index: 1;
    }

    #cave {
        position: absolute;
        bottom: 0; /* Starts at the bottom of salt layer */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0) 80%); /* Radial gradient for cave */
        border-radius: 50%; /* Start with circular idea, will stretch */
        transition: width 1s ease-out, height 1s ease-out; /* Slower, smoother growth */
        z-index: 0; /* Below salt layer */
        opacity: 0; /* Start hidden */
    }

    #sinkhole {
        position: absolute;
        top: 0; /* At the top of the surface layer */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 100%; /* Takes up height of surface layer */
        background-color: rgba(0, 0, 0, 0.8); /* Dark void color */
        border-radius: 50%; /* Circular shape */
        transition: width 0.4s ease-out, height 0.4s ease-out; /* Fast appearance */
        z-index: 5; /* Above everything else */
        opacity: 0; /* Start hidden */
    }

    .hidden {
        display: none; /* Use JS to toggle this */
    }

    #status-message {
        position: absolute;
        bottom: 15px; /* More space */
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.9em;
        color: #004d40; /* Dark teal */
        background-color: rgba(255, 255, 255, 0.8);
        padding: 8px 12px;
        border-radius: 5px;
        z-index: 5;
        white-space: nowrap; /* Prevent wrapping */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* --- Controls --- */
    #controls {
        text-align: center;
        margin: 20px 0;
        display: flex; /* Use flexbox for centering */
        justify-content: center;
        gap: 10px; /* Space between buttons */
        flex-wrap: wrap; /* Allow buttons to wrap on small screens */
    }

    /* --- Explanation Section --- */
    #explanation-section {
        border-top: 1px solid #ccc;
        margin-top: 30px;
        padding-top: 30px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    #explanation-section h2 {
         text-align: right;
         margin-bottom: 15px;
    }

    #explanation-section h3 {
         text-align: right;
         margin-top: 20px;
         margin-bottom: 8px;
         color: #0275d8;
    }

    #explanation-section p {
        text-align: right;
    }

     #explanation-section ul {
        margin-bottom: 15px;
        padding-right: 30px; /* Adjust padding for RTL */
        text-align: right;
    }
     #explanation-section li {
         margin-bottom: 5px;
         text-align: right;
         list-style-type: disc; /* Use disc bullets */
     }


</style>

<script>
    const waterBtn = document.getElementById('add-water-btn');
    const collapseBtn = document.getElementById('trigger-collapse-btn');
    const resetBtn = document.getElementById('reset-btn');
    const caveDiv = document.getElementById('cave');
    const sinkholeDiv = document.getElementById('sinkhole');
    const soilLayer = document.getElementById('soil-layer');
    const saltLayer = document.getElementById('salt-layer');
    const surfaceLayer = document.getElementById('surface-layer');
    const waterFlowDiv = document.getElementById('water-flow');
    const statusMessageDiv = document.getElementById('status-message');
    const explanationSection = document.getElementById('explanation-section');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');

    let dissolutionInterval = null;
    let caveSize = 0; // Represents cave width in pixels
    const maxCaveWidth = 300; // Max cave width
    const collapseThreshold = maxCaveWidth * 0.7; // Collapse when cave reaches 70% of max width
    let isCollapsed = false;
    const dissolutionSpeed = 150; // Milliseconds per growth step (lower = faster)
    const growthStep = 3; // Pixels per growth step

    function updateCaveVisual() {
        const saltLayerRect = saltLayer.getBoundingClientRect();
        const caveHeight = Math.min(caveSize * 0.6, saltLayerRect.height * 0.9); // Cave height based on width and salt layer height
        const caveTop = saltLayerRect.height - caveHeight; // Position cave at bottom of salt layer visually

        caveDiv.style.width = caveSize + 'px';
        caveDiv.style.height = caveHeight + 'px';
        // Position relative to the bottom of the salt layer element's content box
        caveDiv.style.bottom = '0'; // Anchor to bottom of parent (.salt-layer)
        caveDiv.style.opacity = 1; // Make visible
        caveDiv.classList.remove('hidden');

         // Subtle visual cue on soil layer as cave grows
         if (caveSize > maxCaveWidth * 0.3) {
             const sagAmount = (caveSize / maxCaveWidth) * 5; // Max 5px sag
             soilLayer.style.transform = `translateY(${sagAmount}px)`;
         } else {
             soilLayer.style.transform = 'translateY(0)';
         }
    }

    function startDissolution() {
        if (dissolutionInterval !== null || isCollapsed) return;

        waterBtn.disabled = true;
        // resetBtn.disabled = true; // Keep reset enabled

        waterFlowDiv.classList.remove('hidden');
        waterFlowDiv.style.opacity = 1;
        statusMessageDiv.textContent = 'מים מחלחלים עמוק, ממיסים לאט את שכבת המלח...';

        dissolutionInterval = setInterval(() => {
            if (caveSize < maxCaveWidth) {
                caveSize += growthStep; // Increase size gradually
                 // Clamp caveSize to max
                 if (caveSize > maxCaveWidth) caveSize = maxCaveWidth;

                updateCaveVisual();

                if (caveSize >= collapseThreshold && !isCollapsed && collapseBtn.disabled) {
                    collapseBtn.disabled = false;
                    statusMessageDiv.textContent = 'החלל התת-קרקעי גדל וגדל... הגיע הזמן לזרז קריסה?';
                }

                 if (caveSize >= maxCaveWidth && !isCollapsed) {
                     // Automatic collapse if max size reached without trigger
                      triggerCollapse();
                 }

            } else {
                 // If max size reached and not yet collapsed (e.g., if collapse was manual trigger only)
                 if (!isCollapsed) {
                     statusMessageDiv.textContent = 'החלל התת-קרקעי עצום! קריסה קרובה...';
                 }
                 clearInterval(dissolutionInterval);
                 dissolutionInterval = null;
            }
        }, dissolutionSpeed);
    }

    function triggerCollapse() {
        if (isCollapsed) return;

        clearInterval(dissolutionInterval);
        dissolutionInterval = null;
        waterBtn.disabled = true;
        collapseBtn.disabled = true;
        isCollapsed = true;

        waterFlowDiv.style.opacity = 0;
        // waterFlowDiv.classList.add('hidden'); // Keep element for potential reuse, just hide visually

        statusMessageDiv.textContent = 'האדמה קורסת! בולען אדיר נפער!';
         statusMessageDiv.style.color = '#d32f2f'; // Red color for alert

        // Simulate collapse animation
        const caveRect = caveDiv.getBoundingClientRect();
        const soilRect = soilLayer.getBoundingClientRect();
        const fallDistance = soilRect.height + (saltLayer.getBoundingClientRect().height - caveRect.height - parseFloat(caveDiv.style.bottom || 0)); // Fall into the space occupied by the cave and below it in the salt layer

        soilLayer.style.transition = 'transform 0.4s ease-in'; // Faster, more dramatic fall
        soilLayer.style.transform = `translateY(${fallDistance}px)`;

        // Show sinkhole on the surface
        sinkholeDiv.style.width = Math.min(caveSize * 1.1, surfaceLayer.offsetWidth * 0.9) + 'px'; // Sinkhole slightly larger than cave width for visual effect
        sinkholeDiv.style.height = surfaceLayer.offsetHeight * 2 + 'px'; // Make it visually deep into the soil layer
        sinkholeDiv.classList.remove('hidden');
        sinkholeDiv.style.opacity = 1; // Make visible
        sinkholeDiv.style.transition = 'width 0.5s ease-out, opacity 0.5s ease-out'; // Animate appearance

        // resetBtn.disabled = false; // Keep reset enabled
    }

    function resetSimulation() {
        clearInterval(dissolutionInterval);
        dissolutionInterval = null;
        caveSize = 0;
        isCollapsed = false;

        caveDiv.style.width = '0';
        caveDiv.style.height = '0';
        caveDiv.style.opacity = 0; // Use opacity for smoother hide
        // caveDiv.classList.add('hidden'); // Maybe not needed if opacity is 0

        sinkholeDiv.style.width = '0';
        sinkholeDiv.style.height = '0';
        sinkholeDiv.style.opacity = 0; // Use opacity for smoother hide
        // sinkholeDiv.classList.add('hidden'); // Maybe not needed if opacity is 0

        soilLayer.style.transition = 'transform 0.5s ease-out'; // Reset transition
        soilLayer.style.transform = 'translateY(0)'; // Reset soil position

        waterFlowDiv.style.opacity = 0;
        // waterFlowDiv.classList.add('hidden');

        waterBtn.disabled = false;
        collapseBtn.disabled = true;
        resetBtn.disabled = false;

        statusMessageDiv.textContent = 'לחצו "התחילו להוסיף מים" כדי לצאת למסע התת-קרקעי';
         statusMessageDiv.style.color = '#004d40'; // Reset status color
    }

    function toggleExplanation() {
        const isHidden = explanationSection.style.display === 'none' || explanationSection.style.display === '';
        explanationSection.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מדעי' : 'רוצים להבין יותר? קראו את ההסבר המדעי';
    }

    // Event Listeners
    waterBtn.addEventListener('click', startDissolution);
    collapseBtn.addEventListener('click', triggerCollapse);
    resetBtn.addEventListener('click', resetSimulation);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);

    // Initial state
    resetSimulation(); // Ensure initial state is set correctly
</script>
```