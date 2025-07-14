---
title: "קפצתי מהמסך: מסע לכידת תנועה באנימציה"
english_slug: leaping-off-the-screen-motion-capture-in-animation
category: "אמנות דיגיטלית"
tags:
- לכידת תנועה
- אנימציה תלת-ממדית
- Motion Capture
- VFX
- יצירת תוכן דיגיטלי
---
<h1>קפצתי מהמסך: מסע לכידת תנועה באנימציה</h1>
<p>דמיינו שהדמויות האהובות עליכם על המסך נעות בדיוק כמו שחקן אמיתי. איך קורה הקסם הזה, שבו תנועה פיזית הופכת לאנימציה וירטואלית מרהיבה? הצטרפו למסע אל ליבת הטכנולוגיה שהביאה את הדמויות לחיים ריאליסטיים מתמיד, צעד אחר צעד בסימולציה שלנו.</p>

<div id="mocap-simulation-container">
    <div id="simulation-area">
        <div id="stage-preparation" class="simulation-stage active">
            <h2>מכינים את הבמה: מתחפשים ומכיילים</h2>
            <p>הכל מתחיל כאן! השחקן לובש חליפת MoCap מיוחדת עם סמנים מחזירי אור. מצלמות אינפרא-אדום פרוסות באולפן וממתינות. המערכת מכיילת את מיקום הסמנים במרחב התלת-ממדי ומקשרת אותם לשלד הדיגיטלי. המצלמות "מזהות" את הסמנים ומוכנות לעקוב אחריהם.</p>
            <div class="studio">
                <div class="floor"></div>
                <div class="camera camera-1"></div>
                <div class="camera camera-2"></div>
                <div class="camera camera-3"></div>
                <div class="actor-mocap">
                     <div class="mocap-marker head"></div>
                     <div class="mocap-marker torso"></div>
                     <div class="mocap-marker hand-l"></div>
                     <div class="mocap-marker hand-r"></div>
                     <div class="mocap-marker leg-l"></div>
                     <div class="mocap-marker leg-r"></div>
                </div>
                <!-- Visual indicators for calibration -->
                <div class="calibration-beam beam-1"></div>
                <div class="calibration-beam beam-2"></div>
                <div class="calibration-beam beam-3"></div>
            </div>
            <button class="next-stage-button interactive-button">הכנה הושלמה! בואו נתחיל לזוז</button>
        </div>

        <div id="stage-performance" class="simulation-stage">
            <h2>קדימה אקשן! לוכדים את התנועה</h2>
            <p>השחקן מבצע את התנועה! המצלמות יחד עוקבות בדיוק שיא אחר כל סמן וסמן בחליפה, ב מאות פריימים בשנייה. הנתונים נרשמים בזמן אמת ומתורגמים לסדרה של נקודות תלת-ממדיות שעוקבות אחר מסלול התנועה במרחב.</p>
            <div class="studio">
                <div class="floor"></div>
                 <div class="camera camera-1 active"></div>
                <div class="camera camera-2 active"></div>
                <div class="camera camera-3 active"></div>
                 <div class="actor-mocap">
                     <div class="mocap-marker head"></div>
                     <div class="mocap-marker torso"></div>
                     <div class="mocap-marker hand-l"></div>
                     <div class="mocap-marker hand-r"></div>
                     <div class="mocap-marker leg-l"></div>
                     <div class="mocap-marker leg-r"></div>
                 </div>
                <div class="marker-tracking-path"></div> <!-- Element to draw the path -->
                <div class="virtual-skeleton"></div> <!-- Visual placeholder for skeleton concept -->
            </div>
             <button class="next-stage-button interactive-button">ביצוע הושלם. הנתונים נאספו!</button>
        </div>

        <div id="stage-data-processing" class="simulation-stage">
            <h2>מנקים את הקסם: עיבוד וליטוש הנתונים</h2>
            <p>הנתונים הגולמיים מהלכידה מלאים ב"רעש" טכני ואי-דיוקים. בשלב זה, טכנאים מתמחים משתמשים בתוכנות מיוחדות כדי לנקות, להחליק ולתקן את מסלולי הסמנים. תראו איך הגרף ה"רועש" הופך לחלק ונקי.</p>
            <div class="data-display">
                <div class="graph raw-data">
                    <h4>נתונים גולמיים</h4>
                     <div class="graph-line raw"></div>
                </div>
                <div class="processing-indicator"></div> <!-- Visual element for processing -->
                <div class="graph processed-data">
                     <h4>נתונים מעובדים</h4>
                    <div class="graph-line processed"></div>
                </div>
            </div>
             <button id="process-data-button" class="interactive-button">לחצו לעיבוד וניקוי נתונים</button>
             <button class="next-stage-button interactive-button" disabled>נתונים עובדו! עוברים לאנימציה</button>
        </div>

        <div id="stage-application" class="simulation-stage">
            <h2>דמות חדשה נולדת: מחברים את התנועה</h2>
            <p>עכשיו, נתוני התנועה הנקיים מוכנים. הם מוחלים על השלד הדיגיטלי של הדמות התלת-ממדית שתיצרו. כל תנועה של הסמן המקורי מניעה את החלק המקביל בשלד הדיגיטלי, והדמות קמה לתחייה וזזה כאילו היא בעולם האמיתי!</p>
            <div class="character-area">
                <div class="character-rig"></div> <!-- Placeholder for rig concept -->
                <div class="animated-character"></div>
                 <div class="data-flow-effect"></div> <!-- Visualizing data flow -->
            </div>
            <button class="reset-simulation-button interactive-button">התחילו מסע חדש</button>
        </div>
    </div>

    <div id="simulation-controls">
        <!-- Buttons are inside stages now -->
    </div>
    <div id="simulation-status"></div>
</div>

<button id="toggle-explanation" class="interactive-button">הצג/הסתר הצצה אל מאחורי הקלעים (הסבר מורחב)</button>

<div id="explanation-section" style="display: none;">
    <h2>הצצה אל מאחורי הקלעים: לכידת תנועה (Motion Capture)</h2>
    <p><strong>מהי לכידת תנועה (MoCap) ואיך היא מפיחה חיים בדמויות?</strong></p>
    <p>לכידת תנועה היא גשר מופלא בין העולם הפיזי לדיגיטלי. היא מאפשרת לנו "להקליט" תנועות של שחקנים אמיתיים (או אובייקטים אחרים) ולהשתמש בנתונים כדי לגרום לדמויות וירטואליות לזוז באופן טבעי ואמין. במקום שאנימטור ייצור כל תנועה ידנית, ה-MoCap מאפשרת להעביר את הניואנסים העדינים של תנועה אנושית (או אחרת) ישירות לדמות, לחסוך זמן יקר, ולהכניס את יכולות המשחק של שחקנים גם לתוכן דיגיטלי. הטכנולוגיה הזו שינתה את עולם הקולנוע, משחקי הווידאו, הסימולציות ועוד.</p>

    <p><strong>מסע הלכידה ב-4 צעדים (כמו בסימולציה):</strong></p>
    <ul>
        <li><strong>הכנה (Setup):</strong> השחקן מתלבש בחליפה ייעודית עם עשרות סמנים (Markers) הממוקמים בנקודות מפתח על הגוף (מפרקים, גפיים, ראש). אולפן הלכידה מרושת במצלמות (לרוב אינפרא-אדום) שמטרתן לזהות את הסמנים במרחב. שלב הכיול הראשוני "מלמד" את המערכת את מיקום השחקן והקשר בין הסמנים לשלד דיגיטלי וירטואלי.</li>
        <li><strong>ביצוע ולכידה (Performance & Capture):</strong> השחקן מבצע את התנועה (הליכה, קפיצה, דיבור, קרב) והמצלמות עוקבות אחר מסלול כל סמן בזמן אמת. הנתונים הגולמיים הנאספים הם סדרה של נקודות תלת-ממדיות בזמן, המתארות את מיקום הסמנים בכל פריימים שנקלטו (במערכות מתקדמות זה יכול להיות מאות פריימים בשנייה!).</li>
        <li><strong>עיבוד נתונים (Data Processing/Cleaning):</strong> הנתונים הגולמיים לא מושלמים. לפעמים סמן נחסם לרגע, או שהמערכת "מתבלבלת" בזיהוי. שלב העיבוד כולל ניקוי רעשים, מילוי חורים בנתונים, החלקת מסלולי התנועה וקריאתם (Reconstruction). זהו תהליך שדורש ידע טכני ולעיתים גם התערבות ידנית כדי לוודא שהנתונים מדויקים ונקיים ככל הניתן.</li>
        <li><strong>החלת אנימציה (Applying to Rig):</strong> הנתונים המעובדים "מוזרמים" אל שלד (Rig) של דמות תלת-ממדית. כל סמן בחליפה המקורית מקושר ל"מפרק" או נקודה מתאימה בשלד הדיגיטלי. תנועת הסמן מניעה את המפרק הדיגיטלי, וכך כל השלד הדיגיטלי זז בדיוק כמו השחקן המקורי. מודל הדמות התלת-ממדי "מלובש" על השלד הזה, וכתוצאה מכך נראה שהדמות עצמה זזה באופן ריאליסטי להפליא.</li>
    </ul>

    <p><strong>למה MoCap ולא אנימציה ידנית (Keyframe)?</strong></p>
    <ul>
        <li><strong>פלוסים:</strong>
            <ul>
                <li><strong>ריאליזם וטבעיות:</strong> תנועה מורכבת ועשירה בניואנסים אנושיים שקשה מאוד ליצור ידנית.</li>
                <li><strong>מהירות:</strong> ניתן להפיק כמות גדולה של אנימציה באיכות גבוהה יחסית מהר יותר מאנימציית Keyframe מורכבת.</li>
                <li><strong>העברת "הנשמה":</strong> מאפשר להשתמש בכישרון משחק של שחקנים כדי להפיח חיים רגשיים ופיזיים בדמויות הדיגיטליות.</li>
            </ul>
        </li>
        <li><strong>מינוסים:</strong>
            <ul>
                <li><strong>עלות ציוד ותפעול:</strong> מצריך אולפן ייעודי, ציוד יקר וצוות טכני מיומן.</li>
                <li><strong>מגבלות פיזיות:</strong> קשה ליצור תנועות שאינן פיזיות (למשל, מעוף בדימיון) או שדורשות סגנון "קריקטורי" או מוגזם מאוד ללא עבודה נוספת.</li>
                <li><strong>זמן ניקוי:</strong> גם אחרי הלכידה, יש לעיתים צורך בזמן רב של ניקוי ותיקון נתונים ידני.</li>
            </ul>
        </li>
    </ul>

    <p><strong>היכן פוגשים MoCap?</strong></p>
    <p>MoCap הפכה לכלי חיוני בתעשיות רבות: סרטי שוברים קופות ("אווטאר", "שר הטבעות", "כוכב הקופים"), משחקי וידאו ריאליסטיים (NBA 2K, FIFA, The Last of Us), סימולטורים לאימון (טיסה, צבא), ואפילו בתחומי הרפואה (ניתוח הליכה) והספורט (ניתוח ביצועי ספורטאים). זהו תחום שמתפתח כל הזמן, עם חידושים כמו לכידה ללא סמנים (Markerless MoCap) ומערכות ניידות יותר.</p>
</div>

<style>
    /* כל הסגנונות מרוכזים כאן */
    #mocap-simulation-container {
        font-family: 'Arial', sans-serif;
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #d3e0ea; /* Light blue-gray border */
        border-radius: 12px; /* More rounded corners */
        overflow: hidden;
        background-color: #eef5f9; /* Very light blue background */
        direction: rtl; /* Right-to-left for Hebrew */
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer, larger shadow */
        position: relative; /* Needed for potential absolute overlays */
    }

    #simulation-area {
        padding: 30px; /* More padding */
        min-height: 500px; /* Increased height */
        position: relative;
        perspective: 1000px; /* For potential 3D effects */
    }

    .simulation-stage {
        display: none;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ffffff;
        padding: 30px; /* Match simulation area padding */
        border-radius: 12px; /* Match container border radius */
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08); /* Inner shadow */
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        opacity: 0;
        transition: opacity 0.5s ease-in-out; /* Fade transition between stages */
         box-sizing: border-box; /* Include padding in element's total width and height */
    }

    .simulation-stage.active {
        display: flex;
        opacity: 1;
        z-index: 1; /* Ensure active stage is on top */
    }

    .simulation-stage h2 {
        margin-top: 0;
        color: #0277bd; /* Darker blue for headings */
        text-align: center;
        font-size: 1.8em; /* Larger heading */
        margin-bottom: 15px;
    }
    .simulation-stage p {
        text-align: center;
        margin-bottom: 30px; /* More space below description */
        color: #555;
        line-height: 1.6; /* Improved readability */
    }

    .studio {
        position: relative;
        width: 90%; /* Slightly less than 100% */
        height: 250px; /* Taller studio */
        background: linear-gradient(to bottom, #b3e5fc 0%, #e1f5fe 100%); /* Blue gradient background */
        border-radius: 8px;
        margin-bottom: 30px; /* More space below studio */
        overflow: hidden;
        flex-shrink: 0;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
        border: 1px solid #81d4fa; /* Lighter border */
    }

    .floor {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 60px; /* Floor height */
        background-color: #cfd8dc; /* Light gray floor */
        box-shadow: inset 0 5px 10px rgba(0,0,0,0.1);
         z-index: 0; /* Below other elements */
    }

    .camera {
        position: absolute;
        width: 40px; /* Larger cameras */
        height: 25px;
        background-color: #455a64; /* Dark gray cameras */
        border-radius: 5px;
        border: 2px solid #263238;
        transform-origin: 50% 100%; /* Rotate from base */
        z-index: 2;
         transition: transform 0.5s ease; /* Smooth rotation */
    }
    .camera::after {
        content: '';
        position: absolute;
        top: 5px;
        left: 5px;
        width: 10px;
        height: 10px;
        background-color: #b0bec5; /* Lens highlight */
        border-radius: 3px;
    }
    .camera-1 { top: 15px; left: 15px; transform: rotate(35deg); }
    .camera-2 { top: 15px; right: 15px; transform: rotate(-35deg); }
    .camera-3 { bottom: 15px; left: 50%; margin-left: -20px; transform: rotate(0deg); } /* Centered */

    .camera.active {
         animation: camera-pulse 1.5s infinite ease-in-out; /* Add a pulsing effect when active */
    }
     @keyframes camera-pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
     }


    .calibration-beam {
        position: absolute;
        bottom: 60px; /* Start above floor */
        width: 4px;
        background-color: rgba(76, 175, 80, 0.5); /* Green beam */
        z-index: 1;
        transform-origin: bottom center;
        animation: calibrate 2s ease-out forwards;
         display: none; /* Hidden by default */
    }
     #stage-preparation.active .calibration-beam { display: block; } /* Show only on stage 1 */

    .beam-1 { left: 25%; height: 0; transform: scaleY(0); }
    .beam-2 { left: 50%; height: 0; transform: scaleY(0); animation-delay: 0.3s; }
    .beam-3 { left: 75%; height: 0; transform: scaleY(0); animation-delay: 0.6s; }

     @keyframes calibrate {
        0% { height: 0px; transform: scaleY(0); opacity: 0; }
        50% { height: 100px; transform: scaleY(1); opacity: 0.8; }
        100% { height: 0px; transform: scaleY(0); opacity: 0; }
    }


    .actor-mocap {
        position: absolute;
        bottom: 60px; /* On the floor */
        left: 50%;
        transform: translateX(-50%);
        width: 50px; /* Wider actor */
        height: 100px; /* Taller actor */
        background-color: #5c6bc0; /* Indigo suit */
        border: 2px solid #3f51b5;
        border-radius: 8px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: column;
         z-index: 2;
         transition: transform 0.3s ease-out; /* Smooth transitions */
    }
     .actor-mocap::before { /* Head */
        content: '';
        display: block;
        width: 25px; /* Larger head */
        height: 25px;
        background-color: #5c6bc0;
        border: 2px solid #3f51b5;
        border-radius: 50%;
        margin-top: 5px;
     }

     .mocap-marker {
         position: absolute;
         width: 10px;
         height: 10px;
         background-color: #ffeb3b; /* Bright yellow marker */
         border-radius: 50%;
         border: 2px solid #fbc02d;
         z-index: 3;
         box-shadow: 0 0 5px #ffeb3b;
         transition: transform 0.2s ease-out; /* Smooth movement */
     }
     .actor-mocap .head { top: 0px; left: 50%; transform: translateX(-50%); }
     .actor-mocap .torso { top: 40px; left: 50%; transform: translateX(-50%); }
     .actor-mocap .hand-l { top: 40px; left: 5px; }
     .actor-mocap .hand-r { top: 40px; right: 5px; }
     .actor-mocap .leg-l { bottom: 5px; left: 15px; }
     .actor-mocap .leg-r { bottom: 5px; right: 15px; }


    /* Performance Stage Animations */
    .actor-mocap.performing {
        animation: walk-and-jump 3s ease-in-out forwards;
    }
     /* Markers move with the actor based on the animation */
    .actor-mocap.performing .mocap-marker {
         animation: marker-walk-and-jump 3s ease-in-out forwards;
    }

    @keyframes walk-and-jump {
        0% { bottom: 60px; left: 50%; transform: translateX(-50%) rotateY(0); } /* Start center */
        20% { bottom: 60px; left: 30%; transform: translateX(-50%) rotateY(5deg); } /* Walk left */
        40% { bottom: 60px; left: 70%; transform: translateX(-50%) rotateY(-5deg); } /* Walk right */
        60% { bottom: 60px; left: 50%; transform: translateX(-50%) rotateY(0); } /* Return center, prepare jump */
        75% { bottom: 120px; left: 50%; transform: translateX(-50%) rotateY(0); } /* Jump up */
        100% { bottom: 60px; left: 50%; transform: translateX(-50%) rotateY(0); } /* Land */
    }
     /* A simplified marker animation that follows the actor's general path */
      @keyframes marker-walk-and-jump {
        0% { transform: translate(0, 0); } /* Relative to actor's position */
        20% { transform: translate(-10px, 0); }
        40% { transform: translate(10px, 0); }
        60% { transform: translate(0, 0); }
        75% { transform: translate(0, -60px); } /* Jump relative up */
        100% { transform: translate(0, 0); }
      }


    .marker-tracking-path {
         position: absolute;
         bottom: 60px; /* Start on floor level */
         left: 50%;
         transform: translateX(-50%);
         width: 0; /* Start with no width */
         height: 0; /* Start with no height */
         /* This element visually draws the path */
          border-left: 2px dashed rgba(255, 235, 59, 0.6); /* Dashed yellow line */
          z-index: 1;
          display: none; /* Initially hidden */
           pointer-events: none; /* Don't block clicks */
    }
    .studio.tracking .marker-tracking-path {
        display: block;
        animation: draw-path 3s ease-in-out forwards; /* Draw path with actor animation */
    }
     @keyframes draw-path {
         0% { width: 0; height: 0; border-top: 0px dashed transparent; border-left: 0px dashed transparent;}
         20% { width: 30px; height: 0; border-top: 0px dashed transparent; border-left: 2px dashed rgba(255, 235, 59, 0.6);}
         40% { width: 60px; height: 0; border-top: 0px dashed transparent; border-left: 2px dashed rgba(255, 235, 59, 0.6); }
         60% { width: 30px; height: 0; border-top: 0px dashed transparent; border-left: 2px dashed rgba(255, 235, 59, 0.6); }
         75% { width: 30px; height: 60px; border-top: 2px dashed rgba(255, 235, 59, 0.6); border-left: 2px dashed rgba(255, 235, 59, 0.6); }
         100% { width: 30px; height: 0px; border-top: 0px dashed transparent; border-left: 2px dashed rgba(255, 235, 59, 0.6); opacity: 0.5; }
     }
      /* Need to refine path drawing, this is a simplified version */


    .virtual-skeleton {
         position: absolute;
         bottom: 60px;
         left: calc(50% + 80px); /* Position it beside the actor */
         transform: translateX(-50%);
         width: 40px;
         height: 90px;
         background-color: rgba(121, 85, 72, 0.3); /* Transparent brown */
         border: 1px dashed #795548; /* Dashed brown border */
         border-radius: 5px;
         display: none; /* Initially hidden */
         z-index: 1;
         opacity: 0;
         transition: opacity 0.5s ease-in-out;
    }
     #stage-performance.active .virtual-skeleton {
         display: block;
         opacity: 1;
         animation: skeleton-pulse 1.5s infinite ease-in-out alternate; /* Pulse faintly */
     }
      @keyframes skeleton-pulse {
        0% { transform: translateX(-50%) scale(1); }
        100% { transform: translateX(-50%) scale(1.02); }
      }


    .data-display {
        display: flex;
        justify-content: space-around;
        align-items: center; /* Vertically center items */
        width: 100%;
        flex-grow: 1;
         margin-bottom: 30px;
         gap: 20px; /* Space between graphs */
    }

    .graph {
        width: 45%; /* Adjust for gap and processing indicator */
        height: 200px; /* Taller graphs */
        border: 1px solid #b0bec5; /* Light blue-gray border */
        border-radius: 8px;
        padding: 15px; /* More padding */
        text-align: center;
        position: relative;
        overflow: hidden;
         background-color: #eceff1; /* Light gray background */
         box-shadow: inset 0 0 8px rgba(0,0,0,0.05);
         flex-shrink: 0; /* Prevent shrinking */
    }

     .graph h4 {
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1em;
        color: #455a64; /* Dark gray text */
        border-bottom: 1px dashed #cfd8dc; /* Subtle separator */
        padding-bottom: 5px;
     }

     .graph-line {
         position: absolute;
         bottom: 0;
         left: 0;
         width: 100%;
         height: 100%;
         pointer-events: none;
     }

    .graph-line.raw {
         background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,50 C 10,60 20,40 30,55 40,45 50,65 60,35 70,55 80,40 90,60 100,50" stroke="%23e57373" stroke-width="2" fill="none"/></svg>'); /* SVG for noisy line */
         background-repeat: repeat-x;
         background-size: 50% 100%; /* Repeat the pattern */
         background-position: 0% 50%; /* Center vertical */
         transition: background-position 1s ease-in-out, opacity 1s ease-in-out;
     }

    .graph-line.processed {
         background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,50 C 25,50 75,50 100,50" stroke="%2381c784" stroke-width="3" fill="none"/></svg>'); /* SVG for smooth line */
         background-repeat: repeat-x;
         background-size: 100% 100%;
         background-position: 0% 50%; /* Center vertical */
         opacity: 0; /* Start hidden */
         transition: background-position 1s ease-in-out, opacity 1s ease-in-out;
     }

    .processing-indicator {
        width: 50px;
        height: 50px;
        border: 5px solid #b0bec5;
        border-top-color: #03a9f4; /* Blue top */
        border-radius: 50%;
        animation: spin 1s linear infinite;
        display: none; /* Initially hidden */
         flex-shrink: 0; /* Prevent shrinking */
         margin: 0 20px; /* Space it out */
    }
     @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
     }
     #stage-data-processing.processing .processing-indicator { display: block; } /* Show when processing */


    .character-area {
        width: 100%;
        height: 250px; /* Match studio height */
        /* background-color: #e0f7fa; */ /* Light cyan background */
        border-radius: 8px;
         display: flex;
         justify-content: center;
         align-items: flex-end; /* Align to bottom */
         flex-grow: 1;
         position: relative;
         flex-shrink: 0;
         margin-bottom: 30px;
          background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50"><rect width="100" height="50" fill="%23e0f7fa"/><circle cx="20" cy="20" r="5" fill="%23b2ebf2"/><circle cx="80" cy="30" r="7" fill="%23b2ebf2"/><circle cx="50" cy="10" r="4" fill="%23b2ebf2"/></svg>') repeat; /* Subtle background pattern */
          background-size: 100px 50px;
    }

    .character-rig {
         position: absolute;
         bottom: 60px; /* On the floor */
         width: 50px;
         height: 100px;
         background-color: rgba(178, 235, 242, 0.5); /* Transparent light blue */
         border: 1px dashed #4dd0e1; /* Dashed blue border */
         border-radius: 8px;
         z-index: 1;
         display: none; /* Initially hidden */
         opacity: 0;
         transition: opacity 0.5s ease-in-out;
         left: 50%;
         transform: translateX(-50%);
    }
     #stage-application.active .character-rig {
         display: block;
         opacity: 1;
          animation: rig-pulse 1.5s infinite ease-in-out alternate; /* Pulse faintly */
     }
      @keyframes rig-pulse {
        0% { transform: translateX(-50%) scale(1); }
        100% { transform: translateX(-50%) scale(1.02); }
      }


    .animated-character {
         width: 60px; /* Slightly larger than actor */
         height: 120px;
         background-color: #03a9f4; /* Bright blue character */
         border: 3px solid #0288d1;
         border-radius: 10px; /* More rounded */
         position: absolute;
         bottom: 60px; /* Start position on floor */
         opacity: 0; /* Initially hidden */
         transition: opacity 0.8s ease-in-out;
         left: 50%;
         transform: translateX(-50%);
         z-index: 2;
         box-shadow: 0 5px 15px rgba(0, 169, 244, 0.3); /* Blue glow shadow */
    }

    .animated-character.active {
        opacity: 1;
        /* Use the same animation as the actor for consistency */
        animation: walk-and-jump 3s ease-in-out forwards;
    }

    .data-flow-effect {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background: radial-gradient(circle, rgba(3, 169, 244, 0.2) 0%, transparent 70%); /* Subtle radial gradient */
         pointer-events: none;
         opacity: 0;
         transition: opacity 1s ease-in-out;
          z-index: 0;
    }
     #stage-application.active .data-flow-effect {
         opacity: 1;
         animation: data-glow 2s infinite alternate;
     }
     @keyframes data-glow {
         0% { opacity: 0.5; }
         100% { opacity: 0.8; }
     }


    .interactive-button {
        padding: 12px 25px; /* Larger padding */
        background-color: #4caf50; /* Green */
        color: white;
        border: none;
        border-radius: 25px; /* Pill shape */
        cursor: pointer;
        font-size: 1.1em; /* Larger font */
        transition: background-color 0.3s ease, transform 0.1s ease;
        align-self: center;
        flex-shrink: 0;
         box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Button shadow */
    }

    .interactive-button:hover:not(:disabled) {
        background-color: #388e3c; /* Darker green on hover */
        transform: translateY(-2px); /* Lift effect */
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    }

     .interactive-button:active:not(:disabled) {
         transform: translateY(0); /* Press effect */
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
     }


     .interactive-button:disabled {
        background-color: #a5d6a7; /* Lighter green when disabled */
        cursor: not-allowed;
        box-shadow: none;
         transform: none;
     }

    #toggle-explanation {
        display: block;
        margin: 30px auto; /* More margin */
        background-color: #03a9f4; /* Blue */
        box-shadow: 0 4px 8px rgba(0, 169, 244, 0.3); /* Blue glow shadow */
    }
     #toggle-explanation:hover:not(:disabled) {
        background-color: #0288d1; /* Darker blue on hover */
         box-shadow: 0 6px 12px rgba(0, 169, 244, 0.4);
     }
     #toggle-explanation:active:not(:disabled) {
         box-shadow: 0 2px 4px rgba(0, 169, 244, 0.3);
     }


    #explanation-section {
        max-width: 800px;
        margin: 20px auto;
        padding: 30px; /* More padding */
        border: 1px solid #d3e0ea;
        border-radius: 12px; /* Match container */
        background-color: #ffffff;
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    #explanation-section h2 {
        color: #0277bd; /* Match simulation heading color */
        border-bottom: 1px solid #e0e0e0; /* Lighter border */
        padding-bottom: 15px; /* More padding */
        margin-bottom: 20px;
        font-size: 1.6em;
    }

    #explanation-section h3, #explanation-section strong {
        color: #455a64; /* Dark gray */
    }

    #explanation-section ul {
        margin-top: 15px; /* More margin */
        margin-bottom: 20px;
        padding-right: 25px; /* For list bullets */
        list-style: disc inside;
        line-height: 1.6;
    }

    #explanation-section li {
        margin-bottom: 10px; /* More space between list items */
    }

     /* Add subtle hover effect to list items */
     #explanation-section li:hover {
        background-color: #eef5f9; /* Light highlight on hover */
        border-radius: 4px;
        padding: 2px 5px;
         margin-right: -5px; /* Adjust padding/margin for RTL */
         margin-left: -5px;
     }

</style>

<script>
    // שמירה קפדנית על מבנה ה-JS
    const simulationStages = [
        'stage-preparation',
        'stage-performance',
        'stage-data-processing',
        'stage-application'
    ];
    let currentStageIndex = 0;
    const simulationArea = document.getElementById('simulation-area');
    const explanationSection = document.getElementById('explanation-section');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const processDataButton = document.getElementById('process-data-button');
    const dataProcessingNextButton = document.querySelector('#stage-data-processing .next-stage-button');
    const animatedCharacter = document.querySelector('.animated-character');
    const rawGraphLine = document.querySelector('.graph-line.raw');
    const processedGraphLine = document.querySelector('.graph-line.processed');
    const studioElement = document.querySelector('.studio');
    const processingIndicator = document.querySelector('.processing-indicator');

    function showStage(index) {
        // Disable all next/reset buttons momentarily during transition
        document.querySelectorAll('.interactive-button').forEach(btn => btn.disabled = true);

        simulationStages.forEach((stageId, i) => {
            const stageElement = document.getElementById(stageId);
            if (i === index) {
                stageElement.classList.add('active');
                 // Allow transition to finish before making buttons clickable
                 setTimeout(() => {
                     // Enable only the relevant button(s) for the new active stage
                     const activeStageButtons = stageElement.querySelectorAll('.interactive-button');
                     activeStageButtons.forEach(btn => {
                          // Special handling for process button initial state
                          if (btn.id === 'process-data-button') {
                               btn.disabled = false; // Always enable process button when arriving at stage 3
                          } else if (stageElement.id === 'stage-data-processing' && btn.classList.contains('next-stage-button')) {
                               btn.disabled = true; // Keep next disabled until processing is done
                          } else {
                              btn.disabled = false; // Enable others
                          }
                     });

                     // Ensure the reset button is always enabled on the last stage
                     if (stageId === 'stage-application') {
                         const resetButton = stageElement.querySelector('.reset-simulation-button');
                         if (resetButton) resetButton.disabled = false;
                     }


                 }, 600); // Delay matches stage opacity transition

                // --- Stage Specific Setup / Animation Triggers ---
                if (stageId === 'stage-preparation') {
                    // Reset performance animations if coming back
                     const actor = document.querySelector('#stage-performance .actor-mocap');
                     if (actor) {
                         actor.classList.remove('performing');
                         // Reset animation state for re-triggering
                          actor.style.animation = 'none'; actor.offsetHeight; actor.style.animation = null;
                           actor.querySelectorAll('.mocap-marker').forEach(marker => {
                              marker.style.animation = 'none'; marker.offsetHeight; marker.style.animation = null;
                           });
                     }
                     const studio = document.querySelector('#stage-performance .studio');
                     if(studio) studio.classList.remove('tracking');

                     // Reset character animation if coming back from stage 4
                      if(animatedCharacter) {
                         animatedCharacter.classList.remove('active');
                          animatedCharacter.style.animation = 'none'; animatedCharacter.offsetHeight; animatedCharacter.style.animation = null;
                     }


                } else if (stageId === 'stage-performance') {
                    // Trigger performance animation after stage becomes active
                    const actor = stageElement.querySelector('.actor-mocap');
                    const studio = stageElement.querySelector('.studio');
                     if(actor) {
                         // Small delay before starting animation to ensure visibility
                         setTimeout(() => {
                             actor.classList.add('performing');
                              studio.classList.add('tracking'); // Trigger tracking visual
                             // Next button is handled by animationend listener now
                         }, 100);

                         // Use the animationend event on the actor to enable the next button
                          const performanceNextButton = stageElement.querySelector('.next-stage-button');
                         actor.addEventListener('animationend', function animationEndHandler() {
                             if(performanceNextButton) performanceNextButton.disabled = false;
                             // Remove listener after it fires
                             actor.removeEventListener('animationend', animationEndHandler);
                             studio.classList.remove('tracking'); // Hide tracking visual after animation
                         });
                     }


                } else if (stageId === 'stage-data-processing') {
                    // Reset graph appearance
                     if(rawGraphLine) {
                         rawGraphLine.style.backgroundPosition = '0% 50%'; // Center position
                         rawGraphLine.style.opacity = 1; // Ensure visible
                     }
                     if(processedGraphLine) {
                          processedGraphLine.style.backgroundPosition = '0% 50%'; // Center position
                          processedGraphLine.style.opacity = 0; // Start hidden
                     }
                     if(processingIndicator) processingIndicator.style.display = 'none'; // Hide indicator
                     stageElement.classList.remove('processing'); // Remove processing class


                 } else if (stageId === 'stage-application') {
                    // Stage 4 is now active - Trigger character animation
                     if(animatedCharacter) {
                          // Small delay to ensure stage is fully visible before animation
                         setTimeout(() => {
                             animatedCharacter.classList.add('active');
                         }, 100); // Delay
                     }
                 }

            } else {
                stageElement.classList.remove('active');
                // Stop animations on inactive stages
                 stageElement.querySelectorAll('.animated, .performing').forEach(el => {
                     el.classList.remove('animated', 'performing');
                      // Reset animation state for re-triggering if needed later
                      el.style.animation = 'none'; el.offsetHeight; el.style.animation = null;
                 });
                  // Remove tracking visual on performance stage when leaving
                  if(stageId === 'stage-performance') {
                      const studio = stageElement.querySelector('.studio');
                      if(studio) studio.classList.remove('tracking');
                  }
                   // Hide character on stage 4 when leaving
                    if(stageId === 'stage-application' && animatedCharacter) {
                       animatedCharacter.classList.remove('active');
                       animatedCharacter.style.animation = 'none'; animatedCharacter.offsetHeight; animatedCharacter.style.animation = null;
                    }
                    // Hide processing indicator on stage 3 when leaving
                     if(stageId === 'stage-data-processing' && processingIndicator) {
                          processingIndicator.style.display = 'none';
                          stageElement.classList.remove('processing');
                     }
            }
        });
    }

    function attachEventListeners() {
        // Event listener for "Next Stage" and "Reset" buttons (delegation)
        simulationArea.addEventListener('click', (event) => {
            if (event.target.classList.contains('next-stage-button') && !event.target.disabled) {
                 if (currentStageIndex < simulationStages.length - 1) {
                    currentStageIndex++;
                    showStage(currentStageIndex);
                 }
            } else if (event.target.classList.contains('reset-simulation-button') && !event.target.disabled) {
                 // Event listener for "Reset Simulation" button
                currentStageIndex = 0;
                showStage(currentStageIndex);
            }
        });


        // Event listener for "Process Data" button
        if(processDataButton) {
             processDataButton.addEventListener('click', () => {
                 if (!processDataButton.disabled) {
                     processDataButton.disabled = true; // Disable button immediately
                     const stageElement = document.getElementById('stage-data-processing');
                     if(stageElement) stageElement.classList.add('processing'); // Add processing class

                     if(processingIndicator) processingIndicator.style.display = 'block';

                     // Simulate processing time
                     setTimeout(() => {
                         // Simulate data processing visually
                         if(rawGraphLine) {
                            rawGraphLine.style.opacity = 0.3; // Fade raw data
                             rawGraphLine.style.backgroundPosition = '0% 20%'; // Shift raw data slightly as if being refined
                         }
                         if(processedGraphLine) {
                             processedGraphLine.style.opacity = 1; // Show processed data
                             processedGraphLine.style.backgroundPosition = '0% 50%'; // Ensure processed line is centered
                         }

                         if(processingIndicator) processingIndicator.style.display = 'none'; // Hide indicator
                         if(stageElement) stageElement.classList.remove('processing'); // Remove processing class

                         if(dataProcessingNextButton) dataProcessingNextButton.disabled = false; // Enable next stage button

                     }, 2000); // Simulation time
                 }
             });
        }


        // Event listener for explanation toggle
        if(toggleExplanationButton && explanationSection) {
            toggleExplanationButton.addEventListener('click', () => {
                const isHidden = explanationSection.style.display === 'none';
                explanationSection.style.display = isHidden ? 'block' : 'none';
                toggleExplanationButton.textContent = isHidden ? 'הסתר הצצה אל מאחורי הקלעים' : 'הצג/הסתר הצצה אל מאחורי הקלעים (הסבר מורחב)';
            });
        }

         // Listen for animation end on the character to potentially do something after it finishes
         if(animatedCharacter) {
             animatedCharacter.addEventListener('animationend', () => {
                // Animation finished on the character.
                // In this simple case, we just let it finish. Could add a final message or effect here.
             });
         }

          // Listen for calibration animation end to potentially enable first button (though it's enabled initially)
          const calibrationBeams = document.querySelectorAll('.calibration-beam');
           if(calibrationBeams.length > 0) {
               calibrationBeams[calibrationBeams.length - 1].addEventListener('animationend', () => {
                   // Calibration animation on stage 1 finished.
                   // The button is already enabled by showStage logic, so no action needed here currently.
               });
           }

    }

     // Initial display of the first stage when the script loads
    showStage(currentStageIndex);
     // Attach event listeners once the DOM is ready (or script is at the end)
    attachEventListeners();

</script>
```