---
title: "בנה אנזים, בדוק סובסטרטים: הצורה קובעת את הפעולה"
english_slug: build-enzyme-test-substrates-shape-determines-function
category: "מדעי החיים / ביולוגיה"
tags: ["אנזימים", "סובסטרטים", "אתר פעיל", "מבנה חלבון", "קטליזה", "התאמה מושרית"]
---
<h1>בנה אנזים, בדוק סובסטרטים: הצורה קובעת את הפעולה</h1>

<p>האם ידעתם שלא כל אנזים יכול לפרק כל מולקולה? מדוע אנזימים מסוימים פועלים רק על חומרים ספציפיים, בעוד שאחרים נשארים אדישים אליהם? הגילוי טמון במבנה המולקולרי הייחודי שלהם ובעיקרון ההתאמה המדויקת. נסו לבנות אנזים משלכם ובדקו אילו סובסטרטים הוא יוכל לזהות ולקשור!</p>

<div class="simulation-container">
    <div class="enzyme-area">
        <h2>בנה את האנזים שלך</h2>
        <div class="enzyme-builder">
            <div class="builder-controls">
                <label for="active-site-shape">בחר צורת אתר פעיל:</label>
                <select id="active-site-shape">
                    <option value="square">מרובע</option>
                    <option value="circle">עיגול</option>
                    <option value="triangle">משולש</option>
                    <option value="pocket">כיס (מורכב)</option>
                </select>
            </div>
            <div class="attraction-points-controls">
                <h4>הוסף נקודות משיכה (עד 3):</h4>
                <button data-color="red" class="point-button">אדום</button>
                <button data-color="blue" class="point-button">כחול</button>
                <button data-color="green" class="point-button">ירוק</button>
                 <button class="clear-points-btn">נקה נקודות</button>
            </div>
        </div>
        <div id="enzyme" class="enzyme drop-target">
            <div id="active-site" class="active-site"></div>
        </div>
        <div id="interaction-result" class="result-message">גרור סובסטרט לכאן לבדיקה!</div>
    </div>

    <div class="substrate-area">
        <h2>גרור סובסטרטים לבדיקה</h2>
        <div class="substrate-gallery">
            <div class="substrate square" data-shape="square" data-colors='[]' draggable="true">סובסטרט א' (מרובע)</div>
            <div class="substrate circle" data-shape="circle" data-colors='["red"]' draggable="true">סובסטרט ב' (עיגול + אדום) <div class="point red"></div></div>
            <div class="substrate triangle" data-shape="triangle" data-colors='["blue", "green"]' draggable="true">סובסטרט ג' (משולש + כחול, ירוק) <div class="point blue"></div><div class="point green"></div></div>
            <div class="substrate pocket" data-shape="pocket" data-colors='["red", "blue"]' draggable="true">סובסטרט ד' (כיס + אדום, כחול) <div class="point red"></div><div class="point blue"></div></div>
             <div class="substrate circle" data-shape="circle" data-colors='["blue"]' draggable="true">סובסטרט ה' (עיגול + כחול) <div class="point blue"></div></div>
        </div>
    </div>
</div>

<style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #f0f8f4; /* Light greenish background */
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, h4 {
        color: #0056b3; /* Blue headings */
        text-align: center;
    }

    p {
        margin-bottom: 15px;
    }

    /* Simulation Layout */
    .simulation-container {
        display: flex;
        justify-content: space-around;
        margin-top: 30px;
        flex-wrap: wrap;
        gap: 30px; /* Increased gap */
        direction: rtl;
    }

    .enzyme-area, .substrate-area {
        background-color: #ffffff; /* White background for sections */
        border: 1px solid #dcdcdc; /* Light gray border */
        padding: 20px; /* Increased padding */
        border-radius: 12px; /* More rounded corners */
        width: 48%; /* Slightly wider */
        min-width: 320px; /* Increased min-width */
        box-sizing: border-box;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow */
        position: relative;
    }

    /* Enzyme Builder Controls */
    .enzyme-builder {
        margin-bottom: 20px;
        border-bottom: 1px dashed #ccc;
        padding-bottom: 15px;
    }

    .builder-controls select,
    .attraction-points-controls button {
        padding: 8px 12px;
        margin-left: 8px; /* Hebrew spacing */
        border: 1px solid #007bff; /* Blue border */
        border-radius: 5px;
        background-color: #e9f5ff; /* Light blue background */
        color: #0056b3; /* Dark blue text */
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .builder-controls select:hover,
    .attraction-points-controls button:hover {
        background-color: #007bff;
        color: #ffffff;
        border-color: #0056b3;
    }

     .attraction-points-controls {
         display: flex;
         align-items: center;
         flex-wrap: wrap;
         gap: 8px; /* Spacing between buttons */
         margin-top: 10px;
     }

    .attraction-points-controls h4 {
        margin: 0 15px 0 0; /* Hebrew spacing */
        font-size: 1em;
        color: #555;
    }

    .attraction-points-controls .point-button {
         background-color: #fff; /* White background for color buttons */
         border-color: #ccc;
    }
     .attraction-points-controls .point-button[data-color="red"] { color: red; border-color: red; }
     .attraction-points-controls .point-button[data-color="blue"] { color: blue; border-color: blue; }
     .attraction-points-controls .point-button[data-color="green"] { color: green; border-color: green; }

     .attraction-points-controls .point-button:hover {
         background-color: #f0f0f0;
     }
     .attraction-points-controls .point-button[data-color="red"]:hover { background-color: #ffebeb; }
     .attraction-points-controls .point-button[data-color="blue"]:hover { background-color: #ebf3ff; }
     .attraction-points-controls .point-button[data-color="green"]:hover { background-color: #ebf7eb; }


     .attraction-points-controls .clear-points-btn {
         background-color: #f8d7da; /* Light red for clear */
         border-color: #dc3545; /* Red border */
         color: #dc3545; /* Red text */
     }
      .attraction-points-controls .clear-points-btn:hover {
          background-color: #dc3545;
          color: #fff;
      }


    /* Enzyme Display Area */
    .enzyme {
        width: 300px; /* Larger enzyme area */
        height: 200px;
        border: 3px dashed #007bff; /* More prominent dashed border */
        margin: 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        background-color: #f0f8ff; /* Very light blue background */
        border-radius: 10px; /* Slightly rounded enzyme box */
        overflow: hidden;
        transition: border-color 0.3s ease; /* Smooth border change on dragover */
    }

    .enzyme.dragover {
         border-color: #28a745; /* Green border on dragover */
    }


    .active-site {
        width: 120px; /* Larger active site */
        height: 120px;
        background-color: rgba(40, 167, 69, 0.3); /* Semi-transparent green */
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        transition: all 0.5s ease; /* Smooth shape transitions */
         box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); /* Subtle inner shadow */
    }

    /* Active site shapes */
    .active-site.square { border-radius: 0; }
     .active-site.circle { border-radius: 50%; }
     .active-site.triangle {
        width: 0;
        height: 0;
        border-left: 60px solid transparent; /* Larger triangle */
        border-right: 60px solid transparent;
        border-bottom: 120px solid rgba(40, 167, 69, 0.3);
        background-color: transparent;
        top: -30px; /* Adjust position */
        transform: translateY(-10px); /* Slight lift */
    }
    .active-site.pocket {
        width: 140px; /* Wider pocket */
        height: 90px; /* Shorter pocket */
        border-radius: 15px 15px 50px 50px; /* More pronounced pocket shape */
        background-color: rgba(40, 167, 69, 0.3);
    }


    /* Attraction points within Active Site */
    .active-site .point {
        position: absolute;
        width: 12px; /* Larger points */
        height: 12px;
        border-radius: 50%;
        border: 2px solid #fff; /* White border for visibility */
        box-shadow: 0 0 5px rgba(0,0,0,0.3);
        z-index: 1; /* Ensure points are above active site background */
        /* JS will set top/left */
    }
    .active-site .point.red { background-color: #dc3545; } /* Red */
    .active-site .point.blue { background-color: #007bff; } /* Blue */
    .active-site .point.green { background-color: #28a745; } /* Green */


    /* Substrate Gallery */
    .substrate-gallery {
        display: flex;
        flex-wrap: wrap;
        gap: 20px; /* Increased gap */
        margin-top: 20px;
        min-height: 180px; /* Reserve more space */
         justify-content: center;
         align-items: flex-start; /* Align items to the top */
    }

    .substrate {
        padding: 12px; /* Increased padding */
        border: 2px solid #007bff; /* Blue border */
        cursor: grab;
        background-color: #ffffff;
        position: relative;
        min-width: 90px; /* Increased min-width */
        text-align: center;
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         font-size: 0.95em;
         transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow */
         will-change: transform, opacity; /* Hint for animation performance */
    }

    .substrate:hover {
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }

    .substrate.dragging-substrate {
        opacity: 0.7;
        cursor: grabbing;
    }


    /* Substrate shapes - matching active site shapes for visual consistency */
     .substrate.square { border-radius: 5px; } /* Slightly rounded corners for substrates */
     .substrate.circle { border-radius: 50%; }
     .substrate.triangle {
         width: 0;
        height: 0;
        padding: 0;
        border-left: 45px solid transparent; /* Slightly smaller triangle */
        border-right: 45px solid transparent;
        border-bottom: 90px solid #ffffff; /* Base color */
         border-color: transparent transparent #007bff transparent; /* Blue outline */
         box-sizing: content-box;
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         position: relative;
         top: 0;
         font-size: 0.85em;
         line-height: 1.3;
         text-align: center;
         padding-bottom: 10px; /* Add padding below text for points */
          box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Shadow for triangle */
    }
     .substrate.triangle > div {
         position: static; /* Make points stack normally */
         margin: 3px 0; /* Spacing for stacked points */
     }
     .substrate.triangle:hover {
          transform: translateY(-5px);
          box-shadow: 0 6px 12px rgba(0,0,0,0.2);
     }

    .substrate.pocket {
        width: 110px; /* Slightly larger pocket substrate */
        height: 80px;
         background-color: #ffffff;
         border-radius: 12px 12px 40px 40px; /* Matching pocket shape */
         padding: 8px;
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .substrate.pocket:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }


    /* Attraction points within Substrates */
    .substrate .point {
        width: 10px; /* Slightly larger points */
        height: 10px;
        border-radius: 50%;
        margin: 3px 0;
        border: 1px solid #fff; /* White border */
        box-shadow: 0 0 3px rgba(0,0,0,0.2);
    }
    .substrate .point.red { background-color: #dc3545; }
    .substrate .point.blue { background-color: #007bff; }
    .substrate .point.green { background-color: #28a745; }


    /* Result Message */
    .result-message {
        margin-top: 20px;
        padding: 10px;
        border-radius: 8px;
        min-height: 2em; /* Ensure consistent height */
        text-align: center;
        font-size: 1.1em; /* Larger font */
        font-weight: bold;
        color: #333;
        background-color: #e9ecef; /* Light grey default */
        transition: background-color 0.5s ease, color 0.5s ease;
    }

    /* Result Message States */
    .result-message.success {
         background-color: #d4edda; /* Light green */
         color: #155724; /* Dark green */
         border: 1px solid #c3e6cb;
    }
     .result-message.partial {
         background-color: #fff3cd; /* Light yellow */
         color: #856404; /* Dark yellow */
         border: 1px solid #ffeeba;
     }
    .result-message.fail {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        border: 1px solid #f5c6cb;
        animation: shake 0.5s; /* Shake effect on fail */
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-10px); }
        40%, 80% { transform: translateX(10px); }
    }


    /* Animation styles */
    /* Removed previous bind/no-bind animations */

    /* Animation for successful binding */
    .substrate.binding {
        animation: bind-into-active-site 0.8s ease-out forwards;
         opacity: 1 !important; /* Override dragging opacity */
    }

     @keyframes bind-into-active-site {
        0% {
            transform: translate3d(var(--start-dx), var(--start-dy), 0) scale(1);
            opacity: 1;
        }
        70% {
             transform: translate3d(var(--end-dx), var(--end-dy), 0) scale(0.9);
             opacity: 0.9;
             box-shadow: 0 0 15px rgba(40, 167, 69, 0.8); /* Green glow effect */
        }
        100% {
             transform: translate3d(var(--end-dx), var(--end-dy), 0) scale(0.9);
             opacity: 0.8;
             box-shadow: 0 0 15px rgba(40, 167, 69, 0.5);
         }
    }


    /* Animation for failed binding */
     .substrate.no-binding {
         animation: reject-from-active-site 0.8s ease-out forwards;
         border-color: #dc3545; /* Indicate rejection */
         opacity: 1 !important; /* Override dragging opacity */
         box-shadow: 0 0 15px rgba(220, 53, 69, 0.8); /* Red glow effect */
     }

    @keyframes reject-from-active-site {
        0% { transform: translate3d(var(--start-dx), var(--start-dy), 0) scale(1); }
        40% { transform: translate3d(var(--end-dx), var(--end-dy), 0) scale(1); } /* Move close to active site */
        100% { transform: translate3d(var(--start-dx), var(--start-dy), 0) scale(1); } /* Return to start position */
    }


    /* Explanation Section */
    .explanation-button {
        display: block;
        margin: 40px auto 20px auto; /* More margin */
        padding: 12px 25px; /* Larger button */
        font-size: 1.1em;
        cursor: pointer;
        background-color: #007bff; /* Blue button */
        color: #fff;
        border: none;
        border-radius: 6px;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .explanation-button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
     .explanation-button:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    .explanation-content {
        display: none; /* Initially hidden */
        margin-top: 30px;
        padding-top: 25px;
        border-top: 2px solid #007bff; /* Blue border top */
        direction: rtl;
        text-align: right;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

     .explanation-content h2 { text-align: right; color: #0056b3; border-bottom: 1px solid #eee; padding-bottom: 10px; }
     .explanation-content h3 { margin-top: 20px; color: #0056b3; }
     .explanation-content ul {
         margin-top: 10px;
         padding-right: 25px; /* Hebrew list indent */
         list-style: disc; /* Bullet points */
     }
     .explanation-content li {
         margin-bottom: 8px;
     }

     b { font-weight: bold; color: #0056b3; } /* Highlight key terms */


</style>

<button class="explanation-button">הצג/הסתר הסבר על אנזימים וסובסטרטים</button>

<div class="explanation-content">
    <h2>הסבר מעמיק: אנזימים, סובסטרטים והתאמת הצורה</h2>

    <h3>מבוא: המנועים המולקולריים של החיים</h3>
    אנזימים הם גיבורי-על בלתי נראים בעולם הביולוגיה! הם חלבונים מיוחדים שפועלים כמזרזים (קטליזטורים) טבעיים. תפקידם הוא להאיץ תגובות כימיות בגופנו ובכל יצור חי בקצב אדיר - לפעמים מיליוני ואף מיליארדי פעמים מהר יותר מאשר בלעדיהם. דמיינו מפעל ענק שכל המכונות בו פועלות במהירות שיא רק בזכות מנהלי עבודה ספציפיים - אלו הם האנזימים. והכי חשוב, הם מבצעים את עבודתם שוב ושוב מבלי להישחק או להשתנות.

    <h3>מבנה מולקולרי: הצורה שקובעת הכל</h3>
    כמו כל החלבונים, אנזימים בנויים משרשראות ארוכות של יחידות קטנות יותר הנקראות חומצות אמינו. סדר חומצות האמינו הללו אינו אקראי, אלא מקודד גנטית. שרשרת זו מתקפלת במרחב לצורה תלת-ממדית מורכבת ומדויקת להפליא. צורה ייחודית זו היא הסוד לפעילות האנזים! שינוי קל בצורה (למשל, עקב שינוי בטמפרטורה או חומציות) עלול לפגוע או להרוס את פעילותו.

    <h3>האתר הפעיל: אזור הפעולה הסודי</h3>
    בתוך המבנה התלת-ממדי הענק של האנזים, קיים אזור ספציפי אחד, קטן יחסית, הנקרא "האתר הפעיל". אזור זה הוא חלל בעל צורה גיאומטרית ותכונות כימיות (כמו מטענים חשמליים, קבוצות הידרופוביות/הידרופיליות) מדויקות וייחודיות. זהו המקום שבו מתרחשת כל הפעולה!

    <h3>סובסטרטים: המטרות הספציפיות</h3>
    המולקולות שהאנזים פועל עליהן נקראות סובסטרטים. אנזימים מאופיינים בספציפיות גבוהה מאוד - כל אנזים "מכיר" ופועל רק על סובסטרט אחד או קבוצה מצומצמת של סובסטרטים דומים מאוד. הסובסטרט חייב להתאים לאתר הפעיל, לא רק בצורה, אלא גם בתכונות הכימיות שלו.

    <h3>כיצד הם נקשרים? מנעול ומפתח מול התאמה מושרית</h3>
    ההתאמה בין האנזים לסובסטרט היא קריטית לקישור ולקטליזה (זירוז התגובה). שני מודלים עיקריים מסבירים את זה:
    <ul>
        <li><b>מודל "מנעול ומפתח" (Lock and Key Model):</b> המודל הקלאסי והפשוט יותר (זה שאנחנו מדגימים בצורה מפושטת כאן). לפיו, האתר הפעיל של האנזים והסובסטרט הם בעלי צורות קשיחות ומשלימות זו את זו בצורה מדויקת, כמו מפתח שנכנס רק למנעול המתאים לו.</li>
        <li><b>מודל "התאמה מושרית" (Induced Fit Model):</b> המודל המקובל יותר כיום. לפיו, האתר הפעיל אינו קשיח לחלוטין. כאשר הסובסטרט מתקרב ונקשר לאתר הפעיל, מתרחש שינוי קל, "השראה", בצורת האתר הפעיל (ולפעמים גם בצורת הסובסטרט עצמו). שינוי זה משפר את ההתאמה, מחזק את הקישור ומכין את הסובסטרט בצורה אופטימלית לתגובה הכימית. חשבו על כפפה שמתעצבת סביב היד שנכנסת אליה.</li>
    </ul>
    הסימולציה שלנו מאפשרת לכם להתנסות בעקרון הבסיסי המשותף לשני המודלים: הצורך בהתאמה של צורה ותכונות כימיות (המיוצגות על ידי נקודות המשיכה) על מנת שיתרחש קישור.

    <h3>החשיבות של הספציפיות</h3>
    הספציפיות הגבוהה של אנזימים היא המפתח לתפקוד תקין של התא והאורגניזם כולו. היא מבטיחה שכל אנזים יזרז רק את התגובה הנכונה בזמן הנכון, ומונעת "בלבול" ותגובות שגויות שיכולות להיות הרסניות.

    <h3>הניסוי שלך: צורה + תכונות = פעולה!</h3>
    בסימולציה, אתם משנים את הצורה הגיאומטרית של האתר הפעיל ואת התכונות הכימיות שלו (באמצעות הוספת נקודות משיכה בצבעים שונים). כל סובסטרט בגלריה הוא בעל צורה ותכונות משלו. גררו סובסטרטים לאנזים שבניתם וראו האם הם מתאימים. האם הצורה לבדה מספיקה? האם התכונות הכימיות חשובות? נסו וגלו בעצמכם כיצד <b>הצורה (והתכונות) קובעת את הפעולה</b> בעולם המרתק של האנזימים!
</div>

<script>
    const activeSite = document.getElementById('active-site');
    const shapeSelect = document.getElementById('active-site-shape');
    const attractionPointsControls = document.querySelector('.attraction-points-controls');
    const clearPointsBtn = document.querySelector('.clear-points-btn');
    const enzymeArea = document.getElementById('enzyme'); // Drop target
    const resultMessage = document.getElementById('interaction-result');
    const substrates = document.querySelectorAll('.substrate-gallery .substrate'); // Select only from gallery
    const explanationButton = document.querySelector('.explanation-button');
    const explanationContent = document.querySelector('.explanation-content');

    let activeSitePoints = []; // Stores { color: 'red', element: divElement }

    // Initial setup
    updateActiveSiteShape();
    // Initial state of explanation
    explanationContent.style.display = 'none';


    // Event listener for shape change
    shapeSelect.addEventListener('change', updateActiveSiteShape);

    // Event listeners for attraction points
    attractionPointsControls.querySelectorAll('button.point-button').forEach(button => {
        button.addEventListener('click', () => {
            const color = button.dataset.color;
            addActiveSitePoint(color);
        });
    });

     // Event listener for clear points button
     clearPointsBtn.addEventListener('click', clearActiveSitePoints);


    function updateActiveSiteShape() {
        const selectedShape = shapeSelect.value;
        // Remove previous shape classes
        activeSite.className = 'active-site';
        // Add new shape class
        activeSite.classList.add(selectedShape);
        // Clear existing points (shape change resets binding potential)
        clearActiveSitePoints();
        resultMessage.textContent = 'גרור סובסטרט לכאן לבדיקה!'; // Reset message
        resultMessage.className = 'result-message'; // Reset message class

        // Position points based on the new shape if any exist (should be empty after clear)
        positionActiveSitePoints();
    }

    function addActiveSitePoint(color) {
        // Limit number of points for simplicity
        if (activeSitePoints.length >= 3) return;

         // Prevent adding duplicate colors
        if (activeSitePoints.some(point => point.color === color)) return;


        const point = document.createElement('div');
        point.classList.add('point', color);
        activeSite.appendChild(point); // Add to DOM immediately

        activeSitePoints.push({ color: color, element: point }); // Store color and element

        positionActiveSitePoints(); // Position all current points
        resultMessage.textContent = 'גרור סובסטרט לכאן לבדיקה!'; // Clear message on adding point
        resultMessage.className = 'result-message'; // Reset message class
    }

    function clearActiveSitePoints() {
         activeSitePoints.forEach(point => point.element.remove()); // Remove point elements from DOM
         activeSitePoints = []; // Clear array
         resultMessage.textContent = 'גרור סובסטרט לכאן לבדיקה!'; // Clear message on clearing points
         resultMessage.className = 'result-message'; // Reset message class
    }

     function positionActiveSitePoints() {
         const points = activeSitePoints.map(p => p.element); // Get the actual DOM elements
         const numPoints = points.length;
         const activeSiteRect = activeSite.getBoundingClientRect();
         const activeSiteWidth = activeSiteRect.width;
         const activeSiteHeight = activeSiteRect.height;

         // Simple positioning logic based on the number of points
         // Position points relative to the active site container
         if (activeSite.classList.contains('triangle')) {
             // Specific logic for triangle - position points within the visible area
             // Triangle base is at the bottom
              if (numPoints === 1) {
                  points[0].style.cssText = 'bottom: 20%; left: 50%; transform: translate(-50%, 0); top: auto;';
              } else if (numPoints === 2) {
                  points[0].style.cssText = 'bottom: 20%; left: 35%; transform: translate(-50%, 0); top: auto;';
                  points[1].style.cssText = 'bottom: 20%; left: 65%; transform: translate(-50%, 0); top: auto;';
              } else if (numPoints === 3) {
                  points[0].style.cssText = 'bottom: 40%; left: 50%; transform: translate(-50%, 0); top: auto;';
                  points[1].style.cssText = 'bottom: 15%; left: 30%; transform: translate(-50%, 0); top: auto;';
                  points[2].style.cssText = 'bottom: 15%; left: 70%; transform: translate(-50%, 0); top: auto;';
              }
         } else {
             // Default positioning for other shapes (square, circle, pocket)
              if (numPoints === 1) {
                  points[0].style.cssText = 'top: 50%; left: 50%; transform: translate(-50%, -50%);';
              } else if (numPoints === 2) {
                  points[0].style.cssText = 'top: 50%; left: 30%; transform: translate(-50%, -50%);';
                  points[1].style.cssText = 'top: 50%; left: 70%; transform: translate(-50%, -50%);';
              } else if (numPoints === 3) {
                  points[0].style.cssText = 'top: 30%; left: 50%; transform: translate(-50%, -50%);';
                  points[1].style.cssText = 'top: 70%; left: 30%; transform: translate(-50%, -50%);';
                  points[2].style.cssText = 'top: 70%; left: 70%; transform: translate(-50%, -50%);';
              }
         }
     }


    // Drag and Drop functionality
    substrates.forEach(substrate => {
        substrate.addEventListener('dragstart', (event) => {
            // Store substrate data and original index (to find it later)
            const substrateData = {
                shape: substrate.dataset.shape,
                colors: JSON.parse(substrate.dataset.colors || '[]') // Handle empty colors gracefully
            };
            event.dataTransfer.setData('text/plain', JSON.stringify(substrateData));
            event.dataTransfer.effectAllowed = 'copy';

             // Add a class to the dragged element to style it
             setTimeout(() => { // Use timeout to allow drag image to be created first
                 substrate.classList.add('dragging-substrate');
             }, 0);

             // Get the initial position of the dragged element in the viewport
             const subRect = substrate.getBoundingClientRect();
             // Store initial position as custom properties on the element being dragged
             // These will be used by the animation to start from the correct place
             substrate.style.setProperty('--start-dx', `${subRect.left}px`);
             substrate.style.setProperty('--start-dy', `${subRect.top}px`);
             // Temporarily make it fixed for animation control
              substrate.style.position = 'fixed';
              substrate.style.top = `${subRect.top}px`;
              substrate.style.left = `${subRect.left}px`;
              substrate.style.zIndex = '1000';

        });

         substrate.addEventListener('dragend', (event) => {
             // Remove dragging class and reset any animation styles
             const draggedSubstrate = event.target;
             draggedSubstrate.classList.remove('dragging-substrate', 'binding', 'no-binding');
             draggedSubstrate.style.transform = ''; // Reset transform
             draggedSubstrate.style.borderColor = ''; // Reset border color
              draggedSubstrate.style.boxShadow = ''; // Reset shadow
             // Reset position styles added at dragstart
             draggedSubstrate.style.position = '';
             draggedSubstrate.style.top = '';
             draggedSubstrate.style.left = '';
             draggedSubstrate.style.zIndex = '';
             // Clear custom properties
             draggedSubstrate.style.removeProperty('--start-dx');
             draggedSubstrate.style.removeProperty('--start-dy');
             draggedSubstrate.style.removeProperty('--end-dx');
             draggedSubstrate.style.removeProperty('--end-dy');


         });
    });

    enzymeArea.addEventListener('dragover', (event) => {
        event.preventDefault(); // Allow drop
        event.dataTransfer.dropEffect = 'copy';
        enzymeArea.classList.add('dragover'); // Visual cue
    });

    enzymeArea.addEventListener('dragleave', (event) => {
        enzymeArea.classList.remove('dragover'); // Reset visual cue
    });

     enzymeArea.addEventListener('drop', (event) => {
         event.preventDefault();
         enzymeArea.classList.remove('dragover'); // Reset visual cue

         const substrateData = JSON.parse(event.dataTransfer.getData('text/plain'));
         const activeSiteShape = shapeSelect.value;
         const activeSiteColors = activeSitePoints.map(p => p.color);

         // Find the original substrate element that was dragged
         // Need to find it by matching shape and colors data attributes
         const draggedSubstrateElement = Array.from(substrates).find(sub =>
             sub.dataset.shape === substrateData.shape &&
             JSON.stringify(JSON.parse(sub.dataset.colors || '[]').sort()) === JSON.stringify(substrateData.colors.sort()) // Compare sorted arrays
         );

         if (!draggedSubstrateElement) {
             // Should not happen if dragstart works correctly, but good safeguard
             console.error("Dragged substrate element not found in gallery!");
             return;
         }


         // --- Binding Logic Refined ---
         let shapeMatch = false;
         let colorMatchCount = 0;
         const totalSubstrateColors = substrateData.colors.length;
         const totalActiveSiteColors = activeSiteColors.length;

         // Check shape match
         if (substrateData.shape === activeSiteShape) {
             shapeMatch = true;
         } else if (activeSiteShape === 'pocket' && (substrateData.shape === 'square' || substrateData.shape === 'circle')) {
             // Simplified induced fit concept: pocket can partially fit square/circle
             shapeMatch = true; // Consider this a shape match for potential partial bind
         }

         // Check color point matches
         substrateData.colors.forEach(subColor => {
             if (activeSiteColors.includes(subColor)) {
                 colorMatchCount++;
             }
         });

         // Determine binding outcome and message based on refined levels
         let success = false;
         let message = '';
         let resultClass = ''; // For styling the message

         if (!shapeMatch) {
              success = false;
              resultClass = 'fail';
              if (colorMatchCount > 0) {
                 message = 'אין התאמה בצורה! למרות שיש דמיון בחלק מהתכונות.';
              } else {
                 message = 'אין התאמה בצורה וגם לא בתכונות.';
              }
         } else { // Shape matches or is a pocket partial match
             if (totalSubstrateColors === 0 && totalActiveSiteColors === 0) {
                 // Both have no points, shape match is a bind
                 success = true;
                 resultClass = 'success';
                 message = 'התאמה מושלמת בצורה! אין צורך בנקודות משיכה נוספות.';
             } else if (totalSubstrateColors > 0 && totalActiveSiteColors === 0) {
                 // Substrate has points, but active site doesn't
                 success = false; // Cannot bind if required features are missing in enzyme
                 resultClass = 'fail';
                 message = 'הצורה מתאימה, אבל לאנזים אין נקודות משיכה הנדרשות לסובסטרט זה.';
             } else if (totalSubstrateColors === 0 && totalActiveSiteColors > 0) {
                  // Active site has points, but substrate doesn't need them - still a bind if shape matches
                  success = true;
                  resultClass = 'partial'; // Maybe partial because points aren't used? Or just success? Let's say success.
                  resultClass = 'success';
                   message = 'הצורה מתאימה! האנזים יכול לקשור את הסובסטרט גם אם יש לו נקודות משיכה לא נחוצות כאן.';
             }
             else { // Both have points
                 if (colorMatchCount === totalSubstrateColors && totalSubstrateColors === totalActiveSiteColors && substrateData.shape === activeSiteShape) {
                      // Perfect match: shape, all substrate points match, same number of points
                      success = true;
                      resultClass = 'success';
                      message = 'קישור מושלם! הצורה וכל התכונות תואמות באופן מדויק!';
                 } else if (colorMatchCount === totalSubstrateColors) {
                      // Good match: shape, all substrate points match (active site may have more points)
                      success = true;
                      resultClass = 'success';
                       message = 'קישור מוצלח! יש התאמה בצורה וכל התכונות הנדרשות נמצאות.';
                 } else if (colorMatchCount > 0) {
                     // Partial match: shape, but only some points match
                     success = true; // Consider it a partial bind
                     resultClass = 'partial';
                     message = `קישור חלקי! הצורה מתאימה, ויש התאמה ב-${colorMatchCount} מתוך ${totalSubstrateColors} תכונות.`;
                 }
                 else { // Shape match, but 0 point matches
                      success = false;
                      resultClass = 'fail';
                      message = 'הצורה מתאימה, אך אף אחת מנקודות המשיכה אינה תואמת.';
                 }
             }
         }


         // Update message display
         resultMessage.textContent = message;
         resultMessage.className = 'result-message ' + resultClass;


         // Animate the original dragged substrate element
         // The element is already position: fixed from dragstart

         const enzymeRect = enzymeArea.getBoundingClientRect();
         const activeSiteRect = activeSite.getBoundingClientRect();

         // Calculate the target center position relative to the viewport
         const targetX = activeSiteRect.left + activeSiteRect.width / 2;
         const targetY = activeSiteRect.top + activeSiteRect.height / 2;

         // Calculate the distance from the start position (fixed position set in dragstart)
         const startX = parseFloat(draggedSubstrateElement.style.left);
         const startY = parseFloat(draggedSubstrateElement.style.top);

         const endDx = targetX - startX;
         const endDy = targetY - startY;

         // Set end position for animation
         draggedSubstrateElement.style.setProperty('--end-dx', `${endDx}px`);
         draggedSubstrateElement.style.setProperty('--end-dy', `${endDy}px`);


         // Remove previous animation classes and add the new one
         draggedSubstrateElement.classList.remove('binding', 'no-binding');
         // Force reflow to restart animation if needed
         void draggedSubstrateElement.offsetWidth;


         if (success) {
             draggedSubstrateElement.classList.add('binding');
              // Remove animation class and reset styles after animation completes
              draggedSubstrateElement.addEventListener('animationend', function handler() {
                   draggedSubstrateElement.removeEventListener('animationend', handler);
                    draggedSubstrateElement.style.position = '';
                    draggedSubstrateElement.style.top = '';
                    draggedSubstrateElement.style.left = '';
                    draggedSubstrateElement.style.zIndex = '';
                     draggedSubstrateElement.classList.remove('binding');
                    draggedSubstrateElement.style.transform = ''; // Ensure transform is reset
                     draggedSubstrateElement.style.boxShadow = ''; // Reset shadow
                     draggedSubstrateElement.style.borderColor = ''; // Reset border
               }, { once: true }); // Use { once: true } for automatic removal

         } else {
             draggedSubstrateElement.classList.add('no-binding');
              // Remove animation class and reset styles after animation completes
              draggedSubstrateElement.addEventListener('animationend', function handler() {
                   draggedSubstrateElement.removeEventListener('animationend', handler);
                    draggedSubstrateElement.style.position = '';
                    draggedSubstrateElement.style.top = '';
                    draggedSubstrateElement.style.left = '';
                    draggedSubstrateElement.style.zIndex = '';
                     draggedSubstrateElement.classList.remove('no-binding');
                     draggedSubstrateElement.style.transform = '';
                     draggedSubstrateElement.style.borderColor = ''; // Reset border color
                      draggedSubstrateElement.style.boxShadow = ''; // Reset shadow

               }, { once: true });
         }
     });

     // Explanation button logic
     explanationButton.addEventListener('click', () => {
         const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === '';
         explanationContent.style.display = isHidden ? 'block' : 'none';
         explanationButton.textContent = isHidden ? 'הסתר הסבר' : 'הצג/הסתר הסבר על אנזימים וסובסטרטים';
     });

</script>