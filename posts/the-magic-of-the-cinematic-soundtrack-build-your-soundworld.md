---
title: "קסם הפסקול הקולנועי: בנה את העולם השמיעתי של סרט"
english_slug: the-magic-of-the-cinematic-soundtrack-build-your-soundworld
category: "אמנות ועיצוב / קולנוע"
tags: ["פסקול", "קולנוע", "עיצוב סאונד", "עריכת קול", "הפקה קולנועית", "חוויה אינטראקטיבית"]
---
# קסם הפסקול הקולנועי: בנה את העולם השמיעתי של סרט

האם שמתם לב איך מוזיקה או אפקטים קוליים פשוטים יכולים לשנות לגמרי את התחושה של סצנה? איך צליל נכון יכול להקפיץ אתכם בכיסא, לגרום לכם להזיל דמעה, או לשלוח צמרמורת במורד הגב? הפסקול הוא הקוסם הנסתר של הקולנוע, זה שמעצב את הרגש והאווירה מבלי שנשים לב.

איך זה עובד מאחורי הקלעים? איך מעצבי סאונד ומלחינים בונים את העולם השמיעתי שגורם לנו להרגיש כל כך הרבה?

<div id="app-container">
    <div id="video-area">
        <div class="video-wrapper">
             <video id="cinematic-scene" width="640" height="360" playsinline>
                <source src="https://interactive-assets.s3.eu-central-1.amazonaws.com/silent_placeholder_scene.mp4" type="video/mp4">
                דפדפן הווידאו שלך אינו תומך בפורמט זה. (הערה: זהו קטע וידאו שקט וגנרי למטרות הדגמה - דמיינו דמות נכנסת לחדר ומשהו נשבר).
            </video>
             <div class="video-overlay"></div> <!-- For potential future effects or branding -->
        </div>

        <button id="play-button" class="action-button">
            <svg class="play-icon" viewBox="0 0 24 24"><path d="M8,5.14V19.14L19,12.14L8,5.14Z" /></svg>
            נגן סצנה עם הפסקול שבנית
        </button>
         <p class="instruction-text">הגדירו את הפסקול למטה ולחצו על כפתור הנגן כדי לחוות את ההבדל!</p>
    </div>

    <div id="controls-area">
        <h2>בנה את הפסקול שלך:</h2>
        <p class="instruction-text">שחקו עם השילובים השונים ובדקו איך כל רכיב משפיע על האווירה והרגש של הסצנה.</p>

        <div class="control-section">
            <h3><i class="icon">🎵</i> מוזיקת רקע</h3>
            <div class="control-row">
                <label for="music-select">סוג המוזיקה:</label>
                <select id="music-select">
                    <option value="none">ללא מוזיקה</option>
                    <option value="mystery">מסתורית</option>
                    <option value="suspense">מתח</option>
                    <option value="calm">רגועה</option>
                </select>
            </div>
             <div class="control-row">
                <label for="music-volume">ווליום:</label>
                <input type="range" id="music-volume" min="0" max="1" step="0.01" value="0.5">
                <span class="volume-indicator" data-volume-for="music-volume">50%</span>
            </div>
        </div>

        <div class="control-section">
            <h3><i class="icon">🌬️</i> אווירה (Ambiance)</h3>
             <div class="control-row">
                <label for="ambiance-select">סוג האווירה:</label>
                <select id="ambiance-select">
                    <option value="none">ללא אווירה</option>
                    <option value="room_tone">טון חדר שקט</option>
                    <option value="wind">רוח קלה</option>
                    <option value="city">רחוב עיר (מרוחק)</option>
                </select>
             </div>
             <div class="control-row">
                <label for="ambiance-volume">ווליום:</label>
                <input type="range" id="ambiance-volume" min="0" max="1" step="0.01" value="0.5">
                 <span class="volume-indicator" data-volume-for="ambiance-volume">50%</span>
            </div>
        </div>

        <div class="control-section">
            <h3><i class="icon">💥</i> אפקטים קוליים (SFX)</h3>
             <p class="instruction-text">בחרו אילו צלילים יופיעו בזמן הנכון בסצנה. שימו לב איך כל צליל משפיע על הסיפור שאתם רואים ושומעים!</p>
            <div class="sfx-options">
                <div><input type="checkbox" id="sfx-door_knock" value="door_knock"><label for="sfx-door_knock"> דפיקה על דלת</label></div>
                <div><input type="checkbox" id="sfx-footsteps" value="footsteps"><label for="sfx-footsteps"> צעדים (קרובים)</label></div>
                <div><input type="checkbox" id="sfx-glass_break" value="glass_break"><label for="sfx-glass_break"> שבירת זכוכית</label></div>
                <div><input type="checkbox" id="sfx-door_creak" value="door_creak"><label for="sfx-door_creak"> דלת נפתחת (חריקה)</label></div>
            </div>
            <div class="control-row">
                <label for="sfx-volume">ווליום גלובלי לאפקטים:</label>
                <input type="range" id="sfx-volume" min="0" max="1" step="0.01" value="0.7">
                 <span class="volume-indicator" data-volume-for="sfx-volume">70%</span>
            </div>
        </div>
         <button id="reset-audio-button" class="secondary-button">איפוס פסקול</button>
    </div>
</div>

<button id="toggle-explanation" class="toggle-button">הצג/הסתר: לגלות את סודות הפסקול הקולנועי</button>

<div id="explanation" style="display: none;">
    <h2>לגלות את סודות הפסקול הקולנועי</h2>
    <p>מעבר לוויזואליה המרהיבה, הפסקול הוא הלב הפועם של הסרט, זה שנותן לו חיים, רגש ומציאות. הוא לא רק מלווה את התמונה, אלא לעיתים קרובות *יוצר* את התחושה, מספק מידע חיוני, ואפילו משנה את הדרך בה אנו מבינים את מה שקורה על המסך.</p>

    <h3>מרכיבי הקסם: מהו בעצם פסקול קולנועי?</h3>
    פסקול קולנועי איכותי הוא שילוב קפדני של ארבעה סוגי צלילים עיקריים, המעובדים ומעורבבים יחד ביצירתיות אמנותית וטכנית:
    <ul>
        <li>**דיאלוגים וקולות (Dialog & Voice):** אלו הקולות של הדמויות, השיחות ביניהן, וכל קריינות. זהו המידע המילולי שעוזר לנו לעקוב אחרי העלילה ולהכיר את הדמויות. הדיאלוג הוא עמוד השדרה הנרטיבי השמיעתי.</li>
        <li>**אפקטים קוליים (Sound Effects - SFX):** כל הצלילים המיוחדים שמדגישים אירועים, פעולות או אובייקטים בסצנה. חשבו על פיצוץ ענק, דפיקה קטנה על דלת, שבירת כוס, ציוץ ציפור, או צליל פתיחת הודעה בטלפון. אפקטים אלו מוסיפים ריאליזם, הדגשה דרמטית, או אפילו משמשים כרמז עלילתי. הם יכולים להיות מוקלטים באתר הצילומים, מבוצעים באולפן בטכניקת Foley (יצירת צלילים סינכרוניים לתמונה), או מתוך ספריות סאונד עשירות.</li>
        <li>**מוזיקה (Music Score):** המוזיקה שהולחנה במיוחד עבור הסרט או נבחרה בקפידה מפסקולים קיימים. תפקידה העיקרי הוא לעצב את האווירה הרגשית של הסצנה, להדגיש רגעים מסוימים, לבנות מתח, ליצור תחושת שחרור, או פשוט ללוות את האקשן. המוזיקה היא אחד הכלים החזקים ביותר ליצירת חיבור רגשי עם הקהל.</li>
        <li>**אווירה (Ambiance):** צלילי הרקע הקבועים של המיקום בו מתרחשת הסצנה. זה יכול להיות רחש עיר סואנת, שקט של יער, המולה של שוק, או אפילו ה"צליל" הייחודי של חדר סגור (Room Tone). האווירה חיונית ליצירת תחושת מציאות, עומק וקנה מידה למרחב המוצג.</li>
    </ul>

    <h3>התפקיד הסמוי של הפסקול: יותר מסתם ליווי</h3>
    מעצבי סאונד הם אמנים שמפסלים את החוויה האודיו-ויזואלית. הם משתמשים במרכיבים הללו כדי להשיג מטרות דרמטיות וטכניות:
    <ul>
        <li>**עיצוב רגש ואווירה:** המוזיקה והאווירה עובדות יחד כדי לגרום לנו *להרגיש* את הסצנה – האם היא מפחידה, שמחה, מלנכולית, או מותחת?</li>
        <li>**העצמת הנרטיב:** אפקטים קוליים או שינויים במוזיקה יכולים להדגיש רגעים חשובים בעלילה או לרמוז על מה שעומד לקרות.</li>
        <li>**בניית עולם:** אווירה מדויקת ואפקטים קוליים ריאליסטיים (או מכוונים להיות לא ריאליסטיים) עוזרים לנו להאמין בעולם הסרט ולשקוע בו.</li>
        <li>**הכוונה ומיקוד:** מעצב סאונד יכול להשתמש בווליום, במיקום הצליל ובאיכותו כדי להפנות את תשומת הלב שלנו לאלמנטים ספציפיים על המסך או מחוצה לו.</li>
        <li>**יצירת קצב ודינמיקה:** מעברים חדים בין שקט לרעש, שינויים בווליום או בקצב המוזיקה משפיעים ישירות על הקצב הרגשי והויזואלי של הסצנה כולה.</li>
    </ul>

    <h3>מאחורי הקלעים: יצירת הפסקול בפועל</h3>
    תהליך בניית הפסקול מתרחש לרוב בשלב הפוסט-פרודקשן, לאחר שהצילומים הסתיימו והעריכה הוויזואלית הושלמה. עורכי סאונד, מעצבי סאונד, מלחינים ומיקסרים עובדים יחד בסינכרון מושלם עם התמונה. הם מנקדים את הווידאו באפקטים קוליים בזמן הנכון, מוסיפים את רצועות האווירה, משלבים את המוזיקה שהולחנה ומאזנים את כל הערוצים הללו (כולל הדיאלוג המקורי) לכדי יצירה שמיעתית אחת, אחידה ומרתקת – הפסקול הסופי שאותו אנו שומעים באולם הקולנוע או על המסך בבית.

    הניסוי הקצר שחוויתם למעלה הוא רק טעימה קטנה מהכוח העצום שיש לסאונד ביצירת החוויה הקולנועית. נסו אותו שוב עם שילובים שונים כדי לראות כמה דרכים יש לספר אותו סיפור ויזואלי באמצעות סאונד בלבד!
</div>

<style>
    :root {
        --primary-color: #007bff; /* A vibrant blue */
        --secondary-color: #6c757d; /* Grey for secondary actions */
        --accent-color: #ffc107; /* Yellow for highlights/indicators */
        --text-color: #333;
        --bg-color: #f8f9fa; /* Light background */
        --card-bg: #fff; /* White for cards/sections */
        --border-color: #e9ecef; /* Light grey border */
        --shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        --border-radius: 8px;
        --transition-speed: 0.3s ease;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
        margin: 0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: var(--text-color);
        margin-bottom: 15px;
    }
     h1 { font-size: 2em; text-align: center; margin-bottom: 30px; }
     h2 { font-size: 1.5em; border-bottom: 2px solid var(--primary-color); padding-bottom: 5px; margin-top: 20px; }
     h3 { font-size: 1.2em; color: var(--primary-color); margin-bottom: 10px; }


    #app-container {
        display: flex;
        flex-direction: column;
        gap: 30px;
        max-width: 800px;
        margin: 20px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--card-bg);
        box-shadow: var(--shadow);
    }

    #video-area {
        text-align: center;
        position: relative; /* Needed for overlay */
    }

     .video-wrapper {
         position: relative;
         width: 100%; /* Make video wrapper responsive */
         max-width: 640px;
         margin: 0 auto 20px auto;
         background-color: #000;
         border-radius: var(--border-radius);
         overflow: hidden; /* Ensures rounded corners */
     }

    #cinematic-scene {
        display: block;
        width: 100%; /* Video fills wrapper */
        height: auto; /* Maintain aspect ratio */
        margin: 0;
        background-color: #000; /* To make placeholder clear */
    }
     /* Hide default video controls */
     #cinematic-scene::-webkit-media-controls { display:none !important; }
     #cinematic-scene::media-controls { display:none !important; }
    /* Custom controls will be implemented or it relies on the play button */


    .action-button, .secondary-button, .toggle-button {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        transition: background-color var(--transition-speed), transform 0.1s ease;
        margin: 0 auto;
        min-width: 200px;
    }

    .action-button {
        background-color: var(--primary-color);
        color: white;
         margin-bottom: 15px;
    }

    .action-button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
     .action-button:active {
         transform: translateY(0);
     }

     .play-icon {
         fill: white;
         width: 24px;
         height: 24px;
         margin-right: 8px;
     }

     .secondary-button {
         background-color: var(--secondary-color);
         color: white;
         margin-top: 20px;
     }
     .secondary-button:hover {
         background-color: #5a6268;
          transform: translateY(-1px);
     }
      .secondary-button:active {
         transform: translateY(0);
     }

    .toggle-button {
         background-color: var(--secondary-color);
         color: white;
         display: block; /* overridden by margin: auto */
         margin: 20px auto;
     }
     .toggle-button:hover {
        background-color: #5a6268;
     }


    #controls-area {
        display: flex;
        flex-direction: column;
        gap: 25px;
        padding-top: 20px;
         border-top: 1px solid var(--border-color);
    }

    .control-section {
        padding: 20px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--bg-color); /* Slightly different background */
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .control-section h3 {
        margin-top: 0;
        color: var(--text-color);
        border-bottom: none; /* Remove border from h3 here, use gap/margin */
        padding-bottom: 0;
        margin-bottom: 15px;
         display: flex;
         align-items: center;
    }
     .control-section h3 .icon {
         margin-right: 8px;
         color: var(--primary-color);
         font-style: normal; /* Icons are not italic */
     }


    .control-row {
        display: flex;
        align-items: center;
        margin-bottom: 10px; /* Space between rows in a section */
         flex-wrap: wrap; /* Allow wrapping on small screens */
    }
     .control-row:last-child {
         margin-bottom: 0;
     }


    .control-section label {
        display: inline-block;
        margin-bottom: 0; /* Reset margin-bottom from general label */
        font-weight: bold;
        min-width: 120px; /* Give labels a minimum width for alignment */
        margin-right: 10px;
         flex-shrink: 0; /* Prevent shrinking */
         line-height: 30px; /* Align with input height */
    }

    .control-section select,
    .control-section input[type="range"] {
        margin-right: 15px;
        vertical-align: middle;
        flex-grow: 1; /* Allow inputs to take available space */
         max-width: 250px; /* Limit width for range sliders etc. */
         height: 30px; /* Consistent height */
    }
     .control-section select {
         padding: 8px 10px;
         border: 1px solid #ccc;
         border-radius: 4px;
         background-color: var(--card-bg);
         cursor: pointer;
         outline: none;
         transition: border-color var(--transition-speed);
     }
     .control-section select:focus {
         border-color: var(--primary-color);
         box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
     }

     .control-section input[type="range"] {
         -webkit-appearance: none; /* Override default appearance */
         appearance: none;
         background: var(--border-color);
         outline: none;
         opacity: 0.7;
         transition: opacity var(--transition-speed);
          height: 8px; /* Make slider thinner */
          border-radius: 5px;
     }

     .control-section input[type="range"]::-webkit-slider-thumb {
         -webkit-appearance: none;
         appearance: none;
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
         transition: background var(--transition-speed);
          margin-top: -6px; /* Center thumb vertically */
     }

     .control-section input[type="range"]::-moz-range-thumb {
         width: 20px;
         height: 20px;
         background: var(--primary-color);
         border-radius: 50%;
         cursor: pointer;
          transition: background var(--transition-speed);
     }
      .control-section input[type="range"]:hover {
          opacity: 1;
      }
      .control-section input[type="range"]:hover::-webkit-slider-thumb {
           background: #0056b3;
      }
       .control-section input[type="range"]:hover::-moz-range-thumb {
           background: #0056b3;
      }


    .volume-indicator {
        min-width: 40px; /* Ensure space for text */
        text-align: left;
        font-size: 0.9em;
        color: var(--secondary-color);
    }

    .sfx-options {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); /* Adjusted min width */
        gap: 12px; /* Increased gap */
        margin-top: 15px;
         padding: 15px;
         background-color: #f1f1f1; /* Slight background for SFX block */
         border-radius: var(--border-radius);
    }

    .sfx-options div {
        display: flex;
        align-items: center;
         background-color: var(--card-bg);
         padding: 8px;
         border-radius: 4px;
         border: 1px solid var(--border-color);
         cursor: pointer;
         transition: background-color var(--transition-speed), border-color var(--transition-speed);
    }
     .sfx-options div:hover {
         background-color: #e9ecef;
         border-color: var(--primary-color);
     }
      .sfx-options input[type="checkbox"]:checked + label {
          font-weight: bold;
          color: var(--primary-color);
      }
       .sfx-options input[type="checkbox"]:checked + label::before {
           content: '✅ '; /* Add a checkmark or indicator */
       }


    .sfx-options input[type="checkbox"] {
        margin-right: 8px;
        cursor: pointer;
    }
     .sfx-options label {
         font-weight: normal;
         margin-bottom: 0;
         min-width: auto; /* Reset min-width */
         cursor: pointer;
         flex-grow: 1; /* Label fills space */
     }

    .instruction-text {
        text-align: center;
        color: var(--secondary-color);
        font-size: 0.95em;
        margin-top: 5px;
         margin-bottom: 15px;
    }


    #explanation {
        max-width: 800px;
        margin: 30px auto;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--card-bg);
        box-shadow: var(--shadow);
         line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: var(--text-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
     #explanation h2 { margin-top: 0; }


    #explanation ul {
        padding-left: 25px;
        margin-bottom: 20px;
    }

    #explanation li {
        margin-bottom: 12px;
        line-height: 1.6;
    }
     #explanation li strong {
         color: var(--primary-color);
     }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        #app-container, #explanation {
            padding: 20px;
            margin: 15px auto;
            gap: 20px;
        }
         .action-button, .secondary-button, .toggle-button {
             font-size: 1em;
             padding: 10px 20px;
             min-width: unset;
             width: 100%;
         }
         .control-row {
             flex-direction: column;
             align-items: flex-start;
             gap: 5px;
         }
         .control-section label {
             min-width: auto;
             margin-right: 0;
             margin-bottom: 5px;
             line-height: normal;
         }
          .control-section select,
          .control-section input[type="range"] {
             width: 100%;
             max-width: none;
             margin-right: 0;
         }
         .volume-indicator {
             align-self: flex-end; /* Position % indicator */
         }
         .sfx-options {
             grid-template-columns: 1fr; /* Stack SFX options vertically */
         }
          .sfx-options div {
              padding: 10px;
          }
    }

</style>

<script>
    const video = document.getElementById('cinematic-scene');
    const playButton = document.getElementById('play-button');
    const resetButton = document.getElementById('reset-audio-button'); // Get reset button

    const musicSelect = document.getElementById('music-select');
    const musicVolume = document.getElementById('music-volume');
    const ambianceSelect = document.getElementById('ambiance-select');
    const ambianceVolume = document.getElementById('ambiance-volume');
    const sfxCheckboxes = document.querySelectorAll('.sfx-options input[type="checkbox"]');
    const sfxGlobalVolume = document.getElementById('sfx-volume');
     const volumeIndicators = document.querySelectorAll('.volume-indicator'); // Get volume indicators


    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const explanationDiv = document.getElementById('explanation');

    // --- Audio Elements (Placeholders) ---
    // Load audio elements only once
    const audioAssets = {
        music: {
            mystery: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_mystery_music.mp3'),
            suspense: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_suspense_music.mp3'),
            calm: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_calm_music.mp3'),
            none: null
        },
        ambiance: {
            room_tone: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_room_tone.mp3'),
            wind: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_wind.mp3'),
            city: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_city_ambiance.mp3'),
            none: null
        },
        sfx: {
            door_knock: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_door_knock.mp3'),
            footsteps: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_footsteps.mp3'),
            glass_break: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_glass_break.mp3'),
            door_creak: new Audio('https://interactive-assets.s3.eu-central-1.amazonaws.com/placeholder_door_creak.mp3')
        }
    };

    // --- SFX Timing Schedule (based on an imagined 15-20 second scene) ---
    const sfxSchedule = [
        { time: 2.5, sfx: 'door_knock' },
        { time: 4.0, sfx: 'door_creak' }, // Door opens after knock
        { time: 5.5, sfx: 'footsteps' }, // Character enters
        { time: 8.0, sfx: 'footsteps' }, // Character walks further
        { time: 12.0, sfx: 'glass_break' } // Something breaks off-screen?
    ];
    let sfxTriggered = {}; // To track which SFX events have already triggered at a given time

    // --- Initialize Audio Settings and Volumes ---
    let currentMusic = null;
    let currentAmbiance = null;

    // Set initial volumes and update indicators
    function updateVolumeIndicator(inputElement) {
        const indicator = document.querySelector(`.volume-indicator[data-volume-for="${inputElement.id}"]`);
        if (indicator) {
            const percent = Math.round(inputElement.value * 100);
            indicator.textContent = `${percent}%`;
        }
    }

    musicVolume.addEventListener('input', () => {
        if (currentMusic) currentMusic.volume = musicVolume.value;
        updateVolumeIndicator(musicVolume);
    });
    ambianceVolume.addEventListener('input', () => {
        if (currentAmbiance) currentAmbiance.volume = ambianceVolume.value;
        updateVolumeIndicator(ambianceVolume);
    });
    sfxGlobalVolume.addEventListener('input', () => {
        // Update volume for all individual SFX instances if needed (or just rely on the timeupdate logic)
        // For simplicity, we'll ensure the volume is set when the SFX plays in handleVideoTimeUpdate
        updateVolumeIndicator(sfxGlobalVolume);
    });

     // Initial update for all indicators
     volumeIndicators.forEach(indicator => {
         const inputId = indicator.dataset.volumeFor;
         const inputElement = document.getElementById(inputId);
         if(inputElement) {
             updateVolumeIndicator(inputElement);
         }
     });


    // --- Playback Logic ---
    playButton.addEventListener('click', () => {
        // Stop any currently playing audio and video
        video.pause();
        video.currentTime = 0; // Reset video
        stopAllAudio(); // Stop currently playing tracks

        // Reset SFX triggered state
        sfxTriggered = {};
        sfxSchedule.forEach(item => sfxTriggered[item.time + '_' + item.sfx] = false);

        // Add timeupdate listener before playing
        video.removeEventListener('timeupdate', handleVideoTimeUpdate); // Prevent multiple listeners
        video.addEventListener('timeupdate', handleVideoTimeUpdate);

        // Start selected music
        const selectedMusicKey = musicSelect.value;
        if (selectedMusicKey !== 'none') {
            currentMusic = audioAssets.music[selectedMusicKey];
            if (currentMusic) {
                currentMusic.loop = true;
                currentMusic.volume = parseFloat(musicVolume.value); // Ensure float
                // Use a promise to handle potential play() errors (e.g., browser restrictions)
                currentMusic.play().catch(e => console.error("Error playing music:", e));
            }
        } else {
            currentMusic = null;
        }

        // Start selected ambiance
        const selectedAmbianceKey = ambianceSelect.value;
        if (selectedAmbianceKey !== 'none') {
            currentAmbiance = audioAssets.ambiance[selectedAmbianceKey];
            if (currentAmbiance) {
                currentAmbiance.loop = true;
                 currentAmbiance.volume = parseFloat(ambianceVolume.value); // Ensure float
                currentAmbiance.play().catch(e => console.error("Error playing ambiance:", e));
            }
        } else {
            currentAmbiance = null;
        }

        // Play video
        video.play().catch(e => console.error("Error playing video:", e));

        // Stop audio and remove listener when video ends
        video.onended = () => {
            stopAllAudio();
            video.removeEventListener('timeupdate', handleVideoTimeUpdate);
            video.onended = null; // Clean up this specific listener instance
        };
    });

    function handleVideoTimeUpdate() {
        const currentTime = video.currentTime;
        const globalSfxVol = parseFloat(sfxGlobalVolume.value);

        sfxSchedule.forEach(item => {
            const sfxKey = item.sfx;
            const sfxId = 'sfx-' + sfxKey;
            const checkbox = document.getElementById(sfxId);

            // Check if time is reached, not yet triggered, and SFX is enabled
            // Use a small time buffer (e.g., 0.1s) to ensure trigger even if timeupdate isn't exact
            if (currentTime >= item.time && currentTime < item.time + 0.5 && sfxTriggered[item.time + '_' + item.sfx] === false && checkbox && checkbox.checked) {
                 const sfxAudio = audioAssets.sfx[sfxKey];
                 if(sfxAudio) {
                     // Important: To play SFX multiple times if the video is replayed without page refresh,
                     // we might need to manage audio objects differently (e.g. create new ones or manage pools).
                     // For this simple demo, rewinding and playing the single instance is sufficient if SFX don't overlap heavily.
                     sfxAudio.currentTime = 0; // Rewind
                     sfxAudio.volume = globalSfxVol; // Apply global SFX volume
                     sfxAudio.play().catch(e => console.error("Error playing SFX:", sfxKey, e));

                     // Add temporary visual feedback on the checkbox label
                     const label = document.querySelector(`label[for="${sfxId}"]`);
                     if (label) {
                         label.classList.add('sfx-triggered');
                         setTimeout(() => {
                             label.classList.remove('sfx-triggered');
                         }, 500); // Remove class after 500ms
                     }


                     sfxTriggered[item.time + '_' + item.sfx] = true; // Mark as triggered
                 }
            }
        });
    }


    function stopAllAudio() {
        // Pause and rewind current music and ambiance
        if (currentMusic && !currentMusic.paused) {
            currentMusic.pause();
            currentMusic.currentTime = 0;
        }
        if (currentAmbiance && !currentAmbiance.paused) {
            currentAmbiance.pause();
            currentAmbiance.currentTime = 0;
        }
        // Pause and rewind all potential SFX instances
         for (const key in audioAssets.sfx) {
            if (audioAssets.sfx[key] && !audioAssets.sfx[key].paused) {
                audioAssets.sfx[key].pause();
                audioAssets.sfx[key].currentTime = 0;
            }
        }
    }

     // Reset audio settings and controls
     resetButton.addEventListener('click', () => {
        video.pause();
        video.currentTime = 0;
        stopAllAudio();
         video.removeEventListener('timeupdate', handleVideoTimeUpdate); // Clean up listener

        // Reset control values to defaults
        musicSelect.value = 'none';
        musicVolume.value = '0.5';
        ambianceSelect.value = 'none';
        ambianceVolume.value = '0.5';
        sfxCheckboxes.forEach(checkbox => checkbox.checked = false);
        sfxGlobalVolume.value = '0.7';

        // Update volume indicators
        volumeIndicators.forEach(indicator => {
            const inputId = indicator.dataset.volumeFor;
            const inputElement = document.getElementById(inputId);
             if(inputElement) {
                 updateVolumeIndicator(inputElement);
             }
         });

         // Reset SFX triggered state
         sfxTriggered = {};
         sfxSchedule.forEach(item => sfxTriggered[item.time + '_' + item.sfx] = false);

         console.log("Audio settings reset.");
     });


     // Stop audio and video when window is closed or page navigated away
     window.addEventListener('beforeunload', () => {
         video.pause();
         stopAllAudio();
     });


    // --- Explanation Toggle Logic ---
    toggleExplanationButton.addEventListener('click', () => {
        const isHidden = explanationDiv.style.display === 'none';
        // Use a simple class toggle for potential future animation via CSS
        if (isHidden) {
            explanationDiv.style.display = 'block';
            toggleExplanationButton.textContent = 'הסתר: סודות הפסקול הקולנועי';
        } else {
            explanationDiv.style.display = 'none';
             toggleExplanationButton.textContent = 'הצג/הסתר: לגלות את סודות הפסקול הקולנועי';
        }
    });

    // --- Initial state ---
    video.volume = 0; // Ensure video's original audio is off
    // Initial mute for all loaded audio elements
     for (const type in audioAssets) {
         for (const key in audioAssets[type]) {
             if (audioAssets[type][key]) {
                audioAssets[type][key].volume = 0; // Initial mute
                // Preload audio files if possible (optional, can add complexity)
                // audioAssets[type][key].load();
             }
         }
     }


</script>
---
```