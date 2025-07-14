---
title: "ריקוד מולקולרי: סימולציית פעולת האנזים (מודל מנעול ומפתח)"
english_slug: lock-and-key-enzyme-action-simulation
category: "ביולוגיה"
tags: אנזימים, ביוכימיה, מודל מנעול ומפתח, אתר פעיל, קטאליזה ביולוגית, אינטראקטיבי
---
# ריקוד מולקולרי: סימולציית פעולת האנזים (מודל מנעול ומפתח)

איך קורה שכל כך הרבה תהליכים מדהימים בגופנו – מעיכול הסנדוויץ' שלכם עד בניית החומר התורשתי – מתרחשים במהירות וביעילות מסחררות? הכירו את גיבורי המהירות הביולוגית: האנזימים!

הסימולציה הזו תגלה לכם את אחד הסודות המרכזיים שלהם, דרך אנלוגיה קלאסית ומרתקת. בואו נצא לדרך!

<div id="enzyme-app">
    <div class="app-area enzymes-area">
        <h3>האנזימים (ה"מנעולים")</h3>
        <div class="enzyme" id="enzymeA" data-shape="square">
            <div class="active-site square-lock"></div>
            <span class="enzyme-label">אנזים ריבועי</span>
            <div class="reaction-area"></div> <!-- Area for reaction visualization -->
        </div>
        <div class="enzyme" id="enzymeB" data-shape="circle">
             <div class="active-site circle-lock"></div>
            <span class="enzyme-label">אנזים עגול</span>
            <div class="reaction-area"></div> <!-- Area for reaction visualization -->
        </div>
         <div class="enzyme placeholder">
            <h3>אזור לתגובה</h3>
             <p>גרור לכאן "סובסטרט" מתאים</p>
         </div>
    </div>

    <div class="app-area substrates-area">
        <h3>הסובסטרטים (ה"מפתחות")</h3>
        <div class="substrate" id="substrate1" draggable="true" data-shape="square" data-original-parent="substrates-area">
             <div class="key-tip square-key"></div>
             <span class="substrate-label">סובסטרט 1</span>
        </div>
         <div class="substrate" id="substrate2" draggable="true" data-shape="circle" data-original-parent="substrates-area">
             <div class="key-tip circle-key"></div>
             <span class="substrate-label">סובסטרט 2</span>
        </div>
        <div class="substrate" id="substrate3" draggable="true" data-shape="triangle" data-original-parent="substrates-area">
             <div class="key-tip triangle-key"></div>
             <span class="substrate-label">סובסטרט 3</span>
        </div>
         <div class="substrate" id="substrate4" draggable="true" data-shape="square" data-original-parent="substrates-area">
             <div class="key-tip square-key"></div>
            <span class="substrate-label">סובסטרט 4</span>
        </div>
         <div class="substrate" id="substrate5" draggable="true" data-shape="circle" data-original-parent="substrates-area">
             <div class="key-tip circle-key"></div>
             <span class="substrate-label">סובסטרט 5</span>
        </div>
    </div>

    <div class="app-area feedback-area">
        <h3>מה קורה?</h3>
        <div id="feedback">
            <p>גרור "סובסטרט" (מפתח) מאיזור המפתחות אל "אנזים" (מנעול) מתאים באזור התגובה.</p>
        </div>
         <button id="reset-button" style="display: none;">התחל מחדש</button>
    </div>
</div>

<button id="toggle-explanation">הצגת ההסבר המדעי</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מדעי: מודל מנעול ומפתח בפעולת אנזימים</h2>

    <h3>אנזימים: הזרזים של החיים</h3>
    אנזימים הם מולקולות חלבון מופלאות המשמשות כזרזים ביולוגיים (קטאליזטורים). משמעות הדבר היא שהם מסוגלים להאיץ דרמטית תגובות כימיות חיוניות בתאים חיים, פי מיליונים ואף מיליארדים, מבלי להיאכל בעצמם בתהליך. דמיינו שאתם מנסים לפרק סוכר לאבני הבניין שלו – ללא אנזימים, זה ייקח שעות או ימים. עם האנזים המתאים, זה קורה בחלקיק שנייה.

    <h3>כיצד אנזימים פועלים? ה"אתר הפעיל"</h3>
    הסוד ליעילותם של אנזימים טמון במבנה התלת-ממדי הייחודי שלהם, ובעיקר באזור ספציפי הנקרא ה'אתר הפעיל'. האתר הפעיל הוא כיס או שקע על פני האנזים, בעל צורה ומטען חשמלי מדויקים מאוד. רק מולקולות מסוימות, הנקראות 'סובסטרטים', שהמבנה שלהן משלים את צורת האתר הפעיל, יכולות להיקשר אליו.

    <h3>מודל מנעול ומפתח (Lock and Key Model)</h3>
    כדי להמחיש את הספציפיות הגבוהה הזו, הציע הכימאי הגרמני הרמן אמיל פישר בשנת 1894 את מודל 'מנעול ומפתח'. על פי מודל זה, האנזים הוא כמו מנעול בעל צורה ספציפית של האתר הפעיל, והסובסטרט הוא כמו מפתח אחד ויחיד שמתאים בדיוק לצורת המנעול הזה. רק ההתאמה המרחבית המדויקת מאפשרת קשירה והתרחשות התגובה.

    <h3>שלבי הפעולה לפי המודל:</h3>
    1.  **קשירה (Binding):** הסובסטרט (מפתח) "נכנס" לאתר הפעיל (מנעול), ונוצר קומפלקס זמני: קומפלקס אנזים-סובסטרט. זהו שלב מאוד ספציפי הדורש התאמה צורנית מושלמת.
    2.  **קטאליזה (Catalysis):** כשהסובסטרט קשור לאתר הפעיל, האנזים גורם לשינוי כימי בסובסטרט. הוא עשוי לפרק מולקולה גדולה למולקולות קטנות יותר (כמו בעיכול), או לחבר מולקולות קטנות ליצירת מולקולה גדולה (כמו בבניית DNA). האנזים עושה זאת על ידי הורדת אנרגיית ההפעלה הדרושה לתגובה.
    3.  **שחרור (Release):** לאחר שהסובסטרט עבר את התגובה והפך ל'תוצר' (או תוצרים), התוצרים משתחררים מהאתר הפעיל של האנזים.

    <h3>לאחר התגובה: מוכנים לסבב נוסף!</h3>
    נקודה קריטית היא שהאנזים **אינו משתנה** בסוף התגובה. הוא משתחרר מהתוצרים במצבו המקורי, ומוכן לקשור מולקולת סובסטרט חדשה ולזרז תגובה נוספת. מולקולת אנזים אחת יכולה לזרז אלפי ואף מיליוני תגובות בשנייה!

    <h3>מעבר למודל הפשטני: התאמה מושרית</h3>
    חשוב לציין שמודל מנעול ומפתח הוא אנלוגיה פשוטה ויעילה, אך לא תמיד משקף את המציאות המורכבת במלואה. מודל עדכני יותר, 'מודל ההתאמה המושרית' (Induced Fit Model), מציע שהאתר הפעיל אינו קשיח לחלוטין, אלא עשוי לשנות מעט את צורתו כאשר הסובסטרט נקשר אליו. שינוי זה משפר את הקשירה ומביא את הסובסטרט למצב אידיאלי לתגובה. למרות זאת, מודל מנעול ומפתח נשאר כלי מצוין להבנת עקרון הספציפיות האנזימטית.

    <p style="margin-top: 20px; font-style: italic; color: #555;">בסימולציה שלפניכם, הדגמנו את עקרון ה"מנעול ומפתח". שימו לב שרק "מפתחות" בעלי צורה תואמת יתאימו ל"מנעול" הספציפי ויגרמו ל"תגובה".</p>
</div>

<style>
    #enzyme-app {
        font-family: 'Heebo', Arial, sans-serif; /* Using Heebo for better Hebrew support if available */
        direction: rtl;
        text-align: right;
        margin-top: 20px;
        padding: 25px;
        border: none; /* Remove border */
        border-radius: 12px;
        background: linear-gradient(135deg, #e0f7fa, #c8e6c9); /* Softer gradient background */
        display: flex;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Add subtle shadow */
        justify-content: center; /* Center areas horizontally */
    }

    .app-area {
        flex: 1;
        min-width: 280px; /* Increased min-width */
        max-width: 400px; /* Added max-width */
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5); /* Softer border */
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: flex; /* Use flex for internal layout */
        flex-direction: column; /* Stack items vertically */
        align-items: center; /* Center items horizontally within area */
        text-align: center;
    }

    .enzymes-area h3, .substrates-area h3, .feedback-area h3 {
         color: #00796b; /* Teal */
         margin-top: 0;
         margin-bottom: 15px;
         font-size: 1.3em;
         border-bottom: 2px solid #00796b;
         padding-bottom: 8px;
         width: 100%; /* Make border span full width */
         text-align: center;
    }


    .enzyme, .substrate {
        border: 2px solid #555;
        padding: 12px; /* Increased padding */
        margin-bottom: 15px; /* Increased margin */
        background-color: #eee;
        border-radius: 8px; /* Rounded corners */
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative; /* Needed for positioning children */
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; /* Smooth transitions */
         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
         width: 100%; /* Full width within area */
         box-sizing: border-box;
    }

     .enzyme.placeholder {
         border: 2px dashed #00796b;
         background-color: rgba(0, 121, 107, 0.1); /* Light teal */
         min-height: 100px;
         align-items: center;
         justify-content: center;
         color: #004d40; /* Darker teal */
         font-style: italic;
         font-size: 1.1em;
         text-align: center;
         cursor: default;
          box-shadow: none; /* No shadow on placeholder */
     }
     .enzyme.placeholder p {
         margin: 5px 0 0 0;
         font-size: 0.9em;
         color: #00695c;
     }

    .enzyme {
        cursor: default;
        background-color: #a5d6a7; /* Light green */
        min-height: 90px; /* Ensure height */
        flex-direction: column; /* Stack lock and label */
        justify-content: center;
        align-items: center;
    }

    .enzyme .active-site {
         width: 40px; /* Increased size */
         height: 40px;
         margin-bottom: 8px; /* Space between shape and label */
         border: 3px solid #004d40; /* Dark teal border */
         box-sizing: border-box; /* Include border in dimensions */
         background-color: #e8f5e9; /* Very light green */
         display: flex;
         justify-content: center;
         align-items: center;
    }

    .enzyme#enzymeA .active-site.square-lock {
        border-radius: 4px; /* Slightly rounded corners for square */
    }

     .enzyme#enzymeB .active-site.circle-lock {
        border-radius: 50%;
    }

    .enzyme .enzyme-label {
        font-size: 1em;
        color: #004d40; /* Dark teal */
        font-weight: bold;
    }


    .substrate {
        cursor: grab;
        background-color: #ffab91; /* Light orange */
        width: calc(100% - 24px); /* Take full width minus padding+border */
        min-height: 55px; /* Ensure height */
        position: relative;
        z-index: 10; /* Ensure it's above other elements while dragging */
        display: flex;
        flex-direction: row-reverse; /* Text on right, key on left */
        justify-content: space-between;
        align-items: center;
         padding: 10px 15px;
         box-sizing: border-box;
    }
     .substrate:hover {
        transform: translateY(-3px); /* Lift slightly on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
     }

     .substrate .substrate-label {
         font-size: 1em;
         color: #bf360c; /* Deep orange */
         font-weight: bold;
     }


    .key-tip {
        width: 30px; /* Increased size */
        height: 30px;
        background-color: #8d6e63; /* Brown */
        border: 2px solid #4e342e; /* Darker brown border */
        box-sizing: border-box;
         display: flex;
         justify-content: center;
         align-items: center;
    }

    .square-key {
         border-radius: 4px; /* Slightly rounded corners for square */
    }

    .circle-key {
        border-radius: 50%;
    }
    .triangle-key {
         width: 0;
         height: 0;
         /* Use borders to create a triangle shape */
         border-left: 15px solid transparent; /* Half width of intended base */
         border-right: 15px solid transparent; /* Half width of intended base */
         border-bottom: 30px solid #8d6e63; /* Height and color */
         background-color: transparent; /* Ensure no background */
         border-radius: 0; /* Ensure no border-radius interference */
         /* Reset the dimensions of the key-tip container itself for the triangle */
         width: 30px; /* Container width */
         height: 30px; /* Container height */
         overflow: hidden; /* Hide the excess border */
         display: flex;
         align-items: flex-end; /* Align the tip downwards if border-bottom is used */
         justify-content: center;
         box-sizing: content-box; /* Don't include borders in container size */
         border: none; /* Remove the container border */
    }


    #feedback {
        font-size: 1.2em; /* Larger font */
        color: #333;
        min-height: 30px; /* Reserve space */
        margin-bottom: 15px;
        text-align: center;
        font-weight: bold;
        transition: color 0.3s ease-in-out; /* Smooth color change */
    }

     .feedback.success {
         color: #388e3c; /* Green for success */
     }

     .feedback.error {
         color: #d32f2f; /* Red for error */
     }


    button {
        margin-top: 20px;
        padding: 12px 20px; /* Increased padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        background-color: #0288d1; /* Light blue */
        color: white;
        border: none;
        border-radius: 6px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    button:hover {
        background-color: #0277bd; /* Darker blue on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

     #reset-button {
         background-color: #f57c00; /* Orange */
     }
      #reset-button:hover {
         background-color: #ef6c00; /* Darker orange */
      }


    #explanation {
        margin-top: 20px;
        padding: 25px; /* Increased padding */
        border: none; /* Remove border */
        border-radius: 12px;
        background-color: #fff;
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        line-height: 1.6; /* Improved readability */
    }

    #explanation h2 {
        color: #0288d1; /* Matching button blue */
        border-bottom: 2px solid #0288d1;
        padding-bottom: 8px;
        margin-bottom: 20px; /* Increased margin */
        text-align: center; /* Center heading */
    }
     #explanation h3 {
        color: #00796b; /* Teal */
        border-bottom: 1px dashed #b2dfdb; /* Lighter dashed border */
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 10px;
     }
     #explanation p {
         margin-bottom: 15px;
     }


     /* Dragging feedback */
    .dragging {
        opacity: 0.7; /* Slightly more opaque */
        transform: scale(0.95); /* Slightly shrink when dragging */
        border: 2px dashed #0288d1; /* Blue dashed border */
        box-shadow: 0 0 12px rgba(2, 136, 209, 0.6); /* Glow effect */
        cursor: grabbing;
    }

    /* Drop target feedback */
     .enzyme.drag-over {
        border-color: #388e3c; /* Green border */
        box-shadow: 0 0 15px rgba(56, 142, 60, 0.7); /* Stronger green glow */
        transform: scale(1.03); /* Slightly grow target */
     }

     /* Animations */

     /* Correct Match Animation */
     @keyframes bind-react-release {
         0% { transform: translate(0, 0) scale(1); opacity: 1; } /* Start at drop point */
         15% { transform: translate(0, -20px) scale(1.05); opacity: 0.9; } /* Move slightly up, scale */
         30% { transform: translate(0, 0) scale(0.8); opacity: 0.7; } /* Move down into enzyme, shrink a bit */
         50% { transform: scale(0.7); opacity: 0.5; } /* Mid-reaction: smaller, faded */
         70% { transform: scale(0.8); opacity: 0.7; } /* Recovering */
         100% { transform: translate(0, 0) scale(1); opacity: 0; display: none;} /* Disappear completely */
     }

     .substrate.reacting {
         animation: bind-react-release 2s ease-in-out forwards;
         pointer-events: none; /* Ignore clicks/drags during reaction */
     }

      @keyframes enzyme-pulse {
          0%, 100% { transform: scale(1); box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08); }
          50% { transform: scale(1.05); box-shadow: 0 0 10px rgba(56, 142, 60, 0.5); } /* Pulse effect */
      }
     .enzyme.reacting-enzyme {
         animation: enzyme-pulse 2s ease-in-out forwards; /* Pulse while reaction happens */
     }


     .reaction-area {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         display: flex;
         justify-content: space-around; /* Space out products */
         align-items: center;
         pointer-events: none; /* Don't block clicks on enzyme */
         z-index: 1; /* Below enzyme label/site */
     }

     .product {
         width: 20px;
         height: 20px;
         background-color: #ff9800; /* Amber/Orange */
         border-radius: 50%; /* Products are often smaller, simpler */
         position: absolute; /* Position relative to reaction-area */
         opacity: 0; /* Start invisible */
         transform: translateY(0);
         animation: product-release 2s ease-out forwards; /* Animate out */
     }
     /* Distribute products visually */
     .reaction-area .product:nth-child(1) { left: 25%; top: 40%; }
     .reaction-area .product:nth-child(2) { left: 65%; top: 40%; }


     @keyframes product-release {
         0%, 50% { opacity: 0; transform: translateY(0) scale(0.5); } /* Stay hidden/small during binding/reaction */
         60% { opacity: 1; transform: translateY(-15px) scale(1); } /* Appear and move up */
         100% { opacity: 0; transform: translateY(-40px) scale(1.2); } /* Fade out and move further up */
     }


     /* Incorrect Match Animation (Shake) */
     @keyframes shake {
         0%, 100% { transform: translateX(0); }
         10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
         20%, 40%, 60%, 80% { transform: translateX(5px); }
     }
     .enzyme.shake {
         animation: shake 0.5s ease-in-out;
         border-color: red !important; /* Override drag-over color */
     }

     /* Return animation handled by JS adding CSS transition property */

      /* Ensure elements positioned absolutely within flex containers work */
     .app-area {
         position: relative; /* Needed for absolute positioning of children */
     }

     .substrate[style*="position: absolute"] {
          /* Ensure absolute positioned substrates don't affect flex layout */
          flex-shrink: 0;
     }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const substratesArea = document.getElementById('substrates-area');
        const enzymes = document.querySelectorAll('.enzyme:not(.placeholder)'); // Target actual enzymes
        const placeholderEnzymeArea = document.querySelector('.enzyme.placeholder'); // Target the drop area placeholder
        const feedback = document.getElementById('feedback');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const resetButton = document.getElementById('reset-button');

        // Store original positions and parent for returning elements
        const originalPositions = {};
        const substrates = document.querySelectorAll('.substrate'); // Select all draggable substrates

        // --- Helper to save initial positions ---
        function saveOriginalPositions() {
             // Reset any temporary styles before measuring
             substrates.forEach(sub => {
                  sub.style.position = 'static'; // Allow element to be in normal flow
                  sub.style.margin = ''; // Clear any margins
                  sub.style.transition = 'none'; // Clear any transitions
                  sub.style.display = 'flex'; // Ensure display is correct for measurement
                  sub.style.visibility = 'visible';
                  sub.classList.remove('reacting'); // Remove reaction classes
                   if (sub.parentElement && !sub.parentElement.classList.contains('substrates-area')) {
                        // If it's not in the original area, move it back temporarily for measurement
                         substratesArea.appendChild(sub);
                   }
             });

             // Wait for reflow after resetting styles/positioning
             requestAnimationFrame(() => {
                 substrates.forEach(sub => {
                      const rect = sub.getBoundingClientRect();
                      const parentRect = sub.parentElement.getBoundingClientRect();

                      // Calculate position relative to the parent's top-left corner
                      const initialLeft = rect.left - parentRect.left;
                      const initialTop = rect.top - parentRect.top;

                      originalPositions[sub.id] = {
                          left: initialLeft,
                          top: initialTop,
                          parent: sub.parentElement.id
                      };

                      // Now, set position to absolute relative to the parent's current flow position
                      // This 'locks' it visually where it was, but makes it ready for animated moves via left/top
                      sub.style.position = 'absolute';
                      sub.style.left = initialLeft + 'px';
                      sub.style.top = initialTop + 'px';
                       sub.style.right = 'auto';
                       sub.style.bottom = 'auto';
                       sub.style.margin = '0'; // Remove margin as position is absolute
                 });
                 // Show substrates once positions are saved and set
                  substrates.forEach(sub => sub.style.visibility = 'visible');

                 // Hide placeholder area after setup
                 placeholderEnzymeArea.style.display = 'flex'; // Ensure placeholder is visible initially
             });
        }


        // --- Helper to return element to original position with animation ---
         function returnToOriginalPosition(element) {
             const originalPos = originalPositions[element.id];
             if (!originalPos) {
                  console.error("Original position data missing for element:", element.id);
                   // Fallback: just reset styles without animation
                   element.style.position = 'static';
                   element.style.margin = '';
                   element.style.transition = 'none';
                   element.style.display = 'flex';
                   element.style.visibility = 'visible';
                  return;
             }

             const parentElement = document.getElementById(originalPos.parent);
             if (!parentElement) {
                  console.error("Original parent element not found for element:", element.id, "Parent ID:", originalPos.parent);
                   // Fallback: just reset styles
                   element.style.position = 'static';
                   element.style.margin = '';
                   element.style.transition = 'none';
                   element.style.display = 'flex';
                   element.style.visibility = 'visible';
                  return;
             }

             // Ensure element is visible and styled for absolute positioning before calculating current pos
             element.style.display = 'flex';
             element.style.visibility = 'visible';
             element.style.transition = 'none'; // Remove any existing transitions
             element.style.position = 'absolute'; // Must be absolute for left/top animation
             element.style.margin = '0'; // Clear margin


             // Append to target parent first if it's not already there
             if (element.parentElement !== parentElement) {
                 // Temporarily set to static to get its flow position, then back to absolute relative to new parent
                 // This is complex. Simpler: Append, then get its *new* rect relative to the parent it was just appended to.
                 parentElement.appendChild(element);
             }

             // Get the element's *current* position relative to its *current* parent's top-left corner
             // This needs to be calculated *after* it's in the correct parent and styled absolute
             const currentRect = element.getBoundingClientRect();
             const parentRect = parentElement.getBoundingClientRect();
             const currentLeft = currentRect.left - parentRect.left;
             const currentTop = currentRect.top - parentRect.top;

             // Set the element's starting absolute position to its calculated current position
             element.style.left = currentLeft + 'px';
             element.style.top = currentTop + 'px';
             element.style.right = 'auto';
             element.style.bottom = 'auto';


             // Use requestAnimationFrame to ensure the element is painted at the 'current' position
             // before starting the transition to the 'original' position.
             requestAnimationFrame(() => {
                 // Add the transition property
                 element.style.transition = 'left 0.6s ease-in-out, top 0.6s ease-in-out'; // Slower, smoother return

                 // Set the target absolute position (which is the stored original position)
                 element.style.left = originalPos.left + 'px';
                 element.style.top = originalPos.top + 'px';
             });

             // Clean up styles after the transition ends
             element.addEventListener('transitionend', function handler() {
                 // Reset styles to return element to normal flow layout
                 element.style.position = 'absolute'; // Keep absolute for flex child consistency
                 element.style.left = originalPos.left + 'px'; // Ensure it stays at the target position
                 element.style.top = originalPos.top + 'px';
                 element.style.transition = 'none'; // Remove transition
                 // element.style.margin = ''; // Keep margin 0 since position is absolute
                 element.removeEventListener('transitionend', handler); // Clean up listener
             }, { once: true }); // Automatically remove listener after one trigger
         }


        // --- Drag and Drop Event Listeners ---
        substrates.forEach(substrate => {
            // Save initial position data right before dragging starts if not already saved?
            // Better to save all on load, as done in saveOriginalPositions.
             substrate.addEventListener('dragstart', (e) => {
                 e.dataTransfer.setData('text/plain', e.target.id);
                 e.target.classList.add('dragging');
                 // Add a delay to hide the element *after* the drag image is captured
                  requestAnimationFrame(() => {
                     e.target.style.visibility = 'hidden';
                 });
            });

             substrate.addEventListener('dragend', (e) => {
                 const substrateElement = e.target;
                 substrateElement.classList.remove('dragging');

                 // If the element is still hidden (meaning it wasn't consumed by a drop),
                 // it means it was dropped somewhere invalid or the drag was cancelled.
                 // Return it to its original position.
                 // Check its current parent vs original parent recorded on dragstart?
                 // Or just check if it's not marked for permanent removal (like display: none)
                 if (substrateElement.style.display !== 'none') {
                     // Make it visible again *before* returning animation starts
                      substrateElement.style.visibility = 'visible';
                     // The returnToOriginalPosition function handles putting it back in the right parent
                     returnToOriginalPosition(substrateElement);
                     feedback.textContent = 'הפעולה בוטלה או לא היתה התאמה. החזרת סובסטרט...';
                     feedback.classList.add('feedback', 'error');
                      // Remove error state after animation or a short delay
                      setTimeout(() => {
                           feedback.textContent = 'גרור "סובסטרט" (מפתח) אל "אנזים" מתאים.';
                           feedback.classList.remove('feedback', 'error', 'success');
                      }, 700); // Match return animation duration
                 }
             });
        });

        // Allow dropping onto the specific enzyme elements OR the placeholder area
        const dropTargets = [...enzymes, placeholderEnzymeArea];

        dropTargets.forEach(target => {
             target.addEventListener('dragover', (e) => {
                e.preventDefault(); // Necessary to allow dropping
                const targetElement = e.target.closest('.enzyme') || e.target.closest('.placeholder');
                if (targetElement) {
                    targetElement.classList.add('drag-over'); // Highlight the target area
                }
            });

            target.addEventListener('dragleave', (e) => {
                 const targetElement = e.target.closest('.enzyme') || e.target.closest('.placeholder');
                 if (targetElement) {
                    targetElement.classList.remove('drag-over'); // Remove highlight
                 }
            });


            target.addEventListener('drop', (e) => {
                e.preventDefault();
                const targetElement = e.target.closest('.enzyme') || e.target.closest('.placeholder');
                if (!targetElement) return; // Should not happen if drop only allowed on enzyme/placeholder areas
                targetElement.classList.remove('drag-over');

                const substrateId = e.dataTransfer.getData('text/plain');
                const substrateElement = document.getElementById(substrateId);

                // Prevent dropping if substrate was somehow already consumed or invalid
                if (!substrateElement || substrateElement.style.display === 'none' || substrateElement.classList.contains('reacting')) {
                     feedback.textContent = 'פעולה לא חוקית.'; // Should not happen with proper dragend handling
                     feedback.classList.add('feedback', 'error');
                      setTimeout(() => {
                           feedback.textContent = 'גרור "סובסטרט" (מפתח) אל "אנזים" מתאים.';
                           feedback.classList.remove('feedback', 'error', 'success');
                      }, 1000);
                    return;
                }

                 // Make substrate visible immediately after dropping (if it was hidden for drag image)
                 substrateElement.style.visibility = 'visible';
                  substrateElement.style.transition = 'none'; // Clear any return transition


                // Check if dropped on the placeholder area
                if (targetElement.classList.contains('placeholder')) {
                    feedback.textContent = 'גרור סובסטרט לאנזים ספציפי, לא לאזור הכללי.';
                    feedback.classList.add('feedback', 'error');
                     returnToOriginalPosition(substrateElement); // Return it if dropped here
                     setTimeout(() => {
                           feedback.textContent = 'גרור "סובסטרט" (מפתח) אל "אנזים" מתאים.';
                           feedback.classList.remove('feedback', 'error', 'success');
                      }, 700); // Match return animation duration
                    return;
                }

                // Proceed with enzyme specific drop logic
                const enzymeElement = targetElement; // Now we know it's an enzyme element
                const enzymeShape = enzymeElement.dataset.shape;
                const substrateShape = substrateElement.dataset.shape;


                if (enzymeShape === substrateShape) {
                    // Correct match! Simulate binding, reaction, release
                    feedback.textContent = 'התאמה מושלמת! מתרחש תהליך קשירה ותגובה...';
                    feedback.classList.remove('feedback', 'error');
                    feedback.classList.add('feedback', 'success');


                    // Visually move substrate to enzyme's position and start reaction animation
                    const enzymeRect = enzymeElement.getBoundingClientRect();
                    const appRect = document.getElementById('enzyme-app').getBoundingClientRect(); // Get app container rect
                     const enzymeLeftRelApp = enzymeRect.left - appRect.left;
                     const enzymeTopRelApp = enzymeRect.top - appRect.top;

                     // Calculate substrate's current position relative to app container
                     const subRect = substrateElement.getBoundingClientRect();
                     const subLeftRelApp = subRect.left - appRect.left;
                     const subTopRelApp = subRect.top - appRect.top;

                     // Calculate the offset needed to move substrate from its current absolute position
                     // to the enzyme's position, both relative to the app container.
                     // Substrate is already position: absolute relative to its original parent.
                     // We need to change its parent to the enzyme and adjust its left/top to match the enzyme's visual position.

                    // Temporarily move substrate to enzyme's parent for correct relative positioning calculation
                     const originalSubParent = substrateElement.parentElement; // Store original parent
                     enzymeElement.appendChild(substrateElement); // Move element to enzyme's div


                     // Calculate position relative to the enzyme element
                     const newSubRect = substrateElement.getBoundingClientRect(); // Get new rect after moving parent
                     const newEnzymeRect = enzymeElement.getBoundingClientRect();
                     const targetLeftInEnzyme = newEnzymeRect.width/2 - newSubRect.width/2; // Center horizontally in enzyme? Or specific site?
                     const targetTopInEnzyme = newEnzymeRect.height/2 - newSubRect.height/2; // Center vertically

                     // For lock-and-key, let's try to move it towards the active site specifically
                      const activeSite = enzymeElement.querySelector('.active-site');
                      const activeSiteRect = activeSite.getBoundingClientRect();
                      const targetLeftInEnzymeAccurate = (activeSiteRect.left - newEnzymeRect.left) + (activeSiteRect.width / 2) - (newSubRect.width / 2);
                      const targetTopInEnzymeAccurate = (activeSiteRect.top - newEnzymeRect.top) + (activeSiteRect.height / 2) - (newSubRect.height / 2);


                     // Set its absolute position relative to the *new* parent (the enzyme)
                      substrateElement.style.position = 'absolute';
                      substrateElement.style.left = targetLeftInEnzymeAccurate + 'px'; // Set its target position within enzyme
                      substrateElement.style.top = targetTopInEnzymeAccurate + 'px';
                      substrateElement.style.margin = '0';


                    // Add animation class
                    substrateElement.classList.add('reacting');
                    enzymeElement.classList.add('reacting-enzyme');


                    // Create product elements
                    const reactionArea = enzymeElement.querySelector('.reaction-area');
                    const product1 = document.createElement('div');
                    product1.classList.add('product');
                    const product2 = document.createElement('div');
                    product2.classList.add('product');
                    reactionArea.appendChild(product1);
                    reactionArea.appendChild(product2);


                    setTimeout(() => {
                        // Clean up after animation
                        substrateElement.classList.remove('reacting');
                        substrateElement.style.display = 'none'; // Hide the original substrate permanently
                        substrateElement.style.visibility = 'hidden';

                        enzymeElement.classList.remove('reacting-enzyme');
                         product1.remove();
                         product2.remove();


                        feedback.textContent = 'התוצרים שוחררו בהצלחה! האנזים חופשי לפעולה הבאה.';
                        feedback.classList.remove('feedback', 'error');
                        feedback.classList.add('feedback', 'success');

                         checkCompletion(); // Check if all substrates are consumed

                    }, 2000); // Match CSS animation duration

                } else {
                    // Incorrect match
                    feedback.textContent = 'אין התאמה! "המפתח" לא מתאים ל"מנעול" הזה. נסו שוב.';
                    feedback.classList.remove('feedback', 'success');
                    feedback.classList.add('feedback', 'error');

                     // Add shake animation to the enzyme
                     enzymeElement.classList.add('shake');

                     // Return substrate to original position with animation
                    returnToOriginalPosition(substrateElement);

                    setTimeout(() => {
                         enzymeElement.classList.remove('shake'); // Remove shake animation
                         feedback.textContent = 'גרור "סובסטרט" (מפתח) אל "אנזים" מתאים.';
                          feedback.classList.remove('feedback', 'error', 'success');
                    }, 700); // Match shake + return animation duration
                }
            });
        });

        // --- Explanation Toggle ---
        toggleExplanationButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationButton.textContent = isHidden ? 'הסתר הסבר מדעי' : 'הצגת ההסבר המדעי';
        });

        // --- Completion Check & Reset ---
         function checkCompletion() {
             const remainingSubstrates = document.querySelectorAll('.substrate[style*="display: flex"]');
             if (remainingSubstrates.length === 0) {
                 feedback.textContent = 'מדהים! כל הסובסטרטים מצאו את האנזימים שלהם. הבנתם את עקרון ההתאמה!';
                 feedback.classList.remove('feedback', 'error');
                 feedback.classList.add('feedback', 'success');
                 resetButton.style.display = 'block'; // Show reset button
             }
         }

         resetButton.addEventListener('click', () => {
             // Reset all substrates
             substrates.forEach(sub => {
                 sub.style.display = 'flex';
                 sub.style.visibility = 'visible';
                 sub.style.transition = 'none'; // Clear transitions
                 sub.classList.remove('reacting'); // Ensure no lingering classes
                 // Reset position/parent using the return function, or a specific reset function
                 // A simple reset function might be better than returning *with* animation here
                 const originalPos = originalPositions[sub.id];
                 const parentElement = document.getElementById(originalPos.parent);
                 if (parentElement) {
                      parentElement.appendChild(sub);
                       // Now reset absolute positioning to its calculated original spot
                       sub.style.position = 'absolute';
                       sub.style.left = originalPos.left + 'px';
                       sub.style.top = originalPos.top + 'px';
                        sub.style.right = 'auto';
                        sub.style.bottom = 'auto';
                       sub.style.margin = '0';
                       sub.style.transition = 'none'; // Ensure no animation on reset placement
                 } else {
                      console.error("Could not find original parent for reset:", sub.id);
                      // Fallback
                       sub.style.position = 'static';
                       sub.style.margin = '';
                       sub.style.transition = 'none';
                 }
             });

             // Reset enzyme states
             enzymes.forEach(enz => {
                 enz.classList.remove('reacting-enzyme', 'shake');
                 const reactionArea = enz.querySelector('.reaction-area');
                 if (reactionArea) reactionArea.innerHTML = ''; // Clear products
             });

             // Reset feedback
             feedback.textContent = 'גרור "סובסטרט" (מפתח) אל "אנזים" מתאים.';
             feedback.classList.remove('feedback', 'error', 'success');
             resetButton.style.display = 'none'; // Hide reset button
         });


        // --- Initialization ---
        // Save initial positions when the page loads and layout is ready
         saveOriginalPositions();

    });
</script>
---
```