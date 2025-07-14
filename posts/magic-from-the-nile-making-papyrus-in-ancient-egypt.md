---
title: "מסע אל הקסם: יצירת פפירוס במצרים העתיקה"
english_slug: magic-from-the-nile-making-papyrus-in-ancient-egypt
category: "ארכאולוגיה"
tags: [מצרים העתיקה, פפירוס, טכנולוגיה עתיקה, חומרים, כתב, נילוס, אמנות עתיקה]
---
# מסע אל הקסם: יצירת פפירוס במצרים העתיקה

לפני אלפי שנים, על גדות הנילוס הפרועים, המצרים הקדמונים גילו סוד שהפך לקסם אמיתי - חומר מופלא ששינה את עולם הכתב והותיר לנו צוהר אל עברם. איך הצליחו ליצור את הפפירוס המופלא הזה, שהשתמר אלפי שנים וחשף לנו את סיפורי הפרעונים והאלים? בואו נצא למסע קצר בעקבות התהליך המרתק!

<div id="papyrus-app" class="app-container">
    <div id="animation-area">
        <!-- Each visual-element represents a step container -->
        <div id="step-visual-1" class="visual-element active">
            <!-- Visuals for Step 1 -->
            <div class="visual-bg reeds-bg"></div>
            <div class="visual-overlay"></div>
            <div class="visual-text">קצירת קני פפירוס</div>
        </div>
        <div id="step-visual-2" class="visual-element">
            <!-- Visuals for Step 2 -->
            <div class="visual-bg slicing-bg"></div>
            <div class="core-shape"></div>
            <div class="strip strip-1"></div>
            <div class="strip strip-2"></div>
            <div class="strip strip-3"></div>
             <div class="visual-overlay"></div>
             <div class="visual-text">קילוף וחיתוך לרצועות</div>
        </div>
        <div id="step-visual-3" class="visual-element">
            <!-- Visuals for Step 3 -->
            <div class="visual-bg soaking-bg"></div>
            <div class="soaked-strip soaked-strip-1"></div>
            <div class="soaked-strip soaked-strip-2"></div>
            <div class="soaked-strip soaked-strip-3"></div>
            <div class="visual-text">השרייה במים</div>
        </div>
        <div id="step-visual-4" class="visual-element">
            <!-- Visuals for Step 4 -->
             <div class="visual-bg layering-bg"></div>
            <div class="layering-base-strips"></div>
            <div class="layering-top-strips"></div>
            <div class="visual-text">סידור הרצועות בשכבות</div>
        </div>
        <div id="step-visual-5" class="visual-element">
            <!-- Visuals for Step 5 -->
             <div class="visual-bg pressing-bg"></div>
            <div class="papyrus-sheet-before-press"></div>
            <div class="press-element"></div>
             <div class="visual-overlay"></div>
            <div class="visual-text">כבישה וייבוש</div>
        </div>
        <div id="step-visual-6" class="visual-element">
            <!-- Visuals for Step 6 -->
             <div class="visual-bg polishing-bg"></div>
            <div class="papyrus-sheet-for-polish"></div>
            <div class="polish-tool"></div>
             <div class="visual-overlay"></div>
             <div class="visual-text">ליטוש עדין</div>
        </div>
         <div id="step-visual-7" class="visual-element">
            <!-- Visuals for Step 7 -->
             <div class="visual-bg finished-bg"></div>
             <div class="finished-papyrus-sheet"></div>
             <div class="visual-overlay"></div>
             <div class="visual-text">דף פפירוס קסום מוכן!</div>
        </div>
    </div>
    <div id="status-area">
        <h3 id="step-title"></h3>
        <p id="step-description"></p>
    </div>
    <div id="controls">
        <button id="next-step-btn">לשלב הבא במסע</button>
        <button id="reset-btn">נתחיל מהתחלה?</button>
    </div>
</div>

<button id="toggle-explanation-btn" class="explanation-toggle-btn">הצגת הסודות העתיקים (הסבר מפורט)</button>

<div id="detailed-explanation" class="explanation-content hidden">
    <h2>הצצה עמוקה אל סודות יצירת הפפירוס:</h2>
    <p><b>מקור הפלא:</b> הפפירוס אינו סתם נייר, אלא תוצר של אמנות עתיקה שמתחילה בצמח גומא הפפירוס (Cyperus papyrus), שהיה גידול פרא שופע בביצות הפוריות של נהר הנילוס, עורק החיים של מצרים העתיקה.</p>
    <h3>המסע צעד אחר צעד:</h3>
    <p><b>1. הקציר וההכנה הראשונית:</b> בבחירה קפדנית, קטפו המצרים את קני הפפירוס החזקים והארוכים ביותר. רק החלק התחתון והעבה של הקנה, ליבתו הפנימית והעסיסית, שימש לתהליך הייצור.</p>
    <p><b>2. הסרת הקליפה והפיכה לרצועות:</b> הקליפה הירוקה והחיצונית הוסרה בזהירות. ליבת הגבעול הלבנה, ספוגית וגמישה, נפרסה לאורך לרצועות דקות ככל האפשר. האחידות בעובי הרצועות הייתה קריטית ליצירת דף חזק ואחיד.</p>
    <p><b>3. טבילה קסומה במים:</b> הרצועות שהתקבלו הושרו במים - ככל הנראה מי הנילוס עצמו - למשך מספר ימים או שבועות. תהליך ההשרייה ריכך את הסיבים והוציא חלק מהעמילנים והסוכרים הטבעיים. חומרים אלו שנותרו ברצועות שימשו מאוחר יותר כדבק טבעי וחזק.</p>
    <p><b>4. ריקוד הרצועות:</b> לאחר ההשרייה, הרצועות נפרשו על משטח ישר, אחת לצד השנייה, בחפיפה קלה, ליצירת שכבה אחידה. מעליהן, סודרה שכבה נוספת של רצועות, אך הפעם בניצב לשכבה הראשונה (בזווית של 90 מעלות). המפגש והחפיפה של הרצועות בשתי השכבות יצר את המבנה הייחודי של הפפירוס.</p>
    <p><b>5. חיבוק חם ולחיצה:</b> יריעת הרצועות הטריות, שנראתה כמו מחצלת, הונחה בין שתי יריעות אריג והוכנסה תחת משקל כבד (כמו אבנים גדולות) או מכבש פרימיטיבי. הלחיצה סחטה את עודפי המים וגרמה לחומרים הדביקים הטבעיים לפעול, תוך שהרצועות נטמעות זו בזו ליצירת דף יחיד ואחיד. הדף נשאר תחת הכבישה למשך מספר ימים, ואז יובש היטב בשמש המצרית החזקה.</p>
    <p><b>6. הטאץ' האחרון:</b> לאחר הייבוש המלא, הדף עבר ליטוש עדין, לרוב באמצעות אבן חלקה או כלי אחר, כדי להפוך את פני השטח לחלקים, נעימים למגע ומושלמים לקבלת דיו עתיק.</p>
    <h3>מעבר לכתיבה:</h3>
    <p>בעוד השימוש בפפירוס כמשטח כתיבה הוא המפורסם ביותר, הוא היה חומר רב-תכליתי להפליא. ממנו בנו סירות קלות, סלים, מזרנים, חבלים, סנדלים, ואף שימשו בו לצרכי בנייה שונים.</p>
    <h3>המורשת הנצחית:</h3>
    <p>הפפירוס לא היה רק חומר; הוא היה מהפכה. הוא אפשר תיעוד נרחב ושיטתי של חוקים, תרבות, דת, מדע וספרות, בקנה מידה שלא היה מוכר קודם לכן. גילוי הפפירוסים במדבריות המצרים היבשים (כמו במרכזי העתיקות באוקסירינכוס) אפשר לנו לצלול לעומק חיי היומיום, המחשבות והידע של אחת הציוויליזציות המרתקות בעולם העתיק, וכן של תרבויות נוספות שהשתמשו בו (יוונים, רומאים). עמידותו המדהימה בתנאים מסוימים הפכה אותו למפתח שגילה לנו עולם אבוד.</p>
</div>

<style>
    /* General App Styling */
    .app-container {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 700px;
        margin: 20px auto;
        border: 1px solid #d1c4e9; /* Softer, thematic border */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom right, #ede7f6, #f3e5f5); /* Gentle gradient */
        padding: 25px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* More pronounced shadow */
        overflow: hidden;
        position: relative;
    }

    /* Animation Area */
    #animation-area {
        min-height: 280px; /* Taller animation area */
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 25px;
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
        border-radius: 8px;
        overflow: hidden;
        position: relative;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Step Visual Containers */
    .visual-element {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex; /* Use flexbox for centering/layout within step */
        align-items: center;
        justify-content: center;
        opacity: 0;
        visibility: hidden; /* Use visibility for better control */
        transition: opacity 0.8s ease-in-out, visibility 0.8s ease-in-out;
        box-sizing: border-box;
        padding: 20px; /* Add some padding */
    }

    .visual-element.active {
        opacity: 1;
        visibility: visible;
        transition: opacity 0.8s ease-in-out, visibility 0.8s ease-in-out; /* Apply transition on activation */
    }

    /* Backgrounds for Steps */
    .visual-bg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        filter: brightness(0.9) contrast(1.1); /* Subtle image enhancement */
        transition: opacity 0.8s ease-in-out;
        z-index: 0;
    }
     .reeds-bg { background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Papyrus_plant.jpg/800px-Papyrus_plant.jpg'); background-size: contain; background-repeat: no-repeat; }
    .slicing-bg { background: linear-gradient(to bottom, #e0e0e0, #d4b483); } /* Gradient hinting at core */
    .soaking-bg { background: linear-gradient(to bottom, #a0c8e8, #6495ed); } /* Water gradient */
    .layering-bg { background: linear-gradient(to bottom right, #e0e0e0, #c2a578); } /* Hinting at material */
    .pressing-bg { background: linear-gradient(to bottom, #d8d8d8, #b89e75); } /* Hinting at press */
    .polishing-bg { background: linear-gradient(to bottom right, #e8e8e8, #a58c63); } /* Hinting at finished surface */
    .finished-bg { background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Papyrus_Brooklyn_Museum_39.599.jpg/800px-Papyrus_Brooklyn_Museum_39.599.jpg'); background-size: cover; } /* Use cover for final image */


     .visual-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.3); /* Light overlay for text readability */
         z-index: 1;
    }
     .visual-text {
         position: relative;
         z-index: 2; /* Ensure text is above overlay */
         font-size: 1.8em;
         color: #333;
         text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8);
         font-weight: bold;
         text-align: center;
         padding: 10px 20px;
         background-color: rgba(255, 255, 255, 0.7);
         border-radius: 8px;
         animation: fadeInScale 1s ease-out; /* Initial animation */
     }


    /* Step-Specific Animations & Visuals (Abstract/Simulated) */

    /* Step 1: Reeds - subtle sway */
    @keyframes sway {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-0.5deg); }
        75% { transform: rotate(0.5deg); }
    }
    #step-visual-1.active .reeds-bg { animation: sway 5s ease-in-out infinite; }

     /* Step 2: Peeling/Slicing */
     .core-shape {
        position: relative;
        width: 80px;
        height: 200px;
        background-color: #e8d8bf; /* Lighter core color */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden; /* Hide overflowing strips */
        z-index: 2;
         transform: translateX(-50px); /* Position to the left */
         animation: fadeIn 0.8s ease-out;
    }

     .strip {
         position: absolute;
         right: 0; /* Start from the right edge of the core */
         width: 70px; /* Wider strip */
         height: 10px; /* Thin strip */
         background-color: #c2a578; /* Strip color */
         transform: translateX(100%); /* Initially off-screen */
         opacity: 0;
         animation: slideInStrip 1s ease-out forwards; /* Animation to slide in */
         z-index: 3;
     }
     .strip-1 { top: 40px; animation-delay: 0.3s; }
     .strip-2 { top: 95px; animation-delay: 0.6s; }
     .strip-3 { top: 150px; animation-delay: 0.9s; }

    @keyframes slideInStrip {
        to { transform: translateX(calc(100% - 120px)); opacity: 1; } /* Slide left */
    }

    /* Step 3: Soaking */
     .soaked-strip {
         position: absolute;
         width: 150px;
         height: 15px;
         background-color: rgba(255, 255, 255, 0.6); /* Lighter strips */
         border: 1px solid rgba(0,0,0,0.1);
         border-radius: 4px;
         animation: floatInWater 2s ease-in-out infinite alternate; /* Floating animation */
         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
         z-index: 2;
     }
     .soaked-strip-1 { top: 50px; left: 80px; animation-delay: 0s; }
     .soaked-strip-2 { top: 120px; left: 150px; width: 180px; height: 18px; animation-delay: 0.5s; }
     .soaked-strip-3 { top: 180px; left: 100px; animation-delay: 1s; }

     @keyframes floatInWater {
         0%, 100% { transform: translateY(0) rotate(0deg); }
         50% { transform: translateY(5px) rotate(1deg); }
     }
     #step-visual-3.active .soaked-strip { animation-play-state: running; }
      #step-visual-3 .soaked-strip { animation-play-state: paused; }


    /* Step 4: Layering */
    .layering-base-strips, .layering-top-strips {
        position: absolute;
        width: 80%;
        height: 80%;
        background-size: cover; /* Use background-size cover */
        opacity: 0;
        z-index: 2;
    }
    .layering-base-strips {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><pattern id="horiz-stripes" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="8" height="10" fill="%23c2a578"/></pattern><rect width="100%" height="100%" fill="url(%23horiz-stripes)"/></svg>');
        animation: fadeIn 0.8s ease-out forwards;
    }
    .layering-top-strips {
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><pattern id="vert-stripes" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="8" fill="%23c2a578"/></pattern><rect width="100%" height="100%" fill="url(%23vert-stripes)"/></svg>');
        animation: fadeIn 0.8s ease-out 0.5s forwards; /* Appear after base */
    }

    /* Step 5: Pressing */
     .papyrus-sheet-before-press {
        position: absolute;
        width: 70%;
        height: 70%;
        background-color: #c2a578;
        border-radius: 4px;
        opacity: 0.8;
         z-index: 1;
         animation: scaleUp 0.8s ease-out forwards;
     }
    .press-element {
        position: absolute;
        top: 0;
        left: 10%;
        width: 80%;
        height: 50%; /* Represents the press coming down */
        background-color: #8d6e63; /* Stone/wood color */
        border-radius: 8px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transform: translateY(-100%); /* Start above */
        animation: pressDown 1.5s ease-out forwards;
        z-index: 3;
    }

    @keyframes pressDown {
        to { transform: translateY(40%); } /* Press down onto the sheet */
    }
    @keyframes scaleUp {
        from { transform: scale(0.8); opacity: 0.5; }
        to { transform: scale(1); opacity: 0.8; }
    }


    /* Step 6: Polishing */
     .papyrus-sheet-for-polish {
         position: absolute;
        width: 70%;
        height: 70%;
        background-color: #a58c63; /* Slightly smoother color */
        border-radius: 4px;
        z-index: 1;
        overflow: hidden; /* For polish effect */
         animation: fadeIn 0.8s ease-out forwards;
     }
    .polish-tool {
        position: absolute;
        width: 50px;
        height: 30px;
        background-color: rgba(255, 255, 255, 0.8); /* Simulate smooth stone */
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
        z-index: 3;
        top: 30%;
        left: 10%;
        animation: polishSweep 3s ease-in-out infinite; /* Sweep back and forth */
    }
     @keyframes polishSweep {
         0%, 100% { transform: translateX(0%); }
         50% { transform: translateX(calc(100% - 80px)); } /* Sweep across */
     }
     #step-visual-6.active .polish-tool { animation-play-state: running; }
      #step-visual-6 .polish-tool { animation-play-state: paused; }

     /* Step 7: Finished */
     .finished-papyrus-sheet {
         position: relative;
        width: 80%;
        height: 80%;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Papyrus_Brooklyn_Museum_39.599.jpg/800px-Papyrus_Brooklyn_Museum_39.599.jpg');
        background-size: contain; /* Contain for detail */
        background-repeat: no-repeat;
        background-position: center;
        border: 2px solid #7d634a; /* Border to frame it */
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        border-radius: 4px;
        animation: fadeInScale 1s ease-out forwards;
         z-index: 2;
     }


    /* General Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
     @keyframes fadeInScale {
         from { opacity: 0; transform: scale(0.9); }
         to { opacity: 1; transform: scale(1); }
     }


    /* Status Area */
    #status-area {
        margin-bottom: 25px;
        text-align: center;
        min-height: 90px; /* Reserve more space */
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    #step-title {
        color: #4a148c; /* Purple theme */
        margin-bottom: 8px;
        font-size: 1.5em;
        font-weight: bold;
    }

    #step-description {
        color: #6a1b9a; /* Darker purple */
        font-size: 1em;
        line-height: 1.5;
    }

    /* Controls */
    #controls {
        text-align: center;
        margin-top: 20px;
    }

    #controls button {
        padding: 12px 24px;
        margin: 0 8px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 25px; /* Pill shape buttons */
        transition: background-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    #next-step-btn {
        background: linear-gradient(to right, #7b1fa2, #ab47bc); /* Purple gradient */
        color: white;
    }

    #next-step-btn:hover {
        background: linear-gradient(to right, #6a1b9a, #8e24aa);
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(0,0,0,0.3);
    }
     #next-step-btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }


    #reset-btn {
        background: linear-gradient(to right, #d81b60, #ec407a); /* Pink gradient */
        color: white;
    }

    #reset-btn:hover {
        background: linear-gradient(to right, #c2185b, #d81b60);
         transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(0,0,0,0.3);
    }
      #reset-btn:active {
         transform: translateY(0);
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }


    /* Explanation Toggle Button */
    .explanation-toggle-btn {
        display: block;
        margin: 30px auto;
        padding: 12px 24px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid #9575cd; /* Purple border */
        border-radius: 25px;
        background-color: #e1bee7; /* Light purple */
        color: #4a148c; /* Dark purple */
        transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.1s ease, box-shadow 0.3s ease;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .explanation-toggle-btn:hover {
         background-color: #ce93d8; /* Slightly darker */
         border-color: #7e57c2; /* Slightly darker */
         transform: translateY(-1px);
         box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .explanation-toggle-btn:active {
         transform: translateY(0);
         box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    /* Detailed Explanation */
    .explanation-content {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        max-width: 700px;
        margin: 20px auto;
        padding: 25px;
        border: 1px solid #d1c4e9;
        border-radius: 12px;
        background-color: #f3e5f5; /* Lighter purple */
        line-height: 1.7;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    .explanation-content h2, .explanation-content h3 {
        color: #4a148c;
        margin-top: 20px;
        margin-bottom: 12px;
        border-bottom: 1px solid #e1bee7; /* Subtle separator */
        padding-bottom: 5px;
    }

    .explanation-content p {
        margin-bottom: 15px;
        color: #6a1b9a;
        font-size: 1em;
    }
    .explanation-content p b {
         color: #311b92; /* Even darker purple for bold */
    }

    /* Helper class for hiding elements */
    .hidden {
        display: none;
    }

</style>

<script>
    const steps = [
        {
            title: "שלב 1: ליד הנילוס - קציר הקסם",
            description: "המסע מתחיל בביצות הפוריות, שם קוצרים את קני הפפירוס החזקים ביותר, חומר הגלם ליצירת הפלא.",
            visualId: "step-visual-1"
        },
        {
            title: "שלב 2: הפיכה לרצועות - ליבת הסוד",
            description: "הקליפה החיצונית מוסרת בזהירות, וליבת הגבעול הלבנה נפרסת לרצועות דקות - זהו לב הפפירוס לעתיד.",
            visualId: "step-visual-2"
        },
        {
            title: "שלב 3: טבילה מרככת - קסם המים",
            description: "הרצועות הטריות מושרות במי הנילוס למספר ימים. המים מרככים אותן ומכינים אותן להידבקות טבעית.",
            visualId: "step-visual-3"
        },
        {
            title: "שלב 4: אריגה קדומה - שתי וערב",
            description: "הרצועות מוצאות מהמים וסודרות על משטח בשתי שכבות: אחת לאורך, ואחת מעליה בניצב. המפגש הקסום מתחיל.",
            visualId: "step-visual-4"
        },
        {
            title: "שלב 5: חיבוק הדוק - כבישה וייבוש",
            description: "היריעה הלחה נלחצת תחת משקל כבד. הלחץ סוחט את המים וגורם לרצועות להידבק זו לזו, ואז השמש מייבשת את הדף.",
            visualId: "step-visual-5"
        },
        {
            title: "שלב 6: הטאץ' הסופי - ליטוש להחלקה",
            description: "הדף היבש והמוצק מלוטש בעדינות באבן חלקה, כדי ליצור משטח כתיבה חלק ומושלם.",
            visualId: "step-visual-6"
        },
         {
            title: "הקסם מוכן! דף הפפירוס העתיק",
            description: "מגבעול פשוט על שפת הנהר, נוצר חומר ששינה את ההיסטוריה ושימר עבורנו את סיפוריה.",
            visualId: "step-visual-7"
        }
    ];

    let currentStepIndex = 0;

    const stepTitleElement = document.getElementById('step-title');
    const stepDescriptionElement = document.getElementById('step-description');
    const nextStepBtn = document.getElementById('next-step-btn');
    const resetBtn = document.getElementById('reset-btn');
    const toggleExplanationBtn = document.getElementById('toggle-explanation-btn');
    const detailedExplanationDiv = document.getElementById('detailed-explanation');
    const stepVisualElements = document.querySelectorAll('.visual-element');

    function updateAppDisplay() {
        // Ensure all animations reset or are in initial state before showing the next step
        // This might require more complex JS if animations don't reset purely by hiding/showing,
        // but for simple CSS animations triggered by active class, it's often sufficient.

        const currentStep = steps[currentStepIndex];
        stepTitleElement.textContent = currentStep.title;
        stepDescriptionElement.textContent = currentStep.description;

        // Update visual: Fade out all, fade in the active one
        stepVisualElements.forEach(el => {
            el.classList.remove('active');
            // Optional: Force reflow/restart animations by removing and adding class?
            // el.style.display = 'none'; // Temporarily hide
        });

        // Force reflow if needed (sometimes helps restart CSS animations)
        // void document.getElementById('animation-area').offsetWidth;

        const activeVisual = document.getElementById(currentStep.visualId);
        if (activeVisual) {
             // activeVisual.style.display = 'flex'; // Restore display
             activeVisual.classList.add('active');
        }

        // Update buttons visibility using classes
        if (currentStepIndex === steps.length - 1) {
            nextStepBtn.classList.add('hidden');
            resetBtn.classList.remove('hidden');
        } else {
            nextStepBtn.classList.remove('hidden');
            resetBtn.classList.add('hidden');
        }
    }

    function goToNextStep() {
        if (currentStepIndex < steps.length - 1) {
            currentStepIndex++;
            updateAppDisplay();
        }
    }

    function resetApp() {
        currentStepIndex = 0;
        updateAppDisplay();
    }

    function toggleExplanation() {
        detailedExplanationDiv.classList.toggle('hidden');
        if (detailedExplanationDiv.classList.contains('hidden')) {
            toggleExplanationBtn.textContent = 'הצגת הסודות העתיקים (הסבר מפורט)';
        } else {
            toggleExplanationBtn.textContent = 'הסתרת הסודות העתיקים';
        }
    }

    // Event Listeners
    nextStepBtn.addEventListener('click', goToNextStep);
    resetBtn.addEventListener('click', resetApp);
    toggleExplanationBtn.addEventListener('click', toggleExplanation);

    // Initialize the display (hide explanation and reset button initially)
    detailedExplanationDiv.classList.add('hidden');
    resetBtn.classList.add('hidden'); // Ensure reset button is hidden on load
    updateAppDisplay(); // Show the first step

</script>
---