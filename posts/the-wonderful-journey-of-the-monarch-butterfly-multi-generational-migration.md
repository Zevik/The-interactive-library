---
title: "המסע המופלא של פרפר המונרך: נדידה רב-דורית"
english_slug: the-wonderful-journey-of-the-monarch-butterfly-multi-generational-migration
category: "מדעי החיים / ביולוגיה"
tags:
  - נדידה
  - פרפרים
  - מונרך
  - אקולוגיה
  - חרקים
---

# המסע המופלא של פרפר המונרך: נדידה רב-דורית

דמיינו יצור קטן ושברירי, ששוקל פחות מגרם, יוצא למסע של אלפי קילומטרים ברחבי יבשת שלמה. כיצד ייתכן שפרפר מונרך יחיד מצליח לחצות מרחקים עצומים כל כך כדי להגיע לאתר חריפה במקסיקו, ולהימנע מסופות, טורפים ורעב בדרך? בואו נגלה את הסוד מאחורי אחת התופעות המדהימות בטבע, בחוויה אינטראקטיבית שתאפשר לכם לעקוב אחר המסע המופלא.

<div id="app-container">
    <div id="map">
        <div id="mexico-winter-site" class="map-marker" title="אתר החריפה במקסיקו"></div>
        <div id="south-us-region" class="map-region" title="דרום ארה''ב"></div>
        <div id="north-us-canada-region" class="map-region" title="צפון ארה''ב וקנדה"></div>
        <!-- Butterfly groups will be added here dynamically -->
    </div>
    <div id="controls">
        <button id="play-pause-btn">צא למסע</button>
        <button id="reset-btn">מסע חדש</button>
        <span id="simulation-info">יום: 0 | דור: 1</span>
    </div>
    <div id="info-box" class="hidden">
        <h2>מידע על קבוצה</h2>
        <p><strong>דור:</strong> <span id="info-generation">-</span></p>
        <p><strong>מצב:</strong> <span id="info-stage">-</span></p>
        <p><strong>מיקום:</strong> <span id="info-location">-</span></p>
        <p><strong>גיל (ימים):</strong> <span id="info-age">-</span></p>
    </div>
     <div id="app-title-overlay">נדידת פרפר המונרך</div>
</div>

<style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

     @keyframes fadeOut {
         0% { opacity: 1; transform: scale(1); }
         100% { opacity: 0; transform: scale(0.5); }
     }

    #app-container {
        width: 100%;
        max-width: 850px; /* Slightly wider */
        margin: 20px auto;
        border: 1px solid #333; /* Stronger border */
        border-radius: 10px;
        position: relative;
        font-family: 'Arial', sans-serif; /* Use a common font */
        background: linear-gradient(to bottom, #87ceeb 0%, #e0f7fa 50%, #a3c1a3 100%); /* Sky to land gradient */
        overflow: hidden;
        aspect-ratio: 16 / 10; /* More landscape aspect ratio */
        box-shadow: 0 8px 16px rgba(0,0,0,0.3); /* More pronounced shadow */
    }

     #app-title-overlay {
         position: absolute;
         top: 10px;
         left: 50%;
         transform: translateX(-50%);
         z-index: 25; /* Above everything else */
         font-size: 1.5em;
         font-weight: bold;
         color: #333;
         text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
     }

    #map {
        width: 100%;
        height: 100%;
        position: relative;
         /* Simple background to suggest geography */
         background:
            /* Canada */
            linear-gradient(to bottom, rgba(200, 220, 200, 0.5) 0%, rgba(200, 220, 200, 0.0) 20%) 0% 0% / 100% 100% no-repeat,
            /* Mexico/South */
            linear-gradient(to top, rgba(160, 190, 160, 0.5) 0%, rgba(160, 190, 160, 0.0) 20%) 0% 0% / 100% 100% no-repeat;
         /* Using gradients as overlay hints */
    }

    .map-marker {
        position: absolute;
        width: 15px;
        height: 15px;
        background-color: rgba(0, 100, 0, 0.8); /* Dark green */
        border: 2px solid #fff;
        border-radius: 50%;
        z-index: 5;
        transform: translate(-50%, -50%); /* Center marker on the exact point */
         box-shadow: 0 0 5px rgba(0,0,0,0.5);
    }

    #mexico-winter-site {
         /* Position manually based on params.regions.mexicoOverwintering */
         top: 85%;
         left: 50%;
         background-color: #006400; /* Darker green */
         width: 20px;
         height: 20px;
    }

    .map-region {
        position: absolute;
        border: 1px dashed rgba(0,0,0,0.3); /* Dashed border for regions */
        box-sizing: border-box; /* Include border in dimensions */
        pointer-events: none; /* Don't interfere with butterfly clicks */
         opacity: 0.5;
    }

    #south-us-region {
         top: 65%; left: 20%; width: 60%; height: 20%;
         border-color: rgba(0, 100, 0, 0.5);
    }

    #north-us-canada-region {
         top: 10%; left: 20%; width: 60%; height: 25%;
         border-color: rgba(0, 100, 0, 0.5);
    }


    .butterfly-group {
        position: absolute;
        width: 18px; /* Slightly larger */
        height: 18px;
        border-radius: 50%;
        background-color: #ff8c00; /* Orange */
        border: 2px solid rgba(255,255,255,0.8); /* White border */
        cursor: pointer;
        transition: top 0.8s linear, left 0.8s linear; /* Smoother, slightly slower movement */
        box-shadow: 0 0 8px rgba(255,140,0,0.6); /* Glowing effect */
        z-index: 10;
        display: flex; /* Use flex for centering */
        align-items: center;
        justify-content: center;
        color: #fff; /* Text color for generation number */
        font-size: 0.7em;
        font-weight: bold;
         user-select: none; /* Prevent text selection */
         animation: pulse 2s infinite ease-in-out; /* Subtle pulsing animation */
    }

     /* Specific states / types */
    .butterfly-group.super-gen {
        background-color: #8b0000; /* Dark Red */
        border-color: rgba(255,255,255,0.9);
        width: 24px; /* Larger */
        height: 24px;
        box-shadow: 0 0 12px rgba(139,0,0,0.8); /* Stronger glow */
         font-size: 0.9em;
         animation: pulse 1.5s infinite ease-in-out; /* Slightly faster pulse */
    }

    .butterfly-group.overwintering {
        background-color: #006400; /* Dark Green */
        border-color: rgba(255,255,255,0.9);
        box-shadow: 0 0 10px rgba(0,100,0,0.8);
        animation: none; /* Stop pulsing when still */
         opacity: 0.9; /* Slightly less prominent */
    }

    .butterfly-group.reproducing {
         animation: pulse 0.5s infinite alternate; /* Fast pulse when reproducing */
    }

     .butterfly-group.preparing-south {
          background-color: #ff4500; /* Orange-Red tint */
          animation: pulse 1s infinite ease-in-out;
     }

     .butterfly-group.dying {
         animation: fadeOut 1s forwards ease-out; /* Fade out animation */
         pointer-events: none; /* Cannot click dying groups */
     }


    #controls {
        position: absolute;
        bottom: 15px;
        left: 50%;
        transform: translateX(-50%); /* Center controls */
        background: rgba(255, 255, 255, 0.95); /* More opaque */
        padding: 12px 20px; /* More padding */
        border-radius: 8px;
        z-index: 20;
        display: flex;
        align-items: center;
        gap: 15px; /* More space between controls */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

     #controls button {
         background-color: #007bff; /* Blue button */
         color: white;
         border: none;
         border-radius: 5px;
         padding: 10px 15px;
         font-size: 1em;
         cursor: pointer;
         transition: background-color 0.3s ease;
     }

     #controls button:hover {
         background-color: #0056b3;
     }

     #controls button:active {
         background-color: #004085;
     }

    #simulation-info {
        font-weight: bold;
        color: #333;
        font-size: 1.1em;
    }

    #info-box {
        position: absolute;
        top: 15px;
        right: 15px;
        background: rgba(255, 255, 255, 0.95); /* More opaque */
        padding: 15px; /* More padding */
        border-radius: 8px;
        z-index: 20;
        border: 1px solid #555; /* Darker border */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
         width: 200px; /* Fixed width */
         pointer-events: none; /* Do not block clicks on map below */
    }

    #info-box.hidden {
        display: none;
    }

    #info-box h2 {
        margin-top: 0;
        font-size: 1.2em;
        color: #0056b3;
        border-bottom: 1px solid #ccc;
        padding-bottom: 5px;
        margin-bottom: 10px;
    }

    #info-box p {
        margin: 8px 0; /* More spacing */
        font-size: 0.95em;
        line-height: 1.4;
    }

     #info-box strong {
         color: #555;
     }


    #toggle-explanation {
        display: block;
        margin: 30px auto 10px auto; /* More vertical margin */
        padding: 12px 20px;
        font-size: 1.1em;
        cursor: pointer;
         background-color: #f0f0f0;
         border: 1px solid #ccc;
         border-radius: 5px;
         transition: background-color 0.3s ease;
    }

     #toggle-explanation:hover {
         background-color: #e0e0e0;
     }


    #explanation {
        margin-top: 20px;
        border-top: 1px solid #eee; /* Lighter border */
        padding-top: 20px;
        line-height: 1.6; /* More comfortable reading */
        color: #333;
    }

    #explanation h2 {
        color: #0056b3;
        margin-bottom: 15px;
    }

     #explanation h3 {
         color: #007bff;
         margin-top: 20px;
         margin-bottom: 10px;
     }

     #explanation p {
         margin-bottom: 15px;
     }

     /* Style for highlighting key terms */
     #explanation strong {
         color: #555;
     }


</style>

<button id="toggle-explanation">הצג הסבר מפורט על הנדידה</button>

<div id="explanation" style="display: none;">
    <h2>המסע המופלא של פרפר המונרך: נדידה רב-דורית</h2>

    <p>פרפר המונרך (Danaus plexippus) הוא אחד החרקים המוכרים ביותר בצפון אמריקה, בעיקר בזכות צבעיו הכתומים והשחורים הבולטים, ונדידתו המדהימה שהיא אחת התופעות המרשימות בטבע.</p>

    <h3>היקף הנדידה</h3>
    <p>בכל סתיו, מיליוני פרפרי מונרך יוצאים למסע של אלפי קילומטרים מקנדה ומארצות הברית אל אתרי חריפה מוגנים ביערות עצי האויימל (Oyamel fir) בהרי מרכז מקסיקו. זהו אחד המסעות הארוכים ביותר המוכרים בעולם החרקים.</p>

    <h3>הסוד: זו אינה נדידה של פרט בודד הלוך ושוב</h3>
    <p>בניגוד לנדידות רבות אחרות בטבע (כמו אצל ציפורים), מסע הלוך ושוב של פרפר המונרך אורך שנה שלמה, אך אינו מבוצע על ידי פרט בודד. פרפר מונרך רגיל חי רק מספר שבועות.</p>

    <h3>הנדידה הרב-דורית צפונה (אביב-קיץ)</h3>
    <p>באביב, הפרפרים ששרדו את החורף במקסיקו (אותו "דור סופר" מיוחד) מתחילים את המסע צפונה. הם טסים מאות קילומטרים, בעיקר עד דרום ארצות הברית, שם הם מטילים את הביצים הראשונות של השנה על צמחי רכפתן (Milkweed), מזונם היחיד של הזחלים. לאחר ההטלה, פרפרים אלו (דור הסופר המקורי) מתים. מהביצים בוקע דור חדש (דור 1 של השנה), שגדל, הופך לפרפר, וממשיך את המסע צפונה מעט יותר. תהליך זה חוזר על עצמו 3-4 פעמים במהלך האביב והקיץ. כל דור חדש נולד מעט צפונה יותר מקודמו, ובכך האוכלוסייה מתפשטת בהדרגה צפונה, ומגיעה עד קנדה בסוף הקיץ.</p>

    <h3>'דור הסופר'</h3>
    <p>הפרפרים שנולדים בסוף הקיץ בצפון ארצות הברית ודרום קנדה הם דור מיוחד המכונה <strong>'דור הסופר'</strong>. פרפרים אלו שונים פיזיולוגית: הם אינם מתרבים מיד לאחר הבגרות, יש להם מאגרי שומן גדולים יותר, והם יכולים לחיות עד 9 חודשים (במקום שבועות בודדים). דור זה הוא שמבצע את המסע הארוך והרציף דרומה, לעיתים מעל 4,000 קילומטרים, אל אתרי החריפה במקסיקו. המסע מתבצע על ידי דור יחיד זה בלבד.</p>

    <h3>אתרי החריפה במקסיקו</h3>
    <p>המסע מסתיים ביערות הרריים במרכז מקסיקו, בגובה של כ-3,000 מטרים. מיליוני פרפרים מתקבצים על עצי האויימל, יוצרים אשכולות ענק על הענפים, ומבלים שם את חודשי החורף במצב של חוסר פעילות יחסית (דיאפאוזה). הטמפרטורה והלחות ביערות אלו אידיאליות להישרדותם במהלך החורף.</p>

    <h3>המסע חזרה צפונה (אביב)</h3>
    <p>באביב, כשהטמפרטורות עולות ואורך היום מתארך, 'דור הסופר' מתעורר, מתחיל את מסעו חזרה צפונה, ומחפש צמחי רכפתן. כשהוא מגיע לדרום ארצות הברית, הוא מטיל את ביציו (שהופכות לדור הראשון של השנה החדשה) ומת. דור זה ממשיך את הנדידה צפונה, וחוזר חלילה.</p>

    <h3>איומים ושימור</h3>
    <p>נדידת המונרך עומדת בפני איומים רבים, כולל: אובדן בתי גידול (בעיקר עקב שימוש בחומרי הדברה שקוטלים צמחי רכפתן בשטחים חקלאיים), כריתת יערות באתרי החריפה במקסיקו, שינויי אקלים והשפעתם על עיתוי הפריחה של צמחי רכפתן ותנאי החריפה, ושימוש נרחב בקוטלי חרקים. מאמצי שימור כוללים שיקום בתי גידול, נטיעת רכפתן ועצים באתרי החריפה, והעלאת מודעות ציבורית.</p>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const appContainer = document.getElementById('app-container');
        const mapDiv = document.getElementById('map');
        const playPauseBtn = document.getElementById('play-pause-btn');
        const resetBtn = document.getElementById('reset-btn');
        const simulationInfoSpan = document.getElementById('simulation-info');
        const infoBox = document.getElementById('info-box');
        const infoGenerationSpan = document.getElementById('info-generation');
        const infoStageSpan = document.getElementById('info-stage');
        const infoLocationSpan = document.getElementById('info-location');
         const infoAgeSpan = document.getElementById('info-age');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        let simulationState = {
            day: 0, // Day of the simulation start (represents day of the year)
            isPlaying: false,
            butterflyGroups: [],
            currentGenerationDisplay: 1,
            animationFrameId: null,
            speedMultiplier: 5, // Days per frame (lower = slower, higher = faster)
            lastUpdateTime: performance.now(),
            groupCounter: 0 // Unique ID counter for groups
        };

        // --- Map Coordinates Simulation Areas (Relative % of mapDiv) ---
        // These are rough conceptual areas for the simulation logic
        const regions = {
            southUS_northMexico: { topMin: 65, topMax: 85, leftMin: 20, leftMax: 80 },
            centralUS: { topMin: 35, topMax: 65, leftMin: 20, leftMax: 80 },
            northUS_southCanada: { topMin: 10, topMax: 35, leftMin: 20, leftMax: 80 },
            mexicoOverwintering: { top: 85, left: 50 } // Specific point
        };

        // --- Simulation Parameters (tuned for visual flow) ---
        const params = {
            gen1_start_day: 60, // Approx March 1st
            gen_lifespan_days: 35, // approx lifespan for normal generations (adjusted for visual flow)
            gen1_reproduce_latitude_top: 60, // Gen 1 reproduces when reaching this 'latitude' (lower top %)
            gen2_reproduce_latitude_top: 45,
            gen3_reproduce_latitude_top: 25,
             gen4_reproduce_latitude_top: 15, // Gen 4 reaches furthest north

            superGen_form_day_start: 225, // Approx August 15th
            superGen_form_day_end: 270, // Approx Sept 30th
            superGen_form_latitude_top: 30, // Approx north limit where super gen forms
            superGen_lifespan_days: 270, // approx 9 months from formation

            migration_north_speed_percent_per_day: 0.15, // % of map dimension per day
             migration_south_speed_percent_per_day: 0.3, // South migration is faster

            overwintering_arrival_day_min: 300, // Late Oct/Nov
            overwintering_departure_day_min: 60, // Early Spring (March) of next year
            superGen_return_reproduce_latitude_top: 65, // Super gen reproduces back in south US
             reproduction_duration_days: 5, // How long a group is in 'reproducing' state before death
        };

         // --- Helper to get regional state text ---
        function getRegionText(posTop, posLeft) {
             if (Math.sqrt(Math.pow(posTop - regions.mexicoOverwintering.top, 2) + Math.pow(posLeft - regions.mexicoOverwintering.left, 2)) < 5) {
                 return 'באתר החריפה במקסיקו';
             }
             if (posTop > regions.southUS_northMexico.topMin) return 'בדרום ארה"ב';
             if (posTop > regions.centralUS.topMin) return 'במרכז ארה"ב';
             if (posTop > regions.northUS_southCanada.topMin) return 'בצפון ארה"ב';
             return 'בקנדה'; // North of northUS_southCanada region
        }


        // --- Butterfly Group Class/Structure ---
        function createButterflyGroup(generation, type, startPos, dayBorn) {
            const groupDiv = document.createElement('div');
            groupDiv.classList.add('butterfly-group');
            groupDiv.dataset.id = simulationState.groupCounter++; // Assign unique ID
            groupDiv.dataset.generation = generation;
            groupDiv.dataset.type = type;
            groupDiv.dataset.dayBorn = dayBorn;
            groupDiv.dataset.state = 'moving_north'; // Initial state for spring groups
             groupDiv.textContent = generation; // Display generation number inside circle

            groupDiv.style.top = `${startPos.top}%`;
            groupDiv.style.left = `${startPos.left}%`;


            groupDiv.addEventListener('click', () => showInfoBox(groupDiv));
             groupDiv.addEventListener('mouseover', () => showInfoBox(groupDiv)); // Show on hover too
             groupDiv.addEventListener('mouseout', () => hideInfoBox()); // Hide on mouseout

            mapDiv.appendChild(groupDiv);

            return {
                id: parseInt(groupDiv.dataset.id, 10),
                element: groupDiv,
                generation: generation,
                type: type,
                pos: { top: startPos.top, left: startPos.left }, // current position {top: %, left: %}
                dayBorn: dayBorn, // Day the group was created or transitioned to super
                state: 'moving_north', // 'moving_north', 'reproducing', 'moving_south', 'overwintering', 'dead', 'preparing_south', 'dying'
                 reproductionStartDay: null, // To track reproduction state duration
                 overwinteringArrivalDay: null, // To track overwintering duration
                 deathDay: null, // To track when death animation should finish
            };
        }

        // --- Simulation Logic ---
        function initSimulation() {
            simulationState.day = params.gen1_start_day; // Start simulation in early spring
            simulationState.isPlaying = false;
            simulationState.butterflyGroups.forEach(group => group.element.remove());
            simulationState.butterflyGroups = [];
            simulationState.currentGenerationDisplay = 1;
            cancelAnimationFrame(simulationState.animationFrameId);
            hideInfoBox(); // Ensure info box is hidden
             simulationState.groupCounter = 0; // Reset ID counter

            // Start with Gen 1 in the south in Spring
            const startPos = {
                 top: (regions.southUS_northMexico.topMin + regions.southUS_northMexico.topMax) / 2 + (Math.random() - 0.5) * 10,
                 left: (regions.southUS_northMexico.leftMin + regions.southUS_northMexico.leftMax) / 2 + (Math.random() - 0.5) * 20
            };
            // In a full cycle, the 'super' gen from the *previous* year lays the eggs for Gen 1.
            // So, we represent the arrival of the super gen and their reproduction starting the new year.
             // Let's create a 'super' group that has just arrived from overwintering and is about to reproduce.
             const returningSuperGenPos = {
                  top: params.superGen_return_reproduce_latitude_top + (Math.random() - 0.5) * 5,
                  left: regions.southUS_northMexico.leftMin + (regions.southUS_northMexico.leftMax - regions.southUS_northMexico.leftMin) * Math.random()
             };
             const returningSuperGroup = createButterflyGroup(4, 'super', returningSuperGenPos, simulationState.day - 240); // Assume they formed ~240 days ago
             returningSuperGroup.state = 'reproducing'; // They arrive and start reproducing immediately
             returningSuperGroup.reproductionStartDay = simulationState.day;
             returningSuperGroup.element.textContent = 'ס'; // 'S' for Super
             returningSuperGroup.element.classList.add('super-gen'); // Visual style
             simulationState.butterflyGroups.push(returningSuperGroup);

             // And immediately spawn the first generation from this super group
             spawnNewGeneration(returningSuperGroup, simulationState.day, 1);


            updateSimulationInfo();
            drawButterflies();
        }

         function spawnNewGeneration(parentGroup, spawnDay, generationNumber) {
             const newGenPos = {
                 top: parentGroup.pos.top + (Math.random() - 0.5) * 5, // New gen appears around parent location
                 left: parentGroup.pos.left + (Math.random() - 0.5) * 10
             };
              // Ensure new group is within map bounds
             newGenPos.top = Math.max(5, Math.min(95, newGenPos.top));
             newGenPos.left = Math.max(5, Math.min(95, newGenPos.left));

             const newGroup = createButterflyGroup(generationNumber, 'normal', newGenPos, spawnDay);
             newGroup.element.textContent = generationNumber; // Display generation number
              // Temporarily pulse the parent element visually? CSS handles the 'reproducing' class animation
             simulationState.butterflyGroups.push(newGroup);
              console.log(`Day ${Math.floor(spawnDay)}: Gen ${parentGroup.generation} (${parentGroup.type}) reproduces. New Gen ${generationNumber} born at (${newGenPos.top.toFixed(1)}%, ${newGenPos.left.toFixed(1)}%)`);

         }


        function updateSimulation(currentTime) {
            if (!simulationState.isPlaying) {
                 simulationState.animationFrameId = requestAnimationFrame(updateSimulation); // Keep the loop running even when paused for interaction/info box
                return;
            }

            const deltaTime = (currentTime - simulationState.lastUpdateTime) / 1000; // Delta time in seconds
            simulationState.lastUpdateTime = currentTime;

            const daysToAdvance = deltaTime * simulationState.speedMultiplier; // How many simulation days pass

            // Avoid huge jumps if tab was inactive
            if (daysToAdvance > 5) { // If more than 5 days would pass
                //console.warn(`Large delta time detected (${deltaTime.toFixed(2)}s), capping days advanced.`);
                daysToAdvance = 0.5; // Cap the max days advanced per frame
            }


            simulationState.day += daysToAdvance;

             const day = simulationState.day; // Use the updated day


            // Cap simulation after a full cycle is observed
             if (simulationState.day > params.gen1_start_day + 365) { // Run for just over one full year cycle from start
                 simulationState.isPlaying = false;
                 playPauseBtn.textContent = 'מסע חדש';
                 console.log("Simulation cycle complete.");
                 // Allow interaction with final state before reset
             }


            const newButterflies = [];
            let activeGenDisplay = 0; // Used to determine the highest active generation for display

            simulationState.butterflyGroups = simulationState.butterflyGroups.filter(group => {
                const age = day - group.dayBorn;
                let isAlive = true;

                // Death Logic
                if (group.state === 'reproducing' && day - group.reproductionStartDay >= params.reproduction_duration_days) {
                    isAlive = false; // Normal gens and returning super gen die after reproducing
                     group.element.classList.add('dying'); // Add dying animation class
                     group.deathDay = day; // Mark death time for animation
                } else if (group.type === 'normal' && age > params.gen_lifespan_days * 1.2) { // Safety check for normal gen death
                     isAlive = false;
                      group.element.classList.add('dying');
                      group.deathDay = day;
                } else if (group.type === 'super' && group.state !== 'reproducing' && day >= params.superGen_form_day_start + params.superGen_lifespan_days) {
                     // Super gen dies after its long lifespan if it didn't reproduce (e.g., failed migration)
                     isAlive = false;
                     group.element.classList.add('dying');
                     group.deathDay = day;
                }

                // Remove group element after dying animation completes
                 if (group.state === 'dying' && day - group.deathDay >= 1.5) { // 1.5 seconds for animation + cleanup
                     group.element.remove();
                     return false; // Remove group from array
                 }
                 if (group.state === 'dying') return true; // Keep group during dying animation


                // Update state and position
                switch (group.state) {
                    case 'moving_north':
                        // Move north (decrease top %)
                        group.pos.top -= params.migration_north_speed_percent_per_day * daysToAdvance;
                        // Simulate some random spread left/right
                        group.pos.left += (Math.random() - 0.5) * params.migration_north_speed_percent_per_day * daysToAdvance * 0.5;

                         // Clamp position within map bounds (rough)
                        group.pos.top = Math.max(5, group.pos.top);
                        group.pos.left = Math.max(5, Math.min(95, group.pos.left));

                        // Check for reproduction point (reaching target latitude based on generation)
                         if (group.type === 'normal') {
                            let reproductionLatitude = -1; // No reproduction point met yet
                            if (group.generation === 1 && group.pos.top <= params.gen1_reproduce_latitude_top) reproductionLatitude = params.gen1_reproduce_latitude_top;
                            else if (group.generation === 2 && group.pos.top <= params.gen2_reproduce_latitude_top) reproductionLatitude = params.gen2_reproduce_latitude_top;
                            else if (group.generation === 3 && group.pos.top <= params.gen3_reproduce_latitude_top) reproductionLatitude = params.gen3_reproduce_latitude_top;
                            else if (group.generation === 4 && group.pos.top <= params.gen4_reproduce_latitude_top) reproductionLatitude = params.gen4_reproduce_latitude_top;

                            if (reproductionLatitude !== -1) { // If a reproduction latitude was met
                                group.state = 'reproducing';
                                group.reproductionStartDay = day;
                                 // Spawn the new generation when entering the reproducing state
                                 spawnNewGeneration(group, day, group.generation + 1);
                            }
                        }

                         // Check if normal generation group should transition to 'super'
                         // This happens only for groups born late in summer in the north
                         if (group.type === 'normal' && day >= params.superGen_form_day_start && day <= params.superGen_form_day_end && group.pos.top <= params.superGen_form_latitude_top) {
                              // This group becomes the super gen
                               group.type = 'super';
                               group.element.classList.add('super-gen');
                               group.element.textContent = 'ס'; // Visual marker for super gen
                               group.state = 'preparing_south'; // State before migration
                               group.dayBorn = day; // Reset age reference for supergen lifespan calculation
                               console.log(`Day ${Math.floor(day)}: Gen ${group.generation} transitioned to Super Gen.`);
                               // Do NOT spawn new generation here, this group's fate is migration south
                         }

                        // If super gen returning from Mexico, check for reproduction point
                         if (group.type === 'super' && group.state === 'moving_north' && day >= params.gen1_start_day + 365 && group.pos.top >= params.superGen_return_reproduce_latitude_top) { // Use >= for moving south to north check
                             group.state = 'reproducing'; // Super gen laying eggs in south US
                             group.reproductionStartDay = day;
                             // This is Gen 1 of the *new* year cycle
                             spawnNewGeneration(group, day, 1);
                             group.element.classList.add('reproducing'); // Add reproducing animation
                         }

                        break;

                    case 'reproducing':
                        // Stay put while reproducing (implicitly handled by age check for death)
                        // Visual pulse handled by CSS class
                        group.element.classList.add('reproducing');
                        break;

                    case 'preparing_south':
                         group.element.classList.add('preparing-south');
                        // Wait for migration trigger day
                        if (day >= params.superGen_migration_south_day_start) {
                             group.state = 'moving_south';
                             group.element.classList.remove('preparing-south');
                             console.log(`Day ${Math.floor(day)}: Super Gen starts moving south.`);
                        } else {
                            // Linger in the north for a bit before starting south, maybe drift slowly south
                             group.pos.top += params.migration_north_speed_percent_per_day * daysToAdvance * 0.1; // Slow drift south
                             group.pos.left += (Math.random() - 0.5) * params.migration_north_speed_percent_per_day * daysToAdvance * 0.05;
                             group.pos.top = Math.max(5, Math.min(regions.southUS_northMexico.topMax, group.pos.top)); // Clamp within reasonable bounds
                             group.pos.left = Math.max(5, Math.min(95, group.pos.left));
                        }
                        break;

                    case 'moving_south':
                        group.element.classList.remove('reproducing', 'overwintering', 'preparing-south'); // Clean up old states
                        // Move south towards Mexico
                        const mexicoTop = regions.mexicoOverwintering.top;
                        const mexicoLeft = regions.mexicoOverwintering.left;
                        const currentTop = group.pos.top;
                        const currentLeft = group.pos.left;

                        const dy = mexicoTop - currentTop;
                        const dx = mexicoLeft - currentLeft;
                        const distance = Math.sqrt(dy*dy + dx*dx);

                        const moveAmount = params.migration_south_speed_percent_per_day * daysToAdvance; // Use south speed

                        if (distance > moveAmount * 1.5) { // Move towards the target if not already very close
                             const angle = Math.atan2(dy, dx);
                             group.pos.top += moveAmount * Math.sin(angle);
                             group.pos.left += moveAmount * Math.cos(angle);
                              // Add slight random deviation for natural look
                             group.pos.top += (Math.random() - 0.5) * moveAmount * 0.2;
                             group.pos.left += (Math.random() - 0.5) * moveAmount * 0.2;

                             // Clamp position within map bounds
                             group.pos.top = Math.max(5, Math.min(95, group.pos.top));
                             group.pos.left = Math.max(5, Math.min(95, group.pos.left));

                        } else {
                            // If very close, move directly to the target point
                            group.pos.top = mexicoTop;
                            group.pos.left = mexicoLeft;
                        }


                        // Check for arrival at overwintering site
                        const arrivalThreshold = 2; // % distance threshold
                         const currentDistanceToMexico = Math.sqrt(
                             Math.pow(group.pos.top - regions.mexicoOverwintering.top, 2) +
                             Math.pow(group.pos.left - regions.mexicoOverwintering.left, 2)
                         );

                        if (currentDistanceToMexico < arrivalThreshold && day >= params.overwintering_arrival_day_min) {
                            group.state = 'overwintering';
                            group.pos.top = regions.mexicoOverwintering.top + (Math.random() - 0.5) * arrivalThreshold * 0.5; // Cluster slightly around the point
                            group.pos.left = regions.mexicoOverwintering.left + (Math.random() - 0.5) * arrivalThreshold * 0.5;
                            group.element.classList.add('overwintering');
                            group.overwinteringArrivalDay = day;
                             console.log(`Day ${Math.floor(day)}: Super Gen arrived at overwintering site.`);
                        }
                        break;

                    case 'overwintering':
                        // Stay put at the overwintering site, possibly cluster more
                        group.element.classList.add('overwintering');
                         // Slight random drift within the overwintering area
                         if (Math.random() < 0.1) { // Only drift occasionally
                             const driftAmount = 0.1;
                              group.pos.top += (Math.random() - 0.5) * driftAmount;
                              group.pos.left += (Math.random() - 0.5) * driftAmount;
                              // Clamp drift within a small radius around the center point
                              const maxDriftRadius = 1.5; // % radius
                              const currentDriftDistance = Math.sqrt(
                                  Math.pow(group.pos.top - regions.mexicoOverwintering.top, 2) +
                                  Math.pow(group.pos.left - regions.mexicoOverwintering.left, 2)
                              );
                              if (currentDriftDistance > maxDriftRadius) {
                                  const angleToCenter = Math.atan2(regions.mexicoOverwintering.top - group.pos.top, regions.mexicoOverwintering.left - group.pos.left);
                                  group.pos.top += (currentDriftDistance - maxDriftRadius) * Math.sin(angleToCenter);
                                  group.pos.left += (currentDriftDistance - maxDriftRadius) * Math.cos(angleToCenter);
                              }

                              // Re-apply style transitions for the drift movement
                             group.element.style.transition = 'top 0.2s linear, left 0.2s linear';
                         } else {
                              // Reset transition for non-drift frames
                             group.element.style.transition = 'top 0.8s linear, left 0.8s linear'; // Restore normal transition
                         }


                        // Wait for spring to start moving north
                         // Need to handle the year change - check day against 365 + departure day
                        if (day >= params.overwintering_arrival_day_min && day % 365 >= params.overwintering_departure_day_min && group.state === 'overwintering') { // Check based on the current year's day count
                             group.state = 'moving_north'; // Now moving north in the new year
                             group.element.classList.remove('overwintering');
                             group.element.classList.add('super-gen'); // Keep super gen style
                              console.log(`Day ${Math.floor(day)}: Super Gen starts moving north in spring.`);
                         }
                        break;
                    case 'dead': // State should ideally be removed by filter before this
                    case 'dying':
                        // Let the dying animation play out. The filter will remove it later.
                        break;
                }

                // Determine the highest *normal* active generation for display
                let maxNormalGen = 0;
                simulationState.butterflyGroups.forEach(g => {
                    if (g.type === 'normal' && g.state !== 'dead' && g.state !== 'dying' && g.generation > maxNormalGen) {
                        maxNormalGen = g.generation;
                    }
                });

                // Determine overall display generation
                let currentGenDisplay = '';
                const superGenExists = simulationState.butterflyGroups.some(g => g.type === 'super' && g.state !== 'dead' && g.state !== 'dying');

                if (superGenExists) {
                    const superGroup = simulationState.butterflyGroups.find(g => g.type === 'super' && g.state !== 'dead' && g.state !== 'dying');
                    if (superGroup) {
                        switch(superGroup.state) {
                             case 'preparing_south':
                             case 'moving_south':
                                 currentGenDisplay = 'סופר (דרום)';
                                 break;
                             case 'overwintering':
                                currentGenDisplay = 'סופר (חורף)';
                                 break;
                             case 'moving_north': // Returning super gen
                             case 'reproducing': // Returning super gen reproducing
                                currentGenDisplay = 'סופר (חוזר)';
                                 break;
                            default:
                                currentGenDisplay = 'סופר';
                        }
                    } else {
                         currentGenDisplay = 'סופר'; // Should not happen if superGenExists is true
                    }
                } else if (maxNormalGen > 0) {
                    currentGenDisplay = maxNormalGen;
                } else {
                    // If no super gen and no normal gens exist after a full cycle attempt
                    currentGenDisplay = 'הסתיים';
                }


                simulationState.currentGenerationDisplay = currentGenDisplay; // Update the state display value


                return true; // Keep group unless marked for removal
            });

            simulationState.butterflyGroups.push(...newButterflies); // Add new groups

            // If simulation ended and no groups are left, reset button text
             if (!simulationState.isPlaying && simulationState.butterflyGroups.length === 0) {
                 playPauseBtn.textContent = 'מסע חדש';
                 simulationInfoSpan.textContent = `יום: ${Math.floor(simulationState.day % 365)} (שנה ${Math.floor(simulationState.day / 365) + 1}) | דור: הסתיים`;
             }


            drawButterflies();
            updateSimulationInfo();

            // The loop always continues now, but simulation logic runs only if isPlaying is true
            simulationState.animationFrameId = requestAnimationFrame(updateSimulation);

        }

        function drawButterflies() {
            simulationState.butterflyGroups.forEach(group => {
                group.element.style.top = `${group.pos.top}%`;
                group.element.style.left = `${group.pos.left}%`;

                 // Ensure correct class for visualization
                 if (group.type === 'super') {
                     group.element.classList.add('super-gen');
                     group.element.textContent = 'ס';
                 } else {
                      group.element.classList.remove('super-gen');
                      group.element.textContent = group.generation;
                 }
                 if (group.state === 'overwintering') {
                     group.element.classList.add('overwintering');
                 } else {
                     group.element.classList.remove('overwintering');
                 }
                 if (group.state === 'reproducing') {
                      group.element.classList.add('reproducing');
                 } else {
                      group.element.classList.remove('reproducing');
                 }
                 if (group.state === 'preparing_south') {
                      group.element.classList.add('preparing-south');
                 } else {
                      group.element.classList.remove('preparing-south');
                 }
                 if (group.state === 'dying') {
                      group.element.classList.add('dying');
                 } else {
                      group.element.classList.remove('dying');
                 }

            });
        }

        function updateSimulationInfo() {
             const dayDisplay = Math.floor(simulationState.day % 365); // Display day within a year cycle
             const yearDisplay = Math.floor(simulationState.day / 365) + 1; // Display year number (starts from 1)
             const generationDisplay = simulationState.currentGenerationDisplay;

            simulationInfoSpan.textContent = `יום: ${dayDisplay} (שנה ${yearDisplay}) | דור: ${generationDisplay}`;
        }

        function showInfoBox(groupElement) {
            const id = parseInt(groupElement.dataset.id, 10);
            const group = simulationState.butterflyGroups.find(g => g.id === id);

            if (!group || group.state === 'dying') {
                 hideInfoBox(); // Hide if group is dying or not found
                return;
            }

            infoGenerationSpan.textContent = group.generation + (group.type === 'super' ? ' (סופר)' : '');
            let stageText = '';
            switch (group.state) {
                case 'moving_north': stageText = 'נודד צפונה'; break;
                case 'reproducing': stageText = 'מתרבה'; break;
                case 'moving_south': stageText = 'נודד דרומה'; break;
                case 'overwintering': stageText = 'בחריפה במקסיקו'; break;
                case 'preparing_south': stageText = 'מתכונן לנדידת סתיו'; break;
                case 'dead': stageText = 'סיים את חייו'; break;
                case 'dying': stageText = 'גווע'; break; // Should hide before this state usually
                default: stageText = group.state;
            }
            infoStageSpan.textContent = stageText;
            // Use helper function for a more descriptive location
            infoLocationSpan.textContent = getRegionText(group.pos.top, group.pos.left); //`למעלה: ${group.pos.top.toFixed(1)}%, שמאל: ${group.pos.left.toFixed(1)}%`;
            infoAgeSpan.textContent = Math.floor(simulationState.day - group.dayBorn);

            infoBox.classList.remove('hidden');
        }

        function hideInfoBox() {
             infoBox.classList.add('hidden');
        }

        // --- Event Listeners ---
        playPauseBtn.addEventListener('click', () => {
             // If simulation is already finished, clicking starts a new one
             if (!simulationState.isPlaying && simulationState.butterflyGroups.length === 0 && simulationState.day >= params.gen1_start_day + 365) {
                 initSimulation();
                 simulationState.isPlaying = true;
                 playPauseBtn.textContent = 'השהה';
                 simulationState.lastUpdateTime = performance.now(); // Reset timer for smooth start
                 updateSimulation();
             } else {
                simulationState.isPlaying = !simulationState.isPlaying;
                playPauseBtn.textContent = simulationState.isPlaying ? 'השהה' : 'צא למסע';
                simulationState.lastUpdateTime = performance.now(); // Reset timer on pause/play for smooth timing
                 if (simulationState.isPlaying) {
                      updateSimulation(); // Ensure loop is running
                 }
             }
        });

        resetBtn.addEventListener('click', () => {
            initSimulation();
            playPauseBtn.textContent = 'צא למסע'; // Reset button text
             hideInfoBox();
        });

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר מפורט על הנדידה' : 'הצג הסבר מפורט על הנדידה';
        });

         // Hide info box on click outside (excluding control buttons)
         document.addEventListener('click', (event) => {
             let targetElement = event.target;
             let isClickInsideInfoBox = false;
             let isClickOnButterfly = false;
             let isClickOnControls = false; // Check if click is on controls

             while (targetElement) {
                 if (targetElement === infoBox) {
                     isClickInsideInfoBox = true;
                     break;
                 }
                  if (targetElement.classList && targetElement.classList.contains('butterfly-group')) {
                      isClickOnButterfly = true;
                      break;
                  }
                 if (targetElement === controls) { // Check against controls container
                     isClickOnControls = true;
                     break;
                 }
                 targetElement = targetElement.parentElement;
             }

             if (!infoBox.classList.contains('hidden') && !isClickInsideInfoBox && !isClickOnButterfly && !isClickOnControls) {
                 hideInfoBox();
             }
         });


        // --- Initialize ---
        initSimulation(); // Set up the initial state
        simulationState.lastUpdateTime = performance.now(); // Initialize last update time
        updateSimulation(performance.now()); // Start the animation loop (initially paused)
    });
</script>
```