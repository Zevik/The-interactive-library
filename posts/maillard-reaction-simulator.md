---
title: "קסם ההשחמה: סימולטור תגובת מייאר"
english_slug: maillard-reaction-simulator
category: "מדעים מדויקים / כימיה"
tags: [כימיה, בישול, מזון, תגובת מייאר, השחמה, סימולציה, אינטראקטיבי]
---
<section class="intro-section">
    <h1>קסם ההשחמה: סימולטור תגובת מייאר</h1>
    <p>האם אי פעם עצרתם לחשוב מה הופך את קרום הלחם לפריך וזהוב, או מעניק לבשר הצלוי את גווניו העמוקים וטעמיו העשירים? הצטרפו אלינו למסע אל לב המטבח המולקולרי, שם מתרחש תהליך כימי מופלא הידוע כתגובת מייאר. זו לא סתם השחמה, זו כימיה שהופכת מרכיבים פשוטים לחגיגה של צבע, טעם וריח. בואו נתנסה יחד!</p>
</section>

<div class="simulator-container">
    <h2>שחקו עם הכימיה: התנסו בסימולטור</h2>
    <p class="simulator-intro">בחרו את התנאים - טמפרטורה, סוג סוכר וסוג חומצת אמינו - וצפו בקסם קורה בזמן אמת. גלו איך כל גורם משפיע על תוצאת ההשחמה ופיתוח הטעמים.</p>
    <div class="controls">
        <div class="control-group">
            <label for="temperature">טמפרטורה (°C):</label>
            <input type="range" id="temperature" name="temperature" min="50" max="220" value="140" step="1">
            <span id="temperature-value">140</span>°C
        </div>
        <div class="control-group">
            <label for="sugar-type">סוג סוכר:</label>
            <select id="sugar-type" name="sugar-type">
                <option value="glucose">גלוקוז (סוכר ענבים)</option>
                <option value="fructose">פרוקטוז (סוכר פירות)</option>
                <option value="maltose">מלטוז (סוכר לתת)</option>
                <option value="sucrose">סוכרוז (סוכר שולחן)</option>
            </select>
        </div>
        <div class="control-group">
            <label for="amino-acid">סוג חומצת אמינו:</label>
            <select id="amino-acid" name="amino-acid">
                <option value="glycine">גליצין</option>
                <option value="lysine">ליזין</option>
                <option value="proline">פרולין</option>
            </select>
        </div>
    </div>
    <button id="start-simulation">התחילו את התגובה!</button>
    <div class="results">
        <h3>תוצאות הסימולציה:</h3>
        <div id="reaction-visual" class="visual-result">
            <div class="visual-content"></div>
            <div class="progress-bar"></div>
        </div>
        <p id="flavor-description" class="text-result">קבעו את התנאים ולחצו 'התחילו את התגובה!' לראות מה קורה...</p>
    </div>
</div>

<button id="explanation-toggle">רוצים להבין לעומק? הצגת/הסתרת הסבר מפורט</button>

<div id="maillard-explanation">
    <h2>הסבר מפורט: קסם ההשחמה - תגובת מייאר</h2>

    <h3>מהי תגובת מייאר?</h3>
    <p>תגובת מייאר (Maillard reaction), על שם הכימאי הצרפתי לואי קאמיל מייאר שתיאר אותה לראשונה ב-1912, היא סדרה מורכבת של תגובות כימיות המתרחשות בין חומצות אמינו (אבני הבניין של חלבונים) לבין סוכרים מחזרים בנוכחות חום. תגובה זו שונה מקרמליזציה, שהיא פירוק סוכרים בלבד בחום גבוה. תגובת מייאר היא המפתח לצבעים החומים העשירים, לטעמים המורכבים (כמו אגוזי, מאלטי, בשרי, קלוי, קרמלי) ולריחות המפתים שמאפיינים כל כך הרבה מאכלים אהובים.</p>

    <h3>השחקנים הראשיים: סוכרים מחזרים וחומצות אמינו</h3>
    <p>כדי שתגובת מייאר תתרחש, נדרשת נוכחות של שני סוגי מולקולות:</p>
    <ul>
        <li><strong>סוכרים מחזרים:</strong> אלו סוכרים שיש להם קבוצה כימית חופשית (אלדהיד או קטון) שיכולה להשתתף בתגובת חיזור. חד-סוכרים כמו גלוקוז, פרוקטוז וגלקטוז הם תמיד סוכרים מחזרים ומגיבים בקלות. חלק מהדו-סוכרים, כמו מלטוז (שעורה) ולקטוז (חלב), הם גם מחזרים. לעומת זאת, סוכרוז (הסוכר הלבן שאנו מכירים) אינו סוכר מחזר כי הקבוצות הרלוונטיות בו קשורות; הוא ישתתף בתגובת מייאר רק אם יתפרק קודם לכן לגלוקוז ופרוקטוז (למשל בנוכחות חומצה או אנזים, או בחום גבוה מאוד לאורך זמן).</li>
        <li><strong>חומצות אמינו:</strong> אלו המרכיבים הבסיסיים של חלבונים. לכל חומצת אמינו יש קבוצת אמין (-NH₂). בתגובת מייאר, קבוצת האמין של חומצת האמינו מגיבה עם הקבוצה הקרבונילית של הסוכר. סוג חומצת האמינו הוא גורם קריטי בקביעת סוגי מולקולות הטעם והריח הספציפיות שיווצרו. ישנן 20 חומצות אמינו נפוצות בחלבונים, וכל אחת מהן יכולה להוביל לתוצרים ארומטיים שונים מאוד. הסימולטור מתמקד בשלוש לדוגמה: גליצין (תורמת למתיקות, אגוזיות), ליזין (מגיבה בקלות, קשורה לריחות בשר ולחם) ופרולין (קשורה לריחות מאלטיים ומאפייה).</li>
    </ul>

    <h3>מסע ההשחמה: שלבים עיקריים (בפשטות)</h3>
    <p>תגובת מייאר היא למעשה רשת מסועפת של תגובות. הנה פישוט של המסלול העיקרי:</p>
    <ol>
        <li><strong>השלב הראשוני:</strong> הסוכר המחזר וחומצת האמינו מתחברים ליצירת תרכובת ביניים לא יציבה.</li>
        <li><strong>סידור מחדש (Amadori Rearrangement):</strong> תרכובת הביניים עוברת ארגון מחדש פנימי ליצירת "תוצר אמדורי" יציב יותר. בשלב זה עדיין אין צבע או טעם משמעותיים.</li>
        <li><strong>פירוק:</strong> תוצר האמדורי מתפרק בסדרה של תגובות נוספות, כולל איבוד מים. שלב זה הוא קריטי ליצירת מגוון עצום של מולקולות קטנות, רבות מהן נדיפות ובעלות ארומה וטעם חזקים (כמו אלדהידים, קטונים, פוראנים, פיראזינים ועוד). סוגי המולקולות שנוצרות תלויים מאוד בסוגי הסוכרים וחומצות האמינו המגיבים.</li>
        <li><strong>פילמור ויצירת מלנואידינים:</strong> המולקולות הקטנות שנוצרו בשלב הפירוק מתחברות זו לזו (פילמור) ויוצרות מולקולות גדולות ומורכבות הנקראות מלנואידינים. אלו הם הפיגמנטים החומים שאנו רואים במזון המושחם. הם תורמים גם למרקם מסוים ולטעמים עמוקים יותר.</li>
    </ol>

    <h3>גורמים המשפיעים על התגובה</h3>
    <ul>
        <li><strong>טמפרטורה:</strong> זהו הגורם המשפיע ביותר. התגובה מתחילה להיות מורגשת בטמפרטורות מעל 100°C (אחרי שרוב המים התאדו), ומואצת משמעותית ככל שהטמפרטורה עולה (עד לנקודת שריפה).</li>
        <li><strong>פעילות מים (Aw):</strong> התגובה דורשת כמות מים מסוימת, אך לא יותר מדי. היא מתרחשת בצורה מיטבית כשהמזון מתחיל להתייבש על פני השטח (פעילות מים בינונית, Aw 0.3-0.8), כמו בקרום לחם או בשר צלוי. במזון יבש לחלוטין או רטוב מאוד, התגובה איטית.</li>
        <li><strong>pH:</strong> התגובה מהירה יותר בסביבה מעט בסיסית (pH 6-8), אך מתרחשת גם בסביבה ניטרלית או מעט חומצית. בסביבה חומצית מאוד היא כמעט נעצרת.</li>
        <li><strong>סוגי המגיבים:</strong> כפי שראיתם בסימולטור, סוג הסוכר המחזר וסוג חומצת האמינו משפיעים משמעותית על קצב התגובה ועל סוגי הטעמים והצבעים שנוצרים.</li>
    </ul>

    <h3>תגובת מייאר בחיי היומיום</h3>
    <p>הבנת תגובת מייאר מסייעת לנו להבין ולשלוט טוב יותר בתהליכי בישול רבים:</p>
    <ul>
        <li><strong>אפייה:</strong> יצירת הקרום החום והארומטי של לחמים, עוגות ועוגיות.</li>
        <li><strong>צלייה וטיגון:</strong> השחמת פני השטח של בשר, עופות, דגים וירקות, ויצירת טעמים עמוקים.</li>
        <li><strong>קלייה:</strong> פיתוח הטעם והצבע הייחודיים של קפה, פולי קקאו, אגוזים וזרעים.</li>
        <li><strong>הכנת רטבים:</strong> יצירת צבעים וטעמים עשירים ברוטב בשר (Gravy) או בצלי בצל.</li>
    </ul>
    <p>תגובת מייאר היא דוגמה מופלאה לאופן שבו כימיה פשוטה יחסית (על פני השטח) יוצרת מורכבות קולינרית אינסופית. עכשיו כשאתם יודעים, תוכלו לצפות בה קורית במטבח שלכם ולהעריך את הקסם שמאחורי כל ביס שחום וטעים.</p>
</div>

<style>
    /* כללי */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
    }

    h1, h2, h3 {
        color: #5a3e2b; /* Warm brown */
        margin-bottom: 15px;
        text-align: center; /* Center titles */
    }

    h1 {
        font-size: 2.5em;
        margin-top: 0;
        border-bottom: 2px solid #d4a373; /* Complementary line */
        padding-bottom: 10px;
    }

    h2 {
        font-size: 1.8em;
        color: #7f5539; /* Darker warm brown */
    }

     h3 {
        font-size: 1.4em;
        color: #9c6644; /* Medium warm brown */
        margin-bottom: 10px;
    }


    p {
        margin-bottom: 1em;
    }

    ul, ol {
        margin-bottom: 1em;
        padding-right: 25px; /* Adjust padding for RTL list */
    }

    li {
        margin-bottom: 0.5em;
    }

    /* Simulator Container */
    .simulator-container {
        background-color: #fff8f0; /* Very light warm background */
        border: 1px solid #d4a373; /* Warm border */
        border-radius: 12px;
        padding: 30px;
        margin: 30px auto; /* Center the container */
        max-width: 800px; /* Limit width */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        text-align: right;
    }

    .simulator-intro {
        text-align: center;
        margin-bottom: 25px;
        color: #6f451f; /* Slightly darker text */
    }

    /* Controls */
    .controls {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Increased gap */
        margin-bottom: 30px;
    }

    .control-group {
        display: flex;
        align-items: center;
        gap: 15px; /* Increased gap */
        flex-wrap: wrap;
    }

    .control-group label {
        font-weight: bold;
        min-width: 150px; /* Wider label for better alignment */
        text-align: right;
        color: #7f5539;
    }

    .control-group input[type="range"] {
        flex-grow: 1;
        min-width: 180px; /* Ensure range is wide enough */
        -webkit-appearance: none; /* Remove default style */
        appearance: none;
        height: 8px;
        background: #d4a373; /* Warm track */
        outline: none;
        opacity: 0.8;
        transition: opacity .2s ease;
        border-radius: 4px;
    }

     .control-group input[type="range"]:hover {
        opacity: 1;
     }

     .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #9c6644; /* Thumb color */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #7f5539;
     }

     .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #9c6644; /* Thumb color */
        cursor: pointer;
        border-radius: 50%;
        border: 2px solid #7f5539;
     }


    .control-group select {
        flex-grow: 1;
        min-width: 180px;
        padding: 10px; /* More padding */
        border-radius: 6px;
        border: 1px solid #d4a373;
        background-color: #fff;
        font-size: 1em;
        color: #333;
        cursor: pointer;
    }

    .control-group span {
        min-width: 30px; /* Space for value */
        text-align: left; /* Value alignment */
        font-weight: bold;
        color: #5a3e2b;
    }


    /* Simulation Button */
    #start-simulation {
        display: block;
        width: fit-content; /* Button size based on content */
        margin: 20px auto; /* Center button */
        padding: 12px 25px; /* Increased padding */
        background-color: #9c6644; /* Warm button color */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }

    #start-simulation:hover {
        background-color: #7f5539; /* Darker on hover */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }

    #start-simulation:active {
        transform: scale(0.98); /* Slight press effect */
    }

    /* Results Section */
    .results {
        margin-top: 40px; /* More space */
        padding-top: 30px;
        border-top: 2px dashed #d4a373; /* Dashed separator */
        text-align: center;
    }

    .visual-result {
        position: relative; /* Needed for absolute children */
        width: 150px; /* Larger visual */
        height: 150px;
        margin: 25px auto;
        border-radius: 15px; /* Rounded corners */
        background-color: #fff; /* Default white */
        border: 2px solid #ccc;
        overflow: hidden; /* Hide anything outside */
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: background-color 1.5s ease-in-out, border-color 0.5s ease; /* Slower, smoother color transition */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.9em;
        color: #555;
        text-align: center;
        padding: 10px; /* Add some padding */
        box-sizing: border-box; /* Include padding in size */
    }

    .visual-result .visual-content {
         width: 100%;
         height: 100%;
         display: flex;
         justify-content: center;
         align-items: center;
         background-size: cover; /* Or 'contain' */
         background-position: center;
         /* Initial state - maybe a subtle pattern or just empty */
         background-image: radial-gradient(#eee 10%, transparent 10%), radial-gradient(#eee 10%, transparent 10%);
         background-size: 20px 20px;
         background-position: 0 0, 10px 10px;
    }

     /* Animation for cooking/heating */
     @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.03); opacity: 0.95; }
        100% { transform: scale(1); opacity: 1; }
     }

    .visual-result.cooking {
        animation: pulse 1.5s infinite ease-in-out;
        border-color: #e94e1b; /* Hot color */
    }

    /* Progress bar (simple example) */
    .visual-result .progress-bar {
        position: absolute;
        bottom: 0;
        right: 0; /* RTL */
        height: 5px;
        background-color: #d4a373; /* Initial color */
        width: 0%; /* Starts empty */
        transition: width 4s linear; /* Matches simulation duration */
    }

    .visual-result.cooking .progress-bar {
         width: 100%; /* Fills up during simulation */
         background-color: #e94e1b; /* Changes color as it progresses */
    }


    .text-result {
        font-size: 1.2em; /* Larger text */
        color: #5a3e2b;
        min-height: 3em; /* Reserve more space */
        margin-top: 20px;
        font-weight: bold;
    }

    /* Explanation Toggle Button */
    #explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto 20px auto; /* Center and position */
        padding: 10px 20px;
        background-color: #a5a58d; /* Muted green/grey */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }
    #explanation-toggle:hover {
         background-color: #8b8b7a;
    }

    /* Explanation Section Styling */
    #maillard-explanation {
        display: none; /* Initially hidden */
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #a5a58d;
        border-radius: 10px;
        background-color: #f0f0e8; /* Light muted background */
        text-align: right;
        direction: rtl;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }

    #maillard-explanation h3 {
        color: #7f5539;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #d4a373; /* Warm separator */
        padding-bottom: 5px;
    }

    #maillard-explanation p {
        line-height: 1.7; /* Improved readability */
        margin-bottom: 15px;
    }

    #maillard-explanation ul, #maillard-explanation ol {
        margin-bottom: 15px;
        padding-right: 25px;
    }

    #maillard-explanation li {
        margin-bottom: 8px;
    }
</style>

<script>
    const temperatureInput = document.getElementById('temperature');
    const temperatureValueSpan = document.getElementById('temperature-value');
    const sugarTypeSelect = document.getElementById('sugar-type');
    const aminoAcidSelect = document.getElementById('amino-acid');
    const startSimulationButton = document.getElementById('start-simulation');
    const reactionVisualDiv = document.getElementById('reaction-visual');
    const visualContentDiv = reactionVisualDiv.querySelector('.visual-content'); // Get the inner div for content/texture
    const progressBar = reactionVisualDiv.querySelector('.progress-bar');
    const flavorDescriptionP = document.getElementById('flavor-description');
    const explanationToggleBtn = document.getElementById('explanation-toggle');
    const explanationDiv = document.getElementById('maillard-explanation');

    // Update temperature value display on input change
    temperatureInput.addEventListener('input', () => {
        temperatureValueSpan.textContent = temperatureInput.value;
    });

    // Simulation logic
    startSimulationButton.addEventListener('click', () => {
        const temp = parseInt(temperatureInput.value);
        const sugar = sugarTypeSelect.value;
        const aminoAcid = aminoAcidSelect.value;

        // Disable button and add cooking class
        startSimulationButton.disabled = true;
        startSimulationButton.textContent = 'מבשלים...';
        reactionVisualDiv.classList.add('cooking');
        progressBar.style.width = '0%'; // Reset progress bar
        progressBar.style.transition = 'none'; // Disable transition for reset
        requestAnimationFrame(() => { // Use rAF to ensure reset happens before enabling transition
             progressBar.style.transition = 'width 4s linear'; // Re-enable transition
             progressBar.style.width = '100%'; // Start progress
        });


        // Simulate a delay for the "cooking" process
        const simulationDuration = 4000; // 4 seconds

        // Determine results after the delay
        setTimeout(() => {
            let color = '#ffffff'; // Default white
            let description = 'ממתין לתוצאות...'; // Default waiting text

            // Simple logic based on parameters - more detailed descriptions
            if (sugar === 'sucrose') {
                // Sucrose is non-reducing, minimal reaction unless very high temp or long time (hydrolysis/caramelization)
                if (temp >= 180) {
                     // Simulate some potential for caramelization or minor hydrolysis reaction at high temp
                     color = '#f0a060'; // Light brown/caramel
                     description = 'סוכרוז אינו סוכר מחזר. בטמפרטורה גבוהה מאוד ייתכן רמז לקרמל או השחמה קלה עקב פירוק.';
                } else {
                     color = '#ffffff'; // No reaction
                     description = 'סוכרוז אינו סוכר מחזר - אין תגובת מייאר ישירה בתנאים אלה.';
                }
            } else { // Reducing sugars (glucose, fructose, maltose)
                if (temp < 90) {
                    color = '#f8f8f8'; // Very very light
                    description = 'טמפרטורה נמוכה מדי. התגובה איטית מאוד וכמעט בלתי מורגשת.';
                } else if (temp >= 90 && temp < 120) {
                    // Very light browning
                    color = '#f0e0d0';
                    description = 'השחמה עדינה מאוד מתחילה. טעמים ראשוניים מתפתחים.';
                    if (aminoAcid === 'glycine') description += ' רמז למתיקות עדינה.';
                    if (aminoAcid === 'lysine') description += ' ניצני ארומת "אפייה".';
                    if (aminoAcid === 'proline') description += ' ניצני ארומה מאלטית.';

                } else if (temp >= 120 && temp < 150) {
                    // Medium browning
                    color = '#d4a373'; // Warm medium brown
                    description = 'השחמה מתונה. טעמים אופייניים מתחילים להתפתח.';
                     if (sugar === 'glucose') description += ' בסיס לטעמי לחם ובשר בהיר.';
                     if (sugar === 'fructose') description += ' בסיס לטעמים פירותיים-קרמליים.';
                     if (sugar === 'maltose') description += ' בסיס לטעמים מאלטיים וקלויים עדינים.';

                    if (aminoAcid === 'glycine') description += ' טעמים מתוקים-אגוזיים עדינים.';
                    if (aminoAcid === 'lysine') description += ' טעמי לחם אפוי ובשר בהיר מודגשים.';
                    if (aminoAcid === 'proline') description += ' טעמים מאלטיים של מאפייה.';

                } else if (temp >= 150 && temp < 180) {
                    // Intense browning
                    color = '#9c6644'; // Rich brown
                    description = 'השחמה עמוקה ופיתוח טעמים מורכבים.';
                     if (sugar === 'glucose') description += ' טעמים עשירים של לחם קלוי ובשר צלוי.';
                     if (sugar === 'fructose') description += ' טעמים קרמליים עמוקים ופירותיים קלויים.';
                     if (sugar === 'maltose') description += ' טעמים מאלטיים מודגשים וארומות קלייה.';

                    if (aminoAcid === 'glycine') description += ' טעמים מתוקים קלויים, אגוזיים עזים.';
                    if (aminoAcid === 'lysine') description += ' טעמים בשריים חזקים, ארומת קרום לחם כהה.';
                    if (aminoAcid === 'proline') description += ' טעמים מאלטיים חזקים, ארומת מאפייה עשירה ומודגשת.';

                } else { // temp >= 180
                    // Very Intense browning / Potential burning
                    color = '#5a3e2b'; // Very dark brown
                    description = 'השחמה אינטנסיבית מאוד, טעמים חזקים ומורכבים.';
                     if (sugar === 'glucose') description += ' טעמים עזים של לחם קלוי ובשר שחום.';
                     if (sugar === 'fructose') description += ' טעמים קרמליים שרופים קלות.';
                     if (sugar === 'maltose') description += ' טעמים מאלטיים קלויים מאוד.';


                    if (aminoAcid === 'glycine') description += ' טעמים מתוקים-קלויים, אגוזיים חזקים.';
                    if (aminoAcid === 'lysine') description += ' טעמים בשריים עזים, גוונים כהים של קרום לחם.';
                    if (aminoAcid === 'proline') description += ' טעמים מאלטיים שרופים קלות.';

                    if (temp > 200) {
                        color = '#331a0a'; // Almost black
                        description += ' זהירות: בטמפרטורות גבוהות מאוד (מעל 200°C) יש סיכון גבוה לשריפה ויצירת טעמים מרים ותרכובות לא רצויות (כמו אקרילאמיד).';
                    }
                }
            }

            // Update the visual and text results
            reactionVisualDiv.style.backgroundColor = color;
            flavorDescriptionP.textContent = description;

            // Remove cooking class and enable button
            reactionVisualDiv.classList.remove('cooking');
            startSimulationButton.disabled = false;
            startSimulationButton.textContent = 'התחילו את התגובה!';

        }, simulationDuration); // End of setTimeout
    });

    // Toggle explanation visibility
    explanationToggleBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationToggleBtn.textContent = isHidden ? 'רוצים להבין לעומק? הסתרת הסבר מפורט' : 'רוצים להבין לעומק? הצגת הסבר מפורט';
    });

    // Initial state of explanation
    explanationDiv.style.display = 'none';

    // Initial state of visual result text
    flavorDescriptionP.textContent = 'קבעו את התנאים ולחצו \'התחילו את התגובה!\' לראות מה קורה...';

</script>
```