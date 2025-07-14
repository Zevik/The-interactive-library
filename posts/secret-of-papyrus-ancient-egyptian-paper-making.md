---
title: "סוד הפפירוס: מסע אל סדנת הנייר המצרית העתיקה"
english_slug: secret-of-papyrus-ancient-egyptian-paper-making
category: "ארכאולוגיה"
tags: ["פפירוס", "מצרים העתיקה", "היסטוריה", "טכנולוגיה עתיקה", "תהליך ייצור"]
---
# סוד הפפירוס: מסע אל סדנת הנייר המצרית העתיקה

דמיינו עולם ללא נייר מודרני. על מה היו כותבים את הסיפורים, החוקים והמגילות הקדושות? במצרים העתיקה, התשובה הייתה טמונה בסוד גדול: צמח הנילוס שסיפק את חומר הכתיבה המשמעותי ביותר של העולם העתיק - הפפירוס. הצטרפו למסע אינטראקטיבי מרתק וחוו בעצמכם את תהליך הייצור הקסום שהפך גבעול רגיל ל"נייר" של הפרעונים!

<div id="papyrus-app">
    <div id="app-area">
        <div id="papyrus-display">
            <!-- Visuals and interactive elements will appear here -->
            <img id="step-image" src="" alt="שלב בתהליך יצור הפפירוס">
            <div id="interactive-element">
                <!-- Dynamic interactive content -->
            </div>
             <div id="papyrus-animation-overlay"></div> <!-- New element for animations -->
        </div>
        <div id="step-info">
            <p id="step-text"></p>
            <div class="button-container">
                <button id="perform-action-btn" class="action-button" style="display: none;">בצע פעולה</button>
                 <button id="next-step-btn" class="navigation-button">התקדם לשלב הבא</button>
            </div>
        </div>
    </div>
</div>

<style>
    :root {
        --egyptian-sand: #e0d8c1;
        --egyptian-clay: #c0b8a1;
        --egyptian-blue: #0077b6;
        --egyptian-gold: #ffc300;
        --papyrus-light: #f0e9d8;
        --papyrus-dark: #d8cfa1;
        --success-color: #4CAF50;
        --button-bg: var(--egyptian-blue);
        --button-hover: #023e8a;
    }

    #papyrus-app {
        font-family: 'Arial', sans-serif; /* Consider a more thematic font if available/safe */
        direction: rtl;
        text-align: right;
        max-width: 800px;
        margin: 20px auto;
        border: 2px solid var(--egyptian-clay);
        border-radius: 12px;
        padding: 25px;
        background-color: var(--egyptian-sand);
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        overflow: hidden; /* Important for animations */
    }

    #app-area {
        display: flex;
        flex-direction: column;
        gap: 25px;
        align-items: center;
    }

    #papyrus-display {
        width: 100%;
        min-height: 350px; /* Increased height */
        background-color: var(--papyrus-light);
        border: 2px solid var(--egyptian-clay);
        border-radius: 8px;
        display: flex;
        flex-direction: column; /* Allow stacking elements */
        justify-content: center;
        align-items: center;
        overflow: hidden;
        position: relative;
        padding: 15px;
        box-sizing: border-box;
        transition: background-color 0.5s ease;
    }

    #step-image {
        max-width: 100%;
        max-height: 320px;
        display: none; /* Initially hidden, shown by JS */
        object-fit: contain; /* Ensures image fits without distortion */
        transition: opacity 0.5s ease;
    }

     #interactive-element {
        padding: 10px; /* Slightly less padding */
        text-align: center;
        width: 100%;
        box-sizing: border-box;
        flex-grow: 1; /* Allow it to take available space */
        display: flex; /* Use flexbox for centering/layout within interactive area */
        justify-content: center;
        align-items: center;
        position: relative; /* For absolute positioned children */
    }

     #papyrus-animation-overlay {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks to pass through */
         overflow: hidden;
         z-index: 10; /* Above other elements */
     }

    #step-info {
        width: 100%;
        text-align: center;
    }

    #step-text {
        min-height: 4em; /* Reserve more space */
        margin-bottom: 20px;
        line-height: 1.6;
        color: #333;
        font-size: 1.1em;
    }

    .button-container {
        display: flex;
        justify-content: center;
        gap: 15px; /* Space between buttons */
    }

    .action-button, .navigation-button {
        padding: 12px 25px; /* Increased padding */
        font-size: 1em;
        cursor: pointer;
        background-color: var(--button-bg);
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    .action-button:hover, .navigation-button:hover {
        background-color: var(--button-hover);
        transform: translateY(-2px); /* Lift effect on hover */
    }
     .action-button:active, .navigation-button:active {
        transform: translateY(1px); /* Press effect */
    }

    #perform-action-btn.active {
         background-color: var(--success-color); /* Indicate action is ready */
         box-shadow: 0 0 8px var(--success-color);
    }

    #explanation-btn {
        display: block;
        margin: 30px auto 20px;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        background-color: #008CBA; /* Keep a standard blue */
        color: white;
        border: none;
        border-radius: 4px;
        transition: background-color 0.3s ease;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    #explanation-btn:hover {
        background-color: #007bb5;
    }

    #full-explanation {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding: 25px;
        border: 2px solid var(--egyptian-clay);
        border-radius: 8px;
        background-color: #fff;
        direction: rtl;
        text-align: right;
        line-height: 1.7;
        color: #333;
    }

    #full-explanation h2 {
        color: #00509d; /* Deeper blue */
        border-bottom: 2px solid var(--egyptian-clay);
        padding-bottom: 10px;
        margin-bottom: 20px;
        font-size: 1.8em;
    }

    #full-explanation h3 {
        color: var(--egyptian-blue);
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 1.3em;
    }

    #full-explanation p {
        margin-bottom: 15px;
    }

    #full-explanation ul {
        margin-bottom: 15px;
        padding-right: 25px;
        list-style: disc;
    }

    #full-explanation li {
        margin-bottom: 10px;
    }

    /* Specific styles for interactive elements */
    .soaking-timer {
        font-size: 3em; /* Larger */
        font-weight: bold;
        color: var(--egyptian-blue);
        position: absolute; /* Center it */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        opacity: 0; /* Start hidden */
        animation: fadeIn 0.5s forwards;
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    /* Styles for the arrangement grid */
    .layer-grid {
        display: grid;
        grid-template-columns: repeat(3, 90px); /* Larger grid cells */
        grid-template-rows: repeat(3, 90px);
        gap: 8px; /* Increased gap */
        border: 2px dashed var(--egyptian-blue); /* Thematic dashed border */
        padding: 15px; /* Increased padding */
        background-color: var(--papyrus-light);
        justify-content: center;
        margin: 0 auto;
        border-radius: 8px;
        transition: border-color 0.5s ease;
        position: relative; /* For absolute children like "strips" */
    }

    .grid-cell-placeholder {
        border: 1px dashed #888;
        background-color: #f0e9d8;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.9em;
        color: #666;
        border-radius: 4px;
    }

    .grid-cell-arranged {
        border: 1px solid var(--egyptian-clay);
        border-radius: 4px;
        position: relative; /* For pseudo-elements or content */
        overflow: hidden;
    }

     /* Representing strips within the grid cells */
     .grid-cell-arranged::before {
         content: '';
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background-color: var(--papyrus-dark); /* Base strip color */
         opacity: 0.7;
     }

     .grid-cell-arranged.vertical::before {
         /* Simulate vertical strips */
         background: repeating-linear-gradient(to right, var(--papyrus-dark), var(--papyrus-dark) 15px, var(--papyrus-light) 15px, var(--papyrus-light) 18px);
     }

     .grid-cell-arranged.horizontal::before {
         /* Simulate horizontal strips */
          background: repeating-linear-gradient(to bottom, var(--papyrus-dark), var(--papyrus-dark) 15px, var(--papyrus-light) 15px, var(--papyrus-light) 18px);
     }

    .grid-arranged-complete {
        border-color: var(--success-color);
        box-shadow: 0 0 10px var(--success-color);
    }


    /* Animation for cutting */
    @keyframes cut-animation {
        0% { transform: translateX(0); }
        50% { transform: translateX(calc(100% - 20px)); } /* Simulate knife moving across */
        100% { transform: translateX(0); }
    }

     .cutting-knife {
         position: absolute;
         top: 50%;
         left: 0;
         transform: translateY(-50%);
         width: 20px;
         height: 50px; /* Represents a simple knife visual */
         background-color: #555;
         clip-path: polygon(0% 0%, 100% 50%, 0% 100%); /* Triangular blade */
         animation: cut-animation 1s ease-in-out forwards;
         opacity: 0;
         display: none; /* Hidden by default */
     }

     .cutting-knife.active {
         display: block;
         opacity: 1;
     }

    /* Animation for pressing */
    @keyframes press-animation {
        0% { transform: translateY(-100px); opacity: 0; }
        50% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(0); opacity: 1; }
    }

     .press-weight {
         position: absolute;
         top: 0;
         left: 50%;
         transform: translate(-50%, -100px); /* Start above display */
         width: 150px;
         height: 50px;
         background-color: #8B4513; /* Wood brown */
         border-radius: 5px;
         box-shadow: 0 10px 20px rgba(0,0,0,0.3);
         opacity: 0;
         animation: press-animation 1s ease-out forwards;
         display: none; /* Hidden by default */
     }
     .press-weight::after {
         content: '';
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         width: 30px;
         height: 70px;
         background-color: #654321; /* Darker wood */
         border-radius: 3px;
     }

      .press-weight.active {
         display: block;
      }

      /* Polishing effect */
      .polishing-effect {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background: radial-gradient(circle, rgba(255,255,150,0.5) 0%, rgba(255,255,150,0) 70%);
          opacity: 0;
          animation: polish-shine 1.5s ease-out forwards;
          display: none;
      }
       @keyframes polish-shine {
            0% { opacity: 0; transform: scale(0.5); }
            50% { opacity: 1; transform: scale(1); }
            100% { opacity: 0; transform: scale(1.2); }
       }
       .polishing-effect.active {
           display: block;
       }


</style>

<button id="explanation-btn">הצג הסבר מורחב</button>

<div id="full-explanation">
    <h2>סוד הפפירוס: מסע אל סדנת הנייר המצרית העתיקה - הסבר מורחב</h2>

    <p>הפפירוס היה עמוד תווך בציוויליזציה המצרית. הוא לא שימש רק לכתיבה, אלא היה חומר גלם חיוני ליצירת סירות קלות, סלים, חבלים, סנדלים, ואפילו מזון ותרופות. אך תפקידו המשמעותי ביותר היה כ"נייר" העולם העתיק, ששינה את פני התקשורת, המנהל והאגירה של ידע.</p>

    <h3>מקור החומר: צמח הגומא (Cyperus papyrus)</h3>
    <p>צמח הגומא, שגדל לגובה של עד 5 מטרים בגדות הנילוס והאזורים הביצתיים, היה מתנה אמיתית מהטבע עבור המצרים. גבעוליו המשולשים והחזקים, אך מלאי ליבה ספוגית ועשירה בשרף טבעי, היו חומר הגלם המושלם. סוד תהליך הייצור נשמר בקנאות על ידי הסדנאות המצריות, מה שהפך את הפפירוס למצרך יקר ורב-ערך שיוצא לכל רחבי אגן הים התיכון.</p>

    <h3>שלבי הייצור המרכזיים:</h3>
    <ul>
        <li>
            <strong>שלב 1: קציר הגבעולים:</strong> קצירת גבעולי הגומא הצעירים והחזקים ביותר, לרוב מהחלק התחתון אך לא קרוב מדי לשורש.
        </li>
        <li>
            <strong>שלב 2: הסרת הקליפה:</strong> קילוף הזהיר של השכבה החיצונית הירוקה והסיבית כדי לחשוף את הליבה הלבנה והעסיסית שבפנים.
        </li>
        <li>
            <strong>שלב 3: פריסה לרצועות:</strong> חיתוך הליבה לאורכה לרצועות דקות ואחידות ככל הניתן. אחידות ודקות הרצועות השפיעו ישירות על איכות הגיליון הסופי.
        </li>
        <li>
            <strong>שלב 4: השריה במים:</strong> טבילת הרצועות במים (לעיתים מי הנילוס עצמו) למשך מספר ימים או שבועות. תהליך זה רכך אותן, סילק סוכרים ועמילנים לא רצויים, והותיר את השרף הטבעי (הליגנין) שהפך לדבק הטבעי של הגיליון. אורך ההשריה השפיע גם על צבע הפפירוס הסופי (השריה קצרה יותר = צבע בהיר יותר).
        </li>
        <li>
            <strong>שלב 5: סידור הגיליון:</strong> סידור קפדני של הרצועות על משטח שטוח בשתי שכבות ניצבות: שכבה אחת לאורך (עם כיוון הגבעול) ושכבה שנייה לרוחב (מאונכת). הרצועות בכל שכבה חופפות מעט זו את זו.
        </li>
        <li>
            <strong>שלב 6: כבישה:</strong> הגיליון המסודר הונח בין פיסות בד סופגות או לבד צמר והוכנס למכבש כבד. המשקל הכבד סחט את עודפי המים וגרם לשרף הטבעי שנותר ברצועות להידבק ולהתמזג זו בזו ליצירת יחידה אחת – גיליון הפפירוס.
        </li>
         <li>
            <strong>שלב 7: ייבוש:</strong> לאחר הכבישה, הגיליון הועבר לייבוש סופי באוויר הפתוח או בשמש.
        </li>
        <li>
            <strong>שלב 8: ליטוש:</strong> ליטוש עדין של פני הגיליון (בעיקר צד אחד, הצד ה"רקטו" עם הרצועות האופקיות) בעזרת אבן חלקה, קונכייה או כלי עצם, ליצירת משטח כתיבה חלק ואחיד, שאינו "שואב" את הדיו. גיליונות יחידים הודבקו זה לזה ליצירת מגילות ארוכות ונוחות לשימוש ולאחסון.
        </li>
    </ul>

    <h3>חשיבות ותפוצה</h3>
    <p>הפפירוס היה בעל חשיבות כלכלית, מנהלית ותרבותית עצומה. ייצורו ומסחרו היו מונופול מלכותי או מדיני במצרים למשך תקופות ארוכות. מגילות פפירוס נשאו מידע על היסטוריה, ספרות, מדע, רפואה, דת וכלכלה, ואפשרו את ניהולה של אימפריה רחבה ואת הפצת הידע בעולם העתיק. הפפירוס שימש כחומר הכתיבה העיקרי באגן הים התיכון עד שהחל להיות מוחלף בהדרגה על ידי הקלף (עור מעובד, עמיד יותר) בסוף העת העתיקה ובתחילת ימי הביניים.</p>
</div>

<script>
    const stepTextElement = document.getElementById('step-text');
    const stepImageElement = document.getElementById('step-image');
    const interactiveElement = document.getElementById('interactive-element');
    const nextStepBtn = document.getElementById('next-step-btn');
    const performActionBtn = document.getElementById('perform-action-btn');
    const explanationBtn = document.getElementById('explanation-btn');
    const fullExplanation = document.getElementById('full-explanation');
    const papyrusDisplay = document.getElementById('papyrus-display');
     const animationOverlay = document.getElementById('papyrus-animation-overlay');


    let currentStepIndex = 0;
    let timerInterval;

    const steps = [
        {
            text: 'שלב 1: ברוכים הבאים לסדנה! נתחיל בקציר הגבעולים הצעירים והחזקים של צמח הגומא מגדות הנילוס.',
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Papyrus_plant.jpg/400px-Papyrus_plant.jpg', // Example: Image of Papyrus plant
            interactive: null,
            actionRequired: false,
            buttonText: 'נקצור את הגבעולים!'
        },
        {
            text: 'שלב 2: נקלף את הקליפה הירוקה החיצונית כדי להגיע אל הליבה הלבנה והרכה שבפנים.',
            image: 'https://via.placeholder.com/400x250?text=שלב+2:+קילוף+הגבעול', // Placeholder with relevant text
            interactive: null,
            actionRequired: false,
             buttonText: 'נמשיך לקילוף'
        },
        {
            text: 'שלב 3: זהירות! עכשיו נפרוס את הליבה לרצועות דקות כחוט. ככל שהרצועות דקות ואחידות יותר, הפפירוס יהיה איכותי יותר.',
            image: 'https://via.placeholder.com/400x250?text=שלב+3:+פריסת+ליבה', // Placeholder with relevant text
            interactive: { type: 'cutting' }, // New interactive type
            actionRequired: true,
             buttonText: 'פורסים רצועות!'
        },
        {
            text: 'שלב 4: נשרה את הרצועות במים למספר ימים. זה מרכך אותן ומשחרר את השרף הטבעי שישמש כדבק.',
            image: null, // No image for this step to focus on interaction
            interactive: { type: 'soaking-timer', duration: 4 }, // Simulate 4 seconds soak
            actionRequired: true,
             buttonText: 'מתחילים בהשריה' // This button will start the timer
        },
        {
            text: 'שלב 5: מסדרים את הרצועות על משטח שטוח בשתי שכבות ניצבות - אופקי ואנכי - בחפיפה קלה.',
            image: null, // No image, focus on grid interaction
            interactive: { type: 'arrangement-grid' }, // Simulate arrangement
            actionRequired: true,
             buttonText: 'סדר רצועות'
        },
        {
            text: 'שלב 6: מפעילים מכבש כבד! זה סוחט את המים ומדביק את הרצועות זו לזו בעזרת השרף הטבעי.',
            image: 'https://via.placeholder.com/400x250?text=שלב+6:+כבישה+במכבש', // Placeholder
            interactive: { type: 'pressing' }, // New interactive type
            actionRequired: true,
             buttonText: 'מפעילים את המכבש'
        },
        {
            text: 'שלב 7: מייבשים את הגיליון המכובס בשמש. זה מאפשר לו להתמצק ולהפוך לחומר יציב.',
            image: 'https://via.placeholder.com/400x250?text=שלב+7:+ייבוש+בשמש', // Placeholder
            interactive: null,
            actionRequired: false,
             buttonText: 'מייבשים בשמש'
        },
        {
            text: 'שלב 8: מלטשים את פני הגיליון בעזרת אבן חלקה לקבלת משטח כתיבה נעים וחלק. הפפירוס מוכן!',
            image: 'https://via.placeholder.com/400x250?text=שלב+8:+ליטוש+הפפירוס', // Placeholder
            interactive: { type: 'polishing' }, // New interactive type
            actionRequired: true, // Make polishing an action
            buttonText: 'מלטשים את הפפירוס'
        },
         {
            text: 'מזל טוב! יצרתם גיליון פפירוס מצרי עתיק. עכשיו אפשר להתחיל לכתוב עליו הירוגליפים או סיפורים!',
            image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Papyrus_%284015667415%29.jpg/400px-Papyrus_%284015667415%29.jpg', // Example: Image of finished papyrus
            interactive: null,
            actionRequired: false,
            isLastStep: true,
             buttonText: 'סיימנו!' // Button won't show, just for consistency
         }
    ];

    function updateStepDisplay(stepIndex) {
        const step = steps[stepIndex];
        stepTextElement.textContent = step.text;

        // Clear previous visuals and interactive elements
        stepImageElement.style.display = 'none';
        stepImageElement.src = '';
        interactiveElement.innerHTML = '';
        interactiveElement.className = ''; // Reset classes
         animationOverlay.innerHTML = ''; // Clear animations

        // Update image
        if (step.image) {
            stepImageElement.src = step.image;
            stepImageElement.style.display = 'block';
             stepImageElement.style.opacity = 0; // Start faded out
             setTimeout(() => stepImageElement.style.opacity = 1, 50); // Fade in
        }

        // Update buttons
        nextStepBtn.style.display = 'none';
        performActionBtn.style.display = 'none';
        performActionBtn.classList.remove('active');


        if (step.interactive) {
            performActionBtn.textContent = step.buttonText;
            performActionBtn.style.display = 'block';
             performActionBtn.classList.add('active'); // Indicate action is needed

            if (step.interactive.type === 'soaking-timer') {
                // Set up timer display but start timer only on action click
                 interactiveElement.className = 'soaking-timer';
                 interactiveElement.textContent = `לחץ "${step.buttonText}" להתחלת ההשריה...`;
                 // Timer starts in performAction
            } else if (step.interactive.type === 'arrangement-grid') {
                 interactiveElement.className = 'layer-grid';
                 // Add 9 placeholder cells to the grid
                 for (let i = 0; i < 9; i++) {
                     const cell = document.createElement('div');
                     cell.className = 'grid-cell-placeholder';
                     interactiveElement.appendChild(cell);
                 }
            } else if (step.interactive.type === 'cutting') {
                // Cutting animation element is added by performAction
                 interactiveElement.textContent = 'לחץ על הכפתור "פורסים רצועות!" כדי לחתוך את הליבה.';
            } else if (step.interactive.type === 'pressing') {
                 interactiveElement.textContent = 'לחץ על הכפתור "מפעילים את המכבש" כדי לכבוש את הגיליון.';
            } else if (step.interactive.type === 'polishing') {
                 interactiveElement.textContent = 'לחץ על הכפתור "מלטשים את הפפירוס" כדי להחליק את המשטח.';
            }

        } else {
            // No interactive element, show next step button unless it's the last step
            if (!step.isLastStep) {
                 nextStepBtn.textContent = step.buttonText || 'הבא';
                 nextStepBtn.style.display = 'block';
            } else {
                 // Last step, maybe a final message or restart option could go here
                 stepTextElement.textContent = step.text; // Ensure final text is shown
                 nextStepBtn.style.display = 'none';
                 performActionBtn.style.display = 'none';
            }
        }
    }

    function goToNextStep() {
        // Clear any ongoing timers or animations before moving
        clearInterval(timerInterval);
        animationOverlay.innerHTML = ''; // Remove animation elements

        if (currentStepIndex < steps.length - 1) {
            currentStepIndex++;
            updateStepDisplay(currentStepIndex);
        }
    }

    function performAction() {
        const step = steps[currentStepIndex];
        if (step.interactive && step.actionRequired) {
             // Hide action button immediately to prevent double clicks
             performActionBtn.style.display = 'none';
             performActionBtn.classList.remove('active');


            if (step.interactive.type === 'soaking-timer') {
                let timeRemaining = step.interactive.duration;
                interactiveElement.textContent = `זמן השריה: ${timeRemaining} שניות`;
                 interactiveElement.style.opacity = 1; // Ensure timer is visible after action

                timerInterval = setInterval(() => {
                    timeRemaining--;
                    interactiveElement.textContent = `זמן השריה: ${timeRemaining} שניות`;
                    if (timeRemaining <= 0) {
                        clearInterval(timerInterval);
                        interactiveElement.textContent = 'השריה הסתיימה!';
                        // After timer, show next step button
                        nextStepBtn.textContent = steps[currentStepIndex + 1]?.buttonText || 'הבא';
                        nextStepBtn.style.display = 'block';
                    }
                }, 1000);

            } else if (step.interactive.type === 'arrangement-grid') {
                // Simulate arrangement process with visual updates
                 const cells = interactiveElement.querySelectorAll('.grid-cell-placeholder');
                 cells.forEach((cell, i) => {
                     // Simple pattern: alternating horizontal/vertical
                     const isVertical = i % 2 === 0;
                     cell.className = 'grid-cell-arranged ' + (isVertical ? 'vertical' : 'horizontal');
                     // No text needed, the pseudo-elements show the pattern
                 });
                 // Add visual indication of completion
                 interactiveElement.classList.add('grid-arranged-complete');

                // After visual update, show next step button after a short delay
                 setTimeout(() => {
                     nextStepBtn.textContent = steps[currentStepIndex + 1]?.buttonText || 'הבא';
                     nextStepBtn.style.display = 'block';
                 }, 1000); // Give a moment for the user to see the result

             } else if (step.interactive.type === 'cutting') {
                 // Simulate cutting animation
                 const knife = document.createElement('div');
                 knife.className = 'cutting-knife active';
                 animationOverlay.appendChild(knife); // Add knife animation over display area

                 // After animation finishes (approx 1 sec), show next step button
                 setTimeout(() => {
                     animationOverlay.innerHTML = ''; // Remove knife
                     interactiveElement.textContent = 'הליבה נפרסה לרצועות דקות, מוכנות להשריה!'; // Add feedback text
                     nextStepBtn.textContent = steps[currentStepIndex + 1]?.buttonText || 'הבא';
                     nextStepBtn.style.display = 'block';
                 }, 1200); // Slightly longer than animation duration

             } else if (step.interactive.type === 'pressing') {
                 // Simulate pressing animation
                 const weight = document.createElement('div');
                 weight.className = 'press-weight active';
                 animationOverlay.appendChild(weight); // Add weight animation

                 // After animation finishes (approx 1 sec), show next step button
                 setTimeout(() => {
                     animationOverlay.innerHTML = ''; // Remove weight
                     interactiveElement.textContent = 'הגיליון נכבש והרצועות הודבקו!'; // Add feedback text
                     nextStepBtn.textContent = steps[currentStepIndex + 1]?.buttonText || 'הבא';
                     nextStepBtn.style.display = 'block';
                 }, 1200); // Slightly longer than animation duration

              } else if (step.interactive.type === 'polishing') {
                 // Simulate polishing animation
                 const shine = document.createElement('div');
                 shine.className = 'polishing-effect active';
                 animationOverlay.appendChild(shine); // Add shine animation

                 // After animation finishes (approx 1.5 sec), show next step button
                 setTimeout(() => {
                     animationOverlay.innerHTML = ''; // Remove shine
                     interactiveElement.textContent = 'הגיליון לוטש והפך למשטח כתיבה מושלם!'; // Add feedback text
                     nextStepBtn.textContent = steps[currentStepIndex + 1]?.buttonText || 'הבא'; // This should now lead to the final step
                     nextStepBtn.style.display = 'block';
                 }, 1700); // Slightly longer than animation duration

             }
        }
    }


    // Event listeners
    nextStepBtn.addEventListener('click', goToNextStep);
    performActionBtn.addEventListener('click', performAction);

    explanationBtn.addEventListener('click', () => {
        const isHidden = fullExplanation.style.display === 'none' || fullExplanation.style.display === '';
        fullExplanation.style.display = isHidden ? 'block' : 'none';
        explanationBtn.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג הסבר מורחב';
    });

    // Initialize the app with the first step
    updateStepDisplay(currentStepIndex);

</script>