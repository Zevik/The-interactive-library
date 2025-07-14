---
title: "קסם העיגול והסכנה שבדיוק: טעויות חישוב במדע"
english_slug: rounding-errors-in-scientific-calculations
category: "טכנולוגיה / מדעי המחשב"
tags: [שגיאות עיגול, אריתמטיקה של נקודה צפה, חישובים נומריים, דיוק, יציבות נומרית]
---
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>קסם העיגול והסכנה שבדיוק: טעויות חישוב במדע</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

        body {
            font-family: 'Heebo', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background: linear-gradient(to bottom, #eef2f7, #e0e8f0); /* Soft gradient background */
            color: #333;
            direction: rtl;
            text-align: right;
        }

        .container {
            max-width: 900px;
            margin: 30px auto; /* More vertical margin */
            background: #fff;
            padding: 30px; /* More padding */
            border-radius: 12px; /* More rounded corners */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
            overflow: hidden; /* Clear floats */
        }

        h1, h2, h3 {
            color: #0056b3;
            text-align: center; /* Center headings */
            margin-bottom: 20px;
            font-weight: 700; /* Bolder headings */
        }
        h1 {
            margin-top: 0;
            font-size: 2.5em;
        }
         h2 {
             font-size: 1.8em;
             border-bottom: 2px solid #007bff; /* Underline H2 */
             padding-bottom: 10px;
         }
         h3 {
             font-size: 1.4em;
             color: #007bff;
             margin-top: 25px;
         }


        p {
            margin-bottom: 15px;
        }

        .app-section {
            margin-top: 40px; /* More space */
            padding: 30px;
            background-color: #f8f9fa; /* Lighter background for app section */
            border-radius: 8px;
            margin-bottom: 30px;
            border: 1px solid #e0e0e0; /* Subtle border */
        }

        .app-controls {
            display: grid; /* Use grid for better control layout */
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
            gap: 20px; /* Space between grid items */
            margin-bottom: 25px;
            align-items: center; /* Vertically align items */
        }

        .app-controls div {
            margin-bottom: 0; /* Remove margin bottom from grid items */
            display: flex; /* Use flexbox for label and input */
            align-items: center;
            justify-content: space-between; /* Space between label and input */
            background-color: #ffffff; /* White background for input rows */
            padding: 12px 15px;
            border-radius: 6px;
            border: 1px solid #dcdcdc;
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
        }

        .app-controls label {
            font-weight: 700; /* Bolder labels */
            color: #555;
            margin-left: 15px; /* Space between label and input */
            flex-grow: 1; /* Allow label to take space */
            text-align: right; /* Align label text right */
        }

        .app-controls input[type="number"] {
            padding: 8px 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 100px; /* Fixed width for inputs */
            direction: ltr; /* Numbers are LTR */
            text-align: left; /* Align numbers left */
            font-size: 1em;
            transition: border-color 0.3s ease; /* Smooth transition on focus */
        }
         .app-controls input[type="number"]:focus {
             border-color: #007bff; /* Highlight on focus */
             box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
         }

        .app-controls button {
            grid-column: 1 / -1; /* Make button span all columns */
            padding: 12px 25px; /* More padding */
            background: linear-gradient(to right, #007bff, #0056b3); /* Gradient button */
            color: white;
            border: none;
            border-radius: 6px; /* More rounded */
            cursor: pointer;
            font-size: 1.1em; /* Larger font */
            font-weight: 700;
            transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transitions */
            box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3); /* Button shadow */
            display: block; /* Make button a block element */
            width: fit-content; /* Button width based on content */
            margin: 15px auto 0; /* Center button and add margin */
        }
        .app-controls button:hover {
            background: linear-gradient(to right, #0056b3, #003d7a); /* Darker gradient on hover */
            box-shadow: 0 6px 12px rgba(0, 123, 255, 0.4);
        }
         .app-controls button:active {
             transform: scale(0.98); /* Press effect */
         }

        .results {
            margin-top: 30px;
            padding: 20px;
            background-color: #e9f7ef; /* Light green background for results */
            border: 1px solid #c8e6c9;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            font-size: 1.1em;
        }

         .results div {
             margin-bottom: 12px; /* More space between result lines */
             padding-bottom: 12px;
             border-bottom: 1px dashed #d0d0d0; /* Dashed separator */
             display: flex; /* Use flexbox for label and value */
             justify-content: space-between; /* Space out label and value */
             align-items: center;
         }
        .results div:last-child {
             margin-bottom: 0;
             padding-bottom: 0;
             border-bottom: none; /* No border for last item */
        }

        .results strong {
            color: #004085; /* Darker blue for labels */
            font-weight: 700;
        }

         .results span {
             flex-shrink: 0; /* Prevent span from shrinking */
             text-align: left; /* Align numbers/results left */
             direction: ltr; /* Ensure results are LTR */
             font-family: monospace; /* Monospace font for numbers */
             color: #006400; /* Dark green for positive results */
         }

         .difference {
             font-weight: 700;
             color: #dc3545; /* Red color for difference */
             background-color: #f8d7da; /* Light red background for difference */
             border-top: 2px solid #dc3545 !important; /* Stronger border top */
             padding-top: 15px !important;
             margin-top: 15px !important;
             border-radius: 0 0 8px 8px; /* Round only bottom corners */
             margin: -20px -20px 0 -20px; /* Extend background to edges of results box */
             padding: 15px 20px 15px 20px !important;
             display: flex;
             justify-content: space-between;
             align-items: center;
         }
         .difference span {
             color: #dc3545; /* Red color for the difference value */
             font-weight: 700;
         }
         .difference strong {
            color: #a71d2a; /* Darker red for difference label */
         }


        /* Visualization Section */
         .visualization-area {
             margin-top: 30px;
             padding: 20px;
             background-color: #f0f4f7; /* Light blue background */
             border-radius: 8px;
             border: 1px solid #d0d8e0;
             overflow: hidden; /* Needed for bar containment */
         }
        .visualization-area h3 {
             margin-top: 0;
             text-align: center;
             color: #0056b3;
         }
        .vis-item {
            margin-bottom: 15px;
        }
         .vis-label {
             font-weight: 700;
             color: #555;
             margin-bottom: 5px;
             font-size: 0.95em;
         }
         .vis-bar-container {
             width: 100%; /* Container takes full width */
             height: 20px; /* Fixed height for bars */
             background-color: #e0e0e0; /* Background for empty bar space */
             border-radius: 4px;
             overflow: hidden; /* Hide overflow if bar exceeds container */
             position: relative; /* Needed for absolute positioning of difference marker */
         }
         .vis-bar {
             height: 100%;
             width: 0; /* Start with 0 width for animation */
             border-radius: 4px;
             transition: width 1.5s ease-out; /* Animation for bar growth */
             position: absolute; /* Position bars within container */
             top: 0;
             left: 0; /* Bars grow from the left */
         }
        .vis-bar.precise {
            background-color: #28a745; /* Green for precise */
             z-index: 2; /* Bring precise bar slightly forward */
        }
        .vis-bar.rounded {
            background-color: #007bff; /* Blue for rounded */
             z-index: 1; /* Keep rounded bar behind */
        }

        .vis-difference-marker {
             position: absolute;
             top: 0;
             bottom: 0;
             width: 3px; /* Width of the marker line */
             background-color: #dc3545; /* Red color for difference */
             z-index: 3; /* Above the bars */
             transition: left 1.5s ease-out; /* Animate marker position */
         }

        .explanation-button-container {
            text-align: center;
            margin-top: 30px;
            margin-bottom: 30px;
        }

        #explanationButton {
            display: inline-block; /* Make it inline-block */
            padding: 12px 25px;
            background-color: #28a745; /* Green button */
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1.1em;
            font-weight: 700;
            transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
        }
        #explanationButton:hover {
            background-color: #218838; /* Darker green on hover */
            box-shadow: 0 6px 12px rgba(40, 167, 69, 0.4);
        }
         #explanationButton:active {
             transform: scale(0.98);
         }


        .explanation-section {
            margin-top: 30px;
            padding: 25px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            border: 1px solid #e0e0e0;
            display: none; /* Hidden by default */
            opacity: 0; /* Start invisible for fade-in */
            transition: opacity 0.5s ease; /* Fade-in animation */
        }
         .explanation-section.visible {
             display: block;
             opacity: 1;
         }

         .explanation-section ul {
             list-style: disc inside;
             padding-right: 20px;
             margin-bottom: 15px;
         }
         .explanation-section li {
             margin-bottom: 8px;
         }
         .explanation-section p:last-child {
             margin-bottom: 0;
         }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 2em;
            }
            h2 {
                font-size: 1.5em;
            }
             .app-controls div {
                 flex-direction: column; /* Stack label and input on small screens */
                 align-items: flex-end; /* Align stacked items to the right */
             }
            .app-controls label {
                margin-left: 0;
                margin-bottom: 5px; /* Space between stacked label and input */
                 width: 100%; /* Label takes full width */
                 text-align: right;
            }
            .app-controls input[type="number"] {
                width: 100%; /* Input takes full width */
                text-align: right; /* Align input text right in stacked layout */
                direction: rtl; /* Numbers display RTL in stacked layout */
            }
            .app-controls button {
                width: 100%; /* Full width button */
            }
            .results div {
                flex-direction: column;
                 align-items: flex-end;
            }
            .results strong {
                 width: 100%;
                 margin-bottom: 5px;
                 text-align: right;
            }
            .results span {
                 width: 100%;
                 text-align: right; /* Results text RTL */
                 direction: rtl; /* Results numbers RTL */
            }
             .difference {
                 flex-direction: column;
                 align-items: flex-end;
                 text-align: right;
             }
            .difference span {
                 text-align: right;
                 direction: rtl;
            }
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>הסכנה שבדיוק: מסע אל לב שגיאות העיגול</h1>

        <p>האם הייתם מופתעים לגלות שהמחשב שלכם לא תמיד מסוגל לחשב במדויק חיבור פשוט כמו 0.1 + 0.2? בעולם הדיגיטלי, ייצוג מספרים אינו מושלם, וכל חישוב כמעט כרוך ב'עיגול' קטן. מה קורה כשהעיגולים הזעירים האלה מתחילים להצטבר שוב ושוב? בואו נגלה!</p>

        <div class="app-section">
            <h2>מעבדת הדיוק המצטבר</h2>
            <p>הגדירו ניסוי: בחרו מספר, כמה פעמים לחבר אותו לעצמו, ובאיזו רמת דיוק המחשב "מעגל" את התוצאה בכל שלב. ראו במו עיניכם כיצד טעות קטנה הופכת למשמעותית!</p>

            <div class="app-controls">
                <div>
                    <label for="numberToAdd">המספר שנחבר שוב ושוב:</label>
                    <input type="number" id="numberToAdd" value="0.1" step="any">
                </div>
                 <div>
                     <label for="repetitions">כמה פעמים לחזור על החיבור (צעדים):</label>
                     <input type="number" id="repetitions" value="100" min="1">
                 </div>
                 <div>
                     <label for="precision">דיוק החישוב בכל צעד (ספרות אחרי הנקודה):</label>
                     <input type="number" id="precision" value="1" min="0" max="15">
                 </div>
                <button id="runCalculation">בצע את הניסוי!</button>
            </div>

            <div class="results" id="calculationResults">
                <div><strong>תוצאה מדויקת (כפי שהיינו מצפים מתמטית):</strong> <span id="preciseResult">-</span></div>
                <div><strong>תוצאה כשמעגלים בכל שלב:</strong> <span id="roundedResult">-</span></div>
                <div class="difference"><strong>ההפרש המצטבר:</strong> <span id="difference">-</span></div>
            </div>

            <div class="visualization-area">
                 <h3>המחשה ויזואלית של התוצאות</h3>
                 <div class="vis-item">
                     <div class="vis-label">תוצאה מדויקת:</div>
                     <div class="vis-bar-container">
                         <div id="preciseVisBar" class="vis-bar precise"></div>
                     </div>
                 </div>
                 <div class="vis-item">
                     <div class="vis-label">תוצאה מעוגלת:</div>
                     <div class="vis-bar-container">
                         <div id="roundedVisBar" class="vis-bar rounded"></div>
                         <!-- Optional: add a difference marker -->
                         <div id="differenceVisMarker" class="vis-difference-marker"></div>
                     </div>
                 </div>
                 <p style="text-align: center; margin-top: 15px; font-size: 0.9em; color: #555;">הסרגלים ממחישים את התוצאות ביחס לתוצאה המדויקת. הפער האדום מצביע על גודל ההפרש המצטבר.</p>
             </div>

        </div>

        <div class="explanation-button-container">
            <button id="explanationButton">איך זה קורה? פענחו את התעלומה!</button>
        </div>


        <div class="explanation-section" id="explanation">
            <h2>הסבר מורחב: המדע שמאחורי הטעות</h2>

            <h3>מהן שגיאות עיגול (Rounding Errors)?</h3>
            <p>שגיאות עיגול הן הפער הבלתי נמנע בין ערך מתמטי אידיאלי של מספר לבין האופן שבו מחשב מסוגל לייצג אותו בפועל. הן נובעות מכך שלמחשבים יש כמות סופית של זיכרון לייצוג מספרים, ולכן מספרים עשרוניים מסוימים (כמו שברים אינסופיים בייצוג בינארי) חייבים "להיקצץ" או להיות מיוצגים בצורה מקורבת.</p>

            <h3>למה הן קורות בחישובים דיגיטליים?</h3>
            <ul>
                <li><strong>בסיס בינארי:</strong> מחשבים עובדים בבסיס 2 (בינארי). שברים עשרוניים שנראים פשוטים לנו בבסיס 10 (כמו 0.1 או 0.2) עשויים להיות שברים מחזוריים אינסופיים בבסיס 2 (לדוגמה, 0.1 עשרוני הוא 0.0001100110011... בינארי), ולכן חייבים לעבור "קיטום" בדיוק מסוים.</li>
                <li><strong>ייצוג נקודה צפה (Floating-Point):</strong> הדרך הסטנדרטית לייצוג מספרים ממשיים במחשבים. היא משתמשת בפורמט שמזכיר כתיב מדעי (חלק משמעותי הנקרא מנטיסה, וחזקה של 2 הנקראת אקספוננט). כמות הספרות המוקדשת למנטיסה מוגבלת, מה שמכתיב את הדיוק המקסימלי האפשרי.</li>
            </ul>

            <h3>דוגמאות פשוטות לשגיאות עיגול בודדות</h3>
            <p>רוב שפות התכנות המשתמשות בייצוג נקודה צפה סטנדרטי (כמו IEEE 754) יראו שחישוב פשוט כמו <code>0.1 + 0.2</code> אינו שווה בדיוק ל-<code>0.3</code>. במקום זאת, התוצאה תהיה קרוב מאוד, אך לא זהה (למשל, <code>0.30000000000000004</code>). זוהי שגיאת עיגול בודדת, לרוב זניחה.</p>

            <h3>כיצד שגיאות עיגול מצטברות ומתעצמות (אפקט הדומינו)</h3>
            <p>כפי שהניסוי למעלה הדגים, הבעיה הגדולה מתחילה כשמבצעים סדרת חישובים, ובמיוחד כאשר כל חישוב משתמש בתוצאה המעוגלת של החישוב הקודם (חישוב איטרטיבי). גם אם שגיאת העיגול בכל צעד היא זעירה עד כדי כך שכמעט בלתי ניכרת, חזרה עליה אלפי או מיליוני פעמים גורמת לשגיאות הזעירות הללו "להתגלגל" ולהצטבר לסכום משמעותי. הניסוי של חיבור חוזר של מספר קטן הוא דוגמה קלאסית להדגמת האפקט המצטבר.</p>

            <h3>השפעת הצטברות שגיאות על חישובים מדעיים והנדסיים</h3>
            <p>בתחומי מדע והנדסה רבים, חישובים מורכבים כוללים שרשראות ארוכות של פעולות. סימולציות פיזיקליות, חיזוי מזג אוויר, ניווט לוויינים, ניתוח נתונים - כולם תלויים בחישובים נומריים רבים. הצטברות שגיאות עיגול עלולה להוביל ל:</p>
            <ul>
                <li><strong>תוצאות שגויות:</strong> פער משמעותי בין התוצאה הנומרית שהתקבלה לערך התיאורטי הנכון.</li>
                <li><strong>אי-יציבות נומרית:</strong> מצב שבו שגיאה זעירה בקלט או בחישוב הראשוני מתעצמת בצורה בלתי נשלטת ומובילה לתוצאות חסרות משמעות לחלוטין.</li>
                <li><strong>השלכות מעשיות:</strong> החל מחיזוי שגוי ועד כשלים מערכתיים או בעיות בטיחות (למשל, בתעופה או בקרה תעשייתית).</li>
            </ul>

            <h3>דיוק לעומת יציבות נומרית - מה ההבדל?</h3>
            <p><strong>דיוק (Accuracy):</strong> מידת הקרבה של תוצאת החישוב לערך האמיתי הנכון.</p>
            <p><strong>יציבות נומרית (Numerical Stability):</strong> האם אלגוריתם החישוב רגיש לשגיאות קטנות (כולל שגיאות עיגול). אלגוריתם יציב ידאג ששגיאות קטנות לא יתעצמו בצורה פרועה. אלגוריתם לא יציב עלול לקחת שגיאה זעירה ולהפוך אותה לקטסטרופה חישובית.</p>

            <h3>דרכים להתמודד עם האתגר</h3>
            <p>מדענים ומהנדסים המבצעים חישובים נומריים משמעותיים חייבים להיות מודעים לנושא ונקוט בצעדים כדי למזער את הסיכון:</p>
            <ul>
                <li><strong>בחירת אלגוריתמים יציבים:</strong> לעיתים ישנן דרכים שונות לבצע את אותו חישוב מתמטי; יש לבחור בדרך היציבה נומרית.</li>
                <li><strong>שימוש ב"דיוק כפול" (Double Precision):</strong> ייצוג מספרים עם יותר ביטים (לרוב 64 במקום 32), המאפשר יותר ספרות משמעותיות ומפחית משמעותית שגיאות עיגול, אם כי אינו מבטל אותן לחלוטין.</li>
                <li><strong>ניתוח שגיאות:</strong> בחינה תיאורטית או ניסויית של אופן הצטברות השגיאות באלגוריתם ספציפי.</li>
                <li><strong>שימוש בספריות מיוחדות:</strong> במקרים קריטיים, ניתן להשתמש בספריות תכנות המאפשרות חישובים עם "דיוק שרירותי" (Arbitrary-Precision Arithmetic), שבו רמת הדיוק אינה קבועה אלא מותאמת לפי הצורך (על חשבון מהירות).</li>
            </ul>

            <h3>סיכום: חשיבות המודעות</h3>
            <p>שגיאות עיגול אינן בעיה שולית אלא מגבלה מהותית של חישובים דיגיטליים. הבנה עמוקה של מקורן, אופן התנהגותן, והיכולת לזהות מתי הן עלולות להפוך למשמעותיות, חיונית להבטחת אמינות תוצאות בחישובים מדעיים והנדסיים. זהו חלק בלתי נפרד מהאמנות והמדע של פתרון בעיות באמצעות מחשבים.</p>
        </div>
    </div>

    <script>
        function roundToPrecision(num, precision) {
            // Clamp precision to a reasonable range
            precision = Math.max(0, Math.min(precision, 15)); // Standard JS Number safe precision limit ~15-16

            if (precision === 0) {
                return Math.round(num);
            }

            // Use exponential notation for precision handling to avoid floating point issues with multiplication
            const roundedString = num.toFixed(precision);
            return parseFloat(roundedString);

            /* // Alternative method using Math.pow, potentially less accurate for very high precision
            const factor = Math.pow(10, precision);
            // Add a small tolerance to handle edge cases like 0.1 + 0.2 resulting in ~0.30000000000000004
            // and ensure it rounds correctly down or up. Using Number.EPSILON is standard practice.
            const rounded = Math.round((num + Number.EPSILON) * factor) / factor;
            // Handle potential -0 result
            return Object.is(rounded, -0) ? 0 : rounded;
            */
        }

        document.getElementById('runCalculation').addEventListener('click', function() {
            const numberToAddInput = document.getElementById('numberToAdd');
            const repetitionsInput = document.getElementById('repetitions');
            const precisionInput = document.getElementById('precision');

            const numberToAdd = parseFloat(numberToAddInput.value);
            const repetitions = parseInt(repetitionsInput.value, 10);
            const precision = parseInt(precisionInput.value, 10);

            // Add subtle animation/feedback to inputs on click
             [numberToAddInput, repetitionsInput, precisionInput].forEach(input => {
                 input.classList.add('input-flash');
                 setTimeout(() => input.classList.remove('input-flash'), 500);
             });


            if (isNaN(numberToAdd) || isNaN(repetitions) || isNaN(precision) || repetitions < 1 || precision < 0 || precision > 15) { // Keep max precision reasonable for JS Number
                alert('אנא הכנס ערכים תקינים.\nהמספר המצטבר: כל מספר.\nמספר הצעדים: מספר שלם וחיובי (1 ומעלה).\nדיוק החישוב: מספר שלם בין 0 ל-15.');
                return;
            }

            // Precise calculation (standard JS Number multiplication)
            const preciseResult = numberToAdd * repetitions;

            // Rounded calculation
            let roundedResult = 0;
            for (let i = 0; i < repetitions; i++) {
                roundedResult = roundedResult + numberToAdd;
                // Apply rounding at each step
                roundedResult = roundToPrecision(roundedResult, precision);
            }

            // Calculate difference
            const difference = preciseResult - roundedResult;

            // Display results
            // Determine display precision dynamically or use a fixed value that shows enough digits
            const displayPrecision = Math.max(precision + 4, 8); // Show enough digits to see small differences

            const preciseResultSpan = document.getElementById('preciseResult');
            const roundedResultSpan = document.getElementById('roundedResult');
            const differenceSpan = document.getElementById('difference');

             // Fade out old results
             const resultsDiv = document.getElementById('calculationResults');
             resultsDiv.style.opacity = 0;
             resultsDiv.style.transition = 'opacity 0.3s ease-out';

             // Update results and fade in
             setTimeout(() => {
                 preciseResultSpan.textContent = preciseResult.toFixed(displayPrecision);
                 roundedResultSpan.textContent = roundedResult.toFixed(displayPrecision);
                 differenceSpan.textContent = difference.toFixed(displayPrecision);

                 // Highlight difference if it's non-zero (within a small tolerance considering potential FP noise)
                 const differenceParentDiv = differenceSpan.parentElement;
                 if (Math.abs(difference) > Number.EPSILON * Math.abs(preciseResult) * Math.pow(repetitions, 0.5) * 100) { // Heuristic tolerance for accumulated error
                      differenceParentDiv.classList.add('difference');
                      // Maybe add a shake animation to the difference element
                      differenceParentDiv.classList.add('shake-animation');
                      setTimeout(() => differenceParentDiv.classList.remove('shake-animation'), 600); // Match animation duration
                 } else {
                      differenceParentDiv.classList.remove('difference');
                 }
                 resultsDiv.style.opacity = 1;
             }, 300); // Delay update slightly for fade effect


             // --- Update Visualization ---
             const preciseVisBar = document.getElementById('preciseVisBar');
             const roundedVisBar = document.getElementById('roundedVisBar');
             const differenceVisMarker = document.getElementById('differenceVisMarker');
             const visBarContainer = preciseVisBar.parentElement; // Get the container width reference

             // Calculate the maximum value to base the percentage width on
             // Use the larger of the two results, or the precise result as the "target" 100%
             const maxValueForVis = Math.max(Math.abs(preciseResult), Math.abs(roundedResult), Math.abs(numberToAdd * repetitions));
             const containerWidth = visBarContainer.offsetWidth; // Get actual pixel width

             // Reset bars to 0 width for animation restart
             preciseVisBar.style.width = '0';
             roundedVisBar.style.width = '0';
             differenceVisMarker.style.left = '0';
             differenceVisMarker.style.width = '0';


             // Animate bars after a short delay
             setTimeout(() => {
                 if (maxValueForVis === 0) {
                     preciseVisBar.style.width = '0%';
                     roundedVisBar.style.width = '0%';
                     differenceVisMarker.style.width = '0'; // No difference marker if results are zero
                 } else {
                     // Calculate width based on percentage of max value
                     const preciseWidth = (preciseResult / maxValueForVis) * 100;
                     const roundedWidth = (roundedResult / maxValueForVis) * 100;

                     // Cap widths at 100% of the container to avoid overflow issues in visualization
                     // If results are negative, need to handle that - let's assume positive values for simplicity in visualization bars
                     // Or handle negative values by positioning bars from right? Let's stick to positive for this visual
                     const finalPreciseWidth = Math.max(0, Math.min(100, preciseWidth));
                     const finalRoundedWidth = Math.max(0, Math.min(100, roundedWidth));

                     preciseVisBar.style.width = finalPreciseWidth + '%';
                     roundedVisBar.style.width = finalRoundedWidth + '%';

                     // Position the difference marker between the end of the rounded bar and the precise bar
                     // Or, maybe a marker showing the absolute difference magnitude scaled?
                     // Let's make the marker show the *gap* between the end points.
                     // The marker starts at the end of the rounded bar and extends to the end of the precise bar.
                     const minEnd = Math.min(finalPreciseWidth, finalRoundedWidth);
                     const maxEnd = Math.max(finalPreciseWidth, finalRoundedWidth);
                     const diffWidthPercentage = maxEnd - minEnd;

                     // Set marker position and width
                     differenceVisMarker.style.left = minEnd + '%';
                     differenceVisMarker.style.width = diffWidthPercentage + '%';
                     differenceVisMarker.style.backgroundColor = (preciseResult >= roundedResult) ? '#dc3545' : '#ffc107'; // Red if rounded is less, yellow if rounded is more
                 }
             }, 400); // Delay animation slightly after results update

        });


         document.getElementById('explanationButton').addEventListener('click', function() {
             const explanationDiv = document.getElementById('explanation');
             const isVisible = explanationDiv.classList.contains('visible');

             if (isVisible) {
                 explanationDiv.style.opacity = 0;
                 explanationDiv.addEventListener('transitionend', function handler() {
                     explanationDiv.style.display = 'none';
                     explanationDiv.classList.remove('visible');
                     this.removeEventListener('transitionend', handler);
                 });
                 this.textContent = 'איך זה קורה? פענחו את התעלומה!';
             } else {
                 explanationDiv.style.display = 'block';
                 // Use a timeout to allow display: block to take effect before starting transition
                 setTimeout(() => {
                     explanationDiv.classList.add('visible');
                     explanationDiv.style.opacity = 1;
                 }, 10); // Small delay
                 this.textContent = 'הסתירו את ההסבר';
             }
         });

         // Optional: Run calculation with default values on page load for immediate demonstration
          document.addEventListener('DOMContentLoaded', () => {
              // Add a slight delay on load to make sure everything is rendered before calculation/animation
              setTimeout(() => {
                  document.getElementById('runCalculation').click();
              }, 100);
          });

        /* Add CSS for the input flash animation */
         const styleSheet = document.styleSheets[0];
         const flashAnimation = `
             @keyframes inputFlash {
                 0% { background-color: yellow; }
                 100% { background-color: white; }
             }
         `;
         const flashRule = `.input-flash { animation: inputFlash 0.5s ease-out; }`;
         styleSheet.insertRule(flashAnimation, styleSheet.cssRules.length);
         styleSheet.insertRule(flashRule, styleSheet.cssRules.length);

         /* Add CSS for the shake animation */
         const shakeAnimation = `
             @keyframes shake {
                0%, 100% { transform: translateX(0); }
                20%, 60% { transform: translateX(-5px); }
                40%, 80% { transform: translateX(5px); }
             }
         `;
         const shakeRule = `.shake-animation { animation: shake 0.6s cubic-bezier(.36,.07,.19,.97) both; transform: translate3d(0, 0, 0); perspective: 1000px; }`;
          styleSheet.insertRule(shakeAnimation, styleSheet.cssRules.length);
          styleSheet.insertRule(shakeRule, styleSheet.cssRules.length);


    </script>
</body>
</html>