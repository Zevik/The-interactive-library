---
title: "סימולטור Hashing דינמי"
english_slug: dynamic-hashing-simulator
category: "טכנולוגיה / מדעי המחשב"
tags:
  - אלגוריתמים
  - מבני נתונים
  - הדמיה אינטראקטיבית
  - ויזואליזציה
---
# מסע המפתח בטבלת הגיבוב: סימולטור Hashing אינטראקטיבי

ברוכים הבאים למגרש המשחקים של ה-Hashing! כאן תראו במו עיניכם איך פיסות מידע (מפתחות) מוצאות את מקומן הקסום בטבלת הגיבוב, ומה קורה כשהמסע שלהן מוביל אותן לאותו יעד בדיוק. הסימולטור הזה נועד להפוך מושגים מופשטים לחוויה ויזואלית ומרתקת.

<div class="simulator-container">
    <h2 class="simulator-title">הוסף מפתח לטבלת הגיבוב</h2>
    <div class="controls">
        <div class="control-group">
            <label for="keyInput">מפתח (מחרוזת או מספר):</label>
            <input type="text" id="keyInput" placeholder="הכנס מפתח לדוגמה (למשל, 'apple' או 123)">
        </div>
         <div class="control-group">
            <label for="tableSizeInput">גודל טבלה:</label>
            <input type="number" id="tableSizeInput" value="10" min="5" max="30">
         </div>
        <button id="addKeyButton" class="action-button primary">הוסף מפתח</button>
        <button id="resetButton" class="action-button secondary">אפס טבלה</button>
    </div>
    <div class="info-display">
        <div id="keyInfo" class="info-box info-key">מפתח: <span id="currentKey"></span></div>
        <div id="hashInfo" class="info-box info-hash">ערך גיבוב: <span id="currentHash"></span></div>
        <div id="indexInfo" class="info-box info-index">אינדקס יעד: <span id="currentIndex"></span></div>
        <div id="collisionsInfo" class="info-box info-collisions">התנגשויות באינדקס זה: <span id="indexCollisions">0</span></div>
    </div>
    <div class="hash-table-container">
        <div id="hashTableViz" class="hash-table">
            <!-- Table rows will be generated here by JS -->
        </div>
         <div id="keyAnimator" class="key-animator"></div> <!-- Element for animation -->
    </div>
</div>

<button id="toggleExplanation" class="explanation-button">גלה את הסוד מאחורי ה-Hashing</button>

<div id="explanationContent" class="explanation" style="display: none;">
    <h2>מהי בכלל טבלת גיבוב (Hash Table)?</h2>
    <p>דמיינו ספרייה ענקית שבה כל ספר מאוחסן לפי מספר קטלוגי ייחודי. טבלת גיבוב עובדת קצת כמו ספרייה כזו, רק שהיא סופר-מהירה! היא מאפשרת לנו לשמור ולשלוף נתונים בצורה כמעט מיידית (בזמן ממוצע של O(1)), בלי לעבור על כל הנתונים. איך היא עושה את זה? היא משתמשת ב"קסם" שנקרא פונקציית גיבוב.</p>

    <h3>פונקציית הגיבוב: הארכיטקט של הטבלה</h3>
    <p>הלב של טבלת הגיבוב הוא <strong>פונקציית הגיבוב (Hash Function)</strong>. הפונקציה הזו מקבלת כל פיסת מידע (המפתח - Key), לא משנה כמה היא גדולה או מורכבת, ומצמצמת אותה למספר קטן וסופי - האינדקס בטבלה שבו המפתח אמור להיות מאוחסן. בסימולטור שלנו, אנו משתמשים בפונקציה פשוטה לדוגמה שמחשבת סכום מספרי מזהי התווים במפתח (או את ערכו אם הוא מספר), ומפעילה עליו פעולת "מודולו" (שארית חלוקה) לפי גודל הטבלה. התוצאה? מספר שמבטיח שהאינדקס יהיה תמיד בטווח הטבלה.</p>

    <h3>האתגר: התנגשויות (Collisions)</h3>
    <p>פונקציית גיבוב אידיאלית הייתה אמורה לפזר את כל המפתחות באופן מושלם על פני הטבלה, כך שכל מפתח יגיע לאינדקס ייחודי. אבל במציאות, במיוחד כשיש הרבה מפתחות וטבלה בגודל סופי, בלתי נמנע שמפתחות שונים יחושבו לאותו אינדקס. תופעה זו נקראת <strong>התנגשות (Collision)</strong>, וזהו האתגר העיקרי בתכנון ושימוש בטבלאות גיבוב.</p>

    <h3>הפתרון: שרשור (Separate Chaining)</h3>
    <p>אז איך מתמודדים כשיש התנגשות? ישנן כמה שיטות. הסימולטור הזה מדגים את שיטת ה<strong>שרשור (Separate Chaining)</strong>. בשיטה זו, כל תא בטבלה (שמיוצג כאן כשורת אינדקס) לא מאחסן מפתח בודד, אלא רשימה (או "שרשרת") של כל המפתחות שהגיעו לאינדקס הזה. כשיש התנגשות, המפתח החדש פשוט מצטרף לשרשרת הקיימת באותו אינדקס. תוכלו לראות בסימולטור איך מפתחות מצטרפים זה אחרי זה לאותה שורה כשהם "מתנגשים". שיטה זו פשוטה ויעילה, אם כי במקרה הקיצוני שבו כל המפתחות מתנגשים, השרשרת יכולה להתארך מאוד ולהאט את פעולות השליפה.</p>

    <h3>הזמנה להתנסות</h3>
    <p>עכשיו תורכם לשחק! הכניסו מפתחות שונים - שמות, מספרים, מילים - וצפו במסע שלהם בטבלה. נסו לנחש אילו מפתחות עלולים לגרום להתנגשות וראו אם צדקתם. שחקו עם גודל הטבלה (שימו לב ששינוי גודל מאפס את הטבלה) וראו איך זה משפיע על הפיזור ועל הסיכוי להתנגשויות. צפו באנימציה ובמידע שמוצג כדי להבין טוב יותר את התהליך של כל מפתח.</p>
</div>

<style>
    /* גופנים וסגנון כללי */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 20px;
        background: linear-gradient(to right, #e0f7fa, #ccebfa); /* רקע מעודן */
        color: #333;
        direction: rtl; /* כיווניות כללית RTL */
        text-align: right;
        min-height: 100vh;
    }

    h1, h2 {
        color: #004085; /* כחול עמוק לכותרות */
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
    }

    .simulator-container {
        background-color: #ffffff; /* רקע לבן לקונטיינר הראשי */
        padding: 30px;
        border-radius: 12px; /* פינות מעוגלות יותר */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* צל עמוק יותר */
        margin-bottom: 30px;
        border: 1px solid #b3e5fc; /* מסגרת עדינה */
        max-width: 900px; /* הגבלת רוחב לקריאות טובה */
        margin-left: auto;
        margin-right: auto;
    }

    .simulator-title {
        margin-top: 0;
        color: #0056b3;
        text-align: center;
    }

    /* בקרי שליטה */
    .controls {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* מרווח גדול יותר בין אלמנטים */
        margin-bottom: 25px;
        align-items: flex-end; /* יישור אלמנטים לתחתית */
        justify-content: center;
        direction: rtl; /* כיווניות RTL עבור הפלקס קונטיינר */
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* יישור תוכן הקבוצה לימין */
        gap: 8px;
    }

    .controls label {
        font-weight: bold;
        color: #004085;
        font-size: 0.95rem;
    }

    .controls input[type="text"],
    .controls input[type="number"] {
        padding: 10px 12px;
        border: 1px solid #b3e5fc; /* מסגרת בצבע תכלת */
        border-radius: 6px;
        font-size: 1rem;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        direction: ltr; /* קלט עצמו LTR */
        text-align: left; /* טקסט בתוך הקלט משמאל לימין */
        width: 100%; /* רוחב מלא בתוך קבוצת השליטה */
        box-sizing: border-box; /* כולל פאדינג ובורדר ברוחב */
    }

     .controls input[type="text"]:focus,
    .controls input[type="number"]:focus {
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
        outline: none;
    }

    .action-button {
        padding: 10px 25px;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.1s ease, opacity 0.3s ease;
        min-width: 120px; /* רוחב מינימלי לכפתורים */
        text-align: center;
        align-self: flex-end; /* יישור הכפתורים לתחתית בתוך הפלקס קונטיינר */
    }

    .primary {
        background-color: #007bff;
    }

    .primary:hover {
        background-color: #0056b3;
    }

    .secondary {
        background-color: #6c757d;
    }

    .secondary:hover {
        background-color: #5a6268;
    }

     .action-button:active {
        transform: scale(0.98);
    }

     .action-button:disabled {
         opacity: 0.6;
         cursor: not-allowed;
     }

    /* תצוגת מידע */
    .info-display {
        display: flex;
        flex-wrap: wrap;
        gap: 15px; /* מרווח בין תיבות מידע */
        margin-bottom: 25px;
        justify-content: center;
        font-size: 0.95rem;
        direction: rtl; /* כיווניות RTL לתיבות המידע */
    }

    .info-box {
        background-color: #e9ecef;
        padding: 10px 15px;
        border-radius: 6px;
        border: 1px solid #ced4da;
        flex-grow: 1; /* מאפשר לתיבות לגדול */
        text-align: center;
        min-width: 150px; /* רוחב מינימלי לתיבה */
        box-sizing: border-box;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .info-box span {
         font-weight: bold;
         color: #004085;
         direction: ltr; /* ערכים מספריים/טקסטואליים בקלט LTR */
         display: inline-block;
         min-width: 20px; /* רוחב מינימלי לספאן כדי לשמור על יישור */
         text-align: left;
    }

     /* הבהוב קל על תיבות המידע בעת עדכון */
     .info-box.updating {
         background-color: #fffacd; /* צהוב בהיר */
         border-color: #f0ad4e; /* כתום */
     }


    /* תצוגת טבלת הגיבוב */
    .hash-table-container {
        margin-top: 30px;
        overflow-x: auto; /* מאפשר גלילה אם הטבלה רחבה מדי */
        padding: 10px; /* פאדינג סביב הטבלה */
        border: 1px solid #b3e5fc;
        border-radius: 8px;
        background-color: #f8f9fa; /* רקע בהיר לטבלה */
        position: relative; /* להנפשת מפתח במיקום מוחלט */
    }

    .hash-table {
        display: flex;
        flex-direction: column; /* עמודות אנכית */
        gap: 8px; /* מרווח בין שורות */
        padding: 0; /* הסרת פאדינג פנימי אם היה */
        border: none; /* הסרת בורדר פנימי אם היה */
        background-color: transparent;
    }

    .table-row {
        display: flex;
        align-items: center; /* יישור אנכי למרכז בשורה */
        gap: 15px; /* מרווח בין אינדקס לשרשרת */
        padding: 8px;
        background-color: #e0f7fa; /* רקע בהיר לשורה */
        border-radius: 6px;
        border: 1px solid #b3e5fc;
        min-height: 40px; /* גובה מינימלי לשורה */
        transition: background-color 0.3s ease;
         direction: rtl; /* כיווניות RTL לשורה */
         justify-content: flex-end; /* יישור תוכן השורה לימין (אינדקס מימין, שרשרת משמאל) */
    }

    .table-index {
        flex-shrink: 0; /* מונע מהאינדקס להתכווץ */
        width: 45px; /* רוחב קבוע לאינדקס */
        text-align: center;
        font-weight: bold;
        background-color: #007bff; /* צבע הדגשה לאינדקס */
        color: white;
        padding: 8px 5px;
        border-radius: 4px;
        align-self: center; /* יישור אנכי למרכז */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        direction: ltr; /* מספר האינדקס עצמו LTR */
    }

    .chain {
        display: flex;
        flex-wrap: wrap; /* מאפשר למפתחות לעבור שורה */
        gap: 8px; /* מרווח בין מפתחות בשרשרת */
        padding: 5px;
        border: 1px dashed #90caf9; /* גבול מקווקו לשרשרת */
        border-radius: 4px;
        min-height: 30px; /* גובה מינימלי לשרשרת ריקה */
        flex-grow: 1; /* מאפשר לשרשרת לתפוס מקום */
        background-color: #f1f8e9; /* רקע בהיר יותר לשרשרת */
        align-items: center; /* יישור אנכי למרכז בשרשרת */
        direction: ltr; /* מפתחות בשרשרת LTR */
        justify-content: flex-start; /* מפתחות בשרשרת מתחילים משמאל */
    }

    .chain:empty::before {
         content: 'שרשרת ריקה';
         color: #6c757d;
         font-style: italic;
         font-size: 0.9em;
         direction: rtl; /* הטקסט "שרשרת ריקה" RTL */
         width: 100%; /* מאפשר לטקסט להתיישר */
         text-align: right;
     }

    .key-element {
        background-color: #4caf50; /* ירוק למפתחות */
        color: white;
        padding: 6px 10px;
        border-radius: 4px;
        font-size: 0.9rem;
        white-space: nowrap; /* מונע שבירת מילה */
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease; /* אנימציה לצבע */
         direction: ltr; /* ערך המפתח עצמו LTR */
    }

     /* הדגשת מפתח קיים */
     .key-element.highlight-exist {
         background-color: #ff9800; /* כתום */
         animation: pulse 1s ease-in-out infinite alternate; /* אנימציית פעימה */
     }

     @keyframes pulse {
         from { transform: scale(1); opacity: 1; }
         to { transform: scale(1.05); opacity: 0.9; }
     }


    /* כפתור הסבר */
    .explanation-button {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        background-color: #17a2b8; /* צבע טורקיז */
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
        font-weight: 500;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
    }

    .explanation-button:hover {
        background-color: #138496;
    }

     .explanation-button:active {
        transform: scale(0.98);
    }


    /* בלוק הסבר */
    .explanation {
        background-color: #e9ecef;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
        margin-top: 20px;
        border: 1px solid #ced4da;
        direction: rtl; /* כיווניות RTL להסבר */
        text-align: right;
        max-width: 900px; /* הגבלת רוחב */
         margin-left: auto;
        margin-right: auto;
    }

    .explanation h2 {
        color: #0056b3;
        text-align: right;
        margin-bottom: 15px;
    }

    .explanation p {
        margin-bottom: 15px;
        text-align: right;
    }

    .explanation strong {
        color: #004085; /* הדגשה בצבע כחול */
    }

    /* אנימציית המפתח הנע */
     .key-animator {
         position: absolute; /* ימוקם בתוך ה-hash-table-container */
         background-color: #ffc107; /* צהוב בהיר */
         color: #343a40; /* טקסט כהה */
         padding: 8px 12px;
         border-radius: 4px;
         font-size: 1rem;
         white-space: nowrap;
         pointer-events: none; /* אלמנט לא קליקבי */
         opacity: 0; /* התחלה שקוף */
         transform: translate(-50%, -50%); /* מרכז את האלמנט בנקודת המיקום */
         transition: all 1.5s ease-in-out, opacity 0.5s ease; /* אנימציית מעבר */
         z-index: 10; /* מעל הטבלה */
         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
         border: 1px solid #ffb300;
         direction: ltr; /* הערך המוצג LTR */
     }

     /* אנימציית כניסה לשרשרת */
     @keyframes slide-in {
         from { transform: translateX(-20px); opacity: 0; }
         to { transform: translateX(0); opacity: 1; }
     }

     .key-element.animate-in {
         animation: slide-in 0.5s ease forwards;
     }


     /* רספונסיביות בסיסית */
     @media (max-width: 768px) {
         .controls {
             flex-direction: column;
             align-items: stretch;
         }
         .control-group {
             width: 100%;
         }
         .action-button {
             width: 100%;
             min-width: auto;
         }
         .info-display {
             flex-direction: column;
             gap: 10px;
         }
         .info-box {
             width: 100%;
         }
         .table-row {
             flex-direction: row; /* בשורה, שומרים על אינדקס ושרשרת */
             align-items: center;
         }
         .table-index {
             align-self: center;
         }
          .chain {
              justify-content: flex-start; /* מפתחות ממשיכים להתיישר משמאל בשרשרת LTR */
          }

     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const keyInput = document.getElementById('keyInput');
        const tableSizeInput = document.getElementById('tableSizeInput');
        const addKeyButton = document.getElementById('addKeyButton');
        const resetButton = document.getElementById('resetButton');
        const hashTableViz = document.getElementById('hashTableViz');
        const toggleExplanationButton = document.getElementById('toggleExplanation');
        const explanationContent = document.getElementById('explanationContent');
        const keyAnimator = document.getElementById('keyAnimator'); // Element for animation

        const currentKeySpan = document.getElementById('currentKey');
        const currentHashSpan = document.getElementById('currentHash');
        const currentIndexSpan = document.getElementById('currentIndex');
        const indexCollisionsSpan = document.getElementById('indexCollisions');

        const infoBoxes = document.querySelectorAll('.info-box'); // Select all info boxes for highlighting

        let hashTable = [];
        let tableSize = 10;
        let isAnimating = false; // Flag to prevent adding keys during animation

        // Simple hash function (Sum of character codes modulo table size)
        function simpleHash(key, size) {
            let hash = 0;
            const keyStr = String(key);
            for (let i = 0; i < keyStr.length; i++) {
                hash = (hash + keyStr.charCodeAt(i)); // Simple sum
            }
            return hash % size;
        }

        // Render the initial hash table structure
        function renderTable() {
             // Clear previous content and animation element
            hashTableViz.innerHTML = '';
            keyAnimator.style.opacity = 0; // Hide animator
            keyAnimator.textContent = ''; // Clear animator text

            // Reset logical table
            tableSize = parseInt(tableSizeInput.value, 10);
            if (isNaN(tableSize) || tableSize < 5) {
                tableSize = 10;
                tableSizeInput.value = 10;
            }
             if (tableSize > 30) { // Cap size for visual clarity
                 tableSize = 30;
                 tableSizeInput.value = 30;
             }

            hashTable = Array(tableSize).fill(null).map(() => []); // Separate Chaining

            // Create visual table rows
            for (let i = 0; i < tableSize; i++) {
                const rowDiv = document.createElement('div');
                rowDiv.classList.add('table-row');
                rowDiv.setAttribute('data-index', i); // Add index data attribute for selection

                const indexDiv = document.createElement('div');
                indexDiv.classList.add('table-index');
                indexDiv.textContent = i;

                const chainDiv = document.createElement('div');
                chainDiv.classList.add('chain');
                chainDiv.id = `chain-${i}`; // Add an ID for easier access

                rowDiv.appendChild(indexDiv);
                rowDiv.appendChild(chainDiv);
                hashTableViz.appendChild(rowDiv);
            }

             // Reset info display
            clearInfo();
             isAnimating = false;
             addKeyButton.disabled = false;
             tableSizeInput.disabled = false; // Enable table size input
        }

         // Clear all info spans and remove highlighting
         function clearInfo() {
            currentKeySpan.textContent = '';
            currentHashSpan.textContent = '';
            currentIndexSpan.textContent = '';
            indexCollisionsSpan.textContent = '0';
            infoBoxes.forEach(box => box.classList.remove('updating'));
             removeHighlightFromAllKeys(); // Remove any key highlights
         }

         // Remove highlight class from all key elements
         function removeHighlightFromAllKeys() {
             hashTableViz.querySelectorAll('.key-element').forEach(el => {
                 el.classList.remove('highlight-exist');
                 el.style.animation = ''; // Remove pulse animation
             });
         }


        // Add a key to the hash table with animation steps
        async function addKey() {
            if (isAnimating) return; // Prevent multiple animations
            isAnimating = true;
            addKeyButton.disabled = true; // Disable button during animation
             tableSizeInput.disabled = true; // Disable size change during animation


            const key = keyInput.value.trim();
            if (!key) {
                 alert('אנא הכנס מפתח.');
                 isAnimating = false;
                 addKeyButton.disabled = false;
                 tableSizeInput.disabled = false;
                 return;
            }

            // Clear previous info and animations
            clearInfo();
            keyAnimator.style.opacity = 0;
            keyAnimator.textContent = '';


             // Step 1: Display Key and start animation element
            currentKeySpan.textContent = key;
             document.getElementById('keyInfo').classList.add('updating'); // Highlight key info box

             keyAnimator.textContent = key;
             // Position animator near input field initially
             const keyInputRect = keyInput.getBoundingClientRect();
             const hashTableContainerRect = hashTableViz.parentElement.getBoundingClientRect(); // Use parent for positioning context
             keyAnimator.style.left = `${keyInputRect.left - hashTableContainerRect.left + keyInputRect.width / 2}px`;
             keyAnimator.style.top = `${keyInputRect.top - hashTableContainerRect.top + keyInputRect.height / 2}px`;
             keyAnimator.style.opacity = 1;


            await new Promise(resolve => setTimeout(resolve, 800)); // Pause

             document.getElementById('keyInfo').classList.remove('updating');


            // Step 2: Calculate and Display Hash
            const hashValue = simpleHash(key, tableSize);
            currentHashSpan.textContent = hashValue;
            document.getElementById('hashInfo').classList.add('updating'); // Highlight hash info box


             // Move animator towards Hash Info box
             const hashInfoRect = document.getElementById('hashInfo').getBoundingClientRect();
              keyAnimator.style.left = `${hashInfoRect.left - hashTableContainerRect.left + hashInfoRect.width / 2}px`;
             keyAnimator.style.top = `${hashInfoRect.top - hashTableContainerRect.top + hashInfoRect.height / 2}px`;


            await new Promise(resolve => setTimeout(resolve, 1500)); // Pause for hash calculation/move


             document.getElementById('hashInfo').classList.remove('updating');


            // Step 3: Determine and Display Index
            const index = hashValue; // Index is simply the hash result in this sim
            currentIndexSpan.textContent = index;
            document.getElementById('indexInfo').classList.add('updating'); // Highlight index info box


             // Move animator towards Index Info box
             const indexInfoRect = document.getElementById('indexInfo').getBoundingClientRect();
              keyAnimator.style.left = `${indexInfoRect.left - hashTableContainerRect.left + indexInfoRect.width / 2}px`;
             keyAnimator.style.top = `${indexInfoRect.top - hashTableContainerRect.top + indexInfoRect.height / 2}px`;


            await new Promise(resolve => setTimeout(resolve, 1000)); // Pause for index determination/move

             document.getElementById('indexInfo').classList.remove('updating');


            // Step 4: Move towards the target row in the table
            const targetRow = hashTableViz.querySelector(`.table-row[data-index='${index}']`);
             if (!targetRow) {
                 console.error("Target row not found:", index);
                  isAnimating = false;
                 addKeyButton.disabled = false;
                 tableSizeInput.disabled = false;
                 keyAnimator.style.opacity = 0;
                 return;
             }

             // Calculate target position within the hash-table-container
             const targetRowRect = targetRow.getBoundingClientRect();
             // Position the animator near the chain part of the row
             const targetX = targetRowRect.left - hashTableContainerRect.left + targetRowRect.width * 0.8; // Aim towards the right side in RTL layout
             const targetY = targetRowRect.top - hashTableContainerRect.top + targetRowRect.height / 2;

             keyAnimator.style.left = `${targetX}px`;
             keyAnimator.style.top = `${targetY}px`;


            await new Promise(resolve => setTimeout(resolve, 1500)); // Pause for move to row


             // Step 5: Check for collision and add to chain
            const chainDiv = document.getElementById(`chain-${index}`); // Use ID for chain
             const existingChain = hashTable[index];
             const keyExists = existingChain.includes(key);

             let collisionDetected = false;

             if (keyExists) {
                 // Collision with existing key - highlight it
                 const keyElements = chainDiv.querySelectorAll('.key-element');
                 keyElements.forEach(el => {
                     if (el.textContent === key) {
                          el.classList.add('highlight-exist'); // Add highlight class
                     }
                 });
                 collisionDetected = true;
                  indexCollisionsSpan.textContent = existingChain.length - 1; // Still show number of collisions for index
                 document.getElementById('collisionsInfo').classList.add('updating'); // Highlight collision info
                  await new Promise(resolve => setTimeout(resolve, 2000)); // Pause to see highlight
             } else {
                 // Add key to the logical table
                 hashTable[index].push(key);

                 // Update info display for collisions
                 indexCollisionsSpan.textContent = hashTable[index].length - 1;
                 document.getElementById('collisionsInfo').classList.add('updating'); // Highlight collision info

                 // Create and append key element to the visual chain
                 const keyElement = document.createElement('div');
                 keyElement.classList.add('key-element');
                 keyElement.textContent = key;
                 keyElement.setAttribute('data-key-value', key);

                 // Position the animator element precisely where the new key will appear before appending
                 // Calculate the position within the chain div
                 const chainRect = chainDiv.getBoundingClientRect();
                  const targetKeyX = chainRect.left - hashTableContainerRect.left + chainRect.width; // Right edge of chain
                  const targetKeyY = chainRect.top - hashTableContainerRect.top + chainRect.height / 2;


                 keyAnimator.style.transition = 'all 0.5s ease-out'; // Faster transition for final placement
                  keyAnimator.style.left = `${targetKeyX}px`;
                  keyAnimator.style.top = `${targetKeyY}px`;


                 await new Promise(resolve => setTimeout(resolve, 500)); // Short pause before appending


                 keyAnimator.style.opacity = 0; // Hide animator as the real key appears

                 // Append the actual key element and trigger its entrance animation
                 chainDiv.appendChild(keyElement);
                 // Force reflow/repaint before adding the animation class
                 void keyElement.offsetWidth;
                 keyElement.classList.add('animate-in');


                  // Scroll chain into view if needed (optional but good UX)
                 chainDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });


                 await new Promise(resolve => setTimeout(resolve, 800)); // Pause for slide-in animation
             }


             // Clean up
             keyInput.value = ''; // Clear input field
             document.getElementById('collisionsInfo').classList.remove('updating');
              if(collisionDetected) {
                  // Remove highlight after pause if it was a collision
                   const keyElements = chainDiv.querySelectorAll('.key-element');
                   keyElements.forEach(el => el.classList.remove('highlight-exist', 'animate-in'));
                   // Re-apply default animation transition if needed, or let CSS handle it
                    el.style.animation = ''; // Remove pulse animation
               });
             }


             isAnimating = false;
            addKeyButton.disabled = false; // Re-enable button
            tableSizeInput.disabled = false; // Re-enable size change
             keyAnimator.style.transition = 'all 1.5s ease-in-out, opacity 0.5s ease'; // Reset transition for next use
        }

        function resetTable() {
             // Stop any ongoing animations immediately
             isAnimating = false;
             addKeyButton.disabled = false;
             tableSizeInput.disabled = false;
             keyAnimator.style.opacity = 0;
             keyAnimator.textContent = '';
             keyAnimator.style.transition = 'none'; // Remove transition temporarily

            renderTable(); // Re-render empty table
             clearInfo();
             // Re-apply transition after render is complete
             setTimeout(() => {
                 keyAnimator.style.transition = 'all 1.5s ease-in-out, opacity 0.5s ease';
             }, 50); // Small delay to ensure transition is reapplied after rendering
        }

        // Event Listeners
        addKeyButton.addEventListener('click', addKey);
        keyInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                addKey();
            }
        });
        resetButton.addEventListener('click', resetTable);
        tableSizeInput.addEventListener('change', () => {
             if (isAnimating) { // Prevent size change during animation
                 // Maybe alert user or revert value? For now, just ignore change until animation ends.
                 // A better approach is to disable the input, which is done in addKey.
                 // If user changes size while input was disabled, this change listener won't fire until enabled.
             } else {
                 resetTable(); // Reset table when size changes if not animating
             }
        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none';
            explanationContent.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'גלה את הסוד מאחורי ה-Hashing';
        });

        // Initial render
        renderTable();
    });
</script>