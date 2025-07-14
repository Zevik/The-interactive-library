---
title: "לראות את הבלתי נראה: סימולציה אינטראקטיבית של טלסקופ קרני גמא"
english_slug: seeing-the-unseen-how-gamma-ray-telescopes-detect-the-violent-universe
category: "מדעים מדויקים / פיזיקה"
tags: ["קרני גמא", "טלסקופים", "אסטרופיזיקה", "קרינת צ'רנקוב", "יקום אנרגטי", "סימולציה"]
---

# לראות את הבלתי נראה: סימולציה אינטראקטיבית של טלסקופ קרני גמא

דמיינו רגע את האירועים האלימים ביותר ביקום: פיצוצי סופרנובה אדירים, חורים שחורים קורעים לגזרים כוכבים, התנגשויות קוסמיות בלתי נתפסות. אירועים אלו פולטים קרינה קיצונית - קרני גמא, האנרגטיות מכל צורות האור. אבל איך אנו, כאן על כדור הארץ, יכולים 'לראות' את הקרינה החמקמקה הזו, שנעצרת כליל על ידי האטמוספירה שלנו? טלסקופי קרני גמא קרקעיים משתמשים בשיטה גאונית ועקיפה כדי לצוד אותן. בואו נחקור כיצד.

<div class="app-container">
    <div class="sky">
        <div class="instruction">לחצו בכל מקום בשמיים כדי לשלוח קרן גמא!</div>
        <div class="gamma-ray" id="gammaRay"></div>
        <div class="particle-shower" id="particleShower"></div>
        <div class="cherenkov-cone" id="cherenkovCone"></div>
        <div class="cherenkov-flash" id="cherenkovFlash"></div>
        <div class="atmosphere-line"></div>
        <div class="star star1"></div>
        <div class="star star2"></div>
        <div class="star star3"></div>
    </div>
    <div class="ground">
        <div class="telescope" id="telescope">
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="mirror-segment"></div>
            <div class="camera"></div>
            <div class="support support-left"></div>
            <div class="support support-right"></div>
        </div>
         <div class="ground-texture"></div>
    </div>
    <div class="simulation-info">
        <div id="detectionStatus">מחכים לקרינה...</div>
    </div>
</div>

<style>
    /* Improved Color Palette */
    :root {
        --dark-blue-sky: #1A237E; /* Deep Indigo */
        --lighter-blue-sky: #3F51B5; /* Indigo */
        --ground-color: #455A64; /* Blue Gray */
        --telescope-silver: #B0BEC5; /* Blue Gray 200 */
        --telescope-support: #78909C; /* Blue Gray 400 */
        --gamma-yellow: #FFEB3B; /* Yellow 500 */
        --shower-white: rgba(255, 255, 255, 0.9);
        --cherenkov-blue: rgba(63, 81, 181, 0.7); /* Indigo 500 with transparency */
        --flash-blue: rgba(63, 81, 181, 1); /* Indigo 500 */
        --ui-background: #ECEFF1; /* Blue Gray 50 */
        --ui-button-primary: #5C6BC0; /* Indigo 400 */
        --ui-button-hover: #3949AB; /* Indigo 600 */
        --text-color-dark: #263238; /* Blue Gray 900 */
        --atmosphere-line-color: rgba(159, 168, 218, 0.6); /* Lavender 200 */
    }

    .app-container {
        width: 100%;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid var(--telescope-silver);
        border-radius: 12px;
        overflow: hidden;
        background-color: var(--ui-background);
        position: relative;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }

    .sky {
        width: 100%;
        height: 450px; /* Increased height for better visual separation */
        background: linear-gradient(to bottom, var(--dark-blue-sky), var(--lighter-blue-sky));
        position: relative;
        overflow: hidden;
        cursor: pointer; /* Indicate clickable area */
    }

    .star {
        position: absolute;
        width: 2px;
        height: 2px;
        background-color: white;
        border-radius: 50%;
        box-shadow: 0 0 4px white;
    }

    .star1 { top: 10%; left: 20%; animation: twinkle 2s infinite alternate ease-in-out; }
    .star2 { top: 5%; left: 70%; animation: twinkle 2.5s infinite alternate ease-in-out 0.5s; }
    .star3 { top: 15%; left: 90%; animation: twinkle 3s infinite alternate ease-in-out 1s; }

    @keyframes twinkle {
        from { opacity: 0.8; transform: scale(1); }
        to { opacity: 0.4; transform: scale(0.8); }
    }


    .instruction {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 1.5rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        z-index: 15;
        pointer-events: none; /* Allows clicks to pass through */
        transition: opacity 0.5s ease-out;
    }

    .atmosphere-line {
        position: absolute;
        top: 55%; /* Represents top of dense atmosphere */
        left: 0;
        width: 100%;
        height: 3px; /* Thicker line */
        background: linear-gradient(to right, transparent, var(--atmosphere-line-color), transparent);
        box-shadow: 0 0 10px 3px var(--atmosphere-line-color);
        z-index: 2;
    }

    .ground {
        width: 100%;
        height: 250px; /* Increased height */
        background-color: var(--ground-color);
        position: relative;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        border-top: 5px solid var(--telescope-support);
    }

    .ground-texture {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background: repeating-linear-gradient(
             45deg,
             rgba(0,0,0,0.05),
             rgba(0,0,0,0.05) 5px,
             transparent 5px,
             transparent 10px
         );
         opacity: 0.1;
         pointer-events: none;
         z-index: 1;
    }


    .telescope {
        position: absolute;
        bottom: 20px; /* Lifted slightly */
        width: 150px; /* Wider base */
        height: 180px; /* Taller */
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .mirror-segment {
        position: absolute;
        width: 30px;
        height: 15px;
        background-color: var(--telescope-silver);
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transform-origin: bottom center; /* Pivot point for position */
        z-index: 11; /* Above supports */
    }

    /* Arrange segments to form a curved shape */
    .mirror-segment:nth-child(1) { bottom: 10px; left: 15px; transform: rotate(-20deg); }
    .mirror-segment:nth-child(2) { bottom: 5px; left: 40px; transform: rotate(-10deg); }
    .mirror-segment:nth-child(3) { bottom: 2px; left: 65px; transform: rotate(0deg); }
    .mirror-segment:nth-child(4) { bottom: 5px; left: 90px; transform: rotate(10deg); }
    .mirror-segment:nth-child(5) { bottom: 10px; left: 115px; transform: rotate(20deg); }
    /* Add more segments for a fuller look */
    .mirror-segment:nth-child(6) { bottom: 18px; left: 20px; transform: rotate(-30deg); }
    .mirror-segment:nth-child(7) { bottom: 18px; left: 105px; transform: rotate(30deg); }
     .mirror-segment:nth-child(8) { bottom: 25px; left: 65px; width: 40px; height: 20px; background-color: var(--telescope-support); z-index: 10; border-radius: 6px; } /* Base connection */


    .camera {
        width: 25px; /* Slightly larger */
        height: 25px;
        background-color: var(--flash-blue); /* Match flash color */
        border-radius: 50%;
        position: absolute;
        top: 60px; /* Positioned higher above the mirror */
        left: 50%;
        transform: translateX(-50%);
        z-index: 12;
        box-shadow: 0 0 8px var(--flash-blue);
         border: 3px solid white;
    }
     .support {
        position: absolute;
        bottom: 0;
        width: 10px;
        height: 120px; /* Taller */
        background-color: var(--telescope-support);
        z-index: 9;
         border-radius: 5px;
         box-shadow: inset 0 0 5px rgba(0,0,0,0.3);
    }
    .support-left { left: 20px; transform: rotate(10deg); transform-origin: bottom; }
    .support-right { right: 20px; transform: rotate(-10deg); transform-origin: bottom;}


    .gamma-ray {
        position: absolute;
        top: 0;
        left: 50%; /* Starting point */
        width: 3px; /* Thinner */
        height: 0;
        background-color: var(--gamma-yellow);
        box-shadow: 0 0 8px var(--gamma-yellow); /* Glow */
        transform: translateX(-1.5px);
        opacity: 1;
        z-index: 5;
    }

    .particle-shower {
        position: absolute;
        top: 55%; /* Starts at atmosphere interaction line */
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, var(--shower-white) 0%, rgba(255,255,255,0) 70%);
        opacity: 0;
        transform: translate(-50%, -50%); /* Center the shower effect */
        border-radius: 50%;
        pointer-events: none;
        z-index: 4;
        filter: blur(5px); /* Soft glow effect */
    }

     .cherenkov-cone {
        position: absolute;
        top: 55%; /* Starts from shower origin */
        left: 50%;
        width: 0;
        height: 0;
        border-style: solid;
        border-color: transparent;
        border-top-color: var(--cherenkov-blue); /* Blue cone */
        border-top-width: 0; /* Starts as a point */
        border-left-width: 0;
        border-right-width: 0;
        opacity: 0;
        transform: translateX(-50%) translateY(-100%); /* Position tip at shower origin */
        transform-origin: bottom; /* Scale from the tip */
        pointer-events: none;
        z-index: 3;
     }


    .cherenkov-flash {
        position: absolute;
        /* Position calculated by JS */
        width: 0;
        height: 0;
        background: radial-gradient(circle, var(--flash-blue) 0%, rgba(63, 81, 181, 0) 70%); /* Blue flash */
        opacity: 0;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 6;
        box-shadow: 0 0 20px 10px var(--flash-blue); /* Stronger glow */
    }

    .simulation-info {
        padding: 10px;
        text-align: center;
        background-color: var(--ui-background);
        color: var(--text-color-dark);
        font-size: 1.1rem;
    }

    #detectionStatus {
        min-height: 1.5em; /* Reserve space to prevent layout shift */
    }

    #explanationButton {
        display: block; /* Make it a block element */
        width: fit-content; /* Fit button to text width */
        margin: 20px auto; /* Center the button */
        padding: 12px 20px; /* More padding */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 8px; /* More rounded */
        background-color: var(--ui-button-primary);
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #explanationButton:hover {
        background-color: var(--ui-button-hover);
        transform: translateY(-2px);
    }
     #explanationButton:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        background-color: var(--ui-background);
        border-radius: 8px;
        display: none; /* Initially hidden */
        line-height: 1.7; /* Increased line spacing */
        color: var(--text-color-dark);
        border-top: 1px solid var(--telescope-silver);
    }

    #explanation h2, #explanation h3 {
        color: var(--text-color-dark);
        margin-bottom: 12px; /* More space */
        border-bottom: 2px solid var(--telescope-support); /* Thicker border */
        padding-bottom: 6px;
        font-weight: bold;
    }

     #explanation p, #explanation ul {
        margin-bottom: 18px; /* More space */
    }

    #explanation ul {
        padding-left: 25px; /* More indentation */
    }

    #explanation li {
        margin-bottom: 10px; /* More space between list items */
    }

    #explanation a {
        color: var(--ui-button-primary);
        text-decoration: none;
    }
    #explanation a:hover {
        text-decoration: underline;
    }

</style>

<button id="explanationButton">הצג/הסתר את הסוד מאחורי הטלסקופ</button>

<div id="explanation">
    <h2>הסוד מאחורי הטלסקופ: כיצד 'רואים' קרני גמא?</h2>

    <h3>מהן קרני גמא ומאין הן מגיעות?</h3>
    <p>קרני גמא הן אלופי האנרגיה במשפחת הקרינה האלקטרומגנטית. הן נולדות באירועים הקוסמיים הדרמטיים והאלימים ביותר שאפשר לדמיין: פיצוצי כוכבים (סופרנובות), התנגשויות אימתניות בין חורים שחורים או כוכבי נייטרונים, ולבבות גלקסיות פעילים שפולטים סילוני חומר במהירות האור. חקר קרני גמא הוא כמו לראות את היקום בזמן התקף זעם קוסמי - רגעים קצרים אך רבי עוצמה שמגלים לנו על הפיזיקה הקיצונית ביותר.</p>
    <ul>
        <li><strong>התפרצויות קרני גמא (GRBs):</strong> ההבזקים הבהירים ביותר ביקום. חושבים שהם קשורים לקריסת כוכבים מסיביים או התמזגות גופים צפופים במיוחד.</li>
        <li><strong>שאריות סופרנובה:</strong> האפר הקוסמי שנותר מפיצוץ כוכב, בו חלקיקים מואצים לאנרגיות קיצוניות.</li>
        <li><strong>גלעיני גלקסיות פעילים (AGN):</strong> מפלצות-חורים שחורים במרכזי גלקסיות הפולטות סילונים על-יחסותיים של חלקיקים אנרגטיים.</li>
        <li><strong>פולסרים:</strong> כוכבי נייטרונים מסתובבים במהירות שמקרינים אלומות קרינה עוצמתיות.</li>
        <li><strong>חומר אפל (השערה מסעירה):</strong> חלק מהתיאוריות מנבאות שהתנגשויות או דעיכות של חלקיקי חומר אפל עשויות לפלוט קרני גמא – טלסקופים אלו הם ציידי החתימה האפלה הזו.</li>
    </ul>

    <h3>למה אי אפשר פשוט להשתמש במראה?</h3>
    <p>בניגוד לאור רגיל, שמתנהג יפה ומשתקף או נשבר בעדינות, קרני גמא הן פוטונים סופר-אנרגטיים. הן מתעלמות לחלוטין מרוב המראות והעדשות הרגילות, פשוט עוברות דרך האטומים. אם כבר מתרחשת אינטראקציה, היא לרוב הרסנית - כמו מסמר שיורה דרך קיר גבס במקום קפיצה קטנה ממראה. לכן, צריך גישה אחרת לגמרי.</p>

    <h3>הפיתרון: לאסוף את "הרמזים" באטמוספירה</h3>
    <p>כיוון שהאטמוספירה שלנו בולעת קרני גמא, אי אפשר לראות אותן ישירות מהקרקע. טלסקופי חלל (כמו פרמי) עושים זאת, אבל עבור קרני גמא *סופר* אנרגטיות, טלסקופים קרקעיים מסוג Cherenkov (IACT) מספקים דרך יצירתית:</p>

    <h4>1. מפגש באטמוספירה: יצירת מטר חלקיקים</h4>
    <p>כשקרן גמא מהחלל פוגעת באטמוספירה העליונה, היא מתנגשת באטומים. ההתנגשות הזו יוצרת "מבול" של חלקיקים שניוניים - בעיקר אלקטרונים ופוזיטרונים - שגם הם בעלי אנרגיה גבוהה. החלקיקים האלה ממשיכים להתנגש ויוצרים דורות נוספים של חלקיקים במהירות מטורפת. התהליך הזה נקרא "מטר חלקיקים" (particle shower), והוא מתפתח כמו מפולת שלגים אנרגטית שיורדת דרך האטמוספירה.</p>

    <h4>2. שבירת מחסום המהירות הקוסמי: קרינת צ'רנקוב</h4>
    <p>חלקיקים במטר, במיוחד אלקטרונים ופוזיטרונים קלי-משקל, נעים מהר מאוד. למרות שמהירותם נמוכה ממהירות האור בריק, היא *גבוהה יותר* ממהירות האור בתווך האטמוספרי (שהיא איטית יותר). כשחלקיק טעון שובר את מחסום מהירות האור בתווך, הוא יוצר "בום על-קולי" של אור כחלחל חלש וקצר מאוד - זוהי קרינת צ'רנקוב. קרינה זו נפלטת בצורת חרוט, עם זווית תלויה במהירות החלקיק. דמיינו מטוס סילון שעובר את מהירות הקול ויוצר גל הלם קולי; זה אותו עיקרון, רק עם אור וחלקיקים אטומים.</p>

    <h4>3. הטלסקופ: עין הענק לוכדת את ההבזק</h4>
    <p>טלסקופ Cherenkov קרקעי הוא בעצם אספן אור ענק שמטרתו ללכוד את הבזקי צ'רנקוב. הוא מורכב מ:</p>
    <ul>
        <li><strong>מראה סגמנטלית עצומה:</strong> בנויה מהרבה מראות קטנות, המראה כולה מתנהגת כאספן אור אחד ענק (קוטר עשרות מטרים!). היא מכוונת לשמיים כדי לאסוף כמה שיותר פוטוני צ'רנקוב המגיעים בחרוט מהמטר באטמוספירה.</li>
        <li><strong>מצלמת פיקסלים מהירה:</strong> ממוקמת בנקודת המוקד של המראה. זו לא מצלמה רגילה, אלא רשת צפופה של גלאי אור רגישים במיוחד, שמסוגלים לזהות את ההבזק הקצרצר (ננו-שניות!) של קרינת צ'רנקוב ולמדוד את עוצמתו וצורתו המדויקת.</li>
    </ul>

    <h4>4. פענוח התמונה: שחזור קרן הגמא המקורית</h4>
    <p>הבזק צ'רנקוב שנרשם במצלמה הוא "טביעת האצבע" של מטר החלקיקים שיצרה קרן הגמא. הצורה של ההבזק (אליפסה), מיקומו במצלמה, והזמן המדויק שבו הגיעו הפוטונים, מכילים את כל המידע. על ידי ניתוח מדויק של הבזק זה (ובמערכים מודרניים, על ידי השוואת הבזקים מאותו מטר שנקלטו ע"י מספר טלסקופים בו-זמנית), אסטרונומים יכולים לשחזר לאחור את מסלול מטר החלקיקים, וחשוב מכך - לקבוע מה היה הכיוון שממנו הגיעה קרן הגמא המקורית ומה הייתה האנרגיה שלה. כך, למרות שלא ראינו את קרן הגמא עצמה, אנו "רואים" אותה דרך האור הכחול החיוור שהיא השאירה אחריה באטמוספירה.</p>

    <h3>מצפי כרנקוב מובילים</h3>
    <p>מצפים כמו H.E.S.S. (נמיביה), MAGIC (איי הקנריים), ו-VERITAS (ארה"ב) מובילים את המחקר הזה. הפרויקט העתידי הענק CTA (Cherenkov Telescope Array) יבנה את מערך הטלסקופים הגדול והרגיש ביותר אי-פעם, כדי לפתוח חלון חדש ליקום האנרגטי.</p>

    <h3>למה זה חשוב?</h3>
    <p>חקר קרני גמא הוא החזית של האסטרופיזיקה האנרגטית. הוא מאפשר לנו לחקור את הפיזיקה בתנאים שאי אפשר לשחזר במעבדה, להבין כיצד חלקיקים מואצים למהירויות אדירות בסביבת חורים שחורים וכוכבי נייטרונים, לפענח את החידה של התפרצויות קרני הגמא, ואף לחפש אחר עדויות לקיום חומר אפל - אולי החומר המסתורי הזה פולט קרני גמא כשהוא מתנגש בעצמו?</p>
</div>

<script>
    const explanationButton = document.getElementById('explanationButton');
    const explanationDiv = document.getElementById('explanation');
    const skyElement = document.querySelector('.sky');
    const instructionElement = document.querySelector('.instruction');
    const detectionStatusElement = document.getElementById('detectionStatus');

    const gammaRay = document.getElementById('gammaRay');
    const particleShower = document.getElementById('particleShower');
    const cherenkovCone = document.getElementById('cherenkovCone');
    const cherenkovFlash = document.getElementById('cherenkovFlash');
    const atmosphereLine = document.querySelector('.atmosphere-line');
    const telescope = document.getElementById('telescope');

    // Store atmospheric interaction height (as percentage of sky height)
    const atmosphereHeightPercent = 55; // Matches CSS
    const atmosphereLineTop = atmosphereHeightPercent + '%';

    let isAnimating = false; // Flag to prevent multiple animations

    // Function to reset all elements to initial state and clear transitions
    function resetSimulation() {
         // Use a temporary class or inline style to clear transitions
         const elementsToReset = [gammaRay, particleShower, cherenkovCone, cherenkovFlash];
         elementsToReset.forEach(el => {
             el.style.transition = 'none';
             // Reset specific properties that were animated
             el.style.height = '';
             el.style.top = '';
             el.style.left = '';
             el.style.opacity = '';
             el.style.width = '';
             el.style.transform = '';
             el.style.border = ''; // Clear cone borders
             el.style.borderTop = '';
             el.style.borderLeft = '';
             el.style.borderRight = '';
             el.style.boxShadow = ''; // Clear flash shadow
         });


         // Reapply initial styles after clearing transitions and state
         Object.assign(gammaRay.style, { top: '0%', height: '0', opacity: '1', width: '3px', transform: 'translateX(-1.5px)', boxShadow: '0 0 8px var(--gamma-yellow)', backgroundColor: 'var(--gamma-yellow)' });
         Object.assign(particleShower.style, { top: atmosphereLineTop, width: '0', height: '0', opacity: '0', transform: 'translate(-50%, -50%)', backgroundColor: 'transparent', backgroundImage: 'radial-gradient(circle, var(--shower-white) 0%, rgba(255,255,255,0) 70%)', filter: 'blur(5px)' });

          // Ensure cone is reset to a point (0 width borders, 0 height border-top-width)
          Object.assign(cherenkovCone.style, {
              top: atmosphereLineTop,
              left: '50%', // Will be updated by click
              width: '0',
              height: '0',
              opacity: '0',
              borderStyle: 'solid',
              borderColor: 'transparent',
              borderTopColor: 'var(--cherenkov-blue)',
              borderTopWidth: '0',
              borderLeftWidth: '0',
              borderRightWidth: '0',
              transform: 'translateX(-50%) translateY(-100%)', /* Position tip at shower origin */
              transformOrigin: 'bottom' /* Scale from the tip */
          });


         Object.assign(cherenkovFlash.style, { width: '0', height: '0', opacity: '0', transform: 'translate(-50%, -50%)', backgroundImage: 'radial-gradient(circle, var(--flash-blue) 0%, rgba(63, 81, 181, 0) 70%)', boxShadow: '0 0 20px 10px var(--flash-blue)' });


        // Force a reflow to apply reset styles immediately before starting new transitions
        void gammaRay.offsetWidth;
    }

    function startSimulation(clickXPercent) {
        if (isAnimating) return; // Prevent starting if already animating
        isAnimating = true;
        resetSimulation();
        detectionStatusElement.textContent = 'מחפשים קרן גמא...';
        instructionElement.style.opacity = '0'; // Fade out instruction on first click

        const skyHeight = skyElement.offsetHeight;
        const groundHeight = document.querySelector('.ground').offsetHeight;
        const telescopeHeight = telescope.offsetHeight;
        const mirrorBottomOffset = 20; // Matches CSS bottom: 20px on telescope
        const atmospherePixelTop = skyHeight * (atmosphereHeightPercent / 100);

        // Calculate target position for the flash (just above the telescope mirror)
        // Assuming telescope is centered horizontally. Flash position needs to be dynamic
        // based on click X and cone angle. For simplicity here, let's just position
        // the flash horizontally under the shower origin, and vertically just above the mirror.
        const telescopeMirrorTopRelativeToSky = skyHeight - (groundHeight - mirrorBottomOffset - (telescope.querySelector('.mirror-segment:nth-child(8)').offsetHeight / 2)); // Approx position of the mirror's center base
        const flashTargetY = telescopeMirrorTopRelativeToSky; // Vertical position of the flash center

        // --- Step 1: Gamma Ray travels to atmosphere ---
        gammaRay.style.left = clickXPercent + '%'; // Start from click X
        gammaRay.style.transition = 'height 1s linear, top 1s linear, opacity 0.5s ease-out 1s, left 0.5s linear';
        gammaRay.style.height = (atmospherePixelTop) + 'px';
        gammaRay.style.top = atmosphereLineTop;
        gammaRay.style.opacity = '0'; // Fade out as it interacts


        // --- Step 2: Particle Shower (starts when gamma ray hits atmosphere) ---
        const showerStartTime = 1000; // Matches gammaRay transition duration
        const showerStartLeft = clickXPercent; // Shower starts horizontally where ray hit

        setTimeout(() => {
            particleShower.style.left = showerStartLeft + '%'; // Position shower at click X
            particleShower.style.transition = 'width 0.6s ease-out, height 0.6s ease-out, opacity 0.7s ease-out';
            particleShower.style.opacity = '1';
            particleShower.style.width = '180px'; // Max shower size
            particleShower.style.height = '180px';
            detectionStatusElement.textContent = 'מטר חלקיקים נוצר!';
        }, showerStartTime);

        // --- Step 3: Cherenkov Cone (starts slightly after shower initiation) ---
         const coneStartTime = showerStartTime + 400; // Start shortly after shower begins
         const coneStartLeft = showerStartLeft; // Cone starts horizontally where shower began

         setTimeout(() => {
             const coneElement = document.getElementById('cherenkovCone');
             coneElement.style.left = coneStartLeft + '%'; // Position cone origin at shower X

             const totalFallHeight = flashTargetY - atmospherePixelTop; // Height from atmosphere line to flash level
             const coneAngleRad = Math.PI / 10; // Example cone angle (18 degrees) - adjust for visual effect
             const finalConeBaseWidth = totalFallHeight * Math.tan(coneAngleRad); // Width at the flash level

             // Animate cone dimensions
             coneElement.style.transition = `border-top-width 0.8s linear, border-left-width 0.8s linear, border-right-width 0.8s linear, opacity 0.6s ease-out`;
             coneElement.style.opacity = '1';
             coneElement.style.borderTopWidth = `${totalFallHeight}px`;
             coneElement.style.borderLeftWidth = `${finalConeBaseWidth}px`;
             coneElement.style.borderRightWidth = `${finalConeBaseWidth}px`;

             detectionStatusElement.textContent = 'קרינת צ\'רנקוב נוצרת!';
         }, coneStartTime);


        // --- Step 4: Cherenkov Flash Detected (when cone hits telescope level) ---
        const flashStartTime = coneStartTime + 800; // Appears as cone reaches the ground level
        const flashStartLeft = coneStartLeft; // Flash appears below the shower origin horizontally

        setTimeout(() => {
            cherenkovFlash.style.top = `${flashTargetY}px`; // Position flash vertically just above mirror
            cherenkovFlash.style.left = flashStartLeft + '%'; // Position flash horizontally under shower origin

            cherenkovFlash.style.transition = 'width 0.3s ease-out, height 0.3s ease-out, opacity 0.4s ease-out';
            cherenkovFlash.style.opacity = '1';
            cherenkovFlash.style.width = '100px'; // Size of the detected flash on camera
            cherenkovFlash.style.height = '100px';
            detectionStatusElement.textContent = 'הבזק צ\'רנקוב נקלט!';


             // Fade out the flash after a short display and complete animation cycle
            setTimeout(() => {
                 cherenkovFlash.style.transition = 'opacity 0.5s ease-out';
                 cherenkovFlash.style.opacity = '0';
                  detectionStatusElement.textContent = 'נאגוד נתונים... מוכן לקריאה הבאה!';
                 isAnimating = false; // Allow new animation after fade out
                 instructionElement.style.opacity = '1'; // Show instruction again
            }, 1200); // Flash visible for 1.2 second

        }, flashStartTime);
    }

    // Toggle explanation visibility
    explanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        explanationButton.textContent = isHidden ? 'הסתר את הסוד מאחורי הטלסקופ' : 'הצג/הסתר את הסוד מאחורי הטלסקופ';
    });

    // Allow clicking on the sky to trigger the simulation
    skyElement.addEventListener('click', (event) => {
        if (!isAnimating) {
             const skyRect = skyElement.getBoundingClientRect();
             const clickX = event.clientX - skyRect.left;
             const clickXPercent = (clickX / skyRect.width) * 100;
             startSimulation(clickXPercent);
        }
    });


    // Initial state setup (ensure elements are hidden/at start)
    resetSimulation();
    instructionElement.style.opacity = '1'; // Ensure instruction is visible initially

</script>
```