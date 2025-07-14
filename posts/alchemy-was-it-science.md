---
title: "אלכימיה: האם זה היה מדע?"
english_slug: alchemy-was-it-science
category: "היסטוריה של המדע"
tags:
  - אלכימיה
  - היסטוריה
  - מדע
  - ימי הביניים
  - כימיה
---
# אלכימיה: האם זה היה מדע?

האם שמעתם על אלכימאים שניסו להפוך עופרת לזהב? נדמה לנו שהם היו רק קוסמים שרלטנים, אבל האם ידעתם שמאחורי האגדות הסתתר חיפוש אמיתי אחר ידע, שהניח את היסודות למדע המודרני? בואו נחקור במעבדה הווירטואלית!

<div id="alchemy-lab">
    <h2>מעבדת האלכימאי</h2>
    <div id="mission-area">
        <p><strong>המשימה:</strong> <span id="current-mission">נסה ליצור "זהב אלכימי" משילוב מתכות!</span></p>
    </div>
    <div class="lab-container">
        <div id="ingredients">
            <h3>מרכיבים מיסטיים</h3>
            <div class="ingredient" draggable="true" data-name="Lead">עופרת (סמל שבתאי)</div>
            <div class="ingredient" draggable="true" data-name="Copper">נחושת (סמל נוגה)</div>
            <div class="ingredient" draggable="true" data-name="Sulfur">גופרית (עיקרון הבערה)</div>
            <div class="ingredient" draggable="true" data-name="Mercury">כספית (עיקרון הנזילות)</div>
            <div class="ingredient" draggable="true" data-name="Water">מים (עיקרון הלחות)</div>
            <div class="ingredient" draggable="true" data-name="Salt">מלח (עיקרון המוצקות)</div>
            <div class="ingredient" draggable="true" data-name="Unknown Herb">עשב מסתורי</div>
        </div>
        <div id="equipment">
            <h3>כלים עתיקים</h3>
            <div class="equipment-item tool" draggable="true" data-name="Furnace">כור / אטאנור</div>
            <div class="equipment-item tool" draggable="true" data-name="Distillation">מתקן זיקוק</div>
        </div>
        <div id="workbench">
             <h3>שולחן עבודה</h3>
             <div id="beaker" class="equipment-item" data-name="Beaker">
                 <p>כוס כימית<br>(גרור מרכיבים לכאן)</p>
                 <div id="beaker-contents">
                     <div class="liquid"></div>
                 </div>
                 <button id="reset-beaker" title="רוקן ושטוף כוס">X</button>
             </div>
             <div id="reaction-area" class="equipment-item" data-name="Reaction Area">
                 <p>אזור התגובה<br>(גרור כוס עם מרכיבים, ואז כלי)</p>
                 <div id="equipment-in-place"></div>
             </div>
             <button id="perform-action">בצע את התהליך</button>
        </div>
    </div>
    <div id="results-area">
        <h3>תצפית אלכימית</h3>
        <div id="results-text">התחל בבחירת מרכיבים וגרור אותם לכוס הכימית. לאחר מכן, גרור את הכוס המלאה לאזור התגובה, הוסף את הכלי המתאים (כור או זיקוק), ולחץ 'בצע את התהליך'.</div>
        <div id="results-visual"></div>
    </div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;700&family=Noto+Sans+Hebrew:wght@400;700&display=swap');

#alchemy-lab {
    font-family: 'Noto Sans Hebrew', sans-serif;
    direction: rtl;
    text-align: right;
    background-color: #fbf5eb; /* Lighter, warm background */
    border: 2px solid #a08a78; /* Earthy border */
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    position: relative; /* For potential absolute children */
}

#alchemy-lab h2, #alchemy-lab h3 {
    text-align: center;
    color: #5a3a2a; /* Darker earth tone */
    font-family: 'Frank Ruhl Libre', serif;
    margin-bottom: 15px;
}

#mission-area {
    text-align: center;
    margin-bottom: 20px;
    padding: 10px;
    background-color: #e0d0c0;
    border-radius: 6px;
    border: 1px dashed #a08a78;
}

#mission-area strong {
    color: #4a2e1a;
}

.lab-container {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    margin-bottom: 25px;
    justify-content: center; /* Center items */
}

#ingredients, #equipment {
    flex: 1;
    min-width: 150px; /* Slightly wider */
    max-width: 200px; /* Limit max width */
    border: 1px dashed #a08a78;
    padding: 15px;
    border-radius: 8px;
    background-color: #fffdf8; /* Lighter background */
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
}

#ingredients h3, #equipment h3 {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: center;
    color: #6a4e3a;
}

.ingredient, .equipment-item.tool { /* Apply tool style to equipment items */
    background-color: #d4c2b1; /* Muted tone */
    border: 1px solid #a08a78;
    padding: 10px;
    margin-bottom: 8px; /* More space */
    border-radius: 6px;
    cursor: grab;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3); /* Softer shadow */
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    position: relative; /* For pseudo-elements */
}

.ingredient:hover, .equipment-item.tool:hover {
    transform: translateY(-3px); /* Lift effect */
    box-shadow: 3px 3px 8px rgba(0,0,0,0.4);
}

.ingredient:active, .equipment-item.tool:active {
     cursor: grabbing;
     transform: scale(0.98); /* Slightly shrink on grab */
     box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}

/* Add simple icons via pseudo-elements (example for furnace) */
.equipment-item.tool[data-name="Furnace"]::before {
    content: "\1F525"; /* Fire emoji */
    margin-left: 5px;
    font-size: 1.1em;
}
.equipment-item.tool[data-name="Distillation"]::before {
     content: "\2697"; /* Alembic/Retort symbol */
     margin-left: 5px;
     font-size: 1.1em;
}
/* More icon ideas: Lead: ♄, Copper: ♀, Sulfur: 🜢, Mercury: ☿, Water: 🜄, Salt: 🜗 */
.ingredient[data-name="Lead"]::before { content: "♄ "; margin-left: 5px; }
.ingredient[data-name="Copper"]::before { content: "♀ "; margin-left: 5px; }
.ingredient[data-name="Sulfur"]::before { content: "🜢 "; margin-left: 5px; }
.ingredient[data-name="Mercury"]::before { content: "☿ "; margin-left: 5px; }
.ingredient[data-name="Water"]::before { content: "🜄 "; margin-left: 5px; }
.ingredient[data-name="Salt"]::before { content: "🜗 "; margin-left: 5px; }


#workbench {
    flex: 2;
    min-width: 350px; /* Wider workbench */
    border: 3px solid #8b4513; /* Rich brown */
    padding: 20px;
    border-radius: 10px;
    background-color: #f5e8d0; /* Warm background */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

#workbench h3 {
     margin-top: 0;
     color: #4a2e1a;
}

#beaker, #reaction-area {
    width: 180px; /* Larger drop targets */
    height: 220px; /* Taller */
    border: 2px dashed #a08a78;
    border-radius: 10px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #5a3a2a;
    position: relative;
    transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.3s ease;
    overflow: hidden; /* Hide overflow content */
    cursor: default; /* Default cursor for drop targets */
}

#beaker[draggable="true"] {
    cursor: grab; /* Indicate when beaker can be dragged */
}


#beaker p, #reaction-area p {
    margin: 0;
    font-size: 0.9em;
    position: relative;
    z-index: 2; /* Ensure text is above liquid */
}

#beaker.drag-over, #reaction-area.drag-over {
    background-color: #ffe4b5; /* Moccasin */
    border-color: #a0522d; /* Sienna */
    transform: scale(1.02); /* Subtle scale animation on drag over */
}

#beaker-contents {
    position: absolute;
    bottom: 0;
    left: 5%; /* Slightly inset */
    right: 5%; /* Slightly inset */
    width: 90%;
    height: 0; /* Will be set by JS */
    background: linear-gradient(to top, rgba(100, 149, 237, 0.7), rgba(100, 149, 237, 0.3)); /* Gradient for liquid effect */
    transition: height 0.5s ease, background-color 0.5s ease;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    z-index: 1; /* Below text */
}

#beaker-contents .liquid {
    width: 100%;
    height: 100%;
    position: relative;
    /* Could add subtle animation here later */
}

/* Add visual ingredient cues within beaker contents */
#beaker-contents::before {
    content: attr(data-content); /* Display ingredient names */
    position: absolute;
    top: 5px;
    left: 5px;
    right: 5px;
    font-size: 0.7em;
    color: #333; /* Darker text on light liquid */
    text-align: right; /* RTL */
    white-space: pre-wrap; /* Allow line breaks */
    word-break: break-word;
    opacity: 0.9;
    z-index: 3; /* Above liquid */
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5); /* Make text readable */
}


#reset-beaker {
    position: absolute;
    top: 8px;
    right: 8px;
    background-color: #e74c3c; /* Red */
    color: white;
    border: none;
    border-radius: 50%;
    width: 25px; /* Slightly larger button */
    height: 25px;
    padding: 0;
    font-size: 1em; /* Larger font */
    cursor: pointer;
    line-height: 1;
    display: none; /* Initially hidden */
    z-index: 4; /* Above everything in beaker */
    box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    transition: background-color 0.2s ease, transform 0.1s ease;
}

#reset-beaker:hover {
    background-color: #c0392b;
    transform: rotate(90deg); /* Spin effect */
}
#reset-beaker:active {
     transform: scale(0.9);
}


#equipment-in-place {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column; /* Stack beaker and tool */
    justify-content: center;
    align-items: center;
    gap: 10px; /* Space between items */
    font-weight: bold;
    color: #4a2e1a;
}

#equipment-in-place .equipment-item {
    margin: 0;
    padding: 10px;
    width: 80%;
    height: auto; /* Auto height based on content */
    background-color: #e0d0c0;
    border: 2px solid #a08a78;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: default;
    box-shadow: none;
    text-align: center;
}

#equipment-in-place .equipment-item[data-name="Beaker in Place"] {
    height: 50%; /* Beaker takes up more space */
    position: relative;
    overflow: hidden;
    /* Add beaker content representation here if needed */
     background-color: #fff; /* White background for beaker body */
}

#equipment-in-place .equipment-item[data-name="Beaker in Place"]::before {
     content: "כוס";
     position: absolute;
     top: 50%;
     left: 50%;
     transform: translate(-50%, -50%);
     font-size: 1.2em;
     color: #5a3a2a;
     z-index: 2;
}

/* Visual liquid representation in beaker-in-place */
#equipment-in-place .equipment-item[data-name="Beaker in Place"] .in-place-liquid {
    position: absolute;
    bottom: 0;
    left: 10%;
    right: 10%;
    width: 80%;
    height: 30%; /* Example fixed height, could be dynamic */
    background-color: rgba(100, 149, 237, 0.7); /* Blue liquid */
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    z-index: 1;
}


#perform-action {
    padding: 12px 25px; /* Larger button */
    background-color: #5cb85c; /* Green */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em; /* Larger font */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    margin-top: 10px;
}

#perform-action:hover {
    background-color: #4cae4c;
}
#perform-action:active {
     transform: scale(0.98);
     box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}
#perform-action:disabled {
     background-color: #cccccc;
     cursor: not-allowed;
     box-shadow: none;
}

#results-area {
    border: 1px solid #a08a78;
    padding: 20px;
    border-radius: 8px;
    background-color: #fffdf8;
    margin-top: 20px;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

#results-area h3 {
    margin-top: 0;
    margin-bottom: 15px;
    color: #6a4e3a;
}

#results-text {
    margin-bottom: 15px;
    color: #333;
    white-space: pre-wrap; /* Allow line breaks from JS */
    min-height: 3em; /* Give it some space */
    display: flex;
    align-items: center;
    justify-content: center;
    font-style: italic; /* Results feel observational */
}

#results-visual {
    width: 80px; /* Result indicator size */
    height: 80px;
    border: 2px solid #8b4513;
    background-color: transparent; /* Default */
    border-radius: 50%; /* Circle shape initially */
    margin: 10px auto 0;
    transition: background-color 1s ease, border-color 0.5s ease, transform 0.5s ease, border-radius 0.5s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em; /* For potential icon/text */
    color: #fff;
}

/* Specific result styles */
.result-gold {
    background-color: gold;
    border-color: #b8860b; /* DarkGoldenRod */
    box-shadow: 0 0 15px gold;
    transform: scale(1.2) rotate(360deg); /* Spin and grow */
    border-radius: 8px; /* Maybe turn into an ingot shape visually? */
}
.result-cinnabar {
    background-color: #e74c3c; /* Red */
    border-color: #c0392b;
    transform: scale(1.1);
}
.result-black {
    background-color: #333;
    border-color: #111;
    border-radius: 4px; /* Powder shape */
}
.result-liquid {
    background-color: rgba(100, 149, 237, 0.7);
    border-color: royalblue;
    border-radius: 50%; /* Keep circle for liquid drop */
}
.result-clear {
    background-color: transparent;
    border-color: lightblue;
    border-style: dashed;
    border-radius: 50%;
}
.result-smoke {
     background: repeating-linear-gradient(-45deg, #ccc, #ccc 5px, #eee 5px, #eee 10px);
     border-color: grey;
     border-radius: 50%;
     animation: smoke-puff 1s infinite alternate;
}
.result-explosion {
    background-color: orange;
    border-color: red;
    animation: explode 0.5s forwards;
    border-radius: 50%;
}
.result-failure {
    background-color: #e0e0e0;
    border-color: #a0a0a0;
    transform: rotate(45deg); /* Indicate something went wrong */
    border-radius: 8px;
}


@keyframes smoke-puff {
    0% { transform: scale(0.8); opacity: 0.6; }
    100% { transform: scale(1.1); opacity: 1; }
}

@keyframes explode {
    0% { transform: scale(1); opacity: 1; }
    100% { transform: scale(2); opacity: 0; }
}


/* Explanation section styles */
#explanation {
    margin-top: 40px;
    border-top: 2px solid #a08a78;
    padding-top: 30px;
    background-color: #f8f0e8;
    border-radius: 8px;
    padding: 25px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

#explanation h2 {
    text-align: center;
    color: #4a2e1a;
    font-family: 'Frank Ruhl Libre', serif;
    margin-bottom: 20px;
}

#explanation h3 {
    color: #6a4e3a;
    margin-top: 25px;
    margin-bottom: 10px;
    font-family: 'Frank Ruhl Libre', serif;
    border-bottom: 1px solid #d0c0b0;
    padding-bottom: 5px;
}

#explanation p {
    line-height: 1.7;
    color: #333;
    margin-bottom: 15px;
    text-align: justify; /* Justify text for better readability */
}

#explanation ul {
    color: #333;
    margin-bottom: 15px;
    line-height: 1.6;
}

#explanation li {
     margin-bottom: 8px;
}


#show-explanation-button {
    display: block;
    width: fit-content;
    margin: 30px auto 0;
    padding: 12px 25px;
    background-color: #3498db; /* Blue */
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
}

#show-explanation-button:hover {
    background-color: #2980b9;
}

#show-explanation-button:active {
     transform: scale(0.98);
     box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}


.hidden {
    display: none;
}
</style>

<button id="show-explanation-button">חשוף סודות עתיקים (הסבר)</button>

<div id="explanation" class="hidden">
    <h2>העולם המסתורי של האלכימיה</h2>

    <p>אלכימיה, שקודמת לכימיה המודרנית, הייתה שילוב מרתק של פילוסופיה, מיסטיקה, אסטרולוגיה, רפואה, ואמנות מעבדתית. היא לא הייתה רק "הפיכת עופרת לזהב", אלא חיפוש עמוק להבנת ותמצות היקום, החומר, ואף הנפש.</p>

    <h3>מה הייתה אלכימיה? (מעבר לטרנסמוטציה)</h3>
    אלכימאים ביקשו להבין את ה"טבע" של החומרים ולשנות אותם. הם האמינו שניתן "לשפר" חומרים פשוטים ("לא מושלמים") לחומרים אצילים ("מושלמים"). המטרות המפורסמות היו טרנסמוטציה (הפיכת מתכות פשוטות לזהב או כסף), חיפוש 'אבן החכמים' (שמאפשרת טרנסמוטציה ומעניקה חיים ארוכים), ויצירת שיקויים ותרופות מרפא. אך הם עסקו גם בפיתוח שיטות להפקת חומרים שימושיים כמו צבעים, חומצות, מלחים ומוצרי קוסמטיקה, וצברו ידע ניסיוני רב.

    <h3>הקשר ההיסטורי והפילוסופי</h3>
    אלכימיה צמחה במצרים העתיקה, התפתחה בעולם היווני-רומי, שגשגה בעולם הערבי (שהיה בית לתרגום ופיתוח טקסטים אלכימיים רבים), והגיעה לאירופה בימי הביניים ובתקופת הרנסנס. היא הושפעה עמוקות מפילוסופים כמו אריסטו (תורת ארבעת היסודות), ורבים ראו בה דרך לגלות סודות קוסמיים ורוחניים. סימני האלכימיה קשורים לעיתים קרובות לסמלי כוכבי לכת, מה שמדגיש את הקשר לאסטרולוגיה.

    <h3>מטרות מרכזיות</h3>
    <ul>
        <li><strong>טרנסמוטציה (Transmutation):</strong> הפיכת "הבסיס" ל"אציל".</li>
        <li><strong>אבן החכמים (The Philosopher's Stone):</strong> חומר אגדי, מרכז העבודה האלכימית הגדולה, עם סגולות טרנסמוטציה וחיים.</li>
        <li><strong>שיקוי חיים (Elixir of Life):</strong> לריפוי מחלות והארכת חיים.</li>
        <li>**רפואה (Iatrochemistry):** ייצור תרופות מבוססות כימיה.</li>
        <li>**הפקת חומרים:** יצירת פיגמנטים, חומצות, מלכים, זכוכית ועוד לשימושים יומיומיים.</li>
    </ul>

    <h3>יסודות תיאורטיים (במושגים אלכימיים)</h3>
    *   **תורת ארבעת היסודות (אריסטו):** הכל מורכב מאדמה (יבש וקר), מים (לח וקר), אוויר (לח וחם), ואש (יבש וחם). שינוי יחסי היסודות יכול לשנות את החומר.
    *   **תורת שלושת העקרונות (פארצלסוס):** חומרים ניתנים לפירוק לגופרית (עקרון הבעירה/הנשמה), כספית (עקרון הנזילות/הרוח), ומלח (עקרון המוצקות/הגוף). שינוי יחסיהם יוצר חומרים שונים.
    *   **עקרונות אלכימיים:** תהליכים כמו חימום, זיקוק, טיהור, איחוד, הפרדה - נתפסו כתהליכים המשקפים תהליכים קוסמיים ורוחניים, שמטרתם "לטהר" את החומר ולהביאו למצבו המושלם.

    <h3>שיטות עבודה וכלים מעבדתיים</h3>
    האלכימאים היו חוקרים מעבדתיים מדופלמים. הם פיתחו ושיכללו שיטות רבות שמשמשות בכימיה עד היום: חימום וקלייה, זיקוק (באמצעות אלאמביק או רטורט), סינון, אידוי, סובלימציה, גיבוש. הכלים המעבדתיים שלהם - כורים, כוסות, מבחנות, מתקני זיקוק - הם אבות הכלים המודרניים.

    <h3>מורשת האלכימיה למדע המודרני</h3>
    על אף שהתיאוריות האלכימיות נזנחו לטובת המדע המודרני (המבוסס על אטומים, מולקולות וחוקים כמותיים), תרומתה למדע עצומה:
    *   **פיתוח טכניקות מעבדה:** שיטות עבודה וכלים רבים עברו ישירות מהאלכימיה לכימיה.
    *   **גילוי חומרים:** אלכימאים גילו וחקרו חומרים רבים כמו חומצות (גופרתית, חנקתית), מלכים שונים, אלכוהול, ועוד.
    *   **ביסוס העבודה הניסיונית:** הדגש על ניסוי וטעייה, תצפית שיטתית ותיעוד (גם אם בכתב חידה) הניח את היסודות לגישה המדעית הניסיונית.
    *   **תרומה לרפואה:** אלכימאים רבים היו גם רופאים (כמו פארצלסוס), ופיתחו תרופות חדשות על בסיס ידע כימי.

    <p>אלכימיה הייתה גשר בין חשיבה פילוסופית-מיסטית לבין חקר מעבדתי אמפירי, וסיפורה הוא חלק מרתק מהמסע האנושי להבנת העולם החומרני.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const ingredientsContainer = document.getElementById('ingredients');
    const equipmentContainer = document.getElementById('equipment');
    const beaker = document.getElementById('beaker');
    const beakerContents = document.getElementById('beaker-contents');
    const beakerLiquid = beakerContents.querySelector('.liquid'); // Get the liquid element
    const resetBeakerButton = document.getElementById('reset-beaker');
    const reactionArea = document.getElementById('reaction-area');
    const equipmentInPlace = document.getElementById('equipment-in-place');
    const performActionButton = document.getElementById('perform-action');
    const resultsText = document.getElementById('results-text');
    const resultsVisual = document.getElementById('results-visual');
    const showExplanationButton = document.getElementById('show-explanation-button');
    const explanationDiv = document.getElementById('explanation');

    let currentBeakerIngredients = []; // Array to store ingredient names
    let reactionState = {
        beakerReady: false, // Beaker with ingredients is in the reaction area
        toolReady: false,   // A tool is in the reaction area
        beakerContents: [] // Store contents when beaker is moved to reaction area
    };

    // --- Drag and Drop Logic ---

    // Make ingredients draggable
    document.querySelectorAll('.ingredient').forEach(item => {
        item.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/ingredient', e.target.dataset.name); // Use a specific data type
            e.dataTransfer.effectAllowed = 'copy';
            e.target.classList.add('dragging'); // Add visual cue
        });
         item.addEventListener('dragend', (e) => {
             e.target.classList.remove('dragging');
         });
    });

    // Make tools draggable
    document.querySelectorAll('.equipment-item.tool').forEach(item => {
         item.addEventListener('dragstart', (e) => {
             e.dataTransfer.setData('text/tool', e.target.dataset.name); // Use a specific data type
             e.dataTransfer.effectAllowed = 'move';
             e.target.classList.add('dragging'); // Add visual cue
         });
          item.addEventListener('dragend', (e) => {
              e.target.classList.remove('dragging');
          });
    });


    // Beaker Drop Target for Ingredients
    beaker.addEventListener('dragover', (e) => {
        // Only allow drop if the dragged item is an ingredient
        if (e.dataTransfer.types.includes('text/ingredient')) {
            e.preventDefault(); // Allow drop
            beaker.classList.add('drag-over');
            e.dataTransfer.dropEffect = 'copy';
        }
    });

    beaker.addEventListener('dragleave', () => {
        beaker.classList.remove('drag-over');
    });

    beaker.addEventListener('drop', (e) => {
        e.preventDefault();
        beaker.classList.remove('drag-over');

        // Only process if the dragged item is an ingredient
        if (e.dataTransfer.types.includes('text/ingredient')) {
             const ingredientName = e.dataTransfer.getData('text/ingredient');

             if (currentBeakerIngredients.length < 4) { // Limit contents for simplicity
                 currentBeakerIngredients.push(ingredientName);
                 updateBeakerDisplay();
                 resultsText.textContent = `${ingredientName} נוסף לכוס.`;
             } else {
                 resultsText.textContent = 'הכוס מלאה מדי, לא ניתן להוסיף מרכיבים נוספים כרגע.';
             }
        }
    });

    // Make Beaker draggable *only when* it has contents
    // This is handled in updateBeakerDisplay and drop logic

    // Reset Beaker Button
    resetBeakerButton.addEventListener('click', () => {
        currentBeakerIngredients = [];
        updateBeakerDisplay();
        resultsText.textContent = 'הכוס רוקנה ונשטפה. התחל מחדש.';
        resetResultsArea();
        // Ensure beaker is not draggable if empty
        beaker.removeAttribute('draggable');
    });

    // Reaction Area Drop Target for Beaker and Tools
    reactionArea.addEventListener('dragover', (e) => {
         // Allow drop if dragging the beaker or a tool
         if (e.dataTransfer.types.includes('text/ingredient') && beaker.getAttribute('draggable') === 'true') {
              // This check prevents dragging ingredients directly to reaction area
               return;
         }
          if (e.dataTransfer.types.includes('text/tool') || (e.dataTransfer.types.includes('text/ingredient') && beaker.getAttribute('draggable') === 'true')) { // Beaker is dragged as type 'ingredient' from its drop logic
             e.preventDefault(); // Allow drop
             reactionArea.classList.add('drag-over');
             e.dataTransfer.dropEffect = 'move'; // Use move effect
         }
    });

    reactionArea.addEventListener('dragleave', () => {
        reactionArea.classList.remove('drag-over');
    });

     reactionArea.addEventListener('drop', (e) => {
         e.preventDefault();
         reactionArea.classList.remove('drag-over');

         // Check what was dropped
         const isBeakerDrop = e.dataTransfer.types.includes('text/ingredient') && beaker.getAttribute('draggable') === 'true';
         const isToolDrop = e.dataTransfer.types.includes('text/tool');

         if (isBeakerDrop) {
             if (!reactionState.beakerReady) {
                 // Move beaker to reaction area state
                 reactionState.beakerReady = true;
                 reactionState.beakerContents = [...currentBeakerIngredients]; // Store contents
                 // Visual update: Show beaker in reaction area
                 equipmentInPlace.innerHTML = '<div class="equipment-item" data-name="Beaker in Place">כוס מוכנה<div class="in-place-liquid"></div></div>'; // Add liquid visual cue
                 resultsText.textContent = 'כוס כימית עם מרכיבים הונחה באזור התגובה. כעת גרור כלי פעולה (כור או זיקוק) לכאן.';
                 // Beaker is now 'used', reset the original beaker state and draggability
                 currentBeakerIngredients = [];
                 updateBeakerDisplay(); // Clears original beaker
                 beaker.removeAttribute('draggable'); // Make original beaker non-draggable
             } else {
                  resultsText.textContent = 'כבר יש כוס באזור התגובה.';
             }
         } else if (isToolDrop) {
              const toolName = e.dataTransfer.getData('text/tool');
             if (reactionState.beakerReady && !reactionState.toolReady) {
                 // Add tool to reaction area state
                 reactionState.toolReady = true;
                 reactionState.actionTool = toolName;
                 // Visual update: Show tool in reaction area
                 equipmentInPlace.innerHTML += `<div class="equipment-item" data-name="${toolName} in Place">${toolName}</div>`;
                 performActionButton.disabled = false; // Enable action button
                 resultsText.textContent = `הכוס מוכנה לפעולת ${toolName}. לחץ 'בצע את התהליך'.`;
             } else if (!reactionState.beakerReady) {
                  resultsText.textContent = 'הנח קודם את הכוס הכימית באזור התגובה, ורק אז את הכלי לפעולה.';
             } else { // reactionState.toolReady is true
                   resultsText.textContent = 'כבר יש כלי פעולה באזור התגובה.';
             }
         } else {
             resultsText.textContent = 'ניתן לגרור לכאן רק את הכוס הכימית או כלי פעולה.';
         }
     });


    // Update Beaker Display
    function updateBeakerDisplay() {
        const contentText = currentBeakerIngredients.join('\n');
        beakerContents.setAttribute('data-content', contentText);

        const maxLiquidHeight = 180; // Max height inside beaker (beaker height 220 - padding/text space)
        const contentHeight = currentBeakerIngredients.length > 0 ?
                              Math.min(currentBeakerIngredients.length * 40 + 20, maxLiquidHeight) // Simple linear fill + base level
                              : 0; // Empty

        // Smooth transition for liquid height and color
        beakerLiquid.style.height = `${contentHeight}px`;

        // Change liquid color slightly based on ingredients (very basic)
        if (currentBeakerIngredients.includes('Mercury') || currentBeakerIngredients.includes('Sulfur')) {
             beakerLiquid.style.backgroundColor = 'rgba(220, 50, 50, 0.7)'; // Reddish tint
             beakerLiquid.style.background = 'linear-gradient(to top, rgba(220, 50, 50, 0.7), rgba(220, 50, 50, 0.3))';
        } else if (currentBeakerIngredients.includes('Copper') || currentBeakerIngredients.includes('Lead')) {
            beakerLiquid.style.backgroundColor = 'rgba(150, 100, 50, 0.7)'; // Brownish tint
             beakerLiquid.style.background = 'linear-gradient(to top, rgba(150, 100, 50, 0.7), rgba(150, 100, 50, 0.3))';
        } else {
             beakerLiquid.style.backgroundColor = 'rgba(100, 149, 237, 0.7)'; // Default blue
             beakerLiquid.style.background = 'linear-gradient(to top, rgba(100, 149, 237, 0.7), rgba(100, 149, 237, 0.3))';
        }


        // Show/hide reset button and make beaker draggable
        if (currentBeakerIngredients.length > 0) {
            resetBeakerButton.style.display = 'block';
            beaker.setAttribute('draggable', 'true'); // Make beaker draggable only when full
            // Beaker should only be draggable to the reaction area
            beaker.addEventListener('dragstart', handleBeakerDragStart);
            beaker.addEventListener('dragend', handleBeakerDragEnd);
        } else {
            resetBeakerButton.style.display = 'none';
             beaker.removeAttribute('draggable');
             beaker.removeEventListener('dragstart', handleBeakerDragStart);
             beaker.removeEventListener('dragend', handleBeakerDragEnd);
        }
    }

    // Custom dragstart handler for the beaker
     function handleBeakerDragStart(e) {
         if (currentBeakerIngredients.length > 0) {
              // Data transfer type should differentiate from ingredients
              e.dataTransfer.setData('text/ingredient', beaker.dataset.name); // Still use 'text/ingredient' for drop logic, but check target
              e.dataTransfer.effectAllowed = 'move';
              beaker.classList.add('dragging'); // Add visual cue
         } else {
             e.preventDefault(); // Don't allow drag if empty
         }
     }
     function handleBeakerDragEnd(e) {
          beaker.classList.remove('dragging');
     }


    // --- Reaction Logic ---
    performActionButton.addEventListener('click', () => {
        if (reactionState.beakerReady && reactionState.toolReady) {
            simulateAlchemy(reactionState.beakerContents, reactionState.actionTool);

            // Reset the reaction area after performing action (simulate consumption)
            reactionState = { beakerReady: false, toolReady: false, beakerContents: [] };
            equipmentInPlace.innerHTML = '';
            performActionButton.disabled = true;
            resetResultsArea(); // Clear previous visual result

        } else {
            resultsText.textContent = 'אנא גרור את הכוס המלאה לאזור התגובה, ולאחר מכן כלי פעולה מתאים.';
        }
    });

    function simulateAlchemy(contents, action) {
        const sortedContents = [...contents].sort().join('+'); // Sort for easier matching
        let resultDescription = 'התהליך הסתיים... התוצאה אינה ברורה. נסה שילוב אחר!';
        let visualClass = 'result-failure'; // Default failure/unknown state

        // Reset visual before animating new one
        resultsVisual.className = ''; // Remove all classes
        resultsVisual.offsetWidth; // Trigger reflow to restart animation

        // Alchemical Simulation Logic based on historical practices and legends
        if (action === 'Furnace') { // Processes involving heat, calcination, fusion
            if (sortedContents === 'Copper+Sulfur') {
                resultDescription = 'חימום נחושת עם גופרית יוצר סולפיד נחושת שחור/אפור. תצפית חשובה על ריאקציות מתכות!';
                visualClass = 'result-black';
            } else if (sortedContents === 'Lead+Sulfur') {
                 resultDescription = 'קלייה של עופרת וגופרית יוצרת חומר כהה (עופרת גופרתית). בסיס לחקר מינרלים!';
                 visualClass = 'result-black';
             } else if (sortedContents === 'Mercury+Sulfur') {
                 resultDescription = 'אח! השילוב האדום הגדול! חימום כספית עם גופרית יוצר Cinnabar (כספית גופרתית), חומר יפהפה שנקשר למאגיה ורפואה. קרוב לאבן החכמים? אולי...';
                 visualClass = 'result-cinnabar'; // Red color
             } else if (contents.includes('Lead') && contents.includes('Copper') && contents.includes('Sulfur') && contents.includes('Mercury') && contents.length >= 4) {
                 // The legendary attempt for gold (often involving lead, copper, sulfur, mercury as bases)
                 if (Math.random() < 0.15) { // Low probability of 'success' (illusionary gold)
                     resultDescription = 'אור בוהק מילא את הכור! החומרים השתנו באופן מופלא... זה נראה כמו... **זהב**! האם השגת את הפילוסופים? דרוש טיהור נוסף...';
                     visualClass = 'result-gold';
                 } else {
                     resultDescription = 'החום עשה את שלו, אבל התוצאה רחוקה מזהב. עיסה סמיכה וכהה נותרה מאחור.';
                      visualClass = 'result-black';
                 }
             } else if (contents.includes('Water') && action === 'Furnace') {
                  resultDescription = 'חימום מים בכלי סגור עם חומרים אחרים יכול ליצור אדים ולחץ. מסוכן!';
                  visualClass = 'result-explosion'; // Indicate danger/minor explosion
             }
            else {
                 resultDescription = `חימום ה${contents.join(', ')}: התוצאה אינה מוכרת בספרים העתיקים. נסה ללמוד מהתצפית.`;
                 visualClass = 'result-failure';
            }
        } else if (action === 'Distillation') { // Processes involving purification via evaporation/condensation
             if (sortedContents === 'Salt+Water') {
                 resultDescription = 'המים מתאדים ומתעבים במתקן הזיקוק, ומשאירים את המלח מאחור. זוהי טכניקת טיהור חשובה ביותר!';
                 visualClass = 'result-clear'; // Represent clear liquid
             } else if (contents.includes('Unknown Herb') && contents.includes('Water') && contents.length === 2) {
                 resultDescription = 'זיקוק העשב המסתורי עם מים... טפטף נוזל שקוף וריחני. אולי זה שיקוי מרפא או רעל מסוכן?';
                 visualClass = 'result-liquid'; // Represent liquid drop
             } else if (contents.includes('Mercury') && contents.length === 1) {
                 resultDescription = 'כספית מזוקקת! "הכספית הפילוסופית" - מרכיב מפתח בתורות רבות. מבריקה ונקייה!';
                 visualClass = 'result-liquid'; // Represent liquid metal (mercury is liquid)
                  resultsVisual.style.backgroundColor = 'silver'; // Special color for mercury
                  resultsVisual.style.borderRadius = '50%';
             }
            else {
                resultDescription = `זיקוק ה${contents.join(', ')}: המתקן טפטף מעט נוזל, אך התוצאה מעורפלת.`;
                 visualClass = 'result-liquid';
            }
        } else {
             resultDescription = 'כלי הפעולה אינו מוכר או אינו מתאים לשילוב זה.';
             visualClass = 'result-failure';
        }

        // Update results display
        resultsText.textContent = `פעולה: ${action}\nמרכיבים: ${contents.join(', ')}\nתוצאה: ${resultDescription}`;

        // Apply visual result class (triggers CSS animations/styles)
        resultsVisual.classList.add(visualClass);

        // Specific override for mercury visual if needed
         if (visualClass !== 'result-liquid' || !contents.includes('Mercury') || contents.length > 1 || action !== 'Distillation') {
             resultsVisual.style.backgroundColor = ''; // Reset special color if not pure mercury
             resultsVisual.style.borderRadius = '50%'; // Reset shape if not special
             resultsVisual.style.borderStyle = 'solid'; // Reset border style
         }

         if (visualClass === 'result-clear') {
             resultsVisual.style.borderStyle = 'dashed';
         }

         // Ensure gold result is visually distinct if it happened
         if (visualClass === 'result-gold') {
             resultsVisual.style.backgroundColor = 'gold';
             resultsVisual.style.borderColor = '#b8860b';
             resultsVisual.style.borderRadius = '8px'; // Ingot shape hint
         }

    }

    function resetResultsArea() {
        resultsVisual.className = ''; // Remove all classes
        resultsVisual.style.backgroundColor = 'transparent';
        resultsVisual.style.borderColor = '#8b4513';
        resultsVisual.style.borderRadius = '50%'; // Reset to default shape
        resultsVisual.style.transform = 'none'; // Reset animation transform
        resultsVisual.style.borderStyle = 'solid';
    }


    // --- Explanation Toggle ---
    showExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.classList.contains('hidden');
        if (isHidden) {
            explanationDiv.classList.remove('hidden');
            showExplanationButton.textContent = 'הסתר סודות עתיקים';
        } else {
            explanationDiv.classList.add('hidden');
            showExplanationButton.textContent = 'חשוף סודות עתיקים (הסבר)';
        }
    });

    // Initial state setup
    performActionButton.disabled = true;
    updateBeakerDisplay(); // Set initial beaker state (empty, not draggable)
    resetResultsArea(); // Set initial results state

    // Prevent default dragover/drop for the whole document body
    // to avoid accidentally dropping things outside valid zones
    document.body.addEventListener('dragover', function(e) {
        if (!e.target.closest('#alchemy-lab')) { // Check if drag is happening outside the lab
            e.preventDefault();
        }
    });

    document.body.addEventListener('drop', function(e) {
         if (!e.target.closest('#alchemy-lab')) { // Check if drop is happening outside the lab
            e.preventDefault();
        }
    });

});
</script>
```