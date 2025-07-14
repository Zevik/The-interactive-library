---
title: "בונים לגובה: סודות הקתדרלה הגותית"
english_slug: building-up-the-secrets-of-the-gothic-cathedral
category: "מדעי הרוח / היסטוריה וארכאולוגיה"
tags: אדריכלות גותית, קתדרלות, הנדסה, ימי הביניים, היסטוריה של האמנות
---
# בונים לגובה: סודות הקתדרלה הגותית

איך הצליחו בוני הקתדרלות הגותיות בימי הביניים ליצור מבני ענק, גבוהים ודקיקים, עם חלונות ויטראז' ענקיים, ללא שימוש במנופים או בטון? הצצה אל המערכת ההנדסית המורכבת שמאחורי הפאר האדריכלי.

<div id="cathedral-app">
    <div class="app-container">
        <h2>בנה קטע מקתדרלה</h2>
        <div class="building-area">
            <div class="base">בסיס ויסודות</div>
            <div class="column column-left hidden">עמוד תומך</div>
            <div class="column column-right hidden">עמוד תומך</div>
            <div class="rib-vault hidden">קמרון צלעות</div>
            <div class="flying-buttress flying-buttress-left hidden">תמיכה דואה</div>
            <div class="flying-buttress flying-buttress-right hidden">תמיכה דואה</div>
            <div class="stained-glass stained-glass-left hidden">חלון ויטראז'</div>
            <div class="stained-glass stained-glass-right hidden">חלון ויטראז'</div>

            <!-- Force visualizations -->
            <div class="force force-vertical hidden"></div>
            <div class="force force-horizontal-left hidden"></div>
            <div class="force force-horizontal-right hidden"></div>
            <div class="force force-counter-left hidden"></div>
            <div class="force force-counter-right hidden"></div>

            <!-- Instability/Stability indicators -->
             <div class="stability-indicator indicator-left hidden"></div>
             <div class="stability-indicator indicator-right hidden"></div>
        </div>
        <div class="controls">
            <button id="add-columns">בנה עמודים תומכים</button>
            <button id="add-vaults" class="hidden">צור קמרון צלעות</button>
            <button id="add-buttresses" class="hidden">הוסף תמיכות דואות</button>
            <button id="add-glass" class="hidden">קשט בויטראז'ים</button>
            <button id="reset-building">התחל מחדש</button>
        </div>
        <div class="feedback"></div>
    </div>
</div>

<style>
    #cathedral-app {
        font-family: 'Assistant', sans-serif; /* Use a modern, readable font */
        direction: rtl;
        text-align: right;
        margin-bottom: 30px;
        padding: 20px;
        border: none; /* Remove basic border */
        border-radius: 12px;
        background: linear-gradient(to bottom right, #ece9e6, #ffffff); /* Subtle gradient background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Add depth */
        max-width: 700px; /* Limit width for better reading */
        margin-left: auto;
        margin-right: auto;
    }

    #cathedral-app h2 {
        text-align: center;
        color: #333;
        margin-top: 0;
        margin-bottom: 20px;
        font-size: 1.8em;
        font-weight: bold;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 10px;
    }

    .app-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .building-area {
        position: relative;
        width: 100%;
        max-width: 650px; /* Slightly wider */
        height: 450px; /* Slightly taller */
        border: none; /* Remove building area border */
        margin: 25px 0;
        background-color: #e8e4dc; /* Light stone background */
        background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNjY2NjY2MiIGZpbGwtb3BhY2l0eT0iMC4yIj48cGF0aCBkPSJNMjAgMTAuNTV2MS42OWExMCAxMCAwIDAgMS0xMCAwdi0xLjY5Yy0xLjg2LS4xOC0zLjQ4LS44Ni00LjgyLTIuMDFhOS45NyA5LTAgMCAxLTIuMTgtMi44Nkw5Ljg4IDUuNGMtLjE4LjQyLS4zMi44Ni0uNDQgMS4zMS0uNjggMi41NS0yLjA5IDQuNzktNC4wMiA2LjM3YS45OS45OSAwIDAgMS0uMjkuODVsLjcxLjcxYy42Ny42NyAxLjYzIDEuMDQgMi42MyAxLjA0SDEwYy0uOTggMC0xLjkzLS4zNy0yLjYzLTEuMDVsLS43LS43YTEgMSAwIDAgMC0uMy0uODZjMS45NC0xLjU3IDMuMzctMy44MiA0LjA1LTYuMzhhOS45NyA5IDAgMCAxIC40My0xLjMxTDEuMyA2Ljg1QzIuNjMgNS4wMiA0LjU3IDMuNTcgNi43NSAyLjVWMEM0LjA3IDEuMDQgMS44OCAyLjgyIDAgNC45VjguODhjLjkyLjk2IDEuOTkgMS44NyAzLjI3IDIuNjNhOS45NyA5IDAgMCAxIDIuMTggMi44Nkw5Ljg4IDE0LjZDLjk5LjQyIDkuODUuODYgOS43MyAxLjMxYy0uNjcgMi41NS0yLjA5IDQuNzktNC4wMiA2LjM3YS45OS45OSAwIDAgMS0uMjkuODVsLjcxLjcxYy42Ny42NyAxLjYzIDEuMDQgMi42MyAxLjA0SDEwYy45OCAwIDEuOTMtLjM3Mi42My0xLjA1bC43LS43YTEgMSAwIDAgMCAuMy0uODZjLTEuOTQtMS41Ny0zLjM3LTMuODItNC4wNS02LjM4YSkuOTkuOTkgMCAwIDEtLjQzLTEuMzFMMS4zIDYuODVDMi42MyA1LjAyIDQuNTcgMy41NyA2Ljc1IDIuNlYwQzQuMDcgMS4wNCAxLjg4IDIuODIgMCA0LjkwIDguODhjLjkyLjk2IDEuOTkgMS44NyAzLjI3IDIuNjNhOS45NyA5IDAgMCAxIDIuMTggMi44Nkw5Ljg4IDE0LjZjLS4xOC40Mi0uMzIuODYtLjQ0IDEuMzEtLjY4IDIuNTUtMi4wOSA0Ljc5LTQuMDIgNi4zN2EuOTkuOTkgMCAwIDEtLjI5Ljg1bC43MS43MWMuNjcuNjcgMS42MyAxLjA0IDIuNjMgMS4wNEgxMGMtLjk4IDAtMS45My0uMzctMi42My0xLjA1bC43LS43YTEgMSAwIDAgMCAuMy0uODZjLTEuOTQtMS41Ny0zLjM3LTMuODItNC4wNS02LjM4YTkuOTkgOSAwIDAgMS0uNDMtMS4zMUwxLjMgNi44NUMyLjYzIDUuMDIgNC41NyAzLjU3IDYuNzUgMi42VjBDNC4wNyAxLjA0IDEuODggMi44MiAwIDQuOTBWOC44OGMuOTIuOTYgMS45OSAxLjg3IDMuMjcgMi42M0ExMCAxMCAwIDAgMCAxMCAyMC41NXYxLjY5YTEwIDEwIDAgMCAwIDEwIDB2LTEuNjlhMTAgMTAgMCAwIDAtMS0yLjdjMS4yOC0uNzYgMi4zNi0xLjY3IDMuMjctMi42M3YuMDJjMS44OC0yLjA4IDQuMDctMy44NiA2Ljc1LTQuOVYyLjZDNTEuOTMgMy41NyA1My44NyA1LjAyIDU1LjIgNi44NWwuMDEuMDFjLjU4Ljk2Ljk1IDIuMDIgMS4wNiAzLjE1LjIgMi41Ni0uMiA1LjEtMS4wNiA3LjM3LS44OSA1LjUzLTMuNjggMTAuNjQtNy44IDEzLjgzaC0uMDFhMi4wMiAyLjAyIDAgMCAxLTIuMDItMi4wMnYtLjA0Yy0uMzQtMS44MS0xLjItMy40Ni0yLjQ3LTQuNjlhMTAgMTAgMCAwIDAtMy43My0zLjA4bC0xLjUxLS41M2E2LjA2IDYuMDYgMCAwIDEgMS4yOC0yLjlhMTUuMDIgMTUuMDIgMCAwIDAgMy4xNC01LjI0YTIgMiAwIDAgMC0xLjgzLTIuNDNsLS4wOS0uMDFhMTMuMyAxMy4zIDAgMCAxLTUuMzQuMjljLTEuNTguMi0zLjEzLjYtNC41MiAxLjEyYS45OS45OSAwIDAgMC0uODkuNzYlMjAuMS4xIDAgMCAxLS4xNC4wNWwtLjcxLS4wMWExIDIgMCAwIDEtMS4xLS40NUwyOCA0LjdjLS4yLS4zNi0uNDMtLjY5LS42Ny0xLjAxYTUuMDMgNS4wMyAwIDAgMC0uOTgtMS4yOCA3LjAzIDcuMDMgMCAwIDAtMS40My0xLjM3Yy0uNDQtLjQtLjg2LS44NC0xLjI4LTEuMjhIMy40M2EuOTkuOTkgMCAwIDAtLjc2Ljg5bC0uMDEuMTVhMTMuMjcgMTMuMjcgMCAwIDEgLjI5IDUuMzRjLjIuNjQuNiAxLjI0IDEuMTIgMS44M2EuOTkuOTkgMCAwIDAgLjc2Ljg5bC4xNS0uMDFhMiAyIDAgMCAxIDEuODMuNDRsLS4wOS4wMWExNS4wMiAxNS4wMiAwIDAgMC01LjI0IDMuMTRhNi4wNiA2LjA2IDAgMCAxLTIuOSAxLjI4bC0uNTMtMS41MUExMCAxMCAwIDAgMCA2LjA5IDMuODNjLTEuMjMtMS4yOC0yLjg4LTIuMTMtNC42OS0yLjQ3di0uMDRhMiAyIDAgMCAxLTIuMDItMi4wMmgtLjAxQzEuMDQgMTYuMDYgMy44MyAyMC44NyA5LjM2IDI1Ljc2eiI+PC9wYXRoPjwvZz48L2c+PC9zdmc+'); /* Subtle pattern */
        overflow: hidden; /* Hide overflowing elements during animations */
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.2); /* Inner shadow */
    }

    .base {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60px; /* Taller base */
        background-color: #a09484; /* Stone-like color */
        color: white;
        text-align: center;
        line-height: 60px;
        font-weight: bold;
        z-index: 1;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-size: 1.2em;
    }

    .column {
        width: 50px; /* Wider columns */
        height: 300px; /* Taller columns */
        background-color: #c2b2a2; /* Lighter stone */
        position: absolute;
        bottom: 60px; /* Above base */
        z-index: 2;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 10px;
        box-sizing: border-box;
        font-size: 0.9em;
        text-align: center;
        line-height: 1.3;
        color: #444;
        border-top: 5px solid #a09484; /* Cap */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        opacity: 0; /* Start hidden for animation */
        transform: translateY(20px); /* Start slightly below */
        transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animation */
    }

    .column.visible {
         opacity: 1;
         transform: translateY(0);
    }


    .column-left {
        left: 80px; /* Positioned further in */
    }

    .column-right {
        right: 80px; /* Positioned further in */
    }

    .rib-vault {
        position: absolute;
        bottom: 360px; /* Above columns */
        left: 130px; /* Between columns */
        right: 130px;
        height: 150px; /* Taller vault */
        background-color: #d4c4b4; /* Vault color */
        border-top: 8px solid #c2b2a2; /* Ribs */
        border-radius: 50% 50% 0 0 / 100% 100% 0 0;
        z-index: 3;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #444;
        text-align: center;
        padding-top: 30px; /* Center text */
        box-sizing: border-box;
        font-size: 0.9em;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
         opacity: 0;
         transform: translateY(20px);
         transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }

     .rib-vault.visible {
         opacity: 1;
         transform: translateY(0);
    }

    .flying-buttress {
        width: 120px; /* Wider */
        height: 200px; /* Taller */
        background-color: #b8a898; /* Buttress color */
        position: absolute;
        bottom: 160px; /* Connects higher up */
        z-index: 4;
        /* More complex clip-path for a better buttress shape */
        clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 80% 100%, 80% 40%, 40% 40%, 40% 100%, 0% 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        text-align: center;
        line-height: 1.3;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        box-shadow: -4px 4px 8px rgba(0,0,0,0.2);
        opacity: 0;
        transform: translateX(-20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
    .flying-buttress-right {
        box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
        transform: translateX(20px);
    }

     .flying-buttress.visible {
         opacity: 1;
         transform: translateX(0);
     }
     .flying-buttress-right.visible {
         transform: translateX(0);
     }


     .flying-buttress-left {
        left: -80px; /* Position further outside */
        transform: skewY(5deg); /* Simulate angle */
     }
     .flying-buttress-right {
        right: -80px; /* Position further outside */
        transform: skewY(-5deg); /* Simulate angle */
     }


    .stained-glass {
        position: absolute;
        top: 150px; /* Position above columns, below vault */
        width: 120px; /* Wider windows */
        height: 220px; /* Taller windows */
        background: linear-gradient(45deg, #e91e63, #9c27b0, #2196f3, #4caf50, #ffeb3b, #ff9800); /* More varied gradient */
        opacity: 0.9; /* More opaque */
        z-index: 0; /* Behind other elements */
        border: 8px solid #444; /* Thicker leading lines */
        box-sizing: border-box;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.5); /* Inner glow/depth */
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.8em;
        text-align: center;
        line-height: 1.3;
        color: rgba(255,255,255,0.9); /* White text with transparency */
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        opacity: 0;
        transform: scale(0.9); /* Start slightly smaller */
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }
     .stained-glass.visible {
         opacity: 0.9;
         transform: scale(1);
     }

    .stained-glass-left {
         left: 160px; /* Position between column and vault */
    }
     .stained-glass-right {
         right: 160px; /* Position between column and vault */
     }

    /* Load visualization - arrows */
    .force {
        position: absolute;
        width: 0;
        height: 0;
        border-style: solid;
        z-index: 5;
        pointer-events: none; /* Don't block clicks */
        filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.3)); /* Shadow for visibility */
    }

    .force-vertical {
        bottom: 410px; /* Above vault */
        left: 50%;
        transform: translateX(-50%);
        border-width: 20px 10px 0 10px; /* Triangle pointing down */
        border-color: red transparent transparent transparent;
        opacity: 0;
         transition: opacity 0.5s ease-out;
    }

    .force-horizontal-left, .force-horizontal-right {
        bottom: 350px; /* Near vault connection */
        width: 40px; /* Arrow shaft length */
        height: 0;
        border-width: 0;
        border-bottom: 5px solid orange; /* Arrow shaft */
        opacity: 0;
        transition: opacity 0.5s ease-out;
    }
     .force-horizontal-left:after, .force-horizontal-right:after {
         content: '';
         position: absolute;
         width: 0;
         height: 0;
         border-style: solid;
     }

    .force-horizontal-left {
        left: 180px; /* Near left vault edge */
        transform: rotate(-10deg); /* Angle */
    }
    .force-horizontal-left:after {
        right: -15px; /* Position arrowhead */
        bottom: -10px; /* Adjust to align with shaft */
        border-width: 10px 0 10px 15px; /* Triangle pointing right */
        border-color: transparent transparent transparent orange;
    }


    .force-horizontal-right {
        right: 180px; /* Near right vault edge */
        transform: rotate(10deg); /* Angle */
    }
     .force-horizontal-right:after {
        left: -15px; /* Position arrowhead */
         bottom: -10px; /* Adjust to align with shaft */
        border-width: 10px 15px 10px 0; /* Triangle pointing left */
        border-color: transparent orange transparent transparent;
    }


    .force-counter-left, .force-counter-right {
        bottom: 250px; /* Near buttress connection point */
        width: 50px; /* Arrow shaft length */
        height: 0;
        border-width: 0;
        border-bottom: 5px solid green; /* Arrow shaft */
        opacity: 0;
        transition: opacity 0.5s ease-out;
    }
     .force-counter-left:after, .force-counter-right:after {
         content: '';
         position: absolute;
         width: 0;
         height: 0;
         border-style: solid;
     }

    .force-counter-left {
        left: 20px; /* Originates from buttress area */
         transform: rotate(10deg); /* Angle */
    }
     .force-counter-left:after {
        right: -15px; /* Position arrowhead */
         bottom: -10px; /* Adjust to align with shaft */
         border-width: 10px 0 10px 15px; /* Triangle pointing right */
         border-color: transparent transparent transparent green;
     }

    .force-counter-right {
        right: 20px; /* Originates from buttress area */
        transform: rotate(-10deg); /* Angle */
    }
     .force-counter-right:after {
        left: -15px; /* Position arrowhead */
         bottom: -10px; /* Adjust to align with shaft */
         border-width: 10px 15px 10px 0; /* Triangle pointing left */
         border-color: transparent green transparent transparent;
     }

    .force.visible {
        opacity: 1;
    }

    /* Stability indicators */
    .stability-indicator {
        position: absolute;
        bottom: 350px; /* Near vault connection point */
        width: 30px;
        height: 30px;
        border-radius: 50%;
        z-index: 6;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s ease-out;
        filter: drop-shadow(0 0 5px rgba(0,0,0,0.5));
    }

     .indicator-left { left: 120px; }
     .indicator-right { right: 120px; }

    .stability-indicator.unstable {
        background-color: red;
        opacity: 1;
        animation: pulse-red 1s infinite; /* Animation */
    }

    .stability-indicator.stable {
        background-color: green;
        opacity: 1;
        animation: pulse-green 1s infinite; /* Animation */
    }

     @keyframes pulse-red {
         0% { box-shadow: 0 0 0 0 rgba(255,0,0,0.7); }
         70% { box-shadow: 0 0 0 15px rgba(255,0,0,0); }
         100% { box-shadow: 0 0 0 0 rgba(255,0,0,0); }
     }

     @keyframes pulse-green {
         0% { box-shadow: 0 0 0 0 rgba(0,255,0,0.7); }
         70% { box-shadow: 0 0 0 15px rgba(0,255,0,0); }
         100% { box-shadow: 0 0 0 0 rgba(0,255,0,0); }
     }


    .hidden {
        display: none !important; /* Use !important to ensure override */
    }

    .controls {
        margin-top: 25px;
        display: flex;
        flex-wrap: wrap;
        gap: 12px; /* Slightly larger gap */
        justify-content: center;
        padding: 0 10px;
    }

    .controls button {
        padding: 12px 20px; /* Larger buttons */
        font-size: 1.1em;
        cursor: pointer;
        border: none;
        border-radius: 6px;
        color: white;
        transition: background-color 0.3s ease, transform 0.1s ease;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    #add-columns { background-color: #007bff; }
    #add-columns:hover:not(:disabled) { background-color: #0056b3; transform: translateY(-2px); }

    #add-vaults { background-color: #ffc107; color: #333;} /* Yellow/Orange */
    #add-vaults:hover:not(:disabled) { background-color: #e0a800; transform: translateY(-2px); }

    #add-buttresses { background-color: #28a745; } /* Green */
    #add-buttresses:hover:not(:disabled) { background-color: #218838; transform: translateY(-2px); }

    #add-glass { background-color: #6f42c1; } /* Purple */
    #add-glass:hover:not(:disabled) { background-color: #5a32a3; transform: translateY(-2px); }

    #reset-building {
         background-color: #dc3545; /* Red */
         box-shadow: none; /* Reset doesn't need elevation */
    }
     #reset-building:hover:not(:disabled) { background-color: #c82333; transform: translateY(-2px); }


     .controls button:disabled {
         background-color: #cccccc !important; /* Override specific colors */
         cursor: not-allowed;
         box-shadow: none;
         transform: none;
     }
     .controls button:active:not(:disabled) {
         transform: translateY(1px); /* Press effect */
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    .feedback {
        margin-top: 20px;
        font-size: 1.1em;
        color: #555;
        min-height: 1.8em; /* Reserve more space */
        text-align: center;
        font-weight: bold;
    }

    #explanation-toggle {
         display: block;
         margin: 30px auto;
         padding: 12px 25px;
         font-size: 1.1em;
         cursor: pointer;
         border: none;
         border-radius: 6px;
         background-color: #007bff; /* Match primary button color */
         color: white;
         transition: background-color 0.3s ease, transform 0.1s ease;
         font-weight: bold;
         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
     #explanation-toggle:hover {
         background-color: #0056b3;
         transform: translateY(-2px);
     }
    #explanation-toggle:active {
         transform: translateY(1px);
         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
     }


    #full-explanation {
        margin-top: 20px;
        padding: 20px;
        border: none; /* Remove basic border */
        border-radius: 12px;
        background-color: #fefefe; /* White background for text */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        display: none; /* Initially hidden */
        line-height: 1.7;
        color: #333;
    }

    #full-explanation h2 {
        color: #333;
        margin-top: 0;
        margin-bottom: 15px;
        padding-bottom: 8px;
        border-bottom: 2px solid #eee;
        font-size: 1.6em;
        font-weight: bold;
        text-align: right; /* Ensure RTL alignment */
    }
     #full-explanation h3 {
        color: #555;
        margin-top: 20px;
        margin-bottom: 10px;
        padding-bottom: 5px;
        border-bottom: 1px solid #eee;
        font-size: 1.3em;
        font-weight: bold;
        text-align: right; /* Ensure RTL alignment */
    }

    #full-explanation p {
        margin-bottom: 15px;
        text-align: right; /* Ensure RTL alignment */
    }

    #full-explanation ul {
         margin-bottom: 15px;
         padding-right: 20px; /* Indent list */
         text-align: right;
    }
    #full-explanation li {
        margin-bottom: 8px;
        text-align: right; /* Ensure RTL alignment */
    }
</style>

<button id="explanation-toggle">הצג/הסתר הסבר מלא</button>

<div id="full-explanation" class="hidden">
    <h2>הסבר מעמיק: סודות הבנייה לגובה של הקתדרלה הגותית</h2>

    <h3>שאיפה לגובה ואור - הולדת הסגנון הגותי</h3>
    <p>דמיינו את אירופה בימי הביניים המאוחרים. ערים גדלות, אמונה מתחזקת, והשאיפה היא לבנות כנסיות שלא רק יכילו את הקהילה, אלא גם ישאו את הנפש כלפי שמיים. הסגנון הרומנסקי שקדם לגותיקה בנה מבנים מרשימים אך כבדים ומאסיביים, עם קירות עבים וחלונות קטנים, בגלל הצורך לתמוך בתקרות אבן כבדות. אדריכלי הגותיקה חלמו על משהו אחר לגמרי: מבנים שיתמררו לגובה מסחרר, עם קירות שנעלמים כמעט לחלוטין לטובת חלונות ענק שטופי אור. אבל איך עושים את זה כשלרשותכם רק אבן, עץ וכוח אדם?</p>

    <h3>האתגר הפיזיקלי: כוח הכבידה מול שאיפת האבן</h3>
    <p>בניית קירות גבוהים ודקים היא מתכון לקריסה. המשקל העצום של האבן דוחף כלפי מטה (כוח אנכי), וצורת הקשתות והקמרונות שיוצרות את התקרה דוחפת גם לצדדים (כוח אופקי). הרומנסק התמודד עם הכוחות האופקיים באמצעות קירות עבים מאוד. הגותיקה רצתה קירות דקים. פתרון הנדסי גאוני היה הכרחי כדי "לתפוס" את הכוחות הללו ולמנוע מהמבנה להתפרק.</p>

    <h3>קמרונות צלעות (Rib Vaults): השלד המפזר עומס</h3>
    <p>במקום לבנות תקרה אחידה וכבדה, הגותים בנו אותה על בסיס "שלד" של קשתות אלכסוניות מאבן - קמרונות הצלעות. החללים שבין הצלעות מולאו באבן קלה יותר.
        <ul>
            <li>**איך זה עובד?** הצלעות הן כמו מסלולים מתוחכמים שאוספים את כל העומס והדחיפה מהתקרה ומנתבים אותם באופן מרוכז לנקודות ספציפיות מאוד – ממש מעל ראשי העמודים התומכים.</li>
            <li>**היתרון:** הדבר מאפשר להשתמש בפחות אבן, להפחית את המשקל הכולל של התקרה, ובעיקר – לרכז את העומס בנקודות במקום לפזר אותו לאורך כל הקיר. זה המפתח לקירות דקים וגבוהים יותר!</li>
        </ul>
    </p>

    <h3>תמיכות דואות (Flying Buttresses): הידיים שתופסות את הקירות</h3>
    <p>גם אחרי שקמרונות הצלעות ריכזו את העומס לנקודות ספציפיות, בנקודות אלו נוצר עדיין כוח דחיפה אופקי עצום כלפי חוץ, שהיה עלול להפיל את הקירות הגבוהים והדקים. כאן נכנסות לתמונה התמיכות הדואות - אחת ההמצאות המפורסמות ביותר של הגותיקה.
        <ul>
            <li>**מה הן עושות?** אלו קשתות אבן חיצוניות, אלגנטיות במראן, הנשענות על עמודי תמיכה כבדים (Piers) המוצבים מחוץ למבנה. הן מקבלות על עצמן את כוח הדחיפה האופקי שמגיע מראשי הקמרונות (דרך הקירות הגבוהים) ומעבירות אותו הלאה, כלפי מטה ואל הקרקע, הרחק מהקירות עצמם.</li>
            <li>**איך צורתן מסייעת?** צורת הקשת מאפשרת להן "לדאות" מעל האמבולטוריום או האגפים הנמוכים יותר, ולהגיע בדיוק לנקודות בהן כוח הדחיפה הוא החזק ביותר. הן כמו פיגומים חיצוניים קבועים, רק הרבה יותר יפים ומהווים חלק בלתי נפרד מהמערכת המבנית. בזכותן, הקירות הפנימיים משוחררים כמעט לגמרי מהצורך לשאת עומס אופקי!</li>
        </ul>
    </p>

    <h3>ויטראז'ים (Stained Glass): קירות של אור וצבע</h3>
    <p>כאשר העומס האנכי נישא בעיקר על ידי העמודים הפנימיים, והעומס האופקי מנוטרל על ידי התמיכות הדואות החיצוניות – הקירות בין נקודות התמיכה הופכים להיות כמעט מיותרים מבחינה מבנית! זהו הרגע בו אדריכלי הגותיקה יכלו להגשים את חלומם: לפתוח שטחי ענק בקירות ולהחליף את האבן בחלונות!
        <ul>
            <li>**החלונות העצומים:** מערכת התמיכה הגותית היא זו שאפשרה יצירת חלונות ויטראז' עצומים בגודלם, שהם סימן ההיכר של הסגנון.</li>
            <li>**מעבר לאסתטיקה:** הויטראז'ים לא רק שטפו את פנים הקתדרלה באור מסונן וצבעוני, ויצרו אווירה מיסטית עוצרת נשימה. הם גם שימשו כ"ספר ענק" לעם הפשוט, כשהם מספרים את סיפורי התנ"ך והברית החדשה בתמונות מרהיבות עין, לקהל שרובו המכריע לא ידע קרוא וכתוב.</li>
        </ul>
    </p>

    <h3>הקתדרלה השלמה: פלא של הנדסה ואמנות</h3>
    <p>היופי של הקתדרלה הגותית טמון בשילוב ההרמוני בין כל הרכיבים הללו. העמודים הפנימיים, קמרונות הצלעות, התמיכות הדואות והקירות הדקים עם הויטראז'ים - כולם עובדים יחד כמערכת אחת, גאונית ומאוזנת. הקמרונות מנתבים את הכוח, העמודים מחזיקים את האנכי, התמיכות מנטרלות את האופקי, והקירות הפנויים מתמלאים באור. התוצאה היא מבנים מונומנטליים, קלילים למראה, שופעים אור וצבע, שנראים כאילו הם מרחפים מעלה - עדות מדהימה ליצירתיות, לתושייה ההנדסית ולשאיפה הרוחנית של בוני ימי הביניים.</p>
</div>


<script>
    document.addEventListener('DOMContentLoaded', () => {
        const buildingArea = document.querySelector('.building-area');
        const columns = buildingArea.querySelectorAll('.column');
        const vaults = buildingArea.querySelector('.rib-vault');
        const buttresses = buildingArea.querySelectorAll('.flying-buttress');
        const glass = buildingArea.querySelectorAll('.stained-glass');

        const forceVertical = buildingArea.querySelector('.force-vertical');
        const forceHorizontalLeft = buildingArea.querySelector('.force-horizontal-left');
        const forceHorizontalRight = buildingArea.querySelector('.force-horizontal-right');
        const forceCounterLeft = buildingArea.querySelector('.force-counter-left');
        const forceCounterRight = buildingArea.querySelector('.force-counter-right');

        const indicatorLeft = buildingArea.querySelector('.indicator-left');
        const indicatorRight = buildingArea.querySelector('.indicator-right');


        const addColumnsBtn = document.getElementById('add-columns');
        const addVaultsBtn = document.getElementById('add-vaults');
        const addButtressesBtn = document.getElementById('add-buttresses');
        const addGlassBtn = document.getElementById('add-glass');
        const resetBtn = document.getElementById('reset-building');
        const feedbackDiv = document.querySelector('.feedback');
        const explanationToggleBtn = document.getElementById('explanation-toggle');
        const explanationDiv = document.getElementById('full-explanation');

        let step = 0; // 0: Base, 1: Columns, 2: Vaults, 3: Buttresses, 4: Glass

        function updateUI() {
            // Reset all element visibility and state classes first
            columns.forEach(el => { el.classList.add('hidden'); el.classList.remove('visible'); });
            vaults.classList.add('hidden'); vaults.classList.remove('visible');
            buttresses.forEach(el => { el.classList.add('hidden'); el.classList.remove('visible'); });
            glass.forEach(el => { el.classList.add('hidden'); el.classList.remove('visible'); });

            // Reset force indicators
            [forceVertical, forceHorizontalLeft, forceHorizontalRight, forceCounterLeft, forceCounterRight].forEach(f => f.classList.add('hidden'));

            // Reset stability indicators
            [indicatorLeft, indicatorRight].forEach(ind => {
                ind.classList.add('hidden');
                ind.classList.remove('unstable', 'stable');
                 ind.style.animation = ''; // Remove animation
            });

            // Reset button visibility
            addColumnsBtn.classList.add('hidden');
            addVaultsBtn.classList.add('hidden');
            addButtressesBtn.classList.add('hidden');
            addGlassBtn.classList.add('hidden');

            feedbackDiv.textContent = ''; // Clear feedback

            // Update based on step
            if (step === 0) {
                // Base is always visible (part of building-area background/base div)
                addColumnsBtn.classList.remove('hidden');
                feedbackDiv.textContent = 'מתחילים לבנות! יש לנו בסיס ויסודות יציבים.';
            } else if (step === 1) {
                columns.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });
                addVaultsBtn.classList.remove('hidden');
                feedbackDiv.textContent = 'הוספנו את העמודים התומכים. הם מוכנים לשאת את משקל התקרה הגבוהה.';
            } else if (step === 2) {
                columns.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });
                vaults.classList.remove('hidden'); vaults.classList.add('visible');

                // Show vertical and horizontal forces
                forceVertical.classList.remove('hidden');
                forceHorizontalLeft.classList.remove('hidden');
                forceHorizontalRight.classList.remove('hidden');

                // Indicate instability
                indicatorLeft.classList.remove('hidden');
                indicatorRight.classList.remove('hidden');
                indicatorLeft.classList.add('unstable');
                indicatorRight.classList.add('unstable');
                 indicatorLeft.style.animation = 'pulse-red 1s infinite';
                 indicatorRight.style.animation = 'pulse-red 1s infinite';


                addButtressesBtn.classList.remove('hidden');
                feedbackDiv.textContent = 'הקמרון מותקן! שימו לב לכוחות הדחיפה האופקיים החזקים שמאיימים להפיל את הקירות הדקים...';
            } else if (step === 3) {
                columns.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });
                vaults.classList.remove('hidden'); vaults.classList.add('visible');
                buttresses.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });

                 // Show all forces
                forceVertical.classList.remove('hidden');
                forceHorizontalLeft.classList.remove('hidden');
                forceHorizontalRight.classList.remove('hidden');
                forceCounterLeft.classList.remove('hidden');
                forceCounterRight.classList.remove('hidden');


                // Indicate stability
                indicatorLeft.classList.remove('hidden');
                indicatorRight.classList.remove('hidden');
                indicatorLeft.classList.remove('unstable');
                indicatorRight.classList.remove('unstable');
                indicatorLeft.classList.add('stable');
                indicatorRight.classList.add('stable');
                 indicatorLeft.style.animation = 'pulse-green 1s infinite';
                 indicatorRight.style.animation = 'pulse-green 1s infinite';


                addGlassBtn.classList.remove('hidden');
                feedbackDiv.textContent = 'התמיכות הדואות נכנסו לפעולה! הן מנטרלות את הדחיפה האופקית והמבנה יציב. עכשיו אפשר להוסיף חלונות ענק!';
            } else if (step === 4) {
                 columns.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });
                vaults.classList.remove('hidden'); vaults.classList.add('visible');
                buttresses.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });
                 glass.forEach(el => { el.classList.remove('hidden'); el.classList.add('visible'); });

                 // Show all forces (representing the balanced system)
                forceVertical.classList.remove('hidden');
                forceHorizontalLeft.classList.remove('hidden');
                forceHorizontalRight.classList.remove('hidden');
                forceCounterLeft.classList.remove('hidden');
                forceCounterRight.classList.remove('hidden');

                 // Show stable indicators
                 indicatorLeft.classList.remove('hidden');
                 indicatorRight.classList.remove('hidden');
                 indicatorLeft.classList.add('stable');
                 indicatorRight.classList.add('stable');
                  indicatorLeft.style.animation = 'pulse-green 1s infinite';
                  indicatorRight.style.animation = 'pulse-green 1s infinite';


                 feedbackDiv.textContent = 'המערכת הגותית מושלמת! עמודים, קמרונות, תמיכות וחלונות ענק - כולם עובדים יחד לפלא אדריכלי.';
            }
        }

        addColumnsBtn.addEventListener('click', () => {
            step = 1;
            updateUI();
        });

        addVaultsBtn.addEventListener('click', () => {
            step = 2;
            updateUI();
        });

        addButtressesBtn.addEventListener('click', () => {
            step = 3;
            updateUI();
        });

        addGlassBtn.addEventListener('click', () => {
            step = 4;
            updateUI();
        });

        resetBtn.addEventListener('click', () => {
            step = 0;
            updateUI();
        });

        explanationToggleBtn.addEventListener('click', () => {
            explanationDiv.classList.toggle('hidden');
            const isHidden = explanationDiv.classList.contains('hidden');
            explanationToggleBtn.textContent = isHidden ? 'הצג הסבר מלא' : 'הסתר הסבר מלא';
        });


        // Initial state
        updateUI();
    });
</script>
---
```