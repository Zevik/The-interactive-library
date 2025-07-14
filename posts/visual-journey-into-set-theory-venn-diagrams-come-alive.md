---
title: "מסע ויזואלי אל לב תורת הקבוצות: דיאגרמות ון מתעוררות לחיים"
english_slug: visual-journey-into-set-theory-venn-diagrams-come-alive
category: "מדעים מדויקים / מתמטיקה"
tags:
  - תורת הקבוצות
  - דיאגרמות ון
  - מתמטיקה
  - קבוצות
  - פעולות על קבוצות
---
<h1>מסע ויזואלי אל לב תורת הקבוצות: דיאגרמות ון מתעוררות לחיים</h1>

איך נוכל לפענח את הקשרים המורכבים בין אוספים שונים של רעיונות, חפצים, או אפילו אנשים? האם יש דרך פשוטה ומרתקת להפוך את הפעולות הלוגיות המופשטות על קבוצות למשהו שניתן ממש לראות ולגעת בו? התכוננו לצלול לעולם קסום של חיתוכים, איחודים ומשלימים - לא רק בראש, אלא מול העיניים!

<div class="interactive-app">
    <h2>חקור את הקשרים: דיאגרמות ון אינטראקטיביות</h2>

    <div class="controls">
        <div class="control-group">
            <label>מספר קבוצות:</label>
            <div class="radio-group">
                <input type="radio" id="sets-2" name="num-sets" value="2" checked>
                <label for="sets-2">2 קבוצות</label>
                <input type="radio" id="sets-3" name="num-sets" value="3">
                <label for="sets-3">3 קבוצות</label>
            </div>
        </div>

        <div class="control-group">
            <label for="operation-select">בחר פעולה/ביטוי:</label>
            <select id="operation-select">
                <optgroup label="קבוצות בסיסיות">
                    <option value="A">A</option>
                    <option value="B">B</option>
                    <option value="C" class="for-3-sets">C</option>
                    <option value="U">U (הקבוצה האוניברסלית)</option>
                    <option value="Empty">∅ (הקבוצה הריקה)</option>
                </optgroup>
                <optgroup label="פעולות יסוד">
                    <option value="A_union_B">A ∪ B</option>
                    <option value="A_intersect_B">A ∩ B</option>
                    <option value="A_diff_B">A \ B (A פחות B)</option>
                    <option value="B_diff_A">B \ A (B פחות A)</option>
                    <option value="A_complement">Aᶜ (המשלים של A)</option>
                    <option value="B_complement">Bᶜ (המשלים של B)</option>
                    <option value="C_complement" class="for-3-sets">Cᶜ (המשלים של C)</option>
                </optgroup>
                 <optgroup label="שילובים נבחרים (3 קבוצות)">
                    <option value="A_union_B_union_C" class="for-3-sets">A ∪ B ∪ C</option>
                    <option value="A_intersect_B_intersect_C" class="for-3-sets">A ∩ B ∩ C</option>
                    <option value="(A_union_B)_intersect_C" class="for-3-sets">(A ∪ B) ∩ C</option>
                    <option value="(A_intersect_B)_union_C" class="for-3-sets">(A ∩ B) ∪ C</option>
                    <option value="(A_intersect_B)_diff_C" class="for-3-sets">(A ∩ B) \ C</option>
                    <option value="(A_union_B)_complement" class="for-3-sets">(A ∪ B)ᶜ</option>
                    <option value="(A_intersect_B)_complement" class="for-3-sets">(A ∩ B)ᶜ</option>
                </optgroup>
            </select>
        </div>
    </div>

    <div id="venn-diagram-container">
        <!-- 2-Set Venn Diagram SVG -->
        <svg id="venn-2-sets" viewBox="0 0 400 300" class="venn-diagram active">
            <rect x="10" y="10" width="380" height="280" class="universal-set"></rect>
            <text x="385" y="295" text-anchor="end" class="set-label universe">U</text>

            <!-- Regions for 2 sets: A\B, A∩B, B\A, (A∪B)ᶜ -->
            <!-- *** IMPORTANT: These paths are simplified placeholders. Accurate paths require complex geometric calculations or external libraries. The highlighting logic works, but the visual shapes of the regions may not be perfectly accurate. *** -->
            <g class="regions">
                 <!-- Using approximate coordinates for intersection points for slightly better visual placeholders -->
                 <!-- Intersection points approx: (200, 87.55) and (200, 212.45) assuming cx=150, 250, cy=150, r=80 -->
                 <path id="r2_A_not_B" d="M 150 70 A 80 80 0 1 1 150 230 L 200 212.45 A 80 80 0 0 0 200 87.55 L 150 70 Z" class="venn-region"></path>
                 <path id="r2_A_intersect_B" d="M 200 87.55 A 80 80 0 0 1 200 212.45 A 80 80 0 0 1 200 87.55 Z" class="venn-region"></path>
                 <path id="r2_B_not_A" d="M 250 70 A 80 80 0 0 0 200 87.55 A 80 80 0 0 0 200 212.45 L 250 230 A 80 80 0 0 1 250 70 Z" class="venn-region"></path>
                 <path id="r2_None" d="M 10,10 H 390 V 290 H 10 Z M 150,70 A 80,80 0 1 1 250,70 A 80,80 0 1 0 150,70 Z" class="venn-region"></path>
            </g>

            <!-- Circles for visibility/labels -->
            <circle cx="150" cy="150" r="80" class="venn-circle A"></circle>
            <text x="150" y="150" text-anchor="middle" alignment-baseline="middle" class="set-label A-label">A</text>
            <circle cx="250" cy="150" r="80" class="venn-circle B"></circle>
            <text x="250" y="150" text-anchor="middle" alignment-baseline="middle" class="set-label B-label">B</text>

        </svg>

        <!-- 3-Set Venn Diagram SVG -->
        <svg id="venn-3-sets" viewBox="0 0 400 350" class="venn-diagram">
             <rect x="10" y="10" width="380" height="330" class="universal-set"></rect>
             <text x="385" y="345" text-anchor="end" class="set-label universe">U</text>

             <!-- Regions for 3 sets (A, B, C) - 8 regions -->
             <!-- *** IMPORTANT: These paths are simplified placeholders. Accurate paths require complex geometric calculations or external libraries. The highlighting logic works, but the visual shapes of the regions may not be perfectly accurate. *** -->
             <g class="regions">
                 <!-- Placeholder paths based on approximate circle positions: A(200,150,80), B(150,230,80), C(250,230,80) -->
                 <path id="r3_A_only" d="" class="venn-region"></path>
                 <path id="r3_B_only" d="" class="venn-region"></path>
                 <path id="r3_C_only" d="" class="venn-region"></path>
                 <path id="r3_A_intersect_B_not_C" d="" class="venn-region"></path>
                 <path id="r3_A_intersect_C_not_B" d="" class="venn-region"></path>
                 <path id="r3_B_intersect_C_not_A" d="" class="venn-region"></path>
                 <path id="r3_A_intersect_B_intersect_C" d="" class="venn-region"></path>
                 <path id="r3_None" d="M 10,10 H 390 V 340 H 10 Z" class="venn-region"></path>
             </g>

            <!-- Circles for visibility/labels -->
            <circle cx="200" cy="150" r="80" class="venn-circle A"></circle>
            <text x="200" y="150" text-anchor="middle" alignment-baseline="middle" class="set-label A-label">A</text>
            <circle cx="150" cy="230" r="80" class="venn-circle B"></circle>
            <text x="150" y="230" text-anchor="middle" alignment-baseline="middle" class="set-label B-label">B</text>
            <circle cx="250" cy="230" r="80" class="venn-circle C"></circle>
            <text x="250" y="230" text-anchor="middle" alignment-baseline="middle" class="set-label C-label">C</text>

        </svg>
    </div>
     <p class="interactive-hint">בחרו את מספר הקבוצות ואז בחרו פעולה מהרשימה. צפו כיצד הדיאגרמה מתעדכנת מיידית!</p>
</div>

<button id="toggle-explanation">הסבר את הקסם שמאחורי הקבוצות והדיאגרמות</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מעמיק: תורת הקבוצות ודיאגרמות ון</h2>

    <p>דמיינו עולם שבו אנו מארגנים דברים, רעיונות או אנשים לקבוצות מוגדרות. תורת הקבוצות מספקת לנו את הכלים המתמטיים לעשות זאת ולנתח את היחסים ביניהן. זוהי אבן יסוד במתמטיקה, בעלת שימושים נרחבים במדעי המחשב, סטטיסטיקה, ולוגיקה.</p>

    <h3>מהי קבוצה בעצם?</h3>
    <p>קבוצה היא פשוט אוסף, ברור ומדויק, של אובייקטים מובחנים. למשל, קבוצת כל המספרים הראשוניים הקטנים מ-10 {2, 3, 5, 7}, קבוצת הצבעים בדגל ישראל {כחול, לבן}, או קבוצת התלמידים בכיתה שלכם.</p>

    <h3>הקבוצה האוניברסלית (U)</h3>
    <p>בעת דיון על קבוצות מסוימות, אנו מגדירים "עולם תוכן" - הקבוצה האוניברסלית. היא כוללת את כל האובייקטים הרלוונטיים לדיון הנוכחי. כל קבוצה אחרת שנבחנת באותו הקשר היא תת-קבוצה של U.</p>

    <h3>הכרות ויזואלית: דיאגרמות ון</h3>
    <p>דיאגרמות ון הן כלי ויזואלי גאוני, שהומצא על ידי המתמטיקאי ג'ון ון, להמחשת קבוצות והקשרים ביניהן בצורה אינטואיטיבית. הן מציגות את הקבוצה האוניברסלית כמלבן, ואת הקבוצות הנבחנות כמעגלים (או צורות סגורות אחרות) בתוך המלבן. החפיפה בין הצורות מציגה את האיברים המשותפים לקבוצות השונות.</p>

    <h3>פעולות הקסם על קבוצות:</h3>
    <ul>
        <li><strong>איחוד (Union - ∪):</strong> דמיינו שתי קבוצות מתמזגות. A ∪ B היא קבוצה חדשה המכילה את כל האיברים שנמצאים או בקבוצה A, או בקבוצה B, או בשתיהן יחד. בדיאגרמת ון, זהו כל השטח המכוסה על ידי המעגלים של A ו-B.</li>
        <li><strong>חיתוך (Intersection - ∩):</strong> מה משותף לשתי קבוצות? A ∩ B היא הקבוצה שמכילה רק את האיברים הנמצאים *גם* ב-A *וגם* ב-B. בדיאגרמת ון, זהו האזור המרכזי בו המעגלים של A ו-B חופפים.</li>
        <li><strong>הפרש (Difference - \ או -):</strong> מה נשאר בקבוצה אחת כשמסירים ממנה את מה שמשותף לאחרת? A \ B (או A - B) היא קבוצה המכילה את כל האיברים הנמצאים ב-A אך *אינם* נמצאים ב-B. בדיאגרמת ון, זהו החלק במעגל A שאינו חופף למעגל B.</li>
        <li><strong>משלים (Complement - ᶜ או '):</strong> מה נמצא ב"עולם התוכן" שלנו (U) אך *לא* בקבוצה מסוימת (A)? Aᶜ (או A') היא קבוצת כל האיברים ב-U שאינם ב-A. בדיאגרמת ון, זהו כל השטח שבתוך המלבן (U) אך מחוץ למעגל של A.</li>
    </ul>

    <h3>שילובים מורכבים ודיאגרמות ון עם 3 קבוצות</h3>
    <p>היופי בדיאגרמות ון הוא שהן מאפשרות לנו להבין ויזואלית גם ביטויים מסובכים יותר המשלבים מספר פעולות, כמו (A ∪ B) ∩ C או Aᶜ ∪ (B \ C). עבור 3 קבוצות (A, B, C), הדיאגרמה הופכת קצת מורכבת יותר, עם 8 אזורים נפרדים המייצגים את כל השילובים האפשריים (איבר רק ב-A, איבר ב-A וב-B אבל לא ב-C, איבר בשלושתן, איבר מחוץ לשלושתן, וכן הלאה).</p>
    <p>היישום האינטראקטיבי כאן מאפשר לכם לבחור כל ביטוי כזה ולראות באופן מיידי אילו אזורים בדיאגרמה מתאימים לו. כך, תוכלו לבנות אינטואיציה חזקה לגבי המשמעות הלוגית של פעולות על קבוצות באמצעות הצגה ויזואלית דינמית וצבעונית. שחקו עם האפשרויות וגלו בעצמכם את היופי שבתורת הקבוצות!</p>
</div>

<script>
    // --- JavaScript Logic and Interactivity ---

    // Define region IDs for 2 sets
    const venn2RegionIds = {
        "A": ["r2_A_not_B", "r2_A_intersect_B"],
        "B": ["r2_B_not_A", "r2_A_intersect_B"],
        "U": ["r2_A_not_B", "r2_A_intersect_B", "r2_B_not_A", "r2_None"],
        "Empty": [],
        "A_union_B": ["r2_A_not_B", "r2_A_intersect_B", "r2_B_not_A"],
        "A_intersect_B": ["r2_A_intersect_B"],
        "A_diff_B": ["r2_A_not_B"],
        "B_diff_A": ["r2_B_not_A"],
        "A_complement": ["r2_B_not_A", "r2_None"],
        "B_complement": ["r2_A_not_B", "r2_None"],
        "(A_union_B)_complement": ["r2_None"], // (A U B)ᶜ = Aᶜ ∩ Bᶜ
        "(A_intersect_B)_complement": ["r2_A_not_B", "r2_B_not_A", "r2_None"], // (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
    };

    // Define region IDs for 3 sets (mapping assumes standard 8 regions)
     const venn3RegionIds = {
        // Mapping operations to region IDs
        // r3_A_only: A & !B & !C
        // r3_B_only: B & !A & !C
        // r3_C_only: C & !A & !B
        // r3_A_intersect_B_not_C: A & B & !C
        // r3_A_intersect_C_not_B: A & C & !B
        // r3_B_intersect_C_not_A: B & C & !A
        // r3_A_intersect_B_intersect_C: A & B & C
        // r3_None: !A & !B & !C (within U)
        "A": ["r3_A_only", "r3_A_intersect_B_not_C", "r3_A_intersect_C_not_B", "r3_A_intersect_B_intersect_C"],
        "B": ["r3_B_only", "r3_A_intersect_B_not_C", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C"],
        "C": ["r3_C_only", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C"],
        "U": ["r3_A_only", "r3_B_only", "r3_C_only", "r3_A_intersect_B_not_C", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C", "r3_None"],
        "Empty": [],
        "A_union_B": ["r3_A_only", "r3_B_only", "r3_A_intersect_B_not_C", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C"],
        "A_intersect_B": ["r3_A_intersect_B_not_C", "r3_A_intersect_B_intersect_C"],
        "A_diff_B": ["r3_A_only", "r3_A_intersect_C_not_B"],
        "B_diff_A": ["r3_B_only", "r3_B_intersect_C_not_A"],
        "A_complement": ["r3_B_only", "r3_C_only", "r3_B_intersect_C_not_A", "r3_None"],
        "B_complement": ["r3_A_only", "r3_C_only", "r3_A_intersect_C_not_B", "r3_None"],
        "C_complement": ["r3_A_only", "r3_B_only", "r3_A_intersect_B_not_C", "r3_None"],
        "A_union_B_union_C": ["r3_A_only", "r3_B_only", "r3_C_only", "r3_A_intersect_B_not_C", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C"],
        "A_intersect_B_intersect_C": ["r3_A_intersect_B_intersect_C"],
        "(A_union_B)_intersect_C": ["r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_A_intersect_B_intersect_C"],
        "(A_intersect_B)_union_C": ["r3_A_intersect_B_not_C", "r3_A_intersect_B_intersect_C", "r3_C_only", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A"], // Includes C and the intersection of A and B
        "(A_intersect_B)_diff_C": ["r3_A_intersect_B_not_C"],
        "(A_union_B)_complement": ["r3_None"], // (A U B)ᶜ = Aᶜ ∩ Bᶜ ∩ Cᶜ
        "(A_intersect_B)_complement": ["r3_A_only", "r3_B_only", "r3_C_only", "r3_A_intersect_C_not_B", "r3_B_intersect_C_not_A", "r3_None"], // (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
    };


    // Function to highlight regions based on selected operation and number of sets
    function highlightRegions(operation, numSets) {
        const currentSvg = document.getElementById(`venn-${numSets}-sets`);
        if (!currentSvg) return;

        const regionsToHighlight = (numSets === 2 ? venn2RegionIds : venn3RegionIds)[operation] || [];

        // Remove highlighting from all regions in the current diagram
        // Use a slight delay to allow fade-out transition before applying new highlights
         const allRegions = currentSvg.querySelectorAll('.venn-region');
         allRegions.forEach(path => {
             path.classList.remove('highlight');
         });

         // Wait for the fade-out (via transition) or immediately apply if no transition
         requestAnimationFrame(() => {
            regionsToHighlight.forEach(id => {
                const pathElement = document.getElementById(id);
                if (pathElement) {
                    pathElement.classList.add('highlight');
                }
            });
         });
    }

    // Function to update diagram based on selected operation and number of sets
    function updateDiagram() {
        const numSets = parseInt(document.querySelector('input[name="num-sets"]:checked').value);
        const selectElement = document.getElementById('operation-select');
        let selectedOperation = selectElement.value;

        // Show/hide appropriate SVG
        document.getElementById('venn-2-sets').classList.toggle('active', numSets === 2);
        document.getElementById('venn-3-sets').classList.toggle('active', numSets === 3);

        // Update options visibility for 3-set operations
        const threeSetOptions = document.querySelectorAll('#operation-select .for-3-sets');

        if (numSets === 2) {
             threeSetOptions.forEach(opt => opt.style.display = 'none');
             // If a 3-set specific operation was selected, switch to a default 2-set operation
             if (!venn2RegionIds[selectedOperation]) {
                 selectElement.value = 'A_union_B'; // Default to A U B
                 selectedOperation = 'A_union_B';
             }
        } else { // numSets === 3
             threeSetOptions.forEach(opt => opt.style.display = '');
              // If a 2-set specific operation like B_diff_A was selected, check if it's valid for 3 sets.
              // B_diff_A is valid for 3 sets, but options like (A_union_B)_complement might map differently.
              // We need to ensure the selected option exists in the 3-set map.
              if (!venn3RegionIds[selectedOperation]) {
                 // This case should be rare if basic ops are shared, but good for robustness.
                 // If the current selection isn't in the 3-set map, reset to a 3-set default.
                 selectElement.value = 'A_union_B_union_C'; // Default to A U B U C
                 selectedOperation = 'A_union_B_union_C';
              }
        }

        // Apply highlighting
        highlightRegions(selectedOperation, numSets);
    }

    // Initialize paths (note: placeholders are defined directly in HTML SVG for simplicity)
    // A real production app would use a library or calculated paths here.

    // Add event listeners
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('input[name="num-sets"]').forEach(radio => {
            radio.addEventListener('change', updateDiagram);
        });
        document.getElementById('operation-select').addEventListener('change', updateDiagram);
        document.getElementById('toggle-explanation').addEventListener('click', () => {
            const explanationDiv = document.getElementById('explanation');
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            // Optional: smooth toggle animation via CSS classes
            // explanationDiv.classList.toggle('visible', isHidden);
        });

        // Initial diagram update on load
        updateDiagram();
    });

</script>

<style>
    /* --- CSS Styling and Design --- */

    :root {
        --primary-color: #007BFF; /* A friendly blue */
        --secondary-color: #28A745; /* A vibrant green for highlighting */
        --background-light: #e9ecef; /* Light grey background */
        --container-bg: #ffffff; /* White for the app container */
        --border-color: #ced4da; /* Soft border */
        --text-color: #343a40; /* Dark grey text */
        --label-color: #6c757d; /* Slightly lighter label text */
        --shadow-subtle: rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif; /* Use a common web font */
        color: var(--text-color);
        line-height: 1.6;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 20px;
    }

    .interactive-app {
        margin: 20px auto;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
        box-shadow: 0 4px 12px var(--shadow-subtle); /* Subtle shadow */
        max-width: 500px; /* Limit width for better presentation */
        direction: rtl; /* Ensure RTL layout */
        text-align: right;
    }

    .interactive-app h2 {
         margin-top: 0;
         color: var(--secondary-color); /* Title inside app */
         text-align: center;
    }

    .controls {
        display: flex;
        flex-direction: column; /* Stack controls vertically on small screens */
        gap: 20px;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px dashed var(--border-color); /* Separator */
    }

     .control-group label {
         display: block;
         margin-bottom: 8px;
         font-weight: bold;
         color: var(--label-color);
     }

     .radio-group label {
         font-weight: normal; /* Not bold for radio labels */
     }

    .radio-group input[type="radio"] {
        margin-left: 5px; /* Space between radio and label */
    }


    select#operation-select {
        padding: 10px 15px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 1rem;
        cursor: pointer;
        background-color: #fff;
        appearance: none; /* Remove default arrow */
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23333%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2FSVG%3E'); /* Custom arrow */
        background-repeat: no-repeat;
        background-position: left 15px center; /* Position arrow on the left for RTL */
        background-size: 12px;
        padding-left: 40px; /* Make space for the arrow */
        width: 100%; /* Full width */
    }


    #venn-diagram-container {
        position: relative;
        width: 100%;
        max-width: 400px; /* Match viewBox width */
        margin: 0 auto 20px auto; /* Center and add margin below */
        overflow: hidden;
    }

    .venn-diagram {
        display: none;
        width: 100%;
        height: auto;
        border: 1px solid var(--border-color);
        background-color: var(--background-light); /* Light background for U */
        box-sizing: border-box;
        border-radius: 8px; /* Match container border radius */
        transition: opacity 0.5s ease-in-out; /* Smooth transition when switching SVGs */
        opacity: 0; /* Start hidden for transition */
    }

     .venn-diagram.active {
        display: block;
        opacity: 1; /* Fade in */
     }

    .universal-set {
        fill: none;
        stroke: var(--label-color);
        stroke-width: 2;
    }

    .venn-circle {
        fill: none;
        stroke: var(--primary-color); /* Circle outlines */
        stroke-width: 3; /* Thicker stroke for circles */
        pointer-events: none;
    }

    .set-label {
        font-size: 20px; /* Slightly larger labels */
        font-weight: bold;
        fill: var(--text-color);
        pointer-events: none;
        user-select: none; /* Prevent text selection */
    }

     .set-label.universe {
         fill: var(--label-color); /* U label color */
         font-size: 16px;
     }

     .set-label.A-label { fill: #FF6B6B; } /* Reddish */
     .set-label.B-label { fill: #4ECDC4; } /* Teal */
     .set-label.C-label { fill: #45B7D1; } /* Cyan */


    .venn-region {
        fill: none; /* Regions are initially not filled */
        fill-opacity: 0.9; /* Make highlight slightly opaque */
        stroke: none;
        transition: fill 0.4s ease-in-out; /* Smooth transition for highlighting */
        cursor: pointer; /* Hint that these areas are interactive (though clicking doesn't do anything yet) */
    }

    .venn-region.highlight {
        fill: var(--secondary-color); /* Highlight color (vibrant green) */
        animation: pulse 1.5s infinite alternate ease-in-out; /* Add pulse animation */
    }

    /* Pulse animation for highlighted regions */
    @keyframes pulse {
        0% { fill: var(--secondary-color); }
        100% { fill: #3cb371; } /* Slightly different green shade */
    }


    button#toggle-explanation {
        display: block; /* Make button a block element */
        margin: 20px auto; /* Center button */
        padding: 12px 25px;
        font-size: 1rem;
        color: #fff;
        background-color: var(--primary-color);
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button#toggle-explanation:hover {
        background-color: #0056b3; /* Darker shade on hover */
    }

    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
        box-shadow: 0 4px 12px var(--shadow-subtle);
        direction: rtl;
        text-align: right;
        /* Optional: add a CSS class for fade animation */
        /*
        transition: opacity 0.5s ease-in-out;
        opacity: 0;
        max-height: 0;
        overflow: hidden;
        */
    }

    /*
    #explanation.visible {
         opacity: 1;
         max-height: 2000px; // Needs a large enough value to allow content
    }
    */

    #explanation h2, #explanation h3 {
        color: var(--primary-color);
        margin-top: 15px;
        margin-bottom: 10px;
        text-align: right; /* Align explanation headings to the right */
    }

    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust margin for RTL list */
        padding-right: 0;
    }
    #explanation li {
        margin-bottom: 10px;
    }

     p.interactive-hint {
         text-align: center;
         font-size: 0.9rem;
         color: var(--label-color);
         margin-top: 15px;
     }

</style>