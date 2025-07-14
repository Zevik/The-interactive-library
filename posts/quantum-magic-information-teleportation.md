---
title: "מסע מדהים: טלפורטציה קוונטית של מידע"
english_slug: quantum-magic-information-teleportation
category: "מדעים מדויקים / פיזיקה"
tags: [פיזיקה קוונטית, טלפורטציה, שזירה קוונטית, מצב קוונטי, מחשוב קוונטי, קיוביטים]
---
# מסע מדהים: טלפורטציה קוונטית של מידע
דמיינו לרגע שאתם יכולים לשגר מידע ממקום למקום, בלי לשלוח את החומר עצמו דרך המרחב! זה נשמע כמו מסע כוכבים, נכון? ובכן, בעולם המופלא של פיזיקה קוונטית, מושג דומה לגמרי, המכונה טלפורטציה קוונטית, הוא לא רק תיאורטי אלא גם מציאותי לחלוטין - הוכח בניסויים שוב ושוב.

אבל איך זה עובד? איך אפשר "להעביר" את המצב הקוונטי העדין של חלקיק אחד לחלקיק אחר, רחוק ממנו, מבלי ששום דבר פיזי יעבור ביניהם? האפליקציה האינטראקטיבית הזו מזמינה אתכם לצלול לתוך התהליך המרתק הזה, צעד אחר צעד, ולגלות את הקסם האמיתי מאחורי הטלפורטציה הקוונטית. שחקו, התנסו, וראו בעצמכם איך המידע הקוונטי עובר את המרחק באמצעות כוחה של השזירה!

<div id="teleportation-sim">
    <div class="person" id="alice">
        <h2>אליס (השולחת)</h2>
        <div class="qubit-container">
            <div class="qubit" id="qubitA"><div class="state-viz">?</div></div>
            <div class="label">המצב הקוונטי לטלפורט</div>
            <div class="state-selector">
                בחר מצב התחלתי לקיוביט A:<br>
                <button class="state-btn" data-state="0">|0⟩</button>
                <button class="state-btn" data-state="1">|1⟩</button>
                <button class="state-btn" data-state="plus">|+⟩</button>
                <button class="state-btn" data-state="minus">|-⟩</button>
            </div>
        </div>
        <div class="qubit-container">
            <div class="qubit entangled" id="qubitB"><div class="state-viz">שזור</div></div>
             <div class="label">קיוביט B (שזור עם C)</div>
        </div>
        <button class="sim-btn" id="bellMeasureBtn" disabled>1. בצע מדידת בל על A ו-B</button>
        <div class="sim-status">תוצאת מדידת בל: <span id="bellResult"></span></div>
        <button class="sim-btn" id="sendClassicalBtn" disabled>2. שלח מידע קלאסי לבוב</button>
        <div class="sim-status">מידע קלאסי שנשלח: <span id="classicalBits"></span></div>
    </div>

    <div class="classical-channel">
        <div class="channel-icon"><img src="/assets/svg/classical-channel.svg" alt="ערוץ קלאסי"></div>
        <div class="bits-transfer" id="bitsTransfer"></div>
        <div class="channel-label">ערוץ תקשורת קלאסי</div>
    </div>

    <div class="person" id="bob">
        <h2>בוב (המקבל)</h2>
        <div class="qubit-container">
            <div class="qubit entangled" id="qubitC"><div class="state-viz">שזור</div></div>
            <div class="label">קיוביט C (שזור עם B)</div>
        </div>
        <button class="sim-btn" id="applyCorrectionBtn" disabled>3. בצע פעולה מתקנת על C</button>
         <div class="sim-status">פעולה מיושמת על C: <span id="appliedGate"></span></div>
         <div class="sim-status">מצב קיוביט C כעת: <span id="finalStateText">?</span></div>
        <button class="sim-btn" id="measureCBtn" disabled>4. מדוד את קיוביט C הסופי</button>
         <div class="sim-status">תוצאת מדידת C: <span id="finalMeasurement"></span></div>
         <div class="sim-status final-check">האם מצב C תואם למצב A ההתחלתי? <span id="matchStatus">?</span></div>
    </div>

     <div class="entanglement-link">
         <div class="entanglement-particles"></div>
     </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700&display=swap');

    #teleportation-sim {
        font-family: 'Heebo', sans-serif;
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        gap: 30px; /* Increased gap */
        align-items: start;
        justify-items: center;
        padding: 30px; /* Increased padding */
        border: none; /* Remove border */
        border-radius: 12px; /* Rounded corners */
        background: linear-gradient(135deg, #eef2f7 0%, #cce3f1 100%); /* Soft gradient background */
        position: relative;
        overflow: hidden;
        min-height: 550px; /* More height */
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); /* Add shadow */
    }

     #teleportation-sim h2 {
         margin-top: 0;
         color: #0d47a1; /* Darker blue */
         font-weight: 700;
         font-size: 1.5em;
         text-align: center;
         width: 100%;
     }

    .person {
        background-color: #ffffff; /* White background for containers */
        padding: 25px; /* Increased padding */
        border-radius: 10px; /* Rounded corners */
        text-align: center;
        width: 100%;
        max-width: 350px; /* Wider */
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* Soft shadow */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .qubit-container {
        margin-bottom: 25px; /* Increased spacing */
        width: 100%; /* Take full width */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .qubit {
        width: 100px; /* Larger qubits */
        height: 100px; /* Larger qubits */
        border: 3px solid #007bff; /* Primary blue border */
        border-radius: 15px; /* More rounded */
        margin: 15px auto; /* Increased margin */
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.2em;
        background-color: #e3f2fd; /* Light blue background */
        transition: all 0.4s ease-in-out; /* Smooth transitions */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Softer shadow */
        color: #0d47a1; /* Dark blue text */
        position: relative; /* For animations */
    }

     .qubit .state-viz {
         width: 100%;
         height: 100%;
         display: flex;
         flex-direction: column; /* Allow content to stack if needed */
         align-items: center;
         justify-content: center;
         font-size: 2.5em; /* Larger state text */
         font-weight: 500;
         color: #0d47a1;
     }

    /* Specific state visualizations */
    .qubit[data-state="0"] .state-viz::before { content: '↑'; color: #4CAF50; } /* Green Up Arrow */
    .qubit[data-state="1"] .state-viz::before { content: '↓'; color: #f44336; } /* Red Down Arrow */
    .qubit[data-state="plus"] .state-viz::before { content: '→'; color: #FFC107; } /* Amber Right Arrow */
    .qubit[data-state="minus"] .state-viz::before { content: '←'; color: #FF9800; } /* Orange Left Arrow */
     .qubit[data-state="entangled"] .state-viz { font-size: 1.2em; } /* Smaller text for "שזור" */


    .qubit.measured {
        border-color: #9e9e9e; /* Grey border */
        background-color: #f5f5f5; /* Light grey background */
        color: #757575; /* Grey text */
        box-shadow: none;
        opacity: 0.8;
    }

     .qubit.entangled {
         border-color: #673ab7; /* Deep purple */
         background-color: #ede7f6; /* Light purple */
         color: #4527a0; /* Dark purple text */
     }

     .label {
         font-size: 0.9em;
         color: #555;
         margin-top: 5px; /* Increased spacing */
         font-weight: 500;
     }

     .state-selector {
         margin-top: 15px; /* Increased spacing */
         font-size: 0.95em;
         line-height: 1.5;
         text-align: center;
     }

     .state-selector button {
         margin: 3px; /* Increased margin */
         padding: 6px 12px; /* Adjusted padding */
         cursor: pointer;
         border: 1px solid #007bff;
         border-radius: 4px;
         background-color: #e3f2fd;
         color: #007bff;
         font-size: 0.9em;
         transition: background-color 0.2s, border-color 0.2s, transform 0.1s;
     }
     .state-selector button:hover:not(:disabled) {
         background-color: #cce3f1;
         border-color: #0056b3;
     }
     .state-selector button:active:not(:disabled) {
         transform: scale(0.95);
     }
      .state-selector button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
     }


    .sim-btn {
        margin-top: 20px; /* Increased margin */
        padding: 12px 20px; /* Increased padding */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        background-color: #1e88e5; /* Bright blue */
        color: white;
        border: none;
        border-radius: 6px; /* More rounded */
        transition: background-color 0.3s, transform 0.1s ease-in-out;
        font-weight: 500;
        width: 100%; /* Full width */
        max-width: 280px; /* Max width for buttons */
    }

    .sim-btn:disabled {
        background-color: #bdbdbd; /* Greyed out */
        cursor: not-allowed;
        box-shadow: none;
    }

    .sim-btn:hover:not(:disabled) {
        background-color: #0d47a1; /* Darker blue on hover */
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

     .sim-btn:active:not(:disabled) {
         transform: scale(0.98);
     }

    .sim-status {
        margin-top: 10px;
        min-height: 1.4em; /* Reserve space */
        font-size: 0.95em;
        color: #333;
    }

    .final-check {
        font-weight: 700;
        color: #1a237e; /* Darker blue */
        margin-top: 15px;
    }
     .final-check span {
         font-weight: normal;
         color: #333;
     }

    .classical-channel {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 100px; /* Adjust to align vertically */
        width: 150px; /* Width for channel area */
    }

     .channel-icon img {
         width: 60px; /* Larger icon */
         filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.1));
     }

     .channel-label {
         font-size: 0.85em;
         color: #555;
         margin-top: 8px; /* Increased spacing */
         font-weight: 500;
     }

    .bits-transfer {
        width: 120px; /* Width of transfer area */
        height: 25px; /* Height of transfer area */
        margin-top: 15px; /* Increased spacing */
        text-align: center;
        font-weight: 700;
        color: #ff5722; /* Orange/Red for classical bits */
        font-size: 1.1em;
        position: relative; /* For animation */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Entanglement link visual */
    .entanglement-link {
        position: absolute;
        top: 50%; /* Center vertically */
        left: 50%;
        /* Calculate horizontal position and width */
        /* Assuming person max-width 350px, gap 30px */
        /* Alice right edge is roughly 50% - (max-width/2 + gap/2) */
        /* Bob left edge is roughly 50% + (max-width/2 + gap/2) */
        /* Total width is roughly viewport width - (max-width + gap) * 2 */
        /* Let's approximate placement visually */
        transform: translate(-50%, -50%);
        width: calc(100% - 780px); /* Adjusted based on approx max width and gap */
        max-width: 300px; /* Don't get too wide on large screens */
        height: 4px; /* Thicker line */
        background: linear-gradient(to right, #673ab7, #9c27b0, #e040fb); /* Purple gradient */
        border-radius: 2px;
        z-index: -1;
        opacity: 0.7;
        box-shadow: 0 0 10px rgba(156, 39, 176, 0.5); /* Glow effect */
        transition: opacity 0.5s ease-in-out;
    }
     .qubitC.measured + .entanglement-link {
         opacity: 0; /* Fade out entanglement link when C is measured */
     }


    @keyframes particleFlow {
        0% { transform: translateX(0); opacity: 0.5; }
        50% { opacity: 1; }
        100% { transform: translateX(100%); opacity: 0.5; }
    }

     .entanglement-particles {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         overflow: hidden;
     }

     .entanglement-particles::before, .entanglement-particles::after {
         content: '';
         position: absolute;
         top: 50%;
         width: 8px;
         height: 8px;
         background-color: #ffffff; /* White particles */
         border-radius: 50%;
         transform: translateY(-50%);
         animation: particleFlow 3s linear infinite; /* Animation */
     }
     .entanglement-particles::after {
         animation-delay: 1.5s; /* Stagger animation */
     }


    #toggleExplanationBtn {
        display: block; /* Make it a block button */
        width: fit-content; /* Fit button width to content */
        margin: 30px auto 15px auto; /* Center button and add spacing */
        padding: 10px 20px;
        font-size: 1em;
        background-color: #5c6bc0; /* Indigo */
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

     #toggleExplanationBtn:hover {
         background-color: #3f51b5; /* Darker indigo */
     }

     #explanation {
         margin-top: 20px;
         padding: 25px; /* Increased padding */
         border: none;
         border-radius: 12px;
         background-color: #e8f5e9; /* Light green background for explanation */
         box-shadow: 0 5px 15px rgba(0,0,0,0.1);
         line-height: 1.7; /* More readable line height */
         font-size: 1.05em;
     }

     #explanation h2, #explanation h3 {
         color: #2e7d32; /* Dark green for headings */
         margin-bottom: 15px;
     }

     #explanation ul, #explanation ol {
         margin-bottom: 15px;
         padding-left: 20px;
     }
     #explanation li {
         margin-bottom: 8px;
     }

      #explanation strong {
          color: #1b5e20; /* Even darker green */
      }

      .explanation-toggle {
           text-align: center;
      }
</style>

<button id="toggleExplanationBtn">הצג את סוד הטלפורטציה הקוונטית!</button>

<div id="explanation" style="display: none;">
    <h2>מה זה בעצם טלפורטציה קוונטית?</h2>
    <p>שכחו מ"מסע בין כוכבים"! טלפורטציה קוונטית היא לא העברת אדם או חפץ, אלא העברת <strong>מצב קוונטי</strong> - האוסף המדויק של המאפיינים הייחודיים של חלקיק (כמו ספין או קיטוב), ממקום אחד למקום אחר, ללא צורך שהחלקיק המקורי עצמו יעבור במרחב. זה כאילו אתם מעבירים את "הוראות ההפעלה" המדויקות של חלקיק אחד, כדי ליצור במקום אחר חלקיק זהה לו לחלוטין מבחינה קוונטית.</p>

    <h2>השחקנים הראשיים במחזה הקוונטי</h2>
    <p>כדי שהקסם הזה יקרה, אנחנו זקוקים לשלושה דברים:</p>
    <ul>
        <li><strong>קיוביט המקור (אצל אליס):</strong> חלקיק A, שבתוכו נמצא המצב הקוונטי הסודי שאותו אנחנו רוצים לשגר (נסמן את מצבו כ- |ψ⟩A).</li>
        <li><strong>זוג קיוביטים שזורים (אחד אצל אליס, אחד אצל בוב):</strong> שני חלקיקים, B ו-C, שנולדו יחד במצב מיוחד הנקרא "שזירה קוונטית" (Entanglement). קיוביט B נמצא אצל אליס יחד עם קיוביט A, וקיוביט C נמצא אצל בוב, שיכול להיות מרוחק מאוד. שזירה היא הקשר הקוונטי העמוק שמאפשר את כל התהליך.</li>
        <li><strong>ערוץ קלאסי (בין אליס לבוב):</strong> דרך רגילה לגמרי (כמו אינטרנט, טלפון, מייל) להעביר מידע קלאסי (ביטים 0 ו-1 רגילים) מאליס לבוב. בלי זה, הטלפורטציה לא עובדת!</li>
    </ul>

    <h2>הצגה בשלוש מערכות</h2>
    <p>תהליך הטלפורטציה מתרחש בסדר מדויק:</p>
    <ol>
        <li><strong>אליס חוקרת את קיוביט המקור שלה (A) בשילוב עם חלקיק B השזור:</strong> אליס לוקחת את קיוביט A (במצב |ψ⟩A, שהיא לא בהכרח יודעת מהו!) ואת קיוביט B (שהוא חלק מהזוג השזור B-C), ומבצעת עליהם "מדידת בל" מיוחדת. המדידה הזו "אורגת" יחד את המידע של A עם המידע של B. ישנן 4 תוצאות אפשריות למדידת בל, וכל אחת מהן אומרת משהו ספציפי על היחס בין A ל-B. **שימו לב היטב:** המדידה הזו "הורסת" את המצב הקוונטי המקורי של A. הוא מפסיק להיות במצב |ψ⟩A!</li>
        <li><strong>אליס מספרת לבוב מה יצא במדידה (בערוץ קלאסי):</strong> לאחר המדידה, אליס מקבלת אחת מארבע תוצאות. היא מקודדת את התוצאה הזו לשני ביטים קלאסיים (למשל, 00, 01, 10, או 11) ושולחת אותם לבוב דרך ערוץ התקשורת הרגיל. זהו החלק היחיד בתהליך שבו מידע כלשהו עובר פיזית במרחב, והוא כאמור - מידע קלאסי בלבד.</li>
        <li><strong>בוב מקבל את המידע ומתקן את קיוביט C שלו:</strong> בוב מקבל את שני הביטים הקלאסיים מאליס. בהתאם לערכם, הוא יודע בדיוק איזו פעולה קוונטית (המכונה "שער קוונטי", כמו שער X או Z) עליו לבצע על קיוביט C שברשותו (החלק השני של הזוג השזור B-C). כל תוצאת מדידה של בל מתאימה לשער קוונטי אחר שבוב צריך להפעיל.</li>
    </ol>

    <h2>הקסם הושלם!</h2>
    <p>מרגע שבוב סיים לבצע את הפעולה המתקנת הנכונה על קיוביט C, מצבו הקוונטי של קיוביט C זהה לחלוטין למצב הקוונטי המקורי של קיוביט A היה לפני שכל התהליך התחיל! המצב |ψ⟩A "עבר טלפורטציה" מקיוביט A (שנהרס) לקיוביט C.</p>

    <h2>נקודות למחשבה קוונטית</h2>
    <ul>
        <li><strong>אין שיבוט:</strong> לא יצרנו עותק של A! המצב של A נהרס במהלך המדידה של אליס. הטלפורטציה היא העברה, לא העתקה.</li>
        <li><strong>אין מסע על-אורי:</strong> למרות שהשזירה פועלת כביכול באופן מיידי, כדי שהבוב יוכל לשחזר את המצב על C, הוא חייב לקבל את המידע הקלאסי מאליס. מכיוון שמידע קלאסי לא יכול לנוע מהר יותר ממהירות האור, גם תהליך הטלפורטציה כולו מוגבל על ידי מהירות האור. אי אפשר להשתמש בזה כדי לשלוח מסרים מהר יותר מאור.</li>
        <li><strong>חשיבות השזירה:</strong> השזירה היא המשאב הקוונטי החיוני שמאפשר את הטלפורטציה. בלעדיה, התהליך בלתי אפשרי.</li>
    </ul>

    <h2>לא רק תיאוריה: יישומים לעתיד</h2>
    <p>טלפורטציה קוונטית היא אבן בניין קריטית לטכנולוגיות קוונטיות עתידיות. היא תשמש כנראה להעברת מידע בין מעבדים קוונטיים במחשבים קוונטיים, להקמת רשתות תקשורת קוונטיות מאובטחות (שעמידות לפריצות!), ולחיבור צמתים ברשתות קוונטיות גדולות.</p>
</div>

<script>
    const qubitA = document.getElementById('qubitA');
    const qubitB = document.getElementById('qubitB');
    const qubitC = document.getElementById('qubitC');
    const stateSelectors = document.querySelectorAll('.state-selector button');
    const bellMeasureBtn = document.getElementById('bellMeasureBtn');
    const bellResultSpan = document.getElementById('bellResult');
    const sendClassicalBtn = document.getElementById('sendClassicalBtn');
    const classicalBitsSpan = document.getElementById('classicalBits');
    const bitsTransferDiv = document.getElementById('bitsTransfer');
    const applyCorrectionBtn = document.getElementById('applyCorrectionBtn');
     const appliedGateSpan = document.getElementById('appliedGate');
    const measureCBtn = document.getElementById('measureCBtn');
    const finalStateTextSpan = document.getElementById('finalStateText'); // Display expected state on C
    const finalMeasurementSpan = document.getElementById('finalMeasurement'); // Display measurement result
    const matchStatusSpan = document.getElementById('matchStatus'); // Display match status
    const toggleExplanationBtn = document.getElementById('toggleExplanationBtn');
    const explanationDiv = document.getElementById('explanation');
    const entanglementLink = document.querySelector('.entanglement-link');

    let initialStateA = null; // '0', '1', 'plus', 'minus'
    let bellMeasurementOutcome = null; // '00', '01', '10', '11'
    let finalStateOfCBeforeMeasure = null; // This should conceptually be initialStateA after correction

    // Function to visualize qubit state with icons and text
    function visualizeState(qubitElement, state) {
        const stateVizDiv = qubitElement.querySelector('.state-viz');
        qubitElement.dataset.state = state; // Set data attribute for CSS styling

        let textContent = '';
        switch (state) {
            case '0': textContent = '|0⟩'; break;
            case '1': textContent = '|1⟩'; break;
            case 'plus': textContent = '|+⟩'; break;
            case 'minus': textContent = '|-⟩'; break;
            case 'entangled': textContent = 'שזור'; break;
            case 'measured': textContent = 'נמדד'; break;
             case 'unknown': textContent = '?'; break;
            default: textContent = state; // Use original text if state not recognized
        }
         stateVizDiv.textContent = textContent; // Update text content
    }

    // Reset simulation state
    function resetSim() {
        initialStateA = null;
        bellMeasurementOutcome = null;
        finalStateOfCBeforeMeasure = null;

        visualizeState(qubitA, 'unknown');
        visualizeState(qubitB, 'entangled');
        visualizeState(qubitC, 'entangled');

        qubitA.classList.remove('measured');
        qubitB.classList.remove('measured');
        qubitC.classList.remove('measured');
        qubitB.classList.add('entangled'); // Ensure entangled class is there
        qubitC.classList.add('entangled'); // Ensure entangled class is there
        entanglementLink.style.opacity = 0.7; // Show entanglement link

        stateSelectors.forEach(btn => btn.disabled = false);
        bellMeasureBtn.disabled = true;
        sendClassicalBtn.disabled = true;
        applyCorrectionBtn.disabled = true;
        measureCBtn.disabled = true;

        bellResultSpan.textContent = '';
        classicalBitsSpan.textContent = '';
        bitsTransferDiv.textContent = '';
        appliedGateSpan.textContent = '';
        finalStateTextSpan.textContent = '?';
        finalMeasurementSpan.textContent = '';
        matchStatusSpan.textContent = '?';

        // Reset classical channel animation state
         bitsTransferDiv.style.transition = 'none';
         bitsTransferDiv.style.transform = 'translateX(0)';
         bitsTransferDiv.style.opacity = 1;


        console.log("Simulation reset. Select a state for Qubit A to begin."); // Log for debugging
    }

    // Step 1: Select initial state
    stateSelectors.forEach(button => {
        button.addEventListener('click', () => {
            if (initialStateA !== null) return; // Prevent re-selecting

            initialStateA = button.dataset.state;
            visualizeState(qubitA, initialStateA);

            stateSelectors.forEach(btn => btn.disabled = true);
            bellMeasureBtn.disabled = false;
            console.log(`Step 1: Qubit A state selected: ${initialStateA}`);
        });
    });

    // Step 2: Bell Measurement
    bellMeasureBtn.addEventListener('click', () => {
        if (bellMeasureBtn.disabled) return;

        // Simulate a random Bell state outcome (00, 01, 10, 11)
        const outcomes = ['00', '01', '10', '11'];
        bellMeasurementOutcome = outcomes[Math.floor(Math.random() * outcomes.length)];

        // Animate measurement - qubits fade/change appearance
        qubitA.classList.add('measured');
        qubitB.classList.add('measured');
        qubitB.classList.remove('entangled'); // Entanglement broken visually
        // Note: C remains entangled until correction based on classical info

        visualizeState(qubitA, 'measured'); // A is measured and destroyed
        visualizeState(qubitB, 'measured'); // B is measured

        bellResultSpan.textContent = bellMeasurementOutcome;

        bellMeasureBtn.disabled = true;
        sendClassicalBtn.disabled = false;

        console.log(`Step 2: Bell measurement performed. Outcome: ${bellMeasurementOutcome}`);
    });

    // Step 3: Send Classical Info
    sendClassicalBtn.addEventListener('click', () => {
        if (sendClassicalBtn.disabled) return;

        classicalBitsSpan.textContent = bellMeasurementOutcome;
        bitsTransferDiv.textContent = bellMeasurementOutcome; // Show bits on the channel

        // Animate bits transferring
        bitsTransferDiv.style.transition = 'none'; // Reset transition immediately
        bitsTransferDiv.style.transform = 'translateX(-100px)'; // Start off-screen left (relative to channel center)
        bitsTransferDiv.style.opacity = 1;

        // Use requestAnimationFrame for smooth start after style reset
        requestAnimationFrame(() => {
             requestAnimationFrame(() => { // Double rAF for reliable transition start
                 bitsTransferDiv.style.transition = 'transform 2s linear, opacity 0.5s ease-out 1.5s';
                 bitsTransferDiv.style.transform = 'translateX(100px)'; // End off-screen right
                 bitsTransferDiv.style.opacity = 0; // Fade out at the end
            });
        });


        sendClassicalBtn.disabled = true;

        // After animation completes
        setTimeout(() => {
            bitsTransferDiv.textContent = ''; // Clear from channel graphic
            applyCorrectionBtn.disabled = false;
            console.log(`Step 3: Classical info sent (${bellMeasurementOutcome}).`);
        }, 2000); // Match CSS transition duration

    });

    // Step 4: Apply Correction
    applyCorrectionBtn.addEventListener('click', () => {
        if (applyCorrectionBtn.disabled) return;

        let gate = '';
        // Determine gate based on Bell outcome (simplified logic matching state mapping)
        // Bell State |Φ⁺⟩ (00) -> I (Identity)
        // Bell State |Ψ⁺⟩ (01) -> X (NOT)
        // Bell State |Φ⁻⟩ (10) -> Z (Phase)
        // Bell State |Ψ⁻⟩ (11) -> ZX (or Y)
        // This logic depends on the *specific* entangled state (|00>+|11>)/sqrt(2) is common
        // and the *specific* basis of the Bell measurement.
        // A common mapping for (|00>+|11>)/sqrt(2) initial entanglement is:
        // 00 -> I
        // 01 -> X
        // 10 -> Z
        // 11 -> ZX (or Y) - assuming ZX = Y
        // This correctly recovers the initial state |a|0> + b|1> = a'|0> + b'|1> on C

        switch (bellMeasurementOutcome) {
            case '00': gate = 'I (זהות)'; break; // Identity: initial state of A is already on C
            case '01': gate = 'X (NOT)'; break; // X gate needed
            case '10': gate = 'Z (פאזה)'; break; // Z gate needed
            case '11': gate = 'ZX (Y)'; break; // Z followed by X (or Y)
             default: gate = '?';
        }

        appliedGateSpan.textContent = gate;
        qubitC.classList.remove('entangled'); // Entanglement served its purpose

        // Conceptually, C is NOW in the original state of A.
        finalStateOfCBeforeMeasure = initialStateA; // Store for the final check
        let displayedStateText = '';
         switch (finalStateOfCBeforeMeasure) {
            case '0': displayedStateText = '|0⟩'; break;
            case '1': displayedStateText = '|1⟩'; break;
            case 'plus': displayedStateText = '|+⟩'; break;
            case 'minus': displayedStateText = '|-⟩'; break;
             default: displayedStateText = '?';
        }
        finalStateTextSpan.textContent = displayedStateText; // Display the *expected* state visually/textually

        // Animate C changing visually (optional: specific gate animation)
         // For simplicity, just update its visual state style if needed, or add a pulse effect
         qubitC.animate([
             { transform: 'scale(1)', opacity: 1 },
             { transform: 'scale(1.05)', opacity: 0.8 },
             { transform: 'scale(1)', opacity: 1 }
         ], {
             duration: 500,
             iterations: 1
         });


        applyCorrectionBtn.disabled = true;
        measureCBtn.disabled = false;
        console.log(`Step 4: Correction applied to Qubit C: ${gate}. C is now conceptually in state ${initialStateA}.`);
    });

    // Step 5: Measure Final State of C
    measureCBtn.addEventListener('click', () => {
        if (measureCBtn.disabled) return;

        let measurementResult = '?';
        let measuredBasisState = null; // The actual state C collapses to

        // Simulate measurement in the computational basis (|0>/|1>)
        // The state C is in is finalStateOfCBeforeMeasure (which equals initialStateA)
        const stateToMeasure = finalStateOfCBeforeMeasure;

        if (stateToMeasure === '0') {
            measurementResult = '|0⟩';
             measuredBasisState = '0';
        } else if (stateToMeasure === '1') {
            measurementResult = '|1⟩';
            measuredBasisState = '1';
        } else if (stateToMeasure === 'plus') {
            // Measuring |+> = (|0> + |1>)/sqrt(2) in |0>/|1> basis gives 50% |0>, 50% |1>
            measurementResult = Math.random() < 0.5 ? '|0⟩' : '|1⟩';
             measuredBasisState = measurementResult === '|0⟩' ? '0' : '1';
        } else if (stateToMeasure === 'minus') {
            // Measuring |-> = (|0> - |1>)/sqrt(2) in |0>/|1> basis gives 50% |0>, 50% |1>
             measurementResult = Math.random() < 0.5 ? '|0⟩' : '|1⟩';
             measuredBasisState = measurementResult === '|0⟩' ? '0' : '1';
        } else {
             measurementResult = 'שגיאה';
             measuredBasisState = 'error';
        }

        finalMeasurementSpan.textContent = measurementResult;
        visualizeState(qubitC, 'measured'); // C is measured and state collapses
        qubitC.classList.add('measured');

        // Check if the measurement result *confirms* the teleportation worked
        // This check depends on the *initial* state of A and the *measurement basis* of C.
        // If A was |0> or |1>, the measurement should match.
        // If A was |+> or |->, the measurement is probabilistic (50/50), BUT the *state* itself *was* successfully teleported BEFORE the measurement.
        // We need to clarify the check's meaning. Let's check if measuring C in the |0>/|1> basis is consistent with the *expected* state of C (which is the original state of A).
        // This check is only meaningful if the original state A was |0> or |1>.
        let matchStatus = '?';
         if (initialStateA === '0' && measuredBasisState === '0') {
             matchStatus = 'התאמה! ✔️';
             matchStatusSpan.style.color = 'green';
         } else if (initialStateA === '1' && measuredBasisState === '1') {
             matchStatus = 'התאמה! ✔️';
             matchStatusSpan.style.color = 'green';
         } else if (initialStateA === '0' && measuredBasisState === '1') {
              matchStatus = 'אי-התאמה (ציפינו ל-|0⟩)! ❌';
              matchStatusSpan.style.color = 'red';
         } else if (initialStateA === '1' && measuredBasisState === '0') {
              matchStatus = 'אי-התאמה (ציפינו ל-|1⟩)! ❌';
              matchStatusSpan.style.color = 'red';
         } else if (initialStateA === 'plus' || initialStateA === 'minus') {
             // For |+> or |->, any |0> or |1> result is *expected* probabilistically
             matchStatus = 'תוצאה צפויה (|+⟩/|-⟩ מת collapses ל- |0⟩ או |1⟩) ✔️';
             matchStatusSpan.style.color = 'green';
         } else {
             matchStatus = 'לא ניתן לבדוק התאמה.';
             matchStatusSpan.style.color = '#333';
         }
        matchStatusSpan.textContent = matchStatus;


        measureCBtn.disabled = true;

        console.log(`Step 5: Qubit C measured. Result: ${measurementResult}.`);
        console.log(`Check: Original state A was ${initialStateA}. State C after correction was ${finalStateOfCBeforeMeasure}. Measurement result is consistent? ${matchStatus}`);


        // Offer to reset after a delay
        setTimeout(resetSim, 8000); // Reset after 8 seconds to allow user to read results
    });

    // Toggle Explanation visibility
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר את סוד הטלפורטציה הקוונטית!' : 'הצג את סוד הטלפורטציה הקוונטית!';
        // Scroll to explanation if showing it
        if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial setup
    resetSim();

</script>
---
```