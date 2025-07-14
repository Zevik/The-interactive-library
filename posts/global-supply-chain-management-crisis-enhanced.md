---
title: "שרשרת האספקה הגלובלית שלך תחת מתקפה"
english_slug: global-supply-chain-management-crisis-enhanced
category: "ניהול ועסקים / ניהול"
tags: ניהול שרשרת אספקה, לוגיסטיקה, משבר גלובלי, סיכון, חוסן, סימולציה, למידה חווייתית
---
<h1>שרשרת האספקה הגלובלית שלך תחת מתקפה</h1>
<p class="intro-text">דמיין: מכולה אחת תקועה בנמל רחוק, מפעל נדבק בנגיף בלתי צפוי, ופתאום, כאוס. מוצרים הכי בסיסיים נעלמים מהמדפים ברחבי העולם. איך אירוע בודד בקצה העולם מצליח לשתק שרשרת אספקה גלובלית שלמה? והכי חשוב - האם אתה מוכן להתמודד? היכנס לנעליו של מנהל שרשרת אספקה בזמן משבר עולמי ובנה את אסטרטגיית החוסן שלך.</p>

<div class="app-container">
    <h2>סימולציית משבר בשרשרת האספקה</h2>
    <p>אתה מנהל את שרשרת האספקה המורכבת של 'גלובל טק', חברה מובילה למוצרי אלקטרוניקה, הפרוסה על פני יבשות.</p>

    <div class="map-area">
        <div class="location supplier" id="supplier1">
             <span class="location-name">ספק A</span>
             <span class="location-desc">(אסיה)</span>
             <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
        <div class="arrow right" data-route="supplier1-factory1">➔</div>
        <div class="location factory" id="factory1">
            <span class="location-name">מפעל ראשי</span>
            <span class="location-desc">(אירופה)</span>
            <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
        <div class="arrow right" data-route="factory1-distribution1">➔</div>
        <div class="location distribution" id="distribution1">
            <span class="location-name">מרכז הפצה</span>
            <span class="location-desc">(צ. אמריקה)</span>
            <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
        <div class="arrow right" data-route="distribution1-market1">➔</div>
        <div class="location market" id="market1">
             <span class="location-name">השוק</span>
             <span class="location-desc">(עולם)</span>
              <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>

        <!-- Alternate Routes -->
        <div class="location supplier alt" id="supplier2">
            <span class="location-name">ספק B</span>
            <span class="location-desc">(אפריקה)</span>
            <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
        <div class="arrow alt-route" id="alt-supplier-arrow">↖</div>

         <div class="location factory alt" id="factory2">
            <span class="location-name">מפעל חלופי</span>
            <span class="location-desc">(אסיה)</span>
            <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
         <div class="arrow alt-route" id="alt-factory-arrow">↖</div>

         <div class="location distribution alt" id="distribution2">
            <span class="location-name">מרכז הפצה חלופי</span>
            <span class="location-desc">(אסיה)</span>
            <div class="status-indicator"></div>
             <div class="flow-indicator"></div>
        </div>
         <div class="arrow alt-route" id="alt-distribution-arrow">↖</div>

    </div>

    <div class="status-area">
        <h3>סטטוס נוכחי</h3>
        <p>עלות שבועית: <span id="cost">$10,000</span> <span class="status-change" id="cost-change"></span></p>
        <p>זמן אספקה כולל: <span id="leadTime">4 שבועות</span> <span class="status-change" id="leadTime-change"></span></p>
        <p>רמת מלאי (במרכז הפצה): <span id="inventory">200 יחידות</span> <span class="status-change" id="inventory-change"></span></p>
        <p>שביעות רצון לקוחות: <span id="satisfaction">100%</span> <span class="status-change" id="satisfaction-change"></span></p>
        <p>שבוע נוכחי: <span id="week">1</span></p>
    </div>

    <div class="events-area">
        <h3>יומן אירועים והחלטות</h3>
        <div class="event-log" id="eventLog">
             <p>התחל שבוע כדי לראות מה יקרה...</p>
        </div>
        <div id="decisionButtons" class="decision-buttons"></div>
    </div>

    <button id="nextWeekBtn">התחל שבוע חדש</button>
</div>

<button id="toggleExplanation">הצג/הסתר רקע תיאורטי</button>

<div id="explanation" style="display: none;">
    <h2>הסבר תיאורטי: שרשרת אספקה גלובלית במשבר</h2>

    <h3>מהי שרשרת אספקה גלובלית?</h3>
    <p>שרשרת אספקה גלובלית היא רשת מורכבת המחברת ספקים, יצרנים, מפיצים ולקוחות בקצוות שונים של העולם. היא כוללת כל שלב במסע של מוצר – מחומרי גלם דרך ייצור והפצה ועד לצרכן הסופי. בעולם המחובר שלנו, חברות מתבססות על רשת זו כדי לנצל יתרונות גלובליים כמו עלויות נמוכות או גישה לחומרים ייחודיים.</p>

    <h3>מדוע שרשראות אספקה מודרניות כל כך פגיעות?</h3>
    <p>בעוד שהגלובליזציה הביאה יעילות וחיסכון עצומים, היא גם יצרה תלות הדדית עצומה. אירועים כמו מגפות, סכסוכים, אסונות טבע או משברים כלכליים יכולים לשבש בקלות את הזרימה החלקה של סחורות ומידע. תחשוב על זה: ספק יחיד באזור רגיש, ריכוז מפעלי ייצור במדינה אחת, או הסתמכות על נתיבי שינוע בודדים – כל אלה הופכים את המערכת לשברירית מול שיבושים בלתי צפויים.</p>

    <h3>המלכוד של יעילות קיצונית (Just-in-Time, Single Sourcing)</h3>
    <p>"בדיוק בזמן" (Just-in-Time) היא אסטרטגיה חסכונית המצמצמת מלאי למינימום, ומפחיתה עלויות אחסון וסיכונים. "ספק יחיד" (Single Sourcing) מתבססת על קשר עמוק ומועיל עם ספק אחד הטוב ביותר. אסטרטגיות אלו מעולות בתקופות שקטות, אך בזמן משבר הן חושפות את החברה לחוסר מוחלט של גמישות או "בופר" שיכול לספוג זעזועים. אין מלאי? אין ספק חלופי? כל תקלה קטנה יכולה להפוך במהירות למשבר אספקה בקנה מידה גדול.</p>

    <h3>בניית חוסן (Resilience): המפתח לשרידות במשבר</h3>
    <p>חוסן הוא היכולת של שרשרת האספקה לא רק לשרוד שיבושים, אלא גם להסתגל במהירות ולחזור לתפקוד. איך בונים חוסן?</p>
    <ul>
        <li><strong>גיוון:</strong> אל תשים את כל הביצים בסל אחד. עבוד עם מספר ספקים ומפעלים באזורים גאוגרפיים שונים.</li>
        <li><strong>מלאי ביטחון:</strong> שמור על רמות מלאי מינימליות אך מספקות בנקודות אסטרטגיות. זהו "המזומן" של שרשרת האספקה שלך בזמן חירום.</li>
        <li><strong>לוגיסטיקה גמישה:</strong> תכנן מראש נתיבי הובלה חלופיים – דרך הים, האוויר או היבשה – שיכולים לעקוף חסימות בלתי צפויות.</li>
        <li><strong>קירוב ייצור (Reshoring/Nearshoring):</strong> שקול להחזיר חלק מהייצור למדינה שלך או למדינות שכנות. זה אולי יקר יותר, אבל מפחית תלות בשרשראות ארוכות ורגישות.</li>
        <li><strong>שקיפות עמוקה:</strong> הכר לא רק את הספקים הישירים שלך, אלא גם את הספקים שלהם (ספקי משנה). הבנה עמוקה של השרשרת כולה מאפשרת זיהוי סיכונים מוקדם.</li>
    </ul>

    <h3>האיזון העדין: יעילות מול חוסן</h3>
    <p>בניית חוסן עולה כסף. מלאי דורש שטח ואחסון. גיוון ספקים עשוי לבטל הנחות כמות. ייצור קרוב עולה יותר. האתגר האמיתי הוא למצוא את נקודת האיזון האופטימלית: להישאר יעיל ורווחי בתקופות שקטות, אך להשקיע מספיק בחוסן כדי למנוע קריסה פיננסית ואספקתית כשהמשבר מגיע.</p>

    <h3>למד מהעבר: מקרי בוחן</h3>
    <p>משבר השבבים העולמי (פוסט-קורונה) הוא דוגמה מצוינת. תעשיות שלמות - רכב, אלקטרוניקה, מכשירים - נעצרו כי הן היו תלויות במספר זעיר של יצרני שבבים, רובם מרוכזים באזור אחד. סגירת מפעלים או עלייה פתאומית בביקוש יצרו מחסור חמור. דוגמה נוספת היא הכאוס בנמלים ובשינוע ימי במהלך המגפה: עלויות אסטרונומיות, פקקים אינסופיים ועיכובים ששיתקו את הסחר העולמי והראו כמה אנו תלויים בתשתיות לוגיסטיות.</p>
</div>

<style>
    /* Reset and Basic Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 20px;
        background-color: #eef2f7; /* Soft background */
        color: #333;
    }

    h1, h2, h3 {
        color: #0d47a1; /* Darker blue for headings */
        margin-top: 0;
    }

     .intro-text {
         font-size: 1.1em;
         color: #555;
         margin-bottom: 30px;
         text-align: center;
     }

    .app-container {
        border: 1px solid #b0bec5; /* Lighter border */
        padding: 25px;
        margin-bottom: 30px;
        background-color: #ffffff;
        border-radius: 8px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        max-width: 900px; /* Max width for better readability */
        margin-left: auto;
        margin-right: auto;
    }

    /* Map Area */
    .map-area {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 25px; /* Increased gap */
        margin-bottom: 30px;
        flex-wrap: wrap;
        position: relative; /* For absolute positioning of alt routes */
    }

    .location {
        border: 2px solid #1976d2; /* Primary blue border */
        padding: 12px 15px;
        text-align: center;
        font-size: 13px;
        width: 100px; /* Slightly wider */
        height: 60px; /* Slightly taller */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #e3f2fd; /* Light blue background */
        border-radius: 6px;
        position: relative;
        transition: transform 0.3s ease-in-out, border-color 0.3s ease-in-out; /* Smooth transitions */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .location-name {
        font-weight: bold;
        margin-bottom: 3px;
        color: #0d47a1;
    }
    .location-desc {
        font-size: 0.9em;
        color: #5e5e5e;
    }

     .location.alt {
        border-style: dashed;
        background-color: #f0f4c3; /* Light yellow for alt */
        border-color: #fbc02d; /* Yellow border */
        position: absolute; /* Position alternates absolutely */
         /* Default hide */
         display: none;
         opacity: 0;
         pointer-events: none; /* Make it non-interactive when hidden */
         transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    }
     .location.alt.active-alt {
         display: flex; /* Show when active */
         opacity: 1;
         pointer-events: auto;
         transform: translateY(0); /* Reset transform when active */
     }

     /* Positioning for alt locations - Adjust these based on layout */
     #supplier2 { top: 100px; left: 50px; transform: translateY(20px); }
     #factory2 { top: 100px; left: 250px; transform: translateY(20px); }
     #distribution2 { top: 100px; left: 450px; transform: translateY(20px); }


     .status-indicator {
        position: absolute;
        top: -10px;
        right: -10px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #4CAF50; /* Green - Default healthy */
        border: 2px solid #fff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease-in-out;
     }

     .status-indicator.warning {
        background-color: #FFC107; /* Yellow */
     }

     .status-indicator.critical {
        background-color: #F44336; /* Red */
     }

     .flow-indicator {
         position: absolute;
         width: 100%;
         height: 100%;
         top: 0;
         left: 0;
         pointer-events: none;
         overflow: hidden; /* Hide dots outside */
     }
      .flow-dot {
         position: absolute;
         width: 8px;
         height: 8px;
         background-color: rgba(0, 0, 255, 0.7); /* Blue dots */
         border-radius: 50%;
         animation: flow linear infinite;
      }
       .location.in-crisis .flow-dot {
          background-color: rgba(255, 0, 0, 0.7); /* Red dots in crisis */
       }


     @keyframes flow {
         0% { transform: translateX(-10px); opacity: 0; }
         10% { opacity: 1; }
         90% { opacity: 1; }
         100% { transform: translateX(calc(100% + 10px)); opacity: 0; }
     }

     .arrow {
        font-size: 25px;
        font-weight: bold;
        color: #1976d2; /* Blue arrow */
        transition: color 0.3s ease-in-out;
     }

     .arrow.alt-route {
        position: absolute;
        font-size: 28px;
        font-weight: normal;
        color: #fbc02d; /* Yellow arrow */
        z-index: 1; /* Ensure arrows are above locations */
         /* Default hide */
        display: none;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.5s ease-in-out;
     }
      .arrow.alt-route.active-alt {
         display: block;
         opacity: 1;
         pointer-events: auto;
      }

      /* Positioning for alt arrows - requires careful tuning */
      #alt-supplier-arrow { top: 85px; left: 165px; } /* Supplier B to Factory 1 */
      #alt-factory-arrow { top: 85px; left: 365px; } /* Factory 2 to Distribution 1 */
      #alt-distribution-arrow { top: 85px; left: 565px; } /* Distribution 2 to Market 1 */


    /* Status Area */
    .status-area {
        border: 1px solid #b0bec5;
        padding: 18px;
        margin-bottom: 25px;
        background-color: #e1f5fe; /* Lighter blue */
        border-radius: 6px;
    }
     .status-area p {
         margin-bottom: 8px;
         font-size: 1.1em;
         display: flex;
         align-items: center;
     }
     .status-area p span {
         font-weight: bold;
         margin-left: 5px;
         margin-right: 5px;
     }

    .status-change {
        font-size: 0.9em;
        margin-left: 10px;
        padding: 2px 5px;
        border-radius: 3px;
        visibility: hidden; /* Hidden by default */
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
        min-width: 40px; /* Reserve space */
        text-align: center;
    }
     .status-change.positive {
         color: #1b5e20; /* Dark green */
         background-color: #c8e6c9; /* Light green */
     }
      .status-change.negative {
         color: #b71c1c; /* Dark red */
         background-color: #ffcdd2; /* Light red */
      }
       .status-change.visible {
          visibility: visible;
          opacity: 1;
       }


    /* Events Area */
    .events-area {
        border: 1px solid #b0bec5;
        padding: 18px;
        margin-bottom: 25px;
        background-color: #fff;
        border-radius: 6px;
    }
     .event-log {
         min-height: 60px; /* Reserve space */
         margin-bottom: 15px;
         padding: 10px;
         background-color: #f5f5f5;
         border-radius: 4px;
         border: 1px solid #eee;
         font-size: 0.95em;
         white-space: pre-wrap; /* Preserve line breaks added by JS */
     }

    .decision-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
    }

    .decision-buttons button {
        flex-grow: 1; /* Allow buttons to grow */
        min-width: 120px; /* Minimum width */
        max-width: 200px; /* Max width */
        padding: 12px 15px;
        cursor: pointer;
        background-color: #2196F3; /* Primary blue */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 1em;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .decision-buttons button:hover {
        background-color: #1976D2; /* Darker blue on hover */
         box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }
     .decision-buttons button:active {
         transform: scale(0.98); /* Press effect */
     }
      .decision-buttons button:disabled {
         background-color: #b0bec5;
         cursor: not-allowed;
         box-shadow: none;
      }


    #nextWeekBtn {
        display: block;
        width: 100%;
        padding: 18px;
        font-size: 1.2em;
        cursor: pointer;
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        border-radius: 5px;
        transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #nextWeekBtn:hover {
        background-color: #388E3C; /* Darker green on hover */
         box-shadow: 0 5px 10px rgba(0,0,0,0.25);
    }
    #nextWeekBtn:active {
         transform: scale(0.99);
    }


    #toggleExplanation {
        display: block;
        margin: 30px auto;
        padding: 12px 25px;
        cursor: pointer;
        border: 1px solid #b0bec5;
        border-radius: 5px;
        background-color: #cfd8dc; /* Light grey-blue */
        color: #333;
        font-size: 1em;
        transition: background-color 0.2s ease-in-out;
    }
     #toggleExplanation:hover {
         background-color: #b0bec5;
     }


    #explanation {
        border: 1px solid #b0bec5;
        padding: 25px;
        margin-top: 20px;
        background-color: #ffffff;
        border-radius: 8px;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

    #explanation h3 {
        margin-top: 20px;
        color: #1976d2;
    }
     #explanation ul {
         margin-top: 10px;
         margin-bottom: 15px;
         padding-left: 20px;
     }
      #explanation li {
          margin-bottom: 8px;
      }

     /* Responsive adjustments */
    @media (max-width: 768px) {
         body { padding: 10px; }
         .app-container, #explanation { padding: 15px; border-radius: 4px; }
        .map-area {
            flex-direction: column;
            gap: 15px; /* Reduce gap */
        }
        .arrow.right {
            transform: rotate(90deg); /* Rotate arrows for vertical flow */
        }

        .arrow.alt-route {
             transform: rotate(0deg); /* Reset rotation for alt arrows in column */
             position: static; /* Remove absolute positioning */
             display: flex !important; /* Ensure arrows are visible if their element is visible */
             justify-content: center;
             align-items: center;
             height: 20px; /* Space between elements */
             margin: 5px auto;
             font-size: 20px;
        }
         .arrow.alt-route.active-alt { display: flex; } /* Ensure flex is kept */

         /* Adjust positioning for alt locations in column layout */
         .location.alt {
             position: static;
             transform: translateY(0);
             margin-bottom: 5px; /* Space out alternate locations */
         }


        .location {
            width: 80%; /* Wider boxes in column layout */
            height: auto;
            padding: 10px;
            font-size: 1em;
        }

        .decision-buttons button {
            flex-grow: 0; /* Don't force growth on small screens */
            width: 100%; /* Full width buttons */
            max-width: none;
        }

        .status-area p {
             flex-direction: column;
             align-items: flex-start;
        }
        .status-area p span {
            margin-left: 0;
            margin-right: 0;
            margin-top: 3px;
        }
        .status-change {
             margin-left: 0;
             margin-top: 5px;
        }
    }


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggleExplanation');
        const nextWeekBtn = document.getElementById('nextWeekBtn');
        const eventLogDiv = document.getElementById('eventLog');
        const decisionButtonsDiv = document.getElementById('decisionButtons');

        const statusSpans = {
            cost: document.getElementById('cost'),
            leadTime: document.getElementById('leadTime'),
            inventory: document.getElementById('inventory'),
            satisfaction: document.getElementById('satisfaction'),
            week: document.getElementById('week')
        };

         const statusChangeSpans = {
            cost: document.getElementById('cost-change'),
            leadTime: document.getElementById('leadTime-change'),
            inventory: document.getElementById('inventory-change'),
            satisfaction: document.getElementById('satisfaction-change')
         };

        const locations = {
            supplier1: document.getElementById('supplier1'),
            supplier2: document.getElementById('supplier2'),
            factory1: document.getElementById('factory1'),
            factory2: document.getElementById('factory2'),
            distribution1: document.getElementById('distribution1'),
            distribution2: document.getElementById('distribution2'),
            market1: document.getElementById('market1')
        };

         const arrows = document.querySelectorAll('.map-area .arrow:not(.alt-route)');
         const altArrows = {
             supplier2: document.getElementById('alt-supplier-arrow'),
             factory2: document.getElementById('alt-factory-arrow'),
             distribution2: document.getElementById('alt-distribution-arrow')
         };


        let state = {
            week: 1,
            cost: 10000,
            leadTime: 4, // Weeks, total perceived lead time
            inventory: 200, // Units at distribution center
            satisfaction: 100, // Percent
            currentSupplier: 'supplier1',
            currentFactory: 'factory1',
            currentDistribution: 'distribution1',
            baseCost: 10000,
            baseLeadTimes: { supplier1: 1, factory1: 2, distribution1: 1 }, // Lead time for each segment
            productionRate: 50, // Units produced per week
            salesRate: 45, // Units sold per week
            inventoryTarget: 200, // Desired inventory level
            crisisActive: null, // { type: '...', location: '...', severity: '...', effect: '...' }
            alternateSources: { // Cost to unlock/use alternate source
                 supplier2: { costActivate: 5000, costWeekly: 300, leadTime: 2, active: false, unlocked: false },
                 factory2: { costActivate: 7000, costWeekly: 400, leadTime: 3, active: false, unlocked: false },
                 distribution2: { costActivate: 6000, costWeekly: 350, leadTime: 2, active: false, unlocked: false }
            },
            activeEffects: { // Effects currently applied due to crisis/decisions
                 cost: 0,
                 leadTime: 0,
                 inventoryChange: 0,
                 satisfaction: 0,
                 productionMultiplier: 1, // e.g., 0.5 for reduced production
                 salesMultiplier: 1 // e.g., 1.2 for high demand
            },
             // Store previous state to calculate changes
             previousState: {}
        };

         const crises = [
            {
                type: 'supplier_disruption',
                location: 'supplier1',
                text: (loc) => `⚡️ משבר בפס הייצור של ${loc.querySelector('.location-name').textContent}: אספקת חומרי גלם נקטעה!`,
                effects: { productionMultiplier: 0.2, leadTime: 2, inventoryChange: -40, satisfaction: -8 }, // Effects if no action
                decisions: [
                    { text: 'הפעל ספק חלופי (ב')', action: 'switch_supplier', target: 'supplier2', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 5 }, // Cost comes from activation/weekly cost
                    { text: 'המתן בסבלנות', action: 'wait', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 0 } // Crisis effects apply
                ]
            },
             {
                type: 'logistics_disruption',
                location: 'distribution1', // Represents disruption to the route/port
                text: (loc) => `🚢 שביתה גדולה בנמל המרכזי של ${loc.querySelector('.location-name').textContent}: משלוחים מעוכבים!`,
                effects: { leadTime: 3, inventoryChange: -30, satisfaction: -10 }, // Effects if no action
                decisions: [
                    { text: 'הובלה אווירית דחופה (יקר)', action: 'expedite', costDecision: 4000, leadTimeDecision: -2, inventoryDecision: 20, satisfactionDecision: 10 }, // Faster but costly
                    { text: 'הפעל מרכז הפצה חלופי', action: 'switch_distribution', target: 'distribution2', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 8 },
                     { text: 'חכה לפתיחת הנמל', action: 'wait', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 0 }
                ]
            },
             {
                type: 'factory_disruption',
                location: 'factory1',
                text: (loc) => `🛠️ תקלה קריטית במכונות הייצור ב${loc.querySelector('.location-name').textContent}: הייצור הואט משמעותית!`,
                effects: { productionMultiplier: 0.4, leadTime: 1, inventoryChange: -35, satisfaction: -7 }, // Effects if no action
                decisions: [
                    { text: 'הפעל מפעל חלופי', action: 'switch_factory', target: 'factory2', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 6 },
                    { text: 'רכש ח"ג דחוף ויקר', action: 'expedite_material', costDecision: 3500, leadTimeDecision: 0, inventoryDecision: 15, satisfactionDecision: 3 },
                     { text: 'צמצם ייצור והמתן', action: 'wait', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 0 }
                ]
            },
             {
                type: 'demand_spike',
                location: 'market1', // Affects the market/sales side
                text: (loc) => `📈 עלייה פתאומית בביקוש בשוק! המלאי אוזל במהירות.`,
                effects: { salesMultiplier: 1.5, inventoryChange: -50, satisfaction: -15 }, // Increased sales deplete inventory, leading to dissatisfaction
                decisions: [
                    { text: 'הגדל מלאי ביטחון (עלות שבועית קבועה)', action: 'increase_inventory_target', costDecision: 1500, leadTimeDecision: 0, inventoryDecision: 30, satisfactionDecision: 5 }, // Increase target, maybe add some stock immediately
                     { text: 'הפנה מלאי ממקור אחר (אם יש)', action: 'divert_inventory', costDecision: 800, leadTimeDecision: 1, inventoryDecision: 20, satisfactionDecision: 12 }, // Assumes conceptual alternative stock
                     { text: 'קבל מחסור במלאי', action: 'wait', costDecision: 0, leadTimeDecision: 0, inventoryDecision: 0, satisfactionDecision: 0 } // Accept stockout consequences
                ]
            }
        ];

        // Function to update the visual flow indicators (dots)
         function animateFlow() {
             // Remove existing dots
             document.querySelectorAll('.flow-dot').forEach(dot => dot.remove());

             const addFlowDots = (startElement, endElement, duration = 3000) => {
                if (!startElement || !endElement || startElement.style.display === 'none' || endElement.style.display === 'none') return;

                const startRect = startElement.getBoundingClientRect();
                const endRect = endElement.getBoundingClientRect();
                const containerRect = document.querySelector('.map-area').getBoundingClientRect();

                const startX = startRect.left + startRect.width / 2 - containerRect.left;
                const startY = startRect.top + startRect.height / 2 - containerRect.top;
                const endX = endRect.left + endRect.width / 2 - containerRect.left;
                const endY = endRect.top + endRect.height / 2 - containerRect.top;

                const distance = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
                const angle = Math.atan2(endY - startY, endX - startX) * 180 / Math.PI;

                // Add multiple dots
                for (let i = 0; i < 5; i++) { // 5 dots for a continuous flow feel
                    const dot = document.createElement('div');
                    dot.classList.add('flow-dot');
                    dot.style.left = `${startX}px`;
                    dot.style.top = `${startY}px`;
                    dot.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`; // Center and rotate dot
                    dot.style.animation = `flow ${duration / 1000}s linear infinite ${i * (duration / 5 / 1000)}s`; // Stagger animation
                    dot.style.setProperty('--flow-distance', `${distance}px`); // Pass distance for animation
                    document.querySelector('.map-area').appendChild(dot); // Append to map-area
                }
             };

             // Define the active path based on current state
             let path = [];
             if (state.currentSupplier && state.currentFactory && state.currentDistribution) {
                path.push(locations[state.currentSupplier]);
                path.push(locations[state.currentFactory]);
                path.push(locations[state.currentDistribution]);
                path.push(locations['market1']); // Market is always the end
             }


             // Animate flow along the determined path
             for (let i = 0; i < path.length - 1; i++) {
                 addFlowDots(path[i], path[i+1]);
             }

             // Update flow animation based on crisis
             if (state.crisisActive) {
                 const crisisLocationElement = locations[state.crisisActive.location];
                 if (crisisLocationElement) {
                    crisisLocationElement.classList.add('in-crisis');
                 }
             } else {
                 document.querySelectorAll('.location').forEach(loc => loc.classList.remove('in-crisis'));
             }
         }


        function updateUI() {
            // Calculate changes from previous state
            const changes = {};
            for (const key in statusSpans) {
                 if (key === 'week') continue;
                 const currentValue = state[key];
                 const previousValue = state.previousState[key] || currentValue;
                 changes[key] = currentValue - previousValue;

                 const changeSpan = statusChangeSpans[key];
                 if (changeSpan) {
                      changeSpan.textContent = changes[key] > 0 ? `(+${changes[key]})` : (changes[key] < 0 ? `(${changes[key]})` : '');
                      changeSpan.className = 'status-change'; // Reset classes
                      if (changes[key] > 0) changeSpan.classList.add('positive');
                      if (changes[key] < 0) changeSpan.classList.add('negative');
                       // Make visible briefly if there was a change
                      if (changes[key] !== 0) {
                          changeSpan.classList.add('visible');
                          setTimeout(() => changeSpan.classList.remove('visible'), 2000); // Hide after 2 seconds
                      }
                 }
            }


            statusSpans.cost.textContent = '$' + Math.round(state.cost).toLocaleString();
            statusSpans.leadTime.textContent = state.leadTime.toFixed(1) + ' שבועות';
            statusSpans.inventory.textContent = Math.round(state.inventory).toLocaleString() + ' יחידות';
            statusSpans.satisfaction.textContent = Math.max(0, Math.min(100, Math.round(state.satisfaction))) + '%';
            statusSpans.week.textContent = state.week;

            // Update status indicators and active routes
            Object.keys(locations).forEach(locId => {
                const locElement = locations[locId];
                let indicator = locElement.querySelector('.status-indicator');

                let statusClass = '';
                let isCrisisLocation = state.crisisActive && state.crisisActive.location === locId;
                let isActiveSource = (locId === state.currentSupplier || locId === state.currentFactory || locId === state.currentDistribution);
                let isAlternate = locElement.classList.contains('alt');
                let isUnlocked = state.alternateSources[locId] && state.alternateSources[locId].unlocked;


                if (isActiveSource) {
                     // Primary active source
                    statusClass = isCrisisLocation ? 'critical' : ''; // Red if active and in crisis, else green
                    locElement.classList.add('active-route');
                    locElement.classList.remove('inactive-route', 'active-alt');
                } else if (isAlternate) {
                     // Alternate source
                     if (state.alternateSources[locId].active) {
                        statusClass = isCrisisLocation ? 'critical' : ''; // Red if active alt and in crisis, else green
                         locElement.classList.add('active-alt', 'active-route');
                         locElement.classList.remove('inactive-route');
                     } else {
                          statusClass = isUnlocked ? 'warning' : ''; // Yellow if unlocked but inactive
                          locElement.classList.remove('active-alt', 'active-route');
                           locElement.classList.add('inactive-route'); // Style for inactive option
                     }
                } else {
                     // Market or passive elements
                    statusClass = isCrisisLocation ? 'critical' : '';
                    locElement.classList.remove('active-route', 'inactive-route', 'active-alt');
                }


                indicator.className = 'status-indicator ' + statusClass;

                // Show/hide alternate sources and arrows based on being active
                 if (isAlternate) {
                      locElement.classList.toggle('active-alt', state.alternateSources[locId].active);
                      if (altArrows[locId]) {
                           altArrows[locId].classList.toggle('active-alt', state.alternateSources[locId].active);
                      }
                 }
            });

             // Update arrows for main path
             arrows.forEach(arrow => {
                 const route = arrow.dataset.route.split('-');
                 const start = route[0];
                 const end = route[1];
                 let active = false;
                 // Check if this arrow connects current active locations
                 if (start === state.currentSupplier && end === 'factory1') active = true;
                 if (start === state.currentFactory && end === 'distribution1') active = true;
                 if (start === state.currentDistribution && end === 'market1') active = true;

                 arrow.classList.toggle('active-route', active);
             });


             // Animate flow
             animateFlow();

             // Store current state for next week's changes calculation
             state.previousState = { ...state, baseLeadTimes: { ...state.baseLeadTimes }, alternateSources: JSON.parse(JSON.stringify(state.alternateSources)) };

        }

        function logEvent(message, type = 'info') {
             const p = document.createElement('p');
             p.textContent = `שבוע ${state.week}: ${message}`;
             p.classList.add(type); // Use classes for different message types (e.g., 'crisis', 'decision', 'info') - requires CSS
             eventLogDiv.prepend(p); // Add to top
             // Keep log clean, maybe last 10 messages
             while (eventLogDiv.children.length > 15) {
                eventLogDiv.removeChild(eventLogDiv.lastChild);
             }
        }

        function showEvent(event) {
            state.crisisActive = event;
            const crisisLocationElement = locations[event.location];
            const eventMessage = event.text(crisisLocationElement);
            logEvent(eventMessage, 'crisis');
            // Temporarily apply crisis effects to visualize potential impact if "wait"
            // (Actual effects applied in handleDecision or simulateWeek if 'wait')
             // This part might be complex to visualize *before* decision, let's stick to showing effects *after* decision/wait.


            decisionButtonsDiv.innerHTML = '';
            event.decisions.forEach((decision, index) => {
                const button = document.createElement('button');
                button.textContent = decision.text;
                button.onclick = () => {
                     handleDecision(decision);
                     // Disable all buttons after one is clicked
                     decisionButtonsDiv.querySelectorAll('button').forEach(btn => btn.disabled = true);
                };
                decisionButtonsDiv.appendChild(button);
            });
            nextWeekBtn.style.display = 'none'; // Hide "Next Week" button during decision
            updateUI(); // Update UI to show crisis state
        }

        function applyEffects(effects) {
             state.activeEffects.cost += (effects.cost || 0) + (effects.costDecision || 0);
             state.activeEffects.leadTime += (effects.leadTime || 0) + (effects.leadTimeDecision || 0);
             state.activeEffects.inventoryChange += (effects.inventoryChange || 0) + (effects.inventoryDecision || 0);
             state.activeEffects.satisfaction += (effects.satisfaction || 0) + (effects.satisfactionDecision || 0);
             state.activeEffects.productionMultiplier *= (effects.productionMultiplier === undefined ? 1 : effects.productionMultiplier);
             state.activeEffects.salesMultiplier *= (effects.salesMultiplier === undefined ? 1 : effects.salesMultiplier);
        }

        function resetEffects() {
             state.activeEffects = {
                 cost: 0,
                 leadTime: 0,
                 inventoryChange: 0,
                 satisfaction: 0,
                 productionMultiplier: 1,
                 salesMultiplier: 1
             };
        }


        function handleDecision(decision) {
            logEvent(`החלטה: ${decision.text}`, 'decision');

             // Apply costs/effects related to the decision
            applyEffects(decision); // Apply decision-specific effects

            // Handle specific actions that change state parameters
            if (decision.action === 'switch_supplier' && decision.target === 'supplier2') {
                 if (!state.alternateSources.supplier2.unlocked) {
                     state.cost += state.alternateSources.supplier2.costActivate; // One-time activation cost
                     state.alternateSources.supplier2.unlocked = true;
                     logEvent(`הפעלת ספק חלופי B בעלות חד-פעמית של $${state.alternateSources.supplier2.costActivate}.`, 'info');
                 }
                 state.alternateSources.supplier1.active = false; // Deactivate primary
                 state.alternateSources.supplier2.active = true; // Activate alternate
                 state.currentSupplier = 'supplier2';
                 // Adjust base lead time for supplier segment
                 state.baseLeadTimes.supplier1 = state.alternateSources.supplier2.leadTime;
            } else if (decision.action === 'switch_factory' && decision.target === 'factory2') {
                 if (!state.alternateSources.factory2.unlocked) {
                     state.cost += state.alternateSources.factory2.costActivate;
                     state.alternateSources.factory2.unlocked = true;
                     logEvent(`הפעלת מפעל חלופי 2 בעלות חד-פעמית של $${state.alternateSources.factory2.costActivate}.`, 'info');
                 }
                 state.alternateSources.factory1.active = false; // Deactivate primary
                 state.alternateSources.factory2.active = true; // Activate alternate
                 state.currentFactory = 'factory2';
                 // Adjust base lead time for factory segment
                 state.baseLeadTimes.factory1 = state.alternateSources.factory2.leadTime;

            } else if (decision.action === 'switch_distribution' && decision.target === 'distribution2') {
                 if (!state.alternateSources.distribution2.unlocked) {
                     state.cost += state.alternateSources.distribution2.costActivate;
                     state.alternateSources.distribution2.unlocked = true;
                     logEvent(`הפעלת מרכז הפצה חלופי 2 בעלות חד-פעמית של $${state.alternateSources.distribution2.costActivate}.`, 'info');
                 }
                 state.alternateSources.distribution1.active = false; // Deactivate primary
                 state.alternateSources.distribution2.active = true; // Activate alternate
                 state.currentDistribution = 'distribution2';
                 // Adjust base lead time for distribution segment
                 state.baseLeadTimes.distribution1 = state.alternateSources.distribution2.leadTime;
            } else if (decision.action === 'increase_inventory_target') {
                state.inventoryTarget += 100; // Increase target by 100 units
                state.activeEffects.cost += 500; // Apply a smaller immediate cost, weekly cost added in simulateWeek
                logEvent(`מגדיל מלאי ביטחון יעד ל-${state.inventoryTarget}.`, 'info');
            }
             else if (decision.action === 'wait') {
                 // Apply the *full* crisis effects if waiting
                 applyEffects(state.crisisActive.effects);
                 logEvent(`המתנה לסיום המשבר. השפעות מיידיות מורגשות.`, 'info');
            }

            // Crisis is resolved after a decision is made (in this simple model)
            state.crisisActive = null;
            decisionButtonsDiv.innerHTML = '';
            nextWeekBtn.style.display = 'block';

            // Recalculate total lead time based on current active path segments
            state.leadTime = state.baseLeadTimes[state.currentSupplier] + state.baseLeadTimes[state.currentFactory] + state.baseLeadTimes[state.currentDistribution];

            updateUI(); // Update UI immediately after decision

        }


        function simulateWeek() {
            state.week++;
            resetEffects(); // Reset effects from previous week/crisis

            // Apply base weekly costs
            state.cost = state.baseCost;
            // Add weekly costs for active alternate sources
            if (state.alternateSources.supplier2.active) state.cost += state.alternateSources.supplier2.costWeekly;
            if (state.alternateSources.factory2.active) state.cost += state.alternateSources.factory2.costWeekly;
            if (state.alternateSources.distribution2.active) state.cost += state.alternateSources.distribution2.costWeekly;

             // Apply inventory holding costs (simple)
             if (state.inventory > state.inventoryTarget) {
                  state.cost += (state.inventory - state.inventoryTarget) * 1; // Cost for holding excess
             }
              // Apply cost for holding base target stock
              state.cost += state.inventoryTarget * 0.5;


            // Simulate flow and inventory change (simplified)
             const actualProduction = state.productionRate * state.activeEffects.productionMultiplier;
             const actualSales = state.salesRate * state.activeEffects.salesMultiplier;

             // Inventory change is production minus sales plus any immediate changes from effects
             state.inventory = state.inventory - actualSales + actualProduction + state.activeEffects.inventoryChange;


             // Apply effects from crisis/decision (carried over if not resolved immediately - in this model, decision resolves crisis)
             // If a crisis was active last turn and decision was 'wait', its effects apply here.
             // In the current model, crisis is resolved immediately upon decision, so this isn't needed,
             // but 'activeEffects' can be used for temporary decision impacts.

             // Apply active effects to core stats
             state.cost += state.activeEffects.cost;
             state.leadTime = (state.baseLeadTimes[state.currentSupplier] + state.baseLeadTimes[state.currentFactory] + state.baseLeadTimes[state.currentDistribution]) + state.activeEffects.leadTime; // Recalculate total lead time
             state.satisfaction += state.activeEffects.satisfaction;

             // Satisfaction impact from inventory levels
             if (state.inventory < state.inventoryTarget * 0.8) state.satisfaction -= 3; // Penalty for low inventory
             if (state.inventory < state.inventoryTarget * 0.5) state.satisfaction -= 7; // Harsher penalty for very low inventory (stockout risk)
             if (state.inventory > state.inventoryTarget * 1.5) state.satisfaction += 2; // Small bonus for abundant stock


             // Ensure metrics stay within reasonable bounds
             state.satisfaction = Math.max(0, Math.min(100, state.satisfaction));
             state.inventory = Math.max(0, state.inventory);
             state.leadTime = Math.max(1, state.leadTime); // Lead time cannot be less than 1


            // Check for new crisis
            if (!state.crisisActive) { // Only trigger new crisis if previous one is resolved
                const random = Math.random();
                // Increase chance slightly each week? Or fixed? Let's do fixed for simplicity.
                const crisisChance = 0.25; // 25% chance each week
                if (random < crisisChance) {
                    const crisisIndex = Math.floor(Math.random() * crises.length);
                     // Ensure the location exists in the map (e.g. market)
                     const selectedCrisis = crises[crisisIndex];
                     if(locations[selectedCrisis.location]) {
                         showEvent(selectedCrisis);
                     } else {
                         logEvent('שבוע עבר בשקט יחסית.', 'info');
                     }

                } else {
                    logEvent('שבוע עבר בשקט יחסית.', 'info');
                    decisionButtonsDiv.innerHTML = '';
                }
            } else {
                 // If still in an active crisis (shouldn't happen with current decision model, but as fallback)
                 // Maybe apply ongoing crisis effects if no decision was made?
                 // For this simple model, decisions resolve crises. So this block isn't strictly needed if logic is correct.
            }

            updateUI();
        }

         // --- Initial Setup ---
        // Set initial active sources
        state.alternateSources.supplier1.active = true;
        state.alternateSources.factory1.active = true;
        state.alternateSources.distribution1.active = true;


        // Initial UI setup
        updateUI(); // Call once to set initial state display

        nextWeekBtn.addEventListener('click', simulateWeek);

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר רקע תיאורטי' : 'הצג רקע תיאורטי';
        });

        // Start the flow animation initially
         animateFlow();

    });
</script>