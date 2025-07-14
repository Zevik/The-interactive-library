---
title: "הדרך לדיבור: סימולטור האבולוציה של השפה האנושית"
english_slug: the-path-to-speech-human-language-evolution-simulator
category: "מדעי החיים / ביולוגיה"
tags: ["אבולוציה", "דיבור", "שפה", "אדם קדמון", "אנתרופולוגיה", "ביולוגיה"]
---
# הדרך לדיבור: מסע אל עבר הקול האנושי

כיצד הפך הומניד קדום ליצור המסוגל לרקום מילים ורעיונות בקולו? יכולת הדיבור הייחודית שלנו, המאפשרת תקשורת כה עשירה ומורכבת, היא פרי מסע אבולוציוני ארוך ומרתק. אילו שינויים דרמטיים התחוללו בגופנו ובמוחנו במשך מיליוני שנים כדי שנגיע ליכולת המדהימה הזו להפיק, לעבד, ולהבין את צלילי השפה המורכבים ביותר?

<div id="simulator-app">
    <h2>הסימולטור האבולוציוני: צור את הדרך לדיבור</h2>
    <p class="simulator-intro">צא למסע בזמן! התאם את הלחצים האבולוציוניים על האוכלוסייה הקדומה ובדוק כיצד הם משפיעים על התפתחות יכולת הדיבור לאורך מאה דורות.</p>

    <div class="controls">
        <div class="control-group">
            <label for="social-complexity" title="עד כמה הקבוצה מסתמכת על שיתוף פעולה חברתי מורכב? (השפעה על הצורך בתקשורת קולית)">לחץ חברתי ושיתוף פעולה:</label>
            <input type="range" id="social-complexity" min="0" max="100" value="50">
            <span class="range-value" id="social-complexity-value">50</span>
        </div>
        <div class="control-group">
            <label for="hunting-coordination" title="מה מידת הצורך לתאם פעולות קבוצתיות כמו ציד? (השפעה חזקה על הצורך בתקשורת מדויקת)">צורך בתיאום פעולות:</label>
            <input type="range" id="hunting-coordination" min="0" max="100" value="50">
            <span class="range-value" id="hunting-coordination-value">50</span>
        </div>
        <div class="control-group">
            <label for="anatomical-variation" title="מה מידת השונות הגנטית במבנה בית הקול ומערכת הנשימה העליונה? (משפיע על פוטנציאל השיפור הפיזיולוגי ליצירת צלילים)">שונות אנטומית (מערכת קולית):</label>
            <input type="range" id="anatomical-variation" min="0" max="100" value="50">
            <span class="range-value" id="anatomical-variation-value">50</span>
        </div>
        <div class="control-group">
            <label for="hearing-variation" title="מה מידת השונות הגנטית במבנה האוזן ויכולות עיבוד השמע? (משפיע על פוטנציאל השיפור בהבנה ועיבוד שפה)">שונות ביכולות שמיעה:</label>
            <input type="range" id="hearing-variation" min="0" max="100" value="50">
            <span class="range-value" id="hearing-variation-value">50</span>
        </div>
    </div>

    <button id="run-simulation" class="simulation-button">הרץ סימולציה (100 דורות)</button>
     <button id="reset-simulation" class="simulation-button secondary">אפס סימולציה</button>

    <div class="results">
        <h3>תוצאות האבולוציה:</h3>
        <p class="result-item">דור נוכחי: <span id="current-generation">0</span></p>
        <p class="result-item">יכולת דיבור ממוצעת באוכלוסייה:</p>
         <div class="ability-display">
             <span id="average-speech-ability" class="ability-value">0.00</span> / 100
         </div>
        <div class="ability-bar-container">
            <div id="average-ability-bar" class="ability-bar"></div>
        </div>
        <h4>התפתחות לאורך זמן:</h4>
        <ul id="history-list">
            <li class="placeholder-history">הרץ סימולציה כדי לראות את ההיסטוריה...</li>
        </ul>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג / הסתר הסבר מעמיק</button>

<div id="explanation" class="explanation-section">
    <h3>ההסבר המדעי: הצצה אל סודות האבולוציה של הדיבור</h3>

    <div class="explanation-item">
        <h4>מה מייחד את הדיבור האנושי?</h4>
        <p>שלא כמו קריאות אזהרה או חיזור אצל בעלי חיים, הדיבור האנושי מאפשר גמישות ויצירתיות אין-סופית. אנו יכולים ליצור אלפי צלילים מדויקים (פונמות) ולשלב אותם ליצירת מילים חדשות ומשפטים מורכבים להפליא. זה דורש לא רק מנגנון קולי-שמיעתי מפותח, אלא גם מוח בעל יכולות עיבוד והבנה גבוהות של מבנה ומשמעות.</p>
    </div>

     <div class="explanation-item">
        <h4>שינויים פיזיולוגיים: האנטומיה של הקול</h4>
        <p>אחד ההבדלים הבולטים הוא מיקום בית הקול (Larynx) אצל בני אדם. אצל יונקים אחרים, הוא גבוה בגרון, מה שמקל על בליעה ונשימה בו זמנית אך מגביל את מגוון הצלילים. אצלנו, בית הקול ירד, יצר חלל תהודה גדול יותר (Vocal Tract) הכולל את הגרון, הפה והאף. חלל זה, יחד עם לשון שרירית וגמישה, מאפשרים לנו לעצב מגוון עצום של תנועות ועיצורים – אבני הבניין של הדיבור.</p>
    </div>

    <div class="explanation-item">
        <h4>המוח מדבר: אזורי מפתח נוירולוגיים</h4>
        <p>השפה והדיבור מקושרים לרשת מורכבת של אזורים במוח, בעיקר בהמיספרה השמאלית. אזור ברוקה (Broca's Area) חיוני להפקת דיבור ותחביר, בעוד אזור ורניקה (Wernicke's Area) קריטי להבנת שפה. אזורים אלו, המקושרים ביניהם על ידי צרור עצבים (Arcuate Fasciculus), התפתחו והתארגנו מחדש במהלך האבולוציה. במקביל, התפתחו גם יכולות קוגניטיביות כלליות כמו זיכרון עבודה, תכנון, וחשיבה מופשטת, החיוניות לשימוש בשפה.</p>
    </div>

     <div class="explanation-item">
        <h4>למה לדבר? היתרונות האבולוציוניים</h4>
        <p>יכולת תקשורת יעילה העניקה יתרונות הישרדותיים עצומים לאבותינו:</p>
        <ul>
            <li>**תיאום קבוצתי:** ארגון ציד קולקטיבי, התגוננות משותפת, ותכנון מסעות.</li>
            <li>**העברת ידע:** לימוד מהיר ויעיל של מיומנויות חיוניות, סיפורי ניסיון, ומסורות.</li>
            <li>**חיבור חברתי:** בניית קשרים עמוקים, יצירת בריתות, והעברת נורמות חברתיות לחיזוק לכידות הקבוצה.</li>
            <li>**חשיבה מופשטת:** שימוש בסמלים (מילים) לרעיונות מופשטים אפשר תכנון לעתיד, פתרון בעיות מורכבות, ויצירת תרבות.</li>
        </ul>
        יתרונות אלו הפכו את הדיבור לתכונה שנבררה באופן טבעי, והובילו להתפשטותה באוכלוסייה.</p>
    </div>

    <div class="explanation-item">
        <h4>מתי ואיך? ציר הזמן האבולוציוני</h4>
        <p>המעבר לתקשורת דמוית שפה התרחש בהדרגה. בעוד מינים קדומים יותר ייתכן והשתמשו בצלילים מורכבים, הדיבור המודרני כפי שאנו מכירים אותו החל, ככל הנראה, לפני כמה מאות אלפי שנים, אולי עם הופעת ההומו ארקטוס המאוחרים, הניאנדרטלים או ההומו סאפיינס. זה לא היה אירוע פתאומי אלא פסיפס של שינויים אנטומיים, נוירולוגיים, וקוגניטיביים הדדיים.</p>
    </div>

    <div class="explanation-item">
        <h4>עדויות מהעבר הרחוק</h4>
        <p><ul>
            <li>**מאובנים:** בחינת בסיס הגולגולת ומיקום עצם הלשון (Hyoid) יכולים לרמז על מיקום בית הקול. גודל תעלות העצבים המעצבבים את הלשון והסרעפת קשור לשליטה על מערכת הקול.</li>
            <li>**ארכיאולוגיה:** מורכבות כלי עבודה, קיום אמנות, קבורות טקסיות והתנהגויות חברתיות מורכבות מצביעים על התפתחות קוגניטיבית שאולי לוותה או התאפשרה על ידי שפה.</li>
            <li>**גנטיקה:** זיהוי גנים כמו FOXP2, המעורב בהתפתחות שפה, והשוואת גרסאותיו בין מינים שונים, נותנים רמזים מולקולריים לתהליך האבולוציוני.</li>
        </ul>
        כל הראיות הללו, יחד עם מודלים חישוביים וסימולציות, תומכות בהבנה שהדיבור הוא תוצר של תהליך אבולוציוני ארוך ומורכב.</p>
    </div>
</div>

<style>
    /* General Styles */
    #simulator-app, #explanation {
        font-family: 'Arial', sans-serif;
        direction: rtl; /* Ensure Right-to-Left */
        text-align: right; /* Ensure text aligns right */
    }

    body {
        background-color: #eef2f7; /* Light background */
        color: #333;
        line-height: 1.6;
        padding: 20px;
    }

    #simulator-app {
        background: linear-gradient(145deg, #ffffff, #eef2f7); /* Subtle gradient background */
        padding: 25px;
        border-radius: 12px; /* More rounded corners */
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Stronger shadow */
        border: 1px solid #d0d9e6; /* Subtle border */
    }

    #simulator-app h2 {
        text-align: center;
        color: #0a3d62; /* Deep blue heading */
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.8em;
        position: relative; /* For potential decorative elements */
    }

     .simulator-intro {
        text-align: center;
        margin-bottom: 25px;
        color: #555;
        font-size: 1.1em;
    }


    /* Controls Section */
    .controls {
        margin-bottom: 30px;
        border: none; /* Remove border */
        padding: 20px; /* More padding */
        border-radius: 8px;
        background-color: #f8f9fa; /* Light grey background for controls */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08); /* Inner shadow */
    }

    .control-group {
        margin-bottom: 20px; /* More space between groups */
        display: flex; /* Use flexbox for layout */
        align-items: center; /* Vertically center label and input */
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .control-group label {
        display: block; /* Labels are blocks */
        margin-bottom: 8px; /* Space below label */
        font-weight: bold;
        color: #333;
        flex-basis: 180px; /* Fixed width for labels */
        margin-left: 15px; /* Space after label */
        font-size: 1em;
    }

    .control-group input[type="range"] {
        flex-grow: 1; /* Input takes available space */
        height: 8px; /* Thinner slider */
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        background: #ddd; /* Slider track color */
        border-radius: 5px;
        outline: none;
        opacity: 0.7;
        transition: opacity 0.2s ease;
        margin: 0 10px; /* Space around slider */
    }

    .control-group input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px; /* Thumb size */
        height: 20px;
        background: #007bff; /* Blue thumb */
        border: 1px solid #0056b3;
        border-radius: 50%; /* Round thumb */
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

     .control-group input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        border: 1px solid #0056b3;
        border-radius: 50%;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    .control-group input[type="range"]:hover {
        opacity: 1;
    }

     .control-group input[type="range"]::-webkit-slider-thumb:hover {
        background-color: #0056b3;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }

     .control-group input[type="range"]::-moz-range-thumb:hover {
        background-color: #0056b3;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }


    .range-value {
        display: inline-block;
        width: 40px; /* Fixed width for value */
        text-align: center;
        font-weight: normal;
        color: #555;
        font-size: 1em;
    }

    /* Buttons */
    .simulation-button, .toggle-button {
        display: block;
        width: 100%;
        padding: 12px 20px; /* More padding */
        margin-top: 15px; /* Space above buttons */
        background-color: #007bff; /* Primary blue */
        color: white;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        font-size: 1.15em;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
    }

    .simulation-button:hover, .toggle-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
    }

     .simulation-button:active, .toggle-button:active {
        transform: scale(0.98); /* Slight press effect */
        box-shadow: 0 2px 4px rgba(0, 123, 255, 0.4);
    }

     .simulation-button:disabled {
        background-color: #cccccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    .simulation-button.secondary {
        background-color: #6c757d; /* Grey for secondary button */
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
        margin-top: 10px; /* Less space above secondary */
    }

    .simulation-button.secondary:hover {
        background-color: #5a6268;
        box-shadow: 0 6px 12px rgba(108, 117, 125, 0.3);
    }


    /* Results Section */
    .results {
        margin-top: 30px; /* More space above results */
        border: none; /* Remove border */
        padding: 20px;
        border-radius: 8px;
        background-color: #ffffff; /* White background for results */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .results h3, .results h4 {
        color: #0a3d62; /* Deep blue headings */
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 1px solid #eee; /* Separator line */
    }

     .results h4 {
         margin-top: 20px;
     }

    .result-item {
        margin-bottom: 10px;
        font-size: 1.1em;
        color: #333;
    }

    .ability-display {
        font-size: 1.4em;
        font-weight: bold;
        color: #28a745; /* Green color for ability value */
        margin-bottom: 10px;
        text-align: center;
    }

     .ability-value {
        font-variant-numeric: tabular-nums; /* Helps keep numbers aligned as they change */
     }

    .ability-bar-container {
        width: 100%;
        background-color: #e9ecef; /* Light grey bar background */
        border-radius: 5px;
        margin-top: 5px;
        overflow: hidden;
        height: 25px; /* Taller bar */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .ability-bar {
        height: 100%;
        width: 0%;
        background: linear-gradient(90deg, #28a745, #218838); /* Gradient green */
        text-align: center;
        line-height: 25px;
        color: white;
        font-weight: bold;
        border-radius: 5px; /* Inherit border radius */
        transition: width 0.6s ease-out; /* Slower, smoother transition */
        position: relative;
         /* Text inside bar - could add this later if needed */
    }

     /* Optional: add text label inside bar if width is sufficient */
     /*
    .ability-bar::after {
        content: attr(data-ability-text);
        position: absolute;
        right: 5px;
        top: 0;
        color: rgba(255,255,255,0.9);
        font-size: 0.9em;
     }
      */


    #history-list {
        list-style: none;
        padding: 0;
        max-height: 180px; /* Slightly taller history */
        overflow-y: auto;
        border-top: 1px solid #eee;
        margin-top: 15px;
         scrollbar-width: thin; /* Firefox */
         scrollbar-color: #888 #f1f1f1; /* Firefox */
    }

     #history-list::-webkit-scrollbar {
         width: 8px;
     }

     #history-list::-webkit-scrollbar-track {
         background: #f1f1f1;
     }

     #history-list::-webkit-scrollbar-thumb {
         background: #888;
         border-radius: 4px;
     }

     #history-list::-webkit-scrollbar-thumb:hover {
         background: #555;
     }


    #history-list li {
        padding: 8px 0; /* More padding */
        border-bottom: 1px solid #eee;
        font-size: 0.95em;
        color: #555;
        transition: background-color 0.2s ease;
    }

    #history-list li:last-child {
        border-bottom: none;
    }

     #history-list li.placeholder-history {
        text-align: center;
        color: #888;
        font-style: italic;
     }


    /* Explanation Section */
    .toggle-button {
        margin-top: 25px; /* More space above toggle */
        background-color: #17a2b8; /* Info blue/teal */
        box-shadow: 0 4px 8px rgba(23, 162, 184, 0.2);
    }

     .toggle-button:hover {
         background-color: #138496;
         box-shadow: 0 6px 12px rgba(23, 162, 184, 0.3);
     }


    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: none; /* Remove border */
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        opacity: 0; /* Start hidden for transition */
        transition: opacity 0.5s ease-in-out; /* Smooth fade-in */
         transform: translateY(20px); /* Start slightly lower for slide-up */
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; /* Combine transitions */
    }

     #explanation.visible {
         display: block;
         opacity: 1;
         transform: translateY(0);
     }


    #explanation h3 {
        color: #0a3d62; /* Deep blue */
        margin-top: 0;
        margin-bottom: 20px;
        text-align: center;
        font-size: 1.6em;
    }

     .explanation-item {
         margin-bottom: 25px;
         padding-bottom: 15px;
         border-bottom: 1px dashed #eee; /* Dashed separator */
     }

     .explanation-item:last-child {
         border-bottom: none;
         margin-bottom: 0;
         padding-bottom: 0;
     }


    #explanation h4 {
        color: #007bff; /* Primary blue for subheadings */
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.2em;
    }

    #explanation p {
        line-height: 1.7;
        margin-bottom: 15px;
        color: #444;
    }

    #explanation ul {
        margin-bottom: 15px;
        padding-right: 20px; /* Add padding for RTL list */
        list-style: disc inside; /* Use disc for list items */
        color: #444;
    }

     #explanation ul li {
         margin-bottom: 8px;
     }

     /* Responsive adjustments */
     @media (max-width: 600px) {
         .control-group label {
             flex-basis: 100%;
             margin-left: 0;
             margin-bottom: 5px;
             text-align: center;
         }
          .control-group input[type="range"] {
              margin: 0 5px;
          }
          .range-value {
              flex-basis: 100%;
              text-align: center;
              margin-top: 5px;
          }
         .simulation-button, .toggle-button {
             font-size: 1em;
             padding: 10px 15px;
         }
         #simulator-app, #explanation {
             padding: 15px;
         }
         #explanation ul {
            padding-right: 15px;
         }
     }

</style>

<script>
    const socialComplexityInput = document.getElementById('social-complexity');
    const huntingCoordinationInput = document.getElementById('hunting-coordination');
    const anatomicalVariationInput = document.getElementById('anatomical-variation');
    const hearingVariationInput = document.getElementById('hearing-variation');

    const socialComplexityValueSpan = document.getElementById('social-complexity-value');
    const huntingCoordinationValueSpan = document.getElementById('hunting-coordination-value');
    const anatomicalVariationValueSpan = document.getElementById('anatomical-variation-value');
    const hearingVariationValueSpan = document.getElementById('hearing-variation-value');

    const runSimulationButton = document.getElementById('run-simulation');
    const resetSimulationButton = document.getElementById('reset-simulation');
    const currentGenerationSpan = document.getElementById('current-generation');
    const averageSpeechAbilitySpan = document.getElementById('average-speech-ability');
    const averageAbilityBar = document.getElementById('average-ability-bar');
    const historyList = document.getElementById('history-list');

    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // Update span values when sliders move
    socialComplexityInput.addEventListener('input', () => {
        socialComplexityValueSpan.textContent = socialComplexityInput.value;
    });
    huntingCoordinationInput.addEventListener('input', () => {
        huntingCoordinationValueSpan.textContent = huntingCoordinationInput.value;
    });
    anatomicalVariationInput.addEventListener('input', () => {
        anatomicalVariationValueSpan.textContent = anatomicalVariationInput.value;
    });
    hearingVariationInput.addEventListener('input', () => {
        hearingVariationValueSpan.textContent = hearingVariationInput.value;
    });


    // Simulation parameters
    const POPULATION_SIZE = 200;
    const NUM_GENERATIONS = 100;
    const BASE_MUTATION_RATE = 0.03; // Slightly lower base mutation
    const MUTATION_STRENGTH = 8; // Slightly higher potential mutation effect
    const BASE_ABILITY_START = 10; // Starting average ability
    const START_ABILITY_RANGE = 20; // Random range around start

    let population = [];
    let generation = 0;
    let history = [];
    let simulationInterval = null;


    // Initialize population
    function initializePopulation() {
        population = [];
        for (let i = 0; i < POPULATION_SIZE; i++) {
            // Each individual has a 'speechAbility' score between 0 and 100
            population.push({
                speechAbility: Math.random() * START_ABILITY_RANGE + BASE_ABILITY_START // Start with a defined range
            });
        }
        generation = 0;
        history = [];
        updateDisplay();
        historyList.innerHTML = '<li class="placeholder-history">הרץ סימולציה כדי לראות את ההיסטוריה...</li>';
    }

    // Simulate one generation
    function simulateGeneration() {
        generation++;

        const socialComplexity = parseInt(socialComplexityInput.value) / 100; // 0 to 1
        const huntingCoordination = parseInt(huntingCoordinationInput.value) / 100; // 0 to 1
        const anatomicalVariation = parseInt(anatomicalVariationInput.value) / 100; // 0 to 1 (Higher means more potential for improvement)
        const hearingVariation = parseInt(hearingVariationInput.value) / 100; // 0 to 1 (Higher means more potential for improvement)

        // Calculate fitness based on parameters
        // Fitness is influenced by speech ability and the importance of communication (social/hunting)
        // Anatomical/Hearing variation influence the *mutation* strength and potential.
        const fitnessScores = population.map(individual => {
            // Base fitness (e.g., survival chance regardless of speech)
            let fitness = 1.0; // Start with base survival

            // Benefit from speech ability:
            // Ability is capped at 100. Use a curve so higher ability provides diminishing returns initially but becomes very beneficial later.
            const effectiveAbility = Math.min(individual.speechAbility, 100);
            // Sigmoid-like benefit curve: low ability = little benefit, high ability = high benefit
            const abilityBenefitFactor = 1 / (1 + Math.exp(-(effectiveAbility - 50) / 10)); // Adjust center (50) and steepness (10)

            // Communication pressure from social and hunting needs
            const communicationPressure = (socialComplexity * 0.6 + huntingCoordination * 0.4); // Weighted pressure

            // Total benefit from speech ability is pressure * scaled ability benefit
            const communicationBenefit = communicationPressure * abilityBenefitFactor * 3; // Scale the benefit

            fitness += communicationBenefit;

            // Add some randomness to fitness (environmental noise)
            fitness += (Math.random() - 0.5) * 0.3; // Smaller random factor

            // Ensure fitness is never zero or negative (basic survival)
            return Math.max(0.05, fitness);
        });

        // Select individuals for the next generation (proportional selection)
        const totalFitness = fitnessScores.reduce((sum, score) => sum + score, 0);
        const nextGeneration = [];

        for (let i = 0; i < POPULATION_SIZE; i++) {
            let runningTotal = 0;
            let randomIndex = Math.random() * totalFitness;

            // Select a parent based on fitness
            let parentIndex = 0;
            for (let j = 0; j < POPULATION_SIZE; j++) {
                runningTotal += fitnessScores[j];
                if (runningTotal >= randomIndex) {
                    parentIndex = j;
                    break;
                }
            }

            let newAbility = population[parentIndex].speechAbility;

            // Add mutation
            // Mutation strength influenced by BOTH anatomical and hearing variation.
            const effectiveMutationStrength = MUTATION_STRENGTH * ((anatomicalVariation + hearingVariation) / 2 + 0.5); // Add 0.5 so variation=0 still has some mutation potential

            if (Math.random() < BASE_MUTATION_RATE) {
                const mutationAmount = (Math.random() - 0.5) * effectiveMutationStrength;
                newAbility += mutationAmount;
                // Clamp ability between 0 and 100
                newAbility = Math.max(0, Math.min(100, newAbility));
             }

            nextGeneration.push({ speechAbility: newAbility });
        }

        population = nextGeneration;
        updateDisplay();

         if (generation >= NUM_GENERATIONS) {
             clearInterval(simulationInterval);
             runSimulationButton.disabled = false;
             runSimulationButton.textContent = 'הרץ סימולציה שוב';
             resetSimulationButton.disabled = false;
         }
    }

    // Update the display
    function updateDisplay() {
        const totalAbility = population.reduce((sum, individual) => sum + individual.speechAbility, 0);
        const averageAbility = totalAbility / POPULATION_SIZE;

        currentGenerationSpan.textContent = generation;
        averageSpeechAbilitySpan.textContent = averageAbility.toFixed(2);

        // Update the bar width and color based on progress/ability
        averageAbilityBar.style.width = averageAbility + '%';
         // Optional: Change bar color based on level?
         /*
         if (averageAbility > 80) {
             averageAbilityBar.style.background = 'linear-gradient(90deg, #28a745, #1e7e34)'; // Darker green
         } else if (averageAbility > 50) {
             averageAbilityBar.style.background = 'linear-gradient(90deg, #ffc107, #d39e00)'; // Yellow
         } else {
             averageAbilityBar.style.background = 'linear-gradient(90deg, #dc3545, #c82333)'; // Red
         }
          */


        // Add to history (only for certain generations to keep list short and smooth)
        if (generation === 0 || generation % 5 === 0 || generation === NUM_GENERATIONS) {
             history.push({ gen: generation, avg: averageAbility });
             renderHistory();
        }
    }

    // Render history list
    function renderHistory() {
        // Don't clear the whole list, just add the new item
        if (generation === 0) {
            historyList.innerHTML = ''; // Clear on start
        }
         // Remove placeholder if it exists
         const placeholder = historyList.querySelector('.placeholder-history');
         if (placeholder) {
             historyList.removeChild(placeholder);
         }

        const item = history[history.length - 1]; // Get the last added item
        const li = document.createElement('li');
        li.textContent = `דור ${item.gen}: ממוצע ${item.avg.toFixed(2)}`;
        historyList.appendChild(li);

        // Scroll to bottom smoothly
        historyList.scrollTo({
            top: historyList.scrollHeight,
            behavior: 'smooth'
        });
    }

    // Run the simulation for a fixed number of generations
    function runSimulation() {
        if (simulationInterval) { // Clear any existing interval
             clearInterval(simulationInterval);
         }

        runSimulationButton.disabled = true;
        resetSimulationButton.disabled = true;
        runSimulationButton.textContent = 'רץ סימולציה...';

        initializePopulation(); // Start fresh

        let genCount = 0;
        simulationInterval = setInterval(() => {
            simulateGeneration();
            genCount++;
        }, 60); // Slightly faster interval for visual flow
    }

    // Reset simulation
    function resetSimulation() {
         if (simulationInterval) {
             clearInterval(simulationInterval);
         }
         initializePopulation();
         runSimulationButton.disabled = false;
         runSimulationButton.textContent = 'הרץ סימולציה (100 דורות)';
         resetSimulationButton.disabled = false; // Ensure reset button is enabled after reset
         averageAbilityBar.style.width = '0%'; // Reset bar visually
         averageSpeechAbilitySpan.textContent = (BASE_ABILITY_START + START_ABILITY_RANGE/2).toFixed(2); // Show average starting ability
         currentGenerationSpan.textContent = '0';
    }


    // Event listener for the run button
    runSimulationButton.addEventListener('click', runSimulation);

    // Event listener for the reset button
     resetSimulationButton.addEventListener('click', resetSimulation);


    // Event listener for the explanation toggle button
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('visible');
        if (isHidden) {
             explanationDiv.classList.remove('visible');
             // Add display: none after transition ends
             explanationDiv.addEventListener('transitionend', function handler() {
                 explanationDiv.style.display = 'none';
                 explanationDiv.removeEventListener('transitionend', handler);
             });

            toggleExplanationButton.textContent = 'הצג הסבר מעמיק';
        } else {
             explanationDiv.style.display = 'block';
             // Force a reflow to make the transition work
             void explanationDiv.offsetWidth;
             explanationDiv.classList.add('visible');
             toggleExplanationButton.textContent = 'הסתר הסבר מעמיק';
        }
    });


    // Initialize the app display on page load
    initializePopulation();

</script>