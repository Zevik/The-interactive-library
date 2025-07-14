---
title: "היוריסטיקת הזמינות: המלכודת בזיכרון שמעוותת הערכות"
english_slug: availability-heuristic-memory-bias
category: "פסיכולוגיה"
tags: ["היוריסטיקות", "הטיות קוגניטיביות", "זיכרון", "הערכת הסתברות", "דניאל כהנמן", "עמוס טברסקי"]
---
# היוריסטיקת הזמינות: כשהזיכרון מנהל את התפיסה

דמיינו לרגע: אתם שומעים בחדשות על אירוע נדיר אך מזעזע – למשל, תאונה אווירית. מיד לאחר מכן, האם תרגישו חשש גדול יותר מטיסה, למרות שסטטיסטית טיסות הן בטוחות להפליא? התופעה הזו, שבה קלות השליפה מהזיכרון משפיעה על הערכת הסיכון או השכיחות, היא הליבה של **היוריסטיקת הזמינות**. בואו נצלול לחוויה אינטראקטיבית שתמחיש איך זה עובד.

<div id="app-container">
    <div id="instructions">
        <p>אנחנו עומדים להציג בפניכם סדרת 'אירועים' שונים, בזה אחר זה, בקצב מהיר. המשימה שלכם היא לשים לב לאירועים ולנסות להעריך בסוף - איזה סוג אירוע הופיע בתדירות גבוהה יותר.</p>
        <p class="highlight-text">היו מוכנים, זה קורה מהר!</p>
        <button id="startButton" class="game-button primary-button">התחל את ההדמיה</button>
    </div>
    <div id="simulation" class="hidden">
        <div id="event-display">
            <div id="event-card" class="hidden"></div>
        </div>
        <div id="progress-bar">
             <div id="progress-bar-fill"></div>
        </div>
        <div id="simulation-complete" class="hidden">
            <h3>זהו, סיימנו את הסדרה.</h3>
            <p>עכשיו עצרו וחשבו: איזה סוג אירוע הופיע, לדעתכם, בתדירות גבוהה יותר בסדרה שראיתם זה עתה?</p>
            <button class="answer-button game-button" data-answer="mundane">אירועים 'רגילים' (פחות דרמטיים)</button>
            <button class="answer-button game-button" data-answer="dramatic">אירועים 'דרמטיים' (יותר בולטים)</button>
            <div id="feedback" class="hidden"></div>
        </div>
    </div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

body {
    font-family: 'Rubik', sans-serif;
    line-height: 1.8;
    margin: 0;
    padding: 20px;
    background: linear-gradient(to bottom right, #eef2f7, #e0e8f0);
    color: #333;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    direction: rtl; /* For Hebrew */
    text-align: right; /* For Hebrew */
}

h1 {
    color: #2c3e50;
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.2em;
    font-weight: 700;
    line-height: 1.4;
}

#app-container {
    background-color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    max-width: 650px;
    width: 100%;
    text-align: center;
    margin-bottom: 30px;
    border: 1px solid #dcdcdc;
}

#instructions p {
    font-size: 1.15em;
    margin-bottom: 25px;
    color: #555;
}

.highlight-text {
    color: #e74c3c;
    font-weight: 700;
    font-size: 1.2em;
    animation: scaleIn 0.5s ease-out;
}

.game-button {
    padding: 14px 30px;
    font-size: 1.1em;
    font-weight: 500;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
    margin: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.primary-button {
    background-color: #2ecc71; /* Emerald */
}

.primary-button:hover {
    background-color: #27ae60; /* Nephritis */
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}

.primary-button:active {
    transform: scale(0.97);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.answer-button {
     background-color: #3498db; /* Peter River */
}

.answer-button:hover {
    background-color: #2980b9; /* Belize Hole */
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}
.answer-button:active {
    transform: scale(0.97);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}


#simulation {
    min-height: 250px; /* Reserve more space for card animation */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}

#event-display {
    width: 100%;
    height: 180px; /* Increased height */
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 25px;
    position: relative; /* For absolute positioning of card */
    overflow: hidden; /* Hide overflow during animation */
}

#event-card {
    width: 95%; /* Slightly wider */
    min-height: 120px; /* Increased height */
    background-color: #ecf0f1; /* Clouds */
    border-radius: 10px; /* More rounded */
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4em; /* Larger font */
    font-weight: 700; /* Bolder */
    color: #2c3e50; /* Wet Asphalt */
    padding: 15px;
    box-sizing: border-box;
    position: absolute; /* Allow animation from off-screen */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.8); /* Initial state for animation */
    opacity: 0; /* Initial state for animation */
    transition: all 0.3s ease-out; /* Base transition for entry/exit */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

#event-card.visible {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1); /* End state for entry */
}

#event-card.exiting {
     opacity: 0;
     transform: translate(-50%, -50%) scale(0.8) translateY(-20px); /* Exit animation */
}


#event-card.dramatic {
    border: 4px solid #e74c3c; /* Alizarin */
    color: #c0392b; /* Pomegranate */
    background-color: #fdedec; /* Light red background */
    box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4); /* Red glow shadow */
    animation: dramaticPulse 1s infinite alternate ease-in-out; /* More refined pulse */
}

#event-card.mundane {
    border: 2px solid #bdc3c7; /* Silver */
    color: #34495e; /* Midnight Blue */
    background-color: #f8f9fa; /* Very light grey */
}

@keyframes dramaticPulse {
    from {
        box-shadow: 0 0 8px rgba(231, 76, 60, 0.5);
        transform: translate(-50%, -50%) scale(1);
    }
    to {
        box-shadow: 0 0 25px rgba(231, 76, 60, 0.8);
        transform: translate(-50%, -50%) scale(1.02);
    }
}

@keyframes scaleIn {
    from { transform: scale(0.9); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}


#progress-bar {
    width: 100%;
    height: 10px; /* Thicker progress bar */
    background-color: #dcdcdc; /* Light grey */
    border-radius: 5px;
    overflow: hidden;
    margin-top: 20px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

#progress-bar-fill {
    width: 0%;
    height: 100%;
    background: linear-gradient(to right, #3498db, #2980b9); /* Gradient fill */
    border-radius: 5px;
    transition: width 0.2s linear; /* Smoother transition */
}


#simulation-complete h3 {
    margin-bottom: 20px;
    color: #2c3e50;
    font-size: 1.8em;
}

#feedback {
    margin-top: 25px;
    padding: 20px;
    border-radius: 8px;
    background-color: #eef2f7; /* Light background for feedback */
    color: #34495e;
    font-weight: 500;
    line-height: 1.6;
    opacity: 0;
    transition: opacity 0.6s ease-in-out;
    text-align: right;
    width: 100%; /* Make feedback block wider */
    box-sizing: border-box;
}

#feedback.visible {
    opacity: 1;
}

#feedback strong {
    color: #2c3e50;
    font-weight: 700;
}

.hidden {
    display: none;
}

#show-explanation-button {
    display: block;
    margin: 40px auto 0;
    background-color: #9b59b6; /* Amethyst */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
#show-explanation-button:hover {
    background-color: #8e44ad; /* Wisteria */
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}
#show-explanation-button:active {
    transform: scale(0.97);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}


#explanation {
    background-color: #f8f9fa; /* Light grey */
    padding: 30px;
    border-radius: 12px;
    margin-top: 30px;
    text-align: right;
    line-height: 1.8;
    color: #34495e;
    border: 1px solid #e0e0e0;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    max-width: 650px;
    width: 100%;
    box-sizing: border-box;
}

#explanation h2 {
    color: #2c3e50;
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 2em;
    font-weight: 700;
}

#explanation p {
    margin-bottom: 18px;
}

#explanation strong {
     color: #e74c3c; /* Alizarin */
     font-weight: 700;
}

/* Micro-animations for feedback text */
@keyframes fadeInText {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

#feedback p {
    animation: fadeInText 0.5s ease-out forwards;
    opacity: 0; /* Ensure elements are initially hidden before animation */
}
#feedback p:nth-child(1) { animation-delay: 0.2s; }
#feedback p:nth-child(2) { animation-delay: 0.4s; }
#feedback p:nth-child(3) { animation-delay: 0.6s; }
#feedback p:nth-child(4) { animation-delay: 0.8s; }


</style>

<button id="show-explanation-button" class="hidden game-button">למה זה קרה? גלו את ההסבר הפסיכולוגי</button>

<div id="explanation" class="hidden">
    <h2>היוריסטיקת הזמינות – כשהזיכרון משלה אותנו לחשוב אחרת</h2>
    <p>ההדמיה שהרגע חווית נועדה להמחיש בצורה חיה את <strong>היוריסטיקת הזמינות</strong> (Availability Heuristic). זהו אחד מ"קיצורי הדרך המנטליים" (היוריסטיקות) שבהם המוח שלנו משתמש כדי לקבל החלטות מהירות, מושג מרכזי שפותח על ידי חתני פרס נובל דניאל כהנמן ועמוס טברסקי.</p>
    <p>במקום לבצע חישוב מדויק ומורכב של שכיחות או הסתברות של אירוע כלשהו, אנו נוטים להסתמך על שאלה פשוטה הרבה יותר: <strong>כמה קל לי לשלוף דוגמאות או מידע על האירוע הזה מהזיכרון?</strong></p>
    <p>המלכודת היא שקלות השליפה מהזיכרון אינה תמיד משקפת את השכיחות האמיתית בעולם. אירועים שהם יותר <strong>דרמטיים, בולטים, מסוקרים בתקשורת, או מעוררים רגש עז</strong> – כמו התרסקות מטוס, תקיפת כריש או שריפת בית – קל לנו הרבה יותר להיזכר בהם ולדמיין אותם. לעומת זאת, אירועים שכיחים הרבה יותר אך פחות "סקסיים" או טראומטיים – כמו נפילה במדרגות, שפעת קשה או פציעה מפעילות ספורט – נשכחים בקלות יחסית.</p>
    <p>**התוצאה?** ככל שקל יותר להיזכר בדוגמאות לאירוע מסוים, כך אנו נוטים להעריך אותו בטעות כנפוץ או סביר יותר – <strong>גם אם בפועל הוא נדיר יותר</strong> מהאירועים ה"משעממים" שלא קל לנו להיזכר בהם.</p>
    <p>בהדמיה שראיתם, האירועים ה'דרמטיים' עוצבו להיות בולטים יותר מבחינה ויזואלית (צבע, אנימציה, גודל). גם אם המספר בפועל של האירועים ה'רגילים' בסדרה היה גבוה יותר (כפי שקורה לעתים קרובות גם במציאות), הבולטות של ה'דרמטיים' יכלה לגרום לכם להעריך אותם בטעות כנפוצים יותר, כי הם פשוט היו זמינים יותר לזיכרון ברגע הקריטי של ההערכה.</p>
    <p>היוריסטיקת הזמינות מסבירה מגוון רחב של תופעות בחיי היומיום: מדוע אנשים מפחדים לטוס יותר מאשר לנסוע ברכב (תאונות דרכים שכיחות לאין ערוך יותר אך פחות דרמטיות), מדוע הערכת הסיכון ממחלות נדירות שקיבלו כותרות עשויה להיות מנופחת, ומדוע קל לנו יותר לחשוב על מילים שמתחילות באות 'ר' מאשר מילים שהאות 'ר' היא השלישית בהן (כי קל יותר לשלוף אותן לפי האות הראשונה).</p>
    <p>ההבנה של ההטיה הזו מאפשרת לנו להיות מודעים יותר לדרך שבה הזיכרון שלנו משפיע על הערכותינו ולשאוף להסתמך על נתונים אובייקטיביים ומדויקים יותר, במיוחד כשמדובר בהחלטות חשובות.</p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('startButton');
    const instructions = document.getElementById('instructions');
    const simulation = document.getElementById('simulation');
    const eventCard = document.getElementById('event-card');
    const progressBarFill = document.getElementById('progress-bar-fill');
    const simulationComplete = document.getElementById('simulation-complete');
    const answerButtons = document.querySelectorAll('.answer-button');
    const feedbackDiv = document.getElementById('feedback');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

     // Define the events with potentially more mundane than dramatic
    const events = [
        { type: 'mundane', text: 'נפילה קשה במדרגות' },
        { type: 'dramatic', text: 'התרסקות מטוס קל במרחק' },
        { type: 'mundane', text: 'תאונת דרכים קלה עם פצועים' },
        { type: 'mundane', text: 'פגיעת ראש מנפילת חפץ' },
        { type: 'dramatic', text: 'תקיפת כריש (דיווח חדשותי)' },
        { type: 'mundane', text: 'שבר ביד מפעילות ספורט' },
        { type: 'mundane', text: 'כוויות דרגה 2 במטבח' },
        { type: 'dramatic', text: 'נשיכת נחש ארסי' },
        { type: 'mundane', text: 'אשפוז עקב שפעת קשה' },
        { type: 'mundane', text: 'הרעלת מזון קשה' },
        { type: 'dramatic', text: 'שריפה גדולה בבית' },
        { type: 'mundane', text: 'נקע חמור בקרסול' },
        { type: 'mundane', text: 'פציעה ממכשיר חשמלי' },
        { type: 'dramatic', text: 'פגיעת ברק (נדיר מאוד)' },
        { type: 'mundane', text: 'חתך עמוק המחייב תפרים' },
        { type: 'mundane', text: 'פציעה רצינית ממשחק ילדים' },
        { type: 'dramatic', text: 'רעידת אדמה חזקה (מורגשת בבירור)' },
        { type: 'mundane', text: 'אירוע אלרגיה מסכן חיים' },
        { type: 'mundane', text: 'פציעה מנפילה מגובה נמוך' },
        { type: 'dramatic', text: 'פיגוע ירי (דיווח בתקשורת)' }, // Very high availability via news
        { type: 'mundane', text: 'כוויה קשה מהשמש' },
        { type: 'mundane', text: 'אירוע לב קל (אירוע שכיח)' }
    ];

    // Generate a sequence with a controlled ratio (e.g., 60% mundane, 40% dramatic is a common setup for demonstrating the bias)
    const totalEventsToShow = 18; // Slightly more events for better simulation length
    const targetDramaticRatio = 0.35; // Slightly lower ratio for dramatic events than originally (40%) to strengthen the bias potential

    const numDramatic = Math.round(totalEventsToShow * targetDramaticRatio);
    const numMundane = totalEventsToShow - numDramatic;

    // Ensure we don't request more events than available in the pools
    const dramaticEventsPool = events.filter(e => e.type === 'dramatic');
    const mundaneEventsPool = events.filter(e => e.type === 'mundane');

    const selectedDramatic = dramaticEventsPool.sort(() => 0.5 - Math.random()).slice(0, Math.min(numDramatic, dramaticEventsPool.length));
    const selectedMundane = mundaneEventsPool.sort(() => 0.5 - Math.random()).slice(0, Math.min(numMundane, mundaneEventsPool.length));

    let simulationEvents = selectedDramatic.concat(selectedMundane);

    // Final shuffle of the combined list
    simulationEvents.sort(() => 0.5 - Math.random());

    let currentEventIndex = 0;
    let mundaneCount = selectedMundane.length; // Use counts from selected lists
    let dramaticCount = selectedDramatic.length;


    startButton.addEventListener('click', () => {
        instructions.classList.add('hidden');
        simulation.classList.remove('hidden');
        startSimulation();
    });

    function startSimulation() {
        currentEventIndex = 0;
        simulationComplete.classList.add('hidden');
        feedbackDiv.classList.add('hidden');
        feedbackDiv.innerHTML = ''; // Clear previous feedback
        answerButtons.forEach(button => {
            button.classList.remove('hidden');
            button.disabled = false; // Ensure buttons are enabled for interaction
        });
        progressBarFill.style.width = '0%'; // Reset progress bar
        eventCard.classList.add('hidden'); // Ensure card is hidden initially
        eventCard.classList.remove('visible', 'dramatic', 'mundane', 'exiting'); // Clean up classes
        showNextEvent();
    }

    function showNextEvent() {
        if (currentEventIndex < simulationEvents.length) {
            const event = simulationEvents[currentEventIndex];

            // Set up the card for the next event (but keep it hidden momentarily)
            eventCard.textContent = event.text;
            eventCard.className = ''; // Clear all classes
            eventCard.classList.add(event.type); // Add type class
            eventCard.classList.remove('hidden', 'visible', 'exiting'); // Ensure base state before showing


            // Trigger reflow to restart animation if needed (for pulse)
            void eventCard.offsetWidth;

            // Animate the card in
            eventCard.classList.add('visible');


            // Update progress bar
            const progress = ((currentEventIndex + 1) / simulationEvents.length) * 100;
            progressBarFill.style.width = progress + '%';

            currentEventIndex++;

            // Set timeout for how long the card stays visible
            const displayDuration = event.type === 'dramatic' ? 900 : 700; // Dramatic events stay slightly longer to sink in
             setTimeout(() => {
                 // Animate the card out
                 eventCard.classList.add('exiting');
                 eventCard.classList.remove('visible');

                 // Set timeout for the gap between events
                 setTimeout(showNextEvent, 250); // Short delay between events
            }, displayDuration);
        } else {
            // Simulation finished
             // Ensure final state of progress bar
            progressBarFill.style.width = '100%';
            // Wait a moment after the last event exits before showing complete screen
            setTimeout(() => {
                simulationComplete.classList.remove('hidden');
            }, 500); // Delay matches or slightly exceeds card exit animation
        }
    }


    answerButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const userAnswer = event.target.dataset.answer;

            // Disable buttons after selection
            answerButtons.forEach(btn => {
                btn.disabled = true;
                // Optional: grey out or change style of inactive buttons
                if (btn !== event.target) {
                     btn.style.opacity = '0.6';
                }
            });


            const actualMoreFrequent = mundaneCount > dramaticCount ? 'mundane' : (dramaticCount > mundaneCount ? 'dramatic' : 'equal');

            let feedbackHTML = `<p>סיימת את ההדמיה והערכת שאירועים מסוג <strong>"${userAnswer === 'mundane' ? 'רגילים' : 'דרמטיים'}"</strong> היו שכיחים יותר.</p>`;
            feedbackHTML += `<p>בפועל, בהדמיה זו היו: <strong>${mundaneCount}</strong> אירועים 'רגילים' ו- <strong>${dramaticCount}</strong> אירועים 'דרמטיים'.</p>`;

            if (userAnswer === actualMoreFrequent) {
                 feedbackHTML += `<p>ההערכה שלך <strong>תואמת</strong> את התדירות בפועל בהדמיה זו. מעולה!</p>`;
            } else if (actualMoreFrequent === 'equal') {
                 feedbackHTML += `<p>שים לב: בפועל, התדירות של שני סוגי האירועים בהדמיה זו הייתה <strong>זהה</strong>.</p>`;
            }
             else {
                 feedbackHTML += `<p>שים לב: בפועל, בהדמיה שראית, האירועים ה<strong>${actualMoreFrequent === 'mundane' ? 'רגילים' : 'דרמטיים'}</strong> היו שכיחים יותר.</p>`;
            }
            feedbackHTML += `<p>קרא את ההסבר כדי להבין למה לפעמים התפיסה שונה מהמציאות.</p>`;


            feedbackDiv.innerHTML = feedbackHTML;
            feedbackDiv.classList.remove('hidden');
            feedbackDiv.classList.add('visible');

            // Animate feedback text children
            feedbackDiv.querySelectorAll('p').forEach((p, index) => {
                p.style.animationDelay = `${0.2 + index * 0.2}s`;
                p.style.opacity = '0'; // Reset opacity for animation
            });


            // Hide answer buttons after selection
             setTimeout(() => {
                 answerButtons.forEach(btn => btn.classList.add('hidden'));
                 showExplanationButton.classList.remove('hidden'); // Show button to reveal explanation
                 showExplanationButton.style.animation = 'scaleIn 0.5s ease-out forwards'; // Animate explanation button
             }, 1500); // Wait a bit for feedback to settle

        });
    });

    showExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.remove('hidden');
        explanationDiv.style.animation = 'scaleIn 0.5s ease-out forwards';
        showExplanationButton.classList.add('hidden');
         // Scroll to explanation smoothly
        explanationDiv.scrollIntoView({ behavior: 'smooth' });
    });


});

</script>