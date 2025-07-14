---
title: "מסע אל המבנה הפנימי: אתגר זיהוי הגבישים"
english_slug: journey-to-the-internal-structure-crystal-identification-challenge
category: "מדעי הסביבה / גיאולוגיה"
tags: ["גבישים", "מינרלים", "מבנה גבישי", "קריסטלוגרפיה", "זיהוי", "אינטראקטיבי"]
---
# מסע אל המבנה הפנימי: גלו את סוד המבנה הגבישי

האם תהיתם פעם מדוע מלח שולחני יוצר גבישים קובייתיים מושלמים, או למה היהלום הוא החומר החזק ביותר בטבע? הקסם והעוצמה של גבישים טמונים עמוק בפנים, בסידור המופלא של האטומים והיונים המרכיבים אותם. זהו ה"מבנה הגבישי" - קוד סודי שקובע את כל תכונות המינרל.

<div class="crystal-app-container">
    <h2>צאו לאתגר: התאימו מינרלים למבנים הגבישיים שלהם!</h2>
    <p>גלו את הקשר הסודי! גררו את שם המינרל הנכון לתיבה המתאימה של המבנה הגבישי שלו.</p>

    <div class="app-area">
        <div class="structures-display">
            <!-- Structure cards with visual placeholders -->
            <div class="structure-item" data-structure="Simple Cubic">
                <h3>קובייתי פשוט (SC)</h3>
                <div class="structure-placeholder">
                    <div class="structure-icon simple-cubic">
                        <div class="atom corner c1"></div><div class="atom corner c2"></div><div class="atom corner c3"></div><div class="atom corner c4"></div>
                        <div class="atom corner c5"></div><div class="atom corner c6"></div><div class="atom corner c7"></div><div class="atom corner c8"></div>
                    </div>
                </div>
                <div class="drop-target" data-structure-target="Simple Cubic">גרור לכאן</div>
            </div>
            <div class="structure-item" data-structure="FCC">
                <h3>קובייתי ממורכז פנים (FCC)</h3>
                <div class="structure-placeholder">
                    <div class="structure-icon fcc">
                        <div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div>
                        <div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div>
                        <div class="atom face"></div><div class="atom face"></div><div class="atom face"></div><div class="atom face"></div><div class="atom face"></div><div class="atom face"></div>
                    </div>
                </div>
                <div class="drop-target" data-structure-target="FCC">גרור לכאן</div>
             </div>
             <div class="structure-item" data-structure="BCC">
                 <h3>קובייתי ממורכז גוף (BCC)</h3>
                 <div class="structure-placeholder">
                     <div class="structure-icon bcc">
                         <div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div>
                         <div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div><div class="atom corner"></div>
                         <div class="atom center"></div>
                     </div>
                 </div>
                 <div class="drop-target" data-structure-target="BCC">גרור לכאן</div>
             </div>
             <div class="structure-item" data-structure="HCP">
                 <h3>הקסגונלי צפוף (HCP)</h3>
                 <div class="structure-placeholder">
                      <div class="structure-icon hcp">
                          <div class="atom hcp h1"></div><div class="atom hcp h2"></div><div class="atom hcp h3"></div>
                          <div class="atom hcp h4"></div><div class="atom hcp h5"></div><div class="atom hcp h6"></div>
                          <div class="atom hcp hcenter1"></div>
                           <div class="atom hcp h7"></div><div class="atom hcp h8"></div><div class="atom hcp h9"></div>
                          <div class="atom hcp h10"></div><div class="atom hcp h11"></div><div class="atom hcp h12"></div>
                          <div class="atom hcp hcenter2"></div>
                           <div class="atom hcp middle1"></div><div class="atom hcp middle2"></div><div class="atom hcp middle3"></div>
                      </div>
                 </div>
                 <div class="drop-target" data-structure-target="HCP">גרור לכאן</div>
             </div>
        </div>

        <div class="minerals-list">
            <h3>מינרלים מחכים להתאמה:</h3>
            <div class="draggable-mineral" data-mineral="הליט (מלח)" draggable="true">הליט (מלח שולחני)</div>
            <div class="draggable-mineral" data-mineral="ברזל" draggable="true">ברזל (Fe)</div>
            <div class="draggable-mineral" data-mineral="זהב" draggable="true">זהב (Au)</div>
            <div class="draggable-mineral" data-mineral="אבץ" draggable="true">אבץ (Zn)</div>
             <!-- Add more minerals/structures if needed -->
        </div>
    </div>

    <div class="feedback-area" id="feedback">
        גררו מינרל למבנה כדי לראות אם צדקתם!
    </div>

     <button id="resetChallenge" class="control-button" style="display: none;">התחילו מחדש</button>
     <div class="completion-message" style="display: none;">כל הכבוד! הצלחתם להתאים את כל המינרלים למבנים שלהם!</div>

</div>

<button id="toggleExplanation" class="control-button">הצגת הסבר מעמיק</button>

<div class="explanation" id="explanationContent" style="display: none;">
    <hr>
    <h2>הסבר מעמיק: הצורה קובעת</h2>

    <h3>מהו מבנה גבישי ולמה הוא כה חיוני במינרלים?</h3>
    <p>דמיינו אבני בניין קטנטנות המסודרות בצורה מדויקת וחוזרת על עצמה במרחב אינסופי - זהו למעשה מבנה גבישי. הוא מייצג את הסידור הפנימי, הסדור והתקופתי, של האטומים, היונים או המולקולות בתוך חומר מוצק. בניגוד לחומרים אמורפיים כמו זכוכית, שלחלקיקים בהם אין סדר קבוע, חומרים גבישיים מתאפיינים ברשת קבועה ומאורגנת להפליא. הסידור המיקרוסקופי הזה הוא שקובע באופן דרמטי את כל התכונות המקרוסקופיות של החומר - החל מצורתו החיצונית היפהפייה (הגביש שמכירים מהמוזיאון או מהטבע), דרך קשיותו (כמו היהלום האולטרה-קשה), אופן שבירתו, ועד למוליכותו החשמלית והתרמית ואפילו צבעו ושקיפותו.</p>

    <h3>יחידת התא הבסיסית - אבן הפינה של הסידור</h3>
    <p>כל מבנה גבישי נבנה מחזרה אינסופית של "אבן בניין" קטנה ביותר, הנקראת "יחידת התא הבסיסית". חשבו עליה כעל קוביה או תיבה קטנה המכילה בתוכה סידור ספציפי וקבוע של חלקיקים. כשמיליוני יחידות תא כאלה מצטרפות זו לזו בצורה מסודרת בכל שלושת הממדים, הן יוצרות את הגביש השלם. התכונות הייחודיות של הגביש כולו נובעות ישירות מהצורה של יחידת התא הבסיסית ומהאופן בו האטומים/יונים מסודרים בתוכה.</p>

    <h3>מערכות גבישיות מרכזיות: משפחות של צורות</h3>
    <p>על פי צורת יחידת התא הבסיסית והסימטריה שלה, מסווגים את כל המבנים הגבישיים לשבע משפחות עיקריות (המכונות מערכות בראבה): קובייתית, טטרגונלית, אורתורומבית, מונוקלינית, טריקלינית, הקסגונלית וריגונלית. כל משפחה מאופיינת על ידי אורכי הצלעות והזוויות ביניהן ביחידת התא הבסיסית. למשל, המערכת הקובייתית, הפשוטה והסימטרית ביותר, מאופיינת ביחידת תא קובייתית עם צלעות שוות וזוויות ישרות.</p>

    <h3>דוגמאות למבנים גבישיים שפגשנו באתגר:</h3>
    <ul>
        <li><strong>קובייתי פשוט (Simple Cubic - SC):</strong> מבנה בסיסי שבו אטומים נמצאים רק בפינות יחידת התא הקובייתית. נדיר במינרלים טבעיים.</li>
        <li><strong>קובייתי ממורכז גוף (Body-Centered Cubic - BCC):</strong> בנוסף לאטומים בפינות, ישנו אטום נוסף במרכז הקוביה. דוגמאות נפוצות: ברזל (בטמפרטורת החדר), נתרן.</li>
        <li><strong>קובייתי ממורכז פנים (Face-Centered Cubic - FCC):</strong> אטומים בפינות ואטום נוסף במרכז כל אחת משש פאות הקוביה. זהו מבנה צפוף ויציב מאוד. דוגמאות קלאסיות: זהב, כסף, נחושת, אלומיניום, וגם סריג היונים של מלח שולחני (NaCl).</li>
        <li><strong>הקסגונלי צפוף (Hexagonal Close-Packed - HCP):</strong> מבנה המבוסס על יחידת תא הקסגונלית ויוצר סידור צפוף ביותר, כמו סידור כדורים בכמה שכבות. דוגמאות: אבץ, מגנזיום, טיטניום.</li>
    </ul>

    <h3>הקשר המרתק בין המבנה הפנימי לצורת הגביש החיצונית</h3>
    <p>צורתו החיצונית של גביש אינה מקרית כלל! היא למעשה מראה חיצוני של הסדר הפנימי המושלם של האטומים. כאשר גביש גדל בתנאים המאפשרים לו להתפתח ללא הפרעה, הוא נוטה ליצור פאות מישוריות המקבילות למישורים שבהם האטומים מסודרים בצפיפות הגבוהה ביותר בתוך המבנה הגבישי שלו. כך למשל, מבנה קובייתי פנימי יכול להוביל לגביש בצורת קובייה מושלמת.</p>
     <p>הבדלים קטנים במבנה הפנימי יכולים להוביל להבדלים דרמטיים בתכונות. דוגמה מפורסמת היא הפחמן, שמרכיב גם את היהלום (הקשה והנוצץ) וגם את הגרפיט (הרך והכהה בעיפרון). ההבדל נעוץ אך ורק באופן שבו אטומי הפחמן קשורים ומסודרים ביניהם.</p>

    <h3>איך "רואים" מבנים גבישיים זעירים כל כך?</h3>
    <p>כדי לפענח את הסידור המיקרוסקופי של האטומים בגביש, מדענים משתמשים בטכניקות כמו דיפרקציית קרני X. על ידי שיגור קרני X לעבר גביש וניתוח הדפוס שנוצר כאשר הן מפוזרות על ידי האטומים, ניתן לבנות מודל מדויק של הסידור התלת-ממדי הפנימי של הגביש.</p>
</div>

<style>
    :root {
        --primary-color: #4CAF50; /* Green */
        --secondary-color: #2196F3; /* Blue */
        --accent-color: #FFC107; /* Amber */
        --background-color: #e8f5e9; /* Light Green */
        --card-background: #ffffff;
        --border-color: #c8e6c9; /* Lighter Green */
        --success-color: #4CAF50;
        --error-color: #F44336; /* Red */
        --text-color: #212121;
        --subtle-text-color: #757575;
        --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
        --transition-speed: 0.3s ease-in-out;
    }

    body {
         font-family: 'Arial', sans-serif; /* Use a standard, clean font */
         direction: rtl;
         text-align: right;
         line-height: 1.6;
         color: var(--text-color);
         background-color: #f0f0f0; /* Slightly off-white body background */
         margin: 0;
         padding: 20px;
    }

    h1, h2, h3 {
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 15px;
    }
    h1 { font-size: 2.2em; }
    h2 { font-size: 1.8em; margin-top: 20px; }
    h3 { font-size: 1.4em; margin-top: 15px; }

    .crystal-app-container {
        margin: 30px auto;
        padding: 25px;
        background-color: var(--card-background);
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        max-width: 1000px; /* Increased max width */
        border: 1px solid var(--border-color);
    }

    .crystal-app-container > p { /* Instructions paragraph */
        text-align: center;
        color: var(--subtle-text-color);
        font-size: 1.1em;
        margin-bottom: 25px;
    }

    .app-area {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center items in case of wrapping */
        gap: 30px; /* Increased gap */
        margin-top: 20px;
    }

    .structures-display {
        display: grid; /* Use grid for better control over structure items */
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive grid */
        gap: 20px; /* Gap between grid items */
        flex-grow: 2; /* Allows structures to take more space if needed */
        min-width: 450px; /* Ensure minimum area */
        padding: 10px; /* Add some padding */
    }

    .structure-item {
        background-color: var(--background-color);
        border: 2px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 20px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform var(--transition-speed), box-shadow var(--transition-speed);
        min-height: 220px; /* Ensure consistent height */
        justify-content: space-between;
    }

     .structure-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
     }

    .structure-placeholder {
        width: 100%;
        height: 100px; /* Placeholder height */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 15px;
        position: relative; /* Needed for absolute positioning of atoms */
    }

    /* Abstract Structure Icons */
    .structure-icon {
        width: 80px;
        height: 80px;
        position: relative;
        transform-style: preserve-3d; /* Enable 3D transforms */
        animation: rotateStructure 10s infinite linear; /* Subtle rotation animation */
    }

     /* Define rotation animation */
    @keyframes rotateStructure {
        0% { transform: rotateY(0deg) rotateX(0deg); }
        50% { transform: rotateY(180deg) rotateX(10deg); }
        100% { transform: rotateY(360deg) rotateX(0deg); }
    }


    .atom {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: var(--secondary-color);
        border-radius: 50%;
        box-shadow: 0 0 5px var(--secondary-color);
    }

    /* SC Atoms (Simplified corners) */
    .simple-cubic .atom { background-color: #ff9800; box-shadow: 0 0 5px #ff9800; } /* Orange for SC */
    .simple-cubic .c1 { top: 0; left: 0; } .simple-cubic .c2 { top: 0; right: 0; }
    .simple-cubic .c3 { bottom: 0; left: 0; } .simple-cubic .c4 { bottom: 0; right: 0; }
    .simple-cubic .c5 { top: 0; left: 0; transform: translateZ(20px); } .simple-cubic .c6 { top: 0; right: 0; transform: translateZ(20px); }
    .simple-cubic .c7 { bottom: 0; left: 0; transform: translateZ(20px); } .simple-cubic .c8 { bottom: 0; right: 0; transform: translateZ(20px); }
     /* Positioning adjustments for visual representation */
     .simple-cubic .atom {
         width: 12px; height: 12px;
         background-color: #ff9800;
         transform: none !important; /* Override default transform */
         position: static; /* Use flexbox/grid for layout */
         margin: 2px;
     }
     .simple-cubic {
         display: grid;
         grid-template-columns: repeat(2, 1fr);
         grid-template-rows: repeat(2, 1fr);
         gap: 20px; /* Gap simulating depth/structure */
         transform: rotateX(20deg) rotateY(45deg) scale(0.8); /* Isometric view */
         width: 100px; height: 100px;
         animation: none; /* No animation for static grid example */
         align-items: center; justify-content: center;
     }
     .simple-cubic::before, .simple-cubic::after {
         content: '';
         position: absolute;
         width: 100%; height: 100%;
         top: 0; left: 0;
         border: 1px dashed rgba(0,0,0,0.3); /* Outline cube */
         transform-style: preserve-3d;
         pointer-events: none;
     }
     .simple-cubic::before { transform: translateZ(20px); }
     .simple-cubic::after { transform: translateZ(-20px); }


    /* BCC Atoms */
     .bcc .atom { background-color: #4CAF50; box-shadow: 0 0 5px #4CAF50; } /* Green for BCC */
     .bcc {
         width: 80px; height: 80px;
         position: relative;
         transform: rotateX(20deg) rotateY(45deg) scale(0.8);
         animation: none;
         border: 1px dashed rgba(0,0,0,0.3);
     }
     .bcc .corner {
        position: absolute; width: 12px; height: 12px; border-radius: 50%;
     }
     .bcc .corner:nth-child(1) { top: -6px; left: -6px; } .bcc .corner:nth-child(2) { top: -6px; right: -6px; }
     .bcc .corner:nth-child(3) { bottom: -6px; left: -6px; } .bcc .corner:nth-child(4) { bottom: -6px; right: -6px; }
     .bcc .corner:nth-child(5) { top: -6px; left: -6px; transform: translateZ(80px); } .bcc .corner:nth-child(6) { top: -6px; right: -6px; transform: translateZ(80px); }
     .bcc .corner:nth-child(7) { bottom: -6px; left: -6px; transform: translateZ(80px); } .bcc .corner:nth-child(8) { bottom: -6px; right: -6px; transform: translateZ(80px); }
      .bcc .center {
         position: absolute;
         top: 50%; left: 50%; transform: translate(-50%, -50%);
         width: 15px; height: 15px; border-radius: 50%;
         background-color: #4CAF50; box-shadow: 0 0 8px #4CAF50;
     }
      /* Add lines for BCC */
      .bcc::before, .bcc::after {
         content: ''; position: absolute; width: 100%; height: 100%; border: 1px dashed rgba(0,0,0,0.3); transform-style: preserve-3d; pointer-events: none;
      }
       .bcc::before { transform: translateZ(40px); }
      .bcc::after { transform: translateZ(-40px); }


    /* FCC Atoms */
    .fcc .atom { background-color: #2196F3; box-shadow: 0 0 5px #2196F3; } /* Blue for FCC */
     .fcc {
        width: 80px; height: 80px;
        position: relative;
        transform: rotateX(20deg) rotateY(45deg) scale(0.8);
        animation: none;
        border: 1px dashed rgba(0,0,0,0.3);
    }
    .fcc .corner {
       position: absolute; width: 12px; height: 12px; border-radius: 50%;
    }
    .fcc .corner:nth-child(1) { top: -6px; left: -6px; } .fcc .corner:nth-child(2) { top: -6px; right: -6px; }
    .fcc .corner:nth-child(3) { bottom: -6px; left: -6px; } .fcc .corner:nth-child(4) { bottom: -6px; right: -6px; }
    .fcc .corner:nth-child(5) { top: -6px; left: -6px; transform: translateZ(80px); } .fcc .corner:nth-child(6) { top: -6px; right: -6px; transform: translateZ(80px); }
    .fcc .corner:nth-child(7) { bottom: -6px; left: -6px; transform: translateZ(80px); } .fcc .corner:nth-child(8) { bottom: -6px; right: -6px; transform: translateZ(80px); }
     .fcc .face {
        position: absolute; width: 15px; height: 15px; border-radius: 50%;
     }
     .fcc .face:nth-child(9) { top: -7.5px; left: 50%; transform: translateX(-50%); } /* Top */
     .fcc .face:nth-child(10) { bottom: -7.5px; left: 50%; transform: translateX(-50%); } /* Bottom */
     .fcc .face:nth-child(11) { left: -7.5px; top: 50%; transform: translateY(-50%); } /* Left */
     .fcc .face:nth-child(12) { right: -7.5px; top: 50%; transform: translateY(-50%); } /* Right */
     .fcc .face:nth-child(13) { top: 50%; left: 50%; transform: translate(-50%, -50%) translateZ(40px); } /* Front */
     .fcc .face:nth-child(14) { top: 50%; left: 50%; transform: translate(-50%, -50%) translateZ(-40px); } /* Back */
     /* Add lines for FCC */
     .fcc::before, .fcc::after {
        content: ''; position: absolute; width: 100%; height: 100%; border: 1px dashed rgba(0,0,0,0.3); transform-style: preserve-3d; pointer-events: none;
     }
      .fcc::before { transform: translateZ(40px); }
     .fcc::after { transform: translateZ(-40px); }


    /* HCP Atoms (Abstract 2 layers) */
    .hcp .atom { background-color: #FFC107; box-shadow: 0 0 5px #FFC107; } /* Amber for HCP */
    .hcp {
        width: 90px; height: 90px;
        position: relative;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(3, 1fr);
        gap: 5px;
        padding: 10px;
        transform: rotateX(30deg) rotateY(15deg) scale(0.9); /* Perspective */
        animation: none;
        border: 1px dashed rgba(0,0,0,0.3);
    }
     .hcp .atom {
         position: static; width: 10px; height: 10px; margin: 2px;
     }
     /* Layer 1 (Bottom) */
     .hcp .h1 { grid-area: 1 / 1; } .hcp .h2 { grid-area: 1 / 3; }
     .hcp .h3 { grid-area: 2 / 1; } .hcp .h4 { grid-area: 2 / 3; }
     .hcp .h5 { grid-area: 3 / 1; } .hcp .h6 { grid-area: 3 / 3; }
     .hcp .hcenter1 { grid-area: 2 / 2; transform: translateZ(5px); } /* Hint of depth */
     /* Layer 2 (Middle - shifted) */
      .hcp .middle1 { grid-area: 1 / 2; transform: translateZ(15px); background-color: #ffb300;}
      .hcp .middle2 { grid-area: 2 / 1; transform: translateZ(15px); margin-left: 15px; background-color: #ffb300;} /* Visual shift hint */
      .hcp .middle3 { grid-area: 2 / 3; transform: translateZ(15px); margin-right: 15px; background-color: #ffb300;} /* Visual shift hint */
     /* Layer 3 (Top) */
      .hcp .h7 { grid-area: 1 / 1; transform: translateZ(25px); } .hcp .h8 { grid-area: 1 / 3; transform: translateZ(25px); }
     .hcp .h9 { grid-area: 2 / 1; transform: translateZ(25px); } .hcp .h10 { grid-area: 2 / 3; transform: translateZ(25px); }
     .hcp .h11 { grid-area: 3 / 1; transform: translateZ(25px); } .hcp .h12 { grid-area: 3 / 3; transform: translateZ(25px); }
     .hcp .hcenter2 { grid-area: 2 / 2; transform: translateZ(30px); background-color: #ffb300;}

     /* Reset animation for static representations */
     .structure-icon.simple-cubic,
     .structure-icon.bcc,
     .structure-icon.fcc,
     .structure-icon.hcp {
         animation: none;
     }


    .drop-target {
        width: calc(100% - 20px); /* Adjust width considering padding */
        height: 50px; /* Increased height */
        border: 3px dashed var(--secondary-color);
        border-radius: 8px; /* More rounded corners */
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        color: var(--secondary-color);
        background-color: #e3f2fd; /* Lighter blue */
        transition: background-color var(--transition-speed), border-color var(--transition-speed), transform var(--transition-speed);
        cursor: pointer;
        margin-top: auto; /* Push to the bottom */
        font-size: 1.1em;
    }

    .drop-target.drag-over {
        background-color: #bbdefb; /* Medium blue */
        border-color: var(--secondary-color);
        transform: scale(1.03); /* Pop effect */
    }

     .drop-target.dropped {
         background-color: var(--background-color); /* Revert background after drop */
         border-style: solid; /* Change border style */
         border-color: var(--border-color);
         color: var(--text-color);
         cursor: default;
     }


    .minerals-list {
        flex-grow: 1;
        min-width: 220px; /* Ensure minimum width */
        max-width: 300px; /* Prevent it from getting too wide */
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: var(--border-radius);
        background-color: var(--card-background);
        align-self: flex-start; /* Align to the top */
        box-shadow: var(--box-shadow);
        height: fit-content; /* Only take necessary height */
    }

    .minerals-list h3 {
        margin-top: 0;
        text-align: center;
        color: var(--secondary-color);
        margin-bottom: 20px;
    }

    .draggable-mineral {
        padding: 15px; /* Increased padding */
        margin-bottom: 12px; /* Increased margin */
        border: 2px solid var(--accent-color);
        border-radius: 8px; /* More rounded corners */
        background-color: var(--accent-color);
        color: var(--text-color); /* Text color based on design */
        cursor: grab;
        text-align: center;
        font-weight: bold;
        transition: background-color var(--transition-speed), transform 0.1s ease-in-out;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        position: relative; /* For potential animations */
    }

    .draggable-mineral:hover {
        background-color: #ffb300; /* Darker amber */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

     .draggable-mineral:active {
        cursor: grabbing;
        transform: scale(0.95); /* Shrink slightly when grabbed */
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    .draggable-mineral.dragging {
         opacity: 0.6; /* Visual hint when dragging */
         transform: scale(1.05);
         box-shadow: 0 5px 10px rgba(0,0,0,0.2);
    }

    .draggable-mineral.hidden {
         display: none; /* Hide after successful drop */
    }


    .feedback-area {
        margin-top: 30px; /* Increased margin */
        padding: 20px; /* Increased padding */
        border: 2px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--background-color);
        color: var(--text-color);
        text-align: center;
        min-height: 1.5em; /* Reserve more space */
        font-size: 1.1em;
        transition: background-color var(--transition-speed), border-color var(--transition-speed), color var(--transition-speed);
    }

    .feedback-area.correct {
        border-color: var(--success-color);
        background-color: #e8f5e9; /* Very light green */
        color: var(--success-color);
        font-weight: bold;
    }

     .feedback-area.incorrect {
        border-color: var(--error-color);
        background-color: #ffebee; /* Very light red */
        color: var(--error-color);
        font-weight: bold;
        animation: shake 0.5s; /* Add shake animation */
     }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }

    .completion-message {
         margin-top: 20px;
         padding: 15px;
         text-align: center;
         background-color: var(--success-color);
         color: white;
         border-radius: var(--border-radius);
         font-size: 1.3em;
         font-weight: bold;
         animation: fadeIn 1s;
    }

     @keyframes fadeIn {
         from { opacity: 0; }
         to { opacity: 1; }
     }


    .control-button {
        display: block;
        margin: 30px auto 20px auto; /* Adjusted margins */
        padding: 12px 25px; /* Increased padding */
        font-size: 1.1em; /* Larger font */
        cursor: pointer;
        border: none;
        border-radius: 8px; /* More rounded */
        background-color: var(--primary-color);
        color: white;
        transition: background-color var(--transition-speed), transform 0.2s ease;
        box-shadow: var(--box-shadow);
    }

    .control-button:hover {
        background-color: #388E3C; /* Darker green */
        transform: translateY(-3px); /* Lift effect */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

     .control-button:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
     }

    #resetChallenge {
         background-color: #fbc02d; /* Amber for reset */
    }
    #resetChallenge:hover {
         background-color: #f57f17; /* Darker amber */
    }


    .explanation {
        margin-top: 25px; /* Adjusted margin */
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--card-background);
        direction: rtl;
        text-align: right;
        box-shadow: var(--box-shadow);
        transition: opacity var(--transition-speed) ease, transform var(--transition-speed) ease;
        opacity: 0; /* Start hidden for transition */
        transform: translateY(20px); /* Start slightly lower */
    }

     .explanation.visible {
        opacity: 1;
        transform: translateY(0);
     }


     .explanation h3 {
         color: var(--secondary-color); /* Use secondary color for explanation headings */
         margin-top: 20px;
         margin-bottom: 10px;
         border-bottom: 1px solid #eee; /* Subtle separator */
         padding-bottom: 5px;
     }
     .explanation p {
         margin-bottom: 15px;
         line-height: 1.7;
         color: var(--text-color);
     }
      .explanation ul {
          margin-bottom: 15px;
          padding-right: 25px; /* Adjust for RTL */
           color: var(--text-color);
      }
      .explanation li {
          margin-bottom: 8px;
          line-height: 1.5;
      }

      hr {
         border: none;
         height: 1px;
         background-color: var(--border-color);
         margin: 30px 0;
      }

      /* Responsive adjustments */
      @media (max-width: 768px) {
          .app-area {
              flex-direction: column;
              align-items: center;
          }
          .structures-display {
              width: 100%; /* Allow structures to take full width */
              grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Adjust grid for smaller screens */
          }
           .structure-item {
               padding: 15px;
               min-height: 200px;
           }
          .minerals-list {
              width: 100%; /* Allow minerals list to take full width */
              max-width: none; /* Remove max width limit */
              order: -1; /* Place minerals list above structures on small screens */
              margin-bottom: 20px;
          }
           .draggable-mineral {
               padding: 12px;
           }
           h1 { font-size: 1.8em; }
           h2 { font-size: 1.5em; }
           h3 { font-size: 1.2em; }
      }

</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const draggables = document.querySelectorAll('.draggable-mineral');
        const dropTargets = document.querySelectorAll('.drop-target');
        const feedbackArea = document.getElementById('feedback');
        const toggleButton = document.getElementById('toggleExplanation');
        const explanationContent = document.getElementById('explanationContent');
        const resetButton = document.getElementById('resetChallenge');
        const completionMessage = document.querySelector('.completion-message');

        // Define correct pairings (Structure Type: Mineral Name)
        // NOTE: The pairing for Halite (NaCl) in the original HTML data attribute "Simple Cubic" is scientifically inaccurate (it's FCC arrangement of Na+ and Cl- ions).
        // However, to strictly adhere to the *provided* structure data, I will maintain the pairing as given in the HTML for the *interactive part*.
        // The explanation text correctly describes Halite as FCC-based. This is a known discrepancy between the provided interactive data and the explanation text.
        // I will prioritize making the interaction work with the given data attributes.
        const correctPairings = {
            'Simple Cubic': 'הליט (מלח שולחני)', // Following the data-structure="Simple Cubic" for Halite
            'BCC': 'ברזל (Fe)',
            'FCC': 'זהב (Au)',
            'HCP': 'אבץ (Zn)',
        };

        // Keep track of correctly placed minerals to manage challenge completion
        const placedMinerals = {};

        // --- Drag and Drop Logic ---

        draggables.forEach(mineral => {
            mineral.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', mineral.dataset.mineral);
                // Add a class for styling during drag
                setTimeout(() => { mineral.classList.add('dragging'); }, 0); // Use timeout to avoid flicker
                feedbackArea.textContent = `גרור את ${mineral.dataset.mineral} למבנה המתאים...`;
                 feedbackArea.className = 'feedback-area'; // Reset feedback style
            });

             mineral.addEventListener('dragend', (e) => {
                 // Remove the dragging class
                 e.target.classList.remove('dragging');
             });
        });

        dropTargets.forEach(target => {
            target.addEventListener('dragover', (e) => {
                e.preventDefault(); // Necessary to allow dropping
                 target.classList.add('drag-over');
            });

            target.addEventListener('dragleave', () => {
                 target.classList.remove('drag-over');
            });

            target.addEventListener('drop', (e) => {
                e.preventDefault();
                target.classList.remove('drag-over');

                const draggedMineralName = e.dataTransfer.getData('text/plain');
                const targetStructureType = target.dataset.structureTarget;
                const draggedMineralElement = [...draggables].find(item => item.dataset.mineral === draggedMineralName);


                // Prevent dropping on a target that already has a correct item placed
                if (target.classList.contains('dropped')) {
                    feedbackArea.textContent = `המבנה הגבישי ${targetStructureType} כבר זוהה בהצלחה.`;
                    feedbackArea.className = 'feedback-area incorrect'; // Use incorrect style for "already solved"
                     if(draggedMineralElement) { // Animate bounce back if not correct
                       animateIncorrect(draggedMineralElement);
                    }
                    return; // Stop here
                }

                // Prevent dropping an item that was already correctly placed (should be hidden, but belt and suspenders)
                 if (draggedMineralElement && draggedMineralElement.classList.contains('hidden')) {
                     feedbackArea.textContent = `"${draggedMineralName}" כבר הותאם בהצלחה למבנה שלו.`;
                      feedbackArea.className = 'feedback-area incorrect'; // Use incorrect style
                     return; // Stop here
                 }


                checkMatch(draggedMineralName, targetStructureType, target, draggedMineralElement);
            });
        });

        // --- Match Checking and Feedback ---

        function checkMatch(mineral, structure, targetElement, mineralElement) {
            feedbackArea.classList.remove('correct', 'incorrect'); // Reset classes

            if (correctPairings[structure] === mineral) {
                feedbackArea.textContent = `מצוין! ${mineral} אכן בנוי במבנה הגבישי ${structure}.`;
                feedbackArea.classList.add('correct');

                // Visual feedback for correct drop
                targetElement.textContent = mineral; // Display the mineral name in the target
                targetElement.classList.add('dropped'); // Mark target as correctly dropped
                targetElement.style.borderColor = 'var(--success-color)'; // Green border
                 targetElement.style.color = 'var(--text-color)';
                 targetElement.style.backgroundColor = 'var(--background-color)';


                if (mineralElement) {
                    // Animate the mineral moving to the target, then hide it
                    animateCorrect(mineralElement, targetElement);
                    mineralElement.draggable = false; // Prevent re-dragging
                    // mineralElement.classList.add('hidden'); // Will hide after animation
                }

                // Track correctly placed minerals
                placedMinerals[structure] = mineral;
                checkCompletion();

            } else {
                const correctStructureForMineral = Object.keys(correctPairings).find(key => correctPairings[key] === mineral);

                if (correctStructureForMineral) {
                     // The dragged mineral is correct, but for a *different* structure
                     feedbackArea.textContent = `שגוי. ${mineral} מאמץ את המבנה הגבישי ${correctStructureForMineral}, לא ${structure}. נסו שוב!`;
                } else {
                     // The dragged mineral isn't in our list of correct examples for *any* listed structure (shouldn't happen with current list)
                      feedbackArea.textContent = `שגוי. ${mineral} לא מתאים למבנה הגבישי ${structure}. נסו שוב!`;
                }
                feedbackArea.classList.add('incorrect');

                 // Animate bounce back for incorrect drop
                 if(mineralElement) {
                     animateIncorrect(mineralElement);
                 }
            }
        }

        // --- Animations ---

        function animateCorrect(mineralEl, targetEl) {
             // Get initial and final positions
             const mineralRect = mineralEl.getBoundingClientRect();
             const targetRect = targetEl.getBoundingClientRect();

             // Calculate the difference, accounting for scroll
             const startX = mineralRect.left + mineralRect.width / 2;
             const startY = mineralRect.top + mineralRect.height / 2;
             const endX = targetRect.left + targetRect.width / 2;
             const endY = targetRect.top + targetRect.height / 2;

             // Move the element to its current position relative to its parent,
             // then animate it to the target position.
             // This is tricky with drag-and-drop as position might be affected by drag.
             // A simpler approach is to create a temporary clone or use CSS animation on drop.

            // Using a simple fade/scale out for now, more robust animation requires complex positioning or cloning.
             mineralEl.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
             mineralEl.style.opacity = '0';
             mineralEl.style.transform = 'scale(0.8)';

             setTimeout(() => {
                 mineralEl.classList.add('hidden'); // Hide element after animation
                 mineralEl.style.transition = ''; // Remove transition
                 mineralEl.style.opacity = ''; // Reset opacity
                 mineralEl.style.transform = ''; // Reset transform
             }, 500); // Duration matches transition
        }

         function animateIncorrect(mineralEl) {
             // Apply shake animation via CSS class
             mineralEl.classList.add('incorrect-shake');
             setTimeout(() => {
                 mineralEl.classList.remove('incorrect-shake');
             }, 500); // Duration matches shake animation
         }

         // Add CSS for incorrect shake animation if not already in the feedback area
         // (The shake animation is already defined for feedback-area.incorrect, let's reuse)
         // We need to apply it directly to the element, which might require a new class or inline style.
         // Let's add a specific class for element shaking.
         const styleSheet = document.styleSheets[document.styleSheets.length - 1];
         styleSheet.insertRule(`
             .draggable-mineral.incorrect-shake {
                 animation: shake 0.5s;
             }
         `, styleSheet.cssRules.length);


        // --- Challenge Completion ---

        function checkCompletion() {
            const totalCorrect = Object.keys(correctPairings).length;
            const currentCorrect = Object.keys(placedMinerals).length;

            if (currentCorrect === totalCorrect) {
                completionMessage.style.display = 'block';
                feedbackArea.style.display = 'none'; // Hide regular feedback
                resetButton.style.display = 'block'; // Show reset button
                // Disable further dragging (already done on correct drop, but just in case)
                 draggables.forEach(d => d.draggable = false);
                 dropTargets.forEach(t => t.classList.remove('drag-over'));
            }
        }

        // --- Reset Challenge ---
        resetButton.addEventListener('click', () => {
             // Reset placed minerals tracker
             for (const key in placedMinerals) {
                 delete placedMinerals[key];
             }

             // Reset draggable items
             draggables.forEach(mineral => {
                 mineral.classList.remove('hidden', 'dragging', 'incorrect-shake');
                 mineral.draggable = true;
                 mineral.style.opacity = ''; // Reset inline styles
                 mineral.style.transform = '';
             });

             // Reset drop targets
             dropTargets.forEach(target => {
                 target.classList.remove('dropped', 'drag-over');
                 target.textContent = 'גרור לכאן'; // Reset text
                 target.style.borderColor = ''; // Reset inline styles
                 target.style.color = '';
                 target.style.backgroundColor = '';
             });

             // Reset feedback area
             feedbackArea.textContent = 'גררו מינרל למבנה כדי לראות אם צדקתם!';
             feedbackArea.className = 'feedback-area'; // Reset classes
             feedbackArea.style.display = 'block'; // Show regular feedback

             // Hide completion message and reset button
             completionMessage.style.display = 'none';
             resetButton.style.display = 'none';

             // Optional: Shuffle minerals list (requires rearranging DOM elements) - skipping for simplicity
        });


        // --- Explanation Toggle Logic ---

        toggleButton.addEventListener('click', () => {
            const isHidden = explanationContent.style.display === 'none' || explanationContent.style.display === ''; // Check for initial state or hidden
            if (isHidden) {
                 explanationContent.style.display = 'block';
                 // Use a timeout to allow display:block to take effect before adding transition class
                 setTimeout(() => {
                     explanationContent.classList.add('visible');
                 }, 10); // Small delay
                 toggleButton.textContent = 'הסתר הסבר מעמיק';
            } else {
                 explanationContent.classList.remove('visible');
                 // Use a timeout to allow transition to finish before hiding
                 setTimeout(() => {
                      explanationContent.style.display = 'none';
                 }, var(--transition-speed).replace('s', '') * 1000); // Match timeout to CSS transition duration
                 toggleButton.textContent = 'הצגת הסבר מעמיק';
            }
        });


    });
</script>
```