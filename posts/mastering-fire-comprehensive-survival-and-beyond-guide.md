---
title: "אמנות האש: מדריך מקיף לבניית מדורות הישרדות ויותר"
english_slug: mastering-fire-comprehensive-survival-and-beyond-guide
category: "מדעי הטבע"
tags:
  - הישרדות
  - פיזיקה
  - בעירה
  - אש
  - מדורות
  - מדע
---
# אמנות האש: מדריך מקיף לבניית מדורות הישרדות ויותר
האם ידעת ששליטה במבנה המדורה ובחומרי הבעירה יכולה לשנות את גורלך בשטח? מדורה היא לא רק ערימת עצים בוערת; זו מערכת פיזיקלית דינמית שמגיבה לחוקי הטבע. הבנת איך להתאים את המדורה שלך למטרה – בין אם זה להרתיח מים לדקות ספורות, לשמור על חום כל הלילה, או לאותת למרחקים – היא מיומנות הישרדות חיונית ואמנות בפני עצמה. צלול לסימולטור האינטראקטיבי שלנו וגלה את הסודות מאחורי להבה מושלמת!

<div class="fire-simulator app-container">
    <h2 class="app-title">סימולטור אמנות האש</h2>
    <p class="app-intro">בנה את המדורה הווירטואלית שלך ובדוק כמה היא מתאימה למטרתך!</p>

    <div class="control-section goal-section">
        <label for="goal" class="control-label">בחר את המטרה שלך:</label>
        <select id="goal" class="control-select">
            <option value="fast_heat">השגת חום מקסימלי במהירות (למשל, הרתחת מים)</option>
            <option value="long_burn">שמירה על גחלים יציבות לאורך זמן (למשל, חימום ללילה)</option>
            <option value="high_flame">יצירת להבה גבוהה ובולטת (למשל, איתות)</option>
            <option value="steady_cook">חום יציב ואחיד לבישול ממושך</option>
        </select>
    </div>

    <div class="control-section materials-section">
        <h3 class="section-title">בחר את חומרי הבעירה שלך:</h3>
        <div class="material-selection">
            <label for="tinder" class="control-label">ניצוץ ראשוני (Tinder):</label>
            <select id="tinder" class="control-select">
                <option value="small_twigs">ענפים וזרדים דקים מאוד</option>
                <option value="leaves">ענפים דקים + עלים/עשבים יבשים</option>
            </select>
        </div>
        <div class="material-selection">
            <label for="kindling" class="control-label">חומרי תבערה (Kindling):</label>
            <select id="kindling" class="control-select">
                <option value="medium_branches">ענפים בינוניים (עובי אצבע)</option>
                <option value="thick_branches">ענפים עבים יותר (עובי יד)</option>
            </select>
        </div>
        <div class="material-selection">
            <label for="fuel" class="control-label">דלק ראשי (Fuelwood):</label>
            <select id="fuel" class="control-select">
                <option value="small_logs">גזעים קטנים/בינוניים</option>
                <option value="large_logs">גזעים גדולים וכבדים</option>
            </select>
        </div>
    </div>

    <div class="control-section structure-section">
        <h3 class="section-title">בחר את מבנה המדורה שלך:</h3>
        <div class="structure-buttons">
            <button class="structure-btn" data-structure="teepee">פירמידה (Teepee)</button>
            <button class="structure-btn" data-structure="log_cabin">כלוב (Log Cabin)</button>
            <button class="structure-btn" data-structure="star">כוכב (Star)</button>
            <button class="structure-btn" data-structure="trench">טרנץ' (Trench)</button>
        </div>
        <div id="selected-structure" class="selection-display">מבנה נבחר: <span class="selection-value">אף אחד</span></div>
    </div>

    <button id="start-simulation" class="action-button">הדלק את המדורה!</button>

    <div class="simulation-results results-section">
        <h3 class="section-title">תוצאות הסימולציה:</h3>
        <div id="fire-visual" class="fire-visual">🔥</div>
        <p>טמפרטורה מקסימלית: <span id="max-temp">-</span>°C</p>
        <p>זמן בעירה משוער: <span id="burn-time">-</span> דקות</p>
        <p>עוצמת להבה: <span id="flame-height">-</span></p>
    </div>

    <div class="feedback-section">
        <h3 class="section-title">פידבק והמלצות:</h3>
        <p id="feedback-text" class="feedback-text"></p>
    </div>
</div>

<style>
/* General App Styling */
.app-container {
    font-family: 'Arial', sans-serif; /* Changed font for a cleaner look */
    max-width: 750px; /* Slightly wider */
    margin: 30px auto; /* More margin */
    padding: 30px;
    border: 1px solid #e0e0e0; /* Lighter border */
    border-radius: 12px; /* More rounded corners */
    background-color: #ffffff; /* White background */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    color: #333;
}

.app-title {
    text-align: center;
    color: #d9534f; /* Warm red */
    margin-bottom: 15px;
    font-size: 2em; /* Larger title */
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.05); /* Light text shadow */
}

.app-intro {
    text-align: center;
    margin-bottom: 25px;
    color: #555;
    font-size: 1.1em;
}

.control-section {
    margin-bottom: 25px; /* More space between sections */
    padding: 20px; /* More padding */
    border: 1px solid #f0f0f0; /* Very light border */
    border-radius: 8px;
    background-color: #fefefe; /* Slightly off-white */
}

.section-title {
    color: #f0ad4e; /* Orange */
    border-bottom: 2px solid #f0ad4e; /* Matching bottom border */
    padding-bottom: 8px;
    margin-bottom: 20px; /* More space below title */
    font-size: 1.3em;
}

/* Control Styling */
.control-label {
    display: block; /* Labels on new lines */
    margin-bottom: 8px; /* Space below label */
    font-weight: bold;
    color: #555;
    font-size: 1em;
}

.control-select {
    width: 100%; /* Full width selects */
    padding: 10px; /* More padding */
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1em;
    box-sizing: border-box; /* Include padding in width */
    appearance: none; /* Remove default system styling */
    background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.362%22%20height%3D%22292.362%22%3E%3Cpath%20fill%3D%22%23007bff%22%20d%3D%22M287.929%2069.396c-3.704-3.704-9.697-3.704-13.399%200l-123.398%20123.398L28.929%2069.396c-3.704-3.704-9.697-3.704-13.399%200-3.705%203.704-3.705%209.697%200%2013.399l130.098%20130.098c1.852%201.852%204.285%202.78%206.717%202.78s4.866-.928%206.717-2.78l130.098-130.098c3.704-3.702%203.704-9.695%200-13.399z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
    background-repeat: no-repeat;
    background-position: right 10px top 50%;
    background-size: 12px auto;
    padding-right: 30px; /* Make space for custom arrow */
}

.material-selection {
    margin-bottom: 15px; /* Space between material selects */
}

/* Structure Button Styling */
.structure-buttons {
    display: flex; /* Use flexbox for layout */
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    gap: 10px; /* Space between buttons */
    margin-bottom: 15px;
}

.structure-btn {
    flex-grow: 1; /* Allow buttons to grow */
    padding: 12px 18px; /* More padding */
    border: 1px solid #5bc0de; /* Info blue */
    border-radius: 25px; /* Pill shape */
    background-color: #5bc0de;
    color: white;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
    text-align: center;
}

.structure-btn:hover {
    background-color: #31b0d5;
    border-color: #269abc;
    transform: translateY(-2px); /* Slight lift effect */
}

.structure-btn.selected {
    background-color: #5cb85c; /* Success green */
    border-color: #4cae4c;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow on selected */
    transform: none; /* No lift when selected */
}

.selection-display {
    margin-top: 10px;
    font-size: 1.1em;
    color: #555;
}

.selection-value {
    font-weight: bold;
    color: #333;
}


/* Action Button Styling */
.action-button {
    display: block;
    width: 100%;
    padding: 15px; /* More padding */
    background-color: #d9534f; /* Danger red */
    color: white;
    border: none;
    border-radius: 8px; /* More rounded */
    font-size: 1.2em; /* Larger font */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    margin-bottom: 30px; /* Space below button */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Button shadow */
}

.action-button:hover {
    background-color: #c9302c;
    transform: translateY(-2px); /* Lift effect */
}

.action-button:active {
    transform: translateY(0); /* Press effect */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Results Section Styling */
.results-section {
    margin-top: 30px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9; /* Light grey background */
    transition: opacity 0.5s ease; /* Fade in effect */
    opacity: 1; /* Default visible */
}

/* Class to hide results section with fade */
.results-section.hidden {
    opacity: 0;
    height: 0;
    padding-top: 0;
    padding-bottom: 0;
    margin-top: 0;
    margin-bottom: 0;
    overflow: hidden;
}


.fire-visual {
    font-size: 4em; /* Larger emoji */
    text-align: center;
    margin-bottom: 20px;
    transition: transform 0.5s ease; /* Animation for fire visual */
    display: flex; /* Use flexbox to center multiple emojis */
    justify-content: center;
    align-items: center;
    min-height: 1.5em; /* Reserve space even if empty */
}

.simulation-results p {
    margin-bottom: 10px; /* More space between results */
    font-size: 1.1em;
}

/* Feedback Section Styling */
.feedback-section {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #d1ecf1; /* Info blue border */
    border-radius: 8px;
    background-color: #e2f2f3; /* Light info blue background */
}

.feedback-text {
    font-size: 1.1em;
    line-height: 1.6;
    color: #0c5460; /* Dark info blue text */
}

/* Explanation Section Styling */
#toggle-explanation {
    display: block;
    width: 100%;
    padding: 12px;
    background-color: #6c757d; /* Secondary grey */
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    margin-top: 20px;
}
#toggle-explanation:hover {
     background-color: #5a6268;
     transform: translateY(-2px);
}
#toggle-explanation:active {
     transform: translateY(0);
}


#explanation {
    margin-top: 20px;
    padding: 30px; /* More padding */
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #fff;
    display: none; /* Hidden by default */
    line-height: 1.7; /* Improved readability */
}

#explanation h2 {
    color: #d9534f; /* Matching app title color */
    margin-bottom: 15px;
    font-size: 1.8em;
    border-bottom: none; /* Removed border for cleaner look */
}

#explanation h3 {
    color: #f0ad4e; /* Matching section title color */
    border-bottom: 1px solid #f0ad4e; /* Lighter border */
    padding-bottom: 5px;
    margin-bottom: 15px; /* More space below h3 */
    font-size: 1.4em;
}

#explanation p {
    margin-bottom: 18px; /* More space below paragraphs */
    color: #444;
}

#explanation ul {
    margin-bottom: 18px;
    padding-left: 25px; /* More padding for list */
}

#explanation li {
    margin-bottom: 10px; /* More space between list items */
    color: #444;
}

#explanation li strong {
    color: #333; /* Stronger color for bold text */
}
</style>

<button id="toggle-explanation">רוצה להבין את המדע שמאחורי זה? הצג הסבר מפורט</button>

<div id="explanation">
    <h2>הסבר מפורט: עקרונות יסוד באמנות האש</h2>

    <h3>משולש האש: הבסיס לכל בעירה</h3>
    <p>בעירה, או שריפה, היא תגובה כימית הדורשת שלושה מרכיבים חיוניים, המוכרים כ"משולש האש":</p>
    <ol>
        <li><strong>דלק (Fuel):</strong> כל חומר הניתן לבעירה, במקרה של מדורה - עץ. גדלים שונים של עץ נשרפים בקצבים שונים ומספקים אנרגיה (חום) לפרקי זמן שונים.</li>
        <li><strong>מחמצן (Oxidizer):</strong> ברוב המקרים, זהו החמצן שבאוויר. בעירה יעילה דורשת אספקה רציפה של חמצן לאזור הבעירה. מבנה המדורה משפיע ישירות על זרימת האוויר.</li>
        <li><strong>חום (Heat):</strong> אנרגיית התחלה שמביאה את הדלק לטמפרטורת ההתלקחות שלו. הניצוץ הראשוני או הלהבה הקטנה מספקים חום זה, ולאחר מכן החום המופק מהבעירה עצמה ממשיך לקיים את התגובה.</li>
    </ol>
    <p>הסרת אחד מהמרכיבים הללו תגרום להפסקת הבעירה (כיבוי האש).</p>

    <h3>חומרי בערה בשלבים: מהדק לעבה</h3>
    <p>בניית מדורה מוצלחת דורשת מעבר הדרגתי מדלקים שנדלקים בקלות לדלקים שבוערים לאורך זמן. אנו מחלקים את חומרי הבעירה בדרך כלל לשלושה שלבים:</p>
    <ul>
        <li><strong>Tinder (ניצוץ ראשוני):</strong> חומרים דקים, יבשים ואווריריים שנדלקים מניצוץ קטן או גפרור בודד. זהו השלב הקריטי להתנעת האש. דוגמאות: כותנה, קליפת עץ דקה, עלים יבשים פריכים, קש, נוצות.</li>
        <li><strong>Kindling (חומרי תבערה):</strong> חומרים עבים יותר מה-Tinder, אך עדיין דקים מספיק כדי להידלק בקלות מהם. אלו ענפים קטנים ועצים בעובי אצבע עד זרוע. הם מספקים מספיק חום כדי להדליק את הדלק הראשי.</li>
        <li><strong>Fuelwood (דלק ראשי):</strong> גזעים וענפים עבים יותר שמספקים את החום העיקרי ושומרים על האש בוערת לאורך זמן. קצב הבעירה שלהם איטי יותר, והם דורשים כמות משמעותית של חום מחומרי התבערה כדי להידלק היטף.</li>
    </ul>
    <p>מעבר חלק בין השלבים הללו מבטיח שהאש לא תדעך לפני שהדלק הראשי נדלק במלואו.</p>

    <h3>מבני מדורות והפיזיקה שמאחוריהם:</h3>
    <p>צורת המדורה משפיעה על זרימת האוויר (חמצן) ועל אופן פיזור החום, ובכך קובעת את מאפייני הבעירה:</p>
    <ul>
        <li><strong>מדורת פירמידה (Teepee):</strong> חומרי בערה מסודרים בצורת חרוט, כשהדקים במרכז והעבים יותר מבחוץ. מבנה זה יוצר "אפקט ארובה" - אוויר קר נכנס מלמטה, מתחמם, עולה למעלה ומושך עוד אוויר קר פנימה. מעודד זרימת אוויר מצוינת והתלקחות מהירה. טוב לחום התחלתי חזק ולהבה גבוהה, אך בוער מהר יחסית.</li>
        <li><strong>מדורת כלוב (Log Cabin):</strong> גזעים עבים יותר מונחים בצורת ריבוע (או "כלוב"), עם חומרי בערה דקים יותר בפנים. המבנה יציב ומתמוטט פנימה תוך כדי בעירה. מספק זרימת אוויר טובה יחסית ושומר על חום יציב לאורך זמן בינוני. מצוין לבישול וחימום קבוע.</li>
        <li><strong>מדורת כוכב (Star Fire):</strong> גזעים ארוכים מונחים בצורת כוכב, עם הקצוות נפגשים במרכז בו בוערת האש. ככל שהקצוות נשרפים, דוחפים את הגזעים פנימה. דורשת מינימום תחזוקה ומתאימה במיוחד לשמירה על גחלים בוערות וחום לזמן ארוך מאוד (כל הלילה). זרימת האוויר מוגבלת יחסית במרכז, מה שמעודד בעירה איטית ויצירת גחלים.</li>
        <li><strong>מדורת טרנץ' (Trench Fire):</strong> נבנית בתוך חפירה צרה באדמה. האדמה מגנה על האש מרוח ומכוונת את החום כלפי מעלה בקו ישר. זהו מבנה יעיל במיוחד לבישול באמצעות חום מרוכז ישירות מעל הטרנץ', ומצוין גם להחזרת חום (כשהחפירה משמשת כרדיאטור).</li>
    </ul>

    <h3>התאמת המדורה למטרה: להיות אמן אש</h3>
    <p>כעת, כשהבנת את העקרונות, תוכל לבחור את השילוב הנכון:</p>
    <ul>
        <li><strong>לחימום מהיר (הרתחת מים):</strong> בחר במבנה פירמידה (Teepee) עם חומרי תבערה ודלק ראשי בגדלים קטנים ובינוניים. מבנה הפירמידה מבטיח זרימת אוויר וחום התחלתי מקסימלי.</li>
        <li><strong>לשמירה על גחלים לאורך זמן (חימום ללילה):</strong> מדורת כוכב (Star Fire) עם גזעים גדולים היא הבחירה האולטימטיבית. היא בוערת לאט ודורשת מעט תחזוקה.</li>
        <li><strong>ליצירת להבה גבוהה (איתות):</strong> מבנה פירמידה (Teepee) גבוה ומרשים, או כלוב (Log Cabin) עם דלק ראשי בינוני-גדול. אלו מבנים שמאפשרים ללהבה להתפתח לגובה ולבלוט.</li>
        <li><strong>לבישול יציב (ארוחה ממושכת):</strong> מדורת כלוב (Log Cabin) או טרנץ' (Trench Fire) עם דלק ראשי בינוני-גדול. מבנים אלו מספקים חום אחיד ומשטח נוח לבישול.</li>
    </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const goalSelect = document.getElementById('goal');
    const tinderSelect = document.getElementById('tinder');
    const kindlingSelect = document.getElementById('kindling');
    const fuelSelect = document.getElementById('fuel');
    const structureButtons = document.querySelectorAll('.structure-btn');
    const selectedStructureSpan = document.querySelector('#selected-structure .selection-value'); // Use span inside
    const startSimulationBtn = document.getElementById('start-simulation');
    const maxTempSpan = document.getElementById('max-temp');
    const burnTimeSpan = document.getElementById('burn-time');
    const flameHeightSpan = document.getElementById('flame-height');
    const fireVisualDiv = document.getElementById('fire-visual');
    const feedbackTextP = document.getElementById('feedback-text');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const resultsSection = document.querySelector('.simulation-results'); // Get the results section

    let selectedStructure = null;

    // Event listeners for structure selection
    structureButtons.forEach(button => {
        button.addEventListener('click', () => {
            structureButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            selectedStructure = button.dataset.structure;
            selectedStructureSpan.textContent = button.textContent; // Update span
        });
    });

    // Simulation Logic (More sophisticated and rule-based)
    const simulateFire = () => {
        const goal = goalSelect.value;
        const tinder = tinderSelect.value;
        const kindling = kindlingSelect.value;
        const fuel = fuelSelect.value;

        if (!selectedStructure) {
            feedbackTextP.textContent = "רגע לפני האש! 🔥 אנא בחר מבנה מדורה כדי להתחיל.";
            fireVisualDiv.textContent = '🪵🪵🪵'; // Show logs waiting
            maxTempSpan.textContent = '-';
            burnTimeSpan.textContent = '-';
            flameHeightSpan.textContent = '-';
            resultsSection.classList.add('hidden'); // Hide results until simulation starts
            return;
        }

        // Show results section with fade-in
        resultsSection.classList.remove('hidden');


        // --- Simulation Model Parameters (Rule-based) ---
        // Factors for materials (relative contribution to metrics)
        const tinderProps = { small_twigs: { ignite: 1.2, temp: 0.5, time: 0.3, flame: 0.7 }, leaves: { ignite: 1, temp: 0.6, time: 0.4, flame: 0.8 } };
        const kindlingProps = { medium_branches: { ignite: 1.5, temp: 1.5, time: 0.8, flame: 1.2 }, thick_branches: { ignite: 0.8, temp: 1.2, time: 1.0, flame: 1.0 } };
        const fuelProps = { small_logs: { ignite: 0.5, temp: 1.0, time: 1.5, flame: 0.9 }, large_logs: { ignite: 0.2, temp: 0.8, time: 2.5, flame: 0.6 } };

        // Factors for structures (multiplier for metrics, and special behaviors)
        const structureProps = {
            teepee: { temp: 1.8, time: 0.7, flame: 2.0, stability: 0.5, air: 1.8 }, // Fast, high flame, less stable, high airflow
            log_cabin: { temp: 1.4, time: 1.3, flame: 1.2, stability: 1.5, air: 1.2 }, // Steady, good burn time, stable, good airflow
            star: { temp: 1.0, time: 2.5, flame: 0.8, stability: 1.8, air: 0.7 }, // Long burn, low flame, very stable, low airflow in center
            trench: { temp: 1.6, time: 1.1, flame: 1.0, stability: 1.0, air: 1.1, concentrated: 1.5 } // Concentrated heat, good stability, decent airflow
        };

        const currentTinder = tinderProps[tinder];
        const currentKindling = kindlingProps[kindling];
        const currentFuel = fuelProps[fuel];
        const currentStructure = structureProps[selectedStructure];

        // --- Calculate Simulated Metrics (Arbitrary scale, combined factors) ---
        // Temperature: influenced by kindling (fast heat), fuel (sustained heat), structure (airflow/convection)
        let maxTemp = Math.round(
            (currentTinder.temp * 50) + // Small contribution from tinder
            (currentKindling.temp * 150 * currentStructure.air) + // Kindling provides initial spike, amplified by air
            (currentFuel.temp * 100 * currentStructure.temp) // Fuel provides bulk heat, amplified by structure temp factor
        );
        if(currentStructure.concentrated) maxTemp = Math.round(maxTemp * currentStructure.concentrated); // Trench concentrates heat

        // Burn Time: primarily fuel, influenced by kindling (how well fuel ignites) and structure (airflow - faster burn vs slower)
        let burnTime = Math.round(
            (currentTinder.time * 2) + // Tiny contribution from tinder
            (currentKindling.time * 5) + // Kindling burns quickly
            (currentFuel.time * 15 * currentStructure.time) // Fuel determines main duration, adjusted by structure time factor
        );
        // Structures with high airflow might burn faster overall even with lots of fuel
         if (currentStructure.air > 1.5 && currentFuel.time < 2) burnTime = Math.round(burnTime * 0.8); // Teepee with small fuel burns faster
         if (currentStructure.air < 0.8 && currentFuel.time > 2) burnTime = Math.round(burnTime * 1.2); // Star with large fuel burns slower

        // Flame Height/Intensity: influenced by all materials (amount of fuel vapor) and structure (airflow, how flame is channelled)
        let flameIntensity = Math.round(
            (currentTinder.flame * 5) +
            (currentKindling.flame * 10 * currentStructure.air) +
            (currentFuel.flame * 8 * currentStructure.flame)
        );
         // Trench might suppress flame height but concentrate heat
         if (selectedStructure === 'trench') flameIntensity = Math.round(flameIntensity * 0.7);


        // --- Evaluate Success & Generate Feedback (Rule-based matching to Goal) ---
        let success = false;
        let feedbackMsg = "";
        let fireVisualText = ''; // What emoji/text to show for fire

        // Define thresholds and ideal combinations (simplified)
        const thresholds = {
            fast_heat: { minTemp: 400, maxTime: 20, minFlame: 15 }, // Need high temp, fast
            long_burn: { maxTemp: 300, minTime: 40, maxFlame: 10 }, // Need long time, maybe lower temp
            high_flame: { minTemp: 300, minTime: 15, minFlame: 25 }, // Need high flame
            steady_cook: { minTemp: 350, minTime: 25, minFlame: 18, maxFlame: 22, minStability: 1.2 } // Need steady heat (implied by structure/time), medium flame, stable structure
        };

        const goalThreshold = thresholds[goal];
        const overallScore = (maxTemp / 500) + (burnTime / 50) + (flameIntensity / 30); // Arbitrary score for general success

        // --- Goal-Specific Feedback Logic ---

        if (goal === 'fast_heat') {
            if (selectedStructure === 'teepee' && (kindling === 'medium_branches' || kindling === 'thick_branches') && tinder !== 'large_logs') {
                 if (maxTemp >= goalThreshold.minTemp && burnTime <= goalThreshold.maxTime) {
                     success = true;
                     feedbackMsg = `מצוין! מבנה הפירמידה בשילוב חומרי בערה מתאימים יצר חום מקסימלי במהירות - מושלם להרתחת מים או חימום זריז.`;
                     fireVisualText = '🔥🚀🔥'; // Rocket fire
                 } else if (maxTemp >= goalThreshold.minTemp) {
                      feedbackMsg = `השגת חום מהיר במבנה פירמידה, אך זמן הבעירה אולי ארוך מדי למטרה ספציפית זו. ודא שחומרי הבערה קטנים מספיק. הטמפ' הגיעה ל-${maxTemp}°C.`;
                      fireVisualText = '🔥⬆️🔥';
                 } else {
                      feedbackMsg = `מבנה הפירמידה מתאים לחום מהיר, אך הטמפרטורה המקסימלית (${maxTemp}°C) לא מספיק גבוהה. שקול להשתמש בחומרי תבערה שיבערו חזק יותר בהתחלה.`;
                      fireVisualText = '🔥';
                 }
            } else {
                 feedbackMsg = `לחימום מהיר, מבנה פירמידה (Teepee) הוא לרוב האפקטיבי ביותר בשל זרימת האוויר המעולה שלו. השילוב שבחרת הגיע לטמפ' ${maxTemp}°C בזמן ${burnTime} דקות.`;
                 fireVisualText = '🔥';
            }
        } else if (goal === 'long_burn') {
            if (selectedStructure === 'star' && fuel === 'large_logs') {
                if (burnTime >= goalThreshold.minTime) {
                    success = true;
                    feedbackMsg = `מעולה! מבנה הכוכב עם גזעים גדולים מאפשר למדורה לבעור לאורך זמן רב עם מינימום תחזוקה - אידיאלי לחום מתמשך כל הלילה. זמן בעירה משוער: ${burnTime} דקות.`;
                    fireVisualText = '🌟🔥🌟'; // Star fire
                } else {
                     feedbackMsg = `מבנה הכוכב טוב לבעירה ארוכה, אבל גזעים גדולים יותר היו מאפשרים לבעור לזמן ארוך יותר (${burnTime} דקות).`;
                     fireVisualText = '🔥⏳';
                }
            } else {
                 feedbackMsg = `לבעירה הארוכה ביותר עם תחזוקה מינימלית, מבנה כוכב (Star Fire) עם גזעים גדולים הוא לרוב הטוב ביותר. השילוב שבחרת בוער ${burnTime} דקות.`;
                 fireVisualText = '🔥';
            }
        } else if (goal === 'high_flame') {
             if ((selectedStructure === 'teepee' || selectedStructure === 'log_cabin') && flameIntensity >= goalThreshold.minFlame) {
                  success = true;
                  feedbackMsg = `השגת להבה גבוהה ובולטת! מבנה ה${selectedStructure === 'teepee' ? 'פירמידה' : 'כלוב'} עם חומרי בערה שתמכו בלהבה עולה. מושלם לאיתות למרחקים. עוצמת להבה: ${flameIntensity}.`;
                  fireVisualText = '🔥🔥🔥⬆️'; // Flames pointing up
             } else {
                  feedbackMsg = `כדי ליצור להבה גבוהה לאיתות, נסה מבנה שמעודד זרימת אוויר אנכית (כמו פירמידה או כלוב) ושימוש בחומרי תבערה ודלק שמייצרים הרבה גזים בוערים. עוצמת להבה: ${flameIntensity}.`;
                  fireVisualText = '🔥';
             }
        } else if (goal === 'steady_cook') {
            if ((selectedStructure === 'log_cabin' || selectedStructure === 'trench') && currentStructure.stability >= goalThreshold.minStability && maxTemp >= goalThreshold.minTemp * 0.8 && burnTime >= goalThreshold.minTime * 0.8) { // Be slightly more lenient
                 success = true;
                 feedbackMsg = `מצוין לבישול! מבנה ה${selectedStructure === 'log_cabin' ? 'כלוב' : 'טרנץ'''} מספק חום יציב ואחיד ופלטפורמה נוחה לכלי בישול. טמפ' מקס': ${maxTemp}°C, זמן בעירה: ${burnTime} דקות.`;
                 fireVisualText = '🍳🔥🍳'; // Cooking fire
            } else {
                 feedbackMsg = `לבישול יציב, מבנה כלוב (Log Cabin) או טרנץ' (Trench Fire) עדיפים לרוב בשל יציבותם ופיזור החום האחיד יותר. השילוב שבחרת הגיע לטמפ' ${maxTemp}°C ובוער ${burnTime} דקות.`;
                 fireVisualText = '🔥🍽️';
            }
        }

        // --- Default Feedback if not specifically matched or suboptimal ---
        if (!success && feedbackMsg === "") {
             feedbackMsg = `סימולציה הסתיימה. המדורה שבנית הגיעה לטמפרטורה מקסימלית של ${maxTemp}°C, בערה למשך ${burnTime} דקות, והגיעה לעוצמת להבה של ${flameIntensity}. נסה שילובים אחרים ובדוק את התאמתם למטרה שבחרת!`;
             fireVisualText = '🔥'; // Default fire emoji
        }


        // Simple flame height indicator text based on intensity
        let flameText = 'נמוכה';
        if (flameIntensity > 15) flameText = 'בינונית';
        if (flameIntensity > 25) flameText = 'גבוהה';
         if (flameIntensity > 35) flameText = 'עוצמתית';


        // Update results display
        maxTempSpan.textContent = maxTemp;
        burnTimeSpan.textContent = burnTime;
        flameHeightSpan.textContent = `${flameIntensity} (${flameText})`; // Show intensity value + text description
        fireVisualDiv.textContent = fireVisualText;

        // Apply simple animation trigger (via CSS class or direct style)
        fireVisualDiv.style.transform = 'scale(1.1)'; // Pop effect on simulation start
        setTimeout(() => { fireVisualDiv.style.transform = 'scale(1)'; }, 300); // Return to normal size


        // Update feedback
        feedbackTextP.textContent = feedbackMsg;
    };

    // Event listener for simulation button
    startSimulationBtn.addEventListener('click', simulateFire);

    // Initial state: Hide results, show logs, set default feedback
     resultsSection.classList.add('hidden');
     fireVisualDiv.textContent = '🪵🪵🪵';
     feedbackTextP.textContent = "בחר את מבנה המדורה וחומרי הבערה המתאימים למטרתך והדלק את האש!";


    // Event listener for explanation button
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'רוצה להבין את המדע שמאחורי זה? הצג הסבר מפורט';
         // Scroll to explanation when shown
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });
});
</script>
---