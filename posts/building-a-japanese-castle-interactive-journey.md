---
title: "בונים טירה יפנית: מסע אינטראקטיבי"
english_slug: building-a-japanese-castle-interactive-journey
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags:
  - טירות יפניות
  - אדריכלות
  - היסטוריה של יפן
  - בנייה
  - תרבות יפן
---
# בונים טירה יפנית: מסע אינטראקטיבי מלב הסאמוראים

צאו למסע בזמן אל יפן הפיאודלית! האם אתם מוכנים לפענח את סודות הבנייה של המבצרים המרשימים ביותר בהיסטוריה? הצטרפו למסע אינטראקטיבי מרתק וגלו שלב אחר שלב כיצד הפכו ערימות אבן ועץ לטירות אימתניות, מעוז של כוח והגנה. הפעילו את הסימולציה ובנו את הטירה בעצמכם!

<div class="interactive-castle-app">
    <div id="castle-view" class="stage-0">
        <div id="stage-label" class="castle-label">אתר ריק</div>
        <div id="ground-prep-moat" class="castle-layer"></div>
        <div id="stone-walls" class="castle-layer"></div>
        <div id="main-tower-base" class="castle-layer"></div>
         <div id="main-tower-body" class="castle-layer"></div>
        <div id="secondary-buildings" class="castle-layer"></div>
         <div id="gates-outer" class="castle-layer"></div>
        <div id="completed-overlay" class="castle-layer"></div>
    </div>

    <div class="controls">
         <button id="prev-stage" class="nav-button" disabled>&lt; הקודם</button>
         <button id="next-stage" class="nav-button">הבא &gt;</button>
    </div>
     <div class="stage-selection">
         <button data-stage="0">התחלה</button>
         <button data-stage="1">שלב 1</button>
         <button data-stage="2">שלב 2</button>
         <button data-stage="3">שלב 3</button>
         <button data-stage="4">שלב 4</button>
         <button data-stage="5">שלב 5</button>
    </div>
</div>

<style>
    :root {
        --primary-color: #a0522d; /* Earthy brown */
        --secondary-color: #cd853f; /* Lighter brown/tan */
        --stone-color: #a9a9a9; /* Dark gray */
        --water-color: #add8e6; /* Light blue */
        --wood-color: #8b4513; /* Saddle brown */
        --accent-color: #4682b4; /* Steel blue */
        --text-color: #333;
        --bg-color: #f5f5dc; /* Beige */
        --container-bg: #fff;
        --border-color: #d3d3d3;
        --shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --transition-speed: 0.6s;
    }

    .interactive-castle-app {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        margin: 30px auto;
        max-width: 850px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        background-color: var(--container-bg);
        padding: 20px;
        box-shadow: var(--shadow);
        text-align: center;
        overflow: hidden;
    }

    #castle-view {
        position: relative;
        width: 100%;
        height: 450px; /* Increased height for better visualization */
        background: linear-gradient(to bottom, #87ceeb 0%, #87ceeb 60%, var(--bg-color) 60%, var(--bg-color) 100%); /* Simple sky and ground */
        border: 1px solid var(--border-color);
        margin-bottom: 25px;
        overflow: hidden;
        border-radius: 8px;
    }

     .castle-label {
        position: absolute;
        top: 15px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.8);
        padding: 8px 15px;
        border-radius: 5px;
        font-size: 1.1em;
        font-weight: bold;
        color: var(--text-color);
        z-index: 10;
        transition: opacity var(--transition-speed) ease-in-out;
    }


    .castle-layer {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 0%; /* Start hidden */
        height: 0%; /* Start hidden */
        opacity: 0;
        transition: opacity var(--transition-speed) ease-out, width var(--transition-speed) ease-out, height var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out;
        box-sizing: border-box;
    }

    /* Layer Specific Styles */
    #ground-prep-moat {
        width: 90%;
        height: 40%; /* Represents base ground work/moat */
        background: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
         border-radius: 50% / 10% 10% 0 0; /* Simple hill shape */
         bottom: -10%; /* Start slightly below */
         transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out;
    }
     #stone-walls {
        width: 80%;
        height: 30%;
        background-color: var(--stone-color);
        bottom: 25%; /* Position on the ground layer */
        clip-path: polygon(0% 100%, 5% 0%, 95% 0%, 100% 100%); /* Basic trapezoid for wall base */
        transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out, width var(--transition-speed) ease-out, clip-path var(--transition-speed) ease-out;
    }

    #main-tower-base {
        width: 20%;
        height: 15%;
        background-color: var(--wood-color);
        bottom: 54%; /* On top of walls */
        z-index: 2;
        transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out, width var(--transition-speed) ease-out, height var(--transition-speed) ease-out;
    }
     #main-tower-body {
        width: 20%;
        height: 30%;
        background-color: rgba(255, 255, 255, 0.9); /* White plaster effect */
        border: 2px solid var(--wood-color);
        bottom: 68%; /* On top of base */
        z-index: 3;
         transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out, height var(--transition-speed) ease-out;
     }

    #secondary-buildings {
        width: 50%;
        height: 15%;
        background-color: rgba(var(--wood-color), 0.8); /* Slightly transparent wood */
        border: 1px solid var(--wood-color);
        bottom: 54%; /* On top of walls, next to tower */
        left: calc(50% + 15%); /* Position to the side */
         transform: translateX(-50%);
        z-index: 2;
         transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out, width var(--transition-speed) ease-out;
    }

     #gates-outer {
        width: 90%;
        height: 45%; /* Represents the moat and outer gates */
        background-color: rgba(var(--water-color), 0.7);
        border-radius: 50% / 10% 10% 0 0; /* Matches ground shape */
         bottom: -5%; /* Slightly above ground */
        z-index: 4; /* Above ground */
         transition: opacity var(--transition-speed) ease-out, bottom var(--transition-speed) ease-out;

     }
     #gates-outer::before { /* Simple gate representation */
         content: '';
         position: absolute;
         bottom: 30%;
         left: 50%;
         transform: translateX(-50%);
         width: 10%;
         height: 30%;
         background-color: var(--wood-color);
         border: 2px solid #000;
         z-index: 5;
     }


    #completed-overlay {
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.95) url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MDIgNDU4Ij48ZyBmaWxsPSIjYTBlMGEwIj48cGF0aCBkPSJNMzE3LjUgMTEyLjVsLTE5Mi05Ny44Yy0zLjgtMS45LTguNC0xLjQtMTEuOSAxLjMtMy41IDIuNy01LjYgNi45LTUuNiAxMS4zdjE5Mi41YzAgNC41IDIuMiA4LjYgNS42IDExLjQgMy42IDIuNiA4LjEgMy4xIDExLjkgMS4xbDE5Mi05Ny44YzMuOC0xLjkgNi4xLTUuOCA2LjEtOS41cy0yLjMtNy41LTYuMS05LjR6Ii8+PHBhdGggZD0iTTQ5NC41IDE5Ni42bC0xNzcuNy05MS43Yy0zLjktMi04LjUtMS42LTExLjkgMS4xLTMuNSAyLjctNS41IDYuOS01LjUgMTEuNHYxODMuMmMwIDQuNSAyLjEgOC42IDUuNSA1LjZjMy42IDIuNiA4LjEgMy4xIDExLjkgMS4xbDE3Ny43LTkxLjdjMy45LTIgNi4xLTUuOCA2LjEtOS42cy0yLjItNy42LTYuMS05LjV6Ii8+PHBhdGggZD0iTTMxMC42IDMwNC4zbC0xNzcuNy05MS43Yy0zLjktMi04LjUtMS42LTExLjkgMS4xLTMuNSAyLjctNS41IDYuOS01LjUgMTEuNHYxODMuMmMwIDQuNSAyLjEgOC42IDUuNSA1LjZjMy42IDIuNiA4LjEgMy4xIDExLjkgMS4xbDE3Ny43LTkxLjdjMy45LTIgNi4xLTUuOCA2LjEtOS42cy0yLjItNy42LTYuMS05LjV6Ii8+PHBhdGggZD0iTTEyNi43IDQxMmwtMTc3LjctOTEuN2MtMy45LTItOC41LTEuNi0xMS45IDEuMS0zLjUgMi43LTUuNSA2LjktNS41IDExLjR2MTgzLjJjMCA0LjUgMi4xIDguNiA1LjUgNS42YzMuNiAyLjYgOC4xIDMuMSAxMS45IDEuMWwxNzcuNy05MS43YzMuOS0yIDYuMS01LjggNi4xLTkuNnMtMi4yLTcuNi02LjEtOS41eiIvPjxwYXRoIGQ9Ik0zMDUuMyAyMDYuNGwtMTc3LjctOTEuN2MtMy45LTItOC41LTEuNi0xMS45IDEuMS0zLjUgMi43LTUuNSA2LjktNS41IDExLjR2MTgzLjJjMCA0LjUgMi4xIDguNiA1LjUgNS42YzMuNiAyLjYgOC4xIDMuMSAxMS45IDEuMWwxNzcuNy05MS43YzMuOS0yIDYuMS01LjggNi4xLTkuNnMtMi4yLTcuNi02LjEtOS41eiIvPjxwYXRoIGQ9Ik0yNTMuNiA0MjQuMWwtMjIzLjktMTE5LjRjLTQuMS0yLjEtOS4xLTEuOS0xMi43IDEuMS0zLjYgMy01LjcgNy41LTUuNyAxMi4zdi45YzAgNC44IDIuMSA5LjQgNS43IDEyLjQgMy42IDIuOSAxMC41IDMuMiAxMi43IDEuMWwyMjMuOS0xMTkuNGM0LjEtMi4xIDYuNC02LjMgNi40LTEwLjRzLTIuMy04LjMtNi40LTEwLjR6Ii8+PC9nPjwvc3ZnPg==') center center no-repeat;
         background-size: 100px; /* Simple pattern indicating completion */
        z-index: 20; /* On top of everything else */
         color: var(--text-color);
         font-size: 2em;
         font-weight: bold;
         display: flex;
         justify-content: center;
         align-items: center;
         text-align: center;
         opacity: 0; /* Hidden initially */
        transition: opacity var(--transition-speed) ease-in-out;
    }

    /* Stage-Specific Styles */
     .stage-0 .castle-label { content: 'אתר ריק'; opacity: 1; }
     .stage-0 .castle-layer { opacity: 0; }

    .stage-1 #ground-prep-moat { opacity: 1; bottom: 0; width: 90%; height: 40%; }
     .stage-1 .castle-label { content: 'שלב 1: הכנת אתר ובניית חפיר'; opacity: 1;}
     .stage-1 #stone-walls, .stage-1 #main-tower-base, .stage-1 #main-tower-body, #secondary-buildings, #gates-outer, #completed-overlay { opacity: 0; }


    .stage-2 #ground-prep-moat { opacity: 1; bottom: 0; width: 90%; height: 40%; }
    .stage-2 #stone-walls { opacity: 1; bottom: 25%; width: 80%; height: 30%; }
    .stage-2 .castle-label { content: 'שלב 2: בניית חומות אבן (אישיגאקי)'; opacity: 1;}
     .stage-2 #main-tower-base, .stage-2 #main-tower-body, #secondary-buildings, #gates-outer, #completed-overlay { opacity: 0; }


    .stage-3 #ground-prep-moat { opacity: 1; bottom: 0; width: 90%; height: 40%; }
    .stage-3 #stone-walls { opacity: 1; bottom: 25%; width: 80%; height: 30%;}
    .stage-3 #main-tower-base { opacity: 1; bottom: 54%; width: 20%; height: 15%;}
    .stage-3 #main-tower-body { opacity: 1; bottom: 68%; height: 30%;}
    .stage-3 .castle-label { content: 'שלב 3: הקמת המגדל הראשי (טנשו)'; opacity: 1;}
    .stage-3 #secondary-buildings, #gates-outer, #completed-overlay { opacity: 0;}


    .stage-4 #ground-prep-moat { opacity: 1; bottom: 0; width: 90%; height: 40%;}
    .stage-4 #stone-walls { opacity: 1; bottom: 25%; width: 80%; height: 30%;}
    .stage-4 #main-tower-base { opacity: 1; bottom: 54%; width: 20%; height: 15%;}
    .stage-4 #main-tower-body { opacity: 1; bottom: 68%; height: 30%;}
    .stage-4 #secondary-buildings { opacity: 1; bottom: 54%; width: 50%; height: 15%;}
    .stage-4 .castle-label { content: 'שלב 4: מבנים משניים וחצרות'; opacity: 1;}
    .stage-4 #gates-outer, #completed-overlay { opacity: 0;}

    .stage-5 #ground-prep-moat { opacity: 1; bottom: 0; width: 90%; height: 40%;}
    .stage-5 #stone-walls { opacity: 1; bottom: 25%; width: 80%; height: 30%;}
    .stage-5 #main-tower-base { opacity: 1; bottom: 54%; width: 20%; height: 15%;}
    .stage-5 #main-tower-body { opacity: 1; bottom: 68%; height: 30%;}
    .stage-5 #secondary-buildings { opacity: 1; bottom: 54%; width: 50%; height: 15%;}
     .stage-5 #gates-outer { opacity: 1; bottom: -5%; width: 90%; height: 45%;}
    .stage-5 #completed-overlay { opacity: 1; } /* Final stage shows completed overlay */
     .stage-5 .castle-label { opacity: 0; } /* Hide specific label when completed overlay is shown */
     #completed-overlay::before { /* Text on overlay */
         content: "הטירה הושלמה!";
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         color: var(--text-color);
         font-size: 1.8em;
         text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.5);
     }


    .controls, .stage-selection {
        margin-top: 15px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
    }
     .stage-selection {
         margin-top: 10px;
     }


    .controls button, .stage-selection button {
        padding: 10px 18px;
        font-size: 1em;
        cursor: pointer;
        border: 1px solid var(--accent-color);
        border-radius: 6px;
        background-color: var(--accent-color);
        color: white;
        transition: background-color 0.3s ease, opacity 0.3s ease;
        font-weight: bold;
    }

    .controls button:hover, .stage-selection button:hover:not(:disabled) {
        background-color: #3670a0;
        border-color: #3670a0;
    }
     .controls button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
     }

     .stage-selection button[data-active="true"] {
         background-color: #ff6347; /* Tomato color for active stage */
         border-color: #ff6347;
     }

     .explanation-toggle-button {
        display: block;
        margin: 30px auto 20px auto;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: 1px solid #28a745;
        border-radius: 6px;
        background-color: #28a745;
        color: white;
        transition: background-color 0.3s ease;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .explanation-toggle-button:hover {
        background-color: #218838;
    }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background-color: #f9f9f9;
        text-align: right;
        display: none; /* Initially hidden */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    #explanation h2 {
        text-align: center;
        margin-top: 0;
        margin-bottom: 20px;
        color: var(--accent-color);
        font-size: 1.6em;
    }

    #explanation p, #explanation ul {
        line-height: 1.8;
        margin-bottom: 18px;
        color: var(--text-color);
    }

     #explanation ul {
         padding-right: 25px;
     }

     #explanation li {
         margin-bottom: 10px;
         position: relative;
         padding-right: 15px;
     }
     #explanation li::before {
         content: '•';
         position: absolute;
         right: 0;
         color: var(--accent-color);
         font-weight: bold;
     }
      #explanation strong {
          color: var(--primary-color);
      }
</style>

<button class="explanation-toggle-button" id="toggle-explanation">פתח את מגילת הסודות! (הסבר)</button>

<div id="explanation">
    <h2>פענוח סודות הטירה היפנית</h2>
    <p>הטירות היפניות (המכונות ביפנית "שירו") היו הרבה יותר ממבצרים צבאיים. הן היו ליבה הפועם של יפן הפיאודלית – מרכזי שלטון, כלכלה ותרבות, וסמל עוצמתו של הדאימיו (השליט המקומי). בניית טירה הייתה מפעל אדיר שגייס משאבים וכוח אדם עצומים, ויצר יצירות ארכיטקטוניות שהיו גם מופת הנדסי וגם פסגת האסתטיקה.</p>

    <ul>
        <li>
            <strong>לבחור את הנקודה המנצחת: האתר והחפיר</strong>
            הכל מתחיל במיקום! הדאימיו היה בוחר בקפידה אתר אסטרטגי – לרוב גבעה השולטת על סביבתה, סמוך לנהר או נמל, כדי לשלוט בדרכי תנועה ולנצל מכשולים טבעיים. השלב הראשון כלל יישור שטח, ביסוס יסודות עמוקים וחפירת חפיר (הורו) רחב סביב מתחם הטירה. החפיר, מלא במים או יבש, נועד להרחיק את התוקפים ולהכריח אותם להתכנס בנקודות מעבר צרות ופגיעות. האדמה שנחפרה שימשה לעיתים קרובות לבניית סוללות עפר שחיזקו את ההגנה.
        </li>
        <li>
            <strong>עמוק ויציב: חומות האבן (אישיגאקי)</strong>
            גאוות כל טירה יפנית הן חומות האבן המסיביות שלה, ה"אישיגאקי". שלא כמו בטירות אירופאיות שבנו עם מלט, היפנים השתמשו בטכניקה גאונית של הנחת אבנים ענקיות, לרוב ללא סיתות או בסיתות גס, זו על גבי זו. האבנים הכבדות ביותר הונחו בבסיס, ורווחים מולאו באבנים קטנות יותר ואדמה. החומות נבנו בשיפוע קל כלפי מעלה (המכונה "עקומת מניפה" - אוגי קורוי), מה שהקשה על המטפסים והעניק יציבות מדהימה נגד רעידות אדמה, תופעה שכיחה ביפן. חומות אלו יכלו להגיע לגובה של עשרות מטרים ולעובי של מספר מטרים בבסיסן.
        </li>
        <li>
            <strong>שמים את הכתר: המגדל הראשי (טנשו)</strong>
            ה"טנשו" – המגדל הראשי והמפורסם – היה לב הטירה וסמל כוחו של הדאימיו. הוא נבנה לרוב על בסיס אבן מסיבי, שהיה חלק מחומות הטירה עצמן. המבנה העילי, בגובה של 3 עד 6 קומות ויותר, נבנה ברובו מעץ עץ עבה וחזק, מצופה בטיח לבן או עץ כהה. פנים המגדל הכיל רצפות עץ, קורות תמך עצומות ומדרגות תלולות. הטנשו שימש כעמדת תצפית אסטרטגית, מחסן נשק ואספקה חיונית, ולעתים גם כמקום מקלט אחרון בעת מצור. גובהו המרשים הבטיח שהוא יישמע למרחקים ויוכיח את מעמדו הרם של בעליו.
        </li>
        <li>
            <strong>החיים בתוך המבצר: מבנים משניים וחצרות (קורוה)</strong>
            סביב הטנשו המרכזי נבנו מערכות מורכבות של חצרות פנימיות (קורוה), מופרדות על ידי חומות נמוכות יותר ומגדלי שמירה קטנים (יאגורה). בחצרות אלו שוכנו מבני מגורים לדאימיו ומשפחתו (גוטן), מגורי הסמוראים, מחסנים, מטבחים ובארות מים. כל חצר שימשה שכבת הגנה נוספת, והדרך ביניהן הייתה מתוכננת בקפידה עם שערים מורכבים ומעברים מפותלים כדי לבלבל ולהאט כל פולש.
        </li>
        <li>
            <strong>השערים השומרים: מערכות הגנה נוספות</strong>
            השערים (מון) של טירות יפניות היו פלא הנדסי בפני עצמו. לעיתים קרובות היו אלה שערים כפולים עם חצר פנימית קטנה ביניהם (מבנה מאסוגאטה), שתפקידה היה ללכוד את התוקפים בין שני שערים ולאפשר למגנים לירות עליהם מלמעלה ומכל הצדדים. גשרים מתרוממים מעל החפיר, פתחי ירי מוסתרים בחומות וגדרות עץ חודרות (סאמורה) היו חלק ממערך הגנה שתוכנן לפרטי פרטים כדי להפוך את הטירה למכונת הגנה כמעט מושלמת.
        </li>
         <li>
            <strong>מפעל חיים: משך ועלות הבנייה</strong>
             בניית טירה הייתה פרויקט לאומי או אזורי שדרש עשרות אלפי עובדים - מסמוראים מפקחים ועד איכרים שגויסו לעבודות כפיים קשות. הובלת אבנים ענקיות למרחקים, כריתת יערות שלמים עבור קורות עץ ובניית המבנים המורכבים ארכו שנים רבות, לעיתים עשור ואף יותר, ורוקנו משאבים כלכליים עצומים מהאזור.
         </li>
    </ul>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const castleView = document.getElementById('castle-view');
        const stageLabel = document.getElementById('stage-label');
        const stageSelectionButtons = document.querySelectorAll('.stage-selection button');
        const prevButton = document.getElementById('prev-stage');
        const nextButton = document.getElementById('next-stage');
        const explanationDiv = document.getElementById('explanation');
        const toggleButton = document.getElementById('toggle-explanation');

        let currentStage = 0;
        const maxStage = 5; // Total stages including 0

        const stageDescriptions = [
            "אתר ריק: רק השטח הטבעי",
            "שלב 1: הכנת אתר ובניית חפיר",
            "שלב 2: בניית חומות אבן (אישיגאקי)",
            "שלב 3: הקמת המגדל הראשי (טנשו)",
            "שלב 4: מבנים משניים וחצרות",
            "שלב 5: הטירה הושלמה!"
        ];


        // Function to update the castle visualization based on the stage
        function updateCastleView(stage) {
            // Clamp stage value
            stage = Math.max(0, Math.min(maxStage, stage));

            // Update castle view class for CSS transitions
            castleView.classList.remove('stage-' + currentStage);
            castleView.classList.add('stage-' + stage);

            // Update stage label text (CSS handles visibility/text for stage 5)
             if (stage < maxStage) {
                stageLabel.textContent = stageDescriptions[stage];
             }


            // Update active button in stage selection
            stageSelectionButtons.forEach(button => {
                const buttonStage = parseInt(button.getAttribute('data-stage'), 10);
                if (buttonStage === stage) {
                    button.setAttribute('data-active', 'true');
                } else {
                    button.removeAttribute('data-active');
                }
            });

            // Update navigation button states
            prevButton.disabled = (stage === 0);
            nextButton.disabled = (stage === maxStage);

            // Update current stage variable
            currentStage = stage;

             // Accessibility: Announce stage change (optional but good practice)
             // console.log(`Moved to stage ${currentStage}: ${stageDescriptions[currentStage]}`);
        }

        // Add event listeners to the stage selection buttons
        stageSelectionButtons.forEach(button => {
            button.addEventListener('click', () => {
                const stage = parseInt(button.getAttribute('data-stage'), 10);
                updateCastleView(stage);
            });
        });

         // Add event listeners for Next/Previous buttons
         prevButton.addEventListener('click', () => {
             updateCastleView(currentStage - 1);
         });

         nextButton.addEventListener('click', () => {
             updateCastleView(currentStage + 1);
         });

        // Add event listener to the toggle explanation button
        toggleButton.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
             // Update button text based on state
             toggleButton.textContent = isHidden ? "סגור את מגילת הסודות" : "פתח את מגילת הסודות! (הסבר)";
        });

        // Initialize the view to stage 0 on load
        updateCastleView(0);
    });
</script>