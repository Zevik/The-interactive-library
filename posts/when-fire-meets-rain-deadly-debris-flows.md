---
title: "כששריפה פוגשת גשם: זרמי סחף קטלניים"
english_slug: when-fire-meets-rain-deadly-debris-flows
category: "מדעי הסביבה / כדור הארץ"
tags: זרמי סחף, שריפות יער, סכנות טבע, הידרולוגיה, גיאומורפולוגיה
---
# כששריפה פוגשת גשם: זרמי סחף קטלניים

דמיינו עולם ירוק ופורח, שטוף שמש. כעת דמיינו שהעולם הזה נשרף באש. האם הסכנה חלפה עם כיבוי הלהבות? לרוב, רק התחילה. לעיתים קרובות, גשם שקט ותמים לכאורה עלול להפוך ברגע לזרם קטלני של בוץ, אפר וסלעים - אסון טבע שנקרא זרם סחף (Debris Flow). גלו כיצד שריפה משנה את פני השטח והופכת אותם לפגיעים להפליא מול כוח המים, גם שנים אחרי שהאש כבתה.

<div id="app-container">
    <h2>חווית סימולציה: כוח הגשם על מדרון משתנה</h2>
    <div class="controls">
        <label for="terrain-state">מצב המדרון:</label>
        <select id="terrain-state" class="styled-select">
            <option value="vegetated">ירוק, מכוסה צמחייה</option>
            <option value="burned">שרוף, ללא צמחייה</option>
        </select>
        
        <label for="rain-intensity" class="label-margin">עוצמת הגשם:</label>
        <select id="rain-intensity" class="styled-select">
            <option value="light">קלה</option>
            <option value="medium">בינונית</option>
            <option value="heavy">כבדה</option>
        </select>

        <button id="start-simulation" class="styled-button">הפעל הדמיה</button>
    </div>

    <div id="simulation-area">
        <!-- Visual representation of the slope -->
        <div id="slope">
            <div id="rain-animation"></div>
            <div id="flow-animation">
                <span id="flow-label">זרם סחף קטלני!</span>
            </div>
        </div>
    </div>

    <div id="results">
        <h3>תוצאות הסימולציה:</h3>
        <p id="runoff-result"><span>...</span></p>
        <p id="sediment-result"><span>...</span></p>
        <p id="debris-flow-warning">אזהרה: סכנת זרם סחף משמעותית!</p>
    </div>
</div>

<style>
/* גופנים בסיסיים ואפס שוליים/ריפוד */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f7f6;
    color: #333;
}

#app-container {
    border: 1px solid #e0e0e0;
    padding: 25px;
    border-radius: 12px;
    background-color: #ffffff;
    text-align: center;
    max-width: 650px; /* Slightly wider */
    margin: 40px auto 20px auto; /* Centered with more space */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #0056b3; /* Deeper blue */
    margin-bottom: 20px;
    font-size: 1.8em;
}

.controls {
    margin-bottom: 25px;
    display: flex;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
    justify-content: center;
    align-items: center;
    gap: 15px; /* Space between controls */
}

.controls label {
    font-weight: bold;
    color: #555;
}

.label-margin {
    margin-left: 15px; /* Adjusted margin */
}


.styled-select {
    padding: 10px 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
    cursor: pointer;
    transition: border-color 0.3s ease;
}

.styled-select:hover {
    border-color: #007bff;
}

.styled-button {
    padding: 10px 25px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0, 123, 255, 0.3);
}

.styled-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

.styled-button:active {
    transform: scale(0.98); /* Slight press effect */
}

#simulation-area {
    position: relative;
    width: 100%;
    max-width: 600px;
    height: 300px; /* Taller simulation area */
    margin: 0 auto;
    background-color: #e0e0e0; /* Base background */
    border: 1px solid #999;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2); /* Inner shadow for depth */
}

#slope {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    background-image: url('https://via.placeholder.com/600x300/8FBC8F/333333?text=מדרון+פורח+ויציב'); /* Improved placeholder for vegetated */
    transition: background-image 0.6s ease-in-out; /* Smooth transition */
    z-index: 1; /* Ensure slope is below rain/flow effects */
}

#slope.burned {
    background-image: url('https://via.placeholder.com/600x300/A0522D/FFFFFF?text=מדרון+שרוף+וחשוף'); /* Improved placeholder for burned */
}

#rain-animation {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* Don't block clicks */
    z-index: 3; /* Above slope */
}

.rain-drop {
    position: absolute;
    width: 2px;
    height: 15px; /* Slightly longer drops */
    background: rgba(173, 216, 230, 0.6); /* Lighter, semi-transparent blue */
    animation: fall linear infinite;
    filter: blur(0.5px); /* Subtle blur */
    opacity: 0.8;
}

/* Animation Keyframes - adjusted height */
@keyframes fall {
    to {
        transform: translateY(320px); /* Adjusted to fall slightly beyond container height (300px) */
    }
}

#flow-animation {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0; /* Starts hidden */
    height: 60px; /* Thicker flow band */
    background: linear-gradient(to right, rgba(100, 60, 40, 0.4), rgba(100, 60, 40, 0.8)); /* Gradient for depth */
    transition: width 2s ease-out; /* Smoother ease-out transition */
    display: flex; /* Use flex for centering label */
    justify-content: center; /* Center label horizontally */
    align-items: center; /* Center label vertically */
    overflow: hidden;
    z-index: 2; /* Below rain, above slope */
    border-bottom-left-radius: 8px; /* Match container border */
    border-bottom-right-radius: 8px; /* Match container border */
    box-shadow: 0 -5px 10px rgba(100, 60, 40, 0.5); /* Shadow to indicate flow volume */
}

#flow-animation.active {
    transition: width 1s ease-out; /* Faster transition for active flow */
}

#flow-animation.debris {
    background: linear-gradient(to right, rgba(139, 69, 19, 0.6), rgba(139, 69, 19, 0.9)); /* Darker, muddier brown */
    box-shadow: 0 -5px 15px rgba(139, 69, 19, 0.7); /* Stronger shadow */
}


#flow-label {
    color: white;
    font-weight: bold;
    font-size: 1.5em; /* Larger font */
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5); /* Text shadow for readability */
    white-space: nowrap;
    display: none; /* Initially hidden */
}

#results {
    margin-top: 30px;
    text-align: left;
    padding: 0 15px;
    background-color: #eef7ff; /* Light blue background */
    border-radius: 8px;
    padding: 15px;
    border: 1px solid #cce0ff;
}

#results h3 {
    color: #0056b3; /* Match h2 color */
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.4em;
}

#results p {
    margin-bottom: 8px;
    line-height: 1.6;
    color: #333;
    font-size: 1.1em;
}

#results p span {
    font-weight: normal; /* Span content is not bold */
    color: #000;
}

#debris-flow-warning {
    color: #dc3545; /* Red warning */
    font-weight: bold;
    font-size: 1.3em; /* Larger warning text */
    margin-top: 15px;
    display: none;
    animation: pulse 1.5s infinite; /* Add a pulsing effect */
}

@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.7; }
    100% { opacity: 1; }
}


#toggle-explanation {
    margin-top: 30px;
    padding: 12px 25px;
    background-color: #6c757d; /* Grey button */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s ease;
}

#toggle-explanation:hover {
    background-color: #5a6268; /* Darker grey */
}


#explanation {
    display: none;
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f8f9fa; /* Light grey background */
    text-align: justify; /* Justify text for readability */
    line-height: 1.7;
    color: #333;
}

#explanation h2 {
    color: #0056b3; /* Match other headers */
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.6em;
}

#explanation h3 {
    color: #007bff; /* Blue subheadings */
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.3em;
}

#explanation p, #explanation ul {
    margin-bottom: 15px;
}

#explanation ul {
    padding-left: 25px; /* Indent list items */
}

#explanation li {
    margin-bottom: 8px;
}

/* Basic responsiveness */
@media (max-width: 700px) {
    .controls {
        flex-direction: column; /* Stack controls vertically */
        align-items: stretch;
    }
    .label-margin {
        margin-left: 0; /* Remove margin */
        margin-top: 10px; /* Add top margin */
    }
    .styled-select, .styled-button {
        width: 100%; /* Full width controls */
        box-sizing: border-box; /* Include padding in width */
    }
    #app-container {
        padding: 15px;
        margin: 20px auto;
    }
    #simulation-area {
        height: 250px; /* Reduce height on smaller screens */
    }
    @keyframes fall {
        to {
            transform: translateY(270px); /* Adjust animation height */
        }
    }
     #flow-animation {
        height: 50px; /* Adjust flow height */
     }
     #flow-label {
        font-size: 1.2em; /* Adjust label size */
     }
      #results h3 {
        font-size: 1.2em;
      }
      #results p, #debris-flow-warning {
        font-size: 1em;
      }
}

</style>

<button id="toggle-explanation">הצג הסבר מורחב</button>

<div id="explanation">
    <h2>הסבר מורחב: כששריפה פוגשת גשם - זרמי סחף קטלניים</h2>

    <h3>הקדמה: הקשר ההרסני בין אש ומים</h3>
    <p>בדרך כלל אנו רואים שריפות יער ושיטפונות כשני איומים נפרדים לחלוטין, אך למעשה קיים ביניהם קשר עמוק והרסני. שריפה אינה רק מכלה עצים וצמחייה; היא מחוללת שינויים דרמטיים ומתמשכים בקרקע עצמה, והופכת אזור שעבר שריפה למקום פגיע ביותר מול כוחם של מי גשם, גם אם הם אינם עזים במיוחד.</p>

    <h3>שריפות יער: השפעה עמוקה מתחת לפני השטח</h3>
    <p>החום העז של שריפת יער חודר עמוק לתוך הקרקע. הוא שורף את החומר האורגני על פני השטח ומשנה את המבנה הכימי והפיזי של שכבות הקרקע העליונות. התוצאה? קרקע פגועה, בלתי יציבה ושונה לחלוטין מזו שהייתה לפני השריפה.</p>

    <h3>שינויים קריטיים בקרקע לאחר שריפה</h3>
    <ul>
        <li><strong>הידרופוביות (דחיית מים):</strong> זהו אולי השינוי המסוכן ביותר. חומרים אורגניים נדיפים מהצמחייה והקרקע מתאיידים בחום ומתעבים מחדש בשכבת קרקע קרה יותר, מתחת לפני השטח. שם הם יוצרים שכבה דקה דמוית ווקס הדוחה מים באופן אגרסיבי. עוצמת הדחייה תלויה בטמפרטורת השריפה, סוג הצמחייה והקרקע. שכבה זו יכולה למנוע כמעט לחלוטין חלחול של מים לתוך הקרקע.</li>
        <li><strong>הרס מבנה הקרקע ושכבת אפר רופפת:</strong> שורשי צמחים וחומר אורגני הם כמו "דבק" שמחזיק את גושי הקרקע יחד. השריפה הורסת את הקשרים הללו. בנוסף, על פני השטח נותרת שכבת אפר עבה או דקה. גם האפר וגם הקרקע המפוררת מתחתיו אינם מקושרים היטב והופכים לחומר זמין ביותר להיסחפות.</li>
    </ul>

    <h3>איך גשם רגיל הופך לאיום קטלני?</h3>
    <p>כשיורד גשם על אזור שרוף, המים אינם יכולים לחלחל בקלות עקב השכבה ההידרופובית ונקבוביות הקרקע שנסתמו באפר. רוב המים נשארים על פני השטח וזורמים במהירות במורד המדרון כ"נגר עילי" (Overland Flow). כמות הנגר הזה יכולה להיות עשרות מונים גדולה יותר מאשר באותו אזור לפני השריפה, גם בגשם בעוצמה בינונית.</p>

    <h3>היווצרות זרמי סחף: מסה דוהרת והרסנית</h3>
    <p>זרמי סחף הם תופעה שונה משיטפון רגיל. בעוד שיטפון הוא בעיקר זרם של מים, זרם סחף הוא תערובת סמיכה, כבדה והרסנית של מים, אפר, בוץ, סלעים, שברי עצים וכל מה שנקרה בדרכה. יותר מ-50% ממסת הזרם היא חומר מוצק!</p>
    <p>הנגר העילי המוגבר על מדרון שרוף אוסף בקלות את שכבת האפר והקרקע הרופפת. כשהזרם צובר מהירות וכוח, במיוחד בערוצים או על מדרונות תלולים, הוא גורף עמו כמויות הולכות וגדלות של חומר. המסה הצמיגה הזו דוהר במורד במהירות עצומה, לעיתים קרובות ללא התרעה מוקדמת, וביכולתה לגרום לנזק קטסטרופלי למבנים, תשתיות ולסכן חיי אדם באופן מיידי. הסכנה אינה חולפת במהירות; זרמי סחף יכולים להתרחש חודשים ואף שנים לאחר השריפה, עד שהצמחייה מתאוששת ומבנה הקרקע נבנה מחדש באופן טבעי או באמצעות פעולות שיקום.</p>

    <h3>התמודדות עם הסכנה</h3>
    <p>אזורי סיכון עיקריים הם מדרונות תלולים, בסיסי הרים ואזורים הסמוכים לערוצי נחל המנקזים שטחים שרופים. רשויות מנטרות אזורים אלו ומשתמשות במודלים לחיזוי סכנות סחף על בסיס תחזיות גשם. במקרה של התראה על גשם משמעותי באזור שרוף, ייתכנו הוראות פינוי או התרעה מיוחדת. בטווח הארוך, שיקום הצמחייה וטיפולים הנדסיים לקרקע הם המפתח להפחתת הסיכון.</p>
</div>

<script>
const terrainSelect = document.getElementById('terrain-state');
const rainSelect = document.getElementById('rain-intensity');
const startButton = document.getElementById('start-simulation');
const slopeDiv = document.getElementById('slope');
const rainAnimationDiv = document.getElementById('rain-animation');
const flowAnimationDiv = document.getElementById('flow-animation');
const flowLabelSpan = document.getElementById('flow-label');
const runoffResultSpan = document.querySelector('#runoff-result span');
const sedimentResultSpan = document.querySelector('#sediment-result span');
const debrisFlowWarning = document.getElementById('debris-flow-warning');
const explanationDiv = document.getElementById('explanation');
const toggleExplanationButton = document.getElementById('toggle-explanation');

// Event Listeners
startButton.addEventListener('click', runSimulation);
toggleExplanationButton.addEventListener('click', toggleExplanation);

// Function to run the simulation
function runSimulation() {
    const terrain = terrainSelect.value;
    const intensity = rainSelect.value;

    // Disable button during simulation
    startButton.disabled = true;
    startButton.textContent = 'מבצע סימולציה...';
    startButton.style.backgroundColor = '#cccccc';

    // Reset previous simulation
    rainAnimationDiv.innerHTML = ''; // Clear previous rain drops
    flowAnimationDiv.style.width = '0'; // Reset flow width
    flowAnimationDiv.classList.remove('active', 'debris'); // Remove flow states
    flowAnimationDiv.style.transitionDuration = '2s'; // Reset transition duration
    flowAnimationDiv.style.display = 'flex'; // Ensure flex display is active for label positioning even when width is 0
    flowLabelSpan.style.display = 'none'; // Hide label
    debrisFlowWarning.style.display = 'none'; // Hide warning
    slopeDiv.classList.remove('burned'); // Reset slope look

    // Update slope appearance based on terrain state
    if (terrain === 'burned') {
        slopeDiv.classList.add('burned');
    }

    // Simulate rain animation
    let numDrops = 0;
    let dropDuration = '4s'; // Base duration for light rain
    let rainAnimationDuration = 3000; // How long rain animation runs (ms)

    switch (intensity) {
        case 'light':
            numDrops = 30; // More drops for better visual
            dropDuration = '4s';
            rainAnimationDuration = 4000;
            break;
        case 'medium':
            numDrops = 80;
            dropDuration = '3s';
            rainAnimationDuration = 3500;
            break;
        case 'heavy':
            numDrops = 150; // Many drops
            dropDuration = '2s'; // Faster drops
            rainAnimationDuration = 3000;
            break;
    }

    // Create and animate rain drops
    for (let i = 0; i < numDrops; i++) {
        const drop = document.createElement('div');
        drop.classList.add('rain-drop');
        // Vary start position slightly above the container
        drop.style.top = `${-20 + Math.random() * 20}px`;
        drop.style.left = `${Math.random() * 100}%`;
        drop.style.animationDuration = dropDuration;
        drop.style.animationDelay = `${Math.random() * (rainAnimationDuration / 1000)}s`; // Stagger drops over simulation time
        drop.style.opacity = 0.6 + Math.random() * 0.4; // Vary opacity
        drop.style.width = `${1 + Math.random() * 2}px`; // Vary width/size
        drop.style.height = `${10 + Math.random() * 10}px`; // Vary height/length

        rainAnimationDiv.appendChild(drop);

         // Remove drop after it falls to avoid infinite accumulation in DOM
         drop.addEventListener('animationiteration', function() {
             drop.remove();
         });
         // Also remove after a set time in case animationiteration doesn't fire reliably
         setTimeout(() => {
             if(drop.parentElement) drop.remove();
         }, rainAnimationDuration + parseFloat(drop.style.animationDelay.replace('s', '')) * 1000 + parseFloat(drop.style.animationDuration.replace('s', '')) * 1000);
    }


    // Simulate runoff and sediment calculation (relative values)
    let runoffPercentage = 0;
    let sedimentPotential = 0; // Relative scale 0-100
    let isDebrisFlow = false;
    let flowSpeed = 2; // seconds for flow animation

    if (terrain === 'vegetated') {
        switch (intensity) {
            case 'light': runoffPercentage = 15; sedimentPotential = 10; flowSpeed = 3; break;
            case 'medium': runoffPercentage = 40; sedimentPotential = 25; flowSpeed = 2.5; break;
            case 'heavy': runoffPercentage = 70; sedimentPotential = 40; flowSpeed = 2; break;
        }
    } else { // burned - much higher runoff and sediment potential
        switch (intensity) {
            case 'light': runoffPercentage = 60; sedimentPotential = 50; flowSpeed = 1.8; break; // Higher even with light rain
            case 'medium': runoffPercentage = 90; sedimentPotential = 80; flowSpeed = 1.2; break;
            case 'heavy':
                runoffPercentage = 100; // Max runoff
                sedimentPotential = 100; // Max sediment potential
                isDebrisFlow = true; // Debris flow on burned + heavy rain
                flowSpeed = 0.8; // Very fast flow
                break;
        }
    }

    // Display results *after* rain simulation finishes or after a slight delay
    setTimeout(() => {
        runoffResultSpan.textContent = `${runoffPercentage}% מהגשם הפך לנגר עילי מהיר`;
        sedimentResultSpan.textContent = `${sedimentPotential}% פוטנציאל סחיפת חומר ואדמה`;

        // Trigger flow animation and warning based on simulation result
        if (isDebrisFlow) {
             debrisFlowWarning.style.display = 'block';
             flowAnimationDiv.classList.add('active', 'debris'); // Add debris class for styling
             flowLabelSpan.style.display = 'inline'; // Show label

             // Use a timeout to trigger the animation after a short delay
             setTimeout(() => {
                 flowAnimationDiv.style.transitionDuration = `${flowSpeed}s`; // Set dynamic speed
                 flowAnimationDiv.style.width = '100%'; // Trigger animation
             }, 200); // Small delay before flow starts
        } else if (runoffPercentage > 50) { // Show some flow for significant runoff too
             flowAnimationDiv.classList.add('active');
             flowAnimationDiv.style.transitionDuration = `${flowSpeed}s`; // Set dynamic speed
             flowAnimationDiv.style.width = `${runoffPercentage}%`; // Width indicates runoff amount
             // Optionally show a less severe message or different visual
             // flowLabelSpan.textContent = 'נגר עילי מוגבר'; // Example
             // flowLabelSpan.style.display = 'inline';
             // flowLabelSpan.style.color = '#333';
        } else {
             // Ensure flow animation is fully reset if no significant event
            flowAnimationDiv.style.width = '0';
            flowAnimationDiv.classList.remove('active', 'debris');
            flowLabelSpan.style.display = 'none';
        }

        // Re-enable button after a delay to allow animation to start/finish visually
         setTimeout(() => {
            startButton.disabled = false;
            startButton.textContent = 'הפעל הדמיה';
            startButton.style.backgroundColor = '#007bff';
        }, Math.max(rainAnimationDuration, flowSpeed * 1000 + 500)); // Wait for rain or flow animation + buffer

    }, rainAnimationDuration); // Delay results until rain finishes
}

// Function to toggle explanation visibility
function toggleExplanation() {
    if (explanationDiv.style.display === 'none' || explanationDiv.style.display === '') {
        explanationDiv.style.display = 'block';
        toggleExplanationButton.textContent = 'הסתר הסבר מורחב';
    } else {
        explanationDiv.style.display = 'none';
        toggleExplanationButton.textContent = 'הצג הסבר מורחב';
    }
}

// Initial state setup
runoffResultSpan.textContent = 'בחר מצב מדרון ועוצמת גשם...';
sedimentResultSpan.textContent = ''; // Clear initial sediment text

// Hide explanation on load
explanationDiv.style.display = 'none';


</script>
```