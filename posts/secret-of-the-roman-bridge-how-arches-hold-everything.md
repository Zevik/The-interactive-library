---
title: "סוד החוסן הרומי: הקשת שמחזיקה אימפריה"
english_slug: secret-of-the-roman-bridge-how-arches-hold-everything
category: "ארכאולוגיה"
tags:
  - רומא העתיקה
  - הנדסה
  - אדריכלות
  - גשרים
  - קשת
  - פיזיקה
---
# סוד החוסן הרומי: הקשת שמחזיקה אימפריה

תארו לעצמכם מבנים עצומים, גשרים מפוארים ואמות מים אדירות שנבנו לפני אלפיים שנה ועדיין עומדים על תילם. איך הצליחו המהנדסים הרומאים לבנות פלאים אלה, ללא בטון מודרני או פלדה? התשובה טמונה בהבנה גאונית של כוחות הפיזיקה - סוד הקשת הרומית. הקשת לא רק נראית אלגנטית, היא מבנה הנדסי מדהים שיודע להתמודד עם משקלים אדירים.

<div class="arch-builder-container">
    <div id="arch-app">
        <h2>בנה את הקשת שלך!</h2>
        <p id="initial-instruction" class="app-instruction">גרור את אבני הקשת (Voussoirs) לתוך אזור הבנייה כדי להתחיל לבנות על הפיגומים.</p>
         <p id="message" class="app-message"></p>
        <div id="builder-area">
            <div class="abutment left"></div>
            <div id="scaffolding">
                 <div class="voussoir-target voussoir-target-1"></div>
                 <div class="voussoir-target voussoir-target-2"></div>
                 <div class="voussoir-target voussoir-target-3"></div>
                 <div class="voussoir-target voussoir-target-4"></div>
                 <div class="voussoir-target voussoir-target-5"></div>
                 <div class="voussoir-target voussoir-target-6"></div>
                 <div class="voussoir-target voussoir-target-7"></div>
                 <div class="voussoir-target voussoir-target-8"></div>
            </div>
            <div id="arch-structure"></div>
            <div class="abutment right"></div>
             <div id="force-visualizer" style="display: none;">
                <div class="force-arrow left-thrust"></div>
                <div class="force-arrow right-thrust"></div>
                 <div class="force-label left-label">דחיפה צידית (Thrust)</div>
                 <div class="force-label right-label">דחיפה צידית (Thrust)</div>
            </div>
        </div>
        <div id="parts-area">
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable" data-part-type="voussoir">ווסואר</div>
            <div class="part voussoir draggable keystone" data-part-type="keystone">אבן ראשה</div>
        </div>

    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;700&family=Heebo:wght@300;400;700&display=swap');

    body {
         font-family: 'Heebo', sans-serif;
        direction: rtl; /* Ensure RTL for Hebrew */
        text-align: right;
    }

    h1, h2, h3, h4 {
        font-family: 'Frank Ruhl Libre', serif;
        text-align: center;
    }

    p {
        text-align: right;
    }

    .arch-builder-container {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
        padding: 30px 20px;
        background: linear-gradient(to bottom, #f8f8f8, #e0e0e0); /* Subtle gradient */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Soft shadow */
        border: 1px solid #ccc;
    }

    #arch-app h2 {
        color: #5a4a3a; /* Earthy brown */
        margin-bottom: 10px;
         font-size: 1.8em;
    }

    .app-instruction, .app-message {
        color: #666;
        min-height: 1.5em;
        margin: 10px 0;
         font-size: 1.1em;
         font-weight: bold;
    }

    #builder-area {
        position: relative;
        width: 95%; /* Use more width */
        max-width: 700px; /* Increased max width */
        height: 300px; /* Increased height */
        margin: 30px auto;
        border-bottom: 8px solid #8b4513; /* Stronger base ground */
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        overflow: hidden; /* Keep things inside bounds */
    }

    .abutment {
        width: 100px; /* Wider abutments */
        height: 200px; /* Taller abutments */
        background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjx pattern id="stone-texture" patternUnits="userSpaceOnUse" width="10" height="10"><path d="M0 0L10 10ZM10 0L0 10Z" stroke="#a0522d" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="#d2b48c"/><rect width="100%" height="100%" fill="url(#stone-texture)" opacity="0.3"/></svg>') repeat; /* Simple texture */
        background-color: #a0522d; /* Base color */
        border: 3px solid #5a4a3a;
        box-sizing: border-box;
        z-index: 10; /* Higher z-index */
        position: relative; /* For z-index to work */
    }

    #scaffolding {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: calc(100% - 200px); /* Space between abutments */
        height: 150px; /* Height matching arch rise */
        border: 3px dashed #785f4f; /* Earthy dashed line */
        border-bottom: none;
        z-index: 5;
        pointer-events: none;
         transition: all 0.8s ease-in-out; /* Smooth hide animation */
         opacity: 1;
    }

    .voussoir-target {
         position: absolute;
         width: 60px; /* Slightly larger target */
         height: 80px;
         border: 2px dashed rgba(120, 95, 79, 0.5); /* Subtle target outline */
         opacity: 0; /* Initially hidden */
         transition: opacity 0.3s ease-in-out;
         pointer-events: none; /* Don't block drops */
    }

     .voussoir-target.active {
        opacity: 1; /* Show target when voussoirs are available */
     }


    #arch-structure {
        position: absolute;
        bottom: 200px; /* Position above abutments */
        left: 50%;
        transform: translateX(-50%);
        width: calc(100% - 200px - 40px); /* Span width */
        height: 150px; /* Arch rise height */
        /* Visual guide for arch shape */
        border: 2px dashed rgba(170, 82, 45, 0.3); /* Transparent dashed line */
        border-radius: 50% 50% 0 0 / 100% 100% 0 0;
        z-index: 8; /* Below placed stones */
        pointer-events: auto; /* Make it a drop target */
         overflow: visible; /* Let stones sit slightly outside bounds if needed */
    }

    .part {
        width: 60px; /* Adjusted size */
        height: 80px; /* Adjusted size */
        background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iODAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9InN0b25lLXRleHR1cmUiIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSI+PHBhdGggZD0iTTAgMEwxNSA5TDE1IDBMMCA5Wk0xNSA2TDAgMTVWMjRaTTIgMEw4IDEwTDIgMTBaIiBzdHJva2U9IiNhMDUyMmQiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdG09IjYwIiBoZWlnaHQ9IjgwIiBmaWxsPSIjZDJiNDhjIi8+PHJlY3Qgd2lkdG09IjYwIiBoZWlnaHQ9IjgwIiBmaWxsPSJ1cmwoI3N0b25lLXRleHR1cmUpIiBvcGFjaXR5PSIwLjMiLz48L3N2Zz4='); /* Stone texture */
        background-color: #d2b48c; /* Base stone color */
        border: 2px solid #8b4513;
        margin: 8px; /* Spacing between parts */
        display: flex; /* Use flex for centering content */
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        cursor: grab;
        user-select: none;
        box-sizing: border-box;
        position: relative;
        z-index: 15; /* Higher than scaffolding */
        transition: transform 0.3s ease-out, opacity 0.3s ease-out; /* Smooth placement */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }

    .part:hover:not(.placed):not(.dragging):not(.keystone:not(.droppable)) {
        transform: translateY(-5px); /* Lift slightly on hover */
         box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);
    }

    .voussoir {
         /* Specific voussoir styling */
    }

    .keystone {
        height: 95px; /* Keystone is taller */
        background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iOTUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9InN0b25lLXRleHR1cmUiIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSI+PHBhdGggZD0iTTAgMEwxNSA5TDE1IDBMMCA5Wk0xNSA2TDAgMTVWMjRaTTIgMEw4IDEwTDIgMTBaIiBzdHJva2U9IiNhMDUyMmQiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdG09IjYwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI2I4ODYwYiIvPjxyZWN0IHdpZHRtPSI2MCIgaGVpZ2h0PSIxMDAiIGZpbGw9InVybCjac3RvbmUtdGV4dHVyZSkiIG9wYWNpdHk9IjAuMyIvPjwvc3ZnPg==') repeat;
        background-color: #b8860b; /* Golden color */
        font-weight: bold;
        cursor: not-allowed; /* Initially not droppable */
    }

    .keystone.droppable {
        cursor: grab;
         border-color: #ffcc00; /* Highlight when droppable */
         box-shadow: 0 0 10px rgba(255, 204, 0, 0.5);
    }

    #parts-area {
        margin-top: 20px;
        padding: 15px;
        background-color: #f0e4d7; /* Light parchment color */
        border-radius: 8px;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        min-height: 120px; /* Reserve space */
        gap: 10px; /* Space between items */
         box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1); /* Inner shadow */
    }

    .part.dragging {
        opacity: 0.8;
        transform: scale(1.1); /* Slightly larger when dragging */
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
    }

    .part.placed {
        position: absolute; /* Position relative to #arch-structure */
        margin: 0;
        border-color: #5a4a3a; /* Darker border when placed */
        cursor: default;
         box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1); /* Subtler shadow when placed */
         transition: left 0.5s ease-out, bottom 0.5s ease-out, transform 0.5s ease-out; /* Smooth transition to final spot */
    }

    #message {
        color: #0056b3; /* Blue for messages */
        font-weight: bold;
    }

     #message.error {
         color: #d9534f; /* Red for errors */
     }
      #message.success {
         color: #5cb85c; /* Green for success */
      }
     #message.highlight {
         color: #f0ad4e; /* Orange for highlights */
     }


    #force-visualizer {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 20;
    }

    .force-arrow {
        position: absolute;
        /* Positioning will be done by JS relative to keystone/abutments */
        width: 0; /* Start with zero width */
        height: 8px; /* Thicker arrow */
        background: linear-gradient(to right, rgba(217, 83, 79, 0.5), #d9534f); /* Gradient for depth */
        z-index: 25;
        opacity: 0;
        transition: all 1.5s ease-out; /* Slower, more dramatic animation */
         transform-origin: left center; /* Rotate around the start point */
         box-shadow: 0 0 10px rgba(217, 83, 79, 0.7); /* Glowing effect */
    }

    .force-arrow::after {
         content: '';
         position: absolute;
         top: 50%;
         right: -15px; /* Position arrowhead at the end */
         transform: translateY(-50%);
         width: 0;
         height: 0;
         border-top: 8px solid transparent;
         border-bottom: 8px solid transparent;
         border-left: 15px solid #d9534f; /* Arrowhead color */
    }

     .left-thrust::after {
         left: -15px; /* Position arrowhead at the end (left) */
         right: auto;
         border-left: none;
         border-right: 15px solid #d9534f; /* Arrowhead points left */
     }


    .force-arrow.active {
        opacity: 1;
        width: 150px; /* Animate to a specific width */
         /* Rotation and final position handled by JS */
    }

     .force-label {
         position: absolute;
         color: #d9534f;
         font-weight: bold;
         font-size: 1em;
         white-space: nowrap; /* Prevent wrapping */
         z-index: 26;
         opacity: 0;
         transition: opacity 1.5s ease-out;
     }

     .force-label.active {
         opacity: 1;
     }


    /* Explanation Section */
    #explanation {
        margin-top: 40px;
        padding: 25px;
        background-color: #e9e0d7; /* Softer background */
        border-radius: 12px;
         border: 1px solid #d5c2b3;
        text-align: right; /* Hebrew text alignment */
         line-height: 1.7;
    }

    #explanation h3 {
        color: #5a4a3a;
        border-bottom: 2px solid #a0522d;
        padding-bottom: 8px;
        margin-bottom: 20px;
         font-size: 1.6em;
    }

     #explanation h4 {
         color: #8b4513;
         margin-top: 20px;
         margin-bottom: 10px;
         font-size: 1.3em;
     }

    #explanation p, #explanation ul {
        margin-bottom: 18px;
    }

    #explanation ul {
        list-style-type: disc;
        padding-right: 20px;
         list-style-position: outside;
    }

    #explanation li {
        margin-bottom: 10px;
    }

    #explanation strong {
        color: #5a4a3a;
    }

    button#toggle-explanation {
        display: block;
        margin: 30px auto 10px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: #a0522d;
        color: white;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease;
         font-family: 'Heebo', sans-serif;
    }

    button#toggle-explanation:hover {
        background-color: #8b4513;
    }
</style>

<button id="toggle-explanation">הצג הסבר</button>

<div id="explanation" style="display: none;">
    <h3>הסבר: סוד הגשר הרומי והקשת</h3>
    <p>גשרים רומיים הם פלאי הנדסה עתיקה, שסיפקו תשתית חיונית לאימפריה. הם אפשרו תנועה מהירה של לגיונות, סחר, ותקשורת יעילה לאורך אלפי קילומטרים. המפתח לעמידותם יוצאת הדופן הוא מבנה הקשת הרומית - פתרון פשוט לכאורה, אך גאוני בפיזיקה שלו.</p>

    <h4>אבני הבניין של הקשת:</h4>
    <ul>
        <li>**ווסוארים (Voussoirs):** אבני טרפז מעוצבות בקפידה. הן נחתכות בזוויות מדויקות כך שהן נשענות זו על זו ויוצרות דחיפה פנימית חזקה כשהן נלחצות.</li>
        <li>**אבן ראשה (Keystone):** האבן המרכזית והאחרונה הממוקמת בחלק העליון של הקשת. תפקידה הקריטי הוא "לנעול" את המבנה כולו על ידי הפעלת לחץ כלפי מטה וכלפי חוץ על הווסוארים הסמוכים. לפני הצבתה, הקשת אינה יציבה ותלויה בפיגומים.</li>
        <li>**בסיסי גשר (Abutments):** העמודים או המבנים המוצקים התומכים בקצות הקשת. תפקידם לספוג את כוחות הדחיפה הצידית העצומים המופעלים על ידי הקשת ולמנוע את התמוטטותה כלפי חוץ.</li>
         <li>**מפתח (Span):** המרחק האופקי שעל הקשת לגשר עליו - בין בסיס גשר אחד למשנהו.</li>
        <li>**עלייה (Rise):** הגובה האנכי של הקשת מנקודת ההתחלה שלה בבסיס ועד לחלק הגבוה ביותר (אבן הראשה).</li>
    </ul>

    <h4>איך הקשת עובדת (הפיזיקה הפשוטה):</h4>
    <p>הקסם של הקשת טמון באופן בו היא מתרגמת עומסים. בעוד שקורה ישרה שעוברת מעל מפתח נושאת את המשקל על ידי כיפוף (יוצרת כוחות מתיחה בחלק התחתון ולחיצה בחלק העליון - כוחות שעלולים לשבור אבן), הקשת עובדת אחרת לגמרי. כאשר משקל מופעל על הקשת (המשקל העצמי של האבנים, מבנים מעליה, תנועה), הוא לא גורם לה להתכופף במרכז. במקום זאת, העומס מתפזר לאורך העקמומיות של הקשת ומתורגם בעיקר ל**כוחות לחיצה** בין האבנים.</p>
    <p>יתרה מכך, העומס האנכי מתרגם גם ל**כוחות דחיפה צידית (Thrust)** הפועלים כלפי חוץ, לדחוף את קצוות הקשת. כוחות אלו מוסטים אל הבסיסים (Abutments), שאמורים להיות חזקים ומאסיביים מספיק כדי לספוג אותם ולמנוע מהקשת "להיפתח" ולקרוס. ללא אבן הראשה שנועלת את המערכת ומייצרת את הלחץ ההדדי, או ללא בסיסים חזקים מספיק לספוג את הדחיפה, הקשת תתמוטט.</p>

    <h4>היתרונות ההנדסיים:</h4>
    <ul>
        <li>**יעילות חומרית:** אבן חזקה מאוד בלחיצה, ולכן קשתות אבן יכולות לשאת משקלים עצומים על מפתחים גדולים, ולעיתים קרובות דורשות פחות חומר מאשר מבנים אחרים לאותו מפתח.</li>
        <li>**התגברות על מפתחים גדולים:** הקשת מאפשרת לבנות גשרים מעל נהרות ועמקים רחבים בהרבה ממה שהיה אפשרי עם קורות ישרות קצרות.</li>
        <li>**עמידות:** מבנה הקשת מפזר את הכוחות בצורה אופטימלית, מה שהופך אותו לעמיד בפני רעידות אדמה, עומסים כבדים, ושחיקת הזמן - כפי שמעידים גשרים רומיים עתיקים שעדיין עומדים.</li>
    </ul>

    <h4>דוגמאות לפלאי הנדסה רומיים:</h4>
    <p>מספר גשרים ומבנים רומיים מפורסמים המשתמשים בעקרונות הקשת ושרדו עד ימינו:</p>
    <ul>
        <li>**פונט דו גאר (Pont du Gard), צרפת:** אמת מים מרהיבה בת שלוש קומות עם סדרת קשתות.</li>
        <li>**גשר אלקנטרה (Alcántara Bridge), ספרד:** גשר אבן עצום ומסיבי מעל נהר הטאחו, עם קשתות מרשימות.</li>
        <li>**קולוסאום, רומא:** אמנם לא גשר, אך המבנה האיקוני הזה משתמש בהמוני קשתות כדי לתמוך את משקלו העצום.</li>
    </ul>
     <p>המבנה הפשוט והחכם של הקשת שימש את הרומאים לבניית אימפריה פיזית שתשאיר את חותמה על העולם למשך אלפי שנים.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const partsArea = document.getElementById('parts-area');
        const archStructure = document.getElementById('arch-structure');
        const scaffolding = document.getElementById('scaffolding');
        const keystone = partsArea.querySelector('.keystone');
        const voussoirs = Array.from(partsArea.querySelectorAll('.voussoir:not(.keystone)'));
        const voussoirTargets = Array.from(scaffolding.querySelectorAll('.voussoir-target'));
        const forceVisualizer = document.getElementById('force-visualizer');
        const leftThrust = forceVisualizer.querySelector('.left-thrust');
        const rightThrust = forceVisualizer.querySelector('.right-thrust');
        const leftLabel = forceVisualizer.querySelector('.left-label');
        const rightLabel = forceVisualizer.querySelector('.right-label');
        const message = document.getElementById('message');
        const initialInstruction = document.getElementById('initial-instruction');
        const toggleExplanationButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let draggedItem = null;
        let placedVoussoirsCount = 0;
        const totalVoussoirs = voussoirs.length;
        const totalTargets = voussoirTargets.length; // Should be equal to totalVoussoirs
        const archArea = document.getElementById('arch-structure');
        const builderArea = document.getElementById('builder-area');
        const leftAbutment = document.querySelector('.abutment.left');
        const rightAbutment = document.querySelector('.abutment.right');

        // Calculate target positions based on arch shape and voussoir size
        const voussoirWidth = voussoirs[0] ? voussoirs[0].offsetWidth : 60;
        const voussoirHeight = voussoirs[0] ? vouss+oirs[0].offsetHeight : 80;
        const keystoneWidth = keystone ? keystone.offsetWidth : 60;
        const keystoneHeight = keystone ? keystone.offsetHeight : 95;

        // The arch area div defines the space, but the arch curve is what matters
        // We'll position relative to the archStructure div bottom-left corner
        const archWidth = archArea.offsetWidth; // Span excluding abutments/inner gap
        const archHeight = archArea.offsetHeight; // Rise
        const archBaseY = 0; // Relative to archStructure bottom
        const archCenterX = archWidth / 2;

        const voussoirPositions = [];
        const angleRange = Math.PI; // 180 degrees for a semi-circular arch
        const angleStep = angleRange / (totalVoussoirs + 1); // Add 1 for the keystone space
        const radius = archHeight; // Use rise as radius for simplicity

        for (let i = 0; i < totalVoussoirs; i++) {
             // Calculate angle, starting from left base (PI) to right base (0)
             // We distribute voussoirs along the curve, leaving space for the keystone in the middle
             const angle = Math.PI - (angleStep * (i + 1)); // Angles go from PI down to angleStep

            // Calculate position along the circle arc relative to archStructure center
            const x = archCenterX + radius * Math.cos(angle);
            const y = radius - radius * Math.sin(angle); // Distance from the top of the arch area

             // Calculate rotation - tangent to the curve
             const rotationAngle = (angle * 180 / Math.PI) - 90; // Tangent is 90 degrees from radius angle

            // Position relative to the bottom-left of archStructure
             const finalLeft = x - voussoirWidth / 2;
             const finalBottom = archHeight - y - voussoirHeight; // Y is distance from top, bottom needs distance from bottom

             voussoirPositions.push({ left: finalLeft, bottom: finalBottom, rotate: rotationAngle });
        }

         // Keystone position is at the very top center
         const keystoneFinalPosition = {
             left: archCenterX - keystoneWidth / 2,
             bottom: archHeight - keystoneHeight, // At the very top of the rise
             rotate: 0 // Keystone is vertical
        };

        // Assign positions to voussoir targets (optional, just for visual guide)
        // We'll use the voussoirPositions array for actual drop targets
         if (totalTargets === totalVoussoirs) {
             voussoirTargets.forEach((target, index) => {
                  // Position targets roughly where the voussoirs will land
                  // Need to adjust positions slightly as targets are not rotated
                  const pos = voussoirPositions[index];
                  target.style.left = `${pos.left + voussoirWidth / 2 - target.offsetWidth / 2}px`;
                  target.style.bottom = `${pos.bottom + voussoirHeight / 2 - target.offsetHeight / 2}px`;
                  target.style.width = `${voussoirWidth * 1.2}px`; // Make target slightly bigger than stone
                  target.style.height = `${voussoirHeight * 1.2}px`;
                  // Store target index/info on the element
                  target.dataset.index = index;
             });
         }


        // Add drag listeners to parts
        partsArea.querySelectorAll('.draggable').forEach(item => {
            item.addEventListener('dragstart', (e) => {
                if (item.classList.contains('keystone') && placedVoussoirsCount < totalVoussoirs) {
                    e.preventDefault(); // Prevent drag if not ready
                    message.textContent = "הנח קודם את כל אבני הקשת (Voussoirs).";
                     message.classList.add('error');
                    return;
                }
                 if (item.classList.contains('placed')) { // Prevent dragging placed items
                     e.preventDefault();
                     return;
                 }

                draggedItem = item;
                e.dataTransfer.effectAllowed = 'move';
                e.dataTransfer.setData('text/plain', item.id); // Not strictly needed but good practice
                item.classList.add('dragging');
                 message.textContent = ""; // Clear message on drag start
                 message.className = 'app-message'; // Reset message class

                // Show Voussoir targets when dragging voussoir
                 if (item.getAttribute('data-part-type') === 'voussoir' && placedVoussoirsCount < totalVoussoirs) {
                     voussoirTargets.forEach(target => target.classList.add('active'));
                 }
            });

             item.addEventListener('dragend', () => {
                 if (draggedItem) { // Check if draggedItem is still valid
                     draggedItem.classList.remove('dragging');
                 }
                 draggedItem = null;
                 // Hide Voussoir targets
                 voussoirTargets.forEach(target => target.classList.remove('active'));
             });
        });

        // Add drop listener to the arch structure area
        archStructure.addEventListener('dragover', (e) => {
            e.preventDefault(); // Allow drop
            e.dataTransfer.dropEffect = 'move';
            // Add visual feedback to drop zone if needed
             archStructure.style.borderColor = 'rgba(170, 82, 45, 0.8)';
        });

         archStructure.addEventListener('dragleave', () => {
              archStructure.style.borderColor = 'rgba(170, 82, 45, 0.3)';
         });


        archStructure.addEventListener('drop', (e) => {
            e.preventDefault();
             archStructure.style.borderColor = 'rgba(170, 82, 45, 0.3)'; // Reset border color

            if (!draggedItem) return;

            const type = draggedItem.getAttribute('data-part-type');

            if (type === 'voussoir') {
                if (placedVoussoirsCount < totalVoussoirs) {
                    // Find the next available voussoir slot based on count
                    const targetPos = voussoirPositions[placedVoussoirsCount];
                    placePart(draggedItem, archStructure, targetPos.left, targetPos.bottom, targetPos.rotate);
                    placedVoussoirsCount++;
                    checkCompletion();
                } else {
                     message.textContent = "כל חלקי האבן כבר הונחו. כעת הנח את אבן הראשה.";
                     message.classList.add('highlight');
                }
            } else if (type === 'keystone') {
                if (placedVoussoirsCount === totalVoussoirs) {
                    placePart(draggedItem, archStructure, keystoneFinalPosition.left, keystoneFinalPosition.bottom, keystoneFinalPosition.rotate);
                    checkCompletion(); // Will trigger keystone logic
                } else {
                    message.textContent = "הנח קודם את כל אבני הקשת (Voussoirs).";
                     message.classList.add('error');
                }
            }

            // draggedItem = null; // Reset handled by dragend
        });

        // Helper function to place a part inside a container
        function placePart(item, container, left, bottom, rotate) {
            item.style.position = 'absolute';
             // Use requestAnimationFrame for smoother transition start
            requestAnimationFrame(() => {
                 item.style.left = left + 'px';
                 item.style.bottom = bottom + 'px';
                 item.style.transform = `rotate(${rotate}deg)`; // Apply rotation
            });

            item.classList.add('placed');
            item.classList.remove('draggable');
            item.draggable = false; // Disable further dragging
            container.appendChild(item); // Move the element to the target container (archStructure)
             // Remove from original parts area flow (optional, flexbox handles it)
             // item.style.margin = '0';
        }

        // Check progress and update state/message
        function checkCompletion() {
            if (placedVoussoirsCount === totalVoussoirs) {
                message.textContent = "כל אבני הקשת במקום! כעת הגיע תור אבן הראשה.";
                 message.classList.remove('error', 'success');
                 message.classList.add('highlight');

                keystone.classList.add('droppable'); // Make keystone droppable
                keystone.draggable = true; // Enable keystone dragging
            }

            if (placedVoussoirsCount === totalVoussoirs && archStructure.querySelector('.keystone.placed')) {
                 message.textContent = "הקשת הושלמה ויציבה!";
                 message.classList.remove('error', 'highlight');
                 message.classList.add('success');

                 initialInstruction.style.display = 'none'; // Hide initial instruction

                 // Animate scaffolding out
                 scaffolding.style.opacity = 0;
                 setTimeout(() => scaffolding.style.display = 'none', 800); // Match transition duration

                 showForces(); // Show force arrows
            }
        }

        // Animate and show the force arrows
        function showForces() {
             forceVisualizer.style.display = 'block';

            // Calculate positions dynamically based on placed elements
            const keystoneEl = archStructure.querySelector('.keystone.placed');
            const leftAbutmentRect = leftAbutment.getBoundingClientRect();
            const rightAbutmentRect = rightAbutment.getBoundingClientRect();
            const builderRect = builderArea.getBoundingClientRect();

            if (keystoneEl) {
                 const keystoneRect = keystoneEl.getBoundingClientRect();

                 // Start point for arrows (base of keystone) relative to builder area
                 const startX = keystoneRect.left + keystoneRect.width / 2 - builderRect.left;
                 const startY = keystoneRect.bottom - builderRect.top; // Base of keystone

                 // End points for arrows (top corners of abutments) relative to builder area
                 const endLeftX = leftAbutmentRect.right - builderRect.left;
                 const endLeftY = leftAbutmentRect.top - builderRect.top + 20; // Slight offset down

                 const endRightX = rightAbutmentRect.left - builderRect.left;
                 const endRightY = rightAbutmentRect.top - builderRect.top + 20; // Slight offset down


                 // Calculate angles for left arrow (from startX,startY to endLeftX,endLeftY)
                 const angleLeftRad = Math.atan2(endLeftY - startY, endLeftX - startX);
                 const angleLeftDeg = angleLeftRad * 180 / Math.PI;
                 const distLeft = Math.sqrt(Math.pow(endLeftX - startX, 2) + Math.pow(endLeftY - startY, 2));

                 // Calculate angles for right arrow (from startX,startY to endRightX,endRightY)
                 const angleRightRad = Math.atan2(endRightY - startY, endRightX - startX);
                 const angleRightDeg = angleRightRad * 180 / Math.PI;
                 const distRight = Math.sqrt(Math.pow(endRightX - startX, 2) + Math.pow(endRightY - startY, 2));


                // Set initial positions and rotations for animation start (width 0)
                 leftThrust.style.left = `${startX}px`;
                 leftThrust.style.top = `${startY}px`;
                 leftThrust.style.transform = `rotate(${angleLeftDeg}deg)`;
                 leftThrust.style.width = '0px'; // Start width at 0
                 leftThrust.style.opacity = 0;

                 rightThrust.style.left = `${startX}px`;
                 rightThrust.style.top = `${startY}px`;
                 rightThrust.style.transform = `rotate(${angleRightDeg}deg)`;
                 rightThrust.style.width = '0px'; // Start width at 0
                 rightThrust.style.opacity = 0;

                // Position labels initially near keystone, will animate with arrows
                 leftLabel.style.left = `${startX - 50}px`; // Offset slightly
                 leftLabel.style.top = `${startY - 20}px`;
                 leftLabel.style.opacity = 0;

                 rightLabel.style.left = `${startX + 10}px`; // Offset slightly
                 rightLabel.style.top = `${startY - 20}px`;
                 rightLabel.style.opacity = 0;


                 // Animate width and opacity after a delay
                 setTimeout(() => {
                     leftThrust.style.width = `${distLeft - 30}px`; // Animate to calculated distance minus arrowhead size
                     leftThrust.style.opacity = 1;

                     rightThrust.style.width = `${distRight - 30}px`;
                     rightThrust.style.opacity = 1;

                     // Animate labels
                      leftLabel.style.left = `${startX - 50 - (distLeft/2)}px`; // Move label with arrow
                      leftLabel.style.top = `${startY - 20 - (distLeft/4)}px`;
                      leftLabel.style.opacity = 1;

                      rightLabel.style.left = `${startX + 10 + (distRight/2)}px`;
                      rightLabel.style.top = `${startY - 20 - (distRight/4)}px`;
                      rightLabel.style.opacity = 1;


                 }, 300); // Short delay before force animation starts
            }
        }


        // Add event listener for the explanation button
        toggleExplanationButton.addEventListener('click', () => {
            const isVisible = explanationDiv.style.display !== 'none';
            explanationDiv.style.display = isVisible ? 'none' : 'block';
            toggleExplanationButton.textContent = isVisible ? 'הצג הסבר' : 'הסתר הסבר';
             // Scroll to explanation if showing
             if (!isVisible) {
                 setTimeout(() => { // Delay scroll slightly for display:block to render
                     explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
                 }, 10);
             }
        });

         // Initial setup
         message.textContent = "גרור את אבני הקשת (Voussoirs) למקום על הפיגומים.";
         message.classList.add('initial');

         // Make voussoirs initially draggable
         voussoirs.forEach(v => v.draggable = true);
         keystone.draggable = false; // Keystone is not draggable initially
         keystone.classList.remove('droppable'); // Ensure keystone is not droppable initially

         // Initially show voussoir targets
         voussoirTargets.forEach(target => target.classList.add('active'));

    });

</script>
---
```