---
title: "טרנזיסטורים כשערים לוגיים: איך המעבד שלך 'חושב'?"
english_slug: transistors-as-logic-gates-how-your-cpu-thinks
category: "מדעי המחשב"
tags: ["טרנזיסטורים", "שערים לוגיים", "מעבד", "חומרה דיגיטלית", "אלקטרוניקה"]
---
# טרנזיסטורים כשערים לוגיים: המפסק שמניע את המחשב
מכירים את ה"מוח" של המחשב? זה המעבד. הוא מבצע טריליוני פעולות בשנייה, אבל איך הוא מקבל החלטות במהירות האור? הסוד טמון במתגים אלקטרוניים זעירים: טרנזיסטורים. בואו נצלול פנימה ונראה איך הם מרכיבים את אבני הבניין הבסיסיות של כל חישוב דיגיטלי - השערים הלוגיים.

<div id="app-container" class="interactive-module">
    <div class="controls-panel">
        <div class="controls-group">
             <h2>בחרו שער לוגי להתנסות:</h2>
            <div class="gate-selector">
                <label class="radio-label">
                    <input type="radio" name="gate" value="NOT" checked>
                    <span class="gate-name">NOT</span>
                    <span class="gate-desc">הופך את המצב (0 ל-1, 1 ל-0)</span>
                </label>
                <label class="radio-label">
                    <input type="radio" name="gate" value="NAND">
                    <span class="gate-name">NAND</span>
                    <span class="gate-desc">11 נותן 0, כל השאר 1</span>
                </label>
                <label class="radio-label">
                    <input type="radio" name="gate" value="NOR">
                     <span class="gate-name">NOR</span>
                     <span class="gate-desc">00 נותן 1, כל השאר 0</span>
                 </label>
            </div>
        </div>

        <div id="inputs-container" class="controls-group">
            <h2>שלטו במתח הכניסות:</h2>
            <p class="input-info"> (מתח מעל 2.5V נחשב '1' לוגי)</p>
            <div id="inputA" class="input-control">
                <label for="voltageA" class="input-label">כניסה A:</label>
                <input type="range" id="voltageA" min="0" max="5" value="0" step="0.1">
                <div class="input-feedback">
                    <span class="voltage-display">0.0V</span>
                    <span class="logic-display">(0 לוגי)</span>
                </div>
            </div>
            <div id="inputB" class="input-control" style="display: none;">
                <label for="voltageB" class="input-label">כניסה B:</label>
                <input type="range" id="voltageB" min="0" max="5" value="0" step="0.1">
                 <div class="input-feedback">
                    <span class="voltage-display">0.0V</span>
                    <span class="logic-display">(0 לוגי)</span>
                 </div>
            </div>
        </div>
    </div>

    <div class="circuit-area">
        <div id="circuit-diagram-not" class="circuit-diagram active">
            <div class="diagram-title">שער NOT (אינוורטר)</div>
             <div class="diagram-subtitle">היציאה הפוכה לכניסה</div>
            <div class="diagram-components">
                <div class="component voltage-source">+Vcc (5V)</div>
                <div class="component resistor">נגד</div>
                <div class="component transistor" id="transistor-not">טרנזיסטור<br>(NMOS)</div>
                 <div class="component ground">הארקה (0V)</div>
                <div class="component output" id="output-not">מוצא Out</div>
                <div class="component input-point" id="input-point-not">כניסה A</div>

                <!-- Connections & Flow Indicators -->
                <div class="connection conn-vcc-resistor"></div>
                 <div class="connection conn-resistor-transistor"></div>
                 <div class="connection conn-transistor-ground"></div>
                <div class="connection conn-input-a-gate"></div>
                <div class="connection conn-output-line"></div>

                 <div class="flow-indicator flow-vcc-resistor"></div>
                 <div class="flow-indicator flow-resistor-transistor"></div>
                <div class="flow-indicator flow-transistor-ground"></div>
            </div>
        </div>

        <div id="circuit-diagram-nand" class="circuit-diagram">
            <div class="diagram-title">שער NAND</div>
             <div class="diagram-subtitle">היציאה 0 רק אם A=1 וגם B=1</div>
            <div class="diagram-components">
                <div class="component voltage-source">+Vcc (5V)</div>
                <div class="component resistor">נגד</div>
                 <div class="component ground">הארקה (0V)</div>

                <div class="component transistor transistor-a" id="transistor-nand-a">טרנזיסטור A</div>
                <div class="component transistor transistor-b" id="transistor-nand-b">טרנזיסטור B</div>
                 <div class="component output" id="output-nand">מוצא Out</div>
                 <div class="component input-point input-point-a" id="input-point-nand-a">כניסה A</div>
                 <div class="component input-point input-point-b" id="input-point-nand-b">כניסה B</div>

                 <!-- Connections & Flow Indicators -->
                <div class="connection conn-nand-vcc-resistor"></div>
                 <div class="connection conn-nand-resistor-transistora"></div>
                 <div class="connection conn-nand-transistora-transistorb"></div>
                 <div class="connection conn-nand-transistorb-ground"></div>
                <div class="connection conn-nand-input-a-gate"></div>
                <div class="connection conn-nand-input-b-gate"></div>
                <div class="connection conn-nand-output-line"></div>

                <div class="flow-indicator flow-nand-vcc-resistor"></div>
                 <div class="flow-indicator flow-nand-resistor-transistora"></div>
                 <div class="flow-indicator flow-nand-transistora-transistorb"></div>
                 <div class="flow-indicator flow-nand-transistorb-ground"></div>
            </div>
        </div>

        <div id="circuit-diagram-nor" class="circuit-diagram">
            <div class="diagram-title">שער NOR</div>
            <div class="diagram-subtitle">היציאה 1 רק אם A=0 וגם B=0</div>
            <div class="diagram-components">
                 <div class="component voltage-source">+Vcc (5V)</div>
                <div class="component ground">הארקה (0V)</div>
                 <div class="component resistor resistor-nor-top">נגד</div>

                 <div class="component transistor transistor-a" id="transistor-nor-a">טרנזיסטור A</div>
                 <div class="component transistor transistor-b" id="transistor-nor-b">טרנזיסטור B</div>
                 <div class="component output" id="output-nor">מוצא Out</div>
                 <div class="component input-point input-point-a" id="input-point-nor-a">כניסה A</div>
                 <div class="component input-point input-point-b" id="input-point-nor-b">כניסה B</div>

                 <!-- Connections & Flow Indicators -->
                 <div class="connection conn-nor-vcc-split"></div>
                 <div class="connection conn-nor-resistor-a"></div>
                 <div class="connection conn-nor-transistor-a-ground"></div>
                 <div class="connection conn-nor-resistor-b"></div>
                 <div class="connection conn-nor-transistor-b-ground"></div>
                <div class="connection conn-nor-output-split"></div>
                <div class="connection conn-nor-output-common"></div>
                <div class="connection conn-nor-input-a-gate"></div>
                <div class="connection conn-nor-input-b-gate"></div>
                <div class="connection conn-nor-vcc-resistor-line"></div>
                <div class="connection conn-nor-ground-line"></div>


                <div class="flow-indicator flow-nor-resistor-a"></div>
                 <div class="flow-indicator flow-nor-transistor-a-ground"></div>
                 <div class="flow-indicator flow-nor-resistor-b"></div>
                 <div class="flow-indicator flow-nor-transistor-b-ground"></div>
                <div class="flow-indicator flow-nor-vcc-resistor-line"></div>
                <div class="flow-indicator flow-nor-ground-line"></div>
                <div class="flow-indicator flow-nor-output-common-flow"></div>

             </div>
        </div>

        <div id="output-area">
            <h2>תוצאת השער:</h2>
            <div class="output-display">
                <span class="output-label">מתח מוצא:</span>
                <span id="output-voltage" class="output-value voltage-value">--</span>
                 <span class="output-label">מצב לוגי:</span>
                <span id="output-logic" class="output-value logic-value">--</span>
                <div id="output-light" class="light off" title="מייצג 1 לוגי"></div>
            </div>
             <div class="truth-table">
                <h3>טבלת אמת</h3>
                <table>
                    <thead>
                        <tr>
                            <th>A</th>
                            <th class="input-b-header">B</th>
                            <th>Out</th>
                        </tr>
                    </thead>
                    <tbody id="truth-table-body">
                        <!-- Table rows will be generated by JS -->
                    </tbody>
                </table>
                 <p class="table-info">שורה מודגשת מראה את הכניסה הנוכחית.</p>
            </div>
        </div>
    </div>
</div>

<button id="toggle-explanation">גלו את הסוד: הסבר מעמיק</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: טרנזיסטורים כשערים לוגיים - איך זה באמת עובד</h2>

    <h3>טרנזיסטור: המפסק האלקטרוני שבזכותו יש מחשבים</h3>
    <p>תחשבו על טרנזיסטור כמו על ברז חשמלי קטן במעגל מים. ה"מים" הם זרם חשמלי, וה"ברז" הוא הטרנזיסטור. במקום לפתוח או לסגור אותו ביד, אנחנו שולטים בו עם מתח חשמלי קטן על "רגל הבקרה" שלו (שנקראת Gate בטרנזיסטורי MOSFET, הנפוצים במעבדים). כשהמתח על ה-Gate גבוה מספיק (בסימולציה שלנו, מעל 2.5V), הטרנזיסטור "נפתח" ומאפשר לזרם לעבור בין שתי הרגליים האחרות שלו (Source ו-Drain). כשהמתח נמוך, הטרנזיסטור "נסגר" וחוסם את מעבר הזרם. כך הוא משמש כמתג מבוקר מתח.</p>

     <h3>שפה בינארית: 0 ו-1, מתח נמוך וגבוה</h3>
    <p>מחשבים מדברים בשפה של 0 ו-1. במעגלים אלקטרוניים, זה מתבטא בשתי רמות מתח:</p>
    <ul>
        <li>**מתח גבוה (למשל, 5V בסימולציה):** נחשב '1' לוגי (True).</li>
        <li>**מתח נמוך (קרוב ל-0V):** נחשב '0' לוגי (False).</li>
    </ul>
    <p>היכולת להעביר או לחסום זרם (כלומר, לשלוט על מתח המוצא להיות גבוה או נמוך) בהתאם למתח הכניסה, היא המפתח לבניית שערי לוגיקה.</p>

    <h3>שערי לוגיקה: אבני הבניין של המעבד</h3>
    <p>שער לוגי הוא מעגל אלקטרוני שמבצע פעולה לוגית בסיסית אחת. שערי ה-NOT, NAND, ו-NOR הם מהיסודיים ביותר. טבלת אמת מראה מה המוצא של השער עבור כל צירוף אפשרי של כניסות:</p>
    <ul>
        <li>**שער NOT (אינוורטר):** הופך את הרמה. 0 כניסה -> 1 מוצא. 1 כניסה -> 0 מוצא. הוא תמיד נותן את ההפך.</li>
         <li>**שער NAND:** נותן 0 רק אם *שתי* הכניסות הן 1. אחרת, הוא נותן 1. הוא ההפך של שער AND.</li>
        <li>**שער NOR:** נותן 1 רק אם *שתי* הכניסות הן 0. אחרת, הוא נותן 0. הוא ההפך של שער OR.</li>
    </ul>
    <p>שימו לב: NAND ו-NOR נקראים "שערים אוניברסליים" כי ניתן לבנות מהם את כל השערים האחרים וכל פונקציה לוגית.</p>

    <h3>מבנה השערים בסימולציה (בטכנולוגיית NMOS פשוטה):</h3>
    <p>הסימולציה מציגה מימוש פשוט של שערים אלו באמצעות טרנזיסטורי NMOS ונגד, מודל בסיסי שמדגים את העיקרון:</p>
    <ul>
        <li>**NOT:** טרנזיסטור יחיד מחובר בטור עם נגד בין 5V להארקה. המוצא נלקח מהנקודה המשותפת. כשהכניסה גבוהה (1), הטרנזיסטור מוליך ומחבר את נקודת המוצא להארקה (0V, כלומר 0 לוגי). כשהכניסה נמוכה (0), הטרנזיסטור כבוי, והנגד מושך את נקודת המוצא ל-5V (כלומר 1 לוגי).</li>
        <li>**NAND:** שני טרנזיסטורים בטור, מחוברים באותו אופן עם נגד. המוצא יורד ל-0V רק אם *שני* הטרנזיסטורים דולקים (כלומר, שתי הכניסות גבוהות). אם אחד מהם כבוי, השרשרת נשברת והמוצא נשאר ב-5V.</li>
        <li>**NOR:** שני טרנזיסטורים במקביל, מחוברים באותו אופן עם נגד. המוצא יורד ל-0V אם *אחד או יותר* מהטרנזיסטורים דולק (כלומר, לפחות כניסה אחת גבוהה). רק אם *שני* הטרנזיסטורים כבויים (כלומר, שתי הכניסות נמוכות), אין נתיב להארקה והמוצא נשאר ב-5V.</li>
    </ul>
    <p>במעבדים מודרניים משתמשים בטכנולוגיית CMOS מתוחכמת יותר (עם טרנזיסטורי PMOS בנוסף ל-NMOS) שהיא יעילה ומהירה יותר, אך העיקרון הבסיסי של טרנזיסטורים כמתגים זהה.</p>

    <h3>הכוח בשילוב: ממתגים פשוטים לחישובים מסובכים</h3>
    <p>הקסם האמיתי קורה כשמחברים מיליארדי טרנזיסטורים ושערים יחד. ניתן לבנות כל פעולה לוגית או אריתמטית מורכבת (חיבור, חיסור, זיכרון, החלטות) על ידי שילוב נכון של השערים הבסיסיים. המעבד במחשב או בטלפון שלכם מכיל שבב סיליקון אחד עם מיליארדי טרנזיסטורים זעירים המחוברים ברשת עצומה, שמבצעת את כל החישובים הדרושים כדי להריץ תוכנות, להציג תמונות ולעשות את כל הדברים המדהימים שהמכשירים הדיגיטליים שלנו עושים.</p>

</div>

<style>
/* General styles */
#app-container {
    direction: rtl;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    padding: 25px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    max-width: 1000px;
    margin: 20px auto;
    box-sizing: border-box;
}

.controls-panel {
    flex: 1;
    min-width: 280px;
    background-color: #f8f8f8;
    padding: 20px;
    border-radius: 8px;
    box-shadow: inset 0 1px 5px rgba(0, 0, 0, 0.05);
}

.controls-group {
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 1px solid #eee;
}

.controls-group:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.controls-panel h2 {
    margin-top: 0;
    color: #333;
    font-size: 1.3em;
    border-bottom: 2px solid #4CAF50;
    padding-bottom: 5px;
    margin-bottom: 15px;
}

.gate-selector {
    display: flex;
    flex-direction: column;
}

.radio-label {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    cursor: pointer;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.2s ease;
}

.radio-label:hover {
    background-color: #eef;
}

.radio-label input[type="radio"] {
    margin-left: 10px;
    transform: scale(1.2);
}

.gate-name {
    font-weight: bold;
    color: #0056b3;
    min-width: 60px;
}

.gate-desc {
    font-size: 0.9em;
    color: #555;
}

#inputs-container .input-info {
    font-size: 0.8em;
    color: #666;
    margin-top: -10px;
    margin-bottom: 15px;
}

.input-control {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

.input-label {
    display: inline-block;
    min-width: 80px;
    font-weight: normal;
    margin-left: 10px;
    color: #333;
}

.input-control input[type="range"] {
    flex-grow: 1; /* Make slider take available space */
    min-width: 120px; /* Minimum width for slider */
    margin-left: 10px;
    -webkit-appearance: none;
    appearance: none;
    height: 8px;
    background: #ddd;
    outline: none;
    opacity: 0.7;
    transition: opacity .2s;
    border-radius: 5px;
}

.input-control input[type="range"]:hover {
    opacity: 1;
}

.input-control input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #4CAF50;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.input-control input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #4CAF50;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}


.input-feedback {
    display: flex;
    min-width: 150px; /* Fixed width for feedback */
    justify-content: flex-start;
    gap: 10px;
    margin-right: 10px;
    font-size: 0.9em;
}


.voltage-display {
     font-weight: bold;
     color: #007bff;
}

.logic-display {
     font-weight: bold;
     color: #dc3545; /* Default for 0 */
}

.logic-display.logic-1 {
    color: #28a745; /* Color for 1 */
}


.circuit-area {
    flex: 2;
    min-width: 500px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.circuit-diagram {
    border: 2px dashed #a0a0a0;
    padding: 20px;
    position: relative;
    background-color: #ffffff;
    border-radius: 8px;
    min-height: 300px; /* Increased height for better spacing */
    display: none; /* Hide all by default */
}
.circuit-diagram.active {
    display: block; /* Show active diagram */
}

.diagram-title {
    font-size: 1.5em;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
    text-align: center;
}

.diagram-subtitle {
    font-size: 1em;
    color: #666;
    margin-bottom: 20px;
    text-align: center;
}

.diagram-components {
    position: relative;
    width: 100%;
    height: 240px; /* Fixed height for diagrams */
}

.component {
    position: absolute;
    border: 1px solid #555;
    padding: 4px;
    font-size: 0.75em;
    text-align: center;
    border-radius: 4px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
}

.voltage-source {
    top: 0px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    height: 30px;
    background-color: #ffdddd; /* Light red */
    border-color: #cc0000;
    font-weight: bold;
    color: #cc0000;
}

.ground {
    bottom: 0px;
    left: 50%;
    transform: translateX(-50%);
    width: 70px;
    height: 30px;
    background-color: #ddffdd; /* Light green */
    border-color: #00cc00;
    font-weight: bold;
    color: #00cc00;
}

.resistor {
    width: 25px;
    height: 50px;
    background-color: #eeeeee;
    border-color: #333;
}

.transistor {
    width: 60px;
    height: 50px;
    background-color: #ddddff; /* Light blue */
    border-color: #0000cc;
    font-size: 0.65em;
    transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

.transistor.on {
    background-color: #aaffaa; /* Greenish when ON */
    border-color: #00aa00;
    box-shadow: 0 0 8px rgba(0, 170, 0, 0.5);
}

.transistor.off {
    background-color: #ffaaaa; /* Reddish when OFF */
    border-color: #aa0000;
    box-shadow: none;
}

.output {
    width: 80px;
    height: 30px;
    background-color: #ffffdd; /* Light yellow */
    border-color: #cccc00;
    font-weight: bold;
}

.input-point {
     width: 70px;
    height: 30px;
    background-color: #ddffff; /* Light cyan */
    border-color: #00cccc;
    font-weight: bold;
}

/* Connection Lines */
.connection {
    position: absolute;
    background-color: #000;
     /* Default small size, specific sizes overridden below */
}

/* Flow Indicators */
.flow-indicator {
    position: absolute;
    background-color: rgba(255, 165, 0, 0); /* Orange, initially transparent */
    /* Default small size, specific sizes overridden below */
    box-shadow: 0 0 5px rgba(255, 165, 0, 0); /* Orange glow, initially off */
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.flow-indicator.active {
    background-color: rgba(255, 165, 0, 0.8); /* Orange when active */
    box-shadow: 0 0 5px rgba(255, 165, 0, 0.8); /* Orange glow when active */
}

/* Common connection endpoints for flow */
.connection.vertical, .flow-indicator.vertical { width: 2px; }
.connection.horizontal, .flow-indicator.horizontal { height: 2px; }


/* NOT Gate Layout */
#circuit-diagram-not .resistor { top: 40px; left: 50%; transform: translateX(-50%); width: 25px; height: 50px; }
#circuit-diagram-not .transistor { top: 100px; left: 50%; transform: translateX(-50%); }
#circuit-diagram-not .output { top: 70px; left: calc(50% + 60px); }
#circuit-diagram-not .input-point { top: 110px; left: calc(50% - 110px); }

/* NOT Gate Connections & Flow */
#circuit-diagram-not .conn-vcc-resistor { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-not .conn-resistor-transistor { top: 90px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-not .conn-transistor-ground { bottom: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-not .conn-input-a-gate { top: 135px; left: calc(50% - 110px); width: 50px; height: 2px;}
#circuit-diagram-not .conn-output-line { top: 85px; right: calc(50% + 60px); width: 40px; height: 2px;}

#circuit-diagram-not .flow-vcc-resistor { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-not .flow-resistor-transistor { top: 90px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-not .flow-transistor-ground { bottom: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }


/* NAND Gate Layout */
#circuit-diagram-nand .resistor { top: 40px; left: 50%; transform: translateX(-50%); width: 25px; height: 50px; }
#circuit-diagram-nand .transistor-a { top: 100px; left: 50%; transform: translateX(-50%); }
#circuit-diagram-nand .transistor-b { top: 160px; left: 50%; transform: translateX(-50%); }
#circuit-diagram-nand .output { top: 70px; left: calc(50% + 60px); }
#circuit-diagram-nand .input-point-a { top: 110px; left: calc(50% - 110px); }
#circuit-diagram-nand .input-point-b { top: 170px; left: calc(50% - 110px); }

/* NAND Gate Connections & Flow */
#circuit-diagram-nand .conn-nand-vcc-resistor { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .conn-nand-resistor-transistora { top: 90px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .conn-nand-transistora-transistorb { top: 150px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .conn-nand-transistorb-ground { bottom: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .conn-nand-input-a-gate { top: 135px; left: calc(50% - 110px); width: 50px; height: 2px; }
#circuit-diagram-nand .conn-nand-input-b-gate { top: 195px; left: calc(50% - 110px); width: 50px; height: 2px; }
#circuit-diagram-nand .conn-nand-output-line { top: 85px; right: calc(50% + 60px); width: 40px; height: 2px; }

#circuit-diagram-nand .flow-nand-vcc-resistor { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .flow-nand-resistor-transistora { top: 90px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .flow-nand-transistora-transistorb { top: 150px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nand .flow-nand-transistorb-ground { bottom: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }


/* NOR Gate Layout */
#circuit-diagram-nor .resistor-nor-top { top: 40px; left: 50%; transform: translateX(-50%); width: 50px; height: 25px; } /* Horizontal Resistor */
#circuit-diagram-nor .transistor-a { top: 100px; left: calc(50% - 60px); }
#circuit-diagram-nor .transistor-b { top: 100px; left: calc(50% + 0px); }
#circuit-diagram-nor .output { top: 120px; left: calc(50% - 40px); }
#circuit-diagram-nor .input-point-a { top: 110px; left: calc(50% - 140px); }
#circuit-diagram-nor .input-point-b { top: 110px; left: calc(50% + 60px); }


/* NOR Gate Connections & Flow */
/* Vertical line from VCC down to split */
#circuit-diagram-nor .conn-nor-vcc-resistor-line { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
/* Horizontal resistor connection */
#circuit-diagram-nor .conn-nor-vcc-split { top: 40px; left: calc(50% - 25px); width: 50px; height: 2px; } /* Connects vertical line to resistor */
/* Lines from resistor to transistors A & B */
#circuit-diagram-nor .conn-nor-resistor-a { top: 65px; left: calc(50% - 35px); height: 35px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-nor .conn-nor-resistor-b { top: 65px; left: calc(50% + 35px); height: 35px; transform: translateX(-1px); width: 2px;}
/* Lines from transistors A & B down to common output point */
#circuit-diagram-nor .conn-nor-output-split { top: 150px; left: calc(50% - 35px); height: 2px; width: 70px; } /* Horizontal line connecting transistors */
#circuit-diagram-nor .conn-nor-output-common { top: 150px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; } /* Vertical line to output */
/* Lines from transistors A & B to ground */
#circuit-diagram-nor .conn-nor-transistor-a-ground { bottom: 30px; left: calc(50% - 35px); height: 50px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nor .conn-nor-transistor-b-ground { bottom: 30px; left: calc(50% + 35px); height: 50px; transform: translateX(-1px); width: 2px; }
/* Horizontal ground line */
#circuit-diagram-nor .conn-nor-ground-line { bottom: 30px; left: calc(50% - 35px); width: 70px; height: 2px; }

/* Input Gate Connections */
#circuit-diagram-nor .conn-nor-input-a-gate { top: 135px; left: calc(50% - 140px); width: 80px; height: 2px; }
#circuit-diagram-nor .conn-nor-input-b-gate { top: 135px; left: calc(50% + 60px); width: 80px; height: 2px; }


/* NOR Gate Flow Indicators */
#circuit-diagram-nor .flow-nor-vcc-resistor-line { top: 30px; left: 50%; height: 10px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nor .flow-nor-resistor-a { top: 65px; left: calc(50% - 35px); height: 35px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-nor .flow-nor-resistor-b { top: 65px; left: calc(50% + 35px); height: 35px; transform: translateX(-1px); width: 2px;}
#circuit-diagram-nor .flow-nor-transistor-a-ground { bottom: 30px; left: calc(50% - 35px); height: 50px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nor .flow-nor-transistor-b-ground { bottom: 30px; left: calc(50% + 35px); height: 50px; transform: translateX(-1px); width: 2px; }
#circuit-diagram-nor .flow-nor-ground-line { bottom: 30px; left: calc(50% - 35px); width: 70px; height: 2px; }
#circuit-diagram-nor .flow-nor-output-common-flow { top: 150px; left: calc(50% - 35px); height: 2px; width: 70px; } /* Horizontal flow line */


/* Output Area */
#output-area {
    border: 1px solid #ccc;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

#output-area h2 {
    margin-top: 0;
    font-size: 1.3em;
    color: #333;
    border-bottom: 2px solid #2196F3;
    padding-bottom: 5px;
    margin-bottom: 15px;
}

.output-display {
    display: flex;
    align-items: center;
    gap: 15px;
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 20px;
    background-color: #e9ecef;
    padding: 10px 15px;
    border-radius: 5px;
}
.output-label {
     font-weight: normal;
    color: #555;
}

.output-value {
    min-width: 60px;
    text-align: left;
}

#output-voltage.voltage-value {
     color: #007bff;
}

#output-logic.logic-value {
    color: #dc3545; /* Default for 0 */
}

#output-logic.logic-value.logic-1 {
     color: #28a745; /* Color for 1 */
}


.output-display .light {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background-color: #a0a0a0; /* Dim gray when off */
    border: 3px solid #777;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.output-display .light.on {
    background-color: #ffeb3b; /* Bright yellow when on */
    box-shadow: 0 0 15px #ffeb3b, inset 0 0 8px #ffa000;
    border-color: #fbc02d;
}

.truth-table h3 {
     font-size: 1.1em;
     margin-bottom: 10px;
    color: #333;
}

.truth-table table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95em;
    text-align: center;
    margin-bottom: 10px;
}

.truth-table th, .truth-table td {
    border: 1px solid #ddd;
    padding: 10px;
}

.truth-table th {
    background-color: #e9ecef;
    color: #333;
    font-weight: bold;
}

.truth-table td {
    background-color: #ffffff;
}

.truth-table tr:nth-child(even) td {
    background-color: #f8f8f8;
}


.truth-table tr.current-input td {
    background-color: #cce5ff !important; /* Light blue for highlighting */
    font-weight: bold;
    border-color: #007bff;
}

.truth-table td:last-child {
    font-weight: bold;
}

.truth-table td:last-child.logic-1 {
     color: #28a745; /* Green for 1 */
}
.truth-table td:last-child.logic-0 {
     color: #dc3545; /* Red for 0 */
}


.input-b-header {
    display: table-cell; /* Default for NAND/NOR */
}

.table-info {
    font-size: 0.8em;
    color: #666;
    text-align: center;
}


button#toggle-explanation {
    display: block;
    margin: 30px auto 10px auto;
    padding: 12px 25px;
    font-size: 1em;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s ease, transform 0.1s ease;
}

button#toggle-explanation:hover {
    background-color: #0056b3;
}

button#toggle-explanation:active {
     transform: scale(0.98);
}


#explanation {
    margin-top: 20px;
    padding: 25px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

#explanation h2, #explanation h3 {
    color: #333;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
    margin-bottom: 15px;
}
#explanation h2 { border-bottom-color: #4CAF50;}
#explanation h3 { border-bottom-color: #2196F3;}


#explanation p {
    line-height: 1.8;
    color: #555;
    margin-bottom: 15px;
}

#explanation ul {
     margin-bottom: 15px;
}
#explanation li {
    margin-bottom: 8px;
    line-height: 1.6;
    color: #555;
}

#explanation table {
    margin: 10px auto;
    border-collapse: collapse;
    font-size: 0.9em;
    text-align: center;
}
#explanation table th, #explanation table td {
     border: 1px solid #ddd;
    padding: 8px;
}
#explanation table th {
    background-color: #f2f2f2;
}
#explanation table td {
    background-color: #fff;
}


/* Responsive adjustments */
@media (max-width: 768px) {
    #app-container {
        flex-direction: column;
        padding: 15px;
        gap: 20px;
    }
    .circuit-area, .controls-panel {
        min-width: unset;
        width: 100%;
    }
    .output-display {
         flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }
    .input-control {
         flex-direction: column;
        align-items: flex-start;
    }
    .input-control label {
         margin-bottom: 5px;
    }
     .input-control input[type="range"] {
        width: 100%;
         margin-left: 0;
        margin-top: 5px;
    }
     .input-feedback {
        width: 100%;
        justify-content: center;
         margin-right: 0;
         margin-top: 5px;
    }
     .diagram-components {
        height: 300px; /* Adjust height for smaller screens if needed */
    }
    .component, .input-point, .output, .voltage-source, .ground {
         font-size: 0.6em; /* Smaller font for components */
         padding: 2px;
    }
     .transistor { font-size: 0.55em; }
     .connection { background-color: #000;} /* Ensure visibility */
}

/* Specific layout adjustments for smaller screens if components overlap */
/* (More detailed media queries might be needed for complex diagrams) */
@media (max-width: 500px) {
     .diagram-components {
        height: 350px; /* Allow more vertical space */
     }
    /* Adjust absolute positions if necessary */
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const gateRadios = document.querySelectorAll('input[name="gate"]');
    const inputA = document.getElementById('voltageA');
    const inputB = document.getElementById('voltageB');
    const inputBContainer = document.getElementById('inputB');
    const voltageDisplays = document.querySelectorAll('.input-feedback .voltage-display');
    const logicDisplays = document.querySelectorAll('.input-feedback .logic-display');
    const outputVoltageDisplay = document.getElementById('output-voltage');
    const outputLogicDisplay = document.getElementById('output-logic');
    const outputLight = document.getElementById('output-light');
    const circuitDiagrams = document.querySelectorAll('.circuit-diagram');
    const truthTableBody = document.getElementById('truth-table-body');
    const inputBHeader = document.querySelector('.input-b-header');

    // Transistors references
    const transistorNot = document.getElementById('transistor-not');
    const transistorNandA = document.getElementById('transistor-nand-a');
    const transistorNandB = document.getElementById('transistor-nand-b');
    const transistorNorA = document.getElementById('transistor-nor-a');
    const transistorNorB = document.getElementById('transistor-nor-b');

    // Flow Indicators references (get all flow indicators for easy clearing)
    const flowIndicators = document.querySelectorAll('.flow-indicator');


    const VCC = 5.0; // Volts
    const GND = 0.0; // Volts
    const LOGIC_HIGH_THRESHOLD = 2.5; // Volts
    const TRANSISTOR_ON_THRESHOLD = 2.5; // Volts

    function getLogicState(voltage) {
        return voltage >= LOGIC_HIGH_THRESHOLD ? 1 : 0;
    }

    function getTransistorState(gateVoltage) {
        return gateVoltage >= TRANSISTOR_ON_THRESHOLD ? 'on' : 'off';
    }

    function updateCircuit() {
        const selectedGate = document.querySelector('input[name="gate"]:checked').value;
        const voltageA = parseFloat(inputA.value);
        const voltageB = parseFloat(inputB.value);
        const logicA = getLogicState(voltageA);
        const logicB = getLogicState(voltageB);

        let outputVoltage = 0; // Initialize output voltage
        let transistorStates = {}; // Store transistor states
        let activeFlows = []; // Store which flow indicators should be active

        // Hide all diagrams, show only the selected one
        circuitDiagrams.forEach(diagram => {
            diagram.classList.remove('active');
            diagram.style.display = 'none'; // Ensure display none
        });
        const activeDiagram = document.getElementById(`circuit-diagram-${selectedGate.toLowerCase()}`);
         if (activeDiagram) {
            activeDiagram.style.display = 'block'; // Show the correct diagram
            // Use a small timeout to allow display:block to apply before adding class
            setTimeout(() => activeDiagram.classList.add('active'), 10);
         }


        // Update inputs display
        voltageDisplays[0].textContent = `${voltageA.toFixed(1)}V`;
        logicDisplays[0].textContent = `(${logicA} לוגי)`;
        logicDisplays[0].classList.toggle('logic-1', logicA === 1);


        // Update inputs and calculate output based on gate logic
        if (selectedGate === 'NOT') {
            inputBContainer.style.display = 'none';
            if (inputBHeader) inputBHeader.style.display = 'none';

            transistorStates = {
                not: getTransistorState(voltageA)
            };

            // NMOS NOT logic
             if (transistorStates.not === 'on') {
                outputVoltage = GND; // Transistor connects output to ground
                activeFlows = ['flow-resistor-transistor', 'flow-transistor-ground']; // Flow through resistor and transistor
             } else {
                outputVoltage = VCC; // Output pulled up by resistor to VCC
                 activeFlows = ['flow-vcc-resistor']; // Flow only through resistor (no path to ground)
             }
             // Gate signal flow
             activeFlows.push('conn-input-a-gate');


        } else if (selectedGate === 'NAND') {
             inputBContainer.style.display = 'flex';
             if (inputBHeader) inputBHeader.style.display = 'table-cell';
             voltageDisplays[1].textContent = `${voltageB.toFixed(1)}V`;
             logicDisplays[1].textContent = `(${logicB} לוגי)`;
             logicDisplays[1].classList.toggle('logic-1', logicB === 1);


            transistorStates = {
                nandA: getTransistorState(voltageA),
                nandB: getTransistorState(voltageB)
            };
            // NMOS NAND logic (using NMOS in series)
             if (transistorStates.nandA === 'on' && transistorStates.nandB === 'on') {
                 outputVoltage = GND; // Both transistors connect output to ground
                 activeFlows = ['flow-nand-resistor-transistora', 'flow-nand-transistora-transistorb', 'flow-nand-transistorb-ground'];
             } else {
                 outputVoltage = VCC; // Output pulled up by resistor to VCC
                 activeFlows = ['flow-nand-vcc-resistor'];
             }
            // Gate signal flows
            activeFlows.push('conn-nand-input-a-gate', 'conn-nand-input-b-gate');

        } else if (selectedGate === 'NOR') {
             inputBContainer.style.display = 'flex';
             if (inputBHeader) inputBHeader.style.display = 'table-cell';
             voltageDisplays[1].textContent = `${voltageB.toFixed(1)}V`;
             logicDisplays[1].textContent = `(${logicB} לוגי)`;
            logicDisplays[1].classList.toggle('logic-1', logicB === 1);


            transistorStates = {
                norA: getTransistorState(voltageA),
                norB: getTransistorState(voltageB)
            };
            // NMOS NOR logic (using NMOS in parallel)
            if (transistorStates.norA === 'on' || transistorStates.norB === 'on') {
                outputVoltage = GND; // At least one transistor connects output to ground
                // Flow is complex here - it flows through the resistor, then splits.
                // If A is on, flow is VCC -> Resistor -> Transistor A -> Ground.
                // If B is on, flow is VCC -> Resistor -> Transistor B -> Ground.
                // If both are on, flow splits.
                // Simplification for visualization: indicate path from VCC to the ON transistor(s) and then to ground.
                activeFlows = ['flow-nor-vcc-resistor-line', 'flow-nor-ground-line', 'flow-nor-output-common-flow']; // Common paths
                 if (transistorStates.norA === 'on') activeFlows.push('flow-nor-resistor-a', 'flow-nor-transistor-a-ground');
                 if (transistorStates.norB === 'on') activeFlows.push('flow-nor-resistor-b', 'flow-nor-transistor-b-ground');

            } else {
                outputVoltage = VCC; // Output pulled up by resistor to VCC
                 activeFlows = ['flow-nor-vcc-resistor-line']; // Flow only up to the resistor/split point
            }
             // Gate signal flows
            activeFlows.push('conn-nor-input-a-gate', 'conn-nor-input-b-gate');
        }

        // Update transistor visuals
        if (transistorNot) { transistorNot.className = 'component transistor ' + transistorStates.not; }
        if (transistorNandA) { transistorNandA.className = 'component transistor transistor-a ' + transistorStates.nandA; }
        if (transistorNandB) { transistorNandB.className = 'component transistor transistor-b ' + transistorStates.nandB; }
         if (transistorNorA) { transistorNorA.className = 'component transistor transistor-a ' + transistorStates.norA; }
         if (transistorNorB) { transistorNorB.className = 'component transistor transistor-b ' + transistorStates.norB; }

        // Update flow indicators - reset all, then activate specific ones
         flowIndicators.forEach(indicator => indicator.classList.remove('active'));
         activeFlows.forEach(flowClass => {
             const flowElement = activeDiagram ? activeDiagram.querySelector(`.${flowClass}`) : null;
             if(flowElement) flowElement.classList.add('active');
         });


        // Update output display
        const outputLogic = getLogicState(outputVoltage);
        outputVoltageDisplay.textContent = `${outputVoltage.toFixed(1)}V`;
        outputLogicDisplay.textContent = `(${outputLogic} לוגי)`;
        outputLogicDisplay.classList.toggle('logic-1', outputLogic === 1);

        outputLight.className = 'light ' + (outputLogic === 1 ? 'on' : 'off');

        updateTruthTable(selectedGate, logicA, logicB, outputLogic);
    }

     function updateTruthTable(gate, currentLogicA, currentLogicB, currentOutputLogic) {
        truthTableBody.innerHTML = ''; // Clear previous table

        const inputs = gate === 'NOT' ? [[0], [1]] : [[0, 0], [0, 1], [1, 0], [1, 1]];

        inputs.forEach(input => {
            const a = input[0];
            const b = input.length > 1 ? input[1] : null;
            let expectedOutput;

            // Calculate truth table output based on gate definition (not the circuit model)
            if (gate === 'NOT') {
                 expectedOutput = (a === 0) ? 1 : 0;
            } else if (gate === 'NAND') {
                 expectedOutput = (a === 1 && b === 1) ? 0 : 1;
            } else if (gate === 'NOR') {
                 expectedOutput = (a === 0 && b === 0) ? 1 : 0;
            }


            const row = truthTableBody.insertRow();
            // Highlight the row matching the current input *logic* state
            if ((gate === 'NOT' && a === currentLogicA) || (gate !== 'NOT' && a === currentLogicA && b === currentLogicB)) {
                row.classList.add('current-input');
            }

            const cellA = row.insertCell();
            cellA.textContent = a;

            if (gate !== 'NOT') {
                 const cellB = row.insertCell();
                 cellB.textContent = b;
            }

            const cellOut = row.insertCell();
            cellOut.textContent = expectedOutput;
            cellOut.classList.add(expectedOutput === 1 ? 'logic-1' : 'logic-0');
        });
     }


    // Event listeners
    gateRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            // Reset inputs when changing gate
            inputA.value = 0;
            inputB.value = 0;
            updateCircuit();
        });
    });

    inputA.addEventListener('input', updateCircuit);
    inputB.addEventListener('input', updateCircuit);

    // Initial setup
    updateCircuit(); // Run once to set initial state

    // Explanation toggle
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');

    toggleButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר הסבר' : 'גלו את הסוד: הסבר מעמיק';
         // Scroll to explanation if showing it
         if (isHidden) {
             explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
         }
    });

});
</script>
---