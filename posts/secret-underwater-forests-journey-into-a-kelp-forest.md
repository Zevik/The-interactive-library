---
title: "היערות התת-ימיים המופלאים: צלילה ליער קלפ"
english_slug: secret-underwater-forests-journey-into-a-kelp-forest
category: "מדעי הסביבה / אקולוגיה וקיימות"
tags: ["יער קלפ", "מערכת אקולוגית", "חיים ימיים", "מגוון ביולוגי", "אוקיינוס"]
---
<style>
/* --- כללי --- */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f0f8ff; /* Light blue background */
    direction: rtl; /* Ensure Hebrew is right-to-left */
    text-align: right;
}

h1, h2, h3 {
    color: #005f73; /* Dark Teal */
    text-align: center; /* Center titles */
    margin-bottom: 15px;
}

p {
    margin-bottom: 1em;
}

/* --- מיכל יער הקלפ (הסימולציה) --- */
.kelp-forest-container {
    width: 95%; /* Make it slightly wider */
    max-width: 850px; /* Allow a bit more space */
    margin: 30px auto; /* More margin top/bottom */
    border: 2px solid #0077b6; /* Stronger blue border */
    border-radius: 12px; /* Rounded corners */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* Stronger, softer shadow */
    overflow-y: scroll; /* Enable vertical scrolling for depth */
    height: 650px; /* Slightly taller view */
    position: relative;
    background: linear-gradient(to bottom, #48cae4 0%, #0096c7 50%, #023e8a 100%); /* Deeper, more vibrant water gradient */
    filter: saturate(1.1); /* Slightly more saturated colors */
}

.kelp-forest-interactive {
    position: relative;
    width: 100%;
    height: 1500px; /* Increased total height for more perceived depth */
    padding-top: 80px; /* More space above canopy */
    padding-bottom: 100px; /* More space below holdfasts */
    box-sizing: border-box; /* Include padding in total height */
}

/* Optional: Subtle bubbles animation */
.kelp-forest-interactive::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><circle cx="10%" cy="90%" r="3" fill="rgba(255,255,255,0.3)"><animate attributeName="cy" from="90%" to="10%" dur="10s" repeatCount="indefinite" begin="0s"/></circle><circle cx="30%" cy="80%" r="2" fill="rgba(255,255,255,0.3)"><animate attributeName="cy" from="80%" to="0%" dur="12s" repeatCount="indefinite" begin="1s"/></circle><circle cx="70%" cy="85%" r="4" fill="rgba(255,255,255,0.4)"><animate attributeName="cy" from="85%" to="5%" dur="11s" repeatCount="indefinite" begin="2s"/></circle><circle cx="50%" cy="95%" r="2.5" fill="rgba(255,255,255,0.35)"><animate attributeName="cy" from="95%" to="15%" dur="9s" repeatCount="indefinite" begin="0.5s"/></circle><circle cx="90%" cy="70%" r="3.5" fill="rgba(255,255,255,0.45)"><animate attributeName="cy" from="70%" to="-10%" dur="13s" repeatCount="indefinite" begin="3s"/></circle></svg>');
    z-index: 1; /* Behind interactive elements */
    pointer-events: none; /* Don't block clicks */
}


/* --- אלמנטים אינטראקטיביים: אורגניזמים וחלקי קלפ --- */
.organism, .kelp-part {
    position: absolute;
    width: 50px; /* Slightly larger clickable area */
    height: 50px;
    /* Default styling - will be overridden by specific styles */
    background-color: rgba(255, 255, 255, 0.6); /* Semi-transparent white */
    border-radius: 50%; /* Default shape: circle */
    border: 2px solid #0077b6; /* Blue border */
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8em; /* Slightly smaller text */
    font-weight: bold;
    color: #03045e; /* Dark blue text */
    text-align: center;
    padding: 5px; /* Add padding for text */
    box-sizing: border-box; /* Include padding in size */
    opacity: 0.9; /* Slightly less transparent */
    transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth transitions */
    z-index: 10; /* Ensure they are above background/bubbles */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    /* Add subtle bobbing animation */
    animation: bob 4s ease-in-out infinite;
}

/* Keyframes for bobbing animation */
@keyframes bob {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); } /* More pronounced bob */
}

.organism:hover, .kelp-part:hover {
    transform: scale(1.2) translateY(-4px); /* Scale up and lift slightly on hover */
    opacity: 1;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); /* Stronger shadow on hover */
}

/* Style for organisms (default circle) */
.organism {
    background-color: rgba(255, 159, 28, 0.7); /* Orangey-yellow with transparency */
    border-color: #e76f51; /* Salmon border */
    color: #333;
}

/* Specific styling for kelp parts */
.kelp-part {
     background-color: rgba(144, 238, 144, 0.8); /* Light green with transparency */
     border-color: #2a9d8f; /* Teal border */
     color: #004b23; /* Dark green text */
     border-radius: 8px; /* Slightly rounded rectangle */
}

/* Style the kelp stipe as a long band */
.kelp-part[data-name="גבעול (Stipe)"] {
    width: 15px; /* Wider stipe */
    height: calc(80% + 100px); /* Stretches along depth, adjusted for increased padding */
    background: linear-gradient(to top, rgba(0, 100, 0, 0.7) 0%, rgba(0, 128, 0, 0.8) 100%); /* Green gradient for stipe */
    border: none;
    border-radius: 8px; /* Rounded ends */
    left: 50%; /* Center it horizontally */
    transform: translateX(-50%); /* Adjust position */
    z-index: 5; /* Behind organisms */
    animation: grow 6s ease-in-out infinite; /* Optional: Subtle swaying animation */
    transform-origin: bottom; /* Anchor growth/sway at the bottom */
}

@keyframes grow {
    0%, 100% { height: calc(80% + 100px); }
    50% { height: calc(85% + 100px); } /* Slightly changes height */
}

/* Note: Stipe bobbing animation is overridden by its specific animation */
.kelp-part[data-name="גבעול (Stipe)"] { animation: sway 8s ease-in-out infinite; }
@keyframes sway {
    0%, 100% { transform: translateX(-50%) rotate(0deg); }
    25% { transform: translateX(-50%) rotate(2deg); }
    75% { transform: translateX(-50%) rotate(-2deg); }
}


.kelp-part[data-name="עלים (Blades)"] {
    width: 120px; /* Wider blades */
    height: 80px; /* Taller blades */
    border-radius: 15px; /* More rounded */
    background-color: rgba(0, 150, 0, 0.85); /* Vibrant green */
    border-color: #2d6a4f;
    animation: float 5s ease-in-out infinite; /* Different animation for blades */
}

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-5px) rotate(1deg); }
}


.kelp-part[data-name="שלפוחית אוויר (Pneumatocyst)"] {
     width: 30px; /* Slightly larger */
     height: 30px;
     background-color: rgba(255, 224, 102, 0.9); /* Brighter yellow */
     border-color: #ffc300; /* Gold border */
     border-radius: 50%;
     animation: bob 3s ease-in-out infinite alternate; /* Faster bobbing */
}

/* --- תיבת מידע --- */
.info-box {
    position: fixed; /* Fixed position relative to viewport */
    top: 50%;
    left: 20px; /* Position on the left */
    transform: translateY(-50%) translateX(-100%); /* Start off-screen left */
    width: 280px; /* Slightly wider */
    background-color: rgba(237, 246, 249, 0.98); /* Very light blue with transparency */
    border: 2px solid #0077b6; /* Blue border */
    border-radius: 10px; /* Rounded corners */
    padding: 20px; /* More padding */
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); /* Clear shadow */
    z-index: 20; /* Above everything */
    text-align: right;
    opacity: 0; /* Initially hidden */
    visibility: hidden; /* Initially not interactive */
    transition: transform 0.4s ease-out, opacity 0.4s ease-out, visibility 0.4s; /* Smooth slide/fade transition */
}

.info-box.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(-50%) translateX(0); /* Slide into view */
}


.info-box h3 {
    margin-top: 0;
    color: #003f7f; /* Darker blue */
    font-size: 1.2em; /* Slightly larger font */
    border-bottom: 1px solid #0077b6; /* Separator line */
    padding-bottom: 8px;
    margin-bottom: 10px;
}

.info-box p {
    margin-bottom: 0;
    color: #333;
    font-size: 1em; /* Standard font size */
    line-height: 1.5;
}

/* --- כפתור הסבר --- */
#toggle-explanation {
    display: block;
    margin: 30px auto; /* More margin */
    padding: 12px 25px; /* More padding */
    font-size: 1.1em; /* Larger text */
    cursor: pointer;
    background-color: #0096c7; /* Vibrant blue */
    color: white;
    border: none;
    border-radius: 6px;
    transition: background-color 0.3s ease, transform 0.1s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

#toggle-explanation:hover {
    background-color: #0077b6; /* Darker blue on hover */
}

#toggle-explanation:active {
    transform: scale(0.98); /* Push effect on click */
}


/* --- סעיף הסבר מפורט --- */
#explanation-section {
    margin: 20px auto;
    max-width: 800px;
    padding: 25px; /* More padding */
    border: 1px solid #b3cde0; /* Lighter border */
    border-radius: 8px;
    background-color: #e7f5ff; /* Very light blue background */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out; /* Smooth toggle animation */
    overflow: hidden; /* Hide overflow during animation */
    max-height: 0; /* Initially collapsed */
    opacity: 0; /* Initially invisible */
}

#explanation-section.visible {
    max-height: 2000px; /* Sufficient height to show content, adjust if needed */
    opacity: 1;
}

#explanation-section h2 {
    color: #005f73; /* Dark Teal */
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 1.4em;
    border-bottom: 1px dashed #0096c7; /* Dashed separator */
    padding-bottom: 5px;
}

#explanation-section p {
    margin-bottom: 18px; /* More space between paragraphs */
    line-height: 1.7;
    color: #333;
    text-align: right;
}

#explanation-section strong {
    color: #023e8a; /* Dark blue */
}

</style>

<h1>מסע מופלא אל היערות הכחולים: גלו את סודות יערות הקלפ</h1>
<p>האם דמיינתם אי פעם יערות עבותים מתחת לפני המים? ובכן, הם קיימים! הצטרפו אלינו למסע וירטואלי מרתק אל יער קלפ - מערכת אקולוגית תת-ימית שוקקת חיים ומלאת פלאים. לחצו על האורגניזמים השונים וחלקי הקלפ כדי לגלות מי חי כאן ולמה המקום הזה כל כך מיוחד וחיוני.</p>

<div class="kelp-forest-container">
    <div class="kelp-forest-interactive">
        <!-- Bottom/Holdfast layer -->
        <div class="organism" data-name="קיפוד ים" data-desc='"גנן הים" או "מזיק על": אוכל אצות ראשוני. תפקידו חיוני בוויסות גידול האצות, אך התרבות יתר שלו עלולה להרוס את יער הקלפ כולו. טעים ללוטרות ים!' style="bottom: 15%; left: 60%;"></div>
        <div class="organism" data-name="כוכב ים" data-desc="טורף איטי אך יעיל: צרכן שניוני חשוב, ניזון מקיפודי ים, צדפות ואורגניזמים ישיבים אחרים. שומר על איזון המערכת." style="bottom: 10%; left: 30%;"></div>
        <div class="kelp-part" data-name="שורש אחיזה (Holdfast)" data-desc="עוגן הקלפ: לא שורש אמיתי! מבנה חזק דמוי שורש הנאחז בחוזקה בסלעים על קרקעית הים, בדרך כלל בעומק של עד 30 מטר, ומעגן את הצמח למקומו." style="bottom: 5%; left: 45%; width: 80px; height: 50px; border-radius: 15px;"></div>

        <!-- Stipe layer -->
        <div class="kelp-part" data-name="גבעול (Stipe)" data-desc="הגזע הגמיש: צינור חזק וגמיש הצומח במהירות מטורפת כלפי מעלה לעבר פני המים. יכול להגיע לעשרות מטרים, ומספק בית גידול ומקום היצמדות ליצורים קטנים." style="bottom: 5%; left: 50%; height: 90%;"></div>
        <div class="organism" data-name="סרטן" data-desc="מסתתר בסבך: יצורים קטנים וזריזים החיים בין גבעולי הקלפ. ניזונים משאריות, אורגניזמים קטנים יותר ופלנקטון." style="bottom: 40%; left: 70%;"></div>
        <div class="organism" data-name="דג ריף צעיר" data-desc="משתלת הקלפ: מוצא מקלט מושלם בין גבעולי הקלפ הסבוכים מפני טורפים גדולים. ניזון מאצות קטנות ואורגניזמים מיקרוסקופיים." style="bottom: 55%; left: 35%;"></div>


        <!-- Water Column layer -->
        <div class="organism" data-name="דג ריף בוגר" data-desc="שייטים בעמודת המים: דגים בגודל בינוני השוחים במרחב שבין הגבעולים, צדים דגים קטנים יותר וחסרי חוליות." style="top: 30%; left: 25%;"></div>
         <div class="organism" data-name="דג גדול יותר (טורף)" data-desc="שועל הים: טורפים גדולים כמו דגי בס או גרופר שחודרים ליער הקלפ כדי לצוד דגים קטנים יותר." style="top: 50%; left: 75%;"></div>

        <!-- Canopy/Surface layer -->
        <div class="kelp-part" data-name="עלים (Blades)" data-desc="מפעלי האנרגיה: החלקים הרחבים והשטוחים המבצעים פוטוסינתזה אינטנסיבית. צפים קרוב לפני המים כדי לקלוט מקסימום אור שמש. בסיס שרשרת המזון." style="top: 10%; left: 40%; width: 150px; height: 100px; border-radius: 20px;"></div>
         <div class="kelp-part" data-name="שלפוחית אוויר (Pneumatocyst)" data-desc="מצוף ההישרדות: כיס קטן ומלא גז הנמצא בבסיס העלים. מסייע לקלפ כולו לצוף ולהישאר זקוף בעמודת המים, קרוב לאור השמש." style="top: 12%; left: 58%; width: 35px; height: 35px;"></div>
        <div class="organism" data-name="לוטרת ים" data-desc="שומרת היער: טורף על חיוני. ניזונה בעיקר מקיפודי ים, ובכך מונעת מהם להרוס את יער הקלפ. נוכחותה מעידה על מערכת אקולוגית בריאה." style="top: 15%; left: 20%;"></div>
         <div class="organism" data-name="ציפור ים" data-desc="ציידת מעל ומתחת: ציפורים כמו שחפים או קורמורנים שמחפשות דגים קטנים או חסרי חוליות באזור החופה, לעיתים צוללות לתפוס אותם." style="top: 5%; left: 80%;"></div>


        <!-- Info box -->
        <div class="info-box">
            <h3 id="info-box-name">צללו פנימה וגלו!</h3>
            <p id="info-box-desc">לחצו על כל אורגניזם או חלק של הקלפ בסימולציה כדי ללמוד עליו פרטים מרתקים.</p>
        </div>
    </div>
</div>

<button id="toggle-explanation">למד עוד על יערות הקלפ (הצג/הסתר הסבר מפורט)</button>

<div id="explanation-section">
    <h2>מהו יער קלפ ולמה הוא נקרא יער?</h2>
    <p>יער קלפ הוא מערכת אקולוגית תת-ימית מרהיבה, הנוצרת על ידי ריכוזים צפופים וגדולים של אצות חומות ענקיות הנקראות קלפ. הקלפ יכול לצמוח במהירות מסחררת ולהגיע לגבהים של עשרות מטרים, וליצור מבנה תלת-ממדי מורכב שמזכיר להפליא יערות יבשתיים - עם בסיס נאחז ("שורש" אחיזה), "גזעים" ארוכים (גבעולים) ו"חופה" צפופה של עלים הצפים קרוב לפני המים. המבנה הייחודי הזה מספק בית גידול מגוון ומקלט בטוח לאינספור יצורים ימיים, קטנים כגדולים.</p>

    <h2>מבנה הקלפ: עוגן, גזע, עלים ומצופים.</h2>
    <p>לקלפ מספר חלקים עיקריים, שלכל אחד תפקיד חיוני בהישרדותו ובשגשוגו: <strong>שורש האחיזה (Holdfast)</strong> - מבנה דמוי שורש חזק שמעגן את הקלפ בחוזקה לקרקעית סלעית. חשוב להדגיש שאינו סופג מים או חומרים מזינים כמו שורש של צמח רגיל - הקלפ קולט הכל ישירות מהמים דרך כל חלקיו! <strong>הגבעול (Stipe)</strong> - מבנה גמיש אך חזק דמוי גזע, הצומח כלפי מעלה מהשורש האחיזה לעבר האור בפני המים. הוא מספק תמיכה מבנית לקלפ ומשמש בסיס להיצמדות לאורגניזמים קטנים רבים. <strong>העלים (Blades)</strong> - החלקים הרחבים והשטוחים של הקלפ, המזכירים עלים, והם האתר העיקרי של הפוטוסינתזה. כאן הקלפ קולט אור שמש ופחמן דו-חמצני מהמים כדי לייצר אנרגיה. <strong>שלפוחיות אוויר (Pneumatocysts)</strong> - שלפוחיות קטנות ומלאות גז הממוקמות בבסיס העלים. הן פועלות כמצופים טבעיים, מסייעות לעלים ולגבעול להישאר זקופים ולצוף קרוב ככל האפשר לפני המים שטופי השמש.</p>

    <h2>שכבות החיים: מי גר היכן ביער הקלפ?</h2>
    <p>בדומה ליער יבשתי, גם יער הקלפ מחולק לשכבות חיים מובחנות, שלכל אחת קהילת יצורים משלה: <strong>הקרקעית (Holdfast Zone)</strong> - הבסיס הסלעי ויער 'שורשי' האחיזה הצפוף. כאן חיים יצורים הנאחזים בסלעים או מסתתרים במרווחים, כמו קיפודי ים, כוכבי ים, סרטנים, שושנות ים ודגים קטנים. <strong>עמודת המים (Stipe Zone)</strong> - המרחב התלת-ממדי בין הגבעולים הזקופים. זהו אזור שחייה לדגים שונים (מדגי ריף קטנים ועד טורפים גדולים יותר), מקום היצמדות לאלמוגים רכים וספוגים, וציר תנועה לבעלי חיים העוברים בין הקרקעית לחופה. <strong>החופה (Canopy)</strong> - השכבה הצפופה של עלים הצפים סמוך מאוד לפני המים, היכן שהאור חזק ביותר. זוהי 'גג' היער, והיא עשירה בחיים: משתלה לדגים צעירים, מקלט מחסרי חוליות רבים, ואזור פעילות לטורפים כמו לוטרות ים וציפורי ים הצוללות לציד.</p>

    <h2>רשת החיים ביער הקלפ: מגוון ביולוגי ותפקידים.</h2>
    <p>יערות קלפ הם מהמערכות האקולוגיות הפוריות והמגוונות ביותר באוקיינוס: <strong>יצרנים ראשיים:</strong> הקלפ עצמו הוא היצרן הראשי, הממיר את אנרגיית השמש לאנרגיה כימית באמצעות פוטוסינתזה, ומהווה את הבסיס לרשת המזון. <strong>צרכנים ראשוניים (אוכלי עשב):</strong> יצורים הניזונים ישירות מהקלפ או אצות אחרות, כגון קיפודי ים, חלזונות מסוימים ודגים מסוימים. <strong>צרכנים שניוניים (טורפים):</strong> ניזונים מאוכלי העשב או מטורפים קטנים יותר. קבוצה זו כוללת כוכבי ים, סרטנים רבים, ורוב דגי הריף. <strong>טורפי על:</strong> עומדים בראש שרשרת המזון ושולטים על גודל אוכלוסיות הטורפים הנמוכים מהם. לוטרות ים, למשל, הן טורפי על קריטיים ביערות קלפ, שכן טרפתן העיקרית היא קיפודי הים. על ידי ויסות אוכלוסיית הקיפודים, הלוטרות מונעות מהם להרוס את יער הקלפ ושומרות על בריאות המערכת כולה.</p>

    <h2>החשיבות העצומה של יערות הקלפ: לא רק לחיות הים.</h2>
    <p>יערות הקלפ אינם רק יפים ושוקקי חיים; הם חיוניים לבריאות האוקיינוסים וכדור הארץ: <strong>מוקד מגוון ביולוגי:</strong> הם מספקים בית גידול, מקלט ומקור מזון לאלפי מינים של דגים, חסרי חוליות, יונקים ימיים וציפורים. רבים ממינים אלו הם בעלי חשיבות מסחרית או אקולוגית עצומה. <strong>משתלות טבעיות:</strong> מבנה היער הצפוף משמש אזור אידיאלי לדגים צעירים ולפגיות של חסרי חוליות לגדול ולהתפתח הרחק מטורפים. <strong>הגנה על חופים:</strong> יערות הקלפ הסמוכים לחוף בולמים ומפחיתים את עוצמת הגלים, ובכך מגינים על קווי החוף מפני שחיקה וסופות. <strong>מאבק במשבר האקלים:</strong> הקלפ צומח מהר מאוד וסופג כמויות גדולות של פחמן דו-חמצני (CO2) מהאטמוספירה ומהאוקיינוס בתהליך הפוטוסינתזה, ובכך מהווה 'בולען פחמן' טבעי המסייע בהפחתת גזי חממה.</p>

    <h2>איומים והגנה: האתגרים העומדים בפני יערות הקלפ.</h2>
    <p>למרות חוסנם, יערות הקלפ רגישים למגוון הולך וגובר של איומים, רובם קשורים לפעילות אדם: <strong>שינויי אקלים:</strong> התחממות מי הים וגלי חום ימיים פוגעים ישירות ביכולת הקלפ לגדול ולשרוד. החמצת האוקיינוסים מקשה על אורגניזמים רבים ביער, כמו קיפודי ים וצדפות, לבנות את שלדיהם. <strong>זיהום:</strong> נגר עירוני ותעשייתי המכיל חומרים מזינים ורעלים פוגע באיכות המים ומעודד גידול יתר של אצות קטנות שמתחרות בקלפ. <strong>דיג יתר:</strong> פגיעה באוכלוסיות טורפי על (כמו לוטרות ים או דגים גדולים) משבשת את שרשרת המזון הטבעית ועלולה להוביל לפיצוץ אוכלוסין של אוכלי עשב (כמו קיפודי ים), שמכריעים ואוכלים את יער הקלפ עד היסוד ('מדבריות קיפודים'). <strong>מינים פולשים:</strong> מינים חדשים המגיעים לאזור יכולים להתחרות בקלפ המקומי או לטרוף את בעלי החיים שבו. <strong>דרכי שימור:</strong> הגנה על יערות הקלפ דורשת מאמץ משולב הכולל הקמת אזורים ימיים מוגנים (שמורות טבע), בקרת זיהום קפדנית, ניהול דיג בר-קיימא, ומאמצי שיקום פעילים של יערות שנפגעו, כולל השבת מינים חיוניים כמו לוטרות ים.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const infoBox = document.querySelector('.info-box');
    const infoBoxName = document.getElementById('info-box-name');
    const infoBoxDesc = document.getElementById('info-box-desc');
    const clickableElements = document.querySelectorAll('.organism, .kelp-part');
    const toggleButton = document.getElementById('toggle-explanation');
    const explanationSection = document.getElementById('explanation-section');

    // State for info box visibility
    let infoBoxTimeout;

    // Function to show info box
    const showInfoBox = (name, desc) => {
        // Clear any previous timeout to prevent flickering
        clearTimeout(infoBoxTimeout);

        infoBoxName.textContent = name;
        infoBoxDesc.textContent = desc;

        // Add class to trigger CSS transition
        infoBox.classList.add('visible');

        // Optional: Hide the info box after a few seconds of inactivity
        // infoBoxTimeout = setTimeout(() => {
        //     infoBox.classList.remove('visible');
        // }, 10000); // Hide after 10 seconds
    };

    // Function to hide info box (if needed, currently it just changes content on next click)
    // const hideInfoBox = () => {
    //      infoBox.classList.remove('visible');
    //      clearTimeout(infoBoxTimeout);
    // }


    // Event listeners for clickable elements
    clickableElements.forEach(element => {
        element.addEventListener('click', () => {
            const name = element.dataset.name;
            const desc = element.dataset.desc;
            showInfoBox(name, desc);

             // Optional: Add a temporary class to the clicked element for a visual effect
             element.classList.add('clicked');
             setTimeout(() => {
                 element.classList.remove('clicked');
             }, 300); // Remove class after 300ms
        });
    });

    // Event listener for the explanation toggle button
    toggleButton.addEventListener('click', () => {
        const isVisible = explanationSection.classList.contains('visible');

        if (isVisible) {
            explanationSection.classList.remove('visible');
            toggleButton.textContent = 'למד עוד על יערות הקלפ (הצג הסבר מפורט)';
        } else {
            explanationSection.classList.add('visible');
            toggleButton.textContent = 'למד עוד על יערות הקלפ (הסתר הסבר מפורט)';
        }
    });

    // Initial state: Show default info box message
    // The info box is initially hidden by CSS and shown on first click.
    // We can pre-fill the initial message here if we want it to appear immediately
    // showInfoBox('צללו פנימה וגלו!', 'לחצו על כל אורגניזם או חלק של הקלפ בסימולציה כדי ללמוד עליו פרטים מרתקים.');
    // Or keep it hidden until interaction, as per the current CSS/JS logic which feels more interactive.

     // Add a 'clicked' style in CSS if you added the class toggling above
     /*
     .organism.clicked, .kelp-part.clicked {
         animation: pulse 0.5s ease;
     }
     @keyframes pulse {
         0%, 100% { transform: scale(1.2); }
         50% { transform: scale(1.3); }
     }
     */
     // Note: Added scale(1.2) to the base hover, adjust pulse if implemented.
     // Let's rely on the improved hover effect and info box transition for feedback.
});
</script>
```