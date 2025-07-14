---
title: "לבנות את הדרקאר: מסע אינטראקטיבי אל סודות בניית ספינות ויקינגים"
english_slug: building-the-drakkar-interactive-journey
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: [ויקינגים, ספינות, דרקאר, היסטוריה ימית, טכנולוגיה עתיקה, בניית ספינות]
---
<div class="intro-text">
    <h1>לבנות את הדרקאר: מסע אינטראקטיבי אל סודות בניית ספינות ויקינגים</h1>
    <p>דמיינו את גלי הים הצפוני מתנפצים על חרטום ספינה ארוכה וצרה, כשהיא חותכת את המים במהירות עוצרת נשימה. אלו היו ספינות הוויקינגים האגדיות – ה"דרקאר" – שאיפשרו להם להגיע לקצוות העולם. אבל איך, עם כלים פשוטים ועצים בלבד, הם בנו את כלי השייט המופלאים והעמידים הללו? הצטרפו אלינו למסע מרתק צעד אחר צעד, ובנו דרקאר משלכם!</p>
</div>

<div id="viking-ship-builder-app">
    <div id="ship-visualization-container">
        <div id="ship-visualization">
            <!-- Ship parts - ordered by visual layers -->
            <div class="water"></div> <!-- Dynamic water simulation placeholder -->
            <div class="ship-part keel"></div>
            <div class="ship-part stem-stern"></div>
            <div class="ship-part planks plank-layer-1"></div>
            <div class="ship-part planks plank-layer-2"></div>
            <div class="ship-part planks plank-layer-3"></div>
            <div class="ship-part planks plank-layer-4"></div>
            <div class="ship-part rivets-sealing"></div> <!-- Combined for simplicity -->
            <div class="ship-part frames"></div>
            <div class="ship-part mast"></div>
            <div class="ship-part sail"></div>
            <div class="ship-finished-overlay"></div> <!-- Overlay for finished state -->
        </div>
    </div>
    <div id="controls">
        <!-- Buttons will be dynamically enabled/disabled -->
        <button data-step="0" class="step-button">1. העץ מתעורר לחיים</button>
        <button data-step="1" class="step-button">2. עמוד השדרה של הדרקאר</button>
        <button data-step="2" class="step-button">3. קווי המתאר נבנים (מפליג!)</button>
        <button data-step="3" class="step-button">4. חיבורי ברזל חזקים</button>
        <button data-step="4" class="step-button">5. סוד האיטום</button>
        <button data-step="5" class="step-button">6. הצלעות הפנימיות</button>
        <button data-step="6" class="step-button">7. הלב והמפרש</button>
    </div>
    <div id="step-info">
        <p>לחצו על 'העץ מתעורר לחיים' כדי להתחיל במסע הבנייה!</p>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר את יומן הבנאי המורחב</button>

<div id="explanation" style="display: none;">
    <h2>יומן הבנאי המורחב: עמוק אל סודות הדרקאר</h2>
    <p>עבור הוויקינגים, ספינות היו הכל – בית, כלי נשק, גשר לעולמות חדשים. בניית ספינה הייתה אומנות קדומה, המשלבת ידע מדורי דורות, מיומנות עילאית, והבנה עמוקה של חומרי הגלם והים. ה"דרקאר" (ספינת דרקון, על שם ראשי הדרקון שקישטו לעיתים את חרטומן) הייתה פסגת הטכנולוגיה הימית של התקופה.</p>

    <h3>מה הפך את ספינות הוויקינגים למיוחדות כל כך?</h3>
    <ul>
        <li><strong>כושר תמרון ומהירות:</strong> עיצוב ארוך וצר עם שוקע (חלק השקוע במים) נמוך במיוחד. זה איפשר להן לשוט מהר מאוד, לנווט בנתיבי מים רדודים (נהרות, חופים לא מפותחים) ולשנות כיוון במהירות מפתיעה (חרטום וירכתיים דומים).</li>
        <li><strong>חוזק וגמישות (בניית מפליג):</strong> הלוחות החופפים (Clinker/Lapstrake) יצרו גוף ספינה "נושם" – הוא יכל להתגמש ולהתפתל עם עוצמת הגלים בים סוער, במקום להישבר כמו גופים קשיחים יותר.</li>
        <li><strong>יכולת נשיאה:</strong> למרות היותן מהירות, הן יכלו לשאת מספר רב של לוחמים או כמות גדולה של סחורה.</li>
        <li><strong>פשטות וחוסן:</strong> נבנו מחומרים טבעיים בלבד, תוך הסתמכות על חוזק העץ עצמו ושיטות חיבור מוכחות.</li>
    </ul>

    <h3>חומרי גלם וכלי עבודה: מתנת היער והאדמה</h3>
    <p>אלון היה העץ המועדף לגוף הספינה בשל חוזקו ועמידותו, אך גם אשווח (Ash) ואורן (Pine) שימשו. גזעי העץ לא נסרו, אלא בוקעו לאורך הסיבים. שיטה זו, שנקראת "ביקוע קרניים" (Radial Splitting), דרשה מיומנות רבה אך הניבה לוחות חזקים וגמישים להפליא שפחות נטו להתעוות. לאיטום השתמשו בזפת שחוממה והתערבבה בחומר סיבי כמו מוך צמר, טחב או שיער בעלי חיים. כלי העבודה היו פשוטים אך חדים ויעילים להפליא: גרזנים מסוגים שונים (הכלי העיקרי לעיבוד עץ, החל מעצים ענקיים ועד גילוף עדין), מקדחי יד, מפסלות, פטישים, וסכינים. מסמרות הברזל, אלפים מהן לכל ספינה, נוצרו על ידי נפחים מקומיים והיוו רכיב קריטי בחיבור הלוחות.</p>

    <h3>תהליך הבנייה: מהיער אל הים</h3>
    <ol>
        <li><strong>בחירה ועיבוד העץ:</strong> אומני הספינות ידעו לבחור את העצים המתאימים ביותר ואת חלקיהם השונים לשימושים ספציפיים (למשל, ענפים מעוקלים טבעיים לשדרית ולגזעים). הביקוע לאורך הסיבים היה שלב ראשוני ומכריע.</li>
        <li><strong>השדרית והגזעים:</strong> השדרית (Keel), עמוד השדרה של הספינה, הונחה ראשונה. אליה חוזקו גזעי החרטום (Stem) והירכתיים (Sternpost) המעוקלים. חלקים אלו עוצבו לרוב מחלקי עץ בעלי צורה טבעית מתאימה.</li>
        <li><strong>הוספת לוחות האשפה (Planks) בשיטת המפליג:</strong> החל מהשדרית כלפי מעלה, לוחות הגוף (Strakes) חוברו כשהם חופפים זה את זה. כל לוח עליון חפף את קצה הלוח שמתחתיו. זהו לב שיטת ה"מפליג" שמעניקה את החוזק והגמישות.</li>
        <li><strong>חיבור הלוחות במסמרות ברזל:</strong> אלפי מסמרות ברזל שימשו לחיבור הלוחות החופפים. קצה המסמרת הוכנס דרך שני הלוחות החופפים, שייבה (רוב הזמן מברזל, לפעמים מעץ) הונחה בקצה הפנימי, והקצה נחבט וקופל ("מוסמר") אל השייבה, ויוצר חיבור דמוי ניט חזק מאוד.</li>
        <li><strong>איטום התפרים:</strong> הרווחים הצרים בין הלוחות החופפים, היכן שהם נפגשים, נאטמו בחומר סיבי (צמר, טחב) ספוג בזפת חמה. זה היה תהליך קפדני שנועד להבטיח אטימות מוחלטת למים.</li>
        <li><strong>בניית המסגרת הפנימית (Frames):</strong> לאחר שגוף הספינה קיבל את צורתו ויציבותו מהלוחות החופפים המחוברים במסמרות, נוספו המסגרות (צלעות הספינה) בתוך הגוף. הן חיזקו את המבנה עוד יותר, תמכו בלוחות, וסיפקו בסיס לסיפון וספסלי החותרים. המסגרות חוברו ללוחות בשיטת ה"תפירה" (Lashing) או במסמרות עץ/ברזל.</li>
        <li><strong>הקמת התורן והריג:</strong> התורן, לרוב עשוי מעץ אשוח גבוה, הוצב במרכז הספינה וחוזק היטב למסגרות ולשדרית. אליו חוברו החבלים (הריג) שתמכו במפרש המרובע הענק, שאיפשר ניצול יעיל של הרוח למסעות ארוכים ומהירים.</li>
    </ol>

    <h3>מורשת הדרקאר</h3>
    <p>הידע בבניית ספינות היה אחד הנכסים החשובים ביותר של הוויקינגים. ספינותיהם לא רק שינו את ההיסטוריה של סקנדינביה והעולם, אלא גם השפיעו על טכניקות בניית ספינות מאוחרות יותר. ממצאים ארכיאולוגיים מופלאים כמו ספינות אוסברג (Oseberg) וגוקסטד (Gokstad) בנורווגיה, שנשתמרו בקברי ספינות, מאפשרים לנו ללמוד ולהעריך את רמת האומנות והטכנולוגיה של בנאי הספינות הוויקינגים.</p>
</div>

<style>
    /* General App Styling */
    #viking-ship-builder-app {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #d3c6b5; /* Softer border */
        border-radius: 12px; /* More rounded */
        background: linear-gradient(to bottom right, #f8f5f0, #e9e4da); /* Subtle gradient background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Softer shadow */
        overflow: hidden; /* Ensure elements stay within bounds */
    }

    .intro-text {
        text-align: center;
        margin-bottom: 30px;
    }

    .intro-text h1 {
        color: #4a3b33; /* Earthy brown */
        margin-bottom: 10px;
        font-size: 2em;
    }

    .intro-text p {
        color: #5e503f; /* Slightly darker earth */
        line-height: 1.6;
    }


    /* Visualization Container and Stage */
    #ship-visualization-container {
        position: relative;
        width: 100%;
        padding-bottom: 55%; /* Aspect ratio adjusted */
        background: linear-gradient(to bottom, #a3d2f1, #4682b4); /* Sky to Water */
        border: 2px solid #8b7b6b; /* Border to frame the scene */
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 25px;
        box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
    }

    #ship-visualization {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        perspective: 1000px; /* For 3D effects if needed */
    }

     /* Water Simulation */
     .water {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40%; /* Water level */
        background: #4682b4; /* Steel Blue */
        background: linear-gradient(to top, #3a6a9a, #4682b4);
        z-index: 0; /* Below ship parts */
        /* Subtle wave effect - purely visual, no actual physics */
        animation: subtle-waves 5s ease-in-out infinite alternate;
     }

     @keyframes subtle-waves {
         from { transform: translateY(0px); }
         to { transform: translateY(-3px); }
     }


    /* Ship Part Base Styling */
    .ship-part {
        position: absolute;
        bottom: 0; /* Anchor to the bottom */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, 20px) scale(0.8); /* Initial state: slightly below, smaller, hidden */
        opacity: 0; /* Initially hidden */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Smooth transitions */
        transform-origin: center bottom; /* Animation origin */
        z-index: 10; /* Default z-index */
    }

    /* Specific Part Styles (use SVG data URIs for better shapes) */
    .ship-part.keel {
        width: 70%;
        height: 20px;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 20"><path d="M20 20 C 100 5 350 5 680 20 Z" fill="%238B4513"/></svg>') no-repeat center bottom;
        background-size: 100% 100%;
        bottom: 38%; /* Position relative to container bottom, considering water */
        z-index: 5;
    }

    .ship-part.stem-stern {
        width: 78%; /* Slightly wider to cover ends */
        height: 70px; /* Taller for curved ends */
         background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 70"><path d="M10 70 Q 150 0 390 10 Q 630 0 770 70 Z" fill="%23A0522D"/></svg>') no-repeat center bottom;
        background-size: 100% 100%;
        bottom: 35%; /* Position relative to container bottom */
        z-index: 6;
    }

     /* Planks - Layered Approach */
    .ship-part.planks {
        width: 80%; /* Cover the hull width */
        height: 20px; /* Height of each plank layer */
        background-color: #cd853f; /* Peru - base plank color */
        border-bottom: 2px solid #8b4513; /* Overlap line */
        box-sizing: border-box;
        z-index: 7; /* Above keel/stem */
        transform: translate(-50%, 30px); /* Start lower */
        opacity: 0;
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }

    .ship-part.planks.plank-layer-1 { bottom: 39%; } /* Lowest layer */
    .ship-part.planks.plank-layer-2 { bottom: 41%; }
    .ship-part.planks.plank-layer-3 { bottom: 43%; }
    .ship-part.planks.plank-layer-4 { bottom: 45%; height: 30px; /* Top layer can be taller */ }


    /* Rivets and Sealing - Simplified representation */
    .ship-part.rivets-sealing {
        width: 80%;
        height: 80px; /* Cover the plank area */
        bottom: 39%;
        background: radial-gradient(ellipse at center, rgba(139, 69, 19, 0.6) 0%, transparent 70%), /* Tar smudge */
                    repeating-linear-gradient(to right, transparent, transparent 15px, rgba(92, 51, 23, 0.8) 15px, rgba(92, 51, 23, 0.8) 17px), /* Vertical rivets/lines */
                    repeating-linear-gradient(to bottom, transparent, transparent 18px, rgba(92, 51, 23, 0.8) 18px, rgba(92, 51, 23, 0.8) 20px); /* Horizontal rivet lines */
        background-size: 100% 100%, 100% 100%, 100% 100%;
        background-repeat: no-repeat;
        z-index: 8;
        opacity: 0;
        transform: translate(-50%, 20px); /* Start hidden */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }


    /* Frames */
    .ship-part.frames {
        width: 65%; /* Frames are inside */
        height: 80px;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 80"><path d="M0 80 Q 80 10 325 10 Q 570 10 650 80" fill="none" stroke="%238B4513" stroke-width="10" stroke-linecap="round"/></svg>') no-repeat center bottom;
        background-size: 100% 100%;
        bottom: 43%; /* Position higher inside the hull */
        z-index: 9;
        opacity: 0;
        transform: translate(-50%, 30px) scaleX(0.9); /* Start lower, slightly squashed */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }

    /* Mast and Sail */
     .ship-part.mast {
        width: 12px;
        height: 120px;
        background-color: #8B4513; /* Saddle Brown */
        left: 50%;
        bottom: 50%; /* Start above the hull construction */
        transform: translate(-50%, 50px) scaleY(0.5); /* Start lower, shorter */
        opacity: 0;
        z-index: 10; /* Above frames */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
     }

     .ship-part.sail {
         width: 150px; /* Sail width */
         height: 100px; /* Sail height */
         background-color: rgba(245, 222, 179, 0.8); /* Wheat, semi-transparent */
         border: 2px solid #4a3b33;
         left: 50%;
         bottom: 50%; /* Position relative to mast */
         transform: translate(-50%, 60px) scale(0.5) rotateX(90deg); /* Start flat, below, smaller */
         opacity: 0;
         z-index: 11; /* Above mast */
         transition: opacity 1s ease-out, transform 1s ease-out;
         transform-origin: center top; /* Rotate from the top of the sail */
     }


     /* Ship Finished Overlay */
    .ship-finished-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(76, 175, 80, 0.2); /* Greenish tint */
        display: flex;
        justify-content: center;
        align-items: center;
        color: #333;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
        opacity: 0;
        transition: opacity 1.5s ease-in-out;
        z-index: 20; /* On top */
        pointer-events: none; /* Allow clicks to pass through */
    }


    /* State Classes to Show/Animate Parts */

    /* Stage 0: Keel & Stem/Stern appear */
    #ship-visualization.stage-0 .keel,
    #ship-visualization.stage-0 .stem-stern {
        opacity: 1;
        transform: translate(-50%, 0px) scale(1); /* Animate to visible, correct position/size */
    }

    /* Stage 1: Planks appear (layered animation) */
    #ship-visualization.stage-1 .keel, #ship-visualization.stage-1 .stem-stern { /* Keep previous parts visible */ opacity: 1; transform: translate(-50%, 0px) scale(1); }
    #ship-visualization.stage-1 .planks.plank-layer-1 { opacity: 1; transform: translate(-50%, 0px); }
    #ship-visualization.stage-1 .planks.plank-layer-2 { opacity: 1; transform: translate(-50%, 0px); transition-delay: 0.1s; } /* Staggered appearance */
    #ship-visualization.stage-1 .planks.plank-layer-3 { opacity: 1; transform: translate(-50%, 0px); transition-delay: 0.2s; }
    #ship-visualization.stage-1 .planks.plank-layer-4 { opacity: 1; transform: translate(-50%, 0px); transition-delay: 0.3s; }


     /* Stage 3: Rivets/Sealing appear */
     #ship-visualization.stage-3 .keel, #ship-visualization.stage-3 .stem-stern { opacity: 1; transform: translate(-50%, 0px) scale(1); }
     #ship-visualization.stage-3 .planks { opacity: 1; transform: translate(-50%, 0px); } /* Keep planks visible */
     #ship-visualization.stage-3 .rivets-sealing {
         opacity: 1;
         transform: translate(-50%, 0px);
         transition-delay: 0.4s; /* Appear after planks settle */
     }

    /* Stage 4: Sealing becomes more prominent (implied in rivets-sealing opacity) - text change highlights sealing */
    /* Visual change handled by rivets-sealing opacity in stage 3 */


    /* Stage 5: Frames appear */
    #ship-visualization.stage-5 .keel, #ship-visualization.stage-5 .stem-stern { opacity: 1; transform: translate(-50%, 0px) scale(1); }
    #ship-visualization.stage-5 .planks { opacity: 1; transform: translate(-50%, 0px); }
    #ship-visualization.stage-5 .rivets-sealing { opacity: 1; transform: translate(-50%, 0px); }
    #ship-visualization.stage-5 .frames {
        opacity: 1;
        transform: translate(-50%, 0px) scaleX(1); /* Animate to full size */
        transition-delay: 0.5s; /* Appear after external hull */
    }

    /* Stage 6: Mast and Sail appear */
    #ship-visualization.stage-6 .keel, #ship-visualization.stage-6 .stem-stern { opacity: 1; transform: translate(-50%, 0px) scale(1); }
    #ship-visualization.stage-6 .planks { opacity: 1; transform: translate(-50%, 0px); }
    #ship-visualization.stage-6 .rivets-sealing { opacity: 1; transform: translate(-50%, 0px); }
    #ship-visualization.stage-6 .frames { opacity: 1; transform: translate(-50%, 0px) scaleX(1); }
    #ship-visualization.stage-6 .mast {
        opacity: 1;
        transform: translate(-50%, 0px) scaleY(1); /* Mast rises */
        transition-delay: 0.6s;
    }
    #ship-visualization.stage-6 .sail {
        opacity: 1;
        transform: translate(-50%, 0px) scale(1) rotateX(0deg); /* Sail unfolds/drops */
        transition-delay: 1s; /* Appears after mast is up */
    }

    /* Final Stage - Completion */
     #ship-visualization.stage-final .ship-finished-overlay {
        opacity: 1; /* Make overlay visible */
     }
      #ship-visualization.stage-final .water {
         animation: finished-waves 4s ease-in-out infinite alternate; /* Slightly different animation */
      }
      @keyframes finished-waves {
         from { transform: translateY(0px); }
         to { transform: translateY(-5px); }
      }


    /* Controls Styling */
    #controls {
        text-align: center;
        margin-bottom: 20px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px; /* Increased space */
    }

    .step-button {
        padding: 12px 20px; /* More padding */
        font-size: 1.1rem; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 6px; /* Slightly more rounded */
        background-color: #5a2c0f; /* Earthy brown */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        text-align: center;
        flex-grow: 1; /* Allow buttons to grow */
        min-width: 150px; /* Minimum width */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .step-button:hover:not(:disabled) {
        background-color: #8b4513; /* Lighter brown on hover */
        transform: translateY(-2px); /* Subtle lift */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

     .step-button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
     }

     .step-button:disabled {
        background-color: #cccccc;
        color: #666666;
        cursor: not-allowed;
        box-shadow: none;
     }

    /* Info Box Styling */
    #step-info {
        background-color: #f0f0f0; /* Light gray */
        padding: 15px;
        border-radius: 6px;
        min-height: 60px; /* More space */
        text-align: center;
        font-size: 1.1em;
        color: #333;
        border: 1px solid #ddd;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    #step-info strong {
        color: #5a2c0f; /* Match button color */
    }


    /* Explanation Toggle Button */
    .toggle-button {
        display: block;
        margin: 30px auto 20px; /* More space around */
        padding: 12px 25px;
        font-size: 1.1rem;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #005f73; /* Dark Teal */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .toggle-button:hover {
        background-color: #0a9396; /* Lighter Teal */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

     .toggle-button:active {
         transform: translateY(0);
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
     }


    /* Explanation Section */
    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #d3c6b5;
        border-radius: 12px;
        background-color: #f8f5f0; /* Match app background */
        direction: rtl;
        text-align: right;
        color: #4a3b33;
        line-height: 1.7; /* Improved readability */
    }

    #explanation h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #5a2c0f;
    }

    #explanation h3 {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #8b4513;
        border-bottom: 1px solid #d3c6b5; /* Subtle separator */
        padding-bottom: 5px;
    }

    #explanation ul, #explanation ol {
        margin-bottom: 15px;
        padding-right: 25px; /* Add space for bullets/numbers */
    }

     #explanation li {
        margin-bottom: 8px;
     }

     #explanation p {
         margin-bottom: 15px;
     }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const shipVisualization = document.getElementById('ship-visualization');
        const stepInfo = document.getElementById('step-info');
        const controls = document.getElementById('controls');
        const toggleButton = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');
        const stepButtons = controls.querySelectorAll('.step-button');
        const shipFinishedOverlay = document.querySelector('.ship-finished-overlay');

        // Data structure for steps with engaging text
        const steps = [
            {
                info: "<strong>שלב 1: העץ מתעורר לחיים.</strong> הכל מתחיל ביער. אומני הספינות בוחרים בקפידה עצי אלון חזקים וגמישים, ומפצלים אותם בטכניקה עתיקה לאורך הסיבים כדי לשמר את החוזק הטבעי. זהו חומר הגלם שיעמוד בפני גלי הים הפראיים."
                // No specific visual stage class for step 1 yet - implies raw materials
            },
            {
                info: "<strong>שלב 2: עמוד השדרה של הדרקאר.</strong> מניחים את השדרית, החלק התחתון המרכזי שיהווה את 'עמוד השדרה' של הספינה. מחברים אליה גזעים מעוקלים ויציבים שיגדירו את צורת החרטום והירכתיים. היסודות מוצבים במקומם!",
                stageClass: 'stage-0' // Keel & Stem/Stern appear
            },
            {
                info: "<strong>שלב 3: קווי המתאר נבנים (מפליג!).</strong> מתחילים לחבר את לוחות העץ לגוף הספינה, החל מהשדרית כלפי מעלה. כל לוח עליון חופף מעט את קצה הלוח שמתחתיו – זו שיטת ה'מפליג' הייחודית! היא יוצרת מבנה גמיש וחזק להפליא, שיכול לרקוד עם הגלים.",
                stageClass: 'stage-1' // Planks appear layered
            },
            {
                info: "<strong>שלב 4: חיבורי ברזל חזקים.</strong> עכשיו מחברים את הלוחות החופפים זה לזה באמצעות אלפי מסמרות ברזל. כל מסמרת מחוזקת ושייבה ננעצת פנימה כדי ליצור חיבור הדוק ועמיד שיחזיק את הגוף יחד גם בסערות קשות.",
                 stageClass: 'stage-3' // Rivets/Sealing (initial state) appear
            },
            {
                info: "<strong>שלב 5: סוד האיטום.</strong> כדי שהדרקאר תצוף ולא תשקע, צריך לאטום את התפרים הצרים שבין הלוחות החופפים. זה נעשה בעזרת זפת חמה מעורבת בחומר סיבי (כמו צמר), שנמרחת בזהירות על כל סדק. סוד קטן להבטחת אטימות מוחלטת!",
                stageClass: 'stage-4' // Rivets/Sealing (emphasizing sealing aspect - CSS state is the same as stage 3, text adds context)
            },
             {
                info: "<strong>שלב 6: הצלעות הפנימיות.</strong> כעת, כשהגוף החיצוני בנוי ויציב, מוסיפים את המסגרות הפנימיות – 'הצלעות' של הספינה. הן מחזקות את המבנה עוד יותר, נותנות לו קשיחות נוספת, ומספקות בסיס לסיפון ולספסלי החותרים. הדרקאר מקבלת את צורתה הסופית!",
                stageClass: 'stage-5' // Frames appear
            },
            {
                info: "<strong>שלב 7: הלב והמפרש.</strong> לבסוף, מקימים את התורן החזק במרכז הספינה ומקבעים אותו היטב. מפרש מרובע גדול מתחבר אליו – ועכשיו הדרקאר מוכנה לצאת למסע! היא בנויה לעמוד בפני כל אתגר שהים יציב בפניה. מזל טוב, בנינו ספינת ויקינגים!",
                stageClass: 'stage-6', // Mast and Sail appear
                finalStep: true // Mark as the final step
            }
        ];

        let currentStepIndex = -1; // -1 means before the first step

        // Function to update the visual state based on stage class
        const updateVisualization = (stageClass) => {
             // Remove all previous stage classes
            shipVisualization.className = '';
            // Add the current stage class
            if (stageClass) {
                shipVisualization.classList.add(stageClass);
            }
             // Add a class indicating the presence of *any* stage for base visibility if needed
             if (stageClass !== '') {
                 shipVisualization.classList.add('building-active');
             } else {
                  shipVisualization.classList.remove('building-active');
             }

             // Handle final step animation/message
             if (stageClass === 'stage-6') {
                 setTimeout(() => { // Add final touch after animation completes
                    shipVisualization.classList.add('stage-final');
                 }, 1200); // Delay matches sail animation time
             } else {
                 shipVisualization.classList.remove('stage-final');
             }
        };

         // Function to update the step description
         const updateInfo = (infoText) => {
            stepInfo.innerHTML = `<p>${infoText}</p>`;
        };

        // Handler for step button clicks
        const handleStepClick = (stepIndex) => {
            // Prevent clicking if already on this step or a later disabled step
             if (stepIndex === currentStepIndex || stepButtons[stepIndex].disabled) {
                 return;
             }

            // Update button states: enable up to the clicked step, disable subsequent
             stepButtons.forEach((btn, index) => {
                 btn.disabled = (index > stepIndex);
                 // Remove highlight from previous buttons (if any)
                 btn.classList.remove('active-step');
             });

             // Highlight the current step button
             stepButtons[stepIndex].classList.add('active-step');


            currentStepIndex = stepIndex;
            const step = steps[stepIndex];

            // Update information text
            updateInfo(step.info);

            // Update visualization stage
            let visualStage = '';
            if (stepIndex >= 0 && steps[stepIndex].stageClass) {
                visualStage = steps[stepIndex].stageClass;
            }
            updateVisualization(visualStage);

            // Enable the *next* button if it exists and isn't the final step
            if (stepIndex < steps.length - 1) {
                stepButtons[stepIndex + 1].disabled = false;
            }
        };

        // Add event listeners to buttons
        stepButtons.forEach((button, index) => {
            // Initially disable all buttons except the first one
            if (index > 0) {
                button.disabled = true;
            }
            button.addEventListener('click', () => {
                handleStepClick(index);
            });
        });

        // Toggle explanation visibility
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            // toggleButton.textContent = isHidden ? 'הסתר הסבר מורחב' : 'הצג/הסתר הסבר מורחב'; // Keeping original text per instruction example, maybe refine later
            toggleButton.textContent = isHidden ? 'הסתר את יומן הבנאי' : 'הצג/הסתר את יומן הבנאי המורחב'; // More thematic text
        });

        // Initial state setup
        updateVisualization(''); // Start with initial state (water only)
        updateInfo("לחצו על 'העץ מתעורר לחיים' כדי להתחיל במסע הבנייה!"); // Initial info
        stepButtons[0].disabled = false; // Enable the first step button

    });
</script>
---
```