---
title: "הגשרים של קניגסברג: מסע ויזואלי לתורת הגרפים"
english_slug: konigsberg-bridges-visual-introduction-graph-theory
category: "מדעים מדויקים / מתמטיקה"
tags:
  - תורת הגרפים
  - בעיית הגשרים של קניגסברג
  - מסלול אוילר
  - גרפים
  - קומבינטוריקה
---

# הגשרים של קניגסברג: מסע ויזואלי לתורת הגרפים

דמיינו עיר קסומה החצויה על ידי נהר, עם איים ויבשות המחוברות בגשרים עתיקים. במאה ה-18, תושבי העיר קניגסברג נהגו להתווכח על חידה מסתורית: האם אפשר לצאת לטיול בעיר, לחצות כל אחד משבעת הגשרים בדיוק פעם אחת, ולחזור לנקודת ההתחלה (או לכל נקודה אחרת)? נסו בעצמכם!

## המשחק: האם תצליחו לחצות את כל 7 הגשרים?

לחצו על הגשרים כדי לנסות לחצות אותם. כל גשר שתעברו עליו ישנה את צבעו. עקבו אחרי המיקום שלכם על המפה. המטרה: לחצות את כל 7 הגשרים בדיוק פעם אחת!

<div id="konigsberg-app">
    <div id="map-container">
        <!-- Landmasses -->
        <div id="land-N" class="landmass" data-land="N">N (האי הצפוני)</div>
        <div id="land-S" class="landmass" data-land="S">S (היבשה הדרומית)</div>
        <div id="land-W" class="landmass" data-land="W">W (הגדה המערבית)</div>
        <div id="land-E" class="landmass" data-land="E">E (הגדה המזרחית)</div>

        <!-- Bridges -->
        <div id="bridge-b1" class="bridge" data-ends="N,E"></div>
        <div id="bridge-b2" class="bridge" data-ends="N,E"></div>
        <div id="bridge-b3" class="bridge" data-ends="N,W"></div>
        <div id="bridge-b4" class="bridge" data-ends="N,W"></div>
        <div id="bridge-b5" class="bridge" data-ends="N,S"></div>
        <div id="bridge-b6" class="bridge" data-ends="E,S"></div>
        <div id="bridge-b7" class="bridge" data-ends="W,S"></div>

        <div id="current-location-marker" class="location-marker"></div>
    </div>
    <div id="controls">
        <div id="message-area" class="message-area"></div>
        <div id="crossed-count">גשרים שחצית: 0 / 7</div>
        <button id="reset-button" class="control-button">התחל מחדש</button>
    </div>
</div>

<style>
/* הגדרות בסיסיות לקונטיינר */
#konigsberg-app {
    font-family: 'Arial', sans-serif;
    max-width: 700px;
    margin: 30px auto;
    border: 1px solid #d3e0ea; /* Soft blue border */
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff; /* White background */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    overflow: hidden; /* Ensure marker/elements stay within */
}

/* קונטיינר המפה (הנהר) */
#map-container {
    position: relative;
    width: 100%;
    padding-bottom: 65%; /* Aspect ratio 4:3 approx */
    margin-bottom: 30px;
    background: linear-gradient(to bottom, #b3e5fc, #81d4fa); /* Gradient blue for water */
    border: 1px solid #81d4fa;
    border-radius: 8px;
    overflow: hidden;
}

/* יבשות / גדות הנהר (צמתים) */
.landmass {
    position: absolute;
    background-color: #66bb6a; /* Vibrant green */
    border: 2px solid #388e3c; /* Darker green border */
    border-radius: 50%;
    width: 120px; /* Base size */
    height: 120px; /* Base size */
    display: flex;
    flex-direction: column; /* Stack text */
    justify-content: center;
    align-items: center;
    text-align: center;
    font-weight: bold;
    color: #212121; /* Dark grey text */
    font-size: 0.95em;
    cursor: default; /* Not clickable directly */
    z-index: 10;
    box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
    user-select: none;
    padding: 5px;
    box-sizing: border-box; /* Include padding in size */
    transition: transform 0.3s ease-in-out; /* Subtle hover effect */
}
.landmass:hover {
     transform: scale(1.03);
}


/* מיקום ויזואלי (משוער) של היבשות על המפה */
/* אלו נקודות הייחוס עבור הגשרים והמרקר */
#land-N { top: 15%; left: 50%; transform: translate(-50%, -50%); width: 110px; height: 110px;}
#land-S { bottom: 15%; left: 50%; transform: translate(-50%, 50%); width: 160px; height: 160px;} /* Larger */
#land-W { top: 50%; left: 12%; transform: translate(-50%, -50%); }
#land-E { top: 50%; right: 12%; transform: translate(50%, -50%); }


/* הגשרים (קשתות) */
.bridge {
    position: absolute;
    background-color: #795548; /* Brown/wood color */
    height: 10px; /* Thickness */
    transform-origin: 0 0; /* Pivot point for rotation */
    cursor: pointer;
    z-index: 5;
    border-radius: 5px;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease, box-shadow 0.2s ease-in-out;
}

.bridge:hover {
    background-color: #6d4c41; /* Darker brown on hover */
    box-shadow: 2px 2px 6px rgba(0,0,0,0.4);
}

.bridge.crossed {
    background-color: #e53935; /* Red when crossed */
    box-shadow: 1px 1px 4px rgba(229, 57, 53, 0.6); /* Red glow */
}


/* מיקום וסיבוב הגשרים - מותאם ויזואלית לחיבור היבשות */
/* N (top-center), S (bottom-center), W (left-center), E (right-center) */

/* N to E */
#bridge-b1 { width: 290px; transform: rotate(38deg); top: calc(15% + 45px); left: calc(50% + 5px); transform-origin: 0% 50%;}
#bridge-b2 { width: 290px; transform: rotate(38deg); top: calc(15% + 55px); left: calc(50% - 5px); transform-origin: 0% 50%;}

/* N to W */
#bridge-b3 { width: 290px; transform: rotate(-38deg); top: calc(15% + 45px); left: calc(50% - 290px - 5px); transform-origin: 100% 50%;}
#bridge-b4 { width: 290px; transform: rotate(-38deg); top: calc(15% + 55px); left: calc(50% - 290px + 5px); transform-origin: 100% 50%;}

/* N to S */
#bridge-b5 { width: 10px; height: calc(90% - 15% - 110px/2 - 160px/2 - 10px); top: calc(15% + 110px/2); left: calc(50% - 5px); transform: rotate(0deg); transform-origin: 50% 0%;}

/* E to S */
#bridge-b6 { width: 230px; transform: rotate(130deg); top: calc(50% + 40px); left: calc(88% - 230px/2); transform-origin: 50% 0%;}

/* W to S */
#bridge-b7 { width: 230px; transform: rotate(-130deg); top: calc(50% + 40px); left: calc(12% - 230px/2); transform-origin: 50% 0%;}


/* סמן המיקום הנוכחי של המשתמש */
#current-location-marker {
     position: absolute;
     background-color: #ffca28; /* Brighter yellow */
     border: 3px solid #fb8c00; /* Orange border */
     border-radius: 50%;
     width: 40px; /* Smaller, more agile marker */
     height: 40px;
     display: flex;
     justify-content: center;
     align-items: center;
     font-size: 0.75em;
     font-weight: bold;
     color: #333;
     z-index: 20;
     pointer-events: none; /* Don't block clicks on things below */
     transition: top 0.6s ease-in-out, left 0.6s ease-in-out, transform 0.6s ease-in-out; /* Smooth movement */
     text-align: center;
     /* The JS will set top/left based on landmassPositions.
        Transform is needed to center the marker div itself on those coordinates. */
     transform: translate(-50%, -50%);
     box-shadow: 0 0 10px rgba(255, 202, 40, 0.7); /* Glow effect */
}
#current-location-marker::after { /* Add a pulsing effect */
    content: '';
    display: block;
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #ffca28;
    animation: pulse 1.5s infinite;
    z-index: -1; /* Behind the marker */
}

@keyframes pulse {
    0% {
        transform: scale(1);
        opacity: 0.8;
    }
    70% {
        transform: scale(1.5);
        opacity: 0;
    }
    100% {
        transform: scale(1);
        opacity: 0;
    }
}


/* אזור בקרה והודעות */
#controls {
    text-align: center;
    padding-top: 10px;
}

.message-area {
    margin-bottom: 15px;
    font-size: 1.1em;
    min-height: 1.5em; /* Prevent layout shift */
    color: #333;
    font-style: italic;
}

#crossed-count {
    margin-bottom: 15px;
    font-size: 1.1em;
    font-weight: bold;
    color: #424242;
}

.control-button {
    padding: 12px 20px;
    font-size: 1em;
    cursor: pointer;
    background-color: #03a9f4; /* Light blue */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.control-button:hover {
    background-color: #0288d1; /* Darker blue */
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.25);
}
.control-button:active {
    background-color: #01579b; /* Even darker */
    transform: translateY(0);
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}


/* לחצן הצגת הסבר */
#explanation-button {
    display: block;
    width: fit-content;
    margin: 30px auto;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    background-color: #4CAF50; /* Green */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

#explanation-button:hover {
    background-color: #388E3C; /* Darker green */
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.25);
}
#explanation-button:active {
     background-color: #1b5e20; /* Even darker */
     transform: translateY(0);
     box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}


/* אזור ההסבר המלא */
#full-explanation {
    display: none; /* Initially hidden */
    margin-top: 30px;
    padding: 20px;
    border: 1px solid #d3e0ea;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    line-height: 1.7;
    color: #333;
}

#full-explanation h2 {
    color: #212121;
    border-bottom: 2px solid #e0e0e0; /* Light grey border */
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
}

#full-explanation h2:first-child {
     margin-top: 0;
}

#full-explanation p {
    margin-bottom: 15px;
    text-align: justify;
}

#full-explanation ul {
    margin-bottom: 15px;
    padding-left: 20px;
}

#full-explanation li {
    margin-bottom: 8px;
}

</style>

<button id="explanation-button">הצג את הסוד המתמטי מאחורי החידה!</button>

<div id="full-explanation">
    <h2>הגשרים של קניגסברג: הסוד המתמטי נחשף</h2>

    <p>
        כמוכם, תושבי קניגסברג של המאה ה-18 ניסו שוב ושוב למצוא מסלול קסום שיחצה את כל שבעת הגשרים בדיוק פעם אחת. איש לא הצליח. האם זה אומר שהם לא התאמצו מספיק? או שיש סיבה עמוקה יותר לכך?
    </p>

    <h2>הראייה המהפכנית של אוילר</h2>
    <p>
        בשנת 1736, המתמטיקאי השוויצרי הגאון לאונרד אוילר ניגש לבעיה בצורה לא שגרתית. הוא התעלם לחלוטין מצורת הנהר, אורכי הגשרים וגודל היבשות. הוא הבין שמה שחשוב באמת אלו רק ה"חיבורים": אילו פיסות יבשה מחוברות על ידי אילו גשרים, וכמה גשרים מחוברים לכל פיסת יבשה.
    </p>

    <h2>לידתה של תורת הגרפים</h2>
    <p>
        הגישה המבריקה הזו הובילה את אוילר להמציא ענף מתמטי חדש לגמרי: <strong>תורת הגרפים</strong>. בגרף, אנחנו מייצגים את ה"דברים" (כמו היבשות בקניגסברג) כ<strong>צמתים</strong> (או קודקודים), ואת ה"קשרים" ביניהם (כמו הגשרים) כ<strong>קשתות</strong> (או צלעות).
    </p>

    <h2>קניגסברג כגרף - כמה קשרים יש לכל יבשה?</h2>
    <p>
        אם נתרגם את מפת קניגסברג לגרף, נקבל 4 צמתים (N, S, W, E) ו-7 קשתות (b1 עד b7). ה"דרגה" של כל צומת היא פשוט מספר הקשתות המחוברות אליו:
        <ul>
            <li>צומת N (האי הצפוני): מחובר ל-5 גשרים (דרגה 5)</li>
            <li>צומת E (הגדה המזרחית): מחובר ל-3 גשרים (דרגה 3)</li>
            <li>צומת W (הגדה המערבית): מחובר ל-3 גשרים (דרגה 3)</li>
            <li>צומת S (היבשה הדרומית): מחובר ל-3 גשרים (דרגה 3)</li>
        </ul>
        שימו לב: כל הדרגות (5, 3, 3, 3) הן מספרים אי-זוגיים!
    </p>

    <h2>המשפט האלגנטי של אוילר</h2>
    <p>
        אוילר גילה סוד פשוט אך רב עוצמה: ניתן למצוא מסלול שעובר בכל קשת בגרף בדיוק פעם אחת (מסלול אוילר) רק אם מתקיים אחד מהתנאים הבאים:
        <ul>
            <li>לכל הצמתים בגרף יש <strong>דרגה זוגית</strong>. במקרה כזה, אפשר להתחיל ולסיים באותו צומת (מעגל אוילר).</li>
            <li>יש לכל היותר <strong>שני צמתים</strong> בגרף בעלי דרגה אי-זוגית. במקרה כזה, חייבים להתחיל באחד מהם ולסיים בשני.</li>
        </ul>
        אם יש יותר משני צמתים בעלי דרגה אי-זוגית, <strong>מסלול אוילר אינו קיים כלל</strong>.
    </p>

    <h2>הפסיקה לגשרים של קניגסברג</h2>
    <p>
        במקרה שלנו, כל ארבעת הצמתים (N, S, W, E) הם בעלי דרגה אי-זוגית. לפי המשפט של אוילר, מכיוון שיש לנו <strong>ארבעה</strong> צמתים כאלה (הרבה יותר משניים), פשוט <strong>בלתי אפשרי</strong> לחצות את כל שבעת הגשרים בדיוק פעם אחת. ניסיונות התושבים נדונו לכישלון מראש!
    </p>

    <h2>השפעה אדירה: העולם המודרני ותורת הגרפים</h2>
    <p>
        מה שהתחיל כפתרון לחידה מקומית בקניגסברג הפך להיות אחד הכלים היסודיים והחשובים ביותר במתמטיקה ובמדעי המחשב. תורת הגרפים נמצאת בכל מקום סביבנו:
        <ul>
            <li><strong>רשתות חברתיות:</strong> אנשים הם צמתים, חברויות/קשרים הם קשתות. ניתוח רשתות חברתיות מסתמך על תורת הגרפים.</li>
            <li><strong>ניווט ו-GPS:</strong> ערים הן צמתים, כבישים הם קשתות. מציאת המסלול הקצר או המהיר ביותר היא בעיית גרפים קלאסית.</li>
            <li><strong>מנועי חיפוש:</strong> עמודי אינטרנט הם צמתים, קישורים ביניהם הם קשתות. האלגוריתם של גוגל (PageRank) מבוסס על מבנה הגרף של האינטרנט.</li>
            <li><strong>ביולוגיה ומדעי החיים:</strong> רשתות גנטיות, אינטראקציות בין חלבונים - כולם ניתנים לייצוג ולניתוח כגרפים.</li>
            <li><strong>לוגיסטיקה ותכנון:</strong> תכנון קווי תחבורה ציבורית, ניתוב חבילות בדואר, או ארגון שרשרת אספקה - כולם משתמשים בתורת הגרפים.</li>
        </ul>
        כך, חידה שנראתה כמו משחק פשוט הובילה לתגלית מתמטית שהניחה את היסודות לתחומים רבים המעצבים את העולם הטכנולוגי של ימינו.
    </p>
</div>


<script>
document.addEventListener('DOMContentLoaded', () => {
    // Map landmass ID to its approximate center coordinates (relative %) for marker positioning.
    // These should correspond roughly to the visual center specified in CSS.
    const landmassPositions = {
        'N': { top: '15%', left: '50%' },
        'S': { top: '85%', left: '50%' }, /* bottom 15% means top 85% */
        'W': { top: '50%', left: '12%' },
        'E': { top: '50%', left: '88%' } /* right 12% means left 88% */
    };

    // Define bridges and their connections (the graph structure)
    const bridges = {
        'b1': { ends: ['N', 'E'], element: document.getElementById('bridge-b1') },
        'b2': { ends: ['N', 'E'], element: document.getElementById('bridge-b2') },
        'b3': { ends: ['N', 'W'], element: document.getElementById('bridge-b3') },
        'b4': { ends: ['N', 'W'], element: document.getElementById('bridge-b4') },
        'b5': { ends: ['N', 'S'], element: document.getElementById('bridge-b5') },
        'b6': { ends: ['E', 'S'], element: document.getElementById('bridge-b6') },
        'b7': { ends: ['W', 'S'], element: document.getElementById('bridge-b7') }
    };

    // Game state variables
    let currentLandmass = 'N'; // Start on the North island
    let bridgesCrossedState = {}; // Tracks which bridges have been crossed { b1: false, ... }
    let crossedCount = 0;
    const totalBridges = Object.keys(bridges).length;

    // UI elements
    const messageArea = document.getElementById('message-area');
    const crossedCountDisplay = document.getElementById('crossed-count');
    const resetButton = document.getElementById('reset-button');
    const explanationButton = document.getElementById('explanation-button');
    const explanationDiv = document.getElementById('full-explanation');
    const locationMarker = document.getElementById('current-location-marker');
    const landmassElements = {
        'N': document.getElementById('land-N'),
        'S': document.getElementById('land-S'),
        'W': document.getElementById('land-W'),
        'E': document.getElementById('land-E')
    };


    // --- Game Logic Functions ---

    // Updates the visual position of the marker
    function updateMarkerPosition() {
        const pos = landmassPositions[currentLandmass];
        locationMarker.style.top = pos.top;
        locationMarker.style.left = pos.left;

        // Optional: Add a class to the current landmass for visual feedback (e.g., pulse)
        Object.values(landmassElements).forEach(el => el.classList.remove('active'));
        landmassElements[currentLandmass].classList.add('active');
    }

    // Resets the game state and UI
    function resetGame() {
        currentLandmass = 'N'; // Reset to the starting landmass
        crossedCount = 0;
        bridgesCrossedState = {}; // Clear crossed bridges
        for (const bridgeId in bridges) {
            bridgesCrossedState[bridgeId] = false;
            bridges[bridgeId].element.classList.remove('crossed'); // Remove crossed visual state
        }

        // Update UI
        messageArea.textContent = 'לחץ על גשר כדי להתחיל את המסע שלך!';
        crossedCountDisplay.textContent = `גשרים שחצית: ${crossedCount} / ${totalBridges}`;
        updateMarkerPosition(); // Move marker back to start

        // Ensure win message is cleared if reset after winning
         if (messageArea.classList.contains('win-message')) {
            messageArea.classList.remove('win-message');
             messageArea.textContent = 'לחץ על גשר כדי להתחיל את המסע שלך!'; // Reset initial message
        }
    }

    // Handles a bridge click event
    function handleBridgeClick(bridgeId) {
        const bridge = bridges[bridgeId];
        const [end1, end2] = bridge.ends; // The two landmasses the bridge connects

        // Check if the user is currently on one of the landmasses connected by this bridge
        if (currentLandmass !== end1 && currentLandmass !== end2) {
            messageArea.textContent = `אה! כדי לחצות את הגשר הזה, אתה צריך להיות ביבשה ${end1} או ${end2}. אתה נמצא כרגע ב- ${currentLandmass}.`;
            return; // Invalid move
        }

        // Check if the bridge has already been crossed
        if (bridgesCrossedState[bridgeId]) {
            messageArea.textContent = `כבר חצית את הגשר הזה! זכור, המטרה היא לחצות כל גשר בדיוק פעם אחת.`;
            return; // Invalid move
        }

        // Valid move!
        bridgesCrossedState[bridgeId] = true; // Mark bridge as crossed
        bridge.element.classList.add('crossed'); // Change bridge color visually
        crossedCount++; // Increment count

        // Update current location to the other end of the bridge
        currentLandmass = (currentLandmass === end1) ? end2 : end1;

        // Update UI
        messageArea.textContent = `חצית גשר! אתה נמצא כעת ביבשה ${currentLandmass}.`;
        crossedCountDisplay.textContent = `גשרים שחצית: ${crossedCount} / ${totalBridges}`;
        updateMarkerPosition(); // Animate marker to the new location

        // Check for win condition
        if (crossedCount === totalBridges) {
            messageArea.textContent = '🥳 מזל טוב! חצית את כל 7 הגשרים! 🎉 (קרא את ההסבר למטה כדי לגלות למה זה ניצחון מיוחד...)';
            messageArea.classList.add('win-message'); /* Optional class for win styling */
        }
    }

    // --- Event Listeners ---

    // Add click listeners to all bridge elements
    for (const bridgeId in bridges) {
        bridges[bridgeId].element.addEventListener('click', () => handleBridgeClick(bridgeId));
    }

    // Add click listener to the reset button
    resetButton.addEventListener('click', resetGame);

    // Add click listener to the explanation button
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר את הסוד המתמטי' : 'הצג את הסוד המתמטי מאחורי החידה!';
    });

    // --- Initial Setup ---

    resetGame(); // Start the game when the page loads
    explanationDiv.style.display = 'none'; // Ensure explanation is hidden initially
});

</script>