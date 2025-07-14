---
title: "הרפתקת איזון משוואות כימיות"
english_slug: "balancing-chemical-equations-tool"
category: "מדעים מדויקים / כימיה"
tags: ["סימולציה", "כלי אינטראקטיבי", "אנימציה", "איזון משוואות", "למידה ויזואלית", "מעבדה וירטואלית"]
---
# הרפתקת איזון משוואות כימיות

ברוכים הבאים למעבדה הווירטואלית שלכם! כאן תגלו את סוד איזון המשוואות הכימיות. זכרו את חוק שימור המסה: אטומים לא נעלמים ולא נוצרים יש מאין במהלך תגובה כימית. מספר האטומים מכל יסוד חייב להיות זהה לחלוטין לפני התגובה (המגיבים) ואחריה (התוצרים). השתמשו בכלי האינטראקטיבי הזה כדי לשחק עם מקדמים, לראות את האטומים קופצים למקומם, ולהגיע לאיזון המושלם!

<div id="balancing-app" dir="rtl">
    <div class="input-area">
        <label for="equation-input">הכניסו משוואה כימית (לדוגמה: H2 + O2 -> H2O):</label>
        <input type="text" id="equation-input" value="H2 + O2 -> H2O" placeholder="לדוגמה: H2 + O2 -> H2O">
        <button id="parse-button">טען משוואה</button>
    </div>

    <div id="equation-display" class="equation-display">
        <!-- Parsed equation with coefficient inputs will be loaded here -->
        <p class="placeholder">הכניסו משוואה ולחצו "טען משוואה" כדי להתחיל!</p>
    </div>

     <div id="controls-and-feedback">
         <button id="check-button">בדוק איזון</button>
         <div id="feedback" class="feedback"></div>
     </div>


    <div id="atom-counts" class="atom-counts">
        <h3>מניין אטומים</h3>
        <div class="counts-table">
            <!-- Atom counts will be displayed here -->
            <p class="placeholder">טבלת מניין האטומים תופיע כאן.</p>
        </div>
    </div>

    <div id="visual-representation" class="visual-representation">
        <div class="side reactants-side">
            <h3>מגיבים</h3>
            <div class="molecules">
                 <p class="placeholder">המולקולות של המגיבים יופיעו כאן.</p>
            </div>
        </div>
        <div class="arrow">⇄</div> <!-- More dynamic arrow -->
        <div class="side products-side">
            <h3>תוצרים</h3>
            <div class="molecules">
                 <p class="placeholder">המולקולות של התוצרים יופיעו כאן.</p>
            </div>
        </div>
    </div>


</div>

<button id="toggle-explanation" class="toggle-explanation-button">הצג הסבר: איך מאזנים משוואה?</button>

<div id="explanation" class="explanation" style="display: none;">
    <h2>הסבר: מהו איזון משוואה כימית ולמה זה חשוב?</h2>
    <p>משוואה כימית היא כמו מתכון לתגובה כימית. היא מציגה את החומרים ההתחלתיים (המגיבים, מצד שמאל של החץ) ואת החומרים החדשים שנוצרו (התוצרים, מצד ימין של החץ). החץ (→) מייצג את תהליך השינוי.</p>
    <p>אבל בכימיה, האטומים לא נעלמים סתם ככה! הם רק מסדרים את עצמם מחדש. זהו "חוק שימור המסה", אחד החוקים הבסיסיים בכימיה. הוא אומר שסך כל המסה של המגיבים חייבת להיות שווה לסך כל המסה של התוצרים. זה אומר שמספר האטומים מכל סוג חייב להיות זהה בשני צידי המשוואה.</p>
    <p>משוואה שבה מספר האטומים מכל יסוד שווה בשני הצדדים נקראת **משוואה מאוזנת**.</p>

    <h3>איך מאזנים משוואה? הנה הכלל החשוב ביותר:</h3>
    <p>מאזנים משוואה רק על ידי הוספת **מקדמים סטוכיומטריים**. אלו מספרים שלמים גדולים שמוצבים לפני הנוסחה הכימית של מולקולה או אטום בודד (כמו 2H₂O או 3Fe). מקדם זה מכפיל את מספר האטומים של כל יסוד באותה יחידה. למשל, 2H₂O פירושו 2 מולקולות מים, ובסך הכל יש בהן 4 אטומי מימן (2 × 2) ו-2 אטומי חמצן (2 × 1).</p>
    <p>אתם **אסורים** לשנות את המספרים הקטנים בתחתית הנוסחה (האינדקסים, כמו ה-₂ ב-H₂O)! שינוי האינדקסים משנה את סוג החומר לגמרי (H₂O זה מים, H₂O₂ זה מי חמצן - חומר שונה לחלוטין!).</p>

    <h3>בואו נראה דוגמה: איזון יצירת מים H₂ + O₂ → H₂O</h3>
    <ol>
        <li>**סופרים אטומים (משוואה לא מאוזנת):**
            <ul>
                <li>מגיבים: 2H, 2O</li>
                <li>תוצרים: 2H, 1O</li>
            </ul>
            מספר אטומי החמצן לא שווה.
        </li>
        <li>**מאזנים חמצן:** יש O אחד בצד התוצרים, ו-2 בצד המגיבים. כדי לאזן, נכפיל את מולקולת המים ב-2. נוסיף מקדם 2 לפני H₂O:<br>H₂ + O₂ → **2**H₂O</li>
        <li>**סופרים אטומים שוב (אחרי הוספת מקדם):**
            <ul>
                <li>מגיבים: 2H, 2O</li>
                <li>תוצרים: 2 × 2 = 4H, 2 × 1 = 2O</li>
            </ul>
            החמצן מאוזן (2 בשני הצדדים), אבל המימן לא (2 במגיבים, 4 בתוצרים).
        </li>
        <li>**מאזנים מימן:** יש 2H במגיבים ו-4H בתוצרים. כדי לאזן, נכפיל את מולקולת המימן (H₂) ב-2. נוסיף מקדם 2 לפני H₂:<br>**2**H₂ + O₂ → 2H₂O</li>
        <li>**סופרים אטומים בפעם האחרונה:**
            <ul>
                <li>מגיבים: 2 × 2 = 4H, 2O</li>
                <li>תוצרים: 2 × 2 = 4H, 2 × 1 = 2O</li>
            </ul>
        </li>
    </ol>
    <p>מעולה! עכשיו מספר אטומי המימן זהה (4) ומספר אטומי החמצן זהה (2) בשני הצדדים. המשוואה **מאוזנת**!</p>
    <p>הכלי האינטראקטיבי מאפשר לכם לעשות בדיוק את זה - להקליד משוואה, לשחק עם המספרים הגדולים (המקדמים), ולראות מיד איך זה משפיע על כמות האטומים מכל סוג, עד שתצליחו לאזן את הכל! בהצלחה!</p>
</div>

<style>
    /* General App Styling */
    #balancing-app {
        font-family: 'Heebo', sans-serif; /* Modern, clean font */
        direction: rtl;
        text-align: right;
        padding: 25px;
        border: 1px solid #007bff; /* Stronger, branded border */
        border-radius: 12px; /* More rounded corners */
        margin: 20px auto; /* Center the app */
        max-width: 800px; /* Max width for better readability */
        background-color: #e9f5ff; /* Light blue background */
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* More pronounced shadow */
        position: relative; /* Needed for potential absolute positioning */
    }

    #balancing-app h3 {
        text-align: center;
        color: #0056b3; /* Darker blue for headings */
        margin-bottom: 15px;
        font-size: 1.4em;
    }

     .placeholder {
         text-align: center;
         color: #666;
         font-style: italic;
         padding: 20px;
     }

    /* Input Area */
    .input-area {
        margin-bottom: 25px;
        text-align: center;
        display: flex;
        flex-wrap: wrap; /* Allow wrapping on small screens */
        justify-content: center;
        align-items: center;
        gap: 10px; /* Space between input and button */
    }

    .input-area label {
        font-weight: bold;
        color: #0056b3;
        white-space: nowrap; /* Prevent label from wrapping */
    }

    .input-area input[type="text"] {
        padding: 10px;
        border: 1px solid #007bff;
        border-radius: 5px;
        width: 280px; /* Slightly wider input */
        box-sizing: border-box; /* Include padding in width */
        font-size: 1em;
    }

    /* Buttons */
    .input-area button,
    #check-button,
    .toggle-explanation-button {
        padding: 10px 20px; /* More padding */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        margin-right: 0; /* Reset margin for RTL, use gap in flexbox */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .input-area button:hover,
    #check-button:hover,
    .toggle-explanation-button:hover {
        background-color: #0056b3;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

     .input-area button:active,
    #check-button:active,
    .toggle-explanation-button:active {
        transform: scale(0.98);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

     #controls-and-feedback {
         display: flex;
         justify-content: center;
         align-items: center;
         gap: 20px; /* Space between button and feedback */
         margin-bottom: 20px;
         flex-wrap: wrap; /* Allow wrapping */
     }


    /* Equation Display */
    .equation-display {
        text-align: center;
        font-size: 1.6em; /* Slightly larger */
        margin-bottom: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        min-height: 50px; /* Reserve space */
    }

    .equation-part {
        display: flex;
        align-items: center;
        margin: 0 8px; /* Reduced margin */
        transition: transform 0.3s ease; /* Smooth transition on potential changes */
    }


    .equation-part .operator {
         margin: 0 8px;
         font-weight: bold;
         color: #333;
    }

    .equation-part input[type="number"] {
        width: 50px; /* Slightly wider input */
        padding: 8px;
        margin: 0 6px;
        border: 1px solid #007bff;
        border-radius: 5px;
        font-size: 1em;
        text-align: center;
        -moz-appearance: textfield; /* Remove default number arrows in Firefox */
        appearance: textfield;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .equation-part input[type="number"]::-webkit-outer-spin-button,
    .equation-part input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none; /* Remove default number arrows in Chrome/Safari */
        margin: 0;
    }

    .equation-part input[type="number"]:focus {
        border-color: #0056b3;
        box-shadow: 0 0 8px rgba(0,123,255,0.4);
        outline: none;
    }


    .formula {
        font-weight: bold;
        color: #555;
    }

    .subscript {
        vertical-align: sub;
        font-size: 0.7em; /* Slightly smaller subscript */
        color: #333;
    }

    /* Visual Representation */
    .visual-representation {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 20px; /* Added margin-top */
        margin-bottom: 30px;
        flex-wrap: wrap;
        background-color: #ffffff; /* White background for clarity */
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 20px 10px; /* Padding inside visual area */
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.05); /* Inner shadow */
    }

    .visual-representation .side {
        flex: 1;
        min-width: 280px; /* Increased min-width */
        padding: 15px;
        background-color: #f8f9fa; /* Very light grey */
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        margin: 10px; /* Margin around sides */
        min-height: 150px; /* Ensure enough height */
    }

    .visual-representation .arrow {
        font-size: 2.5em; /* Larger arrow */
        margin: 0 20px;
        font-weight: bold;
        color: #007bff;
        animation: pulse-arrow 2s infinite ease-in-out; /* Arrow pulse animation */
    }

     @keyframes pulse-arrow {
         0%, 100% { transform: scale(1); color: #007bff; }
         50% { transform: scale(1.1); color: #0056b3; }
     }


    .side .molecules {
        display: flex;
        flex-wrap: wrap;
        gap: 12px; /* Space between molecules */
        justify-content: center;
        min-height: 100px; /* Minimum height for molecule area */
        align-content: flex-start; /* Align rows to the top */
    }

    .molecule {
        display: inline-flex; /* Use inline-flex */
        align-items: center;
        justify-content: center;
        background-color: #e9ecef;
        border-radius: 15px; /* More rounded pills */
        padding: 6px 12px; /* Padding inside molecule pill */
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, opacity 0.3s ease; /* Animation for appearance */
        opacity: 1; /* Default state */
    }

     /* Animation class for new molecules */
    .molecule.entering {
        opacity: 0;
        transform: scale(0.8);
    }
     .molecule.entered {
        opacity: 1;
        transform: scale(1);
     }

     .molecule span {
        margin: 0 1.5px; /* Less space between atoms */
     }


    .atom {
        display: inline-block;
        width: 22px; /* Slightly larger atoms */
        height: 22px;
        border-radius: 50%;
        margin: 1px; /* Less margin between atoms */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75em; /* Slightly larger font */
        font-weight: bold;
        color: white;
        border: 1.5px solid rgba(255,255,255,0.7); /* Thicker white outline */
        box-shadow: 0 1px 3px rgba(0,0,0,0.2); /* Stronger atom shadow */
        text-shadow: 0 1px 1px rgba(0,0,0,0.3); /* Text shadow for readability */
        transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth color/size transition */
    }

    /* Atom Colors - Enhanced Palette */
    .atom.H { background-color: #6699ff; } /* Brighter Blue */
    .atom.O { background-color: #ff6666; } /* Brighter Red */
    .atom.C { background-color: #99cc99; } /* Soft Green */
    .atom.N { background-color: #ffcc66; } /* Softer Yellow */
    .atom.Cl { background-color: #73d0ff; } /* Sky Blue */
    .atom.Na { background-color: #ff9966; } /* Coral Orange */
    .atom.S { background-color: #ffff66; } /* Bright Yellow */
    .atom.Fe { background-color: #a0a0a0; } /* Medium Grey */
    .atom.Cu { background-color: #cc9966; } /* Copper Brown */
    .atom.P { background-color: #ff99cc; } /* Pink */
    .atom.K { background-color: #9966cc; } /* Purple */
    .atom.Mg { background-color: #99e6b3; } /* Mint Green */
    .atom.Ca { background-color: #ffb366; } /* Peach */


    /* Atom Counts */
    .atom-counts {
        margin-bottom: 25px;
        text-align: center;
    }

    .counts-table {
        display: inline-block;
        text-align: right;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        padding: 15px 20px; /* More padding */
        min-width: 220px; /* Slightly wider */
        border: 1px solid #eee;
    }

    .counts-table div {
        display: flex;
        justify-content: space-between;
        padding: 8px 0; /* More padding */
        border-bottom: 1px solid #eee; /* Solid separator */
        font-size: 1.1em; /* Slightly larger font */
    }

    .counts-table div:last-child {
        border-bottom: none;
    }

    .counts-table .element-symbol {
        font-weight: bold;
        color: #333;
        margin-left: 10px;
    }

    .counts-table .count {
        font-family: 'Courier New', monospace;
        display: flex;
        align-items: center;
    }

    .count .reactant-count {
        color: #007bff;
        margin-left: 8px; /* More space */
         transition: color 0.3s ease; /* Smooth color transition */
    }

    .count .product-count {
        color: #ea4335; /* Red when unbalanced */
        transition: color 0.3s ease; /* Smooth color transition */
    }

     .count .product-count.balanced {
        color: #34a853; /* Green when balanced */
     }

     .count-update-flash {
        animation: flash 0.5s ease-out; /* Animation for count update */
     }

     @keyframes flash {
        0% { background-color: rgba(0,123,255,0.2); } /* Light blue flash */
        100% { background-color: transparent; }
     }


    /* Feedback Messages */
    .feedback {
        text-align: center;
        font-size: 1.4em; /* Larger font */
        margin-top: 15px; /* Adjusted margin */
        min-height: 1.8em; /* Reserve space */
        font-weight: bold;
        transition: color 0.3s ease;
    }

    .feedback.balanced {
        color: #34a853; /* Green */
        animation: pulse-success 1.5s infinite alternate; /* Enhanced pulse animation */
    }

    .feedback.unbalanced {
        color: #ea4335; /* Red */
        animation: shake 0.6s ease-in-out; /* Slightly longer, smoother shake */
    }

     /* Animation keyframes */
    @keyframes pulse-success {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.08); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-10px); }
        40%, 80% { transform: translateX(10px); }
    }


    /* Explanation Section */
    .explanation {
        margin-top: 30px;
        padding: 25px; /* More padding */
        border: 2px dashed #007bff; /* More prominent dashed border */
        border-radius: 12px;
        background-color: #f0f8ff; /* Very light blue */
        direction: rtl;
        text-align: right;
        line-height: 1.7; /* Improved line spacing */
        color: #333;
    }

    .explanation h2 {
        color: #0056b3;
        text-align: center;
        margin-bottom: 20px;
        font-size: 1.6em;
    }

    .explanation h3 {
         color: #0056b3;
         margin-top: 15px;
         margin-bottom: 10px;
         font-size: 1.3em;
         text-align: right; /* Align explanation subheadings right */
    }

    .explanation p, .explanation ul, .explanation ol {
        margin-bottom: 15px;
        color: #333;
    }

    .explanation ul, .explanation ol {
        padding-right: 25px; /* Adjust padding for RTL list markers */
    }

    .explanation li {
        margin-bottom: 10px;
    }

    .toggle-explanation-button {
        display: block;
        margin: 20px auto;
        background-color: #6c757d; /* Grey color */
        font-weight: normal; /* Normal font weight */
    }
    .toggle-explanation-button:hover {
        background-color: #5a6268;
    }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .visual-representation {
            flex-direction: column; /* Stack sides vertically */
            align-items: stretch;
        }
        .visual-representation .arrow {
            margin: 10px auto; /* Center arrow vertically */
            transform: rotate(90deg); /* Rotate arrow */
        }
         .side {
            margin: 10px 0; /* Adjust margin for vertical stack */
         }
         .input-area {
             flex-direction: column;
         }
         .input-area label {
             margin-bottom: 5px;
         }
         .input-area input[type="text"] {
            width: 100%; /* Full width on small screens */
         }
         #controls-and-feedback {
             flex-direction: column;
             gap: 10px;
         }
    }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const equationInput = document.getElementById('equation-input');
        const parseButton = document.getElementById('parse-button');
        const equationDisplay = document.getElementById('equation-display');
        const visualRepresentation = document.getElementById('visual-representation');
        const reactantsSide = visualRepresentation.querySelector('.reactants-side .molecules');
        const productsSide = visualRepresentation.querySelector('.products-side .molecules');
        const atomCountsDiv = document.querySelector('#atom-counts .counts-table');
        const checkButton = document.getElementById('check-button');
        const feedbackDiv = document.getElementById('feedback');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');

        let reactants = [];
        let products = [];
        let coefficientInputs = {}; // Store references to coefficient input elements
        let currentAtomCounts = {}; // Store calculated counts { element: { reactant: X, product: Y }, ... }


        // --- Utility Functions ---

        // Improved Regex to parse a formula, handles basic parentheses and elements.
        // Still might not parse highly complex organic formulas perfectly, but better.
        function parseFormula(formulaString) {
            const atoms = {};
            // Regex to match:
            // 1. Element symbol (like H, O, Fe) potentially followed by a number (like H2, O2)
            // 2. Group in parentheses (like (OH)) potentially followed by a number (like (NH4)2)
            const regex = /([A-Z][a-z]*)(\d*)|(?:\(([A-Za-z0-9]+)\))(\d*)/g;
            let match;
            let tempString = formulaString.trim();
            let lastIndex = 0;

            while ((match = regex.exec(tempString)) !== null) {
                 // Check if there's unparsed text between matches
                 if (match.index > lastIndex) {
                     const unparsed = tempString.substring(lastIndex, match.index).trim().replace(/[+\-\s]/g, '');
                     if (unparsed.length > 0) {
                         console.warn(`Warning: Unparsed segment found in formula "${formulaString}": "${unparsed}"`);
                         // Attempt to parse any leftover single elements? Or just warn?
                         // For now, just warn and skip.
                     }
                 }

                 if (match[1]) { // Simple element like H or O2
                    const element = match[1];
                    const count = match[2] ? parseInt(match[2]) : 1;
                    atoms[element] = (atoms[element] || 0) + count;
                } else if (match[3]) { // Group in parentheses like (NH4)2
                     const groupContent = match[3];
                     const groupMultiplier = match[4] ? parseInt(match[4]) : 1;
                     const groupAtoms = parseFormula(groupContent); // Recursively parse group
                     for (const element in groupAtoms) {
                         atoms[element] = (atoms[element] || 0) + (groupAtoms[element] * groupMultiplier);
                     }
                }
                lastIndex = regex.lastIndex; // Update last index
            }

            // Check for unparsed text at the end
            if (lastIndex < tempString.length) {
                 const unparsed = tempString.substring(lastIndex).trim().replace(/[+\-\s]/g, '');
                 if (unparsed.length > 0) {
                     console.warn(`Warning: Unparsed tail found in formula "${formulaString}": "${unparsed}"`);
                 }
            }

            return atoms;
        }


         function renderFormulaHTML(formulaString) {
            // Renders formula string with subscripts
            // Also escapes HTML characters just in case
            let html = formulaString
                 .replace(/&/g, '&amp;')
                 .replace(/</g, '&lt;')
                 .replace(/>/g, '&gt;')
                 .replace(/"/g, '&quot;')
                 .replace(/'/g, '&#039;');

            // Add subscripts
            html = html.replace(/([A-Za-z)])(\d+)/g, '$1<span class="subscript">$2</span>');

             return html;
         }


        function getAtomColor(symbol) {
            // Enhanced mapping, add more as needed
            const colors = {
                'H': '#6699ff', /* Brighter Blue */
                'O': '#ff6666', /* Brighter Red */
                'C': '#99cc99', /* Soft Green */
                'N': '#ffcc66', /* Softer Yellow */
                'Cl': '#73d0ff', /* Sky Blue */
                'Na': '#ff9966', /* Coral Orange */
                'S': '#ffff66', /* Bright Yellow */
                'Fe': '#a0a0a0', /* Medium Grey */
                'Cu': '#cc9966', /* Copper Brown */
                'P': '#ff99cc', /* Pink */
                'K': '#9966cc', /* Purple */
                'Mg': '#99e6b3', /* Mint Green */
                'Ca': '#ffb366', /* Peach */
                'B': '#c2c2f0', /* Light Purple */
                'Br': '#a52a2a', /* Brown */
                'I': '#8a2be2', /* Blue Violet */
                'F': '#32cd32', /* Lime Green */
                'Li': '#f08080', /* Light Coral */
                 'Al': '#cccccc', /* Light Grey */
                 'Si': '#f08080', /* Light Coral (using same as Li for now, pick a new one if needed) */
                 'Zn': '#b0c4de' /* Light Steel Blue */

                // Add more elements...
            };
            return colors[symbol] || '#9b59b6'; // Default Purple
        }

         // Helper to create a visual atom span
        function createAtomSpan(elementSymbol) {
            const span = document.createElement('span');
            span.classList.add('atom', elementSymbol);
            span.style.backgroundColor = getAtomColor(elementSymbol);
            span.textContent = elementSymbol;
            return span;
        }


         // Helper to create a visual molecule div
         function createMoleculeDiv(formulaString) {
            const moleculeDiv = document.createElement('div');
            moleculeDiv.classList.add('molecule', 'entering'); // Add 'entering' class for animation
             // Use a timeout to trigger the 'entered' class after adding to DOM
             setTimeout(() => {
                 moleculeDiv.classList.remove('entering');
                 moleculeDiv.classList.add('entered');
             }, 10); // Small delay allows the initial state to be set before transition

            const atoms = parseFormula(formulaString);
             const atomsArray = [];
             // Create atom spans and add to a temp array
            for (const element in atoms) {
                for (let i = 0; i < atoms[element]; i++) {
                    atomsArray.push(createAtomSpan(element));
                }
            }
            // Optionally sort atoms within the molecule for consistency
             atomsArray.sort((a, b) => a.textContent.localeCompare(b.textContent));

            // Append atom spans to the molecule div
             atomsArray.forEach(atomSpan => moleculeDiv.appendChild(atomSpan));


            return moleculeDiv;
         }


        function updateVisualsAndCounts() {
             // Clear previous visuals and counts
             reactantsSide.innerHTML = '';
             productsSide.innerHTML = '';
             atomCountsDiv.innerHTML = '';
             // Do NOT clear feedback here, it's controlled by checkButton

             currentAtomCounts = {}; // Reset counts for this update
             const allElements = new Set();

             // Render Reactants & Calculate Counts
             reactants.forEach((formula, index) => {
                 const input = coefficientInputs[`reactant-${index}`];
                 const coefficient = parseInt(input?.value) || 0; // Use 0 if input is not found or value is invalid
                 const atomsInMolecule = parseFormula(formula);

                 for (let i = 0; i < coefficient; i++) {
                     reactantsSide.appendChild(createMoleculeDiv(formula)); // Add molecule element
                 }

                 // Update counts for reactants
                 for (const element in atomsInMolecule) {
                     if (!currentAtomCounts[element]) currentAtomCounts[element] = { reactant: 0, product: 0 };
                     currentAtomCounts[element].reactant += (atomsInMolecule[element] * coefficient);
                     allElements.add(element);
                 }
             });

             // Render Products & Calculate Counts
             products.forEach((formula, index) => {
                  const input = coefficientInputs[`product-${index}`];
                  const coefficient = parseInt(input?.value) || 0; // Use 0 if input is not found or value is invalid
                  const atomsInMolecule = parseFormula(formula);

                  for (let i = 0; i < coefficient; i++) {
                      productsSide.appendChild(createMoleculeDiv(formula)); // Add molecule element
                  }

                  // Update counts for products
                  for (const element in atomsInMolecule) {
                      if (!currentAtomCounts[element]) currentAtomCounts[element] = { reactant: 0, product: 0 };
                      currentAtomCounts[element].product += (atomsInMolecule[element] * coefficient);
                      allElements.add(element);
                  }
              });

            // Display Atom Counts and highlight balance
            const sortedElements = Array.from(allElements).sort();
            sortedElements.forEach(element => {
                const rCount = currentAtomCounts[element]?.reactant || 0;
                const pCount = currentAtomCounts[element]?.product || 0;
                const isBalanced = rCount === pCount && (rCount > 0 || reactants.length === 0 && products.length === 0); // Consider 0 balanced only if equation is empty or all coefficients are 0? Let's stick to rCount === pCount
                const elementDiv = document.createElement('div');
                elementDiv.innerHTML = `
                    <span class="element-symbol">${element}:</span>
                    <span class="count">
                        <span class="reactant-count">${rCount}</span>
                        →
                        <span class="product-count ${isBalanced ? 'balanced' : ''}">${pCount}</span>
                    </span>
                `;
                 // Add a temporary class to trigger flash animation on counts update
                 elementDiv.querySelector('.reactant-count').classList.add('count-update-flash');
                 elementDiv.querySelector('.product-count').classList.add('count-update-flash');

                 atomCountsDiv.appendChild(elementDiv);

                 // Remove the flash class after the animation
                 setTimeout(() => {
                     elementDiv.querySelector('.reactant-count').classList.remove('count-update-flash');
                     elementDiv.querySelector('.product-count').classList.remove('count-update-flash');
                 }, 600); // Match animation duration
            });

             // Add placeholders if no elements are present (e.g., before parsing)
             if (sortedElements.length === 0) {
                  atomCountsDiv.innerHTML = '<p class="placeholder">טבלת מניין האטומים תופיע כאן.</p>';
             }
             if (reactants.length === 0 && products.length === 0) {
                 reactantsSide.innerHTML = '<p class="placeholder">המולקולות של המגיבים יופיעו כאן.</p>';
                 productsSide.innerHTML = '<p class="placeholder">המולקולות של התוצרים יופיעו כאן.</p>';
                  equationDisplay.innerHTML = '<p class="placeholder">הכניסו משוואה ולחצו "טען משוואה" כדי להתחיל!</p>';
             }


        }

        // --- Event Handlers ---

        parseButton.addEventListener('click', () => {
            const equationString = equationInput.value.trim();
            if (!equationString.includes('->')) {
                feedbackDiv.className = 'feedback unbalanced';
                feedbackDiv.textContent = '❌ פורמט משוואה לא תקין. השתמש ב"->" להפרדה בין מגיבים לתוצרים.';
                equationDisplay.innerHTML = '<p class="placeholder">הכניסו משוואה ולחצו "טען משוואה" כדי להתחיל!</p>';
                 reactants = []; products = [];
                 updateVisualsAndCounts(); // Clear display
                return;
            }

            const parts = equationString.split('->').map(side => side.trim());
            reactants = parts[0].split('+').map(formula => formula.trim()).filter(f => f);
            products = parts[1].split('+').map(formula => formula.trim()).filter(f => f);

            if (reactants.length === 0 || products.length === 0) {
                 feedbackDiv.className = 'feedback unbalanced';
                 feedbackDiv.textContent = '❌ יש להכניס מגיבים ותוצרים.';
                 equationDisplay.innerHTML = '<p class="placeholder">הכניסו משוואה ולחצו "טען משוואה" כדי להתחיל!</p>';
                 reactants = []; products = [];
                 updateVisualsAndCounts(); // Clear display
                 return;
            }

            // Clear previous display
            equationDisplay.innerHTML = '';
            coefficientInputs = {}; // Reset coefficient inputs

            // Build the equation display with inputs
            reactants.forEach((formula, index) => {
                if (index > 0) equationDisplay.innerHTML += '<span class="operator">+</span>';
                const partDiv = document.createElement('div');
                partDiv.classList.add('equation-part');
                partDiv.innerHTML = `
                    <input type="number" min="0" value="1" class="coefficient-input" data-side="reactant" data-index="${index}">
                    <span class="formula">${renderFormulaHTML(formula)}</span>
                `;
                 equationDisplay.appendChild(partDiv);
            });

            equationDisplay.innerHTML += '<span class="operator">⇄</span>'; // Use the new arrow

            products.forEach((formula, index) => {
                 if (index > 0) equationDisplay.innerHTML += '<span class="operator">+</span>';
                 const partDiv = document.createElement('div');
                 partDiv.classList.add('equation-part');
                 partDiv.innerHTML = `
                     <input type="number" min="0" value="1" class="coefficient-input" data-side="product" data-index="${index}">
                     <span class="formula">${renderFormulaHTML(formula)}</span>
                 `;
                  equationDisplay.appendChild(partDiv);
             });

            // Get references to the new inputs and add event listeners
            equationDisplay.querySelectorAll('.coefficient-input').forEach(input => {
                const side = input.dataset.side;
                const index = input.dataset.index;
                coefficientInputs[`${side}-${index}`] = input;
                // Add event listener to update visuals and counts on input change
                input.addEventListener('input', updateVisualsAndCounts);
                 // Add event listener to select text on focus
                 input.addEventListener('focus', function() { this.select(); });
                 // Set initial value to 1 for all inputs on parse
                 input.value = 1;
            });

            // Initial rendering after parsing and setting inputs
            updateVisualsAndCounts();
             // Clear feedback when a new equation is loaded
            feedbackDiv.className = 'feedback';
            feedbackDiv.textContent = '';
        });

        checkButton.addEventListener('click', () => {
            let isFullyBalanced = true;
             let allCoefficientsZero = true;

            // Check if balanced for all elements based on current counts
            for (const element in currentAtomCounts) {
                const rCount = currentAtomCounts[element].reactant;
                const pCount = currentAtomCounts[element].product;
                if (rCount !== pCount) {
                    isFullyBalanced = false;
                    break; // No need to check further elements if one is unbalanced
                }
                 // Also check if any coefficient is non-zero
                 if (rCount > 0 || pCount > 0) {
                     allCoefficientsZero = false; // At least one element count is non-zero
                 }
            }

             // If the equation was parsed but all coefficients are zero, it's not truly balanced
            if ((reactants.length > 0 || products.length > 0) && allCoefficientsZero) {
                 isFullyBalanced = false;
            }


            feedbackDiv.className = 'feedback'; // Reset classes
            if (isFullyBalanced) {
                feedbackDiv.classList.add('balanced');
                feedbackDiv.textContent = '🎉 יצרת איזון מושלם! כל הכבוד!';
            } else {
                feedbackDiv.classList.add('unbalanced');
                feedbackDiv.textContent = '🧐 עדיין לא מאוזן. בדוק שוב את מניין האטומים לכל יסוד.';
            }

             // Ensure counts table updates visual balance status immediately after check
            updateVisualsAndCounts();
        });

        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג הסבר: איך מאזנים משוואה?';
        });

        // --- Initial Load ---
        // Automatically parse the default equation on page load
        parseButton.click(); // This will parse the default value and set initial inputs/visuals

    });
</script>