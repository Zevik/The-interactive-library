---
title: "ספקטרוסקופ: טביעות האצבע הקוסמיות של יסודות"
english_slug: spectrometer-cosmic-fingerprints-elements
category: "פיזיקה"
tags:
  - ספקטרוסקופיה
  - אור
  - ספקטרום
  - יסודות
  - בליעה
  - פליטה
  - אסטרונומיה
---
# ספקטרוסקופ: טביעות האצבע הקוסמיות של יסודות
כיצד מדענים מפענחים את ההרכב הכימי של כוכבים רחוקים, ערפיליות מסתוריות או אטמוספרות של כוכבי לכת זרים, מבלי לעזוב את כדור הארץ? האם ייתכן "לשקול" ולהכיר חומרים רק באמצעות ניתוח האור שהם פולטים או בולעים? בואו נגלה בעצמון!

<div class="spectrometer-app">
    <div class="controls-panel">
        <div class="control-group">
            <label for="element-select" class="control-label">בחרו יסוד:</label>
            <div class="select-wrapper">
                 <select id="element-select">
                    <option value="hydrogen">מימן (Hydrogen)</option>
                    <option value="helium">הליום (Helium)</option>
                    <option value="lithium">ליתיום (Lithium)</option>
                    <option value="sodium">נתרן (Sodium)</option>
                    <option value="neon">נאון (Neon)</option>
                </select>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label">בחרו מצב ניתוח:</label>
            <div class="radio-group">
                <input type="radio" id="mode-emission" name="mode" value="emission" checked>
                <label for="mode-emission">פליטה (גז חם/מעורר)</label>
                <input type="radio" id="mode-absorption" name="mode" value="absorption">
                <label for="mode-absorption">בליעה (גז קר מול מקור רציף)</label>
            </div>
        </div>
    </div>

    <div class="animation-stage">
        <!-- Elements for animation flow -->
        <div class="light-source emission">גז חם פולט</div>
        <div class="light-source absorption">מקור אור רציף</div>

        <!-- Animated light path -->
        <div class="light-beam beam-source-to-gas"></div>

        <div class="gas-cloud">
            <span class="element-symbol">H</span>
            <span class="element-full-name">מימן</span>
        </div>
         <div class="gas-interaction-effect"></div>

        <div class="light-beam beam-gas-to-spectrometer"></div>

        <div class="spectrometer-prism">
            <div class="prism-shape"></div>
             <span class="spectrometer-label">ספקטרומטר</span>
        </div>

        <div class="spectrum-output">
            <div class="spectrum-bar"></div>
            <div class="spectral-lines"></div>
             <div class="spectrum-reveal-overlay"></div>
        </div>
    </div>

    <button id="toggle-explanation" class="explanation-button">הצגת רקע והסבר מורחב</button>
</div>


<style>
    :root {
        --primary-color: #5e35b1; /* Deep Purple */
        --secondary-color: #e0e0e0; /* Light Gray */
        --background-color: #f5f5f5; /* Very Light Gray */
        --card-background: #ffffff; /* White */
        --text-color: #333; /* Dark Gray */
        --border-color: #cccccc; /* Gray */
        --spectrum-height: 80px;
        --beam-color: rgba(255, 255, 255, 0.8);
        --beam-width: 8px;
        --speed-fast: 0.8s;
        --speed-medium: 1.5s;
        --speed-slow: 2s;
    }

    .spectrometer-app {
        direction: rtl;
        font-family: 'Arial', sans-serif;
        padding: 30px;
        border: 1px solid var(--border-color);
        border-radius: 12px;
        margin-bottom: 30px;
        background-color: var(--card-background);
        color: var(--text-color);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

    .controls-panel {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin-bottom: 30px;
        justify-content: center;
        padding: 15px;
        background-color: var(--background-color);
        border-radius: 8px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }

    .control-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .control-label {
        font-size: 1em;
        margin-bottom: 8px;
        color: var(--primary-color);
        font-weight: bold;
    }

    .select-wrapper select {
        padding: 10px 15px;
        border: 1px solid var(--border-color);
        border-radius: 5px;
        background-color: white;
        font-size: 1em;
        cursor: pointer;
        outline: none;
        appearance: none; /* Remove default arrow */
        background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23666666%22%20d%3D%22M287%2C114.7L159.3%2C23.4c-5.3-4.2-12.9-4.2-18.2%2C0l-128.7%2C91.3c-6.5%2C4.6-7.9%2C14.5-3.5%2C21c4.4%2C6.5%2C14.3%2C7.9%2C20.8%2C3.5l118.2-83.9l118.2%2C83.9c6.5%2C4.6%2C16.4%2C3.2%2C20.8-3.5C294.9%2C129.2%2C293.5%2C119.3%2C287%2C114.7z%22%2F%3E%3C%2Fsvg%3E');
        background-repeat: no-repeat;
        background-position: left 15px center; /* Position arrow on the left for RTL */
        background-size: 12px;
        padding-left: 35px; /* Make space for arrow */
    }

     .select-wrapper select:focus {
         border-color: var(--primary-color);
         box-shadow: 0 0 5px rgba(var(--primary-color), 0.5);
     }


    .radio-group {
        display: flex;
        gap: 15px;
        align-items: center;
    }

    .radio-group input[type="radio"] {
        /* Hide default radio */
        position: absolute;
        opacity: 0;
        pointer-events: none;
    }

    .radio-group label {
        display: inline-block;
        padding: 8px 15px;
        border: 1px solid var(--border-color);
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.95em;
        background-color: white;
    }

    .radio-group input[type="radio"]:checked + label {
        background-color: var(--primary-color);
        color: white;
        border-color: var(--primary-color);
        box-shadow: 0 2px 5px rgba(var(--primary-color), 0.3);
    }

    .radio-group label:hover {
         border-color: var(--primary-color);
    }

    .animation-stage {
        display: flex;
        align-items: center;
        /* justify-content: space-between; /* Distribute space */
        gap: 10px; /* Adjust gap */
        height: 150px; /* Increased height */
        position: relative;
        margin-bottom: 30px;
        background-color: var(--background-color);
        border-radius: 8px;
        padding: 20px;
        overflow: hidden; /* Hide beams outside */
    }

    .light-source {
        padding: 8px 15px;
        border-radius: 20px; /* Pill shape */
        font-size: 0.9em;
        white-space: nowrap;
        flex-shrink: 0; /* Prevent shrinking */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        position: relative;
        z-index: 2;
    }

    .light-source.emission {
        background-color: #ff7f00; /* Warm color */
        color: white;
    }

    .light-source.absorption {
        background-color: #ffffff; /* White */
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }

    /* Beams - Initially hidden or reset */
    .light-beam {
        position: absolute;
        height: var(--beam-width);
        background: linear-gradient(to left, var(--beam-color), transparent); /* Fade effect */
        z-index: 1;
        opacity: 0; /* Start hidden */
        transform: translateX(0); /* Reset transform */
    }

    .beam-source-to-gas {
         right: 160px; /* Position based on light source width + padding */
         width: 100px; /* Initial width */
         top: calc(50% - var(--beam-width) / 2);
    }

    .beam-gas-to-spectrometer {
        right: calc(160px + 100px + 10px); /* Position after gas cloud */
        width: 100px;
        top: calc(50% - var(--beam-width) / 2);
    }

    /* Animation Keyframes */
    @keyframes flowLightRTL {
        0% { opacity: 1; transform: translateX(0); }
        80% { opacity: 1; transform: translateX(-100px); } /* Move 100px left */
        100% { opacity: 0; transform: translateX(-100px); }
    }
    @keyframes flowLightRTLShort {
         0% { opacity: 1; transform: translateX(0); }
         80% { opacity: 1; transform: translateX(-80px); } /* Move slightly less */
         100% { opacity: 0; transform: translateX(-80px); }
    }


    .spectrometer-app.animate .light-beam.beam-source-to-gas {
        animation: flowLightRTL var(--speed-medium) ease-out forwards;
    }
     .spectrometer-app.animate .light-beam.beam-gas-to-spectrometer {
         animation: flowLightRTLShort var(--speed-slow) ease-out var(--speed-fast) forwards; /* Start after first beam hits gas */
     }


    .gas-cloud {
        width: 100px; /* Increased size */
        height: 100px;
        background: radial-gradient(circle, rgba(94, 53, 177, 0.3) 0%, rgba(94, 53, 177, 0) 70%); /* Use primary color */
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-size: 0.9em;
        text-align: center;
        position: relative;
        z-index: 2;
        flex-shrink: 0;
        border: 1px solid rgba(94, 53, 177, 0.5); /* Subtle border */
    }

    .element-symbol {
        font-size: 2em;
        font-weight: bold;
        color: var(--primary-color);
        margin-bottom: 2px;
    }
    .element-full-name {
        font-size: 0.8em;
        color: var(--text-color);
    }

    .gas-interaction-effect {
         position: absolute;
         width: 120px;
         height: 120px;
         border-radius: 50%;
         background-color: rgba(var(--primary-color), 0.5); /* Pulsing effect */
         opacity: 0;
         z-index: 3;
         transform: scale(0);
    }

    @keyframes gasPulse {
        0% { opacity: 0.6; transform: scale(0.8); }
        50% { opacity: 0; transform: scale(1.2); }
        100% { opacity: 0; transform: scale(1.2); } /* Stay hidden */
    }

    .spectrometer-app.animate .gas-interaction-effect {
        animation: gasPulse var(--speed-fast) ease-out var(--speed-medium) forwards; /* Pulse when beam hits */
    }


    .spectrometer-prism {
        width: 80px; /* Increased size */
        height: 80px;
        position: relative;
        z-index: 2;
        flex-shrink: 0;
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         padding-left: 10px; /* Space for shape */
    }

    .prism-shape {
        width: 100%;
        height: 100%;
        background-color: #b0bec5; /* Grayish blue */
        clip-path: polygon(0% 0%, 100% 50%, 0% 100%); /* Prism shape */
        position: absolute;
        top: 0;
        right: 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
     .spectrometer-label {
         position: absolute;
         font-size: 0.7em;
         color: white;
         z-index: 1;
         left: 5px; /* Position text on the prism */
         transform: translateY(-50%);
         top: 50%;
         font-weight: bold;
     }


    .spectrum-output {
        flex-grow: 1; /* Take remaining space */
        height: var(--spectrum-height);
        border: 1px solid var(--border-color);
        position: relative;
        overflow: hidden;
        border-radius: 5px;
        background-color: black; /* Default black for emission */
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2);
    }

     .mode-absorption .spectrum-output {
         background-color: transparent; /* Transparent for absorption to show gradient */
     }


    .spectrum-bar {
        position: absolute;
        top: 0;
        right: 0; /* Start from right for RTL */
        bottom: 0;
        left: 0;
        background: linear-gradient(to left, red, orange, yellow, green, blue, indigo, violet); /* Visible spectrum colors RTL */
        background-size: 100% 100%;
        transition: opacity var(--speed-medium) ease-out;
        opacity: 1; /* Default visible */
    }

    .mode-emission .spectrum-bar {
        opacity: 0; /* Hide continuous spectrum in emission mode */
    }

    .spectrum-output .spectral-lines {
        position: absolute;
        top: 0;
        right: 0; /* Lines positioned from the right */
        bottom: 0;
        left: 0;
        z-index: 3; /* Above the spectrum bar and overlay */
        pointer-events: none; /* Lines shouldn't block interaction */
        transition: opacity var(--speed-medium) ease-out var(--speed-slow); /* Fade in lines after spectrum appears */
        opacity: 0;
    }

     .spectrometer-app.animate .spectral-lines {
         opacity: 1; /* Reveal lines when animating */
     }


    .spectral-line {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 2px; /* Default width */
        background-color: black; /* Default black for absorption */
        transition: right var(--speed-fast) ease-out, background-color var(--speed-fast) ease-out, width 0.3s ease, box-shadow 0.3s ease; /* Smooth transitions */
    }

    .mode-emission .spectral-line {
        width: 3px; /* Wider for emission lines */
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.8); /* Default glow, will be overridden by JS color */
    }

     .mode-emission .spectral-line[style*="background-color: rgb(255, 0, 0)"] { box-shadow: 0 0 6px rgba(255, 0, 0, 0.8); }
     .mode-emission .spectral-line[style*="background-color: rgb(0, 255, 255)"] { box-shadow: 0 0 6px rgba(0, 255, 255, 0.8); }
     .mode-emission .spectral-line[style*="background-color: rgb(0, 0, 255)"] { box-shadow: 0 0 6px rgba(0, 0, 255, 0.8); }
     .mode-emission .spectral-line[style*="background-color: rgb(75, 0, 130)"] { box-shadow: 0 0 6px rgba(75, 0, 130, 0.8); } /* Indigo */
     .mode-emission .spectral-line[style*="background-color: rgb(255, 165, 0)"] { box-shadow: 0 0 6px rgba(255, 165, 0, 0.8); } /* Orange */
     .mode-emission .spectral-line[style*="background-color: rgb(255, 255, 0)"] { box-shadow: 0 0 6px rgba(255, 255, 0, 0.8); } /* Yellow */
     .mode-emission .spectral-line[style*="background-color: rgb(0, 128, 0)"] { box-shadow: 0 0 6px rgba(0, 128, 0, 0.8); } /* Green */
     .mode-emission .spectral-line[style*="background-color: rgb(255, 69, 0)"] { box-shadow: 0 0 6px rgba(255, 69, 0, 0.8); } /* Red-Orange */
     .mode-emission .spectral-line[style*="background-color: rgb(255, 99, 71)"] { box-shadow: 0 0 6px rgba(255, 99, 71, 0.8); } /* Tomato */
     .mode-emission .spectral-line[style*="background-color: rgb(255, 127, 80)"] { box-shadow: 0 0 6px rgba(255, 127, 80, 0.8); } /* Coral */


    .mode-emission .light-source.absorption,
    .mode-absorption .light-source.emission {
        display: none;
    }

     /* Spectrum reveal animation */
     .spectrum-reveal-overlay {
         position: absolute;
         top: 0;
         right: 0;
         bottom: 0;
         left: 0;
         background-color: var(--card-background); /* Match app background initially */
         z-index: 4; /* Above lines initially */
         transition: transform var(--speed-slow) ease-out var(--speed-slow); /* Start transform after beams */
         transform-origin: right center; /* Reveal from the right */
         transform: scaleX(1); /* Fully cover initially */
     }
      .spectrometer-app.animate .spectrum-reveal-overlay {
          transform: scaleX(0); /* Scale down to reveal */
      }
     .spectrometer-app.animate .spectrum-reveal-overlay.hide {
         /* This class helps ensure it stays hidden after animation */
         display: none;
     }


    #explanation {
        display: none; /* Hidden by default */
        border: 1px solid var(--border-color);
        padding: 30px;
        margin-top: 20px;
        background-color: var(--background-color);
        border-radius: 8px;
        direction: rtl;
        line-height: 1.7;
        color: var(--text-color);
    }

    #explanation h2 {
        margin-top: 0;
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 15px;
        margin-bottom: 20px;
    }

     #explanation h3 {
         color: #673ab7; /* Slightly lighter purple */
         margin-top: 25px;
         margin-bottom: 10px;
         border-right: 3px solid #d1c4e9; /* Light purple marker */
         padding-right: 8px;
     }

     #explanation p {
         margin-bottom: 15px;
     }

     #explanation ul {
         margin-bottom: 15px;
         padding-right: 20px;
     }

     #explanation li {
         margin-bottom: 8px;
     }

    .explanation-button {
        display: block;
        margin: 30px auto 0;
        padding: 12px 25px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        background-color: var(--primary-color);
        color: white;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.3s ease, transform 0.1s ease;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }

    .explanation-button:hover {
        background-color: #7e57c2; /* Lighter purple */
    }

     .explanation-button:active {
         transform: scale(0.98);
     }


    /* Responsive adjustments */
    @media (max-width: 768px) {
        .spectrometer-app {
            padding: 15px;
        }
        .controls-panel {
            flex-direction: column;
            gap: 20px;
        }
        .animation-stage {
            flex-direction: column;
            height: auto;
            padding: 15px;
             gap: 15px;
        }
         .light-source, .gas-cloud, .spectrometer-prism {
             margin: 0 auto; /* Center elements */
         }

         .light-beam {
             /* Adjust beam positioning for vertical flow if needed, or simplify */
             /* For this simple animation, keeping horizontal might be ok but less realistic */
             /* Let's hide beams on small screens for simplicity, or make them static indicators */
             display: none; /* Hide beams on small screens for simplicity */
         }

         .gas-interaction-effect {
             /* Adjust positioning if beams hidden */
              top: initial; bottom: initial; left: initial; right: initial;
              position: relative; /* Change positioning */
              margin-top: -10px; /* Overlap slightly */
         }
         .spectrometer-prism {
             padding-left: 0; /* Center label */
         }
         .spectrometer-label {
             left: 50%;
             transform: translate(-50%, -50%);
         }
         .spectrum-output {
             width: 100%; /* Full width */
             flex-grow: 0;
         }

    }
</style>

<div id="explanation">
    <h2>הסבר: ספקטרוסקופיה - האור שמספר סיפור</h2>

    <h3>מהו אור ואיך הוא נפרד לצבעים? (ספקטרום)</h3>
    <p>האור שאנו רואים הוא למעשה גל אלקטרומגנטי, סוג של אנרגיה המתפשטת במרחב. "אור לבן" - כמו אור שמש או אור מנורה - אינו צבע אחד, אלא אוסף של כל הצבעים הנראים (קשת הצבעים), שלכל אחד מהם "אורך גל" שונה. ספקטרוסקופ (או פריזמה פשוטה) הוא מכשיר שיודע לפרק את האור ה"לבן" לרכיביו לפי אורכי גל, וליצור את רצועת הצבעים המוכרת שנקראת <strong>ספקטרום רציף</strong>.</p>

    <h3>אטומים ואנרגיה: הקשר לאור</h3>
    <p>בתוך כל יסוד (כמו מימן, חמצן או ברזל), האלקטרונים שמקיפים את גרעין האטום אינם יכולים להימצא בכל מקום סתם כך. הם מוגבלים לרמות אנרגיה מדויקות וספציפיות, כמו מדרגות בסולם. אלקטרון יכול לעלות או לרדת במדרגות האנרגיה הללו רק על ידי קליטה או שחרור של מנות אנרגיה מדויקות - "פוטונים". כל פוטון נושא איתו כמות אנרגיה מסוימת, שמתאימה לצבע (אורך גל) מסוים של אור.</p>
    <ul>
        <li>כשאטום <strong>חם</strong> או <strong>מעורר אנרגטית</strong>, האלקטרונים שלו קופצים לרמות גבוהות יותר. כשהם חוזרים לרמות נמוכות יותר, הם משחררים את עודף האנרגיה שלהם בצורת פוטונים - כלומר, הם <strong>פולטים אור</strong> בצבעים מאוד ספציפיים שתואמים להפרשי האנרגיה בין המדרגות.</li>
        <li>כשאור לבן <strong>רציף</strong> עובר דרך גז <strong>קר</strong>, האלקטרונים באטומי הגז יכולים <strong>לבלוע</strong> רק את הפוטונים שהאנרגיה שלהם מתאימה בדיוק להפרש בין רמות האנרגיה שלהם. האור בצבעים אלו "נאכל" על ידי הגז, והם חסרים בספקטרום הסופי.</li>
    </ul>


    <h3>"טביעת האצבע" הייחודית של כל יסוד</h3>
    <p>מכיוון שהמבנה של כל אטום והמדרגות האנרגטיות הייחודיות לו שונות מיסוד ליסוד, גם הפרשי האנרגיה האפשריים בין המדרגות שונים. לכן, כל יסוד בולע או פולט אור רק באורכי גל (צבעים) מאוד ספציפיים וקבועים לו. התבנית הזו של קווי אור ספציפיים (או קווי חושך בספקטרום רציף) היא כמו "טביעת אצבע" כימית - היא ייחודית לכל יסוד ומאפשרת לזהות אותו בוודאות.</p>

    <h3>ספקטרום פליטה מול ספקטרום בליעה</h3>
    <ul>
        <li><strong>ספקטרום פליטה:</strong> מתקבל כשאור מגיע ישירות מגז חם או פלזמה (כמו בנורות ניאון או בשמש עצמה). רואים קווים <strong>צבעוניים בהירים</strong> על רקע <strong>שחור</strong>. אלו הצבעים שהאטומים בגז פולטים.</li>
        <li><strong>ספקטרום בליעה:</strong> מתקבל כשאור רציף (ממקור חם מאוד וצפוף, כמו ליבת כוכב) עובר דרך גז <strong>קר יותר</strong> (כמו האטמוספרה של הכוכב). רואים קווים <strong>שחורים</strong> על רקע <strong>ספקטרום צבעוני רציף</strong>. הקווים השחורים הם הצבעים שהאטומים בגז הקר יותר בלעו.</li>
    </ul>
    <p>הדבר המדהים הוא שמיקומי הקווים הצבעוניים בספקטרום הפליטה של יסוד מסוים תואמים בדיוק למיקומי הקווים השחורים בספקטרום הבליעה של אותו יסוד!</p>

    <h3>למה זה חשוב? ספקטרוסקופיה בעולם האמיתי</h3>
    <p>ספקטרוסקופיה היא אחד הכלים החזקים ביותר במדע:</p>
    <ul>
        <li><strong>באסטרונומיה:</strong> מאפשרת לדעת ממה עשויים כוכבים רחוקים, גלקסיות וערפיליות (מימן, הליום, ברזל וכו'), מה הטמפרטורה והלחץ שלהם, ואפילו אם הם נעים אלינו או מתרחקים מאיתנו (באמצעות ניתוח הסטה של הקווים עקב אפקט דופלר).</li>
        <li><strong>בכימיה ובביולוגיה:</strong> משמשת לזיהוי חומרים שונים, ניתוח מבנה מולקולרי, ובדיקות רפואיות.</li>
        <li><strong>בתעשייה:</strong> לבקרת איכות, זיהוי זיהומים, ופיתוח חומרים חדשים.</li>
    </ul>
    <p>היכולת לנתח אור פותחת חלון אל היקום, מאפשרת לנו להבין את ההרכב של כוכבים שנוצרו לפני מיליארדי שנים, ולפתח טכנולוגיות חדשות כאן על כדור הארץ - והכל מתבסס על "טביעות האצבע" הייחודיות של היסודות!</p>
</div>

<script>
    const elementSelect = document.getElementById('element-select');
    const modeEmission = document.getElementById('mode-emission');
    const modeAbsorption = document.getElementById('mode-absorption');
    const spectralLinesContainer = document.querySelector('.spectral-lines');
    const explanationDiv = document.getElementById('explanation');
    const toggleButton = document.getElementById('toggle-explanation');
    const animationStage = document.querySelector('.animation-stage'); // Use animation-stage
    const appContainer = document.querySelector('.spectrometer-app'); // Main container for animation class
    const elementSymbol = document.querySelector('.element-symbol');
    const elementFullName = document.querySelector('.element-full-name');
    const spectrumRevealOverlay = document.querySelector('.spectrum-reveal-overlay');

    // Simplified spectral data: Position is percentage from the RIGHT (due to RTL).
    // Color is for emission mode. Black is used for absorption lines.
    // Added element symbol and full name for display.
    const spectralData = {
        hydrogen: {
            symbol: 'H',
            name: 'מימן',
            emission: [
                { pos: 85, color: '#FF0000' }, // H-alpha (Red)
                { pos: 75, color: '#00FFFF' }, // H-beta (Cyan)
                { pos: 70, color: '#0000FF' }, // H-gamma (Blue)
                { pos: 55, color: '#4B0082' }  // H-delta (Indigo/Violet) - simplified positions
            ],
            absorption: [
                { pos: 85, color: 'black' },
                { pos: 75, color: 'black' },
                { pos: 70, color: 'black' },
                { pos: 55, color: 'black' }
            ]
        },
        helium: {
            symbol: 'He',
            name: 'הליום',
            emission: [
                { pos: 90, color: '#FFA500' }, // Orange
                { pos: 80, color: '#FFFF00' }, // Yellow
                { pos: 65, color: '#008000' }, // Green
                { pos: 50, color: '#4B0082' }  // Indigo
            ], // Simplified, representative lines
            absorption: [
                { pos: 90, color: 'black' },
                { pos: 80, color: 'black' },
                { pos: 65, color: 'black' },
                { pos: 50, color: 'black' }
            ]
        },
        lithium: {
             symbol: 'Li',
             name: 'ליתיום',
             emission: [{ pos: 67, color: '#FF0000' }], // Simplified, main line (Red)
             absorption: [{ pos: 67, color: 'black' }]
        },
        sodium: {
             symbol: 'Na',
             name: 'נתרן',
             emission: [{ pos: 58, color: '#FFFF00' }, { pos: 59, color: '#FFFF00' }], // Famous doublet (Yellow)
             absorption: [{ pos: 58, color: 'black' }, { pos: 59, color: 'black' }]
        },
        neon: {
             symbol: 'Ne',
             name: 'נאון',
             emission: [
                 { pos: 92, color: '#FF4500' }, // OrangeRed
                 { pos: 88, color: '#FF6347' }, // Tomato
                 { pos: 83, color: '#FF7F50' }, // Coral
                 { pos: 79, color: '#FF8C00' }, // DarkOrange
                 { pos: 62, color: '#FFFF00' }  // Yellow
            ], // Many lines, simplify to a few prominent ones
             absorption: [
                 { pos: 92, color: 'black' },
                 { pos: 88, color: 'black' },
                 { pos: 83, color: 'black' },
                 { pos: 79, color: 'black' },
                 { pos: 62, color: 'black' }
            ]
        }
    };

    function updateSpectrum() {
        const selectedElementKey = elementSelect.value;
        const selectedMode = modeEmission.checked ? 'emission' : 'absorption';
        const elementData = spectralData[selectedElementKey];
        const lines = elementData[selectedMode];

        // Update gas cloud label
        elementSymbol.textContent = elementData.symbol;
        elementFullName.textContent = elementData.name;


        // Clear previous lines
        spectralLinesContainer.innerHTML = '';

        // Set mode class for CSS
        animationStage.classList.remove('mode-emission', 'mode-absorption');
        animationStage.classList.add(`mode-${selectedMode}`);

        // Reset animation state and start animation
        appContainer.classList.remove('animate');
         // Force reflow to restart CSS animations
        void appContainer.offsetWidth;
        appContainer.classList.add('animate');


        // Add new lines with a slight delay to match spectrum reveal animation
        // Wait for spectrum reveal overlay to start hiding
        setTimeout(() => {
            lines.forEach(line => {
                const lineDiv = document.createElement('div');
                lineDiv.classList.add('spectral-line');
                // Position from the right (RTL)
                lineDiv.style.right = `${line.pos}%`;
                // Set color for emission, black for absorption
                lineDiv.style.backgroundColor = selectedMode === 'emission' ? line.color : 'black';
                 // No need to set width/shadow here, CSS handles it based on mode

                spectralLinesContainer.appendChild(lineDiv);
            });
        }, parseFloat(getComputedStyle(spectrumRevealOverlay).transitionDuration) * 1000 + parseFloat(getComputedStyle(spectrumRevealOverlay).transitionDelay) * 1000 - 100); // Add lines slightly before overlay finishes


         // Hide overlay completely after animation
         spectrumRevealOverlay.addEventListener('transitionend', function handler() {
             if (appContainer.classList.contains('animate')) { // Only hide if we just finished an animation
                 spectrumRevealOverlay.classList.add('hide');
             }
              spectrumRevealOverlay.removeEventListener('transitionend', handler);
         });

         // In case of rapid changes, ensure overlay is visible before restart
         spectrumRevealOverlay.classList.remove('hide');
         spectrumRevealOverlay.style.transform = 'scaleX(1)'; // Reset transform
         // Force reflow
         void spectrumRevealOverlay.offsetWidth;


    }

    function toggleExplanation() {
        const isHidden = explanationDiv.style.display === 'none' || explanationDiv.style.display === '';
        explanationDiv.style.display = isHidden ? 'block' : 'none';
        toggleButton.textContent = isHidden ? 'הסתר רקע והסבר מורחב' : 'הצגת רקע והסבר מורחב';
    }

    // Add event listeners
    elementSelect.addEventListener('change', updateSpectrum);
    modeEmission.addEventListener('change', updateSpectrum);
    modeAbsorption.addEventListener('change', updateSpectrum);
    toggleButton.addEventListener('click', toggleExplanation);

    // Initial update on page load
    updateSpectrum();

</script>
```