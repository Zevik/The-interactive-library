---
title: "מסע מופלא: גלגול החרקים - סימולטור אינטראקטיבי"
english_slug: amazing-transformation-insect-metamorphosis-simulator
category: "ביולוגיה"
tags: ["חרקים", "גלגול", "מחזור חיים", "גלגול מלא", "גלגול חסר", "מטמורפוזה", "ביולוגיה התפתחותית"]
---
# מסע מופלא: גלגול החרקים

היצורים הזעירים שמסביבנו עוברים שינויים מדהימים במהלך חייהם! האם חשבתם פעם איך זחל קטן וזולל עלים הופך ליצור מעופף וצבעוני כמו פרפר? או איך ג'וק צעיר שונה אך מעט מהוריו הגדולים? מחזור החיים של חרקים הוא מסע של טרנספורמציה, והוא שונה באופן דרמטי בין קבוצות שונות. בואו נחקור את שני סוגי הגלגול העיקריים!

<div class="metamorphosis-simulator-container">
    <div class="metamorphosis-section complete-metamorphosis">
        <h2>גלגול מלא (Holometabola)</h2>
        <p>בחר חרק כדי לראות את המסע המדהים שלו:</p>
        <div class="insect-select">
            <label><input type="radio" name="complete_insect" value="פרפר" checked> פרפר</label>
            <label><input type="radio" name="complete_insect" value="חיפושית"> חיפושית</label>
        </div>
        <div class="stages-container" data-type="complete">
            <!-- Stages will be populated by JS -->
        </div>
        <div class="stage-info" data-type="complete">
            <!-- Stage info will be displayed here -->
        </div>
    </div>

    <div class="metamorphosis-section incomplete-metamorphosis">
        <h2>גלגול חסר (Hemimetabola)</h2>
        <p>בחר חרק ובחן את התפתחותו ההדרגתית:</p>
         <div class="insect-select">
            <label><input type="radio" name="incomplete_insect" value="חגב" checked> חגב</label>
            <label><input type="radio" name="incomplete_insect" value="מקק"> מקק</label>
        </div>
         <div class="stages-container" data-type="incomplete">
            <!-- Stages will be populated by JS -->
        </div>
        <div class="stage-info" data-type="incomplete">
            <!-- Stage info will be displayed here -->
        </div>
    </div>
</div>

<div class="controls">
    <button id="runSimulationBtn">הפעל מסע גלגול!</button>
</div>

<button id="toggleExplanationBtn">הצג/הסתר את סודות הגלגול</button>

<div id="explanation" class="explanation-section">
    <h2>מהו גלגול (מטמורפוזה) בחרקים?</h2>
    <p>גלגול הוא תהליך התפתחותי מופלא ודרמטי בו חרקים משנים את צורת גופם באופן יסודי לאחר הבקיעה מהביצה. תהליך זה מאפשר לחרקים הצעירים (זחלים או נימפות) להיות שונים מאוד מהבוגרים - לא רק במראה החיצוני, אלא גם במזון שהם אוכלים ובסביבת המחיה שלהם.</p>

    <h3>היתרונות האבולוציוניים של הגלגול</h3>
    <p>היתרון העיקרי של הגלגול הוא "חלוקת עבודה" אקולוגית בין הצעירים לבוגרים. הצעירים מתמקדים בעיקר באכילה מואצת ובגדילה, אוגרים אנרגיה וחומרים. הבוגרים, לעומת זאת, מתמקדים ברבייה ובהתפוצה (לרוב באמצעות תעופה). הפרדה זו מצמצמת תחרות על משאבים כמו מזון ומקום מחיה בין שלבי החיים השונים של אותו המין, ובכך מגדילה משמעותית את סיכויי ההישרדות וההצלחה של המין כולו.</p>

    <h2>גלגול מלא (Holometabola) - הטרנספורמציה המלאה</h2>
    <p>גלגול מלא הוא סוג הגלגול המרשים והמורכב ביותר, המאפיין את רובם המוחלט של מיני החרקים (כ-88%). הוא מורכב מארבעה שלבי חיים נפרדים, שונים לחלוטין זה מזה מבחינה מורפולוגית ואקולוגית:</p>
    <ul>
        <li><strong>ביצה:</strong> נקודת ההתחלה של המסע. לרוב מוטלת באופן אסטרטגי על או בסמוך למקור מזון עתידי עבור הזחל הבוקע.</li>
        <li><strong>זחל:</strong> שלב "מכונת האכילה" של החרק. הזחל מתמחה בגדילה מהירה, ושונה באופן דרמטי מהבוגר. אין לו כנפיים, עיניו פשוטות יחסית, והוא ניזון ממזון שונה לחלוטין (למשל, עלים לעומת צוף). הוא גדל באמצעות סדרה של "התנשלויות" - השלת השלד החיצוני הישן.</li>
        <li><strong>גולם (Pupa):</strong> שלב ה"מנוחה" החיצונית, אך בתוכו מתרחשת מהפכה ביולוגית מדהימה. רקמות הזחל מתפרקות כמעט לחלוטין, ונבנות מחדש לרקמות ומבנים של הבוגר. הגולם נראה דומם, אך הוא זירת שינוי פנימית עצומה. הוא יכול להיות מוגן בתוך פקעת (כמו אצל פרפרים), קבור בחומר, או חשוף, תלוי במין.</li>
        <li><strong>בוגר (Imago):</strong> התוצר הסופי של הטרנספורמציה. החרק הבוגר מגיח מהגולם, לרוב בעל כנפיים מפותחות המאפשרות תעופה, איברי רבייה בשלים, ומערכת עצבים מתקדמת יותר. תפקידו העיקרי הוא מציאת בן/בת זוג, רבייה והפצת המין. הבוגר יכול לאכול מזון שונה לחלוטין מהזחל, או לאכול כלל.</li>
    </ul>
    <p><strong>דוגמאות לחרקים בעלי גלגול מלא:</strong> עשירים בקבוצות כמו פרפרים ועשים, חיפושיות, זבובים ויתושים, ודבורים, צרעות ונמלים.</p>

    <h2>גלגול חסר (Hemimetabola) - ההתפתחות ההדרגתית</h2>
    <p>גלגול חסר הוא תהליך התפתחותי פשוט יותר, המאופיין בהתפתחות הדרגתית וכולל שלושה שלבי חיים עיקריים:</p>
    <ul>
        <li><strong>ביצה:</strong> גם כאן, זוהי נקודת ההתחלה.</li>
        <li><strong>נימפה (Nymph):</strong> הנימפה בוקעת מהביצה ו-הפתעה! - היא דומה באופן כללי לבוגר. היא קטנה יותר, לרוב חסרת כנפיים מפותחות (אם הבוגר מכונף), וחסרה איברי רבייה בשלים. הנימפה חיה לרוב באותה סביבה ואוכלת מזון דומה לבוגר. היא גדלה באמצעות סדרה של התנשלויות, ובכל התנשלות היא הופכת מעט גדולה יותר ומפתחת בהדרגה מאפיינים בוגרים יותר, כולל ניצני כנפיים הגדלים עד שהופכים לכנפיים מלאות בשלב הבוגר האחרון. אין שלב גולם.</li>
        <li><strong>בוגר (Imago):</strong> השלב הסופי. הבוגר מתפתח מהנימפה האחרונה, בעל כנפיים ואיברי רבייה מפותחים, ומוכן לרבייה.</li>
    </ul>
    <p>בשונה מגלגול מלא, המעבר מהנימפה לבוגר הוא הדרגתי ואין שלב מנוחה דרמטי הכולל ארגון מחדש נרחב של הגוף.</p>
     <p><strong>דוגמאות לחרקים בעלי גלגול חסר:</strong> חגבים, מקקים, שפיריות, בריומות, פשפשים, טרמיטים ועוד רבים.</p>

    <h2>הבדלים עיקריים - סיכום מהיר:</h2>
    <ul>
        <li><strong>מספר שלבים:</strong> גלגול מלא - 4 שלבים (ביצה, זחל, גולם, בוגר); גלגול חסר - 3 שלבים (ביצה, נימפה, בוגר).</li>
        <li><strong>נוכחות גולם:</strong> מאפיין בלעדי של גלגול מלא.</li>
        <li><strong>דמיון בין צעיר לבוגר:</strong> בגלגול מלא, הזחל שונה דרמטית מהבוגר. בגלגול חסר, הנימפה דומה לבוגר (מלבד גודל, כנפיים בשלות ואיברי רבייה).</li>
        <li><strong>תהליך השינוי:</strong> דרמטי וריכוזי בשלב הגולם בגלגול מלא; הדרגתי ומתמשך דרך סדרת התנשלויות בגלגול חסר.</li>
    </ul>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green */
        --primary-dark-color: #388E3C; /* Darker Green */
        --secondary-color: #FFC107; /* Amber */
        --background-color: #E8F5E9; /* Light Green Background */
        --card-background: #FFFFFF; /* White cards */
        --text-color: #212121; /* Dark Grey */
        --subtle-text-color: #757575; /* Grey */
        --border-color: #B9F6CA; /* Very Light Green */
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
    }

    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif; /* Use a common system font */
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 20px;
    }

    h1, h2, h3 {
        color: var(--primary-dark-color);
        text-align: center;
        margin-bottom: 20px;
    }

    h1 {
        font-size: 2.5em;
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: 10px;
        display: inline-block;
        margin-left: auto;
        margin-right: auto;
    }

    h2 {
        font-size: 1.8em;
        margin-top: 0;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    h3 {
        font-size: 1.3em;
        color: var(--primary-color);
        margin-bottom: 10px;
    }

    .metamorphosis-simulator-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
        margin-bottom: 30px;
        direction: rtl; /* Ensure right-to-left layout for Hebrew */
        justify-content: center; /* Center sections if flex-wrap occurs */
    }

    .metamorphosis-section {
        flex: 1;
        min-width: 300px;
        max-width: 500px; /* Limit max width for larger screens */
        background-color: var(--card-background);
        padding: 20px;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
        border: 1px solid var(--border-color);
    }

    .metamorphosis-section p {
        margin-bottom: 15px;
        font-weight: normal;
        color: var(--subtle-text-color);
        font-size: 1em;
    }

     .insect-select {
         margin-bottom: 15px;
         display: flex;
         gap: 15px;
         align-items: center;
     }

     .insect-select label {
         font-weight: bold;
         cursor: pointer;
         color: var(--text-color);
         transition: color 0.2s ease;
     }

     .insect-select label:hover {
        color: var(--primary-dark-color);
     }

     .insect-select input[type="radio"] {
         margin-left: 5px; /* Adjust for RTL */
         accent-color: var(--primary-color); /* Style the radio button */
     }


    .stages-container {
        display: flex;
        justify-content: space-around;
        align-items: flex-start; /* Align stages to top */
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid var(--border-color);
        flex-grow: 1; /* Allow container to fill space */
    }

    .stage {
        text-align: center;
        cursor: pointer;
        padding: 10px 5px;
        border-radius: 8px;
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.2s ease;
        flex-shrink: 0;
        width: 80px; /* Fixed width for stages */
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative; /* Needed for ::after */
    }

    .stage::after {
        content: '';
        position: absolute;
        bottom: -10px; /* Position below the stage */
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background-color: var(--primary-color);
        transition: width 0.3s ease;
    }

    .stage:hover {
        background-color: #e0f2f7; /* Light blue-green on hover */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .stage.active {
        background-color: #c8e6c9; /* Light green when active */
        font-weight: bold;
        color: var(--primary-dark-color);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    .stage.active::after {
         width: 80%; /* Underline active stage */
    }

     .stage.simulating {
         animation: pulse 1.5s infinite ease-in-out;
         border: 2px solid var(--primary-color);
         box-shadow: 0 0 15px var(--primary-color);
     }

     @keyframes pulse {
         0% { transform: scale(1); box-shadow: 0 0 10px var(--primary-color); }
         50% { transform: scale(1.05); box-shadow: 0 0 20px var(--primary-color); }
         100% { transform: scale(1); box-shadow: 0 0 10px var(--primary-color); }
     }


    .stage img {
        display: block;
        margin: 0 auto 8px;
        width: 60px; /* Adjusted size */
        height: 60px;
        object-fit: cover; /* Use cover to ensure placeholder text is visible */
        border-radius: 50%; /* Make images round */
        border: 2px solid var(--border-color);
        background-color: #f0f0f0; /* Grey background for placeholders */
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    }

    .stage-name {
        font-size: 0.9em;
        color: var(--text-color);
    }

    .stage-info {
        border-top: 1px solid var(--border-color);
        padding-top: 15px;
        min-height: 100px; /* Ensure space is reserved */
        font-size: 0.95em;
        color: var(--subtle-text-color);
    }

    .stage-info h3 {
        margin-top: 0;
        font-size: 1.2em;
        color: var(--primary-dark-color);
        margin-bottom: 8px;
    }

    .stage-info p {
        margin-bottom: 8px;
        font-weight: normal;
    }

    .controls {
        text-align: center;
        margin-bottom: 30px;
    }

    .controls button {
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: var(--shadow);
    }

    .controls button:hover {
        background-color: var(--primary-dark-color);
        transform: translateY(-2px);
    }

     .controls button:active {
         transform: translateY(0);
         box-shadow: none;
     }


    #toggleExplanationBtn {
         display: block; /* Make it a block button */
         width: fit-content; /* Fit content width */
         margin: 20px auto; /* Center the button */
         padding: 10px 20px;
         font-size: 1em;
         cursor: pointer;
         background-color: var(--subtle-text-color);
         color: white;
         border: none;
         border-radius: 20px;
         transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: var(--shadow);
    }

    #toggleExplanationBtn:hover {
         background-color: #5a6268;
         transform: translateY(-1px);
    }
     #toggleExplanationBtn:active {
         transform: translateY(0);
         box-shadow: none;
     }


    .explanation-section {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--card-background);
        box-shadow: var(--shadow);
        display: none; /* Initially hidden */
    }

    .explanation-section p {
        margin-bottom: 15px;
        line-height: 1.7;
        color: var(--text-color);
    }

     .explanation-section ul {
         margin-bottom: 15px;
         padding-right: 20px; /* Adjust padding for RTL */
     }

     .explanation-section li {
         margin-bottom: 8px;
     }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .metamorphosis-simulator-container {
            flex-direction: column;
            align-items: center;
        }

        .metamorphosis-section {
            min-width: 95%; /* Allow sections to take more width on smaller screens */
            max-width: 95%;
        }

        .stages-container {
             flex-wrap: wrap; /* Allow stages to wrap if too many */
             justify-content: center;
        }

        .stage {
            width: 60px; /* Smaller width for stages */
        }

        .stage img {
            width: 45px; /* Smaller images */
            height: 45px;
        }

         h1 {
             font-size: 2em;
         }

         h2 {
             font-size: 1.5em;
         }
    }

</style>

<script>
    const insectsData = {
        complete: {
            "פרפר": [
                { name: "ביצה", desc: "המסע מתחיל כאן! ביצים זעירות מוטלות על צמח המזון של הזחל.", duration: "מספר ימים עד שבועות", img: "https://via.placeholder.com/60x60?text=ביצת+פרפר" }, // Placeholder images
                { name: "זחל", desc: "שלב ה"מכונה אוכלת"! הזחל גדל במהירות, משיל את עורו מספר פעמים (התנשלויות).", duration: "שבועות עד חודשים", img: "https://via.placeholder.com/60x60?text=זחל+פרפר" },
                { name: "גולם", desc: "השינוי המסתורי. בתוך הגולם מתרחשת טרנספורמציה מוחלטת מזחל לבוגר.", duration: "שבועות עד חודשים", img: "https://via.placeholder.com/60x60?text=גולם+פרפר" },
                { name: "בוגר", desc: "פרפר יפהפה מגיח מהגולם, מוכן לרבייה ולהפצת המין. תפקידו העיקרי - למצוא בן/בת זוג.", duration: "ימים עד שבועות ספורים", img: "https://via.placeholder.com/60x60?text=פרפר+בוגר" }
            ],
            "חיפושית": [
                { name: "ביצה", desc: "השלב ההתחלתי, מוטלת לרוב בסביבת מזון מתאימה.", duration: "מספר ימים עד שבועות", img: "https://via.placeholder.com/60x60?text=ביצת+חיפושית" },
                { name: "זחל", desc: "שלב האכילה האינטנסיבית. זחלי חיפושיות מגוונים מאוד בצורתם, לעיתים מכונים 'רימות'.", duration: "חודשים, ולעיתים אף שנים!", img: "https://via.placeholder.com/60x60?text=זחל+חיפושית" },
                { name: "גולם", desc: "שלב הטרנספורמציה, לעיתים בתוך מעריסת הגנה באדמה או בעץ.", duration: "שבועות עד חודשים", img: "https://via.placeholder.com/60x60?text=גולם+חיפושית" },
                { name: "בוגר", desc: "החיפושית הבוגרת יוצאת, מוכנה לרבייה. לעיתים היא גם אוכלת מזון שונה מהזחל.", duration: "חודשים עד שנה ויותר", img: "https://via.placeholder.com/60x60?text=חיפושית+בוגרת" }
            ]
        },
        incomplete: {
            "חגב": [
                { name: "ביצה", desc: "מוטלת במקבצים (תרמילים) באדמה, מוגנים מהסביבה.", duration: "שבועות עד חודשים (לעיתים עובר את החורף)", img: "https://via.placeholder.com/60x60?text=ביצת+חגב" },
                { name: "נימפה", desc: "דומה לחגב בוגר אך קטנה, חסרת כנפיים מפותחות ואיברי רבייה בשלים. גדלה דרך התנשלויות הדרגתיות.", duration: "שבועות עד חודשים", img: "https://via.placeholder.com/60x60?text=נימפת+חגב" },
                { name: "בוגר", desc: "החגב הגיע לבגרות מינית, בעל כנפיים מפותחות (לרוב). מוכן לרבייה.", duration: "שבועות עד חודשים", img: "https://via.placeholder.com/60x60?text=חגב+בוגר" }
            ],
            "מקק": [
                 { name: "ביצה", desc: "מוטלת בתוך תיק ביצים (אוטקה) קשיח ומגן.", duration: "שבועות", img: "https://via.placeholder.com/60x60?text=ביצת+מקק" },
                 { name: "נימפה", desc: "מקק צעיר, נראה כמו הבוגר אך קטן יותר, בהיר יותר, וחסר כנפיים. עובר מספר התנשלויות.", duration: "חודשים עד שנה ויותר", img: "https://via.placeholder.com/60x60?text=נימפת+מקק" },
                 { name: "בוגר", desc: "מקק בוגר, בעל כנפיים (לעיתים), ומוכן לרבייה. ניזון ממגוון מזונות.", duration: "חודשים עד שנה", img: "https://via.placeholder.com/60x60?text=מקק+בוגר" }
            ]
        }
    };

    let simulationInterval = null;
    let currentSimulationIndices = { complete: 0, incomplete: 0 }; // Track current stage for simulation

    function renderStages(type) {
        const selectedInsectName = document.querySelector(`input[name="${type}_insect"]:checked`).value;
        const stages = insectsData[type][selectedInsectName];
        const container = document.querySelector(`.stages-container[data-type="${type}"]`);
        container.innerHTML = ''; // Clear current stages

        if (!stages) {
             console.error(`No stages data found for type: ${type}, insect: ${selectedInsectName}`);
             return;
        }

        stages.forEach((stage, index) => {
            const stageElement = document.createElement('div');
            stageElement.classList.add('stage');
            stageElement.dataset.index = index;
            stageElement.dataset.type = type;
            stageElement.setAttribute('aria-label', `שלב: ${stage.name} של ${selectedInsectName}`); // Accessibility
            stageElement.innerHTML = `
                <img src="${stage.img}" alt="איור של ${stage.name} ${selectedInsectName}">
                <div class="stage-name">${stage.name}</div>
            `;
            // Use an anonymous function to pass parameters correctly to event listener
            stageElement.addEventListener('click', () => {
                stopSimulation(); // Stop simulation on manual click
                displayStageInfo(type, index);
            });
            container.appendChild(stageElement);
        });

        // Reset and display info for the first stage initially
        currentSimulationIndices[type] = 0;
        displayStageInfo(type, 0);
    }

    function displayStageInfo(type, index) {
        const selectedInsectName = document.querySelector(`input[name="${type}_insect"]:checked`).value;
        const stages = insectsData[type][selectedInsectName];
        const infoContainer = document.querySelector(`.stage-info[data-type="${type}"]`);
        const stagesElements = document.querySelectorAll(`.stages-container[data-type="${type}"] .stage`);

        // Remove active & simulating classes from all stages in this section
        stagesElements.forEach(el => {
             el.classList.remove('active');
             el.classList.remove('simulating'); // Ensure simulating class is removed on manual click
        });

        // Add active class to the selected stage
        if (stagesElements[index]) {
             stagesElements[index].classList.add('active');
        }

        // Display info
        if (stages && stages[index]) {
            const stage = stages[index];
            infoContainer.innerHTML = `
                <h3>${stage.name}</h3>
                <p>${stage.desc}</p>
                <p><strong>משך השלב:</strong> ${stage.duration}</p>
            `;
        } else {
             infoContainer.innerHTML = `<p>לחץ על שלב במסע הגלגול כדי ללמוד עליו!</p>`;
        }
    }

    function runSimulation() {
        stopSimulation(); // Stop any existing simulation first

        const types = ['complete', 'incomplete'];
        const simulationSpeed = 1500; // milliseconds per stage

        // Reset indices to start from the beginning
        currentSimulationIndices = { complete: 0, incomplete: 0 };

        // Function to advance the simulation by one step for both types
        function nextStep() {
            let allFinished = true; // Flag to check if all simulations are done

            types.forEach(type => {
                const selectedInsectName = document.querySelector(`input[name="${type}_insect"]:checked`).value;
                const stages = insectsData[type][selectedInsectName];
                 const stagesElements = document.querySelectorAll(`.stages-container[data-type="${type}"] .stage`);

                if (!stages || stages.length === 0) {
                    return; // Skip if no data for this type/insect
                }

                // Remove simulating class from previous stage
                 if (currentSimulationIndices[type] > 0 && stagesElements[currentSimulationIndices[type] - 1]) {
                     stagesElements[currentSimulationIndices[type] - 1].classList.remove('simulating');
                 }

                // Check if there's a next stage for this type
                if (currentSimulationIndices[type] < stages.length) {
                    // Display info and highlight the current stage
                    displayStageInfo(type, currentSimulationIndices[type]);
                    if (stagesElements[currentSimulationIndices[type]]) {
                        stagesElements[currentSimulationIndices[type]].classList.add('simulating'); // Add simulating class
                    }
                    currentSimulationIndices[type]++; // Move to the next stage index
                    allFinished = false; // At least one simulation is still running
                } else {
                    // If finished, ensure the last stage is still active but not simulating
                    if (stagesElements[stages.length - 1]) {
                        stagesElements[stages.length - 1].classList.remove('simulating');
                        stagesElements[stages.length - 1].classList.add('active'); // Keep last stage active
                    }
                     // Optionally, display a "Finished" message
                     // const infoContainer = document.querySelector(`.stage-info[data-type="${type}"]`);
                     // infoContainer.innerHTML += "<p>הגלגול הושלם!</p>";
                }
            });

            // If all simulations have finished their stages, stop the interval
            if (allFinished) {
                stopSimulation();
                 document.getElementById('runSimulationBtn').textContent = 'התחל מסע מחדש!'; // Change button text
                 document.getElementById('runSimulationBtn').classList.add('reset'); // Optional: Add a class for styling reset state
            }
        }

         // Run the first step immediately before starting the interval
        nextStep();

         // Start the interval only if there are stages to show in at least one type initially
        const hasStagesToStart = types.some(type => {
            const selectedInsectName = document.querySelector(`input[name="${type}_insect"]:checked`).value;
            return insectsData[type][selectedInsectName] && insectsData[type][selectedInsectName].length > 0;
        });

        if (hasStagesToStart && !allFinishedInitially()) { // Check if simulation didn't finish on the first step
             simulationInterval = setInterval(nextStep, simulationSpeed);
             document.getElementById('runSimulationBtn').textContent = 'במהלך מסע...'; // Change button text
              document.getElementById('runSimulationBtn').classList.remove('reset');
        } else if (allFinishedInitially()) {
             // If simulation finishes on the first step (e.g., no stages or only 1), update button text
            document.getElementById('runSimulationBtn').textContent = 'מסע קצרצר הושלם!';
             document.getElementById('runSimulationBtn').classList.add('reset');
        }

         function allFinishedInitially() {
             return types.every(type => {
                 const selectedInsectName = document.querySelector(`input[name="${type}_insect"]:checked`).value;
                 const stages = insectsData[type][selectedInsectName];
                 return !stages || currentSimulationIndices[type] >= stages.length;
             });
         }
    }


    function stopSimulation() {
        if (simulationInterval) {
            clearInterval(simulationInterval);
            simulationInterval = null;
        }
         // Remove simulating class from any stages that might still have it
        document.querySelectorAll('.stage').forEach(el => el.classList.remove('simulating'));
         document.getElementById('runSimulationBtn').textContent = 'הפעל מסע גלגול!'; // Reset button text
         document.getElementById('runSimulationBtn').classList.remove('reset');
         // Keep the last active stage highlighted by displayStageInfo, do not reset all to inactive unless explicitly needed.
    }


    function toggleExplanation() {
        const explanationDiv = document.getElementById('explanation');
        const button = document.getElementById('toggleExplanationBtn');
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';

        if (isHidden) {
            explanationDiv.style.display = 'block';
            button.textContent = 'הסתר את סודות הגלגול';
        } else {
            explanationDiv.style.display = 'none';
            button.textContent = 'הצג/הסתר את סודות הגלגול';
        }
    }

    // Initialize the simulator
    document.addEventListener('DOMContentLoaded', () => {
        // Initial rendering of stages for both types
        renderStages('complete');
        renderStages('incomplete');

        // Add event listeners for insect selection changes
        document.querySelectorAll('input[name="complete_insect"]').forEach(radio => {
            radio.addEventListener('change', () => {
                stopSimulation(); // Stop simulation when insect changes
                renderStages('complete'); // Re-render stages for the new insect
            });
        });
         document.querySelectorAll('input[name="incomplete_insect"]').forEach(radio => {
            radio.addEventListener('change', () => {
                stopSimulation(); // Stop simulation when insect changes
                renderStages('incomplete'); // Re-render stages for the new insect
            });
        });


        // Add event listener for the Run button
        document.getElementById('runSimulationBtn').addEventListener('click', runSimulation);

        // Add event listener for explanation toggle button
        document.getElementById('toggleExplanationBtn').addEventListener('click', toggleExplanation);

        // Ensure explanation is hidden on load - controlled by CSS initially
        // const explanationDiv = document.getElementById('explanation');
        // if (explanationDiv) {
        //     explanationDiv.style.display = 'none'; // Explicitly hide using JS too for toggle state
        // }
    });

</script>
```