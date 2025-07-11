---
title: "המוח הבינארי: איך מחשבים סוכמים?"
english_slug: logic-gate-builder-binary-addition
category: "מחשבים וטכנולוגיה"
tags: ["שערים לוגיים", "מעגלים לוגיים", "בינארי", "אלקטרוניקה", "סימולציה", "אינטראקטיבי"]
---
# המוח הבינארי: איך מחשבים סוכמים?

האם אי פעם חשבתם איך המחשב שלכם יודע לחבר מספרים? זה לא קסם! בלב כל מחשב יושבים רכיבים זעירים וחכמים שנקראים שערים לוגיים. כל שער כזה הוא כמו מתג אלקטרוני שמקבל קלט בינארי (0 או 1) ומפיק פלט בינארי על פי כלל לוגי פשוט.

במשימה האינטראקטיבית שלפניכם, תראו בדיוק איך שילוב של כמה שערים בסיסיים יכול לבצע את אחת הפעולות החשובות ביותר במחשוב: **חיבור בינארי**. זהו הצעד הראשון להבנת איך מחשבים "חושבים" ומבצעים חישובים מסובכים.

<div id="logic-circuit-app">
    <h2>סימולטור מחבר שלם (חיבור בינארי עם נשא)</h2>
    <div class="circuit-container">
        <div class="inputs">
            <div class="input-group">
                <label for="inputA">קלט A:</label>
                <select id="inputA" class="logic-input" aria-label="קלט A">
                    <option value="0">0</option>
                    <option value="1">1</option>
                </select>
            </div>
            <div class="input-group">
                <label for="inputB">קלט B:</label>
                <select id="inputB" class="logic-input" aria-label="קלט B">
                    <option value="0">0</option>
                    <option value="1">1</option>
                </select>
            </div>
            <div class="input-group">
                <label for="carryIn">נשא כניסה (Ci):</label>
                <select id="carryIn" class="logic-input" aria-label="נשא כניסה">
                    <option value="0">0</option>
                    <option value="1">1</option>
                </select>
            </div>
        </div>

        <div class="gates-container">
            <!-- Visual representation of a Full Adder circuit -->
            <div class="gate-layer layer-1">
                <div id="xor1" class="gate xor-gate" data-label="XOR1">XOR</div>
                <div id="and1" class="gate and-gate" data-label="AND1">AND</div>
            </div>
            <div class="gate-layer layer-2">
                <div id="xor2" class="gate xor-gate" data-label="XOR2">XOR</div>
                <div id="and2" class="gate and-gate" data-label="AND2">AND</div>
            </div>
             <div class="gate-layer layer-3">
                <div id="or1" class="gate or-gate" data-label="OR1">OR</div>
            </div>
        </div>

        <div class="outputs">
             <div id="sumOutput" class="output" data-label="סכום (S)">סכום (S): <span class="output-value">0</span></div>
            <div id="carryOutput" class="output" data-label="נשא יציאה (Co)">נשא יציאה (Co): <span class="output-value">0</span></div>
        </div>
    </div>

    <div class="connections-container">
        <!-- Connections will be drawn here by JS/CSS -->
        <!-- Example visual placeholders (CSS will style lines): -->
        <div class="connection conn-A-xor1" data-from="#inputA" data-to="#xor1" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="-10"></div>
        <div class="connection conn-B-xor1" data-from="#inputB" data-to="#xor1" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="10"></div>
        <div class="connection conn-A-and1" data-from="#inputA" data-to="#and1" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="-10"></div>
        <div class="connection conn-B-and1" data-from="#inputB" data-to="#and1" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="10"></div>

        <div class="connection conn-xor1-xor2" data-from="#xor1" data-to="#xor2" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="-10"></div>
        <div class="connection conn-xor1-and2" data-from="#xor1" data-to="#and2" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="-10"></div>
        <div class="connection conn-carryIn-xor2" data-from="#carryIn" data-to="#xor2" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="10"></div>
        <div class="connection conn-carryIn-and2" data-from="#carryIn" data-to="#and2" data-from-offset-x="50" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="10"></div>

        <div class="connection conn-and1-or1" data-from="#and1" data-to="#or1" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="-15"></div>
        <div class="connection conn-and2-or1" data-from="#and2" data-to="#or1" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-40" data-to-offset-y="15"></div>

        <div class="connection conn-xor2-sum" data-from="#xor2" data-to="#sumOutput" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-60" data-to-offset-y="0"></div>
        <div class="connection conn-or1-carry" data-from="#or1" data-to="#carryOutput" data-from-offset-x="40" data-from-offset-y="0" data-to-offset-x="-60" data-to-offset-y="0"></div>

    </div>
</div>

<button id="toggleExplanation" class="explanation-button" aria-expanded="false" aria-controls="explanation">הצג איך זה עובד (הסבר מפורט)</button>

<div id="explanation" class="hidden" aria-hidden="true">
    <h2>מאחורי הקלעים: מחבר שלם ושערים לוגיים</h2>
    <p>התרשים שלמעלה אינו רק ציור - הוא סימולציה של "מחבר שלם" (Full Adder), אבן בניין קריטית ביחידות העיבוד המרכזיות (CPU) של כל מחשב! תפקידו הוא לחבר שתי סיביות בינאריות (A ו-B), יחד עם סיבית "נשא" מהחיבור הקודם (Carry In), ולהפיק את סיבית ה"סכום" הנוכחי (Sum) ואת סיבית ה"נשא" שתעבור לשלב החיבור הבא (Carry Out).</p>

    <p>המעגל בנוי משילוב אלגנטי של שלושה סוגי שערים לוגיים בסיסיים:</p>
    <ul>
        <li><strong class="xor-color">שער XOR (בלעדי או):</strong> "מגלה הבדלים". פלטו הוא 1 רק אם הקלטים *שונים* זה מזה (0 ו-1, או 1 ו-0). אם הקלטים זהים (0 ו-0, או 1 ו-1), הפלט הוא 0.</li>
        <li><strong class="and-color">שער AND (וגם):</strong> "גלאי הסכמה". פלטו הוא 1 רק ורק אם *כל* הקלטים הם 1. בכל מקרה אחר, הפלט הוא 0.</li>
        <li><strong class="or-color">שער OR (או):</strong> "גלאי נוכחות". פלטו הוא 1 אם *לפחות אחד* מהקלטים הוא 1. רק אם *כל* הקלטים הם 0, הפלט הוא 0.</li>
    </ul>
    <p>עקבו אחר זרימת הסימולציה (הקווים הצבעוניים!) וראו איך הסיביות (0 ו-1) עוברות דרך השערים, משנות את מצבם ומובילות לתוצאה הסופית של הסכום והנשא. המחבר השלם למעשה מחשב את הטבלה הבאה:</p>
    <table class="logic-table">
        <thead>
            <tr>
                <th>A</th>
                <th>B</th>
                <th>Ci</th>
                <th>S</th>
                <th>Co</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
            <tr><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
            <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
            <tr><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
            <tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
        </tbody>
    </table>
    <p>נסו לשנות את ערכי הקלט (A, B, Carry In) וצפו בסימולציה מציגה את התוצאה בכל שלב!</p>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Varela Round', sans-serif; /* Using a slightly more modern font */
        direction: rtl;
        text-align: right;
        background: linear-gradient(135deg, #e0f7fa 0%, #cce0f5 100%); /* Gentle gradient background */
        color: #333;
        line-height: 1.7; /* Improved readability */
        padding: 20px;
        margin: 0; /* Remove default margin */
        overflow-x: hidden; /* Prevent horizontal scroll */
    }

    h1, h2 {
        color: #004a8f; /* Deeper blue */
        text-align: center;
        margin-bottom: 25px;
        font-weight: bold;
    }

    h1 {
        font-size: 2.2rem;
        margin-top: 10px;
    }

    #logic-circuit-app {
        background-color: #ffffff; /* Pure white for cleanliness */
        border-radius: 16px; /* More rounded corners */
        padding: 30px;
        margin: 20px auto; /* Center the app */
        max-width: 900px; /* Max width for better layout on large screens */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Stronger, softer shadow */
        overflow: hidden;
        position: relative;
        border: 1px solid #e0e0e0;
    }

    #logic-circuit-app h2 {
         margin-top: 0;
         color: #007bff; /* Primary blue */
         font-size: 1.6rem;
         margin-bottom: 30px;
    }

    .circuit-container {
        display: flex;
        align-items: center;
        justify-content: space-around;
        gap: 30px; /* Reduced gap slightly, adjust based on element size */
        position: relative;
        z-index: 1;
        padding: 20px 0; /* Add vertical padding */
    }

    .inputs, .outputs {
        display: flex;
        flex-direction: column;
        align-items: stretch; /* Stretch items to fill container */
        gap: 25px; /* Increased gap */
        min-width: 120px; /* Ensure minimum width */
    }

     .input-group {
         display: flex;
         flex-direction: column;
         align-items: flex-start;
     }

    .inputs label {
        font-weight: bold;
        margin-bottom: 8px; /* More space below label */
        color: #555;
        font-size: 1rem;
    }

     .logic-input {
        padding: 10px 15px; /* Increased padding */
        border: 1px solid #ccc;
        border-radius: 8px; /* More rounded */
        font-size: 1rem;
        cursor: pointer;
        transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        background-color: #f8f9fa; /* Light grey background */
        -webkit-appearance: none; /* Remove default appearance */
        -moz-appearance: none;
        appearance: none;
         background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23333%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13.4-28.1H18.4c-6.8%200-13.3%202.7-17.6%207.9-4.3%205.2-5.2%2012.3-2.7%2018.9l128%20153.6c3.5%204.2%208.7%206.7%2014.1%206.7s10.6-2.5%2014.1-6.7l128-153.6c2.5-6.6%201.6-13.7-2.7-18.9z%22%2F%3E%3C%2Fsvg%3E'); /* Custom arrow */
        background-repeat: no-repeat;
        background-position: left 15px center; /* Position arrow on the left for RTL */
        background-size: 12px;
        padding-left: 35px; /* Make space for the arrow */
        width: 100%; /* Fill parent width */
        box-sizing: border-box; /* Include padding and border in element's total width */
    }

    .logic-input:focus {
        border-color: #007bff;
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.4);
        outline: none;
        background-color: #e9f5ff; /* Light blue focus */
    }


    .gates-container {
        display: flex;
        flex-direction: row;
        gap: 50px; /* Space between layers */
        align-items: center;
    }

    .gate-layer {
        display: flex;
        flex-direction: column;
        gap: 30px; /* Space between gates in a layer */
        align-items: center;
    }


    .gate {
        width: 90px; /* Slightly larger */
        height: 50px; /* Slightly larger */
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px solid; /* Border color set by specific gate class */
        border-radius: 8px; /* Consistent rounding */
        background-color: #e9ecef; /* Light grey */
        font-weight: bold;
        font-size: 1rem; /* Slightly larger font */
        position: relative;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); /* More prominent shadow */
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease; /* Add transform for click/active effect */
        cursor: default; /* Indicate not clickable */
         color: #333; /* Default text color */
    }

     .gate::after {
         content: attr(data-label); /* Add gate label below */
         position: absolute;
         bottom: -25px;
         left: 50%;
         transform: translateX(-50%);
         font-size: 0.8rem;
         font-weight: normal;
         color: #555;
     }


    .xor-gate {
        border-color: #28a745; /* Green */
         color: #1e7e34;
    }

    .and-gate {
        border-color: #dc3545; /* Red */
         color: #c82333;
    }

     .or-gate {
        border-color: #ffc107; /* Yellow */
         color: #d39e00;
    }

     /* Gate pulse animation */
     .gate.pulse {
         animation: gate-pulse 0.4s ease-out forwards;
     }

     @keyframes gate-pulse {
         0% { transform: scale(1); box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); }
         50% { transform: scale(1.05); box-shadow: 0 5px 10px rgba(0, 0, 0, 0.25); }
         100% { transform: scale(1); box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); }
     }


    .output {
        padding: 12px 20px; /* Increased padding */
        border: 2px solid #007bff;
        border-radius: 8px;
        background-color: #e9ecef;
        font-weight: bold;
        text-align: center;
        min-width: 120px; /* Match input width */
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease;
        color: #0056b3;
        position: relative;
    }

    .output::after {
         content: attr(data-label); /* Add output label below */
         position: absolute;
         bottom: -25px;
         left: 50%;
         transform: translateX(-50%);
         font-size: 0.8rem;
         font-weight: normal;
         color: #555;
     }

    .output-value {
        font-size: 1.4rem; /* Larger value font */
        margin-right: 5px;
        color: #007bff; /* Match border color */
    }

    /* State Colors */
    .state-0 {
        background-color: #f8d7da; /* Light red */
        border-color: #dc3545; /* Red */
        color: #721c24; /* Dark red text */
    }

     .state-0 .output-value {
         color: #dc3545; /* Red value text */
     }

    .state-1 {
        background-color: #d4edda; /* Light green */
        border-color: #28a745; /* Green */
         color: #155724; /* Dark green text */
    }
    .state-1 .output-value {
         color: #28a745; /* Green value text */
     }


    /* Connections - Abstract representation */
    .connections-container {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none; /* Allow clicks through connections */
         z-index: 0; /* Below circuit elements */
         /* background-color: rgba(0,255,0,0.1); /* Debug */
    }

    .connection {
        position: absolute;
        background-color: #999; /* Default wire color */
        height: 3px; /* Thicker lines */
        transform-origin: 0 0; /* Rotate from the start */
        box-sizing: border-box; /* Include border/padding in size */
        transition: background-color 0.2s ease, box-shadow 0.2s ease; /* Smooth color/shadow change */
        border-radius: 2px; /* Rounded ends */
    }

    /* Connection States */
     .connection.state-0 {
        background-color: #dc3545; /* Red for 0 */
         box-shadow: 0 0 5px #dc3545; /* Glow */
    }

    .connection.state-1 {
        background-color: #28a745; /* Green for 1 */
         box-shadow: 0 0 5px #28a745; /* Glow */
    }

    /* Connection Pulse Animation */
     .connection.pulse {
         animation: wire-pulse 0.4s linear forwards; /* Add pulse animation */
     }

     @keyframes wire-pulse {
         0% { transform: scaleX(0); opacity: 0.8; } /* Start thin, fade */
         100% { transform: scaleX(1); opacity: 1; } /* End normal, solid */
     }


    /* Explanation Section */
    .explanation-button {
        display: block;
        width: auto;
        margin: 30px auto; /* More margin */
        padding: 12px 30px; /* Increased padding */
        font-size: 1.1rem; /* Larger font */
        color: #fff;
        background-color: #007bff;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }

    .explanation-button:hover {
        background-color: #0056b3;
        box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
    }

    .explanation-button:active {
         transform: scale(0.98);
         box-shadow: 0 2px 4px rgba(0, 123, 255, 0.5);
    }

    .hidden {
        display: none;
    }

    #explanation {
        background-color: #e9f5ff;
        border: 1px solid #b8daff;
        border-radius: 12px;
        padding: 25px; /* Increased padding */
        margin-top: 20px;
        color: #004085;
        transition: opacity 0.5s ease-in-out; /* Fade transition for showing */
    }

     #explanation h2 {
        color: #007bff;
        margin-top: 0;
        font-size: 1.5rem;
        margin-bottom: 20px;
     }

    #explanation p {
        margin-bottom: 15px;
    }

    #explanation ul, #explanation ol {
        margin-top: 15px;
        margin-bottom: 15px;
        padding-right: 25px; /* Adjust padding for RTL */
    }

    #explanation li {
        margin-bottom: 10px;
    }

     .xor-color { color: #1e7e34; font-weight: bold; }
     .and-color { color: #c82333; font-weight: bold; }
     .or-color { color: #d39e00; font-weight: bold; }

     .logic-table {
         width: auto; /* Adjust width */
         margin: 20px auto; /* Center table */
         border-collapse: collapse;
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
         font-size: 0.95rem;
     }

     .logic-table th, .logic-table td {
         border: 1px solid #ddd;
         padding: 10px 15px;
         text-align: center;
     }

     .logic-table th {
         background-color: #007bff;
         color: white;
         font-weight: bold;
     }

     .logic-table tr:nth-child(even) {
         background-color: #f2f2f2;
     }

      /* Optional: Responsive adjustments */
     @media (max-width: 768px) {
         .circuit-container {
             flex-direction: column; /* Stack elements vertically */
             gap: 60px; /* Increase gap when stacked */
             padding-top: 50px; /* Add space for potentially overlapping connections */
             padding-bottom: 50px;
         }

         .inputs, .outputs {
             flex-direction: row; /* Inputs/outputs side-by-side */
             justify-content: center;
             gap: 20px;
             min-width: auto;
             width: 100%; /* Allow inputs/outputs to take full width */
             box-sizing: border-box;
             padding: 0 10px;
         }

         .input-group, .output {
             width: auto; /* Auto width for flexibility */
             text-align: center; /* Center text */
             align-items: center; /* Center label and select */
         }

          .input-group label {
              margin-bottom: 5px;
          }

         .logic-input {
             width: auto; /* Auto width */
             min-width: 80px; /* Ensure min width */
         }

         .gates-container {
             flex-direction: column; /* Stack gate layers vertically */
             gap: 60px;
         }

          .gate-layer {
              flex-direction: row; /* Gates in a layer side-by-side */
               gap: 30px;
          }

         .gate, .output {
              width: 80px;
              height: 45px;
              font-size: 0.9rem;
         }
          .gate::after, .output::after {
              bottom: -20px; /* Adjust label position */
              font-size: 0.75rem;
          }
         .output-value {
              font-size: 1.1rem;
         }

         /* Connection positioning needs significant adjustment in JS for mobile */
         /* The current drawLine logic might break or look strange */
         /* For this exercise, assume desktop layout or complex JS handling */
         /* Keeping the simple div method means connections are best suited for stable layouts */
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const inputA = document.getElementById('inputA');
        const inputB = document.getElementById('inputB');
        const carryIn = document.getElementById('carryIn');

        const xor1Gate = document.getElementById('xor1');
        const and1Gate = document.getElementById('and1');
        const xor2Gate = document.getElementById('xor2');
        const and2Gate = document.getElementById('and2');
        const or1Gate = document.getElementById('or1');

        const sumOutput = document.getElementById('sumOutput');
        const carryOutput = document.getElementById('carryOutput');

        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggleExplanation');

        const gateDelay = 300; // Milliseconds delay between gate updates
        const connectionDelay = 200; // Milliseconds delay for connection pulse

        // Helper function to set state class and content
        function setState(element, state) {
             // Ensure state is 0 or 1
             state = state ? 1 : 0;
            element.classList.remove('state-0', 'state-1');
            element.classList.add(`state-${state}`);
            if (element.classList.contains('output')) {
                 element.querySelector('.output-value').textContent = state;
            }
             // Remove pulse class after animation (if added)
             element.classList.remove('pulse'); // Remove previous pulse
        }

         // Helper function to trigger pulse animation
         function pulseElement(element, state) {
              setState(element, state); // Set state first
              // Use a tiny timeout to re-add the class and trigger animation
              requestAnimationFrame(() => {
                   element.classList.add('pulse');
              });
         }


         // Helper function for gates logic
        function gateLogic(type, input1, input2) {
            input1 = parseInt(input1);
            input2 = parseInt(input2);
            switch (type) {
                case 'AND': return (input1 && input2) ? 1 : 0;
                case 'OR':  return (input1 || input2) ? 1 : 0;
                case 'XOR': return (input1 ^ input2) ? 1 : 0;
                default: return 0;
            }
        }

         // Async function to update the circuit state with animations
        async function updateCircuitAnimated() {
             // Disable inputs during animation
            inputA.disabled = true;
            inputB.disabled = true;
            carryIn.disabled = true;

            // Clear previous states and animations
            const allConnectios = document.querySelectorAll('.connection');
            const allGates = document.querySelectorAll('.gate');
            const allOutputs = document.querySelectorAll('.output');
             const allElementsToClear = [...allConnectios, ...allGates, ...allOutputs, inputA, inputB, carryIn];

             allElementsToClear.forEach(el => {
                 el.classList.remove('state-0', 'state-1', 'pulse');
             });


            const valA = parseInt(inputA.value);
            const valB = parseInt(inputB.value);
            const valCi = parseInt(carryIn.value);

            // Stage 0: Inputs animation
            pulseElement(inputA, valA);
            pulseElement(inputB, valB);
            pulseElement(carryIn, valCi);
            await new Promise(resolve => setTimeout(resolve, connectionDelay)); // Small delay after inputs pulse

            // Stage 1: Inputs to Layer 1 Connections
            pulseElement(document.querySelector('.conn-A-xor1'), valA);
            pulseElement(document.querySelector('.conn-B-xor1'), valB);
            pulseElement(document.querySelector('.conn-A-and1'), valA);
            pulseElement(document.querySelector('.conn-B-and1'), valB);
            await new Promise(resolve => setTimeout(resolve, connectionDelay)); // Delay for connections

            // Stage 2: Layer 1 Gates (XOR1, AND1)
            const xor1Out = gateLogic('XOR', valA, valB);
            pulseElement(xor1Gate, xor1Out);

            const and1Out = gateLogic('AND', valA, valB);
            pulseElement(and1Gate, and1Out);
            await new Promise(resolve => setTimeout(resolve, gateDelay)); // Delay for gates to process

            // Stage 3: Layer 1 & CarryIn to Layer 2 Connections
            pulseElement(document.querySelector('.conn-xor1-xor2'), xor1Out);
            pulseElement(document.querySelector('.conn-xor1-and2'), xor1Out);
            pulseElement(document.querySelector('.conn-carryIn-xor2'), valCi);
            pulseElement(document.querySelector('.conn-carryIn-and2'), valCi);
            await new Promise(resolve => setTimeout(resolve, connectionDelay)); // Delay for connections

            // Stage 4: Layer 2 Gates (XOR2, AND2) & Sum Output
            const xor2Out = gateLogic('XOR', xor1Out, valCi); // Sum output
            pulseElement(xor2Gate, xor2Out);
            pulseElement(sumOutput, xor2Out); // Update Sum output visually
             pulseElement(document.querySelector('.conn-xor2-sum'), xor2Out); // Animate conn to sum

            const and2Out = gateLogic('AND', xor1Out, valCi);
            pulseElement(and2Gate, and2Out);
            await new Promise(resolve => setTimeout(resolve, gateDelay)); // Delay for gates to process

            // Stage 5: ANDs to OR1 Connections
             pulseElement(document.querySelector('.conn-and1-or1'), and1Out);
             pulseElement(document.querySelector('.conn-and2-or1'), and2Out);
            await new Promise(resolve => setTimeout(resolve, connectionDelay)); // Delay for connections

            // Stage 6: OR1 Gate & Carry Output
            const or1Out = gateLogic('OR', and1Out, and2Out); // Carry output
            pulseElement(or1Gate, or1Out);
            pulseElement(carryOutput, or1Out); // Update Carry Out output visually
             pulseElement(document.querySelector('.conn-or1-carry'), or1Out); // Animate conn to carry

            // Animation finished, enable inputs
            inputA.disabled = false;
            inputB.disabled = false;
            carryIn.disabled = false;

        }


         // --- Connection Drawing Logic ---
         // Using data attributes to store connection points
        function positionConnections() {
            const app = document.getElementById('logic-circuit-app');
            const appRect = app.getBoundingClientRect();

            const getElementCenter = (selector) => {
                const el = document.querySelector(selector);
                if (!el) return null;
                const rect = el.getBoundingClientRect();
                 // Calculate center relative to the app container
                const x = rect.left + rect.width / 2 - appRect.left;
                const y = rect.top + rect.height / 2 - appRect.top;
                return { x, y };
            };

             document.querySelectorAll('.connection').forEach(lineEl => {
                 const startElSelector = lineEl.getAttribute('data-from');
                 const endElSelector = lineEl.getAttribute('data-to');
                 const startOffsetX = parseInt(lineEl.getAttribute('data-from-offset-x')) || 0;
                 const startOffsetY = parseInt(lineEl.getAttribute('data-from-offset-y')) || 0;
                 const endOffsetX = parseInt(lineEl.getAttribute('data-to-offset-x')) || 0;
                 const endOffsetY = parseInt(lineEl.getAttribute('data-to-offset-y')) || 0;


                 const start = getElementCenter(startElSelector);
                 const end = getElementCenter(endElSelector);

                 if (!start || !end) {
                      console.warn(`Could not find start or end element for connection: ${startElSelector} -> ${endElSelector}`);
                     return;
                 }

                 const x1 = start.x + startOffsetX;
                 const y1 = start.y + startOffsetY;
                 const x2 = end.x + endOffsetX;
                 const y2 = end.y + endOffsetY;

                 // Calculate distance and angle
                 const distance = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
                 const angle = Math.atan2(y2 - y1, x2 - x1);

                 // Position the line element
                 lineEl.style.width = `${distance}px`;
                 lineEl.style.left = `${x1}px`;
                 lineEl.style.top = `${y1}px`;
                 lineEl.style.transform = `rotate(${angle}rad)`;
                 // Transform origin is already set in CSS to 0 0
             });
         }


        // Add event listeners to inputs
        inputA.addEventListener('change', updateCircuitAnimated);
        inputB.addEventListener('change', updateCircuitAnimated);
        carryIn.addEventListener('change', updateCircuitAnimated);

        // Add event listener for the explanation button
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.classList.toggle('hidden');
            toggleButton.textContent = isHidden ? 'הצג איך זה עובד (הסבר מפורט)' : 'הסתר הסבר';
            toggleButton.setAttribute('aria-expanded', !isHidden);
            explanationDiv.setAttribute('aria-hidden', isHidden);
        });

        // Initial setup
        // Use setTimeout to ensure all elements are rendered before positioning connections
        setTimeout(() => {
             positionConnections(); // Position lines on load
             updateCircuitAnimated(); // Calculate and display initial state with animation
        }, 50); // Short delay


        // Re-position connections on window resize with a debounce
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                 positionConnections();
                 // Re-run animation after resize if needed, or just update state
                 // updateCircuitAnimated(); // Might be annoying on resize
                 // A simpler update might be better on resize:
                 const valA = parseInt(inputA.value);
                 const valB = parseInt(inputB.value);
                 const valCi = parseInt(carryIn.value);
                 const xor1Out = gateLogic('XOR', valA, valB);
                 const and1Out = gateLogic('AND', valA, valB);
                 const xor2Out = gateLogic('XOR', xor1Out, valCi);
                 const and2Out = gateLogic('AND', xor1Out, valCi);
                 const or1Out = gateLogic('OR', and1Out, and2Out);

                 setState(inputA, valA); setState(inputB, valB); setState(carryIn, valCi);
                 setState(xor1Gate, xor1Out); setState(and1Gate, and1Out);
                 setState(xor2Gate, xor2Out); setState(and2Gate, and2Out); setState(or1Gate, or1Out);
                 setState(sumOutput, xor2Out); setState(carryOutput, or1Out);

                  document.querySelectorAll('.connection').forEach(lineEl => {
                     const fromElSelector = lineEl.getAttribute('data-from');
                     const toElSelector = lineEl.getAttribute('data-to');
                     let state = 0; // Default state

                     if (fromElSelector === '#inputA') state = parseInt(inputA.value);
                     else if (fromElSelector === '#inputB') state = parseInt(inputB.value);
                     else if (fromElSelector === '#carryIn') state = parseInt(carryIn.value);
                     else if (fromElSelector === '#xor1') state = xor1Out;
                     else if (fromElSelector === '#and1') state = and1Out;
                     else if (fromElSelector === '#xor2') state = xor2Out;
                     else if (fromElSelector === '#and2') state = and2Out;
                     else if (fromElSelector === '#or1') state = or1Out;

                      setState(lineEl, state);
                 });

            }, 100); // Debounce delay
        });
    });
</script>