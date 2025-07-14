---
title: "שעון אטומי: מכונת הזמן המדויקת ביותר בעולם"
english_slug: what-makes-an-atomic-clock-so-accurate
category: "מדעים מדויקים / פיזיקה"
tags: ["שעון אטומי", "פיזיקה אטומית", "מדידת זמן", "תהודה קוונטית", "טכנולוגיה"]
---
# שעון אטומי: מכונת הזמן המדויקת ביותר בעולם

שעונים אטומיים אינם רק שעונים – הם תקני הזמן היציבים והמדויקים ביותר שהאנושות יצרה אי פעם. הם עומדים בבסיס טכנולוגיות קריטיות כמו GPS, תקשורת מודרנית, וסנכרון רשתות עולמיות. אבל מה סוד הדיוק המדהים שלהם, ואיך יצורים זעירים כמו אטומים עוזרים לנו למדוד את זרימת הזמן בדיוק שאין לו אח ורע?

בואו נתנסה בלב הפועם של שעון אטומי, ונבין כיצד הוא "מקשיב" ל"פעימות" הטבעיות והקבועות של אטום הצסיום כדי לשמור על קצב מושלם.

<div id="atomic-clock-app">
    <h2 class="app-title">סימולציית ליבת שעון אטומי (מבוסס צסיום)</h2>

    <div class="clock-diagram">
        <div class="component source" title="מקור אטומים מחומם">מקור אטומים (צסיום)</div>
        <div class="beam beam-in">
            <div class="atom" style="--delay: 0s;"></div>
            <div class="atom" style="--delay: 0.5s;"></div>
            <div class="atom" style="--delay: 1s;"></div>
            <div class="atom" style="--delay: 1.5s;"></div>
            <div class="atom" style="--delay: 2s;"></div>
        </div>
        <div class="component cavity" title="חלל אינטראקציה עם מיקרוגל">
            חלל מיקרוגל
            <div class="microwave-field"></div>
            <div class="microwave-label">תדר: <span id="freq-display">9,192,631,770</span> הרץ</div>
        </div>
        <div class="beam beam-out">
             <div class="atom state-changed" style="--delay: 0s;"></div>
             <div class="atom state-changed" style="--delay: 0.5s;"></div>
             <div class="atom state-changed" style="--delay: 1s;"></div>
             <div class="atom state-changed" style="--delay: 1.5s;"></div>
             <div class="atom state-changed" style="--delay: 2s;"></div>
        </div>
        <div class="component detector" title="גלאי אטומים במצב אנרגטי ספציפי">
            גלאי אטומים
            <div class="detector-output">זוהו אטומים: <span id="detected-count">0</span></div>
            <div class="detector-peak-indicator">▲</div>
        </div>
    </div>

    <div class="controls">
        <h3 class="controls-title">כוונון תדר המיקרוגל: מצא את תדר התהודה האטומי!</h3>
        <input type="range" id="frequency-slider" min="9192631700" max="9192631840" value="9192631770" step="1">
        <div class="freq-labels">
            <span>תדר נמוך</span>
            <span>9,192,631,770 הרץ (התדר המדויק!)</span>
            <span>תדר גבוה</span>
        </div>
        <p class="hint">נענעו את המחוון כדי למצוא את התדר שגורם למקסימום אטומים לשנות מצב ולהגיע לגלאי.</p>
        <button id="auto-tune-button" class="control-button">כוונון אוטומטי (הפעלת לולאת המשוב)</button>
    </div>

    <div class="feedback-loop">
        <h3 class="loop-title">לולאת משוב: כך השעון "שומר" על התדר הנכון</h3>
        <div class="component oscillator" title="מייצר את גלי המיקרוגל">מתנד אלקטרוני</div>
        <div class="arrow">→</div>
        <div class="component signal-processor" title="מנתח את האות מהגלאי">מעבד אות</div>
        <div class="arrow">→</div>
        <div class="component control-loop" title="משנה את תדר המתנד">לולאת בקרה</div>
         <div class="arrow feedback-arrow">↩</div>
        <div class="lock-status">סטטוס נעילה: <span id="lock-indicator">מכוון ידנית</span></div>
    </div>

    <div class="time-counter">
        <h3 class="counter-title">מונה זמן (פועל כשהתדר נעול)</h3>
        <div class="counter-display"><span id="seconds-counter">0</span> שניות</div>
        <p class="counter-info">כל שנייה כאן מייצגת מיליארדי מחזורי מיקרוגל בתדר הנעול.</p>
    </div>
</div>

<style>
    #atomic-clock-app {
        font-family: 'Heebo', sans-serif; /* Using Heebo for better Hebrew support and modern feel */
        background: linear-gradient(to bottom right, #e0f7fa, #b2ebf2);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 30px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }

     #atomic-clock-app::before {
        content: '';
        position: absolute;
        top: -50px;
        right: -50px;
        width: 150px;
        height: 150px;
        background: rgba(0, 188, 212, 0.3);
        border-radius: 50%;
        filter: blur(30px);
        z-index: 0;
     }

    .app-title, .controls-title, .loop-title, .counter-title {
        color: #00796b; /* Dark Teal */
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }

    .clock-diagram {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        flex-wrap: wrap;
        gap: 15px; /* Space between components */
        position: relative;
    }

    .component {
        border: 1px solid #b2ebf2; /* Light Cyan */
        padding: 15px 20px;
        border-radius: 8px;
        text-align: center;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        min-width: 100px; /* Ensure minimum width */
        font-size: 0.9em;
        position: relative;
        z-index: 1;
    }

    .component:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .source { background-color: #c8e6c9; border-color: #a5d6a7; } /* Light Green */
    .detector { background-color: #ffccbc; border-color: #ffab91; } /* Light Orange */
    .cavity {
         background-color: #bbdefb; /* Light Blue */
         border-color: #90caf9;
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         min-height: 90px;
         position: relative;
         overflow: hidden; /* Hide field animation overflow */
    }
     .cavity::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(0, 150, 136, 0.2) 0%, rgba(0, 150, 136, 0) 70%);
        opacity: 0; /* Hidden by default */
        transition: opacity 0.5s ease;
     }
    .cavity.resonant::before {
        opacity: 1; /* Visible when close to resonance */
        animation: pulse-light 1.5s infinite;
    }

    @keyframes pulse-light {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    .microwave-field {
         width: 60px;
         height: 60px;
         background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M0 50 Q25 25 50 50 T100 50" fill="none" stroke="%23009688" stroke-width="10" stroke-linecap="round"/></svg>'); /* Teal wave */
         background-size: contain;
         background-repeat: no-repeat;
         animation: microwave-wave 2s linear infinite;
         opacity: 0.8;
    }

    @keyframes microwave-wave {
        0% { transform: translateX(0); }
        100% { transform: translateX(0); } /* Static wave icon, animation handled by parent glow */
    }

    .microwave-label {
        font-size: 0.85em;
        margin-top: 8px;
        color: #0277bd; /* Deep Sky Blue */
        font-weight: bold;
    }
     #freq-display {
         color: #01579b; /* Dark Blue */
     }


    .beam {
         flex-grow: 1;
         border: none;
         background: none;
         position: relative;
         height: 30px; /* Give space for atoms */
         overflow: hidden;
         display: flex;
         align-items: center;
         justify-content: center;
         margin: 0 10px; /* Space around beam */
         min-width: 50px;
    }
     .beam-in::before {
        content: '◀'; /* Right arrow for RTL */
        position: absolute;
        left: 10px; /* Adjust arrow position */
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.5em;
        color: #555;
         z-index: 1;
     }
      .beam-out::before {
        content: '◀'; /* Right arrow for RTL */
        position: absolute;
        left: 10px; /* Adjust arrow position */
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.5em;
        color: #555;
         z-index: 1;
     }


    .atom {
        position: absolute;
        width: 6px;
        height: 6px;
        background-color: #333; /* Dark gray for initial state */
        border-radius: 50%;
        top: 50%;
        transform: translateY(-50%);
        right: 0; /* Start from right for RTL */
        animation: moveAtomRTL 3s linear infinite;
        animation-delay: var(--delay);
         box-shadow: 0 0 3px rgba(0,0,0,0.5);
    }

     .beam-in .atom {
         background-color: #555; /* Default atom color */
     }

    /* Simulate state change in beam-out */
    .beam-out .atom.state-changed {
         background-color: #e57373; /* Light Red - signifies changed state */
         box-shadow: 0 0 5px #e57373;
         transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }


    @keyframes moveAtomRTL {
        0% { right: -10%; opacity: 0; } /* Start slightly outside and invisible */
        10% { opacity: 1; } /* Become visible */
        90% { opacity: 1; } /* Stay visible */
        100% { right: 110%; opacity: 0; } /* Move across and exit */
    }


    .detector-output {
        font-weight: bold;
        margin-top: 8px;
        font-size: 1.1em;
        color: #d32f2f; /* Red */
    }

    .detector-peak-indicator {
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 1.5em;
        color: gold; /* Gold indicator */
        opacity: 0; /* Hidden by default */
        transition: opacity 0.3s ease;
        text-shadow: 0 0 5px rgba(255, 215, 0, 0.8);
    }

    .detector-peak-indicator.active {
        opacity: 1; /* Visible when at peak */
        animation: peak-bounce 0.8s ease-out;
    }
     @keyframes peak-bounce {
        0% { transform: translateX(-50%) translateY(0); }
        50% { transform: translateX(-50%) translateY(-15px); }
        100% { transform: translateX(-50%) translateY(0); }
     }


    .controls {
        margin-bottom: 30px;
        padding: 20px;
        border: 1px solid #b2ebf2;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #frequency-slider {
        width: 100%;
        margin-top: 15px;
        -webkit-appearance: none;
        appearance: none;
        height: 8px;
        background: #e0e0e0;
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
        border-radius: 4px;
    }

    #frequency-slider:hover {
        opacity: 1;
    }

    #frequency-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: #00796b; /* Dark Teal */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    #frequency-slider::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: #00796b; /* Dark Teal */
        cursor: pointer;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    .freq-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.75em;
        color: #555;
        margin-top: 5px;
    }

    .hint {
        text-align: center;
        font-size: 0.9em;
        color: #444;
        margin-top: 15px;
    }

     .control-button {
        display: block;
        width: fit-content;
        margin: 15px auto 0;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
        background-color: #0288d1; /* Light Blue */
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
         box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
     .control-button:hover {
         background-color: #039be5; /* Darker Light Blue */
         transform: translateY(-1px);
     }
     .control-button:active {
         background-color: #0277bd; /* Even Darker Blue */
         transform: translateY(0);
         box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
     }


    .feedback-loop {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #b2ebf2;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        flex-wrap: wrap;
        gap: 10px; /* Space between loop components */
    }

    .feedback-loop .component {
        border: 1px dashed #80cbc4; /* Light Teal */
        padding: 10px 15px;
        margin: 0; /* Removed margin for gap */
        background-color: #e0f2f7; /* Extra Light Cyan */
        min-width: 80px;
        font-size: 0.8em;
         transition: border-color 0.3s ease, background-color 0.3s ease;
    }
    .feedback-loop .component.active {
        border-color: #00796b; /* Dark Teal */
        background-color: #b2ebf2; /* Light Cyan */
        box-shadow: 0 0 8px rgba(0, 121, 107, 0.3);
    }


    .arrow {
        font-size: 1.8em; /* Larger arrows */
        margin: 0 8px; /* Space around arrows */
        color: #00796b; /* Dark Teal */
        font-weight: bold;
         transition: color 0.3s ease;
    }
     .arrow.feedback-arrow {
         transform: rotate(90deg); /* Rotation for feedback arrow */
         margin-top: 10px; /* Space below feedback arrow */
         margin-bottom: 10px;
         color: #0288d1; /* Light Blue for feedback */
     }

    .lock-status {
        font-weight: bold;
        margin-right: 20px; /* Space to the left in RTL */
        color: #757575; /* Gray */
        font-size: 1em;
    }

    .lock-status #lock-indicator.locked {
        color: #388e3c; /* Dark Green */
        animation: pulse-text 1s infinite;
    }
     @keyframes pulse-text {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
     }


     .time-counter {
        margin-top: 30px;
        padding: 20px;
        border: 1px solid #b2ebf2;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        overflow: hidden; /* For potential effects */
     }
     .time-counter.active {
         background: linear-gradient(to right, #e1f5fe, #bbdefb, #e1f5fe); /* Gradient when active */
         box-shadow: 0 0 15px rgba(2, 136, 209, 0.5); /* Glow when active */
     }


     .counter-display {
        font-family: 'Share Tech Mono', monospace; /* Digital-like font */
        font-size: 3em; /* Larger */
        font-weight: bold;
        color: #0288d1; /* Light Blue */
        margin-bottom: 10px;
         text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
         transition: color 0.5s ease;
     }
      .counter-display span {
         display: inline-block; /* For potential digit animation */
         animation: count-up 0.5s ease-out; /* Simple animation on change */
      }
      @keyframes count-up {
          0% { transform: translateY(5px); opacity: 0.5; }
          100% { transform: translateY(0); opacity: 1; }
      }


     .counter-info {
         font-size: 0.8em;
         color: #555;
     }


    #explanation-toggle {
        display: block;
        width: fit-content;
        margin: 30px auto 20px;
        padding: 12px 25px;
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        background-color: #00796b; /* Dark Teal */
        color: white;
         box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease, transform 0.1s ease;
    }
     #explanation-toggle:hover {
         background-color: #00897b; /* Slightly lighter */
         transform: translateY(-1px);
     }
     #explanation-toggle:active {
         background-color: #00695c; /* Slightly darker */
         transform: translateY(0);
         box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
     }


    #explanation {
        margin-top: 20px;
        padding: 25px;
        border: 1px solid #b2ebf2;
        border-radius: 8px;
        background-color: #ffffff;
        direction: rtl;
        text-align: right;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        line-height: 1.7;
    }

    #explanation h2, #explanation h3 {
        color: #00796b; /* Dark Teal */
        margin-bottom: 15px;
        border-bottom: 1px solid #e0f2f7; /* Extra Light Cyan */
        padding-bottom: 8px;
        font-weight: bold;
    }

    #explanation p {
        margin-bottom: 15px;
        line-height: 1.6;
        color: #333;
    }
    #explanation ul, #explanation ol {
        margin-bottom: 15px;
        padding-right: 20px;
    }
    #explanation li {
        margin-bottom: 8px;
        line-height: 1.5;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .clock-diagram, .feedback-loop {
            flex-direction: column;
            gap: 15px;
        }
        .beam {
            width: 80%; /* Make beams take more width */
            height: 30px;
             margin: 0; /* Adjust margin for column layout */
             justify-content: flex-start; /* Align atoms to start of flow */
        }
         .beam::before { /* Adjust arrow direction for vertical flow */
             content: '▼'; /* Down arrow */
             top: auto;
             bottom: -20px; /* Position below beam */
             left: 50%;
             transform: translateX(-50%);
         }
        .component {
            margin: 0; /* Adjust margin for gap */
            width: 90%; /* Make components take more width */
        }
         .feedback-loop .component {
             width: 80%;
         }
        .arrow {
             transform: rotate(90deg); /* Rotate arrows */
             margin: 10px 0;
        }
         .arrow.feedback-arrow {
             transform: rotate(180deg); /* Feedback arrow goes up */
         }
         .lock-status {
             margin-right: 0;
             margin-top: 15px;
         }
         .microwave-field {
             width: 40px;
             height: 40px;
         }
    }

    @media (max-width: 480px) {
         #atomic-clock-app {
             padding: 15px;
         }
        .app-title, .controls-title, .loop-title, .counter-title {
             font-size: 1.2em;
        }
        .component {
            padding: 10px 15px;
            min-width: 80px;
            font-size: 0.8em;
        }
        .cavity {
            min-height: 70px;
        }
        .microwave-label {
            font-size: 0.75em;
        }
         .detector-output {
             font-size: 1em;
         }
        .controls {
             padding: 15px;
        }
        #frequency-slider {
             height: 6px;
        }
        #frequency-slider::-webkit-slider-thumb, #frequency-slider::-moz-range-thumb {
            width: 18px;
            height: 18px;
        }
        .freq-labels {
            font-size: 0.7em;
        }
        .control-button {
            padding: 8px 15px;
            font-size: 0.9em;
        }
        .feedback-loop {
             padding: 15px;
        }
        .feedback-loop .component {
            padding: 8px 10px;
            min-width: 60px;
            font-size: 0.7em;
        }
        .arrow, .arrow.feedback-arrow {
             font-size: 1.5em;
        }
        .lock-status {
            font-size: 0.9em;
        }
         .time-counter {
             padding: 15px;
         }
         .counter-display {
             font-size: 2em;
         }
         .counter-info {
             font-size: 0.7em;
         }
        #explanation-toggle {
             padding: 10px 20px;
             font-size: 1em;
        }
        #explanation {
             padding: 15px;
             font-size: 0.9em;
        }
         #explanation h2, #explanation h3 {
             font-size: 1.1em;
         }
    }

</style>

<button id="explanation-toggle">מה בדיוק קורה כאן? הצג הסבר מלא</button>

<div id="explanation" style="display: none;">
    <h2>הסבר מלא: הפלא הקוונטי שבשעון האטומי</h2>

    <p>השעונים האטומיים הם אבני היסוד של העולם הטכנולוגי המודרני, ומספקים את הדיוק הכרונומטרי הדרוש למערכות עולמיות. הדיוק המופלג הזה לא נובע מכוח המכניקה הקלאסית, אלא מעקרונות הליבה של המכניקה הקוונטית.</p>

    <h3>ה"פעימות" של האטום: רמות אנרגיה וקרינה</h3>
    <p>במקום להתבסס על תנועה מכנית או תנודות גביש, שעון אטומי מודד זמן על סמך תופעה יסודית יותר: המעברים האנרגטיים בתוך אטומים. אלקטרונים באטום יכולים להימצא רק ברמות אנרגיה מסוימות ומוגדרות היטב (רמות קוונטיות). מעבר אלקטרון בין שתי רמות אנרגיה שונות כרוך בפליטה או בליעה של מנת אנרגיה (פוטון) בעלת תדר מדויק להפליא. תדר זה הוא "טביעת אצבע" אנרגטית ייחודית לזוג רמות האנרגיה הספציפי ולקבוע טבעי שאינו מושפע כמעט כלל מתנאי סביבה כמו טמפרטורה או לחץ.</p>
     <p>עבור אטומי צסיום-133, המעבר האנרגטי הספציפי המשמש בשעונים אטומיים תקניים מתרחש בתדר של 9,192,631,770 הרץ בדיוק. זהו תדר קבוע, יציב ואינהרנטי לטבעו של אטום הצסיום.</p>


    <h3>תהודה קוונטית: "הקשבה" לתדר האטומי</h3>
    <p>כאשר אטום נחשף לקרינה אלקטרומגנטית (למשל גלי מיקרוגל) שתדרה תואם במדויק את ההפרש האנרגטי בין שתי רמות קוונטיות, האטום עובר "תהודה" - הוא בולע את אנרגיית הקרינה ומקפץ לרמת האנרגיה הגבוהה יותר. אם תדר הקרינה אפילו מעט שונה מתדר התהודה המדויק, ההסתברות למעבר אנרגטי כזה צונחת דרמטית.</p>

    <h3>איך בונים שעון כזה? (מבנה בסיסי של שעון צסיום)</h3>
    <p>הסימולציה מציגה את הרכיבים העיקריים של שעון צסיום:</p>
    <ol>
        <li><strong>מקור אטומים:</strong> תנור קטן מחמם צסיום ומאדה אותו. האטומים נפלטים כ"קרן" ונשלחים דרך שפופרת ואקום. לרוב, לפני הכניסה לחלל המיקרוגל, האטומים עוברים סינון (לא מוצג בסימולציה) כדי להבטיח שהם נמצאים במצב אנרגטי התחלתי מתאים.</li>
        <li><strong>חלל המיקרוגל (חלל תהודה):</strong> קרן האטומים עוברת בתוך חלל שמופעל עליו שדה מיקרוגל. תדר המיקרוגל מגיע מ"מתנד אלקטרוני" (אוסצילטור) שאת תדרו ניתן לכוונן (זה מה שאתם עושים עם המחוון בסימולציה!).</li>
        <li><strong>גלאי האטומים:</strong> בקצה השני, גלאי מיוחד (למשל, עם שדה מגנטי נוסף שמפריד אטומים לפי מצבם האנרגטי) מודד כמה אטומים הגיעו אליו במצב האנרגטי הסופי (לאחר שעברו שינוי בחלל המיקרוגל). מספר האטומים המזוהים בגלאי הוא המדד למידת ההתאמה בין תדר המיקרוגל לתדר התהודה האטומי.</li>
    </ol>

    <h3>הקסם של לולאת המשוב: נעילת התדר</h3>
    <p>המטרה היא להגיע לתדר המיקרוגל המדויק - 9,192,631,770 הרץ - שבו מספר האטומים שמגיעים לגלאי הוא מקסימלי. איך השעון עושה זאת אוטומטית? באמצעות לולאת משוב אלקטרונית (שמופעלת בסימולציה בלחיצה על "כוונון אוטומטי"):</p>
    <ul>
        <li>המתנד האלקטרוני (שמייצר את תדר המיקרוגל) מתחיל לפעול בתדר קרוב.</li>
        <li>מעגל הבקרה מקבל את האות מהגלאי (כמה אטומים זוהו).</li>
        <li>אם מספר האטומים אינו מקסימלי, מעגל הבקרה מסיק שהתדר אינו מדויק.</li>
        <li>מעגל הבקרה שולח אות תיקון למתנד האלקטרוני, ומשנה מעט את תדר המיקרוגל.</li>
        <li>התהליך חוזר על עצמו: השעון מכוונן את התדר שוב ושוב, תוך שהוא "מקשיב" לגלאי, עד שהוא מוצא את התדר שנותן את תפוקת האטומים הגבוהה ביותר בגלאי.</li>
        <li>בנקודה זו, תדר המתנד ה"ננעל" (Locked) בדיוק על תדר התהודה האטומי היציב.</li>
    </ul>

    <h3>איך הופכים תדר קבוע למונה זמן? הגדרת השנייה</h3>
    <p>ברגע שהמתנד ננעל על תדר התהודה של צסיום, הוא מייצר אות אלקטרוני בתדר קבוע להפליא: 9,192,631,770 מחזורים בשנייה. אות זה הוא למעשה ה"שעון" הפנימי של המכשיר. על פי ההגדרה הבינלאומית של השנייה, <strong>שנייה אחת מוגדרת בדיוק כמספר המחזורים הזה של קרינת המיקרוגל המתאימה למעבר האנרגטי הספציפי באטום צסיום-133 במצב היסוד שלו.</strong></p>
    <p>מונה דיגיטלי פשוט סופר את מחזורי האות הנעול הזה. כל 9,192,631,770 מחזורים, המונה מקדם את ספירת השניות באחת. הדיוק המדהים של התדר האטומי מתורגם ישירות לדיוק חסר תקדים במדידת זמן.</p>
     <p>הסימולציה שלנו מקפיצה את מונה השניות בכל שנייה אמיתית (לאחר נעילת התדר), כדי להמחיש שהמערכת אכן "מודדת" זמן קבוע, שנגזר מהיציבות של האטום עצמו.</p>
</div>

<script>
    const targetFrequency = 9192631770; // Hz
    const frequencySlider = document.getElementById('frequency-slider');
    const freqDisplay = document.getElementById('freq-display');
    const detectedCountSpan = document.getElementById('detected-count');
    const detectorPeakIndicator = document.querySelector('.detector-peak-indicator');
    const lockIndicatorSpan = document.getElementById('lock-indicator');
    const secondsCounterSpan = document.getElementById('seconds-counter');
    const explanationToggleBtn = document.getElementById('explanation-toggle');
    const explanationDiv = document.getElementById('explanation');
    const autoTuneButton = document.getElementById('auto-tune-button');
    const cavityElement = document.querySelector('.cavity');
    const timeCounterElement = document.querySelector('.time-counter');
    const beamOutAtoms = document.querySelectorAll('.beam-out .atom'); // Select state-changed atoms

    let currentFrequency = parseInt(frequencySlider.value);
    let seconds = 0;
    let isLocked = false;
    let counterInterval = null;
    let autoTuneInterval = null;
    let autoTuneSpeed = 5; // How many Hz to adjust per step during auto-tune
    const autoTuneStepTime = 50; // Milliseconds between auto-tune steps

    // Simulate the resonance curve (more pronounced peak)
    function simulateDetection(frequency) {
        const width = 10; // Narrower width for sharper peak
        const maxDetected = 100; // Max atoms detected at resonance
        const backgroundNoise = 10; // Some atoms detected even off-resonance

        const detuning = Math.abs(frequency - targetFrequency);
        // Using a Gaussian-like decay: maxDetected * exp(-(detuning/width)^2)
        // Add background noise
        let detected = backgroundNoise + (maxDetected - backgroundNoise) * Math.exp(-Math.pow(detuning / width, 2));

        // Add some random fluctuation for realism (small)
        detected += (Math.random() - 0.5) * 5; // +/- 2.5 fluctuation

        return Math.max(backgroundNoise, Math.round(detected)); // Ensure at least background noise is detected
    }

    function updateFrequency(value, fromAutoTune = false) {
        currentFrequency = parseInt(value);
        freqDisplay.textContent = currentFrequency.toLocaleString('en-US'); // Use en-US for digits format consistency
        const detectedCount = simulateDetection(currentFrequency);
        detectedCountSpan.textContent = detectedCount;

        // Visual feedback for peak
        const detectionPercentage = (detectedCount - 10) / 90; // Scale from background (10) to max (100)
        if (detectionPercentage > 0.8) { // Show indicator when close to peak
            detectorPeakIndicator.classList.add('active');
             cavityElement.classList.add('resonant'); // Add resonant class for glow
        } else {
            detectorPeakIndicator.classList.remove('active');
             cavityElement.classList.remove('resonant'); // Remove resonant class
        }

        // Visual feedback for state-changed atoms
        const changedOpacity = detectionPercentage > 0 ? detectionPercentage : 0; // Atoms change state based on detection rate
         beamOutAtoms.forEach(atom => {
             atom.style.opacity = changedOpacity;
         });


        // Simple simulation of locking behavior
        const lockThreshold = 2; // Lock within 2 Hz of target
        if (Math.abs(currentFrequency - targetFrequency) <= lockThreshold) {
            if (!isLocked) {
                isLocked = true;
                lockIndicatorSpan.textContent = 'נעול (על התדר האטומי)';
                lockIndicatorSpan.classList.add('locked');
                timeCounterElement.classList.add('active'); // Activate counter visuals
                startCounter();
                 if (!fromAutoTune) { // If locked manually, make slider reflect exact target
                    frequencySlider.value = targetFrequency;
                    freqDisplay.textContent = targetFrequency.toLocaleString('en-US');
                 }
                 autoTuneButton.disabled = true; // Disable auto-tune when locked
            }
        } else {
            if (isLocked) {
                isLocked = false;
                lockIndicatorSpan.textContent = 'מכוון ידנית';
                lockIndicatorSpan.classList.remove('locked');
                timeCounterElement.classList.remove('active'); // Deactivate counter visuals
                stopCounter();
                 autoTuneButton.disabled = false; // Enable auto-tune when unlocked
            }
             // If manually tuned while auto-tuning is active, stop auto-tuning
             if (autoTuneInterval !== null && !fromAutoTune) {
                 stopAutoTune();
             }
        }
    }

    function startCounter() {
        if (counterInterval === null) {
            // In a real clock, this counter counts 9,192,631,770 cycles per second.
            // Here we just increment once per simulated second for visualization.
            counterInterval = setInterval(() => {
                seconds++;
                secondsCounterSpan.textContent = seconds;
            }, 1000); // Increment every 1000ms (1 second)
        }
    }

    function stopCounter() {
        if (counterInterval !== null) {
            clearInterval(counterInterval);
            counterInterval = null;
        }
         // Don't reset seconds, just stop counting for demo clarity
    }

    function startAutoTune() {
        if (autoTuneInterval === null && !isLocked) {
             autoTuneButton.textContent = 'מכוון...';
             autoTuneButton.disabled = true;
             frequencySlider.disabled = true; // Disable manual slider during auto-tune

            autoTuneInterval = setInterval(() => {
                // Simulate the feedback loop trying to maximize detected atoms
                // This is a simplified hill-climbing algorithm
                const currentDetected = simulateDetection(currentFrequency);
                const stepSize = autoTuneSpeed; // Base step size

                // Check slightly higher and lower frequencies
                const detectedHigher = simulateDetection(currentFrequency + stepSize);
                const detectedLower = simulateDetection(currentFrequency - stepSize);

                let nextFrequency = currentFrequency;

                if (detectedHigher > currentDetected && detectedHigher >= detectedLower) {
                    nextFrequency += stepSize;
                } else if (detectedLower > currentDetected && detectedLower > detectedHigher) {
                     nextFrequency -= stepSize;
                } else if (currentDetected >= detectedHigher && currentDetected >= detectedLower) {
                    // We are near the peak, slow down and refine search
                    autoTuneSpeed = Math.max(1, autoTuneSpeed / 2); // Reduce speed
                    if (autoTuneSpeed < 2 && Math.abs(currentFrequency - targetFrequency) <= 5) { // Close enough, try smaller steps
                        // Try steps of 1 Hz
                        const detectedPlus1 = simulateDetection(currentFrequency + 1);
                        const detectedMinus1 = simulateDetection(currentFrequency - 1);
                         if (detectedPlus1 > currentDetected && detectedPlus1 >= detectedMinus1) {
                             nextFrequency += 1;
                         } else if (detectedMinus1 > currentDetected && detectedMinus1 > detectedPlus1) {
                             nextFrequency -= 1;
                         } else {
                             // Found the peak within 1 Hz, lock it
                             nextFrequency = targetFrequency; // Snap to the exact target
                             stopAutoTune();
                         }
                    }
                }

                 // Clamp frequency to slider bounds
                 nextFrequency = Math.max(parseInt(frequencySlider.min), Math.min(parseInt(frequencySlider.max), nextFrequency));

                currentFrequency = nextFrequency;
                frequencySlider.value = currentFrequency; // Update slider visually
                updateFrequency(currentFrequency, true); // Update displays and check for lock

                 // If locked by updateFrequency, interval will be cleared there.
                 if (isLocked) {
                     stopAutoTune(); // Ensure interval is cleared if updateFrequency locked it
                 }


            }, autoTuneStepTime);
        }
    }

    function stopAutoTune() {
        if (autoTuneInterval !== null) {
            clearInterval(autoTuneInterval);
            autoTuneInterval = null;
             autoTuneButton.textContent = 'כוונון אוטומטי (הפעלת לולאת המשוב)';
             autoTuneButton.disabled = false; // Re-enable button
            frequencySlider.disabled = false; // Re-enable slider
             autoTuneSpeed = 5; // Reset speed for next time
        }
    }


    // Add event listeners
    frequencySlider.addEventListener('input', (event) => {
        // Allow manual tuning only if not locked and not currently auto-tuning
        if (!isLocked && autoTuneInterval === null) {
             updateFrequency(event.target.value);
        } else if (isLocked) {
            // If already locked, moving slider *unlocks* it
            stopCounter();
             isLocked = false; // Need to explicitly change state here
             lockIndicatorSpan.textContent = 'מכוון ידנית';
             lockIndicatorSpan.classList.remove('locked');
             timeCounterElement.classList.remove('active');
             autoTuneButton.disabled = false;
            updateFrequency(event.target.value); // Now update based on manual input
        }
    });

    autoTuneButton.addEventListener('click', () => {
        if (!isLocked && autoTuneInterval === null) {
            startAutoTune();
        } else if (autoTuneInterval !== null) {
            stopAutoTune();
        }
         // If locked, button is disabled, so this handler won't fire
    });


    // Explanation toggle button
    explanationToggleBtn.addEventListener('click', () => {
        if (explanationDiv.style.display === 'none') {
            explanationDiv.style.display = 'block';
            explanationToggleBtn.textContent = 'הסתר הסבר מלא';
        } else {
            explanationDiv.style.display = 'none';
            explanationToggleBtn.textContent = 'מה בדיוק קורה כאן? הצג הסבר מלא';
        }
    });

    // Initialize app state
    updateFrequency(frequencySlider.value); // Set initial frequency and detected count


    // Initial animation for atoms (adjusting delay values if needed)
    const atoms = document.querySelectorAll('.atom');
    atoms.forEach((atom, index) => {
        atom.style.setProperty('--delay', `${index * 0.4}s`); // Adjust delay for smoother flow
    });


</script>
---