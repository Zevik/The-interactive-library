---
title: "מהצמח למדף: המסע המופלא של הסוכר"
english_slug: from-plant-to-shelf-the-wonderful-journey-of-sugar
category: "מדעי החיים / מדעי המזון"
tags:
  - סוכר
  - הפקת סוכר
  - תעשייה
  - כימיה
  - חקלאות
---

**המסע המדהים של הסוכר: מהשדה אל הכפית שלכם!**

איך קורה הקסם? צמחים כמו קנה סוכר או סלק סוכר, שנראים כל כך שונים, הופכים לאותם גבישים לבנים ומתוקים שכולנו מכירים? בואו נצא למסע אינטראקטיבי מרתק ונלמד על תהליך הפקת הסוכר התעשייתי - צעד אחר צעד.

<div id="sugar-journey-app">
    <div id="raw-material-select">
        <h2>איזו הרפתקה נבחר?</h2>
        <p>הצטרפו למסע הסוכר דרך...</p>
        <button id="select-cane">
            <img src="https://via.placeholder.com/60x80?text=קנה+סוכר" alt="קנה סוכר">
            קנה סוכר
        </button>
        <button id="select-beet">
             <img src="https://via.placeholder.com/60x80?text=סלק+סוכר" alt="סלק סוכר">
            סלק סוכר
        </button>
    </div>

    <div id="stage-display">
         <div id="process-line">
            <!-- Visual representation of the factory process -->
             <div class="process-segment field"></div>
             <div class="process-segment factory-entrance"></div>
             <div class="process-segment extraction"></div>
             <div class="process-segment purification"></div>
             <div class="process-segment evaporation"></div>
             <div class="process-segment crystallization"></div>
             <div class="process-segment separation"></div>
             <div class="process-segment drying"></div>
             <div class="process-segment packaging"></div>
             <div class="process-segment shelf"></div>
         </div>
        <div id="animation-area">
             <!-- The material representation will move along the process-line -->
            <div id="material-representation"></div>
        </div>
        <div id="stage-info">
             <div id="current-stage-name"></div>
            <div id="current-stage-description"></div>
        </div>
    </div>

    <div id="stage-navigation">
        <button id="prev-stage" disabled>שלב קודם</button>
        <div id="stage-progress">
            <!-- Stage indicators will be added here by JS -->
        </div>
        <button id="next-stage">שלב הבא</button>
    </div>

     <button id="back-to-selection" style="display: none;">בחירת חומר גלם מחדש</button>
</div>

<button id="toggle-explanation" class="toggle-btn">הצג/הסתר הסבר מפורט</button>

<div id="detailed-explanation" style="display: none;">
    <h2>המסע המופלא של הסוכר: הצלילה לעומק</h2>

    <h3>חומרי הגלם - גיבורי הסיפור:</h3>
    <p>מאחורי כל גרגיר סוכר מסתתר סיפורו של צמח. גיבורינו הראשיים הם **קנה הסוכר** (Saccharum officinarum), ענק ירוק הטופח באקלים טרופי חם ולח, ו**סלק הסוכר** (Beta vulgaris), שורש עגול הגדל באזורים ממוזגים. על אף השוני הדרמטי במראה ובאקלים הגידול, שניהם אוגרים ביעילות מדהימה כמויות גדולות של סוכרוז - המולקולה המתוקה שאנחנו מחפשים. קנה הסוכר אוגר אותו בגבעולו העסיסי, ואילו סלק הסוכר מתרכז באגירתו בשורש הבשרני שלו.</p>

    <h3>מתחילים בשדה - הקציר:</h3>
    <p>המסע מתחיל באדמה הפורייה. קנה הסוכר נאסף לרוב לאחר שריפה מבוקרת המסירה את העלים היבשים ומקלה על הקציר המכני. סלק הסוכר פשוט נעקר בעדינות מהאדמה. המהירות חיונית בשלב זה! חומר הגלם חייב להגיע למפעל במהירות הבזק כדי למנוע אובדן סוכר יקר מפז, שעלול "להיעלם" בתהליכי נשימה טבעיים של התאים או כתוצאה מפעילות של מיקרואורגניזמים זעירים. עם ההגעה למפעל, מטען היבול עובר שטיפה יסודית - אמבטיה גדולה שמסירה בוץ, אבנים ושאר אורחים לא רצויים מהשדה.</p>

    <h3>מיצוי הזהב המתוק - שלב ההפרדה הראשוני:</h3>
    <p>המטרה כאן ברורה: לחלץ את הסוכרוז מתוך המסה הצמחית הסיבית. דרך הפעולה משתנה בהתאם לחומר הגלם:</p>
    <ul>
        <li>**קנה סוכר:** הגבעולים עוברים מסע דרך סדרת מכונות ריסוק וסחיטה עצומות (Mills). המכונות הללו כמו סוחטות את המיץ עד טיפת הסוכר האחרונה. לעיתים, מקלחת של מים חמים (שיטת המצננת) עוזרת "לשכנע" עוד סוכר לעזוב את הסיבים ולהצטרף למיץ.</li>
        <li>**סלק סוכר:** שורשי הסלק נפרסים לשבבים דקים דקים, ממש כמו פתיתי תירס ענקיים, הנקראים "קוסקטים". שבבים אלו עוברים שחייה בבריכות מיצוי ענקיות בהן מוזרמים מים חמים. בתהליך קסום הנקרא **דיפוזיה**, הסוכר נע בטבעיות מתוך תאי הצמח אל המים החמים.</li>
    </ul>
    בסיום שלב זה, אנו נשארים עם "מיץ גולמי" - תערובת עשירה בסוכרוז... אבל גם מלאה במזהמים שונים שנדבקו מהצמח ומהאדמה.</p>

    <h3>ניקוי יסודי - הופכים את המיץ לצלול:</h3>
    <p>המיץ הגולמי הוא אמנם מתוק, אך גם עכור ומלוכלך. הוא מכיל חלבונים, פקטינים, מינרלים ואפילו צבענים טבעיים שאינם סוכר. כדי להגיע לגבישי סוכר לבנים וטהורים, נדרש תהליך ניקוי יסודי ומתוחכם:</p>
    <ol>
        <li>**"אמבטיית סיד" (ריכוך - Liming):** מוסיפים חומר קסום הנקרא סידן הידרוקסיד (או בקיצור, סיד). הסיד גורם לחלק מהמזהמים לשקוע כמו בוצה, ולחלבונים להתקבץ יחד.</li>
        <li>**"בועות מנקות" (קרבונטציה/סולפיטציה):** כעת מזרימים גז - פחמן דו-חמצני לסלק סוכר (קרבונטציה) או גופרית דו-חמצנית לקנה סוכר (סולפיטציה). הגז גורם לסיד העודף לשקוע יחד עם מזהמים נוספים שנדבקו אליו, ויוצר "פתיתי לכלוך" גדולים יותר.</li>
        <li>**"זמן שקיעה" (צלילה - Settling/Clarification):** המיץ המטופל נח במכלים ענקיים. כוח הכבידה עושה את שלו - ה"פתיתים" המלוכלכים שוקעים לתחתית כ"בוצה", ואילו המיץ הנקי יותר, קל יותר, צף למעלה.</li>
        <li>**סינון אחרון (Filtration):** המיץ ה"צף" עובר מסננת אחרונה ויעילה שמבטיחה שגם שאריות המוצקים הקטנות ביותר יוסרו. עכשיו יש לנו "מיץ צלול" - שקוף ונקי כמעט לחלוטין.</li>
    </ol>

    <h3>הופכים לנוזל זהוב - אידוי וריכוז:</h3>
    <p>המיץ הצלול עדיין דליל יחסית (כ-85% ממנו הם מים!). כדי לגבש סוכר, עלינו לרכז אותו משמעותית. התהליך מתרחש ב"מגדלי אידוי" (Multiple Effect Evaporators) - סדרת מכלי ענק הפועלים בוואקום. הוואקום הוא קריטי - הוא מאפשר למים לרתוח ולהתאדות בטמפרטורות נמוכות יותר. זהו מהלך מבריק שחוסך אנרגיה יקרה ומונע מהסוכר המתוק שלנו להתפרק מחום גבוה מדי. בסיום שלב זה, אנו מקבלים נוזל סמיך ומתוק - "סירופ".</p>

    <h3>לידת הגבישים - קריסטליזציה:</h3>
    <p>הסירופ המרוכז נכנס למכלי ואקום מיוחדים הנקראים "וואקום פאן" (Vacuum Pans). כאן, בתנאים מבוקרים בקפידה, ממשיכים לאדות מים. כשהסירופ הופך סמיך ועשיר במיוחד בסוכר (מצב הנקרא על-רוויה), מוסיפים "זרעי קריסטליזציה" - גבישי סוכר זעירים ביותר. גבישים זעירים אלו הם כמו "מגנטים" - הסוכר שבתמיסה נדבק אליהם ו"בונה" אותם לגבישים גדולים יותר ויותר, ככל שמים נוספים מתאדים. זהו שלב אמנותי כמעט, הדורש בקרת טמפרטורה וריכוז מדויקות כדי לגדל את הגבישים בדיוק בגודל ובצורה הרצויים לנו.</p>

    <h3>הפרדת כוחות - הסוכר והמולסה נפרדים:</h3>
    <p>לאחר שהגבישים גדלו מספיק, אנו נשארים עם תערובת של גבישי סוכר מוצקים ושיירי סירופ כהה וצמיג שנותר מסביבם - ה"מולסה" (Molasses). כדי להפריד ביניהם, משתמשים במכונות "מערבולת" ענקיות הנקראות צנטריפוגות. הצנטריפוגות מסתובבות במהירות מסחררת. כוח הצנטריפוגלי העצום דוחף את המולסה הנוזלית החוצה דרך מסננת דקה, בעוד שגבישי הסוכר המוצקים והכבדים יותר נשארים בתוך התוף המסתובב.</p>

    <h3>טאץ' אחרון - ייבוש וקירור:</h3>
    <p>גבישי הסוכר שיצאו מהצנטריפוגה עדיין לחים מעט. ייבוש סופי הכרחי כדי להבטיח שהסוכר לא יידבק ויתגבש שוב בגושים גדולים, וכדי לאפשר אחסון ארוך טווח ללא חשש מקלקול. הגבישים עוברים דרך מייבשי אוויר חם (כמו סרט נע של אוויר חם או תוף מסתובב) המפחיתים את הלחות לרמה זניחה. לאחר מכן, הם מקוררים כדי להתייצב.</p>

    <h3>מוכנים למדף - בקרת איכות ואריזה:</h3>
    <p>רגע לפני היציאה למסע אל הצרכן, הסוכר עובר בדיקות מחמירות. בודקים את טוהרו, גודל הגבישים, הצבע הלבן בוהק, ורמת הלחות. רק סוכר שעומד בכל התקנים נחשב ל"סוכר לבן" איכותי ומוכן לאריזה. הוא נארז במגוון אריזות, משקיות קטנות לשימוש ביתי ועד שקים ענקיים או בתפזורת לתעשייה, ומוכן לצאת למסע האחרון - אל המדפים בחנויות ואל המטבח שלכם!</p>

    <h3>חיים שניים - תוצרי הלוואי:</h3>
    <p>מסע הסוכר מותיר אחריו גם אוצרות נוספים, תוצרי לוואי יקרי ערך המקבלים חיים שניים בתעשיות אחרות:
    <ul>
        <li>**מולסה:** הנוזל הכהה שנותר לאחר הפרדת הסוכר. היא עשירה בסוכרים (אך לא סוכרוז טהור) ומינרלים. משמשת במגוון רחב של יישומים: בסיס לייצור רום, מרכיב חשוב בייצור שמרים, מזון מזין לבעלי חיים, ואף חומר גלם בתעשייה הכימית.</li>
        <li>**בגאס (Bagasse):** הסיבים הנותרים מקנה הסוכר אחרי הסחיטה. זהו דלק טבעי ואנרגטי במיוחד! במפעלים רבים, שורפים את הבגאס כדי ליצור קיטור ואנרגיה המניעים את המפעל כולו - מעגל אנרגטי יעיל וירוק. הוא משמש גם לייצור נייר וחומרי בניין.</li>
        <li>**פאלפ סלק:** שאריות שבבי סלק הסוכר לאחר תהליך הדיפוזיה. גם הוא משמש בעיקר כמזון איכותי ומזין לבעלי חיים.</li>
        <li>**בוצה (Filter Cake):** המשקעים והמוצקים שהופרדו בשלבי הטיהור. לעיתים קרובות מוצאת את דרכה חזרה לשדות, ומשמשת כדשן טבעי המחזיר לאדמה חומרים מזינים.</li>
    </ul></p>

    <h3>קצת כימיה - מולקולת הפלא:</h3>
    <p>סוכרוז (Sucrose) הוא הגיבור הכימי הראשי. זוהי מולקולה מורכבת יחסית, דו-סוכר, הנוצרת מחיבור של שתי מולקולות סוכר פשוטות יותר: גלוקוז ופרוקטוז, המחוברות יחד בקשר כימי מיוחד (קשר גליקוזידי). הנוסחה הכימית שלה היא C₁₂H₂₂O₁₁. כל תהליך ההפקה נועד לבודד את המולקולה המיוחדת הזו, להפריד אותה מכל שאר החומרים שבצמח, ולגבש אותה לגבישים הטהורים והמוכרים. תהליכי הניקוי מסירים את כל מה שאינו סוכרוז, ותהליכי האידוי והגיבוש מנצלים את התכונות הייחודיות של הסוכרוז - מסיסותו הגבוהה במים ויכולתו להתגבש לגבישים בתנאים מדויקים. אתגר מרכזי בתהליך הוא למנוע את פירוק הסוכרוז (הידרוליזה) חזרה לגלוקוז ופרוקטוז, פירוק שיכול לקרות אם התנאים (חום, חומציות) אינם נשלטים בקפידה.</p>
</div>

<style>
/* --- General App Styling --- */
#sugar-journey-app {
    font-family: 'Arial', sans-serif; /* More standard font */
    direction: rtl;
    text-align: right;
    margin: 20px auto;
    padding: 30px; /* More padding */
    border: none; /* Remove default border */
    border-radius: 15px; /* More rounded corners */
    max-width: 900px; /* Wider container */
    background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2); /* Soft gradient background */
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* More pronounced shadow */
    color: #333; /* Darker text color */
    overflow: hidden; /* Ensure internal elements don't overflow */
}

h2 {
    color: #004d40; /* Teal color for headings */
    text-align: center;
    margin-bottom: 25px;
    font-size: 1.8em; /* Larger main heading */
}

/* --- Raw Material Selection Screen --- */
#raw-material-select {
    text-align: center;
    padding: 40px 20px; /* More internal padding */
    background-color: #ffffff; /* White background */
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

#raw-material-select p {
    font-size: 1.1em;
    color: #555;
    margin-bottom: 30px;
}

#raw-material-select button {
    display: inline-flex; /* Align image and text */
    flex-direction: column; /* Stack image and text */
    align-items: center;
    padding: 20px 30px; /* Larger clickable area */
    margin: 0 15px; /* More space between buttons */
    cursor: pointer;
    border: 2px solid #00796b; /* Teal border */
    border-radius: 10px;
    background-color: #ffffff;
    color: #00796b;
    font-size: 1.2em; /* Larger font */
    font-weight: bold;
    transition: background-color 0.3s ease, color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
    min-width: 150px; /* Minimum width */
}

#raw-material-select button img {
     display: block;
     margin-bottom: 10px; /* Space between image and text */
     border-radius: 5px;
     object-fit: cover; /* Cover the image area */
     box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}


#raw-material-select button.selected,
#raw-material-select button:hover {
    background-color: #00796b; /* Teal background on hover/selected */
    color: #ffffff; /* White text on hover/selected */
    transform: translateY(-5px); /* Lift effect on hover */
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); /* Stronger shadow on hover */
}

/* --- Stage Display (after selection) --- */
#stage-display {
    margin-bottom: 30px;
    min-height: 450px; /* Ensure enough space for animation */
    display: flex;
    flex-direction: column; /* Stack elements */
    align-items: center;
    justify-content: space-between; /* Distribute space */
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    position: relative; /* For positioning process line and material */
}

#process-line {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 20px; /* Thickness of the line */
    display: flex;
    justify-content: space-between; /* Distribute segments */
    align-items: center;
    z-index: 1; /* Below material representation */
}

.process-segment {
    flex-grow: 1; /* Each segment takes equal space */
    height: 100%;
    background-color: #e0e0e0; /* Default gray color */
    position: relative;
    margin: 0 2px; /* Small gap between segments */
    border-radius: 5px; /* Slightly rounded segments */
}

.process-segment:first-child { margin-right: 2px;}
.process-segment:last-child { margin-left: 2px; }


/* Specific segment styling to hint at the process */
.process-segment.field { background-color: #8bc34a; } /* Green */
.process-segment.factory-entrance { background-color: #795548; } /* Brown */
.process-segment.extraction { background-color: #ff9800; } /* Orange */
.process-segment.purification { background-color: #2196f3; } /* Blue */
.process-segment.evaporation { background-color: #ffeb3b; } /* Yellow */
.process-segment.crystallization { background-color: #e1bee7; } /* Light Purple */
.process-segment.separation { background-color: #00bcd4; } /* Cyan */
.process-segment.drying { background-color: #fbc02d; } /* Dark Yellow */
.process-segment.packaging { background-color: #4caf50; } /* Dark Green */
.process-segment.shelf { background-color: #9e9e9e; } /* Gray */


#animation-area {
    width: 100%;
    height: 120px; /* Height for the animation */
    position: relative;
    margin-bottom: 20px;
    display: flex;
    justify-content: center; /* Initially center */
    align-items: center; /* Initially center */
    z-index: 2; /* Above the process line */
    /* The materialRepresentation will move within this area, positioned absolutely relative to it */
}

#material-representation {
    position: absolute;
    width: 50px; /* Larger initial size */
    height: 50px; /* Larger initial size */
    background-color: #795548; /* Initial brown color */
    border-radius: 10px; /* Start as a block/chunk */
    transition: left 1.5s ease-in-out, background-color 1s ease-in-out, width 0.8s ease, height 0.8s ease, border-radius 0.8s ease; /* Smooth transitions for all properties */
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 0.8em;
    font-weight: bold;
    text-align: center;
}

#stage-info {
     text-align: center;
     margin-top: auto; /* Push info to the bottom */
     padding-top: 10px;
     border-top: 1px solid #eee;
     width: 100%;
}

#current-stage-name {
    font-size: 1.6em; /* Slightly larger stage name */
    font-weight: bold;
    color: #004d40;
    margin-bottom: 8px;
    min-height: 1.6em; /* Prevent layout shifts */
    transition: opacity 0.5s ease; /* Fade in/out */
}

#current-stage-description {
    font-size: 1em;
    color: #555;
    min-height: 4em; /* Prevent layout shifts */
    transition: opacity 0.5s ease; /* Fade in/out */
}

/* --- Navigation and Progress --- */
#stage-navigation {
    text-align: center;
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#stage-navigation button {
    padding: 12px 25px; /* Larger buttons */
    cursor: pointer;
    border: none;
    border-radius: 25px; /* Pill shape buttons */
    background-color: #00796b; /* Teal */
    color: white;
    font-size: 1.1em;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
}

#stage-navigation button:disabled {
    background-color: #b2dfdb; /* Lighter teal when disabled */
    cursor: not-allowed;
    box-shadow: none;
}

#stage-navigation button:hover:not(:disabled) {
    background-color: #004d40; /* Darker teal on hover */
    transform: translateY(-2px);
}

#stage-progress {
    display: flex;
    justify-content: center;
    flex-grow: 1; /* Take up available space */
    margin: 0 20px;
    gap: 8px; /* Smaller gap between indicators */
}

.stage-indicator {
    width: 15px; /* Smaller indicators */
    height: 15px; /* Smaller indicators */
    border-radius: 50%;
    background-color: #e0f2f7; /* Very light blue */
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    border: 2px solid #00796b; /* Teal border */
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}

.stage-indicator.active {
    background-color: #004d40; /* Dark teal when active */
    border-color: #004d40;
    transform: scale(1.2); /* Slightly enlarge active indicator */
}

.stage-indicator:hover:not(.active) {
    background-color: #4db6ac; /* Medium teal on hover */
    transform: scale(1.1);
}

#back-to-selection {
    display: block;
    width: fit-content;
    margin: 20px auto 0; /* Position below navigation */
    padding: 8px 15px;
    cursor: pointer;
    border: 1px solid #d32f2f; /* Reddish border */
    border-radius: 5px;
    background-color: #ffebee; /* Very light red */
    color: #d32f2f; /* Reddish text */
    font-size: 0.9em;
    transition: background-color 0.3s, color 0.3s;
}

#back-to-selection:hover {
     background-color: #ffcdd2; /* Lighter red on hover */
}


/* --- Detailed Explanation Toggle Button --- */
.toggle-btn {
    display: block;
    width: fit-content;
    margin: 30px auto 20px; /* Centered, more space */
    padding: 12px 25px;
    cursor: pointer;
    border: none; /* Remove border */
    border-radius: 25px; /* Pill shape */
    background-color: #bdbdbd; /* Gray */
    color: #333;
    font-size: 1em;
    font-weight: bold;
    transition: background-color 0.3s ease, box-shadow 0.2s ease;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
}

.toggle-btn:hover {
    background-color: #9e9e9e; /* Darker gray on hover */
    box-shadow: 0 5px 12px rgba(0, 0, 0, 0.15);
}

/* --- Detailed Explanation Section --- */
#detailed-explanation {
    margin-top: 20px;
    padding: 25px;
    border: none; /* Remove border */
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    color: #333;
    line-height: 1.7; /* Improve readability */
}

#detailed-explanation h2,
#detailed-explanation h3 {
    color: #004d40; /* Teal headings */
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e0f2f7; /* Light blue border */
    padding-bottom: 5px;
}

#detailed-explanation h2 {
     font-size: 1.6em;
}

#detailed-explanation h3 {
    font-size: 1.3em;
    color: #00796b; /* Slightly lighter teal */
}


#detailed-explanation p,
#detailed-explanation ul {
    margin-bottom: 15px;
    color: #555; /* Slightly lighter text */
}

#detailed-explanation ul {
    padding-right: 20px; /* Indent list */
}

#detailed-explanation ul li {
    margin-bottom: 8px;
    list-style: disc outside; /* Use standard discs */
}

</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('sugar-journey-app');
    const rawMaterialSelect = document.getElementById('raw-material-select');
    const selectCaneBtn = document.getElementById('select-cane');
    const selectBeetBtn = document.getElementById('select-beet');
    const stageDisplay = document.getElementById('stage-display');
    const currentStageName = document.getElementById('current-stage-name');
    const currentStageDescription = document.getElementById('current-stage-description');
    const animationArea = document.getElementById('animation-area');
    const materialRepresentation = document.getElementById('material-representation');
    const prevStageBtn = document.getElementById('prev-stage');
    const nextStageBtn = document.getElementById('next-stage');
    const stageProgressContainer = document.getElementById('stage-progress');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const detailedExplanation = document.getElementById('detailed-explanation');
    const backToSelectionBtn = document.getElementById('back-to-selection'); // Get the new button

    let selectedMaterial = null; // 'cane' or 'beet'
    let currentStageIndex = 0;

    // Define stages with enhanced details for animation and description
    const stages = [
        // Stage 0: Initial Selection (Hidden process)
        { name: "בחירת חומר גלם", description: "בחר מאיזה צמח יופק הסוכר למסע זה.",
          materialParams: { left: '50%', top: '50%', width: '0', height: '0', borderRadius: '50%', backgroundColor: '#ccc' }, // Invisible/Placeholder
          processSegment: null, // No associated segment
          visible: false // This stage is not part of the visual process flow
        },
        // Process Stages (Index 1 to stages.length - 1)
        { name: "קציר", description: "המסע מתחיל בשדה: קצירת קנה הסוכר או עקירת סלק הסוכר מהאדמה.",
          materialParams: { left: '5%', top: '50%', width: '60px', height: '40px', borderRadius: '10px', backgroundColor: '#8B4513' }, // Raw chunk
          processSegment: 'field'
        },
        { name: "הכנה במפעל", description: "חומר הגלם מגיע למפעל, נשטף ביסודיות ומוכן לשלב הבא.",
          materialParams: { left: '15%', top: '50%', width: '55px', height: '35px', borderRadius: '8px', backgroundColor: '#795548' }, // Slightly smaller, cleaner chunk
          processSegment: 'factory-entrance'
        },
        { name: "ריסוק ומיצוי", description: "(קנה: גריסה וסחיטה) / (סלק: פריסה ודיפוזיה) - מפיקים את המיץ הגולמי.",
          materialParams: { left: '28%', top: '50%', width: '40px', height: '40px', borderRadius: '50%', backgroundColor: '#ff9800' }, // Turns into liquid/juice
          processSegment: 'extraction'
        },
        { name: "טיהור וסינון", description: "מוסיפים חומרים כימיים ומסננים כדי להסיר מזהמים מהמיץ הגולמי.",
          materialParams: { left: '42%', top: '50%', width: '35px', height: '35px', borderRadius: '50%', backgroundColor: '#2196f3' }, // Cleaner liquid
          processSegment: 'purification'
        },
        { name: "אידוי וריכוז", description: "מאדים מים מהמיץ המטוהר בוואקום לקבלת סירופ סוכר סמיך ומרוכז.",
          materialParams: { left: '58%', top: '50%', width: '30px', height: '30px', borderRadius: '50%', backgroundColor: '#ffeb3b' }, // Thicker, yellower syrup
          processSegment: 'evaporation'
        },
        { name: "גיבוש (קריסטליזציה)", description: "בתנאים מבוקרים, מוסיפים 'זרעים' וגבישי הסוכר מתחילים להיווצר ולגדול.",
          materialParams: { left: '70%', top: '50%', width: '40px', height: '40px', borderRadius: '50%', backgroundColor: '#e1bee7', text: '💎' }, // Crystals appear
          processSegment: 'crystallization'
        },
        { name: "הפרדה (צנטריפוגה)", description: "משתמשים בצנטריפוגה מהירה להפרדת גבישי הסוכר המוצקים מהמולסה הנוזלית.",
          materialParams: { left: '82%', top: '50%', width: '35px', height: '35px', borderRadius: '5px', backgroundColor: '#f5f5f5', text: '✨' }, // Separated, almost white crystals
          processSegment: 'separation'
        },
        { name: "ייבוש וקירור", description: "מייבשים את גבישי הסוכר באוויר חם ומקררים אותם.",
          materialParams: { left: '90%', top: '50%', width: '30px', height: '30px', borderRadius: '3px', backgroundColor: '#ffffff', text: '❄️' }, // Dry, white crystals
          processSegment: 'drying'
        },
        { name: "בקרת איכות ואריזה", description: "הסוכר נבדק, נשקל ונארז לאריזות קטנות או גדולות.",
          materialParams: { left: '95%', top: '50%', width: '25px', height: '35px', borderRadius: '5px', backgroundColor: '#eeeeee', text: '📦' }, // Packaged
           processSegment: 'packaging'
        },
         { name: "המוצר המוגמר", description: "הסוכר הטהור מוכן למסעו האחרון - אל המדף, ומשם אליכם!",
          materialParams: { left: '98%', top: '50%', width: '20px', height: '30px', borderRadius: '5px', backgroundColor: '#ffffff', text: '🥄' }, // On the shelf/spoon
           processSegment: 'shelf'
        }
    ];

     // Adjust descriptions based on material selection for specific stages
    function adjustDescriptions(material) {
        if (material === 'beet') {
            stages[2].description = "שורשי הסלק מגיעים למפעל, נשטפים ונפרסים לשבבים דקים."; // Preparation for beet
            stages[3].description = "שבבי הסלק עוברים תהליך דיפוזיה להוצאת הסוכר למים חמים."; // Extraction for beet
        } else { // cane
             stages[2].description = "גבעולי קנה הסוכר מגיעים למפעל, נשטפים ומוכנים לריסוק."; // Preparation for cane
            stages[3].description = "גבעולי הקנה נגרסים ונסחטים בעוצמה להפקת מיץ גולמי."; // Extraction for cane
        }
        // Re-apply description for the current stage if already selected
        if (currentStageIndex > 0) {
             currentStageDescription.textContent = stages[currentStageIndex].description;
        }
    }

    function updateDisplay() {
        const currentStage = stages[currentStageIndex];

        // Update stage info
        currentStageName.textContent = currentStage.name;
        currentStageDescription.textContent = currentStage.description;

        // Animate material representation
        const materialParams = currentStage.materialParams;
        materialRepresentation.style.left = materialParams.left;
        materialRepresentation.style.top = materialParams.top;
        materialRepresentation.style.width = materialParams.width;
        materialRepresentation.style.height = materialParams.height;
        materialRepresentation.style.borderRadius = materialParams.borderRadius;
        materialRepresentation.style.backgroundColor = materialParams.backgroundColor;
        materialRepresentation.textContent = materialParams.text || ''; // Update text content for icons

        // Update navigation button states
        // Prev is disabled at stage 0 (selection) and stage 1 (harvest) as going back before process start needs special handling
        prevStageBtn.disabled = currentStageIndex <= 1;
        nextStageBtn.disabled = currentStageIndex >= stages.length - 1;
        backToSelectionBtn.style.display = currentStageIndex > 0 ? 'block' : 'none';


        // Update progress indicators state
        updateProgressIndicators();

        // Show/hide sections
        if (currentStageIndex === 0) {
            rawMaterialSelect.style.display = 'block';
            stageDisplay.style.display = 'none';
            stageNavigation.style.display = 'none';
            stageProgressContainer.style.display = 'none'; // Hide progress bar
             backToSelectionBtn.style.display = 'none'; // Hide back button on selection screen
        } else {
            rawMaterialSelect.style.display = 'none';
            stageDisplay.style.display = 'flex';
            stageNavigation.style.display = 'flex';
             stageProgressContainer.style.display = 'flex'; // Show progress bar
        }

         // Highlight current process segment
         document.querySelectorAll('.process-segment').forEach(segment => segment.style.opacity = '0.5'); // Dim all
         if (currentStage.processSegment) {
             const activeSegment = document.querySelector(`.process-segment.${currentStage.processSegment}`);
             if (activeSegment) {
                 activeSegment.style.opacity = '1'; // Highlight active one
             }
         }

         // Adjust animation area alignment based on position
         if (currentStageIndex <= 1) { // Beginning
            animationArea.style.justifyContent = 'flex-start';
            animationArea.style.alignItems = 'center';
         } else if (currentStageIndex >= stages.length - 2) { // End
            animationArea.style.justifyContent = 'flex-end';
             animationArea.style.alignItems = 'center';
         } else { // Middle
             animationArea.style.justifyContent = 'center';
              animationArea.style.alignItems = 'center';
         }

         // Simple fade transition for text
         currentStageName.style.opacity = '0';
         currentStageDescription.style.opacity = '0';
         setTimeout(() => {
             currentStageName.style.opacity = '1';
             currentStageDescription.style.opacity = '1';
         }, 100); // Small delay for fade effect
    }

    function updateProgressIndicators() {
        stageProgressContainer.innerHTML = ''; // Clear existing indicators
        // Create indicators only for the actual process stages (index 1 onwards)
        for (let i = 1; i < stages.length; i++) {
            const indicator = document.createElement('div');
            indicator.classList.add('stage-indicator');
            if (i <= currentStageIndex) { // Mark stages up to the current one as active/visited
                indicator.classList.add('active');
            }
            // Allow clicking indicators to jump to a stage
            indicator.addEventListener('click', () => {
                 if (selectedMaterial && i > 0) { // Only allow jumping if material selected and not stage 0
                    currentStageIndex = i;
                    updateDisplay();
                 }
            });
            indicator.dataset.stageIndex = i; // Store index
            stageProgressContainer.appendChild(indicator);
        }
    }

    function selectMaterial(material) {
        selectedMaterial = material;
        adjustDescriptions(selectedMaterial);
        // Start the process from the first actual stage (index 1)
        currentStageIndex = 1;
        updateDisplay();
        // Add progress indicators after material selection
        updateProgressIndicators();
        // Add visual feedback to selected button
        selectCaneBtn.classList.remove('selected');
        selectBeetBtn.classList.remove('selected');
        document.getElementById('select-' + material).classList.add('selected');
    }

    // Event Listeners for raw material selection
    selectCaneBtn.addEventListener('click', () => selectMaterial('cane'));
    selectBeetBtn.addEventListener('click', () => selectMaterial('beet'));

    // Event Listeners for navigation
    nextStageBtn.addEventListener('click', () => {
        if (currentStageIndex < stages.length - 1) {
            currentStageIndex++;
            updateDisplay();
        }
    });

    prevStageBtn.addEventListener('click', () => {
        if (currentStageIndex > 1) { // Allow going back through process stages
            currentStageIndex--;
            updateDisplay();
        } else if (currentStageIndex === 1) { // Special case to go back to selection from stage 1
             currentStageIndex = 0;
             selectedMaterial = null; // Reset selection
             updateDisplay();
        }
    });

    // Event Listener for back to selection button
    backToSelectionBtn.addEventListener('click', () => {
         currentStageIndex = 0;
         selectedMaterial = null; // Reset selection
         updateDisplay();
    });


    // Event Listener for explanation toggle
    toggleExplanationBtn.addEventListener('click', () => {
        const isHidden = detailedExplanation.style.display === 'none';
        detailedExplanation.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט' : 'הצג הסבר מפורט';
        // Optional: Scroll to the detailed explanation if it's shown
        if (!isHidden) {
             detailedExplanation.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    // Initial display setup
    updateDisplay(); // Call once to show the initial state (material selection)

});
</script>
```