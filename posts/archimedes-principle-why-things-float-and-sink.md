---
title: "סוד הציפה: למה עצמים צפים או שוקעים במים?"
english_slug: archimedes-principle-why-things-float-and-sink
category: "מדעים מדויקים / פיזיקה"
tags: [ארכימדס, ציפה, צפיפות, כוח ציפה, נוזלים]
---
# סוד הציפה: למה עצמים צפים או שוקעים במים?

איך זה ייתכן שאוניית ענק מפלדה שטה בקלילות על פני הים, בעוד שאבן קטנה צוללת ישירות לתחתית? האם יש חוק נסתר שקובע את גורלם של עצמים בנוזל? בואו נחקור יחד את הקסם הפיזיקלי שמאחורי ציפה ושקיעה!

<div id="simulator">
    <div id="object-shelf">
        <h2>בחר עצם וגרור למיכל המים:</h2>
        <div class="object" id="obj-wood" draggable="true" data-density="600" data-name="עץ">🪵 עץ</div>
        <div class="object" id="obj-plastic" draggable="true" data-density="950" data-name="פלסטיק">🧴 פלסטיק</div>
        <div class="object" id="obj-iron" draggable="true" data-density="7800" data-name="ברזל">🔩 ברזל</div>
        <div class="object" id="obj-neutral" draggable="true" data-density="1000" data-name="צפיפות-מים">💧 צפיפות מים</div>
        <div class="object" id="obj-stone" draggable="true" data-density="2500" data-name="אבן">🪨 אבן</div>
    </div>
    <div id="tank-container">
        <div id="water-tank">
            <div id="water">
                 <div id="simulated-object"></div>
            </div>
           
        </div>
        <div id="info-panel">
            <h3>דוח ניסוי:</h3>
            <p id="info-water-density">צפיפות מים: 1000 ק"ג/מ³</p>
            <p id="info-object-name">עצם: <span class="info-value">--</span></p>
            <p id="info-object-density">צפיפות עצם: <span class="info-value">--</span></p>
            <p id="info-result">תוצאה: <span class="info-value">--</span></p>
             <div id="reset-container">
                <button id="reset-button">🧪 נסה שוב!</button>
             </div>
        </div>
    </div>
     <div id="water-level-indicator"></div>
</div>

<style>
/* General body and root styles for a modern feel */
body {
    margin: 0;
    padding: 0;
    background-color: #f4f7f6; /* Soft background */
    color: #333;
    font-family: 'Arial', sans-serif; /* Use a standard, clean font */
    line-height: 1.6;
}

#simulator {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 40px;
    padding: 20px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); /* Soft, modern shadow */
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

#object-shelf {
    display: flex;
    justify-content: center;
    gap: 20px; /* Increased gap */
    margin-bottom: 40px; /* More space below shelf */
    flex-wrap: wrap;
    padding: 15px;
    background-color: #e0f2f7; /* Light blue background for shelf */
    border-radius: 8px;
    width: 100%;
    box-sizing: border-box;
}

#object-shelf h2 {
    width: 100%;
    text-align: center;
    margin-bottom: 15px;
    color: #0056b3; /* A shade of blue */
    font-size: 1.4em; /* Slightly larger font */
    font-weight: bold;
}

.object {
    width: 70px; /* Slightly larger objects */
    height: 70px;
    border: 2px solid #aaa; /* More prominent border */
    cursor: grab;
    display: flex;
    flex-direction: column; /* Stack emoji and text */
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 0.9em; /* Slightly larger text */
    font-weight: bold;
    border-radius: 10px; /* More rounded corners */
    box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* Softer shadow */
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Smooth transitions */
    user-select: none; /* Prevent text selection during drag */
}

.object:hover {
    transform: translateY(-5px) scale(1.05); /* Lift and slightly enlarge on hover */
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    cursor: grab;
}

.object:active {
    cursor: grabbing;
    transform: scale(1.03); /* Slightly shrink when clicked */
}

.object span { /* Style for emoji */
    font-size: 1.5em;
    margin-bottom: 3px;
}


/* Specific object styles */
#obj-wood { background-color: #f0d9b5; border-color: #c8a27d; color: #4a2f0f; }
#obj-plastic { background-color: #b3e5fc; border-color: #81d4fa; color: #01579b; }
#obj-iron { background-color: #90a4ae; border-color: #607d8b; color: white; }
#obj-neutral { background-color: #e0f7fa; border-color: #b2ebf2; color: #006064; }
#obj-stone { background-color: #a1887f; border-color: #795548; color: white; }


#tank-container {
    display: flex;
    align-items: flex-start; /* Align items to the top */
    gap: 40px; /* Increased gap between tank and panel */
    width: 100%;
    max-width: 750px; /* Max width for the container */
    justify-content: center;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

#water-tank {
    width: 300px;
    height: 450px; /* Taller tank */
    border: 6px solid #0d47a1; /* Darker, richer border */
    position: relative;
    overflow: hidden;
    background: linear-gradient(to bottom, #b3e5fc, #e1f5fe); /* Subtle sky gradient */
    border-radius: 15px; /* More rounded */
    box-shadow: inset 0 0 15px rgba(0,0,0,0.1), 0 8px 20px rgba(0,0,0,0.1); /* Inner and outer shadow */
    flex-shrink: 0; /* Prevent shrinking */
}

#water {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 90%; /* Water fills 90% */
    background: linear-gradient(to top, rgba(41, 128, 185, 0.8), rgba(109, 213, 250, 0.8)); /* Gradient for water depth */
    /* Add subtle wave effect later if possible with CSS */
}

#simulated-object {
    position: absolute;
    width: 70px; /* Match object size */
    height: 70px; /* Match object size */
    left: 50%;
    /* Start off-screen or near the top */
    transform: translateX(-50%);
    background-color: transparent; /* Will be set by JS */
    border: 2px solid transparent; /* Will be set by JS, match shelf objects border width */
    display: flex;
    flex-direction: column; /* Stack emoji and text */
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 0.9em;
    font-weight: bold;
    border-radius: 10px; /* Match shelf objects */
    box-sizing: border-box; /* Include border in dimensions */
    color: white; /* Default text color - will be overridden */
    /* Initial transition for dropping */
    transition: top 3s ease-out; /* Animation for sinking/floating */
     /* Add box-shadow for depth */
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

#info-panel {
    width: 280px; /* Slightly wider panel */
    border: 1px solid #e0e0e0; /* Lighter border */
    padding: 20px; /* More padding */
    border-radius: 10px; /* More rounded corners */
    background-color: #ffffff; /* White background */
    box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Softer shadow */
    flex-grow: 1; /* Allow panel to grow */
}

#info-panel h3 {
    margin-top: 0;
    color: #0d47a1; /* Match tank border color */
    font-size: 1.2em; /* Slightly larger font */
    border-bottom: 1px solid #eee; /* Separator */
    padding-bottom: 10px;
    margin-bottom: 15px;
}

#info-panel p {
    margin-bottom: 12px; /* More space between paragraphs */
    font-size: 1em; /* Standard font size */
    color: #555;
    display: flex; /* Use flexbox for alignment */
    justify-content: space-between; /* Space out label and value */
}

.info-value {
    font-weight: bold;
    color: #333;
}

#reset-container {
    text-align: center; /* Center the button */
    margin-top: 20px; /* Space above button */
}

#reset-button {
    display: inline-block; /* Center button */
    padding: 12px 25px; /* More padding */
    background-color: #ff9800; /* Orange button */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

#reset-button:hover {
    background-color: #f57c00; /* Darker orange on hover */
    transform: translateY(-2px); /* Lift effect */
}

#reset-button:active {
     transform: translateY(0); /* Press effect */
     box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}


#toggle-explanation {
    display: block;
    width: 220px; /* Wider button */
    margin: 40px auto; /* More space */
    padding: 14px; /* More padding */
    background-color: #4caf50; /* Green button */
    color: white;
    border: none;
    border-radius: 25px; /* Pill shape */
    cursor: pointer;
    font-size: 1.1em; /* Larger font */
    font-weight: bold;
    text-align: center;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

#toggle-explanation:hover {
    background-color: #388e3c; /* Darker green on hover */
    transform: translateY(-2px); /* Lift effect */
}
#toggle-explanation:active {
     transform: translateY(0); /* Press effect */
     box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}


#explanation {
    margin-top: 40px; /* More space above explanation */
    padding: 30px; /* More padding */
    border-top: 2px solid #eee; /* Thicker separator */
    line-height: 1.7; /* More relaxed line height */
    color: #333;
    background-color: #ffffff; /* White background for explanation */
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

#explanation h2, #explanation h3 {
    color: #0d47a1; /* Match heading color */
    margin-top: 25px; /* More space above headings */
    margin-bottom: 12px; /* More space below headings */
}

#explanation h2 {
    font-size: 1.8em;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
}

#explanation h3 {
     font-size: 1.4em;
}


#explanation p {
    margin-bottom: 18px; /* More space between paragraphs */
    font-size: 1.1em; /* Slightly larger text */
}

#explanation ul {
    margin-bottom: 18px;
    padding-left: 30px; /* More padding */
}

#explanation li {
    margin-bottom: 10px; /* More space between list items */
    font-size: 1.1em;
}

/* Styling for drag feedback */
.object.dragging {
    opacity: 0.7; /* Slightly transparent */
    transform: scale(1.1); /* Enlarge while dragging */
    cursor: grabbing;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3); /* More prominent shadow */
}

/* Add a subtle ripple effect to water when object drops */
/* This is a simple visual effect, not a physics simulation */
#water.ripple::after {
    content: '';
    position: absolute;
    top: 0; /* Position at the top of the water */
    left: 0;
    width: 100%;
    height: 10px; /* Height of the visual ripple area */
    background: radial-gradient(ellipse at 50% 0%, rgba(255, 255, 255, 0.5) 0%, transparent 70%);
    animation: ripple-animation 1.5s ease-out forwards;
}

@keyframes ripple-animation {
    0% { opacity: 1; transform: scaleX(0.5); }
    100% { opacity: 0; transform: scaleX(1.5); }
}


/* Media Queries for responsiveness */
@media (max-width: 768px) {
    #simulator {
        padding: 10px;
    }

    #object-shelf {
        gap: 10px;
        margin-bottom: 20px;
        padding: 10px;
    }

     #object-shelf h2 {
        font-size: 1.3em;
    }

    .object {
        width: 60px;
        height: 60px;
        font-size: 0.8em;
        border-radius: 8px;
    }

    .object span {
        font-size: 1.2em;
    }

    #tank-container {
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

    #water-tank {
        width: 250px;
        height: 380px;
        border-radius: 10px;
    }

     #simulated-object {
        width: 60px;
        height: 60px;
         border-radius: 8px;
         font-size: 0.8em;
     }

    #info-panel {
        width: calc(100% - 20px); /* Adjust width */
        max-width: 300px; /* Limit max width */
        padding: 15px;
        border-radius: 8px;
    }

     #info-panel h3 {
        font-size: 1.1em;
        margin-bottom: 10px;
     }

     #info-panel p {
         font-size: 0.9em;
         margin-bottom: 8px;
     }


    #reset-button, #toggle-explanation {
        padding: 10px 20px;
        font-size: 1em;
    }

    #explanation {
        padding: 20px;
        margin-top: 30px;
        border-radius: 10px;
    }

     #explanation h2 {
        font-size: 1.6em;
     }
     #explanation h3 {
        font-size: 1.3em;
     }
     #explanation p, #explanation li {
        font-size: 1em;
     }
}

</style>

<button id="toggle-explanation">הצג/הסתר את הסוד מאחורי הציפה</button>

<div id="explanation" style="display: none;">
    <h2>עקרון ארכימדס נחשף!</h2>

    <h3>מסע אל תוך הנוזל: מה מרגיש עצם כשהוא נכנס למים?</h3>
    דמיינו שאתם דוחפים כדור לתוך אמבטיה מלאה מים. אתם מרגישים שהמים "דוחפים" את הכדור בחזרה כלפי מעלה, נכון? זוהי תחושת כוח הציפה! בכל פעם שעצם נכנס לנוזל (בין אם זה מים, שמן או אפילו אוויר!), הוא תופס את מקומם של המים שהיו שם קודם. הנוזל "מגיב" לכך בכך שהוא מפעיל כוח כלפי מעלה על העצם.

    <h3>הגיבור שלנו: כוח הציפה</h3>
    כוח הציפה הוא אותו כוח קסום שהנוזל מפעיל כלפי מעלה על כל עצם שטבול בו, חלקית או כולה. למה הוא קיים? כי הלחץ בנוזל גדל ככל שיורדים לעומק. לכן, החלק התחתון של העצם "מרגיש" לחץ גדול יותר כלפי מעלה מהלחץ ש"מרגיש" החלק העליון כלפי מטה. ההפרש הזה יוצר כוח נטו שדוחף את העצם למעלה.

    <h3>עקרון ארכימדס: הגודל קובע... אבל של מה?</h3>
    החכם היווני ארכימדס גילה את החוק הבסיסי שקובע בדיוק כמה גדול כוח הציפה: **כוח הציפה הפועל על עצם שווה בדיוק למשקל הנוזל שהעצם דחה.**
    חשבו על זה: אם העצם טבול לגמרי, הוא דוחה נפח נוזל השווה לנפח שלו. אם הוא צף רק קצת, הוא דוחה רק נפח נוזל השווה לנפח החלק השקוע שלו.
    הנוסחה פשוטה: **כוח ציפה = צפיפות הנוזל * נפח הנוזל שהודח * תאוצת הכבידה**.

    <h3>הקרב המכריע: צפיפות העצם מול צפיפות הנוזל</h3>
    האם העצם יצוף או ישקע? הכל תלוי בקרב בין שני כוחות: המשקל של העצם (שמושך מטה) וכוח הציפה (שדוחף מעלה). והיחס בין שני הכוחות האלה מושפע בעיקר מהיחס בין צפיפות העצם לצפיפות הנוזל.

    <ul>
        <li>
            <strong>אם צפיפות העצם קטנה מצפיפות הנוזל:</strong>
            העצם "קל" יותר מנפח שווה של נוזל. כשהוא נכנס למים, כוח הציפה גדול ממשקלו. הכוח העודף דוחף אותו למעלה עד שחלק ממנו יוצא מהמים. ברגע שהעצם צף, הוא דוחה פחות מים. הוא יתייצב כשלחלק השקוע שלו יש בדיוק את הנפח הדרוש כדי לדחות מספיק מים שמשקלם שווה למשקל העצם כולו. **העצם יצוף!**
        </li>
        <li>
            <strong>אם צפיפות העצם גדולה מצפיפות הנוזל:</strong>
            העצם "כבד" יותר מנפח שווה של נוזל. גם אם הוא טבול כולו ודוחה נפח מים השווה לנפחו, כוח הציפה שפועל עליו קטן ממשקלו. משום שהכבידה מנצחת, העצם ימשיך לשקוע עד שיגיע לתחתית. **העצם ישקע!**
        </li>
        <li>
            <strong>אם צפיפות העצם שווה לצפיפות הנוזל:</strong>
            העצם שוקל בדיוק כמו נפח שווה של נוזל. כשהוא טבול כולו, כוח הציפה שווה בדיוק למשקלו. הכוחות מאוזנים בצורה מושלמת, והעצם יישאר במקום שבו הנחתם אותו בתוך הנוזל, בלי לשקוע או לצוף. זוהי **"ציפה ניטרלית"**.
        </li>
    </ul>

    <h3>החידה נפתרה: איך אוניות ענק צפות?</h3>
    אז למה אוניית פלדה לא שוקעת מיד? הסוד טמון בצפיפות ה*ממוצעת* של האונייה, לא רק בחומר ממנו היא עשויה. האונייה חלולה! היא מלאה באוויר, שהוא הרבה פחות צפוף ממים. כשהאונייה שקועה במים, היא דוחה נפח מים *עצום* שכולל לא רק את נפח הפלדה אלא גם את נפח החללים המלאים באוויר. הצפיפות הממוצעת של כל המערכת הזו (פלדה + אוויר + מטען) קטנה מצפיפות המים. לכן, כוח הציפה העצום שנוצר כתוצאה מדחיקת נפח המים הזה, גדול מספיק כדי לאזן את משקלה הכולל של האונייה, והיא צפה. אבן קטנה מפלדה, לעומת זאת, דוחה רק נפח מים השווה לנפחה הקטן, וצפיפותה גבוהה מאוד, ולכן היא שוקעת ללא תחרות.

    <h3>ארכימדס סביבנו: דוגמאות מהחיים</h3>
    עקרון ארכימדס מסביר לנו כל מיני דברים מדליקים:
    *   איך צוללות שולטות בעומק שלהן (על ידי הכנסת או הוצאת מים ממיכלים).
    *   למה בלוני הליום עפים (צפיפות ההליום קטנה מצפיפות האוויר - כן, אוויר הוא גם נוזל לצורך העניין!).
    *   איך דגים נשארים בעומק הרצוי (יש להם שלפוחית ציפה שמשנה את נפחה).
    *   ו, כמובן, למה אתם צפים בים המלח (צפיפות המים בו גבוהה בהרבה!).

</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const waterTank = document.getElementById('water-tank');
    const water = document.getElementById('water');
    const simulatedObject = document.getElementById('simulated-object');
    const objectShelf = document.getElementById('object-shelf');
    const infoObjectName = document.getElementById('info-object-name').querySelector('.info-value');
    const infoObjectDensity = document.getElementById('info-object-density').querySelector('.info-value');
    const infoResult = document.getElementById('info-result').querySelector('.info-value');
    const resetButton = document.getElementById('reset-button');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    const waterDensity = 1000; // kg/m³
    const gravity = 9.8; // m/s² (though we only care about relative densities here)

    // Define the fill level of the water relative to the tank height (0 to 1)
    const waterFillRatio = 0.9;

    // Calculate the water level Y position (distance from top of tank)
    // Need to wait for the tank element to be rendered to get its clientHeight
    let tankHeight = 0;
    let waterHeight = 0;
    let waterLevelY = 0; // Y coordinate of the water surface (from the top of the tank)

    // Object dimensions (assuming they are square and consistent)
    // Need to get this from the actual simulated-object div once it's visible/styled
    let objectWidth = 0;
    let objectHeight = 0;

    // Variable to track if an object is currently in the tank
    let isObjectInTank = false;

    // Function to update dimensions after layout is settled
    const updateDimensions = () => {
        tankHeight = waterTank.clientHeight;
        waterHeight = waterTank.clientHeight * waterFillRatio;
        waterLevelY = tankHeight - waterHeight; // Y from top

        // Get object dimensions - assuming simulatedObject has the final size applied by CSS
        // A temporary element might be needed if simulatedObject isn't always visible
        // For now, assuming simulatedObject is sized by CSS and starts off-screen.
        // We can grab the dimensions from a shelf object if they are guaranteed identical
        const sampleObject = objectShelf.querySelector('.object');
        if (sampleObject) {
             objectWidth = sampleObject.offsetWidth;
             objectHeight = sampleObject.offsetHeight;
        } else {
            // Fallback if no objects on shelf (shouldn't happen)
            objectWidth = 70; // Default size from CSS
            objectHeight = 70; // Default size from CSS
        }

         // Apply calculated water height to the water element
         water.style.height = `${waterHeight}px`;
         water.style.top = `${waterLevelY}px`;
    };

    // Update dimensions initially and on window resize
    window.addEventListener('resize', updateDimensions);
    // Use requestAnimationFrame or a small timeout to ensure CSS is applied before getting dims
    requestAnimationFrame(updateDimensions);
    // Or slightly delayed fallback:
    setTimeout(updateDimensions, 50);


    // Add drag start listener to objects on the shelf
    objectShelf.querySelectorAll('.object').forEach(obj => {
        obj.addEventListener('dragstart', (event) => {
            // Prevent dragging if an object is already in the tank
            if (isObjectInTank) {
                 event.preventDefault();
                 return;
            }

            event.dataTransfer.setData('text/plain', event.target.id);
            event.dataTransfer.effectAllowed = 'copy';
            event.target.classList.add('dragging');

            // Clear previous object info visually and logically
            resetSimulation(false); // Reset without animating object away, just clear info
        });

        obj.addEventListener('dragend', (event) => {
             event.target.classList.remove('dragging');
        });
    });

    // Allow dropping on the water tank
    waterTank.addEventListener('dragover', (event) => {
        event.preventDefault(); // Necessary to allow dropping
        // Only allow drop if no object is in the tank
        if (!isObjectInTank) {
            event.dataTransfer.dropEffect = 'copy';
        } else {
            event.dataTransfer.dropEffect = 'none'; // Indicate cannot drop
        }
    });

    waterTank.addEventListener('drop', (event) => {
        event.preventDefault();

        // Only process drop if no object is in the tank
        if (isObjectInTank) {
             return;
        }

        const objectId = event.dataTransfer.getData('text/plain');
        const draggedObject = document.getElementById(objectId);

        if (draggedObject) {
            isObjectInTank = true; // Mark that an object is now in the tank

            const density = parseInt(draggedObject.dataset.density, 10);
            const name = draggedObject.dataset.name;
            const originalColor = draggedObject.style.backgroundColor;
            const originalBorderColor = draggedObject.style.borderColor;
            const originalColorText = draggedObject.style.color; // Text color

            // Set up the simulated object visual properties
            simulatedObject.style.transition = 'none'; // Disable transition initially
            simulatedObject.style.backgroundColor = originalColor;
            simulatedObject.style.borderColor = originalBorderColor;
            simulatedObject.style.color = originalColorText;
            // Copy the emoji and text content
            simulatedObject.innerHTML = draggedObject.innerHTML;
            simulatedObject.style.width = `${objectWidth}px`; // Ensure correct size
            simulatedObject.style.height = `${objectHeight}px`; // Ensure correct size


            // Calculate where the object starts its fall (adjust for centering)
            const dropX = event.offsetX; // X relative to tank
            const dropY = event.offsetY; // Y relative to tank
            const startLeft = dropX - objectWidth / 2; // Centered horizontally
            const startTop = Math.max(0, dropY - objectHeight / 2); // Start at drop point or top if dropped high

            simulatedObject.style.left = `${startLeft}px`;
            simulatedObject.style.top = `${startTop}px`;


            // Calculate behavior
            let finalPositionTop; // Y position (top)
            let resultText;
            let animationDuration = 2000; // Base animation duration in ms

            if (density < waterDensity) {
                // Floats
                const submergedRatio = density / waterDensity; // Ratio of volume submerged
                const submergedHeight = objectHeight * submergedRatio;
                // Calculate the final top position so the bottom of the object is at the water level
                finalPositionTop = waterLevelY - submergedHeight;
                 // Ensure it doesn't float *above* the water level visually if ratio is tiny
                 finalPositionTop = Math.min(finalPositionTop, waterLevelY - (objectHeight * 0.1)); // Keep at least 10% submerged visually for very low densities? Or just trust the math: waterLevelY - submergedHeight
                 resultText = `יצוף!`;
                 // Duration for floating is less than sinking
                 animationDuration = 2500; // Shorter duration to surface
            } else if (density > waterDensity) {
                // Sinks
                // Calculate the final top position so the bottom of the object is at the bottom of the tank
                const tankBottomY = tankHeight; // Bottom edge of tank relative to its top
                finalPositionTop = tankBottomY - objectHeight; // Object's top when it sits on the bottom
                resultText = `ישקע...`;
                // Duration for sinking depends on depth
                 animationDuration = 3000; // Longer duration to sink
            } else { // density === waterDensity
                // Neutral buoyancy - will float anywhere inside the water
                // For simplicity, let's make it settle just below the surface
                 // Keep it roughly where it was dropped vertically, but ensure it's within the water
                 let midDropY = dropY;
                 // Ensure it's between water surface and bottom
                 midDropY = Math.max(midDropY, waterLevelY + objectHeight/2); // At least half submerged
                 midDropY = Math.min(midDropY, tankHeight - objectHeight/2); // At most half above bottom

                 finalPositionTop = midDropY - objectHeight / 2; // Position top for center
                 resultText = `מרחף!`;
                 animationDuration = 2000; // Moderate duration to settle
            }

            // Update info panel
            infoObjectName.textContent = name;
            infoObjectDensity.textContent = `${density} ק"ג/מ³`;
            infoResult.textContent = resultText;

            // Trigger the animation with a small delay to allow initial position setting
             setTimeout(() => {
                 simulatedObject.style.transition = `top ${animationDuration}ms ease-in-out`;
                 simulatedObject.style.top = `${finalPositionTop}px`;
                 // Add subtle horizontal centering animation too
                 simulatedObject.style.transition += `, left ${animationDuration/2}ms ease-in-out`;
                 simulatedObject.style.left = `calc(50% - ${objectWidth/2}px)`;

                 // Add visual ripple effect to water surface
                 water.classList.add('ripple');
                 // Remove ripple class after animation
                 setTimeout(() => {
                     water.classList.remove('ripple');
                 }, 1500); // Matches ripple animation duration

             }, 50); // Small delay

             // After the animation finishes, maybe add a slight bounce or settle effect (more complex JS animation needed)
             // For now, just ensure transition is reset after animation
            simulatedObject.addEventListener('transitionend', handleAnimationEnd, { once: true });
        }
    });

    function handleAnimationEnd() {
         // Animation finished. Could potentially add a subtle bounce here
         // For this simplified version, just ensure transitions are ready for next action (reset)
         simulatedObject.style.transition = ''; // Remove transition after settling
    }


    // Reset button functionality
    function resetSimulation(animate = true) {
        if (animate) {
             simulatedObject.style.transition = 'top 0.8s ease-in, opacity 0.8s ease-in'; // Animation to move up and fade
             simulatedObject.style.top = '-100px'; // Move object off-screen above tank
             simulatedObject.style.opacity = '0'; // Fade out
             isObjectInTank = false; // Allow dropping a new object
             // Clear info after animation
             simulatedObject.addEventListener('transitionend', function _listener() {
                 simulatedObject.style.backgroundColor = 'transparent';
                 simulatedObject.style.borderColor = 'transparent';
                 simulatedObject.style.color = 'white'; // Reset color
                 simulatedObject.textContent = ''; // Clear content
                 simulatedObject.style.opacity = '1'; // Reset opacity for next time
                 simulatedObject.removeEventListener('transitionend', _listener); // Clean up listener
             }, { once: true });

        } else {
             // Instant reset
            simulatedObject.style.transition = 'none';
            simulatedObject.style.top = '-100px';
            simulatedObject.style.left = '50%'; // Reset horizontal position too
            simulatedObject.style.transform = 'translateX(-50%)';
            simulatedObject.style.backgroundColor = 'transparent';
            simulatedObject.style.borderColor = 'transparent';
             simulatedObject.style.color = 'white'; // Reset color
            simulatedObject.textContent = '';
             simulatedObject.style.opacity = '1'; // Reset opacity
            isObjectInTank = false;
        }


        infoObjectName.textContent = '--';
        infoObjectDensity.textContent = '--';
        infoResult.textContent = '--';
    }


    resetButton.addEventListener('click', () => {
        resetSimulation(true); // Animate reset
    });


    // Toggle explanation visibility
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationButton.textContent = isHidden ? 'הסתר את הסוד מאחורי הציפה' : 'הצג/הסתר את הסוד מאחורי הציפה';
    });

    // Initial setup: Ensure simulated object is hidden and reset info panel
     resetSimulation(false); // Perform instant reset on load

});
</script>