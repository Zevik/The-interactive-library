---
title: "מחזור הפחמן: סימולטור גלובלי דינמי"
english_slug: dynamic-global-carbon-cycle-simulator
category: "מדעי הסביבה / כללי"
tags: [מחזור הפחמן, שינוי אקלים, גזי חממה, ביוספרה, אוקיינוסים, אינטראקטיבי]
---
# מחזור הפחמן: סימולטור גלובלי דינמי

מאיפה מגיע כל הפחמן שמקיף אותנו, ולאן הוא הולך? צללו ללב מחזור החיים של הפחמן על פני כדור הארץ. גלו כיצד הפחמן עובר בין האוקיינוסים העצומים, האטמוספרה הנושמת, והביוספרה התוססת, ומה קורה כשאנחנו, בני האדם, משנים את האיזון העדין הזה בקנה מידה חסר תקדים. התנסו בעצמכם – האם פעולות אנושיות באמת יכולות לטלטל מערכת גלובלית כה עצומה? שחקו עם הזרמים ובחנו את העתיד!

<div id="carbon-cycle-simulator">
    <div class="reservoir atmosphere" id="res-atm">
        <i class="fas fa-cloud"></i> <!-- Example icon - assumes FontAwesome is available -->
        <h2>אטמוספרה</h2>
        <div class="carbon-amount" id="atm-amount"></div>
        <div class="unit">PgC</div>
    </div>

    <div class="reservoir ocean-shallow" id="res-ocean-shallow">
         <i class="fas fa-water"></i>
        <h2>אוקיינוס (שטחי)</h2>
        <div class="carbon-amount" id="ocean-shallow-amount"></div>
        <div class="unit">PgC</div>
    </div>

     <div class="reservoir ocean-deep" id="res-ocean-deep">
         <i class="fas fa-water deep"></i>
        <h2>אוקיינוס (עמוק)</h2>
        <div class="carbon-amount" id="ocean-deep-amount"></div>
        <div class="unit">PgC</div>
    </div>

    <div class="reservoir biosphere" id="res-bio">
         <i class="fas fa-tree"></i>
        <h2>ביוספרה יבשתית</h2>
        <div class="carbon-amount" id="bio-amount"></div>
        <div class="unit">PgC</div>
    </div>

    <div class="reservoir fossil-fuels" id="res-fossil">
         <i class="fas fa-smog"></i>
        <h2>דלקים מאובנים</h2>
        <div class="carbon-amount" id="fossil-amount"></div>
        <div class="unit">PgC</div>
    </div>

    <!-- Flux Arrows (Visual Representation) -->
    <div class="flux-arrow natural atm-ocean-arrow"></div>
    <div class="flux-arrow natural ocean-atm-arrow"></div>
    <div class="flux-arrow natural atm-bio-arrow"></div>
    <div class="flux-arrow natural bio-atm-arrow"></div>
    <div class="flux-arrow natural ocean-shallow-deep-arrow"></div>
    <div class="flux-arrow natural ocean-deep-shallow-arrow"></div>
     <div class="flux-arrow human fossil-atm-arrow"></div>
      <div class="flux-arrow human bio-atm-human-arrow"></div> <!-- For land use -->


    <!-- Controls and Inputs -->
    <div class="controls">
        <h3>שליטה על זרימות אנושיות (PgC/שנה)</h3>
         <div class="human-flux-controls">
             <div class="control-group">
                 <label for="input-human-fossil">פליטות מדלקים מאובנים:</label>
                 <input type="range" id="input-human-fossil" value="10" min="0" max="20" step="0.5">
                 <span id="value-human-fossil">10</span>
             </div>
             <div class="control-group">
                 <label for="input-human-landuse">פליטות משימוש קרקע:</label>
                 <input type="range" id="input-human-landuse" value="1.5" min="0" max="5" step="0.1">
                 <span id="value-human-landuse">1.5</span>
             </div>
         </div>

        <div class="simulation-controls">
             <label for="simulation-years">שנות סימולציה:</label>
             <input type="number" id="simulation-years" value="100" min="1" step="10" style="width: 80px;">
             <button id="run-simulation" class="button-run">הפעל סימולציה</button>
             <button id="reset-simulation" class="button-reset">איפוס</button>
        </div>
    </div>

    <div class="simulation-output" id="simulation-output">
        <h3>ריכוז פחמן לאורך זמן (PgC)</h3>
        <div id="output-graph"></div>
        <div class="graph-legend">
             <span class="legend-item"><span class="legend-color atm-color"></span> אטמוספרה</span>
             <span class="legend-item"><span class="legend-color ocean-shallow-color"></span> אוקיינוס (שטחי)</span>
             <span class="legend-item"><span class="legend-color ocean-deep-color"></span> אוקיינוס (עמוק)</span>
             <span class="legend-item"><span class="legend-color bio-color"></span> ביוספרה יבשתית</span>
         </div>
    </div>
</div>

<button id="toggle-explanation">הצג/הסתר הסבר על מחזור הפחמן</button>

<div id="explanation" style="display: none;">
    <h2>הסבר: מחזור הפחמן הגלובלי</h2>

    <h3>מבוא: מהו מחזור הפחמן ולמה הוא חשוב?</h3>
    מחזור הפחמן הוא מסע בלתי פוסק של פחמן בין מרכיבי מערכת כדור הארץ: האוויר (אטמוספרה), המים (הידרוספרה), האדמה (גיאוספרה ופדוספרה) והחיים (ביוספרה). פחמן הוא מרכיב יסוד בכל אורגניזם חי וגם שחקן מפתח בוויסות האקלים העולמי, בעיקר דרך גז החממה פחמן דו-חמצני (CO2). הבנת המחזור חיונית כדי לפענח את מנגנוני האקלים של כדור הארץ ואת טביעת האצבע ההולכת וגוברת של האדם עליו.

    <h3>המאגרים העיקריים של פחמן על פני כדור הארץ</h3>
    הפחמן מאוחסן בכמויות משתנות ובזמני שהייה שונים במאגרים הבאים:
    <ul>
        <li>**אטמוספרה:** המאגר הקטן יחסית (CO2, CH4 וגזים נוספים), אך המפתח לוויסות הטמפרטורה. שינויים קטנים בו משפיעים דרמטית על אפקט החממה.</li>
        <li>**אוקיינוסים:** המאגר הפעיל הגדול ביותר, מכיל פחמן מומס (יוני ביקרבונט וקרבונט), חומר אורגני ופחמן באורגניזמים ימיים. האוקיינוס השטחי מחליף פחמן במהירות עם האוויר, בעוד שהאוקיינוס העמוק אוגר פחמן לאורך מאות ואלפי שנים.</li>
        <li>**ביוספרה יבשתית:** כוללת את כל החומר האורגני החי (צמחים ובעלי חיים) והמת (במיוחד בקרקעות ובצמחייה נבולה). יערות מהווים כיור פחמן משמעותי.</li>
        <li>**גיאוספרה (דלקים מאובנים וסלעים):** מאגר ענק של פחמן שהיה "נעול" בתוכו במשך מיליוני שנים. הסלעים (כמו אבן גיר) מהווים את המאגר הגדול ביותר, אך איטי מאוד. דלקים מאובנים (פחם, נפט, גז טבעי) הפכו למאגר משמעותי שאנחנו משחררים במהירות שיא לאטמוספרה.</li>
    </ul>

    <h3>זרימות הפחמן הטבעיות (Fluxes)</h3>
    פחמן נע בין המאגרים הללו בתהליכים טבעיים:
    <ul>
        <li>**פוטוסינתזה:** צמחים ואורגניזמים אחרים קולטים CO2 מהאטמוספרה או מהמים וממירים אותו לסוכרים וחומר אורגני בעזרת אנרגיית השמש.</li>
        <li>**נשימה:** אורגניזמים (צמחים, בעלי חיים, חיידקים) מחזירים CO2 לאטמוספרה/מים כחלק מתהליך הפקת אנרגיה.</li>
        <li>**המסה ושחרור באוקיינוס:** CO2 נמס במים השטחיים של האוקיינוס ולהפך, בתהליך שתלוי בריכוזי ה-CO2 באטמוספרה ובטמפרטורת המים.</li>
        <li>**שקיעה ועליה באוקיינוס:** פחמן מועבר מהשכבה השטחית לעמוקה (שקיעת חומר אורגני, זרמים) ומועלה חזרה בתהליך העליה (Upwelling).</li>
        <li>**תהליכים גיאולוגיים:** התפרצויות הרי געש משחררות CO2 מהגיאוספרה לאטמוספרה בקצב אטי מאוד. בליית סלעים מעבירה פחמן למערכות המים.</li>
    </ul>

    <h3>השפעת פעילות האדם על מחזור הפחמן</h3>
    האדם הפך להיות כוח גיאולוגי משמעותי, המשנה את מחזור הפחמן בקצב מסחרר:
    <ul>
        <li>**שריפת דלקים מאובנים:** השחרור המהיר ביותר והמשמעותי ביותר של פחמן ממאגר שהיה יציב במשך מיליוני שנים ישירות לאטמוספרה (בעיקר כ-CO2).</li>
        <li>**שינויים בשימושי קרקע:** כריתת יערות (בירוא יערות), שריפת צמחייה ושינויים בקרקע משחררים פחמן שאגור בביוספרה ובקרקע לאטמוספרה.</li>
        <li>**תהליכים תעשייתיים:** כמו ייצור מלט, שגם הוא פולט CO2.</li>
    </ul>

    <h3>הקשר בין מחזור הפחמן לשינוי האקלים</h3>
    CO2 הוא גז חממה מרכזי. הוא בולע קרינת חום שנפלטת מכדור הארץ ומחזיר אותה כלפי מטה, ובכך "לוכד" חום ומחמם את הפלנטה (אפקט החממה). העלייה בריכוז ה-CO2 באטמוספרה, כתוצאה מפליטות אנושיות, היא הגורם העיקרי לעלייה בטמפרטורה הגלובלית הממוצעת – תופעת שינוי האקלים שאנו חווים כיום.

    <h3>כיורים (Sinks): ספיגת פחמן עודף</h3>
    כאשר כמות הפחמן באטמוספרה עולה, המערכת הטבעית מנסה לספוג חלק מהעודף הזה דרך תהליכים כמו:
    <ul>
        <li>**ספיגת אוקיינוס:** הים בולע חלק משמעותי מה-CO2 העודף. תהליך זה ממתן את עליית ריכוז ה-CO2 באטמוספרה, אך גורם להחמצת מי ים הפוגעת במערכות ימיות רבות. יכולת הספיגה של האוקיינוס תלויה בטמפרטורה ובריכוזים.</li>
        <li>**ספיגת ביוספרה יבשתית:** גידול מוגבר של צמחים (תלוי בזמינות מים וחומרי מזון) יכול לספוג יותר CO2. עם זאת, תהליכים כמו בירוא יערות ושינויי אקלים (בצורות, שריפות) יכולים להפוך את הביוספרה ממסייעת לפולטת פחמן.</li>
    </ul>
    כיום, האוקיינוסים והביוספרה סופגים יחד כשמחצית מהפליטות האנושיות, אך החצי השני נשאר באטמוספרה וממשיך להצטבר, ומשנה את הרכב האוויר בקצב חסר תקדים במיליוני השנים האחרונות.

    <h3>הסימולטור ככלי ללמידה</h3>
    הסימולטור מאפשר לכם לשחק עם זרימות הפחמן המרכזיות, במיוחד אלה שהאדם משפיע עליהן, ולראות כיצד שינויים קטנים בקצבי הזרימה יכולים להשפיע באופן דרמטי על גודל המאגרים לאורך זמן, ובעיקר על כמות הפחמן באטמוספרה – המנוע המרכזי של שינוי האקלים.

</div>

<style>
     /* Import a clean web font */
     @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');
      /* Import Font Awesome for icons (example) */
     @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');


    #carbon-cycle-simulator {
        position: relative;
        width: 100%;
        max-width: 900px; /* Increased max-width */
        margin: 40px auto; /* More space */
        border: 1px solid #e0e0e0; /* Softer border */
        padding: 30px; /* More padding */
        font-family: 'Heebo', sans-serif; /* Use imported font */
        direction: rtl;
        text-align: right;
        min-height: 700px; /* Ensure enough space */
        background-color: #f8f8f8; /* Light background */
        border-radius: 8px; /* Rounded corners */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Subtle shadow */
        overflow: hidden; /* Keep everything inside */
    }

    .reservoir {
        border: none; /* Remove border */
        padding: 15px 10px; /* Adjust padding */
        margin: 10px;
        text-align: center;
        position: absolute;
        width: 140px; /* Slightly wider */
        box-sizing: border-box;
        background-color: #fff; /* White background */
        border-radius: 8px; /* Rounded corners */
        box-shadow: 0 2px 6px rgba(0,0,0,0.1); /* Subtle shadow */
        transition: transform 0.3s ease-in-out; /* Add hover effect */
         display: flex; /* Flexbox for centering content */
         flex-direction: column;
         align-items: center;
         justify-content: center;
    }

     .reservoir:hover {
         transform: translateY(-5px); /* Lift on hover */
     }

     .reservoir i { /* Style for icons */
         font-size: 2em;
         margin-bottom: 8px;
         color: rgba(0,0,0,0.6); /* Default icon color */
     }

     .atmosphere i { color: #0277bd; }
     .ocean-shallow i { color: #0288d1; }
      .ocean-deep i { color: #039be5; }
     .biosphere i { color: #388e3c; }
     .fossil-fuels i { color: #6d4c41; }


    .atmosphere { top: 40px; left: 50%; transform: translateX(-50%); background-color: #e1f5fe; /* Light blue */ border-top: 4px solid #0277bd;}
    .ocean-shallow { top: 220px; left: 80px; background-color: #b3e5fc; /* Lighter blue */ border-top: 4px solid #0288d1;}
    .ocean-deep { top: 450px; left: 80px; background-color: #81d4fa; /* Blue */ border-top: 4px solid #039be5;}
    .biosphere { top: 220px; right: 80px; background-color: #c8e6c9; /* Light green */ border-top: 4px solid #388e3c;}
    .fossil-fuels { top: 450px; right: 80px; background-color: #d7ccc8; /* Light brown */ border-top: 4px solid #6d4c41;}


    .reservoir h2 {
        font-size: 1.1em;
        margin: 0 0 5px 0;
        color: #333;
         font-weight: normal;
    }

    .carbon-amount {
        font-size: 1.5em; /* Larger amount */
        font-weight: 700; /* Bolder */
        color: #000;
        margin-bottom: 3px;
    }

    .unit {
        font-size: 0.9em; /* Slightly larger unit */
        color: #555;
         font-weight: 300;
    }

     /* Flux Arrows - Styling */
     .flux-arrow {
         position: absolute;
         width: 40px; /* Base width */
         height: 4px; /* Base thickness */
         background-color: #666; /* Default grey */
         z-index: 1; /* Above reservoirs */
         pointer-events: none; /* Don't block clicks */
         transform-origin: 0 50%; /* Rotate around start */
     }

      .flux-arrow::after {
          content: '';
          position: absolute;
          width: 0;
          height: 0;
          border-style: solid;
          border-width: 6px 0 6px 10px; /* Arrowhead size and shape */
          border-color: transparent transparent transparent #666; /* Arrowhead color */
          right: -10px; /* Position at the end */
          top: 50%;
          transform: translateY(-50%); /* Center vertically */
      }

      /* Natural Flux Arrow Colors */
      .flux-arrow.natural { background-color: #5cb85c; } /* Green for natural fluxes */
       .flux-arrow.natural::after { border-color: transparent transparent transparent #5cb85c; }

       /* Human Flux Arrow Colors */
      .flux-arrow.human { background-color: #d9534f; } /* Red for human fluxes */
       .flux-arrow.human::after { border-color: transparent transparent transparent #d9534f; }


     /* Positioning Flux Arrows - Need careful placement */
     /* Example - requires precise calculation based on reservoir positions */
     /* This is a placeholder, actual values need adjustment */
     .atm-ocean-arrow { top: 190px; left: 220px; width: 100px; transform: rotate(90deg); } /* Placeholder - needs fine-tuning */
     .ocean-atm-arrow { top: 190px; left: 180px; width: 100px; transform: rotate(90deg); } /* Placeholder - needs fine-tuning */

     .atm-bio-arrow { top: 190px; right: 220px; width: 100px; transform: rotate(-90deg); transform-origin: 100% 50%; } /* Placeholder */
     .bio-atm-arrow { top: 190px; right: 180px; width: 100px; transform: rotate(-90deg); transform-origin: 100% 50%; } /* Placeholder */

     .ocean-shallow-deep-arrow { top: 360px; left: 150px; width: 50px; transform: rotate(90deg); } /* Placeholder */
      .ocean-deep-shallow-arrow { top: 390px; left: 150px; width: 50px; transform: rotate(90deg); } /* Placeholder */

      .fossil-atm-arrow { bottom: 180px; right: 200px; width: 200px; transform: rotate(-45deg); transform-origin: 100% 50%; } /* Placeholder */
      .bio-atm-human-arrow { top: 360px; right: 200px; width: 100px; transform: rotate(-90deg); transform-origin: 100% 50%; } /* Placeholder */


    .controls {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        padding: 20px; /* Increased padding */
        border-top: 1px solid #eee;
        width: calc(100% - 60px); /* Use calc for dynamic width */
        background-color: #fff; /* White background */
        border-radius: 8px;
        box-shadow: 0 -2px 6px rgba(0,0,0,0.05);
         display: flex;
         flex-direction: column;
         align-items: center;
    }

     .controls h3 {
         margin-top: 0;
         margin-bottom: 15px;
         color: #333;
         font-size: 1.2em;
     }

     .human-flux-controls {
         display: flex;
         justify-content: center;
         gap: 30px; /* Space between control groups */
         margin-bottom: 20px;
         flex-wrap: wrap; /* Allow wrapping on smaller screens */
     }

     .control-group {
         display: flex;
         align-items: center;
         background-color: #f0f0f0;
         padding: 10px 15px;
         border-radius: 5px;
     }

    .controls label {
        margin-right: 10px; /* More space */
        font-size: 1em;
        color: #555;
    }

    .controls input[type="number"] {
        width: 80px;
        padding: 8px; /* Increased padding */
        margin: 0 10px;
        text-align: center;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1em;
    }
     .controls input[type="range"] {
         margin: 0 10px;
          width: 120px; /* Adjust slider width */
     }
     .control-group span {
         font-weight: bold;
         color: #000;
         width: 40px; /* Fixed width for value display */
         text-align: left;
     }


     .simulation-controls {
         display: flex;
         align-items: center;
         justify-content: center;
         flex-wrap: wrap;
     }

     .controls button {
         padding: 10px 20px; /* Increased padding */
         margin: 0 8px; /* Adjust margin */
         color: white;
         border: none;
         border-radius: 4px;
         cursor: pointer;
         font-size: 1em;
         transition: background-color 0.3s ease;
     }
      .button-run {
          background-color: #4CAF50; /* Green */
      }
       .button-run:hover {
           background-color: #45a049;
       }
       .button-reset {
            background-color: #f44336; /* Red */
       }
       .button-reset:hover {
           background-color: #da190b;
       }


    .simulation-output {
        position: absolute;
        top: 50px; /* Below atmosphere reservoir */
        left: 50%;
        transform: translateX(-50%);
        width: 90%; /* Wider output */
        max-height: 400px; /* Increased height */
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #eee;
        text-align: center;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
         padding: 20px;
         box-sizing: border-box;
         display: none; /* Hide initially */
    }

     #output-graph {
         width: calc(100% - 20px); /* Allow space for Y axis labels */
         height: 250px; /* Increased graph height */
         border: 1px solid #ccc;
         margin: 10px auto; /* Center graph */
         position: relative;
         background-color: #fff;
         overflow: hidden;
         border-radius: 4px;
         box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
     }

      /* Graph Line Styling (JS adds color) */
     .graph-line {
        position: absolute;
        height: 2px; /* Thicker line */
        background-color: currentColor;
        transform-origin: left center;
        transition: stroke 0.3s ease; /* Smooth color changes if implemented */
     }

     /* Graph Legend */
     .graph-legend {
         margin-top: 15px;
         text-align: center;
         font-size: 0.9em;
         color: #555;
     }
     .legend-item {
         display: inline-block;
         margin: 0 15px;
     }
     .legend-color {
         display: inline-block;
         width: 15px;
         height: 10px;
         margin-left: 5px;
         vertical-align: middle;
         border-radius: 2px;
     }
     .atm-color { background-color: #0277bd; }
     .ocean-shallow-color { background-color: #0288d1; }
     .ocean-deep-color { background-color: #039be5; }
     .bio-color { background-color: #388e3c; }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        padding: 12px 25px; /* Larger button */
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-family: 'Heebo', sans-serif;
    }
    #toggle-explanation:hover {
        background-color: #0056b3;
         transform: translateY(-2px);
    }
     #toggle-explanation:active {
         transform: translateY(0);
     }


    #explanation {
        margin: 20px auto;
        max-width: 900px;
        padding: 25px; /* More padding */
        border: 1px solid #ddd;
        background-color: #fff; /* White background */
        border-radius: 8px;
        direction: rtl;
        text-align: right;
        line-height: 1.7; /* More spacious text */
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
         font-family: 'Heebo', sans-serif;
         color: #333;
    }
    #explanation h2, #explanation h3 {
        color: #0056b3; /* Blue headings */
        border-bottom: 1px solid #eee;
        padding-bottom: 8px;
        margin-top: 25px;
         margin-bottom: 15px;
         font-weight: 700;
    }
     #explanation h3 {
         font-size: 1.2em;
         font-weight: 400;
          color: #007bff;
     }
    #explanation ul {
        list-style-type: disc;
        margin-right: 25px; /* Adjust margin */
        padding-right: 0;
    }
     #explanation li {
         margin-bottom: 12px; /* More space between items */
     }
     #explanation li strong {
         color: #555; /* Slightly darker for emphasis */
     }

     /* Add simple responsiveness - basic example */
     @media (max-width: 768px) {
          #carbon-cycle-simulator {
              padding: 15px;
              min-height: 800px; /* May need more height on small screens */
          }
         .reservoir {
             width: 100px; /* Smaller reservoirs */
             padding: 10px 5px;
              font-size: 0.9em;
         }
          .atmosphere { top: 20px; }
          .ocean-shallow { top: 150px; left: 20px; }
          .biosphere { top: 150px; right: 20px; }
          .ocean-deep { top: 350px; left: 20px; }
          .fossil-fuels { top: 350px; right: 20px; }

           /* Adjust arrow positions - requires recalculation */
           /* Example: */
           .atm-ocean-arrow { left: 150px; width: 50px; }
            .ocean-atm-arrow { left: 120px; width: 50px; }
             /* etc. for all arrows */

         .controls {
             bottom: 10px;
             padding: 10px;
             width: calc(100% - 30px);
              flex-direction: column; /* Stack controls vertically */
         }
          .human-flux-controls {
               flex-direction: column;
               gap: 15px;
          }
          .control-group {
              flex-direction: column;
              align-items: flex-start;
              width: 100%; /* Full width */
          }
           .control-group label { margin-right: 0; margin-bottom: 5px; }
           .control-group input[type="range"] { width: 80%; }

          .simulation-controls {
              flex-direction: column;
              gap: 10px;
          }
           .simulation-controls label { margin-bottom: 5px; }
           .controls button { margin: 5px 0; width: 100%; }


         .simulation-output {
             top: 500px; /* Position below reservoirs */
             position: relative; /* Change positioning */
             left: auto; transform: none;
             width: 100%; /* Full width */
             margin-top: 30px;
             padding: 10px;
         }
          #output-graph {
              height: 200px;
               width: calc(100% - 10px);
          }
          .graph-legend {
              margin-top: 10px;
               font-size: 0.8em;
          }
           .legend-item { margin: 0 5px; }
     }

      /* Adjust specific arrow positioning based on new reservoir positions */
     /* Note: Accurate dynamic arrow drawing based on element positions would require complex JS.
              Manual absolute positioning in CSS based on media queries is simpler but less flexible.
              I will add basic positions for the main layout and suggest dynamic positioning is an advanced feature.
              The placeholders above need manual calculation relative to their start/end reservoirs.
              For this improved version, I'll position them visually for the standard view.
              For the mobile view, the reservoir positions change significantly, making simple CSS positioning hard.
              I'll remove the mobile positioning adjustments for arrows as it's too complex to guess accurately
              without a visual editor and will rely on the main layout positioning which might break
              on smaller screens for arrows. The focus is on the simulation and core design.
              Let's refine main layout arrow positions. */

        /* Refined Arrow Positions (Manual adjustment based on visual guess) */
        .atm-ocean-arrow { top: 250px; left: 180px; width: 70px; transform: rotate(70deg); }
        .ocean-atm-arrow { top: 240px; left: 150px; width: 70px; transform: rotate(70deg); }

        .atm-bio-arrow { top: 250px; right: 180px; width: 70px; transform: rotate(-70deg); transform-origin: 100% 50%; }
        .bio-atm-arrow { top: 240px; right: 150px; width: 70px; transform: rotate(-70deg); transform-origin: 100% 50%; }

        .ocean-shallow-deep-arrow { top: 390px; left: 150px; width: 50px; transform: rotate(90deg); }
         .ocean-deep-shallow-arrow { top: 420px; left: 150px; width: 50px; transform: rotate(90deg); }

         .fossil-atm-arrow { top: 480px; right: 220px; width: 250px; transform: rotate(-30deg); transform-origin: 100% 50%; }
         .bio-atm-human-arrow { top: 380px; right: 150px; width: 50px; transform: rotate(90deg); transform-origin: 100% 50%; }


</style>

<script>
     // Use a global object for simulation parameters and state
     const simState = {
        // Initial reservoir amounts (PgC) - These will be reset values
        initialReservoirs: {
            atm: 850,
            ocean_shallow: 900,
            ocean_deep: 37100,
            bio: 2500,
            fossil: 10000
        },
        // Current reservoir amounts
        currentReservoirs: {},
        // Natural flux rate constants (derived from initial approximate steady state)
        // Flux = k * Source_Amount
        naturalFluxRates: {
             k_atm_ocean: 80 / 850, // Initial atm_to_ocean flux / initial atm amount
             k_ocean_atm: 78 / 900, // Initial ocean_to_atm flux / initial ocean_shallow amount
             k_atm_bio: 120 / 850, // Initial atm_to_bio flux / initial atm amount
             k_bio_atm: 118 / 2500, // Initial bio_to_atm flux / initial bio amount
             // Ocean internal fluxes - keeping simpler, could be proportional to depth/temp etc.
             // Let's keep these fixed for this version based on initial values
             ocean_shallow_to_deep_fixed: 90,
             ocean_deep_to_shallow_fixed: 85
        },
        // Human flux inputs (PgC/year) - Read from sliders
        humanFluxInputs: {
             fossil_to_atm: 0, // Will be read from input
             landuse_to_atm: 0 // Will be read from input
        },
        // Simulation parameters
        yearsToSimulate: 100, // Will be read from input number
        // History for graphing
        history: {
             atm: [],
             ocean_shallow: [],
             ocean_deep: [],
             bio: []
        }
     };


    // --- DOM Elements ---
    const reservoirElements = {
        atm: document.getElementById('atm-amount'),
        ocean_shallow: document.getElementById('ocean-shallow-amount'),
        ocean_deep: document.getElementById('ocean-deep-amount'),
        bio: document.getElementById('bio-amount'),
        fossil: document.getElementById('fossil-amount')
    };

    const humanFluxInputs = {
         fossil_to_atm: document.getElementById('input-human-fossil'),
         landuse_to_atm: document.getElementById('input-human-landuse')
    };
     const humanFluxValueDisplays = {
         fossil_to_atm: document.getElementById('value-human-fossil'),
         landuse_to_atm: document.getElementById('value-human-landuse')
     }

    const simYearsInput = document.getElementById('simulation-years');
    const runButton = document.getElementById('run-simulation');
    const resetButton = document.getElementById('reset-simulation');
    const outputDiv = document.getElementById('simulation-output');
    const graphDiv = document.getElementById('output-graph');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');

    // --- Functions ---

    function updateDisplay() {
        for (const key in reservoirElements) {
            if (simState.currentReservoirs[key] !== undefined) {
                reservoirElements[key].textContent = simState.currentReservoirs[key].toFixed(0); // Display rounded values
            }
        }
    }

    function readHumanFluxInputs() {
         simState.humanFluxInputs.fossil_to_atm = parseFloat(humanFluxInputs.fossil_to_atm.value);
         simState.humanFluxInputs.landuse_to_atm = parseFloat(humanFluxInputs.landuse_to_atm.value);
         simState.yearsToSimulate = parseInt(simYearsInput.value);

         // Update display values for sliders
         humanFluxValueDisplays.fossil_to_atm.textContent = simState.humanFluxInputs.fossil_to_atm.toFixed(1);
         humanFluxValueDisplays.landuse_to_atm.textContent = simState.humanFluxInputs.landuse_to_atm.toFixed(1);
    }


    function runSimulation() {
        readHumanFluxInputs(); // Get current input values

        if (isNaN(simState.yearsToSimulate) || simState.yearsToSimulate <= 0) {
            alert("אנא הכנס מספר חוקי של שנים לסימולציה.");
            return;
        }

        // Initialize current state from initial state for a fresh run
         // Deep copy initial state
        simState.currentReservoirs = JSON.parse(JSON.stringify(simState.initialReservoirs));


        // Clear previous history and add initial state
        simState.history = { atm: [], ocean_shallow: [], ocean_deep: [], bio: [] };
        for(const resKey in simState.history) {
            simState.history[resKey].push(simState.currentReservoirs[resKey]);
        }

        // Show output area
        outputDiv.style.display = 'block';
        graphDiv.innerHTML = ''; // Clear previous graph

        // Time step simulation (e.g., annual step)
        // Using a simple Euler method with annual steps
        for (let i = 0; i < simState.yearsToSimulate; i++) {

            // Calculate natural fluxes based on current reservoir amounts
            const flux_atm_to_ocean = simState.naturalFluxRates.k_atm_ocean * simState.currentReservoirs.atm;
            const flux_ocean_to_atm = simState.naturalFluxRates.k_ocean_atm * simState.currentReservoirs.ocean_shallow;
            const flux_atm_to_bio = simState.naturalFluxRates.k_ab * simState.currentReservoirs.atm;
            const flux_bio_to_atm = simState.naturalFluxRates.k_ba * simState.currentReservoirs.bio;
            const flux_ocean_shallow_to_deep = simState.naturalFluxRates.ocean_shallow_to_deep_fixed; // Fixed rate for simplicity
            const flux_ocean_deep_to_shallow = simState.naturalFluxRates.ocean_deep_to_shallow_fixed; // Fixed rate for simplicity

            // Get human fluxes from inputs
            const flux_human_fossil_to_atm = simState.humanFluxInputs.fossil_to_atm;
            const flux_human_landuse_to_atm = simState.humanFluxInputs.landuse_to_atm;

            // Calculate net change for each reservoir (delta)
            const deltaAtm = (flux_ocean_to_atm + flux_bio_to_atm + flux_human_fossil_to_atm + flux_human_landuse_to_atm) - (flux_atm_to_ocean + flux_atm_to_bio);
            const deltaOceanShallow = (flux_atm_to_ocean + flux_ocean_deep_to_shallow) - (flux_ocean_to_atm + flux_ocean_shallow_to_deep);
            const deltaOceanDeep = flux_ocean_shallow_to_deep - flux_ocean_deep_to_shallow;
            const deltaBio = flux_atm_to_bio - (flux_bio_to_atm + flux_human_landuse_to_atm); // Human land use removes from bio reservoir
            const deltaFossil = -flux_human_fossil_to_atm; // Fossil fuels only decrease from human use

            // Update reservoirs for the next step
            simState.currentReservoirs.atm += deltaAtm;
            simState.currentReservoirs.ocean_shallow += deltaOceanShallow;
            simState.currentReservoirs.ocean_deep += deltaOceanDeep;
            simState.currentReservoirs.bio += deltaBio;
            simState.currentReservoirs.fossil += deltaFossil; // Fossil fuels decrease

            // Prevent negative amounts (simplified)
            for (const key in simState.currentReservoirs) {
                 if (simState.currentReservoirs[key] < 0) simState.currentReservoirs[key] = 0;
            }

            // Store history for graph (after update)
             for(const resKey in simState.history) {
                simState.history[resKey].push(simState.currentReservoirs[resKey]);
            }
        }

        // Update display with final amounts
        updateDisplay();

        // Draw simple graph
        drawGraph();
    }

    function drawGraph() {
         const graphWidth = graphDiv.clientWidth;
         const graphHeight = graphDiv.clientHeight;
         const padding = 30; // Padding for axes labels

         // Find max value for scaling (excluding fossil fuels)
         let maxY = 0;
         for(const resKey in simState.history) {
             const maxRes = Math.max(...simState.history[resKey]);
             if (maxRes > maxY) maxY = maxRes;
         }
         // Add a small buffer to maxY
         maxY = maxY * 1.1;
         if (maxY === 0) maxY = 1000; // Default if all values are 0 (unlikely but safe)


         const numYears = simState.history.atm.length - 1; // Number of steps = years

         // Draw lines
         const reservoirKeys = ['atm', 'ocean_shallow', 'ocean_deep', 'bio']; // Order for legend/colors
         const colors = {
             atm: '#0277bd',
             ocean_shallow: '#0288d1',
             ocean_deep: '#039be5',
             bio: '#388e3c'
         };


         reservoirKeys.forEach(resKey => {
             const data = simState.history[resKey];
             if (data.length < 2) return;

             for(let i = 0; i < data.length - 1; i++) {
                 const x1 = padding + (i / numYears) * (graphWidth - 2 * padding);
                 const y1 = graphHeight - padding - (data[i] / maxY) * (graphHeight - 2 * padding);
                 const x2 = padding + ((i + 1) / numYears) * (graphWidth - 2 * padding);
                 const y2 = graphHeight - padding - (data[i+1] / maxY) * (graphHeight - 2 * padding);

                 const line = document.createElement('div');
                 line.classList.add('graph-line');
                 line.style.backgroundColor = colors[resKey]; // Use color map

                  // Calculate distance and angle for the line segment
                  const distance = Math.sqrt((x2 - x1)**2 + (y2 - y1)**2);
                  const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;

                 line.style.width = distance + 'px';
                 line.style.left = x1 + 'px';
                 line.style.top = y1 + 'px';
                 line.style.transform = `rotate(${angle}deg)`;
                 graphDiv.appendChild(line);
             }
         });


         // Add Y-axis labels
          for(let i = 0; i <= 4; i++) {
              const value = (maxY / 4) * i;
              const yPos = graphHeight - padding - (value / maxY) * (graphHeight - 2 * padding);
              const label = document.createElement('div');
              label.style.position = 'absolute';
              label.style.right = '5px'; /* Position on the right for RTL */
              label.style.top = (yPos) + 'px';
              label.style.fontSize = '0.8em';
              label.style.color = '#555';
              label.style.transform = 'translateY(-50%)'; // Center vertically
              label.style.textAlign = 'left';
               label.textContent = value.toFixed(0);
               graphDiv.appendChild(label);
          }

           // Add X-axis label
           const xlabel = document.createElement('div');
           xlabel.style.position = 'absolute';
           xlabel.style.left = '50%';
           xlabel.style.bottom = '5px';
           xlabel.style.fontSize = '0.8em';
           xlabel.style.color = '#555';
           xlabel.style.transform = 'translateX(-50%)';
           xlabel.textContent = 'שנים';
           graphDiv.appendChild(xlabel);

            // Add Y-axis title
            const ylabel = document.createElement('div');
            ylabel.style.position = 'absolute';
            ylabel.style.top = '50%';
            ylabel.style.right = '0px'; /* Position on the right for RTL */
            ylabel.style.fontSize = '0.9em';
            ylabel.style.color = '#555';
            ylabel.style.transform = 'translateY(-50%) rotate(-90deg)';
             ylabel.style.transformOrigin = 'right center';
            ylabel.textContent = 'כמות פחמן (PgC)';
            graphDiv.appendChild(ylabel);

    }


     function resetSimulation() {
         // Restore initial reservoir values
         simState.currentReservoirs = JSON.parse(JSON.stringify(simState.initialReservoirs));

          // Reset human flux inputs to their default values (matching initial HTML values)
         humanFluxInputs.fossil_to_atm.value = "10";
         humanFluxInputs.landuse_to_atm.value = "1.5";
         simYearsInput.value = "100";

         // Update human flux value displays
         humanFluxValueDisplays.fossil_to_atm.textContent = "10.0";
         humanFluxValueDisplays.landuse_to_atm.textContent = "1.5";


         updateDisplay(); // Update display with reset values
         graphDiv.innerHTML = ''; // Clear graph
         outputDiv.style.display = 'none'; // Hide output
     }

     function toggleExplanation() {
         if (explanationDiv.style.display === 'none') {
             explanationDiv.style.display = 'block';
             toggleExplanationButton.textContent = 'הסתר הסבר על מחזור הפחמן';
         } else {
             explanationDiv.style.display = 'none';
             toggleExplanationButton.textContent = 'הצג/הסתר הסבר על מחזור הפחמן';
         }
     }

     // Function to update slider value display
     function updateSliderValueDisplay(event) {
         const inputElement = event.target;
         const displayElementId = inputElement.id.replace('input-', 'value-');
         const displayElement = document.getElementById(displayElementId);
         if (displayElement) {
             displayElement.textContent = parseFloat(inputElement.value).toFixed(1); // Format to 1 decimal place
         }
     }


    // --- Event Listeners ---
    runButton.addEventListener('click', runSimulation);
    resetButton.addEventListener('click', resetSimulation);
    toggleExplanationButton.addEventListener('click', toggleExplanation);

    // Add event listeners for slider input to update value display
     humanFluxInputs.fossil_to_atm.addEventListener('input', updateSliderValueDisplay);
     humanFluxInputs.landuse_to_atm.addEventListener('input', updateSliderValueDisplay);


    // --- Initial setup ---
    function initialize() {
         // Copy initial reservoir values to current state on load
         simState.currentReservoirs = JSON.parse(JSON.stringify(simState.initialReservoirs));
         updateDisplay(); // Display initial values

          // Ensure initial slider values are displayed correctly
         humanFluxValueDisplays.fossil_to_atm.textContent = parseFloat(humanFluxInputs.fossil_to_atm.value).toFixed(1);
         humanFluxValueDisplays.landuse_to_atm.textContent = parseFloat(humanFluxInputs.landuse_to_atm.value).toFixed(1);

    }

    // Run initialization when the script loads
    initialize();

</script>