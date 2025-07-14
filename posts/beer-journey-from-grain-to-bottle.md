---
title: "מסע קסום: לידתה של בירה מגרעין ועד בקבוק"
english_slug: beer-journey-from-grain-to-bottle
category: "מדעי המזון"
tags:
  - בירה
  - בישול בירה
  - תהליך ייצור
  - התססה
  - כימיה
---
<h1>מסע קסום: לידתה של בירה מגרעין ועד בקבוק</h1>

<p>הבירה, המשקה שמאחד תרבויות וסיפורים ברחבי העולם. איך קורה שהקסם הזה מתחיל בגרעין צנוע והופך לנוזל הזהוב המבעבע שאנחנו כל כך אוהבים? בואו נצא למסע קסום ונפענח את סודות תהליך הבישול, שלב אחר שלב.</p>

<div class="beer-journey-app">
    <div class="timeline" id="beer-timeline">
        <div class="step" data-step="malting">הלתת</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="mashing">מעיכה</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="lautering">סינון</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="boiling">רתיחה</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="cooling">קירור</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="fermentation">תסיסה</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="conditioning">יישון</div>
        <div class="arrow"><span>&rarr;</span></div>
        <div class="step" data-step="packaging">ביקבוק</div>
    </div>
    <div class="display-area" id="step-display">
        <!-- Step content and visual representation will be loaded here by JS -->
        <div class="process-visual">
            <!-- Dynamic visual element controlled by CSS/JS -->
        </div>
        <div class="process-text">
            <h3 class="step-title"></h3>
            <p class="step-description"></p>
        </div>
    </div>
</div>

<style>
    :root {
        --beer-gold: #ffcc00;
        --beer-dark-gold: #ffa500;
        --beer-brown: #a0522d;
        --beer-light-brown: #cd853f;
        --neutral-bg: #f5f5dc; /* Beige */
        --neutral-border: #d2b48c; /* Tan */
        --dark-text: #333;
        --light-text: #fff;
        --shadow: rgba(0, 0, 0, 0.1);
    }

    .beer-journey-app {
        direction: rtl;
        font-family: 'Arial', sans-serif; /* More common/clean font */
        margin-top: 20px;
        border: 1px solid var(--neutral-border);
        padding: 20px; /* Slightly more padding */
        border-radius: 12px; /* More rounded corners */
        background-color: var(--neutral-bg);
        box-shadow: 0 4px 8px var(--shadow); /* Add subtle shadow */
    }

    .timeline {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px; /* More space */
        overflow-x: auto;
        padding-bottom: 15px; /* More padding below for scrollbar */
        scrollbar-width: thin; /* Thinner scrollbar */
        scrollbar-color: var(--beer-dark-gold) var(--neutral-border); /* Style scrollbar */
    }

    .timeline::-webkit-scrollbar {
        height: 8px;
    }

    .timeline::-webkit-scrollbar-track {
        background: var(--neutral-border);
        border-radius: 10px;
    }

    .timeline::-webkit-scrollbar-thumb {
        background-color: var(--beer-dark-gold);
        border-radius: 10px;
        border: 2px solid var(--neutral-bg);
    }


    .step {
        flex: 1;
        text-align: center;
        padding: 12px 8px; /* More padding */
        cursor: pointer;
        border: 2px solid var(--neutral-border); /* Slightly thicker border */
        border-radius: 8px;
        background-color: #fff; /* White steps */
        color: var(--dark-text);
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.2s ease; /* Add transform transition */
        min-width: 90px; /* Slightly wider steps */
        white-space: nowrap;
        font-size: 0.95em; /* Slightly larger font */
        font-weight: bold; /* Steps text bolder */
        user-select: none; /* Prevent text selection */
    }

    .step.active {
        background-color: var(--beer-gold); /* Beer color */
        border-color: var(--beer-dark-gold);
        color: var(--dark-text); /* Keep text dark for contrast */
        transform: translateY(-3px); /* Subtle lift */
        box-shadow: 0 3px 6px var(--shadow);
    }

    .step:hover:not(.active) {
        background-color: #fff8dc; /* Lighter hover */
        border-color: var(--beer-gold);
    }

    .step:active {
        transform: translateY(0); /* Press effect */
        box-shadow: none;
    }


    .arrow {
        padding: 0 8px; /* More padding */
        font-size: 1.5em; /* Larger arrow */
        color: var(--beer-dark-gold); /* Match beer color */
        animation: arrow-pulse 1.5s infinite ease-in-out; /* Subtle animation */
    }

    @keyframes arrow-pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
    }


    .display-area {
        border: 1px solid var(--neutral-border);
        padding: 20px; /* More padding */
        border-radius: 8px;
        background-color: #fff;
        min-height: 200px; /* More space for visuals */
        display: flex; /* Use flexbox for layout */
        gap: 20px; /* Space between visual and text */
        align-items: flex-start; /* Align items to the top */
    }

    .process-visual {
        flex-shrink: 0; /* Don't shrink */
        width: 150px; /* Fixed width for visual area */
        height: 150px; /* Fixed height */
        background-color: #eee; /* Placeholder background */
        border-radius: 8px;
        position: relative; /* Needed for absolute positioning of animations */
        overflow: hidden; /* Hide overflowing animation elements */
        border: 1px dashed var(--neutral-border); /* Indicate it's a placeholder/visual */
        display: flex; /* Use flex for centering/positioning internal elements */
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        color: #666;
        text-align: center;
    }

    .process-text {
        flex-grow: 1; /* Take remaining space */
    }

    .display-area h3 {
        margin-top: 0;
        color: var(--beer-dark-gold); /* Match step color */
        margin-bottom: 10px;
        font-size: 1.4em;
    }

    .display-area p {
        color: var(--dark-text);
        line-height: 1.6;
        font-size: 1.1em;
    }

    /* --- Visual Animations --- */
    /* Malting: Represents grain transformation */
    .process-visual.malting {
        background: linear-gradient(to bottom, #f0d9b5, var(--beer-light-brown)); /* Grain color change */
    }

    /* Mashing: Represents mixing and sugar extraction */
    .process-visual.mashing {
        background: linear-gradient(to bottom, var(--beer-light-brown) 50%, var(--beer-gold) 50%); /* Grain & Wort */
        animation: mash-mix 2s infinite linear;
    }
    @keyframes mash-mix {
        0% { background-position: 0% 0%; }
        100% { background-position: 0% -100%; } /* Simulate downward movement */
    }

    /* Lautering: Represents separation */
    .process-visual.lautering {
        background: linear-gradient(to top, var(--beer-brown) 30%, var(--beer-gold) 30%); /* Layers */
        position: relative;
    }
    .process-visual.lautering::after {
        content: '';
        position: absolute;
        top: 30%; /* Starting point of separation */
        left: 0;
        right: 0;
        height: 5px;
        background-color: rgba(255, 255, 255, 0.5); /* White line indicating separation */
        animation: separate 1.5s ease-in-out;
    }
    @keyframes separate {
        0% { transform: scaleX(0); }
        100% { transform: scaleX(1); }
    }

    /* Boiling: Represents heat and hop addition */
    .process-visual.boiling {
        background-color: var(--beer-gold);
        position: relative;
        overflow: visible; /* Allow bubbles to go outside */
    }
    .process-visual.boiling::before, .process-visual.boiling::after {
        content: '';
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 50%;
        animation: bubble 1.5s infinite linear;
        bottom: 0;
        opacity: 0;
    }
    .process-visual.boiling::before { left: 20%; animation-delay: 0s; }
    .process-visual.boiling::after { left: 60%; animation-delay: 0.5s; width: 8px; height: 8px; }
    @keyframes bubble {
        0% { bottom: 0; opacity: 0.5; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
        100% { bottom: 100%; opacity: 0; transform: scale(1); }
    }


    /* Cooling: Represents temperature drop */
    .process-visual.cooling {
        background: linear-gradient(to bottom, #ffcc00, #ffcc00); /* Start color */
        animation: cool-down 1.5s ease-out forwards;
    }
    @keyframes cool-down {
        0% { background: linear-gradient(to bottom, #ffcc00, #ffcc00); }
        100% { background: linear-gradient(to bottom, #ffeb7f, #ffcc00); } /* Subtle color shift */
    }


    /* Fermentation: Represents yeast activity and bubbling */
    .process-visual.fermentation {
        background-color: var(--beer-gold);
        position: relative;
        overflow: visible; /* Allow bubbles to go outside */
    }
    .process-visual.fermentation::before, .process-visual.fermentation::after,
    .process-visual.fermentation .ferment-bubble1, .process-visual.fermentation .ferment-bubble2 {
        content: '';
        position: absolute;
        width: 8px;
        height: 8px;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 50%;
        animation: ferment-bubble 2s infinite linear;
        bottom: 0;
        opacity: 0;
    }
     .process-visual.fermentation::before { left: 15%; animation-delay: 0s; width: 6px; height: 6px;}
     .process-visual.fermentation::after { left: 45%; animation-delay: 0.7s; }
     .process-visual.fermentation .ferment-bubble1 { left: 75%; animation-delay: 1.4s; width: 7px; height: 7px; }
     .process-visual.fermentation .ferment-bubble2 { left: 30%; animation-delay: 0.3s; width: 5px; height: 5px; }

    @keyframes ferment-bubble {
        0% { bottom: 0; opacity: 0.6; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
        100% { bottom: 100%; opacity: 0; transform: scale(1); }
    }


    /* Conditioning: Represents settling and clarification */
    .process-visual.conditioning {
        background: linear-gradient(to bottom, rgba(255, 204, 0, 0.8) 70%, rgba(160, 82, 45, 0.5) 70%); /* Simulate clarity */
        animation: settle 3s ease-out forwards;
    }
     @keyframes settle {
        0% { background-position: 0% 0%; }
        100% { background-position: 0% -20%; } /* Simulate sediment settling */
    }


    /* Packaging: Final product */
    .process-visual.packaging {
         background: linear-gradient(to top, var(--beer-gold), #ffeb7f); /* Clear beer gradient */
         position: relative;
         overflow: visible; /* Allow bubbles to escape */
    }
     .process-visual.packaging::before, .process-visual.packaging::after {
        content: '';
        position: absolute;
        width: 5px;
        height: 5px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        animation: fizz 3s infinite linear;
        bottom: 10%; /* Start above bottom */
        opacity: 0;
    }
     .process-visual.packaging::before { left: 30%; animation-delay: 0s; }
     .process-visual.packaging::after { left: 70%; animation-delay: 1s; width: 4px; height: 4px; }

    @keyframes fizz {
        0% { bottom: 10%; opacity: 0.5; }
        100% { bottom: 100%; opacity: 0; }
    }


    /* Reset animation on step change */
     .process-visual:not(.malting):not(.mashing):not(.lautering):not(.boiling):not(.cooling):not(.fermentation):not(.conditioning):not(.packaging) {
        animation: none !important;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More margin */
        padding: 12px 20px; /* More padding */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 8px; /* More rounded */
        background-color: var(--beer-dark-gold); /* Match design */
        color: var(--dark-text); /* Dark text on button */
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
    }

    #toggle-explanation:hover {
        background-color: #ffbf00;
        transform: translateY(-1px);
    }
     #toggle-explanation:active {
         transform: translateY(0);
     }


    .explanation {
        border: 1px solid var(--neutral-border);
        padding: 20px; /* More padding */
        margin-top: 20px;
        border-radius: 12px;
        background-color: #fff8dc; /* Lighter background for explanation */
        display: none; /* Hidden by default */
        box-shadow: 0 2px 4px var(--shadow);
    }

    .explanation h2, .explanation h3 {
        color: var(--beer-dark-gold);
        border-bottom: 1px solid var(--neutral-border); /* Separator */
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    .explanation h2 { font-size: 1.6em; }
    .explanation h3 { font-size: 1.3em; color: var(--beer-brown);}


    .explanation p {
        color: var(--dark-text);
        line-height: 1.7; /* More space between lines */
        margin-bottom: 15px;
    }

</style>

<button id="toggle-explanation">לחשוף את סודות הבירה! (הסבר מפורט)</button>

<div class="explanation" id="detailed-explanation">
    <h2>המסע נחשף: שלבי הקסם של יצירת הבירה</h2>

    <h3>מבוא קצר: הגיבורים של תהליך הבישול</h3>
    <p>בירה היא לא רק משקה, היא תוצר של כימיה, ביולוגיה ואמנות עתיקה. ארבעה גיבורים עיקריים שותפים ליצירה: המים - הבמה לכל התהליך; הדגנים (בעיקר שעורה מולתתת) - מספקים את הסוכרים הדרושים למסיבה; הכשות - מוסיפה ארומה, מרירות נעימה ושומרת על הטריות; והשמרים - האמנים הזעירים שהופכים את הסוכרים לאלכוהול וגיזוז. יחד, הם יוצאים למסע מרתק.</p>

    <h3>שלב 1: הלתת (Malting) - להעיר את הגרעין</h3>
    <p>הכל מתחיל בגרעין השעורה. בשלב הלתת, הגרעינים מושרים במים כדי להתחיל נביטה. זהו טריק קסום מהטבע: הנביטה מפעילה אנזימים חבויים בגרעין, שתפקידם יהיה לפרק בהמשך את העמילנים המורכבים לסוכרים פשוטים (הדלק של השמרים!). כדי לשמר את הכוח האנזימטי הזה בדיוק ברגע הנכון, עוצרים את הנביטה בייבוש בחום (kilning). טמפרטורת הייבוש תשפיע גם על צבע וטעמי הקליה של הגרעין, ותתן את הבסיס לגוון ולטעם של הבירה הסופית, מבהיר ועד כהה כמו שוקולד.</p>

    <h3>שלב 2: המעיכה (Mashing) - מרק הסוכר המתוק</h3>
    <p>עכשיו כשהגרעינים "ערים" ואנזימים מוכנים, מגיע זמן המעיכה. הגרעינים המולתתים נטחנים גס ומעורבבים עם מים חמים בטמפרטורות מדויקות (בדרך כלל סביב 62-70 מעלות צלזיוס). כאן מתרחש הקסם האנזימטי: האנזימים שהופעלו בהלתת מתחילים לפרק את העמילנים הגדולים לסוכרים קטנים ומסיסים, בעיקר מלטוז. התוצאה היא נוזל מתוק ומלא הבטחה שנקרא "וורט" (Wort).</p>

    <h3>שלב 3: הסינון (Lautering) - להפריד את הטוב מהמוצק</h3>
    <p>אחרי שהסוכרים הומסו בוורט, צריך להפריד את הנוזל המתוק מהשאריות המוצקות של הגרעינים (שנקראות Spent Grains). תהליך הסינון (Lautering) עושה בדיוק את זה. הוורט מסונן, לרוב דרך שכבה טבעית של הגריינס עצמם שמשמשת כמסנן טבעי. לעיתים שוטפים את הגריינס במים חמים נוספים (Sparge) כדי לוודא שכל טיפת סוכר נוצלה.</p>

    <h3>שלב 4: הרתיחה (Boiling) - טיהור והוספת אופי</h3>
    <p>הוורט הצלול מועבר למיכל הרתיחה ומתחיל להתבשל בעוצמה במשך שעה עד שעה וחצי. זוהי תחנת טיהור ועיצוב טעם: הרתיחה הורגת חיידקים לא רצויים (חיטוי!), מאדה חומרים נדיפים שעלולים לפגוע בטעם, והכי חשוב - זה הזמן להוסיף את הכשות! הוספת כשות בתחילת הרתיחה תעניק לבירה מרירות נקייה, והוספה בסופה או אחרי כיבוי האש תעניק לה ארומות פרחוניות, פירותיות או עשבוניות נפלאות.</p>

    <h3>שלב 5: הקירור (Cooling) - להכין את הבמה לשמרים</h3>
    <p>מיד לאחר הרתיחה, הוורט רותח וחם מדי בשביל האורחים הבאים שלנו - השמרים העדינים. יש לקרר אותו במהירות לטמפרטורת החדר או קצת פחות (בדרך כלל 18-24°C לאיילים או 8-14°C ללאגרים). קירור מהיר חיוני למניעת זיהומים חיידקיים ולשקיעת חלבונים וטאנינים שהתגבשו בחום. המטרה: סביבה מושלמת לשמרים.</p>

    <h3>שלב 6: התסיסה (Fermentation) - הקסם הביולוגי מתחיל</h3>
    <p>הוורט המקורר מועבר למיכל התסיסה, וזה הרגע הגדול של השמרים! מוסיפים את זן השמרים המתאים, והם מתחילים במלאכתם: המרת הסוכרים שבוורט לאלכוהול ולפחמן דו-חמצני. המיכל מתחיל לבעבע בעדינות, עדות לעבודה המאומצת בפנים. תהליך זה נמשך בדרך כלל שבוע עד שלושה שבועות, והוא הלב הפועם של ייצור הבירה, זה שמעניק לה את האלכוהול והגיזוז הראשוני.</p>

    <h3>שלב 7: היישון (Conditioning) - הזמן עושה את שלו</h3>
    <p>אחרי שהשמרים סיימו את רוב עבודתם, הבירה הצעירה עוברת לשלב מנוחה וגיבוש טעמים. היישון יכול לכלול העברה למיכל אחר, קירור לטמפרטורות נמוכות יותר (ליצירת לאגרים חלקים במיוחד), או הוספת מרכיבים נוספים לטעם כמו שבבי עץ אלון. שלב זה מאפשר לטעמים להתפתח, להתעגל, למשקעים לשקוע, וטעמי לוואי קלים להיעלם. זהו השלב בו הבירה מקבלת את הליטוש הסופי לפני שתהיה מוכנה לקהל.</p>

    <h3>שלב 8: הביקבוק/אריזה (Packaging) - מוכנה למסיבה!</h3>
    <p>המסע כמעט הושלם! הבירה המיושנת והמוכנה מוכנסת לאריזתה הסופית – בקבוקים, פחיות או חביות. לעיתים קרובות מוסיפים כמות קטנה של סוכר טבעי (סוכר פרימינג) לפני הסגירה. הסוכר הזה מאפשר לשאריות השמרים הקטנות שנותרו בבירה לבצע תסיסה נוספת בתוך האריזה הסגורה. תסיסה זו יוצרת את הגיזוז הטבעי והעדין שמתפרץ בשמחה כשהבקבוק נפתח!</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const steps = document.querySelectorAll('.beer-journey-app .step');
        const displayArea = document.getElementById('step-display');
        const processVisual = displayArea.querySelector('.process-visual');
        const stepTitle = displayArea.querySelector('.step-title');
        const stepDescription = displayArea.querySelector('.step-description');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('detailed-explanation');

        // Content for each step - more dynamic and action-oriented language
        const stepContents = {
            malting: {
                title: "שלב 1: הלתת - להעיר את הקסם בגרעין",
                description: "גרעיני שעורה שורים במים ומתחילים לנבוט, מעירים אנזימים חיוניים. ייבוש עדין מכין אותם לשחרר את מלוא הפוטנציאל המתוק שלהם.",
                visualClass: 'malting'
            },
            mashing: {
                title: "שלב 2: מעיכה - ליצור את הבסיס המתוק",
                description: "הגרעינים הגרוסים פוגשים מים חמים, והאנזימים מתחילים לפרק עמילנים לסוכרים. נוצר ה'וורט' - נוזל עשיר, מתוק ומלא הבטחה.",
                visualClass: 'mashing'
            },
            lautering: {
                title: "שלב 3: סינון - להפריד את הנוזל הטהור",
                description: "הוורט המתוק מסונן דרך שכבת הגרעינים עצמם, המפרידה את הנוזל הצלול מהשאריות המוצקות. מקבלים נוזל נקי מוכן לרתיחה.",
                visualClass: 'lautering'
            },
            boiling: {
                title: "שלב 4: רתיחה - טיהור והוספת אופי",
                description: "הוורט רותח! החום מחטא, טעמי לוואי נעלמים, והכשות המרה והארומטית מצטרפת לחגיגה ומעניקה לבירה את ייחודה.",
                visualClass: 'boiling'
            },
            cooling: {
                title: "שלב 5: קירור - להתכונן לאורחים הקטנים",
                description: "מקררים במהירות את הוורט לטמפרטורה המושלמת. עכשיו הוא בטוח וחם (או קר) בדיוק במידה הנכונה כדי לקבל את פני השמרים.",
                visualClass: 'cooling'
            },
            fermentation: {
                title: "שלב 6: תסיסה - הקסם הביולוגי בפעולה",
                description: "השמרים האמנים מתחילים לעבוד! הם 'אוכלים' את הסוכרים והופכים אותם באטיות לאלכוהול ופחמן דו-חמצני. הבירה ממש נולדת כאן.",
                visualClass: 'fermentation'
            },
            conditioning: {
                title: "שלב 7: יישון - לתת לטעמים להתפתח",
                description: "הבירה נחה ומתבגרת בשלווה. טעמים מתעגלים, משקעים שוקעים, והבירה מקבלת את הליטוש הסופי והגיזוז העדין.",
                visualClass: 'conditioning'
            },
            packaging: {
                title: "שלב 8: ביקבוק - מוכנה לצאת לעולם!",
                description: "הבירה המוכנה עוברת לבקבוקים או חביות, לעיתים עם נגיעת סוכר ליצירת הגיזוז המושלם והטבעי שמתפרץ בשמחה בפתיחה.",
                visualClass: 'packaging'
            }
        };

        // Add necessary fermentation bubbles elements (for CSS animation)
        // This is a simple way to add elements for complex CSS animations without complex JS DOM manipulation per step
        const fermentBubble1 = document.createElement('div');
        fermentBubble1.classList.add('ferment-bubble1');
        processVisual.appendChild(fermentBubble1);

        const fermentBubble2 = document.createElement('div');
        fermentBubble2.classList.add('ferment-bubble2');
        processVisual.appendChild(fermentBubble2);


        // Function to display step content and trigger animation
        const displayStep = (stepKey) => {
            const content = stepContents[stepKey];
            if (content) {
                // Update text content
                stepTitle.textContent = content.title;
                stepDescription.textContent = content.description;

                // Update active class on timeline steps
                steps.forEach(step => step.classList.remove('active'));
                const activeStepElement = document.querySelector(`.step[data-step="${stepKey}"]`);
                if (activeStepElement) {
                    activeStepElement.classList.add('active');
                    // Optional: Scroll active step into view if timeline overflows
                     activeStepElement.scrollIntoView({ behavior: 'smooth', inline: 'center' });
                }

                // Trigger visual animation
                // Remove all previous animation classes
                Object.values(stepContents).forEach(c => processVisual.classList.remove(c.visualClass));
                // Add the new class
                processVisual.classList.add(content.visualClass);

                // Reset/Restart specific animations if needed (more complex, basic CSS animation restart on class add is often sufficient)
                 // For ferment bubbles, ensure they are added/removed or controlled by the fermentation class state
                 if (stepKey === 'fermentation') {
                     fermentBubble1.style.display = 'block';
                     fermentBubble2.style.display = 'block';
                 } else {
                      fermentBubble1.style.display = 'none';
                      fermentBubble2.style.display = 'none';
                 }


                // Optional: Add a subtle fade-in effect to the text
                 processText.style.opacity = 0;
                 setTimeout(() => {
                     processText.style.opacity = 1;
                 }, 100); // Small delay to allow reflow

            }
        };

        // Add click listeners to steps
        steps.forEach(step => {
            step.addEventListener('click', () => {
                const stepKey = step.getAttribute('data-step');
                displayStep(stepKey);
            });
        });

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleButton.textContent = isHidden ? 'הסתר את סודות הבירה!' : 'לחשוף את סודות הבירה! (הסבר מפורט)'; // Update button text
        });

        // Initialize: Display the first step (Malting) on load with animation
        displayStep('malting');
    });
</script>