---
title: "מסע הקסם לגבן: מכינים גבינת טלמה יוונית כמו פעם"
english_slug: magic-of-curd-making-greek-teleme-cheese
category: "מדע המזון"
tags: [ייצור גבינה, טלמה, יוון, מדע המזון, טכנולוגיות מזון]
---
<h1>מסע הקסם לגבן: מכינים גבינת טלמה יוונית כמו פעם</h1>
<p>איך הופך חלב פשוט - בתוך כלי אחד - לגבינה לבנה, מלוחה ורכה כל כך כמו הטלמה היוונית האותנטית שאנחנו אוהבים? הצטרפו למסע אינטראקטיבי מרתק דרך סדרת תהליכים מדעיים ומסורתיים שהופכים נוזל למוצק... וטעים במיוחד!</p>

<div id="cheeseSimulation">
    <div id="simulationArea">
        <!-- Visual representation of the stages -->
        <div id="milkPot" class="stage-element active">
             <div class="liquid" id="milkLiquid"></div>
        </div>
        <div id="curdBlock" class="stage-element"></div>
        <div id="cutCurd" class="stage-element">
             <div class="whey"></div>
             <div class="curd-cubes"></div>
        </div>
        <div id="cheeseMold" class="stage-element">
             <div class="cheese-in-mold"></div>
        </div>
        <div id="finishedCheese" class="stage-element">
             <div class="final-cheese-block"></div>
        </div>

         <!-- Add visual cues or text overlays -->
         <div class="visual-cue" id="tempCue">🌡️</div>
         <div class="visual-cue" id="bacteriaCue">🦠</div>
         <div class="visual-cue" id="rennetCue">🧪</div>
         <div class="visual-cue" id="knifeCue">🔪</div>
         <div class="visual-cue" id="drainCue">💧</div>
         <div class="visual-cue" id="saltCue">🧂</div>

    </div>
    <div id="interactionArea">
        <!-- Buttons to trigger actions -->
        <button class="action-button" id="pasteurizeMilkButton">⚡ פסטר את החלב</button>
        <button class="action-button" id="addStarterButton" style="display: none;">🦠 הוסף תרבית סטרטר</button>
        <button class="action-button" id="addRennetButton" style="display: none;">🧪 הוסף רנט (אנזים הגבנה)</button>
        <button class="action-button" id="cutCurdButton" style="display: none;">🔪 חתוך את הגבן</button>
        <button class="action-button" id="drainWheyButton" style="display: none;">💧 נקז מי גבן והעבר לתבנית</button>
        <button class="action-button" id="saltCheeseButton" style="display: none;">🧂 המלח את הגבינה</button>
        <button class="action-button" id="finishButton" style="display: none;">📦 אחסן וסיים</button>
         <button class="action-button secondary-button" id="resetButton" style="display: none;">🔄 התחל מחדש</button>
    </div>
    <div id="stageExplanation">
        <!-- Stage specific explanation -->
        <p id="currentExplanation">ברוכים הבאים למטבח הגבינות שלנו! החלב הטרי מוכן למסע.</p>
    </div>
</div>

<button id="toggleExplanationButton" class="secondary-button">הצג הסבר מלא</button>

<div id="fullExplanation" style="display: none;">
    <h2>מסע הגבן: הסבר מעמיק על ייצור גבינת טלמה</h2>
    <p>ייצור גבינה הוא אומנות עתיקה ומדע מרתק. כל שלב משפיע על הטעם, המרקם והארומה של הגבינה הסופית. גבינת טלמה, עם מרקמה הרך וטעמה המלוח האופייני, היא דוגמה נפלאה לתהליך כזה.</p>

    <h3>מקור החלב: הלב הפועם של הגבינה</h3>
    <p>טלמה מיוצרת בדרך כלל מחלב כבשים, עיזים, או שילוב שלהם. סוג החלב קריטי - הוא משפיע על כל מה שקורה אחר כך, בזכות ההבדלים בהרכב השומן, החלבונים והמינרלים. חלב איכותי הוא הבסיס לגבינה משובחת.</p>

    <h3>שלב הפסטור: שומרים על הבריאות בלי לפגוע בטעם</h3>
    <p>כדי להבטיח בטיחות ולהגן מפני חיידקים לא רצויים, החלב עובר פסטור. זהו חימום עדין (כ-72°C ל-15 שניות, או 63°C ל-30 דקות) שמחסל פתוגנים אך שומר בקפדנות על מרכיבי החלב החיוניים להגבנה. זהו צעד הכרחי במסע הבטוח לגבינה.</p>
    <p class="explanation-note"><strong>ההסבר המלא נמשך וכולל פרטים נוספים על כל שלב:</strong> תפקיד חיידקי הסטרטר בבניית הטעם והחומציות, קסם הגבנה בעזרת הרנט והפיכת החלב לנוזל ומוצק, אמנות חיתוך הגבן ואיך גודל הקוביות משפיע על המרקם, דרכי ניקוז מי הגבן (הווי) ועיצוב הגבינה, חשיבות ההמלחה לטעם ולשימור, וכיצד אחסון במי מלח שומר על הטלמה ונותן לה את אופייה הייחודי.</p>
    <!-- Remaining explanation text is assumed to be here but shortened for brevity in this structured output example -->
    <!-- The original text structure is preserved -->
     <h3>הוספת תרביות סטרטר: קסם החיידקים הטובים</h3>
    <p>לאחר הפסטור והקירור לטמפרטורה הנכונה, מוספים את "החברים הטובים" - חיידקי סטרטר מחומצת חלב. החיידקים האלה "אוכלים" את הלקטוז ומייצרים חומצה לקטית. החומציות הגוברת הזו לא רק מכינה את הבמה לרנט, אלא גם מתחילה לבנות את הטעם והארומה המורכבים שמאפיינים את הטלמה.</p>
    <h3>הוספת רנט (אנזים הגבנה): הפיכת הלא ייאמן למציאות</h3>
    <p>זהו רגע הקסם! מוסיפים את אנזים הרנט (בדרך כלל כימוזין), שתפקידו לגרום לחלבון העיקרי בחלב, הקזאין, להתאגד. הרנט חותך את הקזאין במקום ספציפי, גורם לו ליצור רשת תלת-ממדית שכולאת את כל הטוב (שומן, מינרלים) ואת הנוזלים (מי הגבן). כך הופך החלב הנוזלי לג'ל מוצק ורוטט - הגבן.</p>
    <h3>חיתוך הגבן: פיסול המרקם העתידי</h3>
    <p>אחרי שהגבן התמצק יפה, מגיע שלב "הניתוח העדין". הגבן נחתך לקוביות קטנות באמצעות סכיני גבן מיוחדים. למה? כדי להגדיל משמעותית את שטח הפנים ולאפשר למי הגבן (הווי) להתנקז ביעילות החוצה. גודל החיתוך הוא סוד מקצועי - קוביות קטנות יותר משמעותן ניקוז רב יותר וגבינה יבשה וקשה יותר. קוביות גדולות יותר ישאירו יותר לחות ויתנו גבינה רכה ועסיסית יותר.</p>
    <h3>ניקוז מי הגבן (ווי): נפרדים מהנוזלים המיותרים</h3>
    <p>השלב הזה הוא בעצם ההפרדה הגדולה. הגבן המוצק מופרד ממי הגבן הנוזליים. בשיטות מסורתיות לטלמה, לעיתים קרובות אורזים את הגבן בשקי בד ותולים אותם, ונותנים לכבידה לעשות את שלה ולנקז את המים. אפשר גם להשתמש בתבניות מחוררות ולעיתים להפעיל לחץ קל. כמות המים שמנוקזת קובעת ישירות את הלחות והמרקם הסופי של הגבינה. מי הגבן עצמם לא הולכים לפח! מהם מכינים, למשל, גבינת ריקוטה או משקאות בריאות.</p>
    <h3>המלחה: הקסם שמשמר ומוסיף טעם</h3>
    <p>המלחה בטלמה היא קריטית. היא תורמת לטעם המוכר, משמרת את הגבינה (המלח מעכב גדילת חיידקים לא רצויים), סופחת לחות נוספת ומשפיעה על המרקם. אפשר למלוח יבש (לפזר מלח ישירות) או רטוב (להשרות בתמיסת מי מלח). בטלמה לרוב עוברים לשלב הבריין בשלב האחסון העיקרי.</p>
    <h3>עיצוב ואחסון במי מלח: הבית של הטלמה</h3>
    <p>אחרי הניקוז (ולעיתים ההמלחה היבשה), הגבן מעוצב לגושים מלבניים בתבניות. המאפיין הבולט ביותר של טלמה הוא אחסונה בתוך תמיסת מי מלח (בריין). אחסון זה לא רק שומר על טריותה לאורך זמן, מונע התייבשות וממשיך להעניק לה טעם מלוח עמוק, אלא גם מאפשר לגבינה "להתבגר" בעדינות בסביבה מבוקרת. זה הבית שלה, ושם היא מפתחת את אופייה הסופי.</p>
</div>

<style>
    /* General Setup & Typography */
    #cheeseSimulation {
        direction: rtl;
        font-family: 'Heebo', sans-serif; /* Using a modern Hebrew-friendly font */
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
        padding: 25px;
        border: none; /* Remove basic border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom, #f0f4f8, #e8ebef); /* Subtle gradient background */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
    }

    h1 {
        color: #2c3e50; /* Darker shade */
        text-align: center;
        margin-bottom: 15px;
    }

    p {
         color: #34495e; /* Slightly lighter dark */
         line-height: 1.6;
    }

    /* Simulation Area */
    #simulationArea {
        width: 100%;
        max-width: 550px; /* Slightly wider */
        height: 350px; /* Slightly taller */
        background-color: #ffffff; /* Clean white background */
        border: 2px solid #bdc3c7; /* Lighter, cleaner border */
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.05); /* Inner shadow */
    }

    .stage-element {
        position: absolute;
        width: 90%;
        height: 90%;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        transition: opacity 0.6s ease-in-out, transform 0.6s ease-in-out; /* Smooth transitions */
        opacity: 0; /* Start hidden */
        transform: scale(0.95); /* Slightly smaller initially */
        display: none; /* Hide by default, JS will show */
        justify-content: center; /* Center contents like curd text */
        align-items: center;
    }

    .stage-element.active {
        opacity: 1;
        transform: scale(1);
        display: flex; /* Use flex to center content */
    }

    /* Visual Elements within Stages */
    #milkPot {
         background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><rect width="300" height="300" fill="none"/></svg>'); /* Transparent SVG base */
         position: relative;
         width: 80%;
         height: 80%;
    }

    .liquid {
        position: absolute;
        bottom: 0;
        left: 10%;
        width: 80%;
        height: 90%; /* Starts full */
        background: linear-gradient(to top, #ffffff, #f2f2f2); /* Milk gradient */
        border: 1px solid #ccc;
        border-bottom-left-radius: 40% 10%;
        border-bottom-right-radius: 40% 10%;
        border-top-left-radius: 5% 2%;
        border-top-right-radius: 5% 2%;
         box-shadow: inset 0 -5px 10px rgba(0,0,0,0.1);
        transition: height 1s ease-in-out, background 0.6s ease-in-out;
    }

     #milkPot.pasteurized .liquid {
         background: linear-gradient(to top, #ecf0f1, #dcdfe4); /* Slight color change for pasteurized */
     }

     #milkPot.starter-added .liquid {
         /* Maybe subtle ripple or color change */
         animation: pulse 1s infinite alternate;
     }
     @keyframes pulse {
         from { transform: scale(1); }
         to { transform: scale(1.01); }
     }


    #curdBlock {
        background: linear-gradient(to bottom right, #fcf3cf, #f8e7a8); /* Creamy yellow gradient */
        border: 2px solid #f1c40f; /* Mustard yellow */
        width: 70%; /* Larger curd block */
        height: 70%;
        border-radius: 8px;
        font-size: 2em;
        color: #8b6f1b; /* Darker yellow text */
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #cutCurd {
        position: relative;
        background-color: #e0f7fa; /* Whey color */
        border: 2px solid #03a9f4;
        width: 85%; /* Wider area for cubes + whey */
        height: 85%;
        border-radius: 8px;
        overflow: hidden;
        display: flex; /* To position internal elements */
        justify-content: center;
        align-items: center;
    }

    #cutCurd .whey {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: #e0f7fa; /* Light blue */
        z-index: 1;
    }
    #cutCurd .curd-cubes {
         position: absolute;
         top: 10%; left: 10%;
         width: 80%; height: 80%;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="none"/><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#fcf3cf" stroke="#f1c40f" stroke-width="0.5"/></pattern><rect width="100" height="100" fill="url(%23grid)"/></svg>'); /* SVG grid pattern for cubes */
        background-size: 100px 100px; /* Adjust size as needed */
         z-index: 2;
         transition: transform 1s ease-in-out;
    }

     #cutCurd.drained .whey {
         height: 20%; /* Simulate draining whey */
         transition: height 1.5s ease-in-out;
     }
     #cutCurd.drained .curd-cubes {
          transform: translateY(20px); /* Cubes settle */
     }


    #cheeseMold {
         background-color: #ffffff;
         border: 2px solid #95a5a6; /* Silver */
         width: 60%; /* Mold shape */
         height: 50%;
         border-radius: 6px;
         position: relative;
         overflow: hidden;
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    #cheeseMold .cheese-in-mold {
        position: absolute;
        bottom: 0; left: 5%;
        width: 90%;
        height: 95%; /* Almost filling mold */
        background-color: #ecf0f1; /* Off-white cheese color */
        border-radius: 4px;
        transition: background-color 0.8s ease-in-out, box-shadow 0.8s ease-in-out;
    }

     #cheeseMold.salted .cheese-in-mold {
         background-color: #dcdfe4; /* Slight grey tint from salt */
         box-shadow: inset 0 0 15px rgba(0,0,0,0.2); /* Simulate salt crystallization appearance */
     }


    #finishedCheese {
        background-color: #ffffff;
        border: 2px solid #27ae60; /* Emerald green for finished product */
        width: 55%; /* Final block size */
        height: 45%;
        border-radius: 6px;
        box-shadow: 0 8px 16px rgba(39, 174, 96, 0.2); /* Green shadow */
        position: relative;
    }
     #finishedCheese .final-cheese-block {
          width: 100%; height: 100%;
          background: linear-gradient(to bottom, #ecf0f1, #bdc3c7); /* Gradient for depth */
          border-radius: 6px;
     }
     #finishedCheese::after {
         content: '✅'; /* Checkmark icon */
         position: absolute;
         top: 10px;
         left: 10px;
         font-size: 2em;
         color: #27ae60;
         animation: fadeIn 1s ease-out;
     }

     /* Visual Cues */
     .visual-cue {
         position: absolute;
         font-size: 2em;
         opacity: 0;
         transition: opacity 0.5s ease-out, transform 0.5s ease-out;
         pointer-events: none; /* Don't block clicks */
         z-index: 10;
         transform: translate(0, 0);
     }
     #tempCue { top: 10%; left: 10%; }
     #bacteriaCue { top: 30%; left: 80%; }
     #rennetCue { top: 50%; left: 20%; }
     #knifeCue { top: 40%; left: 50%; }
     #drainCue { top: 70%; left: 70%; }
     #saltCue { top: 20%; left: 30%; }

     .visual-cue.active {
         opacity: 1;
         transform: translate(10px, -10px); /* Small float animation */
     }


    /* Interaction Area */
    #interactionArea {
        margin-bottom: 20px;
        text-align: center;
        min-height: 50px; /* Reserve space */
    }

    .action-button {
        padding: 12px 20px; /* Larger buttons */
        margin: 5px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #2ecc71; /* Brighter green */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s ease, transform 0.1s active;
        box-shadow: 0 4px 6px rgba(46, 204, 113, 0.2);
        font-weight: bold;
    }

     .action-button:hover {
        background-color: #27ae60; /* Darker green */
     }

     .action-button:active {
         transform: scale(0.98); /* Press effect */
         box-shadow: 0 2px 4px rgba(46, 204, 113, 0.2);
     }

     .secondary-button {
         background-color: #95a5a6; /* Grey */
         box-shadow: 0 4px 6px rgba(149, 165, 166, 0.2);
     }
     .secondary-button:hover {
         background-color: #7f8c8d; /* Darker grey */
     }
      .secondary-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(149, 165, 166, 0.2);
     }


    #resetButton {
         background-color: #e74c3c; /* Red */
         box-shadow: 0 4px 6px rgba(231, 76, 60, 0.2);
    }
    #resetButton:hover {
         background-color: #c0392b; /* Darker Red */
    }


    #stageExplanation {
        margin-top: 15px;
        padding: 18px;
        border: 1px dashed #3498db; /* Brighter blue dashed */
        border-radius: 8px;
        background-color: #ecf0f1; /* Very light grey-blue */
        min-height: 70px; /* Slightly taller */
        width: 100%;
        max-width: 550px;
        text-align: center;
        font-size: 1em; /* Slightly larger text */
        color: #2c3e50;
    }

    #fullExplanation {
        margin-top: 30px;
        padding: 25px;
        border: none;
        border-radius: 12px;
        background: linear-gradient(to bottom, #e0e8f0, #d7dee6); /* Gradient for explanation */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
        direction: rtl;
        color: #34495e;
    }

    #fullExplanation h2 {
        color: #2c3e50;
        margin-top: 0;
        margin-bottom: 10px;
        text-align: center;
    }
     #fullExplanation h3 {
        color: #3498db; /* Blue for subheadings */
        margin-top: 20px;
        margin-bottom: 8px;
        border-bottom: 1px solid #bdc3c7; /* Subtle separator */
        padding-bottom: 4px;
     }

    #fullExplanation p {
        line-height: 1.7;
        margin-bottom: 12px;
    }

     .explanation-note {
         font-style: italic;
         color: #7f8c8d;
         margin-top: 15px;
         padding-top: 10px;
         border-top: 1px dashed #bdc3c7;
     }


    #toggleExplanationButton {
        display: block;
        margin: 25px auto; /* More margin */
        padding: 12px 25px; /* Larger */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #f39c12; /* Orange */
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s active;
         box-shadow: 0 4px 6px rgba(243, 156, 18, 0.2);
         font-weight: bold;
    }

    #toggleExplanationButton:hover {
         background-color: #e67e22; /* Darker orange */
    }
    #toggleExplanationButton:active {
         transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(243, 156, 18, 0.2);
    }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const simulationArea = document.getElementById('simulationArea');
        const milkPot = document.getElementById('milkPot');
        const milkLiquid = document.getElementById('milkLiquid');
        const curdBlock = document.getElementById('curdBlock');
        const cutCurd = document.getElementById('cutCurd');
        const cheeseMold = document.getElementById('cheeseMold');
        const finishedCheese = document.getElementById('finishedCheese');

        const pasteurizeMilkButton = document.getElementById('pasteurizeMilkButton');
        const addStarterButton = document.getElementById('addStarterButton');
        const addRennetButton = document.getElementById('addRennetButton');
        const cutCurdButton = document.getElementById('cutCurdButton');
        const drainWheyButton = document.getElementById('drainWheyButton');
        const saltCheeseButton = document.getElementById('saltCheeseButton');
        const finishButton = document.getElementById('finishButton');
        const resetButton = document.getElementById('resetButton');

        const tempCue = document.getElementById('tempCue');
        const bacteriaCue = document.getElementById('bacteriaCue');
        const rennetCue = document.getElementById('rennetCue');
        const knifeCue = document.getElementById('knifeCue');
        const drainCue = document.getElementById('drainCue');
        const saltCue = document.getElementById('saltCue');


        const currentExplanation = document.getElementById('currentExplanation');
        const fullExplanationDiv = document.getElementById('fullExplanation');
        const toggleExplanationButton = document.getElementById('toggleExplanationButton');

        let currentStage = 0; // 0: Initial, 1: Pasteurization, 2: Starter, 3: Rennet, 4: Cut, 5: Drain, 6: Salt, 7: Finish/Store, 8: End

        const stages = [
            { // Stage 0: Initial Milk
                element: milkPot,
                actionButton: pasteurizeMilkButton,
                explanation: "החלב הטרי ממתין. נתחיל עם צעד קריטי לבטיחות: הפסטור.",
                visualUpdate: () => {
                    // Initial state handled by CSS active class on load
                },
                cue: null
            },
            { // Stage 1: Pasteurization
                element: milkPot,
                actionButton: addStarterButton,
                explanation: "החלב עבר פסטור! כעת יש לקרר ולהוסיף את חיידקי הסטרטר.",
                visualUpdate: () => {
                    milkPot.classList.add('pasteurized'); // Change milk appearance
                    milkLiquid.style.height = '85%'; // Simulate slight volume change or cooling effect
                    showCue(tempCue);
                },
                 cue: bacteriaCue // Next cue
            },
            { // Stage 2: Add Starter
                element: milkPot,
                actionButton: addRennetButton,
                explanation: "החיידקים עובדים! הם מורידים את החומציות ומפתחים טעם. עכשיו זמן לקסם ההגבנה.",
                 visualUpdate: () => {
                    milkPot.classList.add('starter-added'); // Indicate bacterial activity
                     showCue(bacteriaCue);
                 },
                 cue: rennetCue // Next cue
            },
             { // Stage 3: Add Rennet
                element: curdBlock,
                actionButton: cutCurdButton,
                explanation: "וואו! הרנט עבד! החלב כולו התגבן והפך לגוש אחד מוצק. מוכנים לחתוך?",
                 visualUpdate: () => {
                    milkPot.classList.remove('active', 'pasteurized', 'starter-added');
                    milkPot.style.display = 'none';
                    milkLiquid.style.height = '90%'; // Reset for potential restart

                    curdBlock.classList.add('active');
                    curdBlock.textContent = "גבן מוצק";
                    showCue(rennetCue);
                 },
                 cue: knifeCue // Next cue
            },
             { // Stage 4: Cut Curd
                element: cutCurd,
                actionButton: drainWheyButton,
                explanation: "הגבן נחתך לקוביות. עכשיו מי הגבן יכולים להתנקז בקלות ולחשוף את הגבינה.",
                 visualUpdate: () => {
                    curdBlock.classList.remove('active');
                    curdBlock.style.display = 'none';

                    cutCurd.classList.add('active');
                    showCue(knifeCue);
                 },
                 cue: drainCue // Next cue
            },
            { // Stage 5: Drain Whey
                element: cheeseMold,
                actionButton: saltCheeseButton,
                explanation: "מי הגבן נוקזו! הגבן הועבר לתבנית לקבלת צורה. מה השלב הבא?",
                 visualUpdate: () => {
                    cutCurd.classList.remove('active');
                    cutCurd.classList.add('drained'); // Trigger drain animation
                    // Wait for animation before changing element
                    setTimeout(() => {
                        cutCurd.style.display = 'none';
                        cheeseMold.classList.add('active');
                        showCue(drainCue);
                    }, 1000); // Match animation duration
                 },
                 cue: saltCue // Next cue
            },
            { // Stage 6: Salt Cheese
                element: cheeseMold,
                actionButton: finishButton,
                explanation: "הגבינה הומלחה! המלח מוסיף המון טעם וגם עוזר לשמור עליה לאורך זמן.",
                 visualUpdate: () => {
                    cheeseMold.classList.add('salted'); // Indicate salting visually
                    showCue(saltCue);
                 },
                 cue: null // No cue after this
            },
             { // Stage 7: Finish/Store
                element: finishedCheese,
                actionButton: null, // No button needed after last action
                explanation: "תהליך ייצור גבינת הטלמה הסתיים! הגבינה מוכנה לאחסון במי מלח וליהנות ממנה.",
                 visualUpdate: () => {
                     cheeseMold.classList.remove('active', 'salted');
                     cheeseMold.style.display = 'none';
                     finishedCheese.classList.add('active');
                 },
                 cue: null
            }
        ];

         function showCue(cueElement) {
             if (cueElement) {
                 cueElement.classList.add('active');
                 // Hide cue after a short delay
                 setTimeout(() => {
                     cueElement.classList.remove('active');
                 }, 1500); // Show for 1.5 seconds
             }
         }


        function updateSimulation(stageIndex) {
            // Hide all elements and buttons first, reset visual states
            [milkPot, curdBlock, cutCurd, cheeseMold, finishedCheese].forEach(el => {
                el.classList.remove('active');
                el.style.display = 'none';
            });
             // Reset states for potential restart
             milkPot.classList.remove('pasteurized', 'starter-added');
             milkLiquid.style.height = '90%';
             curdBlock.textContent = "";
             cutCurd.classList.remove('drained');
             cheeseMold.classList.remove('salted');


            [pasteurizeMilkButton, addStarterButton, addRennetButton, cutCurdButton, drainWheyButton, saltCheeseButton, finishButton, resetButton].forEach(btn => btn.style.display = 'none');


            if (stageIndex < stages.length) {
                const currentStageData = stages[stageIndex];
                currentStageData.element.style.display = 'flex'; // Show the element
                // Allow element to become visible before adding active class for transition
                requestAnimationFrame(() => {
                     currentStageData.element.classList.add('active');
                });


                if (currentStageData.actionButton) {
                     currentStageData.actionButton.style.display = 'block';
                } else {
                     // If no action button, show reset
                    resetButton.style.display = 'block';
                }
                currentExplanation.textContent = currentStageData.explanation;

                 // Show cue associated with the *next* step if it exists
                 if (stageIndex + 1 < stages.length && stages[stageIndex + 1].cue) {
                      // Cue is shown when the *current* action is clicked and successful
                      // This is handled in the button listener now
                 }


            } else {
                // End of simulation
                finishedCheese.style.display = 'flex'; // Keep final cheese visible
                 requestAnimationFrame(() => {
                    finishedCheese.classList.add('active');
                 });
                currentExplanation.textContent = "המסע הושלם! למדת את השלבים המופלאים בייצור גבינת טלמה. עיין בהסבר המלא לפרטים נוספים.";
                resetButton.style.display = 'block'; // Show reset button at the end
            }
        }

        function resetSimulation() {
             currentStage = 0;
             updateSimulation(currentStage);
        }


        // Add event listeners to buttons
        stages.forEach((stage, index) => {
            if (stage.actionButton) {
                stage.actionButton.addEventListener('click', () => {
                    if (currentStage === index) {
                        // Disable button temporarily to prevent double clicks
                        stage.actionButton.disabled = true;
                        stage.visualUpdate();

                         // Show the cue associated with the stage action *after* the action is triggered
                         if (stage.cue) {
                             showCue(stage.cue);
                         }


                        // Wait a moment for visual update/animation before moving to next stage
                        setTimeout(() => {
                            currentStage++;
                            updateSimulation(currentStage);
                            stage.actionButton.disabled = false; // Re-enable button if it reappears (it won't in this sequential model)
                        }, 800); // Adjust delay based on animation duration
                    }
                });
            }
        });

        resetButton.addEventListener('click', resetSimulation);

        // Initialize the simulation
        updateSimulation(currentStage);

        // Toggle full explanation
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = fullExplanationDiv.style.display === 'none';
            fullExplanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מלא' : 'הצג הסבר מלא';
            // Scroll to explanation if revealing it
            if (!isHidden) {
                 fullExplanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });

         // Ensure initial state is correct on load
         milkPot.style.display = 'flex'; // Start with the milk pot visible
         milkPot.classList.add('active');
    });
</script>
```