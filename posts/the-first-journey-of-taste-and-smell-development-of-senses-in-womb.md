---
title: "מסע הטעמים והריחות הראשון: התפתחות החושים בעולם הסודי שברחם"
english_slug: the-first-journey-of-taste-and-smell-development-of-senses-in-womb
category: "ביולוגיה"
tags: [עובר, התפתחות עוברית, חושים, טעם, ריח, הריון]
---
<h1>מסע הטעמים והריחות הראשון: התפתחות החושים בעולם הסודי שברחם</h1>
<p>האם תינוקות מכירים טעמים וריחות עוד לפני שהם פוגשים את העולם שבחוץ? התשובה מפתיעה! מסע התפתחות החושים מתחיל מוקדם מאוד, בתוך העולם המימי והמוגן של הרחם. העובר הקטן לומד לחוש, לשמוע, ואפילו לטעום ולהריח את "התפריט" של אמא ואת הריחות שמסביב.</p>
<p>בואו נגלה יחד איך מערכות הטעם והריח מתפתחות צעד אחר צעד, ומתי העובר הופך לשף קטן שמכיר את המטבח עוד לפני שהוא יוצא מהרחם!</p>

<div class="interactive-app">
    <div class="fetal-head">
        <!-- Representation of the head shape -->
        <div class="mouth-area">
             <div class="taste-buds-layer layer-1" data-stage="early"></div>
             <div class="taste-buds-layer layer-2" data-stage="mid"></div>
             <div class="taste-buds-layer layer-3" data-stage="late"></div>
             <div class="taste-signal-area"></div> <!-- Area for taste signals -->
        </div>
        <div class="nose-area">
            <div class="olfactory-epithelium"></div>
            <div class="olfactory-signal-area"></div> <!-- Area for smell signals -->
        </div>
         <!-- Fluid flow paths - distinct for taste and smell -->
        <div class="fluid-path taste-path">
             <div class="chemical-icon taste mol-1" style="--delay: 0s;"></div>
             <div class="chemical-icon taste mol-2" style="--delay: 2s;"></div>
             <div class="chemical-icon taste mol-3" style="--delay: 4s;"></div>
        </div>
        <div class="fluid-path smell-path">
             <div class="chemical-icon smell mol-4" style="--delay: 1s;"></div>
             <div class="chemical-icon smell mol-5" style="--delay: 3s;"></div>
             <div class="chemical-icon smell mol-6" style="--delay: 5s;"></div>
        </div>
         <div class="development-label"></div> <!-- Label for key milestones -->
    </div>
    <div class="timeline-control">
        <input type="range" id="weekSlider" min="8" max="35" value="8">
        <label for="weekSlider">שבוע הריון: <span id="currentWeek">8</span></label>
        <div class="week-markers">
            <span style="left: 0%;">שבוע 8</span>
            <span style="left: calc((10 - 8)/(35 - 8) * 100%);">שבוע 10</span>
            <span style="left: calc((12 - 8)/(35 - 8) * 100%);">שבוע 12</span>
            <span style="left: calc((20 - 8)/(35 - 8) * 100%);">שבוע 20</span>
             <span style="left: calc((30 - 8)/(35 - 8) * 100%);">שבוע 30+</span>
            <span style="left: 100%; transform: translateX(-100%);">שבוע 35</span>
        </div>
    </div>
</div>

<button id="toggleExplanation">רוצה לדעת יותר? הקלק להסבר המלא</button>

<div id="explanation" style="display: none;">
    <h2>המסע המופלא של הטעם והריח ברחם: צלילה לעומק</h2>
    <p>היכולת שלנו לחוש טעם וריח, שהכרחית להישרדות ולהנאה, מתחילה את דרכה הרבה לפני הלידה. ברחם, העובר אינו שוכן בבועה מבודדת; הוא חווה עולם עשיר בגירויים, כולל כימיקלים הנמסים במי השפיר, המעניקים לו "טעימה" ראשונה של העולם.</p>
    <ul>
        <li>**הניצנים הראשונים (שבוע 8-12):** מסע החושים מתחיל עם הופעת לוחות החישה (sensory placodes) באקטודרם. סביב שבוע 8-12 מתחילות להיווצר פקעיות הטעם – לא רק בלשון הפצפונת, אלא גם בחיך, בלוע ובאזורים נוספים. במקביל, באף העליון מתפתח אפיתל הריח שמכיל את התאים הקולטים ריח. זהו שלב הבנייה של מערכות הקליטה.</li>
        <li>**יצירת הקשרים במוח (שבוע 12-20):** בזמן שמבני הקליטה מתפתחים, נוצרים בהדרגה הקשרים העצביים המחברים אותם למוח המתפתח. סיבים עצביים מתחילים לשלוח אותות מגזע המוח, שם מעובדים הגירויים הראשוניים, אל אזורים בקליפת המוח המוקדשים לטעם וריח. זהו שלב "חיווט" המערכת.</li>
        <li>**התפתחות והתמיינות (שבוע 20-30):** פקעיות הטעם נעשות מורכבות יותר ומספרן גדל משמעותית (לעוברים יש יותר פקעיות טעם מאשר למבוגרים, והן מפוזרות על שטח רחב יותר!). גם אפיתל הריח ממשיך להבשיל. המערכות מתחילות להיות רגישות יותר לגירויים כימיים.</li>
        <li>**פעילות תפקודית ולמידה (שבוע 30 ואילך):** בשליש השלישי להריון, מערכות הטעם והריח כבר פעילות! העובר בולע ושואף מי שפיר באופן קבוע, חוויה החושפת אותו למגוון מולקולות טעם וריח. מולקולות אלו מקורן בתזונת האם, בחילוף החומרים שלה, ואפילו בהפרשות העובר עצמו. כל בליעה ושאיפה היא שיעור פרטי בעולם הטעמים והריחות.</li>
        <li>**השפעה ארוכת טווח:** חשיפה זו ברחם אינה סתמית. היא משפיעה ישירות על העדפותיו של התינוק לאחר הלידה! מחקרים הראו שתינוקות שנחשפו ברחם לטעמים או ריחות מסוימים (למשל, שום, אניס, גזר) דרך מי השפיר, הראו העדפה ברורה לאותם טעמים בריחות בחלב אם או כאשר החלו לאכול מזון מוצק. הרחם הוא למעשה "בית הספר" הראשון לטעמים, המכין את התינוק לסביבתו התזונתית העתידית ומשפיע על הרגלי האכילה שלו בהמשך החיים.</li>
    </ul>
</div>

<style>
    /* Overall page styling */
    body {
         direction: rtl;
         text-align: right;
         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* More modern font */
         line-height: 1.7; /* Increased line height */
         color: #2c3e50; /* Dark blue-gray */
         background-color: #f4f7f6; /* Very light soft background */
         padding: 20px;
    }

    h1, h2 {
        text-align: center;
        color: #1abc9c; /* Teal green - vibrant but calming */
        margin-bottom: 0.7em;
        font-weight: 600; /* Slightly bolder */
    }

    h1 {
        font-size: 2.2em;
        margin-top: 0.5em;
         text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

     h2 {
         font-size: 1.6em;
         margin-top: 1.8em;
         border-bottom: 2px solid #3498db; /* Blue underline */
         padding-bottom: 0.4em;
         color: #34495e; /* Darker shade */
     }

    p {
        text-align: center;
        font-size: 1.1em;
        max-width: 700px;
        margin: 0.5em auto 1.5em auto;
        color: #555;
    }


    /* Interactive Simulation Area */
    .interactive-app {
        width: 100%;
        max-width: 650px; /* Slightly larger max width */
        margin: 30px auto;
        border: 1px solid #bdc3c7; /* Light gray border */
        padding: 30px 20px; /* More padding */
        position: relative; /* Needed for absolute positioning inside */
        background: linear-gradient(to bottom, #ecf0f1, #dde1e3); /* Soft gradient background */
        border-radius: 15px;
        overflow: hidden; /* Hide fluid particles outside area */
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* Stronger shadow */
    }

    .fetal-head {
        width: 85%; /* Slightly larger head representation */
        height: 400px; /* Approximate head size */
        margin: 0 auto 40px auto; /* Center and add space below */
        position: relative;
        background: linear-gradient(to bottom, #ffe0bd, #ffcc99); /* Soft skin tone gradient */
        border: none; /* Remove border */
        border-radius: 50% 50% 50% 50% / 55% 55% 45% 45%; /* More natural head shape */
        overflow: hidden; /* Ensure internal elements stay within head shape */
        box-shadow: inset 0 0 15px rgba(0,0,0,0.1); /* Inner shadow for depth */
    }

    /* Sensory Areas (Mouth & Nose) */
    .mouth-area, .nose-area {
        position: absolute;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 15px; /* Softer corners */
        opacity: 0; /* Initially hidden */
        transition: opacity 0.7s ease-in-out, background-color 0.7s ease-in-out; /* Smoother transitions */
        background-color: rgba(231, 76, 60, 0.1); /* Very subtle transparent background */
        border: none; /* Remove dashed border */
    }

    .mouth-area {
        width: 60%; /* Adjusted size */
        height: 80px; /* Adjusted height */
        bottom: 60px; /* Positioned higher */
        left: 20%;
    }

    .nose-area {
        width: 35%; /* Adjusted size */
        height: 70px; /* Adjusted height */
        top: 140px; /* Positioned lower */
        left: 32.5%; /* Centered */
        background-color: rgba(52, 152, 219, 0.1); /* Subtle blue transparent background */
    }

    /* Visual representation of Taste Buds */
     .taste-buds-layer {
         width: 100%; /* Covers mouth area */
         height: 100%;
         position: absolute;
         top: 0;
         left: 0;
         background-repeat: no-repeat;
         background-size: contain; /* Ensure dots scale with container */
         opacity: 0;
         transition: opacity 0.6s ease-in-out;
         pointer-events: none; /* Don't block clicks */
     }

     .taste-buds-layer.layer-1 { /* Early stage - few dots */
          background-image: radial-gradient(circle at 30% 40%, rgba(192, 57, 43, 0.7) 4px, transparent 4px),
                            radial-gradient(circle at 65% 55%, rgba(192, 57, 43, 0.7) 4px, transparent 4px),
                            radial-gradient(circle at 50% 20%, rgba(192, 57, 43, 0.7) 4px, transparent 4px);
     }
     .taste-buds-layer.layer-2 { /* Mid stage - more dots */
          background-image: radial-gradient(circle at 20% 30%, rgba(192, 57, 43, 0.8) 3px, transparent 3px),
                            radial-gradient(circle at 50% 60%, rgba(192, 57, 43, 0.8) 3px, transparent 3px),
                            radial-gradient(circle at 80% 40%, rgba(192, 57, 43, 0.8) 3px, transparent 3px),
                            radial-gradient(circle at 10% 70%, rgba(192, 57, 43, 0.8) 3px, transparent 3px),
                            radial-gradient(circle at 75% 25%, rgba(192, 57, 43, 0.8) 3px, transparent 3px),
                            radial-gradient(circle at 35% 85%, rgba(192, 57, 43, 0.8) 3px, transparent 3px);
         background-size: cover; /* Distribute dots more evenly */
     }
      .taste-buds-layer.layer-3 { /* Late stage - denser dots */
          background-image: radial-gradient(circle at 5% 10%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 25% 40%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 55% 20%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 85% 60%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 40% 80%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 70% 10%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 15% 75%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 80% 25%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 50% 50%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 30% 15%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 90% 90%, rgba(192, 57, 43, 0.9) 3px, transparent 3px),
                            radial-gradient(circle at 10% 50%, rgba(192, 57, 43, 0.9) 3px, transparent 3px);
         background-size: cover;
     }


    /* Visual representation of Olfactory Epithelium */
    .olfactory-epithelium {
        width: 90%; /* Wider area */
        height: 70%; /* Taller area */
        background-color: rgba(52, 152, 219, 0.5); /* More visible blue */
        border-radius: 8px; /* Softer corners */
        opacity: 0;
        transition: opacity 0.6s ease-in-out;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1); /* Inner shadow */
    }

     /* Signal representation (flashing area) */
     .taste-signal-area, .olfactory-signal-area {
         position: absolute;
         width: 100%;
         height: 100%;
         top: 0;
         left: 0;
         border-radius: 15px;
         pointer-events: none; /* Don't block clicks */
         background-color: rgba(255, 255, 0, 0.5); /* Yellowish flash */
         opacity: 0; /* Initially hidden */
     }

    /* Fluid flow paths */
    .fluid-path {
        position: absolute;
        width: 10%; /* Width of the flow channel */
        pointer-events: none; /* Don't interfere with clicks */
        overflow: hidden; /* Keep particles within path */
    }

    .fluid-path.taste-path {
        top: 0; /* Starts from top of head */
        left: 40%; /* Positioned towards mouth area */
        height: 100%; /* Flows down through head */
    }

     .fluid-path.smell-path {
         top: 0; /* Starts from top of head */
         left: 55%; /* Positioned towards nose area */
         height: 100%; /* Flows down through head */
     }


    /* Chemical particle icons */
    .chemical-icon {
         width: 12px; /* Slightly smaller */
         height: 12px;
         position: absolute;
         border-radius: 50%;
         opacity: 0; /* Initially hidden */
         filter: drop-shadow(0 0 3px rgba(0,0,0,0.3)); /* Small shadow */
         animation-play-state: paused; /* Start paused */
         transform: translateY(-20px); /* Start slightly above area */
    }
    .chemical-icon.taste {
         background-color: #2ecc71; /* Green for taste */
         animation: fluidFlowTaste 8s infinite linear; /* Adjusted duration */
         left: 50%; /* Center in its path */
         transform: translateX(-50%); /* Center horizontally */
    }
    .chemical-icon.smell {
         background-color: #f1c40f; /* Yellow for smell */
         animation: fluidFlowSmell 8s infinite linear; /* Same duration */
         left: 50%; /* Center in its path */
         transform: translateX(-50%); /* Center horizontally */
    }

    /* Animation for taste particles (downwards) */
    @keyframes fluidFlowTaste {
        0% { transform: translate(-50%, -20px); opacity: 0; }
        5% { opacity: 1; }
        95% { opacity: 1; }
        100% { transform: translate(-50%, 420px); opacity: 0; } /* Move down past head */
    }

    /* Animation for smell particles (downwards) */
    @keyframes fluidFlowSmell {
         0% { transform: translate(-50%, -20px); opacity: 0; }
         5% { opacity: 1; }
         95% { opacity: 1; }
         100% { transform: translate(-50%, 420px); opacity: 0; } /* Move down past head */
     }

     /* Specific timing within the animation cycle for activation */
     @keyframes tasteActivation {
         0%, 100% { opacity: 0; }
         10%, 90% { opacity: 0.5; }
     }
      @keyframes smellActivation {
          0%, 100% { opacity: 0; }
          10%, 90% { opacity: 0.5; }
      }


    /* Timeline Control */
    .timeline-control {
        text-align: center;
        margin-top: 30px;
        padding: 0 10px;
        position: relative; /* Needed for week markers */
    }

    #weekSlider {
        width: 100%; /* Full width */
        margin-bottom: 15px;
        cursor: grab;
        -webkit-appearance: none; /* Remove default styling */
        appearance: none;
        height: 8px; /* Thicker slider */
        background: #bdc3c7; /* Light gray track */
        outline: none;
        opacity: 0.8;
        -webkit-transition: .2s;
        transition: opacity .2s;
        border-radius: 4px;
    }
    #weekSlider:hover {
        opacity: 1;
    }
     #weekSlider::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px; /* Round thumb */
         height: 20px;
         background: #1abc9c; /* Teal thumb color */
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }
      #weekSlider::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: #1abc9c;
         cursor: pointer;
         border-radius: 50%;
         border: 2px solid #fff;
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      }
      #weekSlider:active {
        cursor: grabbing;
     }


    .timeline-control label {
        font-size: 1.2em;
        color: #34495e;
        font-weight: 600;
        margin-bottom: 10px;
        display: inline-block; /* Allow centering */
    }
     .timeline-control #currentWeek {
         color: #e74c3c; /* Red for week number */
         font-weight: bold;
     }

     .week-markers {
         position: absolute;
         width: 100%;
         left: 0;
         bottom: -10px; /* Position below slider */
         display: flex;
         justify-content: space-between; /* Distribute markers */
         font-size: 0.9em;
         color: #7f8c8d; /* Gray */
         pointer-events: none; /* Don't interfere */
         padding: 0 5px; /* Add padding to align with slider ends */
         box-sizing: border-box;
     }

    .week-markers span {
        position: absolute; /* Absolute positioning within the container */
         transform: translateX(-50%); /* Center the text horizontally */
         bottom: 0;
    }
     .week-markers span:first-child { transform: translateX(0); } /* Align first left */
     .week-markers span:last-child { transform: translateX(-100%); } /* Align last right */


     /* Key milestone label */
    .development-label {
        position: absolute;
        top: 20px; /* Position above the head */
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(44, 62, 80, 0.85); /* Dark background */
        color: white;
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 1em;
        font-weight: 600;
        white-space: nowrap; /* Prevent wrapping */
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        z-index: 10; /* Above other elements */
        text-align: center;
    }


    /* Explanation Button */
    button#toggleExplanation {
        display: block;
        margin: 30px auto; /* More space */
        padding: 14px 25px; /* Larger button */
        font-size: 1.15em;
        cursor: pointer;
        background-color: #3498db; /* Blue */
        color: white;
        border: none;
        border-radius: 8px; /* Softer corners */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
     button#toggleExplanation:hover {
         background-color: #2980b9; /* Darker blue */
         box-shadow: 0 5px 8px rgba(0,0,0,0.2);
     }
     button#toggleExplanation:active {
         transform: translateY(1px); /* Press down effect */
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }

    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 25px; /* More padding */
        border: none; /* Remove border */
        background-color: #ecf0f1; /* Light background */
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08); /* Softer shadow */
        transition: all 0.5s ease-in-out; /* Smooth appearance/disappearance */
    }

    #explanation h2 {
        color: #2c3e50; /* Dark blue-gray */
        margin-top: 0;
        margin-bottom: 0.8em;
        border-bottom: 2px solid #3498db; /* Blue underline */
        padding-bottom: 0.5em;
        text-align: right; /* Align header right */
        font-weight: 600;
    }

    #explanation p {
        text-align: right; /* Align text right */
        margin: 0 0 1em 0;
        font-size: 1em;
        color: #444;
    }

    #explanation ul {
        list-style: none; /* Remove default bullets */
        padding-right: 0; /* Adjust for RTL */
    }

     #explanation li {
        margin-bottom: 1.2em; /* More space between items */
        line-height: 1.8; /* More space within lines */
        padding-right: 25px; /* Space for custom bullet */
        position: relative; /* For custom bullet */
        color: #333;
     }

    #explanation li::before {
        content: '•'; /* Custom bullet point */
        position: absolute;
        right: 0;
        top: 0;
        color: #1abc9c; /* Teal bullet color */
        font-size: 1.2em;
        font-weight: bold;
        width: 20px; /* Area for bullet */
        text-align: center;
    }

     #explanation li strong {
         color: #2c3e50; /* Darker bold text */
     }

     /* Animation for signal flash */
     @keyframes signalFlash {
         0% { opacity: 0; }
         50% { opacity: 1; }
         100% { opacity: 0; }
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const weekSlider = document.getElementById('weekSlider');
        const currentWeekSpan = document.getElementById('currentWeek');
        const tasteBudsLayers = document.querySelectorAll('.taste-buds-layer');
        const olfactoryEpithelium = document.querySelector('.olfactory-epithelium');
        const mouthArea = document.querySelector('.mouth-area');
        const noseArea = document.querySelector('.nose-area');
        const tasteChemicalIcons = document.querySelectorAll('.chemical-icon.taste');
        const smellChemicalIcons = document.querySelectorAll('.chemical-icon.smell');
        const tasteSignalArea = document.querySelector('.taste-signal-area');
        const olfactorySignalArea = document.querySelector('.olfactory-signal-area');
        const developmentLabel = document.querySelector('.development-label');
        const toggleButton = document.getElementById('toggleExplanation');
        const explanationDiv = document.getElementById('explanation');

        const milestones = {
            8: "שבוע 8: ניצני טעם ראשונים מתחילים להיווצר",
            10: "שבוע 10: אפיתל הריח מתחיל להתפתח",
            12: "שבוע 12: התפתחות פקעיות טעם ממשיכה",
            20: "שבוע 20: פקעיות טעם מתמיינות, קשרים במוח מתחזקים",
            30: "שבוע 30+: מערכות הטעם והריח פעילות, העובר טועם ומריח!"
        };

        function showMilestone(week) {
             developmentLabel.style.opacity = 0; // Hide previous label
             developmentLabel.style.transform = 'translateX(-50%) translateY(-10px)'; // Move slightly up

             setTimeout(() => { // Allow time for transition out
                if (milestones[week]) {
                    developmentLabel.textContent = milestones[week];
                    developmentLabel.style.opacity = 1;
                    developmentLabel.style.transform = 'translateX(-50%) translateY(0)'; // Slide in
                     // Hide after a few seconds
                    developmentLabel.dataset.timer = setTimeout(() => {
                         developmentLabel.style.opacity = 0;
                         developmentLabel.style.transform = 'translateX(-50%) translateY(-10px)';
                    }, 4000); // Show for 4 seconds
                } else {
                    // Clear any active timer if no milestone at this week
                    if (developmentLabel.dataset.timer) {
                        clearTimeout(developmentLabel.dataset.timer);
                         developmentLabel.dataset.timer = null;
                    }
                }
             }, 500); // Wait for transition out before showing new one
        }

        function updateSimulation(week) {
            currentWeekSpan.textContent = week;

            // Clear any active label timer
            if (developmentLabel.dataset.timer) {
                 clearTimeout(developmentLabel.dataset.timer);
                 developmentLabel.dataset.timer = null;
            }


            // --- Update Visual Elements based on Week ---

            // Sensory Areas Visibility
            mouthArea.style.opacity = week >= 8 ? 1 : 0;
            noseArea.style.opacity = week >= 10 ? 1 : 0;

            // Taste Buds Development Stages
            tasteBudsLayers.forEach(layer => layer.style.opacity = 0); // Hide all first
            if (week >= 8 && week < 12) {
                document.querySelector('.taste-buds-layer[data-stage="early"]').style.opacity = 1;
            } else if (week >= 12 && week < 20) {
                 document.querySelector('.taste-buds-layer[data-stage="mid"]').style.opacity = 1;
            } else if (week >= 20) { // Late stage implies most development/coverage
                 document.querySelector('.taste-buds-layer[data-stage="late"]').style.opacity = 1;
            }

            // Olfactory Epithelium
            olfactoryEpithelium.style.opacity = week >= 10 ? 1 : 0;


            // Chemical Particles Flow and Activation
            const isFunctional = week >= 30;

             // Control particle animation state
            [...tasteChemicalIcons, ...smellChemicalIcons].forEach(icon => {
                icon.style.animationPlayState = isFunctional ? 'running' : 'paused';
                 // If pausing, also reset position to make it less jarring if resumed
                 if (!isFunctional) {
                     icon.style.opacity = 0; // Hide if not functional
                      // Optionally reset position if needed, but animation handles entry/exit
                 } else {
                     // Ensure they are visible when functional and animation is running
                      // Animation keyframes handle opacity fading in/out
                 }
            });

            // Signal flash - Trigger when particles might hit receptors (more noticeable when functional)
             // We can't easily detect collision here, so let's link it to the particles' animation cycle
             // Or simply make the signal areas visible/reactive when the system is functional
             tasteSignalArea.style.opacity = 0; // Hide signals by default
             olfactorySignalArea.style.opacity = 0;

             if(isFunctional) {
                 // Simple approach: Make signal areas slightly visible
                 tasteSignalArea.style.opacity = 0.1;
                 olfactorySignalArea.style.opacity = 0.1;

                 // More advanced: Trigger flash animation periodically, perhaps tied to the particles' cycle
                  // This is complex without tracking individual particles.
                  // Let's simulate a pulse effect on the area when functional.
                  // Remove previous animation first
                  tasteSignalArea.style.animation = 'none';
                  olfactorySignalArea.style.animation = 'none';
                  // Trigger reflow to restart animation
                  void tasteSignalArea.offsetWidth;
                  void olfactorySignalArea.offsetWidth;

                  tasteSignalArea.style.animation = 'signalFlash 3s infinite ease-in-out';
                  olfactorySignalArea.style.animation = 'signalFlash 3.5s infinite ease-in-out'; // Slightly different speed

             } else {
                 // Ensure animations are stopped and areas are hidden
                 tasteSignalArea.style.animation = 'none';
                 olfactorySignalArea.style.animation = 'none';
                 tasteSignalArea.style.opacity = 0;
                 olfactorySignalArea.style.opacity = 0;
             }


            // --- Show Milestones ---
             // Check for milestones at the exact week number on input release
             // Or trigger slightly after the input changes to give visual update time
             // Let's trigger on 'change' event instead of 'input' for stability
        }

        // Initial state
        updateSimulation(weekSlider.value);
         showMilestone(parseInt(weekSlider.value)); // Show initial milestone if applicable


        // Listen for slider input (real-time visual updates)
        weekSlider.addEventListener('input', (event) => {
            updateSimulation(event.target.value);
        });

         // Listen for slider change (when user releases thumb) to trigger milestones
         weekSlider.addEventListener('change', (event) => {
              showMilestone(parseInt(event.target.value));
         });


        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר הסבר מפורט' : 'רוצה לדעת יותר? הקלק להסבר המלא';

            // Optional: Scroll to the explanation when shown
            if (isHidden) {
                explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

         // Make milestones clickable/hoverable hints on slider (optional, adds complexity, stick to label for now)
         // const milestoneElements = document.querySelectorAll('.week-markers span');
         // milestoneElements.forEach(marker => {
         //     marker.addEventListener('mouseover', () => {
         //         const week = parseInt(marker.textContent.replace('שבוע ', ''));
         //         if (milestones[week]) {
         //             developmentLabel.textContent = milestones[week];
         //             developmentLabel.style.opacity = 1;
         //             developmentLabel.style.transform = 'translateX(-50%) translateY(0)';
         //         }
         //     });
         //     marker.addEventListener('mouseout', () => {
         //          developmentLabel.style.opacity = 0;
         //          developmentLabel.style.transform = 'translateX(-50%) translateY(-10px)';
         //     });
         // });


    });
</script>
```