---
title: "מי יזכה בטיורינג? סימולטור קבלת החלטות בוועדה"
english_slug: who-will-win-turing-award-committee-decision-simulator
category: "מדעי המחשב"
tags:
  - פרס טיורינג
  - מדעי המחשב
  - קבלת החלטות
  - ועדה
  - הערכת מחקר
---
# מי יזכה בטיורינג? סימולטור קבלת החלטות בוועדה

האם תצליח לנווט בין שיקולים תיאורטיים למעשיים, מקוריות מול השפעה, ולהכריע מי ראוי לפרס היוקרתי ביותר במדעי המחשב? צלול עכשיו לנעלי חבר בוועדת פרס טיורינג והשפע על ההיסטוריה של התחום!

<div id="app-container">
    <div id="intro-screen">
        <h2>מסע אל לב ועדת פרס טיורינג</h2>
        <p>ברוך הבא לוועדת פרס טיורינג היוקרתית. תפקידך קריטי: להעריך מועמדים מובילים על פי קריטריונים מגוונים, להשתתף בדיון סוער, ובסוף - להכריע. החלטותיך יעצבו את התפיסה העולמית לגבי מי הם פורצי הדרך האמיתיים של מדעי המחשב.</p>
        <p>מוכן לאתגר?</p>
        <button id="start-simulation-btn">התחל את הסימולציה</button>
    </div>

    <div id="evaluation-area" class="screen hidden">
        <h2>הערכת המועמדים</h2>
        <p>עבור על רשימת המועמדים והערך כל אחד מהם בכל קריטריון. זכור: אין תשובה אחת נכונה, אבל כל נקודה חשובה!</p>

        <div id="candidates-overview">
             <h3>מועמדים על השולחן:</h3>
             <div class="candidate">
                 <h4>וינט סרף ובוב קאהן</h4>
                 <p>תרומה: אבות האינטרנט - פיתוח פרוטוקולי TCP/IP שאיפשרו את המהפכה הדיגיטלית העולמית.</p>
             </div>
             <div class="candidate">
                 <h4>אלן קיי</h4>
                 <p>תרומה: חזון המחשוב האישי - חלוץ OOP, ממשקי GUI ותפיסת ה"מחשב האישי" (dynabook concept).</p>
             </div>
             <div class="candidate">
                 <h4>לסלי למפורט</h4>
                 <p>תרומה: יסודות המערכות המבוזרות - עבודת מפתח על אלגוריתמים כמו פאקסוס, הכרחי לעולם הענן והמערכות הגדולות.</p>
             </div>
         </div>

        <div id="candidate-evaluations">
            <!-- Evaluation sliders will be populated here by JS -->
        </div>
        <button id="start-discussion-btn">סיימתי להעריך. קדימה לדיון!</button>
    </div>

    <div id="discussion-area" class="screen hidden">
        <h2>דיון בוועדה</h2>
        <p>הקשב היטב לעמדות חברי הוועדה האחרים. הן עשויות להשפיע על ההחלטה הסופית...</p>
        <div id="discussion-text">
            <!-- Dynamic discussion text will appear here -->
        </div>
        <button id="make-decision-btn" class="hidden">הצבעה סופית - מי יזכה?</button>
    </div>

    <div id="result-area" class="screen hidden">
        <h2>החלטת הוועדה</h2>
        <div id="final-result">
            <!-- Final result and explanation will appear here -->
        </div>
        <button id="reset-simulation-btn">התחל סימולציה חדשה</button>
    </div>
</div>

<style>
    /* Basic Reset & Body Styling */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        background-color: #f4f7f6; /* Light background */
        color: #333;
        margin: 0;
        padding: 0;
    }

    #app-container {
        max-width: 850px; /* Slightly wider */
        margin: 30px auto;
        padding: 30px;
        border: 1px solid #e0e0e0;
        border-radius: 12px; /* More rounded */
        background-color: #ffffff; /* White background for content */
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08); /* Softer shadow */
        overflow: hidden; /* Clear floats/margins */
    }

    h1 {
        text-align: center;
        color: #0056b3; /* Primary brand color */
        margin-bottom: 20px;
        font-size: 2em;
    }

    h2 {
        color: #007bff; /* Accent color */
        border-bottom: 2px solid #007bff;
        padding-bottom: 10px;
        margin-bottom: 20px;
        text-align: center;
        font-size: 1.6em;
    }

    h3 {
         color: #495057;
         margin-top: 25px;
         margin-bottom: 15px;
         font-size: 1.3em;
    }

    h4 {
        color: #212529;
        margin-top: 10px;
        margin-bottom: 8px;
        font-size: 1.1em;
    }

    p {
        margin-bottom: 15px;
        color: #555;
    }

    /* Screens and Transitions */
    .screen {
        opacity: 1;
        transition: opacity 0.6s ease-in-out;
    }

    .screen.hidden {
        opacity: 0;
        height: 0; /* Collapse height */
        overflow: hidden;
        padding: 0;
        margin: 0;
        border: none;
        transition: opacity 0.6s ease-in-out, height 0s linear 0.6s, padding 0s linear 0.6s, margin 0s linear 0.6s; /* Delay height/padding transition */
    }

     #intro-screen {
         text-align: center;
         padding: 40px 20px;
     }

    /* Candidate Styles */
    .candidate, .evaluation-candidate {
        border: 1px solid #dee2e6;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 8px;
        background-color: #e9ecef; /* Light grey background */
        transition: transform 0.2s ease-in-out;
    }

    .candidate:hover, .evaluation-candidate:hover {
         transform: translateY(-3px); /* Subtle lift effect */
         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* Evaluation Area Styles */
    #evaluation-area, #discussion-area, #result-area {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #ced4da;
    }

    .evaluation-candidate {
         background-color: #f8f9fa; /* Lighter background for eval */
         margin-bottom: 25px;
         padding: 20px;
    }

    .criterion {
        margin-bottom: 20px;
        padding: 10px 0;
        border-bottom: 1px dashed #e9ecef; /* Subtle separator */
    }
     .criterion:last-child {
         border-bottom: none;
     }

    .criterion label {
        display: block;
        margin-bottom: 8px;
        font-weight: bold;
        color: #343a40;
    }

    .slider-container {
        display: flex;
        align-items: center;
        gap: 15px; /* Space between slider and value */
    }

    .slider-container input[type="range"] {
        flex-grow: 1;
        -webkit-appearance: none; /* Override default look */
        appearance: none;
        height: 8px;
        background: #ced4da; /* Track color */
        outline: none;
        opacity: 0.7;
        transition: opacity .2s ease-in-out;
        border-radius: 4px;
    }

    .slider-container input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #007bff; /* Thumb color */
        cursor: pointer;
        border-radius: 50%; /* Circle thumb */
        transition: background 0.2s ease-in-out, transform 0.2s ease-in-out;
    }

    .slider-container input[type="range"]::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #007bff;
        cursor: pointer;
        border-radius: 50%;
        transition: background 0.2s ease-in-out, transform 0.2s ease-in-out;
    }

    .slider-container input[type="range"]:hover {
        opacity: 1;
    }

     .slider-container input[type="range"]:active::-webkit-slider-thumb,
     .slider-container input[type="range"]:active::-moz-range-thumb {
         background: #0056b3; /* Darker on active */
         transform: scale(1.1); /* Slight enlarge on active */
     }


    .slider-container span {
        min-width: 25px; /* Give value space */
        text-align: center;
        font-weight: bold;
        color: #007bff; /* Match thumb color */
         transition: color 0.2s ease-in-out;
    }
     .slider-container input[type="range"]:active + span {
         color: #0056b3;
     }


    /* Button Styles */
    button {
        display: block; /* Make buttons block for better layout */
        width: fit-content; /* Fit text width */
        margin: 20px auto; /* Center buttons */
        background-color: #28a745; /* Green for primary actions */
        color: white;
        padding: 12px 25px; /* Larger padding */
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease-in-out;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.2); /* Green shadow */
    }

    button:hover {
        background-color: #218838; /* Darker green */
        box-shadow: 0 6px 12px rgba(40, 167, 69, 0.3);
    }

    button:active {
        transform: scale(0.98); /* Slight press effect */
    }

     #start-simulation-btn {
         background-color: #007bff;
         box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
     }
     #start-simulation-btn:hover {
          background-color: #0056b3;
          box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
     }

    #start-discussion-btn {
         background-color: #ffc107; /* Yellowish for transition action */
         color: #212529;
         box-shadow: 0 4px 8px rgba(255, 193, 7, 0.2);
    }
     #start-discussion-btn:hover {
         background-color: #e0a800;
         box-shadow: 0 6px 12px rgba(255, 193, 7, 0.3);
     }


    #make-decision-btn {
         background-color: #dc3545; /* Red for final action */
         box-shadow: 0 4px 8px rgba(220, 53, 69, 0.2);
    }
     #make-decision-btn:hover {
         background-color: #c82333;
          box-shadow: 0 6px 12px rgba(220, 53, 69, 0.3);
     }

    #reset-simulation-btn {
        background-color: #6c757d; /* Grey for reset */
        box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
    }
    #reset-simulation-btn:hover {
         background-color: #5a6268;
          box-shadow: 0 6px 12px rgba(108, 117, 125, 0.3);
    }

    /* Discussion Area Styles */
    #discussion-text {
        border: 2px dashed #b2bec3; /* More prominent dashed border */
        padding: 20px;
        margin-top: 25px;
        background-color: #fdfdfe; /* Very light background */
        font-style: italic;
        color: #555;
        border-radius: 8px;
        min-height: 150px; /* Ensure it has some height */
        overflow: auto; /* Allow scrolling if content is long */
    }

    #discussion-text p {
        margin-bottom: 15px;
        line-height: 1.8;
        animation: fadeInText 1s ease-in-out; /* Animation for discussion text */
    }

     /* Optional: Styling for different speakers if implemented */
     /* #discussion-text p:nth-child(odd) { background-color: #f0f0f0; padding: 5px; border-radius: 4px; } */

    /* Result Area Styles */
    #final-result {
        margin-top: 20px;
        padding: 20px;
        border: 2px solid #28a745; /* Border matching winner button */
        border-radius: 8px;
        background-color: #d4edda; /* Light green background */
        color: #155724; /* Dark green text */
        text-align: center;
         animation: scaleIn 0.6s ease-out; /* Animation for the result */
    }

    #final-result h4 {
        color: #155724; /* Dark green */
        font-size: 1.5em;
        margin-bottom: 15px;
    }

    #final-result p {
        color: #155724; /* Dark green */
        text-align: justify; /* Justify text */
        margin-top: 10px;
    }

     /* Animation Keyframes */
     @keyframes fadeInText {
         from { opacity: 0; }
         to { opacity: 1; }
     }

     @keyframes scaleIn {
         from { transform: scale(0.9); opacity: 0.8; }
         to { transform: scale(1); opacity: 1; }
     }


    /* Explanation Section */
    #toggle-explanation-btn {
         display: block;
         margin: 30px auto;
         background-color: #6c757d;
         color: white;
         padding: 10px 20px;
         border-radius: 5px;
         font-size: 1em;
         box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
         transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
         width: fit-content;
     }
     #toggle-explanation-btn:hover {
         background-color: #5a6268;
         box-shadow: 0 6px 12px rgba(108, 117, 125, 0.3);
     }

    #explanation {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eee;
        transition: opacity 0.6s ease-in-out;
    }

     #explanation.hidden {
         opacity: 0;
         height: 0;
         overflow: hidden;
         padding-top: 0;
         margin-top: 0;
         transition: opacity 0.6s ease-in-out, height 0s linear 0.6s, padding-top 0s linear 0.6s, margin-top 0s linear 0.6s;
     }

     #explanation h2, #explanation h3 {
         color: #333;
         text-align: right; /* Adjust text direction for Hebrew */
         border-bottom-color: #adb5bd; /* Lighter border */
         padding-bottom: 8px;
     }
     #explanation p {
         text-align: justify; /* Justify explanation text */
         color: #444;
     }

    /* Utility Classes */
    .hidden {
        display: none; /* Used by JS for hiding elements instantly before animation */
    }

</style>

<button id="toggle-explanation-btn">הצג/הסתר הסבר מורחב על פרס טיורינג</button>

<div id="explanation" class="hidden">
    <h2>הסבר מורחב: פרס טיורינג ותהליך הבחירה</h2>

    <h3>מהו פרס טיורינג ומעמדו במדעי המחשב</h3>
    <p>פרס טיורינג (A.M. Turing Award), המוענק מדי שנה על ידי איגוד המכונות החישוביות (ACM), נחשב לפרס היוקרתי והחשוב ביותר בתחום מדעי המחשב. הוא קרוי על שם אלן טיורינג, מתמטיקאי וחוקר אנגלי שנחשב לאחד מאבות מדעי המחשב התיאורטיים והבינה המלאכותית. הפרס, המכונה לעתים "פרס נובל של מדעי המחשב", מוענק ליחידים או קבוצות קטנות של חוקרים על תרומה משמעותית, מתמשכת ובעלת השפעה לעולם מדעי המחשב.</p>

    <h3>היסטוריה קצרה של הפרס ומועמדים בולטים בעבר</h3>
    <p>הפרס מוענק מאז 1966. בין הזוכים הבולטים נמנים שמות כמו דונלד קנות' (על תרומותיו לאנליזה של אלגוריתמים ותכנון שפות תכנות), אדסחר דייקסטרה (על פיתוח תוכנה כשכבות, שפות תכנות ובדיקת תוכניות), אלן קיי (על תכנות מונחה עצמים), דניס ריצ'י וקן תומפסון (על מערכת ההפעלה יוניקס ושפת C), ג'ון הנסי ודיוויד פטרסון (על תרומות יסודיות לארכיטקטורות מחשבים RISC), ועוד רבים אחרים שתרומותיהם עיצבו את התחום.</p>

    <h3>מבנה ועדת הפרס ותהליך הבחירה (כפי שידוע לציבור)</h3>
    <p>ועדת הפרס מורכבת מחוקרים מובילים בתחומים שונים של מדעי המחשב. תהליך הבחירה כולל שלב של הגשת מועמדויות, בחינה מעמיקה של התרומות המדעיות, ודיונים פנימיים בוועדה. ההחלטה הסופית מתקבלת לאחר שקלול מורכב של כל ההיבטים הרלוונטיים לתרומת המועמד.</p>

    <h3>קריטריונים אפשריים להערכת מועמדים (פורמליים ולא פורמליים)</h3>
    <p>הקריטריונים העיקריים כוללים לרוב: עומק תיאורטי (עד כמה הרעיונות יסודיים וחדשניים), השפעה מעשית (כיצד התרומה השפיעה על תעשייה, טכנולוגיה או חברה), מקוריות (האם הרעיונות היו פורצי דרך בזמנם), והשפעה ארוכת טווח (האם הרעיונות נותרו רלוונטיים ובסיסיים לאורך שנים). קריטריונים לא פורמליים עשויים לכלול גם הכרה קודמת על ידי הקהילה המדעית (פרסים אחרים), האופן שבו התרומה השתלבה בפיתוח התחום, ולעתים נדירות אולי גם שיקולים הקשורים למצב אישי או ייצוג של תחומי משנה.</p>

    <h3>המורכבות והאתגרים בתהליך קבלת ההחלטות</h3>
    <p>הערכת תרומה מדעית ברמה זו היא מורכבת. קשה לכמת השפעה ארוכת טווח, במיוחד כשהטכנולוגיה מתפתחת במהירות. לעתים קרובות, תרומות משמעותיות הן תוצאה של עבודה משותפת של מספר חוקרים, והוועדה צריכה להחליט האם להעניק את הפרס לקבוצה או לחלק ממנה. ישנן גם דילמות הקשורות לגבולות התחום - האם תרומה ספציפית שייכת למדעי המחשב באופן מובהק? לעתים עשויים להיות שיקולים אסטרטגיים לגבי אילו תחומי מחקר הפרס "ידגיש" בשנה מסוימת.</p>

     <h3>דוגמאות למקרים קשים או החלטות שנויות במחלוקת בהיסטוריה של הפרס</h3>
     <p>בעוד שרוב ההחלטות זוכות להסכמה רחבה, היו מקרים של דיון ציבורי או אקדמי לגבי מי היה צריך לזכות או מדוע אדם מסוים לא זכה בזמן מסוים. לדוגמה, שאלת הענקת הפרס למפתחי קוד פתוח משפיעים או לחוקרים בתחומים חדשים יחסית תמיד עולה לדיון. לעיתים, השפעתה האמיתית של תרומה מתבררת רק שנים רבות לאחר פרסומה הראשוני, מה שמציב אתגר בפני ועדות מוקדמות יותר.</p>

    <h3>הקשר בין הפרס לבין ההתפתחות ההיסטורית של מדעי המחשב</h3>
    <p>זוכי פרס טיורינג הם למעשה רשימה של האנשים שעיצבו באופן המשמעותי ביותר את תחום מדעי המחשב. סקירת רשימת הזוכים לאורך השנים מספקת מבט מרתק על התפתחות התחום - מהיסודות התיאורטיים והאלגוריתמים הראשונים, דרך שפות התכנות ומערכות ההפעלה, ועד לגרפיקה ממוחשבת, בינה מלאכותית, מסדי נתונים ואינטרנט. הפרס לא רק מכיר בהישגי עבר, אלא גם מסייע בעיצוב התפיסה הציבורית והאקדמית לגבי מהם "התחומים החשובים" במדעי המחשב.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const candidates = [
            { id: 'cerf-kahn', name: 'וינט סרף ובוב קאהן', desc: 'אבות האינטרנט - פיתוח פרוטוקולי TCP/IP שאיפשרו את המהפכה הדיגיטלית העולמית.', scores: { theoretical: 3, practical: 5, originality: 4, 'long-term': 5, recognition: 5 } }, // Added base scores for potential weighting/discussion focus
            { id: 'kay', name: 'אלן קיי', desc: 'חזון המחשוב האישי - חלוץ OOP, ממשקי GUI ותפיסת ה"מחשב האישי" (dynabook concept).', scores: { theoretical: 5, practical: 4, originality: 5, 'long-term': 4, recognition: 5 } },
            { id: 'lamport', name: 'לסלי למפורט', desc: 'יסודות המערכות המבוזרות - עבודת מפתח על אלגוריתמים כמו פאקסוס, הכרחי לעולם הענן והמערכות הגדולות.', scores: { theoretical: 5, practical: 4, originality: 4, 'long-term': 4, recognition: 5 } }
        ];

        const criteria = [
            { id: 'theoretical', name: 'עומק תיאורטי' },
            { id: 'practical', name: 'השפעה מעשית' },
            { id: 'originality', name: 'מקוריות וחדשנות' },
            { id: 'long-term', name: 'השפעה ארוכת טווח' },
            { id: 'recognition', name: 'הכרה קודמת/פרסים' } // Added recognition as a factor
        ];

        const introScreen = document.getElementById('intro-screen');
        const startSimulationBtn = document.getElementById('start-simulation-btn');
        const evaluationArea = document.getElementById('evaluation-area');
        const evaluationCandidatesDiv = document.getElementById('candidate-evaluations');
        const startDiscussionBtn = document.getElementById('start-discussion-btn');
        const discussionArea = document.getElementById('discussion-area');
        const discussionTextDiv = document.getElementById('discussion-text');
        const makeDecisionBtn = document.getElementById('make-decision-btn');
        const resultArea = document.getElementById('result-area');
        const finalResultDiv = document.getElementById('final-result');
        const resetSimulationBtn = document.getElementById('reset-simulation-btn');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');

        let userEvaluations = {};

        // --- Flow Control & Screen Management ---
        function showScreen(screenElement) {
            // Hide all screens except the one we want to show
            [introScreen, evaluationArea, discussionArea, resultArea].forEach(screen => {
                if (screen === screenElement) {
                    screen.classList.remove('hidden');
                    // Force reflow to ensure transition plays
                     screen.offsetWidth;
                } else {
                    screen.classList.add('hidden');
                }
            });
        }

        // --- Initialize Simulation ---
        function initializeSimulation() {
            userEvaluations = {}; // Reset evaluations
            evaluationCandidatesDiv.innerHTML = ''; // Clear previous content

            candidates.forEach(candidate => {
                userEvaluations[candidate.id] = {};
                const candidateDiv = document.createElement('div');
                candidateDiv.classList.add('evaluation-candidate');
                candidateDiv.innerHTML = `<h4>${candidate.name}</h4>`;

                criteria.forEach(criterion => {
                    const criterionDiv = document.createElement('div');
                    criterionDiv.classList.add('criterion');
                    criterionDiv.innerHTML = `
                        <label for="${candidate.id}-${criterion.id}">${criterion.name}:</label>
                        <div class="slider-container">
                            <input type="range" id="${candidate.id}-${criterion.id}" name="${candidate.id}-${criterion.id}" min="1" max="5" value="3">
                            <span id="${candidate.id}-${criterion.id}-value">3</span>
                        </div>
                    `;
                    candidateDiv.appendChild(criterionDiv);

                    // Add event listener for slider
                    const slider = criterionDiv.querySelector('input[type="range"]');
                    const valueSpan = criterionDiv.querySelector('span');
                    slider.addEventListener('input', (event) => {
                        valueSpan.textContent = event.target.value;
                         // Store evaluation
                        userEvaluations[candidate.id][criterion.id] = parseInt(event.target.value);
                    });

                    // Initialize userEvaluation with default values
                    userEvaluations[candidate.id][criterion.id] = parseInt(slider.value);
                });
                evaluationCandidatesDiv.appendChild(candidateDiv);
            });

            // Hide elements for next steps
            discussionTextDiv.innerHTML = '';
            finalResultDiv.innerHTML = '';
            makeDecisionBtn.classList.add('hidden');

            // Show intro screen initially
            showScreen(introScreen);
        }

        // --- Start Simulation Button ---
        startSimulationBtn.addEventListener('click', () => {
             showScreen(evaluationArea);
        });


        // --- Start Discussion Logic ---
        startDiscussionBtn.addEventListener('click', async () => {
            showScreen(discussionArea);
            discussionTextDiv.innerHTML = ''; // Clear previous text
             makeDecisionBtn.classList.add('hidden'); // Hide button until discussion is done

            const discussionLines = [
                { speaker: 'יו"ר הוועדה', text: 'תודה לכולם על ההערכות הראשוניות. בואו נתחיל את הדיון. יש לנו מועמדים יוצאים מהכלל השנה.' },
                { speaker: 'חבר א\'', text: 'אני חייב להדגיש את ההשפעה העולמית הבלתי נתפסת של סרף וקאהן. האינטרנט הוא אבן יסוד בעולמנו, והם אדריכליו. ההשפעה המעשית שלהם עצומה!' },
                { speaker: 'חברה ב\'', text: 'נכון, אבל אלן קיי היה עם חזון קונספטואלי עמוק הרבה לפני זמנו. OOP ו-GUI שינו את הדרך שבה אנחנו מתכנתים ומתקשרים עם מחשבים. זו מקוריות תיאורטית ברמה אחרת.' },
                { speaker: 'חבר ג\'', text: 'אנחנו לא יכולים להתעלם מלסלי למפורט. בעולם מבוזר כמו שלנו, העבודה שלו על פאקסוס ומערכות קונסיסטנטיות היא קריטית לתשתיות בקנה מידה גדול. אולי פחות זוהר, אבל יסודי ביותר מבחינה תיאורטית ולטווח ארוך.' },
                { speaker: 'חבר א\'', text: 'האם אנחנו מעניקים פרס על "השפעה" או על "תיאוריה טהורה"? סרף וקאהן לקחו רעיונות קיימים ובנו מהם משהו ששינה את העולם. קיי ולמפורט התמקדו יותר ביסודות תיאורטיים, שהשפעתם המעשית הגיעה מאוחר יותר או עקיפה יותר.' },
                { speaker: 'חברה ב\'', text: 'אבל המקוריות של קיי והעומק של למפורט היו פריצות דרך מדעיות אמיתיות בזמנן. אנחנו אמורים לזהות את ההישגים המדעיים פורצי הדרך, לא רק את היישומים הנפוצים ביותר.' },
                { speaker: 'חבר ג\'', text: 'ומה עם הכרה קודמת? כולם קיבלו פרסים חשובים אחרים, אבל טיורינג הוא שיא הקריירה. האם יש למישהו מהם יתרון מובהק בהקשר זה?' },
                 { speaker: 'יו"ר הוועדה', text: 'דיון מרתק ומורכב, כצפוי. זכרו שוב את הקריטריונים: עומק תיאורטי, השפעה מעשית, מקוריות, השפעה ארוכת טווח, והכרה בקהילה. קחו רגע לשקול הכל שוב בראש. עוד מעט נתבקש להצביע.' },
            ];

            // Simulate typing or progressive reveal
            for (const line of discussionLines) {
                const p = document.createElement('p');
                p.innerHTML = `<strong>${line.speaker}:</strong> `;
                discussionTextDiv.appendChild(p);

                const textSpan = document.createElement('span');
                p.appendChild(textSpan);

                for (let i = 0; i < line.text.length; i++) {
                    textSpan.textContent += line.text.charAt(i);
                    await new Promise(resolve => setTimeout(resolve, 15)); // Typing speed
                }
                 await new Promise(resolve => setTimeout(resolve, 700)); // Pause between lines
            }

            // Show the decision button after discussion ends
            makeDecisionBtn.classList.remove('hidden');
        });

        // --- Make Decision Logic ---
        makeDecisionBtn.addEventListener('click', () => {
            showScreen(resultArea);
            finalResultDiv.innerHTML = ''; // Clear previous result

            const finalScores = {};
            let maxScore = -1;
            let winnerId = null;

            candidates.forEach(candidate => {
                let totalScore = 0;
                // Use user's scores for calculation
                criteria.forEach(criterion => {
                     const score = userEvaluations[candidate.id][criterion.id] || 3; // Use 3 if no interaction
                    totalScore += score;
                });

                // Add a weighted component for committee "bias" or external factors,
                // possibly slightly influenced by high/low user scores on specific criteria.
                // For simplicity, still using a random bias, but could be more complex.
                const bias = Math.random() * 6 - 3; // Wider random range
                finalScores[candidate.id] = totalScore + bias;

                // Log scores for debugging (optional)
                console.log(`${candidate.name}: User Score = ${totalScore}, Bias = ${bias.toFixed(2)}, Final = ${finalScores[candidate.id].toFixed(2)}`);


                if (finalScores[candidate.id] > maxScore) {
                    maxScore = finalScores[candidate.id];
                    winnerId = candidate.id;
                }
            });

            const winner = candidates.find(c => c.id === winnerId);
            let resultText = `<h4>תוצאות ההצבעה הסופית:</h4>`;
            resultText += `<p>לאחר דיון מעמיק ושקלול כל ההערכות, ועדת פרס טיורינג החליטה להעניק את הפרס לשנה זו ל...</p>`;
            resultText += `<h3>${winner.name}!</h3>`; // Make winner name prominent

             resultText += `<p><strong>נימוקי הוועדה:</strong></p>`;

             // Generate slightly more detailed explanation based on winner
             if (winner.id === 'cerf-kahn') {
                 resultText += `<p>הוועדה שקלה בכובד ראש את ההשפעה המעשית העצומה והבלתי ניתנת לערעור של פיתוח פרוטוקולי ה-TCP/IP על בניית רשת האינטרנט, אשר שינתה את העולם מקצה לקצה. למרות דיונים על עומק תיאורטי מול השפעה הנדסית, משקל ההשפעה ארוכת הטווח והמעשית הכריע את הכף לטובתם.</p>`;
             } else if (winner.id === 'kay') {
                 resultText += `<p>הבחירה באלן קיי משקפת את ההכרה במקוריותו פורצת הדרך ובעומק התיאורטי של רעיונותיו על תכנות מונחה-עצמים וממשקי משתמש גרפיים. למרות שהשפעתם המעשית התממשה באופן מלא רק שנים רבות לאחר מכן, הוועדה הדגישה את חזונו העתידי והשפעתו על עיצוב המחשוב האישי כפי שאנו מכירים אותו היום.</p>`;
             } else if (winner.id === 'lamport') {
                 resultText += `<p>לסלי למפורט נבחר בזכות תרומותיו היסודיות והעמוקות לתחום המורכב של מערכות מבוזרות. הוועדה זיהתה את ההשפעה התיאורטית והמעשית הקריטית של אלגוריתמים כמו פאקסוס על תשתיות המחשוב המודרניות בקנה מידה גדול. בחירה זו מדגישה את חשיבות המחקר התיאורטי היסודי כתשתית לטכנולוגיות עתידיות.</p>`;
             }

             resultText += `<p class="note">(<strong>הערה:</strong> סימולציה זו מפשטת תהליך מורכב ביותר הכולל דיונים מעמיקים, מועמדויות רבות, ושקלולים שונים. ההחלטה הסופית כאן היא המחשה ולא שיקוף מדויק של תהליך הבחירה האמיתי, אשר לעתים גם מעניק פרס ליותר מזוכה יחיד או קבוצה).</p>`;


            finalResultDiv.innerHTML = resultText;
        });

        // --- Reset Simulation ---
        resetSimulationBtn.addEventListener('click', () => {
            initializeSimulation(); // This also shows the intro screen
        });

        // --- Toggle Explanation ---
        toggleExplanationBtn.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
             if (explanationDiv.classList.contains('hidden')) {
                 toggleExplanationBtn.textContent = 'הצג/הסתר הסבר מורחב על פרס טיורינג';
                 // Collapse explanation div
                  explanationDiv.style.height = '0px';
                  explanationDiv.style.paddingTop = '0px';
                  explanationDiv.style.marginTop = '0px';

             } else {
                 toggleExplanationBtn.textContent = 'הסתר הסבר מורחב על פרס טיורינג';
                 // Expand explanation div - need to calculate height
                 explanationDiv.style.height = 'auto'; // Temporarily auto to calculate
                 const actualHeight = explanationDiv.scrollHeight; // Get full height
                 explanationDiv.style.height = '0px'; // Reset to 0 for transition
                 explanationDiv.offsetHeight; // Trigger reflow
                 explanationDiv.style.height = actualHeight + 'px'; // Animate to full height
                 explanationDiv.style.paddingTop = '20px'; // Restore padding
                 explanationDiv.style.marginTop = '30px'; // Restore margin

                 // Clear height after transition to allow fluid layout changes later
                  explanationDiv.addEventListener('transitionend', function handler() {
                      explanationDiv.style.height = '';
                      explanationDiv.removeEventListener('transitionend', handler);
                 });
             }
        });


        // Initial setup
        initializeSimulation();
    });
</script>
```