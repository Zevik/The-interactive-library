---
title: "משיש לאל: מסע הפיסול הפיגורטיבי הקלאסי"
english_slug: from-marble-to-form-classical-sculpture-journey
category: "אמנות ועיצוב / אמנות חזותית"
tags:
  - פיסול
  - שיש
  - אמנות קלאסית
  - פיסול פיגורטיבי
  - שיטת הנקודות
  - סדנה
---
# משיש לאל: מסע הפיסול הפיגורטיבי הקלאסי

איך גוש שיש חסר צורה הופך ליצירת מופת אלמותית, מלאת חיים ועוצמה? הצטרפו אלינו למסע מרתק אל עומק הסטודיו של הפסל הקלאסי וגלו את סודות המלאכה שהפכו אמנים לגאונים ואבנים קפואות ליצורים נושמי נצח.

<div id="sculpture-app" class="app-container">
    <div id="stage-container" class="stage-area">
        <!-- Stage 1: The Beginning -->
        <div class="stage active" id="stage-1">
            <h2 class="stage-title">שלב 1: החזון והמודל</h2>
            <p class="stage-description">הכל מתחיל בחלום, ברעיון. רעיון זה מתגבש לגוש שיש גולמי ענק ולמודל מוקפד, לרוב מחימר או גבס. המודל הוא המפה המדויקת למסע הפיסול.</p>
            <div class="stage-content stage-1-content">
                <div class="visual-asset marble-block">
                    <!-- Placeholder for the raw marble block -->
                     <img src="https://via.placeholder.com/350x450?text=גוש+שיש+גולמי" alt="גוש שיש גדול וגולמי" class="asset-image">
                </div>
                 <div class="visual-asset model">
                    <!-- Placeholder for the model -->
                    <img src="https://via.placeholder.com/180x360?text=מודל+גבס" alt="מודל קטן של פסל מחימר או גבס" class="asset-image">
                 </div>
            </div>
             <p class="instruction animated-instruction">צפו בחומרי הגלם שמהם נולדת האמנות.</p>
        </div>

        <!-- Stage 2: Blocking Out -->
        <div class="stage" id="stage-2">
            <h2 class="stage-title">שלב 2: החסימה (Blocking Out)</h2>
            <p class="stage-description">בעזרת פטישים ואזמלים כבדים, הפסל מסיר גושי שיש גדולים. זוהי מלאכה פיזית החושפת את הצורה הבסיסית הנסתרת בתוך האבן.</p>
            <div class="stage-content stage-2-content">
                <div class="visual-asset blocked-marble" id="blocked-marble">
                     <!-- Background image represents the marble -->
                     <img src="https://via.placeholder.com/350x450?text=שיש+אחרי+חסימה" alt="גוש שיש עם צורה כללית חסומה" class="asset-image">
                    <!-- Interactive overlays representing material to remove -->
                    <div class="block-overlay block-1" data-block="1"></div>
                    <div class="block-overlay block-2" data-block="2"></div>
                    <div class="block-overlay block-3" data-block="3"></div>
                    <div class="block-overlay block-4" data-block="4"></div>
                     <div class="tool-icon chisel-heavy">🔨</div> <!-- Heavy chisel icon -->
                </div>
            </div>
            <p class="instruction interactive-instruction" id="stage-2-instruction">לחצו על האזורים המוצללים באפור כדי להסיר "שיש" ולחשוף את צורת הבסיס!</p>
        </div>

        <!-- Stage 3: Pointing -->
        <div class="stage" id="stage-3">
            <h2 class="stage-title">שלב 3: שיטת הנקודות (Pointing)</h2>
            <p class="stage-description">כדי להעתיק את המודל במילימטרים, נעזרים במכונת נקודות מיוחדת. היא מודדת נקודות על המודל הקטן ומעבירה את המיקום והעומק המדויק שלהן לגוש השיש הגדול.</p>
            <div class="stage-content stage-3-content">
                 <div class="visual-asset model pointing-model" id="pointing-model-asset">
                     <img src="https://via.placeholder.com/180x360?text=מודל+גבס+למדידה" alt="מודל גבס עם סימונים אפשריים" class="asset-image">
                      <!-- Clickable points on the model -->
                      <div class="clickable-point" data-point="1" style="top: 20%; left: 40%;"></div> <!-- Head -->
                      <div class="clickable-point" data-point="2" style="top: 50%; left: 60%;"></div> <!-- Shoulder -->
                      <div class="clickable-point" data-point="3" style="top: 75%; left: 35%;"></div> <!-- Knee -->
                 </div>
                  <div class="visual-asset pointing-machine">
                      <img src="https://via.placeholder.com/100x200?text=מכונת+נקודות" alt="מכונת נקודות למדידה" class="asset-image tool-image">
                  </div>
                 <div class="visual-asset marble-with-points" id="pointing-marble-asset">
                    <img src="https://via.placeholder.com/350x450?text=שיש+עם+סימונים" alt="גוש שיש מוכן לסימוני נקודות" class="asset-image">
                      <!-- Point indicators (will be positioned by JS) -->
                      <div class="point-indicator model-point"></div>
                      <div class="point-indicator marble-point"></div>
                      <div class="measurement-line"></div>
                 </div>
            </div>
             <p class="instruction interactive-instruction" id="stage-3-instruction">לחצו על אחד מהנקודות האדומות על המודל כדי לראות איך המידה עוברת לשיש!</p>
        </div>

        <!-- Stage 4: Sculpting Details -->
        <div class="stage" id="stage-4">
            <h2 class="stage-title">שלב 4: עיצוב ופירוט</h2>
            <p class="stage-description">הקסם קורה כשהפסל לוקח אזמלים קטנים ועדינים יותר, מגרדות ומקדחים. עכשיו הוא "מצייר" באבן, חושף את תווי הפנים, קפלי הבגד, השיער, ושרירים - כל מה שמעניק לפסל את אופיו.</p>
            <div class="stage-content stage-4-content">
                <div class="visual-asset detailed-marble" id="detailed-marble-asset">
                     <img src="https://via.placeholder.com/350x450?text=פסל+בשלב+פירוט" alt="פסל שיש עם פירוט ראשוני" class="asset-image">
                     <!-- Interactive areas for detailing -->
                     <div class="detail-area face" data-detail="face" style="top: 15%; left: 50%; width: 80px; height: 100px; transform: translateX(-50%);">פנים</div>
                     <div class="detail-area drapery" data-detail="drapery" style="top: 60%; left: 30%; width: 120px; height: 150px;">בגד</div>
                     <div class="detail-area limb" data-detail="limb" style="top: 40%; right: 20%; width: 70px; height: 200px;">יד/רגל</div>
                </div>
                 <div class="visual-asset tools">
                     <img src="https://via.placeholder.com/150x100?text=כלים+עדינים" alt="אזמלים קטנים ומגרדות" class="asset-image tool-image">
                </div>
            </div>
            <p class="instruction interactive-instruction" id="stage-4-instruction">לחצו על האזורים המסומנים (פנים, בגד, יד/רגל) כדי "לפסל" את הפרטים העדינים!</p>
        </div>

        <!-- Stage 5: Finishing -->
        <div class="stage" id="stage-5">
            <h2 class="stage-title">שלב 5: ליטוש וגימור מבריק</h2>
            <p class="stage-description">נגיעות הקסם האחרונות. הפסל מלטש את פני השטח בחומרים שונים – החל מאבני ליטוש ונייר זכוכית (גרסאות עתיקות) ועד משחות מיוחדות. הליטוש חושף את השקיפות העדינה של השיש ומעניק לפסל את המראה החלק, החי והמבריק שלו.</p>
             <div class="stage-content stage-5-content">
                 <div class="visual-asset finished-sculpture" id="finished-sculpture-asset">
                     <img src="https://via.placeholder.com/350x450?text=פסל+מוגמר+מלוטש" alt="פסל שיש מוגמר ומבריק" class="asset-image">
                      <!-- Interactive area for polishing -->
                      <div class="polish-overlay"></div>
                 </div>
                  <div class="visual-asset tools">
                      <img src="https://via.placeholder.com/150x100?text=חומרי+ליטוש" alt="חומרי ליטוש וגימור" class="asset-image tool-image">
                 </div>
            </div>
             <p class="instruction interactive-instruction" id="stage-5-instruction">לחצו שוב ושוב על הפסל כדי "ללטש" אותו ולגרום לו לזהור!</p>
        </div>
    </div>

    <div class="controls">
        <button id="prev-stage" class="control-button" disabled>שלב קודם</button>
        <button id="next-stage" class="control-button">שלב הבא</button>
    </div>
</div>

<button id="toggle-explanation" class="explanation-toggle-button">הצג הסבר מעמיק על הפיסול הקלאסי</button>

<div id="explanation" class="explanation-area" style="display: none;">
    <h2>הסבר מעמיק: מסע הפיסול בשיש - אמנות בת אלפי שנים</h2>
    <p>פיסול שיש פיגורטיבי קלאסי הוא אחת האומנויות הנעלות והדורשניות ביותר בהיסטוריה האנושית. פסלים קדומים ומודרניים כאחד התמודדו עם האבן האדירה והפיחו בה רוח חיים, תוך שימוש בשילוב מופלא של חזון אמנותי, ידע מדעי-אנטומי, ומיומנות טכנית שאין לה רבות.</p>

    <h3>מה מייחד פיסול שיש פיגורטיבי קלאסי?</h3>
    <p>סגנון זה, שהגיע לשיאו ביוון וברומא העתיקות ובהמשך ברנסנס, מתמקד ביצירת דמויות אדם, אלים או גיבורים משיש. המאפיינים המרכזיים כוללים הקפדה יתרה על פרופורציות אנטומיות מדויקות, תנועה, הבעות פנים, ועיצוב עשיר של פרטים - מבגדים נשפכים ועד תלתלי שיער עדינים. המטרה לרוב הייתה אידיאליזציה של הדמות, הצגת היופי, הכוח והשאיפה לשלמות אנושית ואלוהית כאחד.</p>

    <h3>קסם השיש: למה דווקא האבן הזו?</h3>
    <p>שיש אינו סתם אבן; הוא סלע מטמורפי הנוצר מסלע גיר שעבר שינויים קיצוניים של חום ולחץ לאורך מיליוני שנים. תכונותיו הייחודיות הופכות אותו לחומר גלם אידיאלי (אם כי מאתגר) לפיסול:</p>
    <ul>
        <li>**עמידות נצחית:** מסוגל לשרוד אלפי שנים, עומד בפני פגעי טבע וזמן.</li>
        <li>**עיבוד נוח יחסית:** בהשוואה לסלעים קשים יותר כמו גרניט, ניתן לעבד שיש עם אזמלים וכלים אחרים ברמה גבוהה של דיוק.</li>
        <li>**הטרנסלוסנטיות הקסומה:** זו אולי התכונה המופלאה ביותר. אור חודר מעט פנימה לשכבות השיש העליונות לפני שהוא מוחזר. זה מעניק לפסל תחושת עומק, רכות, ומדמה באופן מדהים את מראה העור האנושי החי.</li>
        <li>**טוהר וטקסטורה:** לרוב לבן וטהור, אך יכול להכיל גם ורידים בצבעים שונים המוסיפים אופי. המבנה הגבישי העדין מאפשר יצירת משטחים חלקים ומבריקים ופרטים חדים כתער.</li>
    </ul>

    <h3>מתודולוגיה של גאונים: שלבי העבודה המסורתיים</h3>
    <p>פיסול בשיש הוא תהליך של גריעה בלבד – מה שהוסר אינו חוזר. לכן, כל תנועת אזמל דורשת תכנון קפדני, דיוק אינסופי, וראייה מרחבית יוצאת דופן.</p>
    <ul>
        <li>**בחירת החומר והכנה:** איתור גוש שיש איכותי ללא סדקים או פגמים פנימיים הוא צעד יסודי. לפעמים מתבצעת "חסימה" גסה כבר במחצבה.</li>
        <li>**שלב ה'חסימה' (Blocking Out):** שימוש באזמלים כבדים ופטישים להסרת כמויות גדולות של חומר. המטרה היא להפחית את גוש השיש לצורה כללית ומוגדרת שקרובה לצורת הפסל המתוכנן. זהו שלב של גילוף גס שדורש כוח והבנה של הנפחים העיקריים.</li>
        <li>**שיטת הנקודות (Pointing System):** טכניקה שפותחה ואומצה כדי לאפשר העתקה מדויקת של מודלים קטנים לגודל מלא בשיש. מכשיר ה'פוינטר' (מכונת נקודות) מודד אלפי נקודות ייחוס ועומק על המודל, ונקודות אלו מועברות בקפידה לשיש. הפסל חורג עד לסימון העומק בכל נקודה, מה שמאפשר דיוק בלתי רגיל ומקטין את הסיכון לטעויות הרסניות.</li>
        <li>**פירוט ועיצוב עדין:** לאחר שהפרופורציות והנפחים העיקריים הוגדרו, עוברים לכלים עדינים יותר – אזמלים קטנים, סכיני גילוף, ומגרדות (Rasps, Rifflers). בשלב זה נוצרים תווי הפנים, מובלטות עצמות ושרירים, ומעוצבים קפלי הבגד והשיער באמנות מירבית. זהו שלב שדורש סבלנות, מיומנות טכנית גבוהה, ורגישות אמנותית.</li>
        <li>**ליטוש וגימור:** השלב הסופי המעניק לפסל את ה"חיים" שלו. שימוש הדרגתי בחומרים שוחקים עדינים יותר ויותר (מאבנים טבעיות גסות ועד משחות ליטוש) הופך את פני השטח לחלקים ומבריקים. הליטוש הנכון מדגיש את יופיו הטבעי של השיש ואת הטרנסלוסנטיות הייחודית שלו, וניתן לשנות את רמת הליטוש באזורים שונים כדי ליצור טקסטורות מנוגדות (למשל, עור מלוטש לעומת שיער פחות מלוטש).</li>
    </ul>

    <h3>כלים מסורתיים: ידיהם המורחבות של הפסלים</h3>
    <p>הפסלים הקלאסיים הסתמכו על מגוון רחב של כלים ידניים, שכל אחד שימש למטרה ספציפית:</p>
    <ul>
        <li>**פטישים ואזמלים:** בגדלים שונים – כבדים לחסימה גסה, קטנים ועדינים לפירוט.</li>
        <li>**מגרדות (Rasps & Rifflers):** כלי שיוף ידניים להסרת חומר בקנה מידה קטן ולעיצוב עקומות עדינות.</li>
        <li>**מקדחים:** שימשו לחורים עמוקים או להסרת חומר מהירה באזורים מסוימים.</li>
        <li>**מכונת נקודות (Pointing Machine):** המכשיר המכני שאיפשר העתקה מדויקת מהמודל לשיש.</li>
        <li>**חומרי ליטוש:** החל מחול ואבני ליטוש טבעיות ועד משחות מיוחדות לשלב הגימור הסופי.</li>
    </ul>

    <h3>יצירות מופת שהשפיעו על העולם</h3>
    <p>המורשת של הפיסול הקלאסי נשמרת ביצירות מופת כמו פסלי הפרתנון, "ונוס ממילו", "דוד" ו"פייטה" של מיכאלאנג'לו, "אפולו ודפנה" של ברניני, ועוד רבות. יצירות אלו, המוצגות במוזיאונים החשובים בעולם, אינן רק יופי אסתטי אלא גם עדות לידע, למיומנות וליכולת האנושית לחשוף יופי נסתר בתוך החומר הגולמי.</p>
</div>

<style>
    /* --- General Styling --- */
    .app-container {
        font-family: 'Arial Hebrew', 'Heebo', sans-serif; /* Use Hebrew font with fallback */
        direction: rtl;
        text-align: right;
        margin: 20px auto;
        max-width: 800px; /* Wider container */
        border: 1px solid #d3c6b7; /* Softer border color */
        padding: 30px; /* More padding */
        border-radius: 12px; /* More rounded corners */
        background: linear-gradient(to bottom, #f5f0eb, #e8e3dd); /* Subtle gradient background */
        position: relative;
        overflow: hidden; /* Hide overflow during transitions */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Softer shadow */
    }

    .stage-area {
        min-height: 500px; /* Increased height */
        margin-bottom: 30px;
        position: relative;
        overflow: hidden; /* Ensure stages don't overflow during animation */
    }

    .stage {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start; /* Align content to top */
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: transparent; /* Transparent background */
        padding: 10px;
        opacity: 0; /* Start hidden */
        transition: opacity 0.7s ease-in-out; /* Fade transition */
        pointer-events: none; /* Disable pointer events when hidden */
        text-align: center; /* Center text within stage */
    }

    .stage.active {
        opacity: 1;
        pointer-events: all; /* Enable pointer events when active */
    }

    .stage-title {
        color: #5a4a3c; /* Earthy tone */
        margin-bottom: 15px;
        font-size: 1.8em;
        font-weight: bold;
    }

    .stage-description {
        color: #444;
        margin-bottom: 20px;
        max-width: 90%;
        line-height: 1.6;
        font-size: 1.1em;
    }

    .stage-content {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 30px; /* Increased gap */
        margin-bottom: 25px;
        position: relative;
        width: 100%; /* Use full width */
        flex-grow: 1; /* Allow content to grow */
        padding-bottom: 30px; /* Add space for instruction below */
    }

     .instruction {
        font-style: italic;
        color: #777;
        position: absolute;
        bottom: 5px; /* Position relative to stage-area bottom */
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        font-size: 1em;
         text-align: center;
    }

    .animated-instruction {
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.6; }
        100% { opacity: 1; }
    }

    .interactive-instruction {
         color: #007bff; /* Highlight instructions for interaction */
         font-weight: bold;
    }


    .visual-asset {
         position: relative; /* For positioning elements/overlays inside */
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: flex-end; /* Align image to bottom of its container */
    }

    .asset-image {
        border: 1px solid #c0b4a5;
        border-radius: 8px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.15);
        height: 380px; /* Standard height for main visuals */
        object-fit: contain;
        background-color: #f0ede9; /* Light background */
        transition: transform 0.5s ease; /* Subtle scale transition on hover */
    }

     .asset-image:hover {
        transform: scale(1.02);
     }

    .model .asset-image {
        height: 320px; /* Slightly smaller model */
    }

    .tool-image {
        height: 100px; /* Tool image size */
        width: auto;
        align-self: center;
        border: none;
        box-shadow: none;
        background-color: transparent;
    }

     .tool-icon {
        font-size: 3em;
        position: absolute;
        top: 20px;
        right: 20px;
        opacity: 0.7;
     }


    /* --- Stage 2: Blocking Out Specific Styles --- */
    .stage-2-content .blocked-marble {
        position: relative;
    }

    .stage-2-content .asset-image {
        position: relative;
        z-index: 1; /* Keep image below overlays */
    }

    .block-overlay {
        position: absolute;
        background-color: rgba(100, 80, 60, 0.6); /* Earthy, translucent overlay */
        border: 2px solid #705c4a; /* Darker border */
        cursor: pointer;
        z-index: 2; /* Keep overlay above image */
        transition: opacity 0.3s ease, transform 0.3s ease;
        opacity: 1; /* Start visible */
    }

    .block-overlay:hover {
        opacity: 0.8;
         transform: scale(1.05); /* Hint at clickability */
    }

     .block-overlay.removed {
         opacity: 0;
         pointer-events: none; /* Disable clicks after removal */
     }


    /* Positioning for block overlays - these need careful tuning based on the actual image */
    .blocked-marble { width: 350px; height: 450px; } /* Match image size for positioning */
    .block-1 { top: 30px; left: 15%; width: 100px; height: 80px; border-radius: 5px; }
    .block-2 { top: 160px; left: 45%; transform: translateX(-50%); width: 140px; height: 70px; border-radius: 5px; }
    .block-3 { bottom: 60px; right: 20%; width: 110px; height: 90px; border-radius: 5px; }
    .block-4 { top: 80px; right: 10%; width: 90px; height: 130px; border-radius: 5px; }


    /* --- Stage 3: Pointing Specific Styles --- */
    .stage-3-content {
         gap: 15px;
         align-items: center; /* Align items centered vertically */
    }

    .pointing-model-asset .asset-image {
         cursor: crosshair; /* Indicate clickable area */
         position: relative;
         z-index: 1;
    }

     .pointing-machine .asset-image {
        height: 150px; /* Adjust pointer tool size */
     }


     .clickable-point {
        position: absolute;
        width: 15px;
        height: 15px;
        background-color: rgba(255, 0, 0, 0.8); /* Semi-transparent red */
        border: 2px solid white;
        border-radius: 50%;
        transform: translate(-50%, -50%); /* Center the dot on the exact coordinate */
        cursor: pointer;
        z-index: 10; /* Above model image */
        transition: transform 0.2s ease, background-color 0.2s ease;
     }

     .clickable-point:hover {
         transform: translate(-50%, -50%) scale(1.2);
         background-color: rgba(255, 50, 50, 1);
     }


     .point-indicator {
        position: absolute;
        width: 12px;
        height: 12px;
        background-color: #00aaff; /* Blue for precision */
        border: 2px solid white;
        border-radius: 50%;
        transform: translate(-50%, -50%); /* Center the dot */
        z-index: 15; /* Above everything */
        display: none; /* Start hidden */
     }

     .measurement-line {
        position: absolute;
        background-color: #00aaff; /* Match indicator color */
        height: 3px;
        transform-origin: 0 0; /* Rotate from the start point */
        z-index: 12; /* Below indicators, above images */
        display: none; /* Start hidden */
        animation: draw-line 0.5s ease-out forwards;
     }

     @keyframes draw-line {
         0% { width: 0; }
         100% { width: var(--line-length, 0); } /* Use CSS variable for dynamic length */
     }

     .pointing-marble-asset {
          position: relative; /* Needed for marble-point positioning */
     }


    /* --- Stage 4: Detailing Specific Styles --- */
     .stage-4-content .detailed-marble {
         position: relative;
     }

     .detail-area {
        position: absolute;
        background-color: rgba(150, 110, 80, 0.3); /* Semi-transparent brown */
        border: 2px dashed #705c4a; /* Dashed border to indicate area */
        cursor: pointer;
        z-index: 5; /* Above image */
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        border-radius: 8px;
        transition: background-color 0.3s ease, border-color 0.3s ease;
     }

     .detail-area:hover {
         background-color: rgba(150, 110, 80, 0.6);
         border-color: #5a4a3c;
     }

     .detail-area.detailed {
        background-color: rgba(60, 180, 60, 0.3); /* Greenish tint after detailing */
        border-color: green;
        pointer-events: none; /* Disable clicks after detailing */
     }

      /* Add subtle visual change on detailing */
      .detailed-marble-asset.detailed-face .asset-image { filter: saturate(1.1) contrast(1.05); } /* Example filter */
      .detailed-marble-asset.detailed-drapery .asset-image { filter: brightness(1.05); }
      .detailed-marble-asset.detailed-limb .asset-image { filter: grayscale(0.05); }


     /* --- Stage 5: Finishing Specific Styles --- */
     .stage-5-content .finished-sculpture {
         position: relative;
     }

     .polish-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 5; /* Above image */
        background: radial-gradient(circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255,255,200, 0.4) 0%, rgba(255,255,200, 0) 10%, rgba(0,0,0,0) 100%); /* Shine effect */
        opacity: 0; /* Start hidden */
         transition: opacity 0.1s ease; /* Quick fade for shine */
        pointer-events: none; /* Do not block clicks on image */
     }

    .finished-sculpture-asset.polished .asset-image {
        filter: brightness(1.1) contrast(1.05); /* Subtle filter change */
    }

     .finished-sculpture-asset .asset-image {
         cursor: pointer; /* Indicate clickability */
     }


    /* --- Controls and Explanation --- */
    .controls {
        text-align: center;
        margin-top: 20px;
    }

    .control-button {
        padding: 12px 25px;
        margin: 0 8px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #705c4a; /* Earthy button */
        color: white;
        font-size: 1.1em;
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .control-button:disabled {
        background-color: #c0b4a5; /* Disabled color */
        cursor: not-allowed;
        box-shadow: none;
    }

    .control-button:hover:not(:disabled) {
        background-color: #5a4a3c; /* Darker hover */
        transform: translateY(-1px); /* Subtle lift */
    }
     .control-button:active:not(:disabled) {
        transform: translateY(0); /* Press effect */
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }


    .explanation-toggle-button {
        display: block;
        margin: 30px auto 0; /* Space above */
        padding: 12px 25px;
        cursor: pointer;
        border: 1px solid #c0b4a5;
        border-radius: 6px;
        background-color: #f0ede9; /* Light background */
        font-size: 1.1em;
        color: #5a4a3c;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .explanation-toggle-button:hover {
        background-color: #e8e3dd;
        color: #444;
    }

    .explanation-area {
        margin-top: 30px;
        padding: 25px;
        border: 1px solid #d3c6b7;
        border-radius: 12px;
        background-color: #fff; /* White background for readability */
        text-align: right;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }

    .explanation-area h2, .explanation-area h3 {
        color: #5a4a3c;
        margin-bottom: 12px;
        border-bottom: 1px solid #eee; /* Subtle separator */
        padding-bottom: 5px;
    }

    .explanation-area h3 {
        font-size: 1.3em;
        margin-top: 20px;
    }


    .explanation-area p, .explanation-area ul {
        color: #444;
        line-height: 1.7; /* Increased line height */
        margin-bottom: 15px;
        font-size: 1em;
    }

    .explanation-area ul {
        padding-right: 25px; /* Increased padding */
        list-style-type: disc;
    }

    .explanation-area li {
        margin-bottom: 8px; /* Increased space between list items */
    }

</style>

<script>
    const stages = document.querySelectorAll('.stage');
    const prevBtn = document.getElementById('prev-stage');
    const nextBtn = document.getElementById('next-stage');
    const toggleExplanationBtn = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    let currentStageIndex = 0;
    let stage2BlocksRemoved = 0;
    const totalStage2Blocks = 4; // Hardcoded based on HTML structure

    // Stage 2 specific elements
    const stage2Blocks = document.querySelectorAll('#stage-2 .block-overlay');
    const stage2Instruction = document.getElementById('stage-2-instruction');
    const stage2BlockedMarbleAsset = document.getElementById('blocked-marble'); // Parent of blocks

    // Stage 3 specific elements
    const stage3ClickablePoints = document.querySelectorAll('#stage-3 .clickable-point');
    const modelPoint = document.querySelector('#stage-3 .model-point');
    const marblePoint = document.querySelector('#stage-3 .marble-point');
    const measurementLine = document.querySelector('#stage-3 .measurement-line');
    const pointingModelAsset = document.getElementById('pointing-model-asset'); // Parent of clickable points
    const pointingMarbleAsset = document.getElementById('pointing-marble-asset');
    const stage3Instruction = document.getElementById('stage-3-instruction');

    // Stage 4 specific elements
    const stage4DetailAreas = document.querySelectorAll('#stage-4 .detail-area');
    const stage4DetailedMarbleAsset = document.getElementById('detailed-marble-asset');
    const stage4Instruction = document.getElementById('stage-4-instruction');
    let stage4DetailsCompleted = 0;
    const totalStage4Details = stage4DetailAreas.length;


    // Stage 5 specific elements
    const stage5FinishedSculptureAsset = document.getElementById('finished-sculpture-asset');
    const stage5PolishOverlay = document.querySelector('#stage-5 .polish-overlay');
    const stage5Instruction = document.getElementById('stage-5-instruction');
    let stage5PolishCount = 0; // Simple counter for polishing clicks
    const requiredPolishClicks = 10;


    function showStage(index) {
        stages.forEach((stage, i) => {
            if (i === index) {
                stage.classList.add('active');
            } else {
                stage.classList.remove('active');
            }
        });
        prevBtn.disabled = index === 0;
        nextBtn.disabled = index === stages.length - 1;

        // Reset or initialize interactive elements for the visible stage
        initializeStage(index);
    }

    function initializeStage(index) {
        // Reset all interactive states from other stages
        resetAllStagesInteractivity();

        // Initialize interactivity for the current stage
        if (index === 1) { // Stage 2: Blocking
            stage2BlocksRemoved = 0;
            stage2Blocks.forEach(block => {
                block.classList.remove('removed');
            });
            stage2Instruction.textContent = 'לחצו על האזורים המוצללים באפור כדי להסיר "שיש" ולחשוף את צורת הבסיס!';
            stage2BlockedMarbleAsset.classList.remove('blocked-complete'); // Add class for potential visual change
        } else if (index === 2) { // Stage 3: Pointing
            modelPoint.style.display = 'none';
            marblePoint.style.display = 'none';
            measurementLine.style.display = 'none';
             stage3Instruction.textContent = 'לחצו על אחד מהנקודות האדומות על המודל כדי לראות איך המידה עוברת לשיש!';
             stage3ClickablePoints.forEach(point => point.classList.remove('clicked')); // Reset clicked state
        } else if (index === 3) { // Stage 4: Detailing
             stage4DetailsCompleted = 0;
             stage4DetailAreas.forEach(area => {
                 area.classList.remove('detailed');
             });
             // Reset asset classes for potential visual changes
             stage4DetailedMarbleAsset.classList.remove('detailed-face', 'detailed-drapery', 'detailed-limb');
             stage4Instruction.textContent = 'לחצו על האזורים המסומנים (פנים, בגד, יד/רגל) כדי "לפסל" את הפרטים העדינים!';
        } else if (index === 4) { // Stage 5: Finishing
             stage5PolishCount = 0;
             stage5FinishedSculptureAsset.classList.remove('polished');
             stage5PolishOverlay.style.opacity = 0; // Hide shine overlay
             stage5Instruction.textContent = `לחצו שוב ושוב על הפסל כדי "ללטש" אותו ולגרום לו לזהור! (${stage5PolishCount}/${requiredPolishClicks})`;
        }
         // Note: Stage 1 is passive, no specific initialization needed beyond showing it.
    }

    function resetAllStagesInteractivity() {
         // Hide all specific interactive elements from all stages
         // Stage 2
         stage2Blocks.forEach(block => {
             // Preserve their state, just ensure they don't interfere if stage was left mid-interaction
         });
         // Stage 3
         modelPoint.style.display = 'none';
         marblePoint.style.display = 'none';
         measurementLine.style.display = 'none';
         // Stage 4
         stage4DetailAreas.forEach(area => {
            // Preserve state
         });
         // Stage 5
         stage5PolishOverlay.style.opacity = 0;
    }


    function nextStage() {
        if (currentStageIndex < stages.length - 1) {
            currentStageIndex++;
            showStage(currentStageIndex);
        }
    }

    function prevStage() {
        if (currentStageIndex > 0) {
            currentStageIndex--;
            showStage(currentStageIndex);
        }
    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מעמיק' : 'הצג הסבר מעמיק על הפיסול הקלאסי';
    }

    /* --- Stage 2 Interactivity --- */
    function removeBlock(blockElement) {
        if (blockElement.classList.contains('removed')) return; // Prevent double click

        blockElement.classList.add('removed');
        stage2BlocksRemoved++;

        if (stage2BlocksRemoved >= totalStage2Blocks) {
            stage2Instruction.textContent = 'צורת הבסיס נחשפה! המשיכו לשלב הבא.';
            stage2BlockedMarbleAsset.classList.add('blocked-complete'); // Trigger potential visual change via CSS
            // Optionally enable next button automatically if all interactions are done on a stage
            // nextBtn.disabled = false;
        } else {
             stage2Instruction.textContent = `עוד ${totalStage2Blocks - stage2BlocksRemoved} אזורים להסרה... המשיכו לחצוב!`;
        }
    }

    stage2Blocks.forEach(block => {
        block.addEventListener('click', function() {
            removeBlock(this);
        });
    });

    /* --- Stage 3 Interactivity --- */
     // Pre-calculated or hardcoded point positions relative to the model image
     const modelPointPositions = {
         '1': { top: '20%', left: '40%' }, // Head approx
         '2': { top: '50%', left: '60%' }, // Shoulder approx
         '3': { top: '75%', left: '35%' }  // Knee approx
         // Add more points as needed
     };

     // Simulate corresponding points on the marble image (these would need careful mapping based on actual images)
     // For this simulation, we'll use a simple proportional mapping and offset
     const marblePointMapping = {
         '1': { top: '18%', left: '42%', offsetMultiplier: 1.1 }, // Slightly shifted
         '2': { top: '48%', left: '62%', offsetMultiplier: 1.05 },
         '3': { top: '77%', left: '38%', offsetMultiplier: 0.98 }
     };


    function handlePointingClick(event) {
        const clickedPoint = event.target;
        if (!clickedPoint.classList.contains('clickable-point') || clickedPoint.classList.contains('clicked')) return;

        clickedPoint.classList.add('clicked'); // Mark as clicked

        const pointId = clickedPoint.dataset.point;
        const modelPos = modelPointPositions[pointId];
        const marblePos = marblePointMapping[pointId];

        if (!modelPos || !marblePos) return;

        // Get bounding rectangles for calculations
        const modelRect = pointingModelAsset.querySelector('.asset-image').getBoundingClientRect();
        const marbleRect = pointingMarbleAsset.querySelector('.asset-image').getBoundingClientRect();
        const stageContentRect = document.querySelector('#stage-3 .stage-content').getBoundingClientRect();


        // Position model point indicator
        // Need position relative to the model asset's top-left
        const modelPointX = parseFloat(modelPos.left) / 100 * modelRect.width;
        const modelPointY = parseFloat(modelPos.top) / 100 * modelRect.height;

        modelPoint.style.left = `${modelPointX}px`;
        modelPoint.style.top = `${modelPointY}px`;
        modelPoint.style.display = 'block';


        // Position marble point indicator
         // Need position relative to the marble asset's top-left
        const marblePointX = parseFloat(marblePos.left) / 100 * marbleRect.width;
        const marblePointY = parseFloat(marblePos.top) / 100 * marbleRect.height;

         marblePoint.style.left = `${marblePointX}px`;
         marblePoint.style.top = `${marblePointY}px`;
         marblePoint.style.display = 'block';


         // Position and animate measurement line
         // Line starts at model point, ends at marble point
         const modelPointAbsX = modelRect.left + modelPointX;
         const modelPointAbsY = modelRect.top + modelPointY;

         const marblePointAbsX = marbleRect.left + marblePointX;
         const marblePointAbsY = marbleRect.top + marblePointY;


         const dx = marblePointAbsX - modelPointAbsX;
         const dy = marblePointAbsY - modelPointAbsY;
         const dist = Math.sqrt(dx*dx + dy*dy);
         const ang = Math.atan2(dy, dx); // Angle in radians


         // Position line relative to its container (stage-content)
         measurementLine.style.left = `${modelPointAbsX - stageContentRect.left}px`;
         measurementLine.style.top = `${modelPointAbsY - stageContentRect.top}px`;
         measurementLine.style.width = `${dist}px`; // Set final width
         measurementLine.style.transform = `rotate(${ang}rad)`;
         measurementLine.style.transformOrigin = '0 0';
         measurementLine.style.display = 'block';

         // Set CSS variable for animation
         measurementLine.style.setProperty('--line-length', `${dist}px`);


        stage3Instruction.textContent = 'המידה הועברה! הפסל יודע בדיוק עד לאיזה עומק לחצוב כאן.';

        // Hide indicators and line after animation/delay
         setTimeout(() => {
             modelPoint.style.display = 'none';
             marblePoint.style.display = 'none';
             measurementLine.style.display = 'none';
             // Check if all points clicked
             const remainingPoints = document.querySelectorAll('#stage-3 .clickable-point:not(.clicked)').length;
             if (remainingPoints === 0) {
                 stage3Instruction.textContent = 'כל הנקודות הועברו! מוכנים לשלב הפירוט?';
             } else {
                 stage3Instruction.textContent = 'לחצו על נקודה נוספת על המודל.';
             }
         }, 1500); // Hide indicators after a short time
    }

    // Add event listener to the model asset container and use event delegation
    pointingModelAsset.addEventListener('click', handlePointingClick);


    /* --- Stage 4 Interactivity --- */
    function handleDetailAreaClick(event) {
         const clickedArea = event.target;
         if (!clickedArea.classList.contains('detail-area') || clickedArea.classList.contains('detailed')) return;

         clickedArea.classList.add('detailed');
         stage4DetailsCompleted++;

         const detailType = clickedArea.dataset.detail;
         // Add a class to the marble asset to potentially trigger CSS visual changes
         stage4DetailedMarbleAsset.classList.add(`detailed-${detailType}`);


         if (stage4DetailsCompleted >= totalStage4Details) {
             stage4Instruction.textContent = 'כל הפרטים עובדו! האבן מקבלת חיים!';
         } else {
             stage4Instruction.textContent = `עבדתם על ה-${detailType}! נותרו עוד ${totalStage4Details - stage4DetailsCompleted} אזורים לפירוט.`;
         }
    }

    stage4DetailAreas.forEach(area => {
         area.addEventListener('click', handleDetailAreaClick);
    });


    /* --- Stage 5 Interactivity --- */
     function handlePolishClick(event) {
         const marbleAsset = event.target.closest('.finished-sculpture');
         if (!marbleAsset) return;

         stage5PolishCount++;

         // Update instruction text with progress
         stage5Instruction.textContent = `מלטשים... מלטשים... הפסל הופך חלק ומבריק! (${stage5PolishCount}/${requiredPolishClicks})`;

         // Show a temporary shine effect
         // Get click position relative to the asset image
         const rect = marbleAsset.getBoundingClientRect();
         const x = event.clientX - rect.left; // x position within the element
         const y = event.clientY - rect.top;  // y position within the element

         // Set CSS variables for radial gradient position
         stage5PolishOverlay.style.setProperty('--mouse-x', `${(x / rect.width) * 100}%`);
         stage5PolishOverlay.style.setProperty('--mouse-y', `${(y / rect.height) * 100}%`);
         stage5PolishOverlay.style.opacity = 1; // Show shine

         // Hide shine after a short delay
         setTimeout(() => {
             stage5PolishOverlay.style.opacity = 0;
         }, 150); // Quick flash


         if (stage5PolishCount >= requiredPolishClicks) {
             stage5Instruction.textContent = 'הליטוש הסתיים! יצירת המופת מוכנה!';
             marbleAsset.classList.add('polished'); // Trigger final visual change
             // Optional: Disable further clicking on the marble
             stage5FinishedSculptureAsset.style.pointerEvents = 'none';
         }
     }

     // Add event listener to the marble asset container for clicks
     stage5FinishedSculptureAsset.addEventListener('click', handlePolishClick);


    /* --- General Setup --- */
    // Event Listeners for navigation buttons
    nextBtn.addEventListener('click', nextStage);
    prevBtn.addEventListener('click', prevStage);

    // Event Listener for explanation toggle button
    toggleExplanationBtn.addEventListener('click', toggleExplanation);


    // Initialize the first stage when the page loads
    showStage(currentStageIndex);

</script>
```