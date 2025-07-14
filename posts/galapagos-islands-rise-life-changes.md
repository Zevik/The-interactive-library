---
title: "גלאפגוס: איים עולים, חיים משתנים"
english_slug: galapagos-islands-rise-life-changes
category: "מדעי החיים / ביולוגיה"
tags: אבולוציה, גלאפגוס, צ'ארלס דרווין, גיאולוגיה, אקולוגיה
---
# גלאפגוס: איים עולים, חיים משתנים

מסע אל איי גלאפגוס - ארכיפלג ששינה את ההיסטוריה של המדע! גלו כיצד כוחות אדירים מתחת למים יצרו מעבדת טבע יוצאת דופן שחשפה בפנינו את סודות האבולוציה. התנסו בסימולציה דינמית הממחישה את הקשר המרתק בין גיאולוגיה לביולוגיה.

<div id="galapagos-simulation">
    <svg id="simulation-svg" width="800" height="400" viewBox="0 0 800 400"></svg>
    <div class="controls">
        <label for="time-slider">זמן (אלפי שנים):</label>
        <input type="range" id="time-slider" min="0" max="120" value="0" step="0.1">
        <span id="current-time">0</span>
        <button id="play-pause-btn">התחילו!</button>
        <button id="reset-btn">איפוס</button>
    </div>
</div>

<button id="toggle-explanation">מה קורה כאן? הסבירו לי!</button>

<div id="explanation" style="display: none;">
    <h2>סודות גלאפגוס: מסע בין וולקניזם, זרמים ואבולוציה</h2>
    <p>איי גלאפגוס, פסיפס וולקני השוכן בלב האוקיינוס השקט, הם הרבה יותר מגן עדן לבעלי חיים. זהו שדה ניסויים טבעי ענק ופורץ דרך, ששימש השראה מרכזית לצ'ארלס דרווין וסייע לו לפענח את מנגנון הברירה הטבעית. הסימולציה שלפניכם ממחישה את שתי התופעות המרכזיות המעצבות את גלאפגוס: הגיאולוגיה הדינמית של הארכיפלג והאבולוציה המהירה של מינים המאכלסים אותו.</p>

    <h3>אדמה רוחשת: היווצרות האיים על "נקודה חמה"</h3>
    <ul>
        <li><strong>מוקד אנרגיה קבוע:</strong> מתחת לאיי גלאפגוס קיים אזור ספציפי במעטפת כדור הארץ, הנקרא 'נקודה חמה' (Hotspot). מנקודה זו, שאינה זזה, עולה מגמה חמה בעקביות.</li>
        <li><strong>מסע על פלטה טקטונית:</strong> בעוד הנקודה החמה נשארת במקומה, הלוח הטקטוני שמעליה (לוח נזקה) נע באיטיות בכיוון מזרח-דרום מזרח.</li>
        <li><strong>לידת איים חדשים:</strong> בכל פעם שהלוח החוצה את הנקודה החמה, המגמה פורצת אל קרקעית הים ויוצרת הרי געש ימיים. התפרצויות חוזרות בונות את ההר עד שהוא מבצבץ מעל פני המים - אי וולקני חדש נולד! בסימולציה שלנו, זה הרגע שבו מופיע אי חדש ליד הנקודה החמה.</li>
        <li><strong>שרשרת של זמן:</strong> התנועה המתמדת של הלוח מרחיקה את האיים שנוצרו מהנקודה החמה. ככל שהאי מתרחק, הוא מתבגר גיאולוגית, חשוף יותר לכוחות הטבע (גשם, רוח, גלי ים) ונשחק בהדרגה. הסימולציה מראה את האיים "נוסעים" מזרחה ומשתנים עם הזמן.</li>
        <li><strong>מערב צעיר, מזרח זקן:</strong> התוצאה היא שרשרת איים ייחודית: האיים המערביים ביותר (הקרובים לנקודה החמה) הם הצעירים והפעילים וולקנית, בעוד שהאיים המזרחיים הם העתיקים ביותר, לרוב שחוקים יותר, נמוכים יותר, ולעתים אף שוקעים בחזרה לים. בסימולציה, שימו לב כיצד האיים הופכים שטוחים ודהויים יותר ככל שהם מתרחקים.</li>
    </ul>

    <h3>מעבדת אבולוציה: החיים מתאימים את עצמם</h3>
    <ul>
        <li><strong>מסע אל הלא נודע:</strong> לחיים קשה להגיע לאיים מבודדים באמצע האוקיינוס. מינים יבשתיים (כמו זרעים, חרקים, או ציפורים קטנות) מגיעים בדרך כלל בטעות - נישאים על רוחות, צפים על רפסודות טבעיות של צמחייה, או נסחפים בזרמים. אם אוכלוסייה קטנה מצליחה להגיע לאי חדש ולהתבסס בו, היא נקראת 'אוכלוסייה מייסדת'. בסימולציה, הופעת הפרושים הראשונים על אי היא אירוע כזה.</li>
        <li><strong>בידוד יוצר גיוון:</strong> הבידוד הגאוגרפי בין איי גלאפגוס מקשה על מינים לנוע ולהתרבות בין איים שונים. כל אוכלוסייה באי מסוים מתפתחת בנפרד, נתונה לתנאים סביבתיים ייחודיים של אותו אי (זמינות מזון, בתי גידול, טורפים).</li>
        <li><strong>התאמה קטלנית:</strong> תהליך הברירה הטבעית נכנס לפעולה. פרטים באוכלוסייה שיש להם תכונות (המבוססות על גנטיקה) שמתאימות יותר לסביבה המקומית - למשל, מקור שמתאים לאכול זרעים קשים אם זה המזון היחיד, או יכולת לשרוד באקלים יבש - שורדים טוב יותר ומתרבים יותר, ומעבירים את התכונות הללו לדור הבא.</li>
        <li><strong>התפצלות מרהיבה:</strong> לאורך דורות רבים, התאמות שונות לאיים שונים מובילות לכך שאוכלוסיות שונות של אותו מין אב מתפתחות לכיוונים שונים ולבסוף הופכות למינים נפרדים. תהליך זה, שבו מין אחד "מתפצל" למינים רבים המותאמים לנישות אקולוגיות שונות בארכיפלג, נקרא 'התפצלות אבולוציונית' (Adaptive Radiation).</li>
        <li><strong>פרושי דרווין:</strong> הדוגמה המפורסמת ביותר היא 15 מיני הפרושים של גלאפגוס. הם ככל הנראה התפתחו ממין אב יחיד של פרוש שהגיע מהיבשת. השוני העצום בצורת מקורם (המותאם לאכילת חרקים, זרעים, צוף, או אפילו שימוש בכלים!), גודל גופם והתנהגותם הוא עדות מוחשית לכוחה של האבולוציה המתרחשת ב"מעבדה" הטבעית של איי גלאפגוס. שימו לב בסימולציה כיצד פרושים בצבעים שונים (המייצגים מינים שונים) מופיעים על איים שונים בהתאם לסביבה המקומית.</li>
    </ul>
    <p>גלאפגוס מזכיר לנו שוב ושוב כיצד כוחות גיאולוגיים אדירים ותהליכים ביולוגיים עדינים שזורים זה בזה, ויוצרים את השטיח העשיר והמגוון של החיים על פני כדור הארץ.</p>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');

    body {
        font-family: 'Varela Round', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #e0f7fa; /* Light cyan background */
    }

    h1, h2, h3 {
        color: #004d40; /* Dark cyan heading color */
        font-weight: bold;
    }

    #galapagos-simulation {
        margin: 20px auto;
        border: 2px solid #004d40; /* Dark cyan border */
        border-radius: 10px;
        position: relative;
        overflow: hidden;
        background: linear-gradient(to bottom, #4dd0e1, #00bcd4); /* Gradient ocean background */
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Soft shadow */
    }

    #simulation-svg {
        display: block;
        background-color: transparent; /* SVG shows the CSS background */
        /* Ensure SVG fills the container */
        width: 100%;
        height: 400px; /* Fixed height */
    }

    .controls {
        background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white background */
        padding: 15px;
        text-align: center;
        border-top: 1px solid #b2ebf2; /* Light border */
        display: flex; /* Use flexbox for alignment */
        justify-content: center; /* Center controls horizontally */
        align-items: center; /* Align controls vertically */
        flex-wrap: wrap; /* Allow controls to wrap on smaller screens */
    }

    .controls label {
        margin-right: 10px;
        font-weight: bold;
        color: #00796b; /* Teal color */
    }

    .controls input[type="range"] {
        width: 300px;
        margin-right: 15px;
        flex-grow: 1; /* Allow slider to take available space */
        max-width: 400px; /* Prevent slider from getting too wide */
    }

    #current-time {
        display: inline-block;
        width: 40px; /* Increased width for better readability */
        text-align: left;
        margin-right: 15px;
        font-weight: bold;
        color: #00796b; /* Teal color */
    }

    button {
        padding: 10px 20px; /* Larger padding */
        cursor: pointer;
        border: none;
        background-color: #00796b; /* Teal button */
        color: white;
        border-radius: 25px; /* Pill shape */
        margin: 5px;
        font-size: 1rem;
        transition: background-color 0.3s ease, transform 0.1s ease; /* Smooth transition */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    button:hover {
        background-color: #004d40; /* Darker teal on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    button:active {
        transform: scale(0.98); /* Slightly press button on click */
    }


    #toggle-explanation {
        display: block;
        margin: 20px auto;
        background-color: #e65100; /* Deep orange */
    }
     #toggle-explanation:hover {
        background-color: #bf360c; /* Darker orange */
    }


    #explanation {
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #b2ebf2; /* Light border */
        background-color: #ffffff; /* White background */
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    #explanation h2, #explanation h3 {
        color: #004d40; /* Dark cyan */
        margin-bottom: 10px;
    }

     #explanation h3 {
         margin-top: 20px;
     }

    #explanation ul {
        list-style-type: disc;
        margin-left: 30px;
        padding-left: 0;
    }

    #explanation li {
        margin-bottom: 10px;
        line-height: 1.5;
    }

    /* SVG element styles */
    .hotspot {
        fill: #ff7043; /* Deep orange */
        animation: pulse-hotspot 2s infinite cubic-bezier(0.4, 0, 0.6, 1) alternate; /* Smoother pulse */
        transform-box: fill-box;
        transform-origin: center;
    }

    @keyframes pulse-hotspot {
        0% { r: 12; opacity: 0.9; }
        100% { r: 18; opacity: 1; }
    }

     /* Style for young volcanic island hint */
    .volcanic-island {
        stroke: #e64a19; /* Reddish outline */
        stroke-width: 3px;
        stroke-dasharray: 5,5; /* Dashed line */
        animation: pulse-volcano 1s infinite ease-out alternate;
    }

    @keyframes pulse-volcano {
        from { stroke-dashoffset: 0; opacity: 1; }
        to { stroke-dashoffset: 10; opacity: 0.7; }
    }


    .island {
        fill: #8d6e63; /* Base brown color */
        transition: cx linear 0.2s, cy linear 0.2s, r linear 0.2s, fill linear 0.5s, opacity linear 0.5s; /* Smooth changes */
        stroke: #4e342e; /* Darker brown stroke */
        stroke-width: 1.5px;
        filter: drop-shadow(2px 2px 3px rgba(0,0,0,0.3)); /* Add a little shadow */
    }

    /* Island age appearance */
    .island.age-0 { fill: #a1887f; stroke: #5d4037; opacity: 1; } /* Youngest - reddish brown, prominent */
    .island.age-1 { fill: #bcaaa4; stroke: #795548; opacity: 0.95; } /* Middle age - browner, slightly less prominent */
    .island.age-2 { fill: #d7ccc8; stroke: #a1887f; opacity: 0.8; } /* Older - greyer brown, fading */
    .island.age-3 { fill: #f5f5f5; stroke: #d7ccc8; opacity: 0.5; } /* Oldest/eroded - very pale, low opacity */
     .island.age-4 { fill: #f5f5f5; stroke: #d7ccc8; opacity: 0.3; } /* Even older */


    .finch {
        fill: #212121; /* Default dark finch */
        r: 2.5; /* Slightly smaller dots */
        transition: cx linear 0.1s, cy linear 0.1s, fill linear 0.5s; /* Smoother finch movement */
    }

    /* Finch species colors - visually distinct */
    .finch.species-0 { fill: #388e3c; } /* Green - maybe seed eaters on younger islands */
    .finch.species-1 { fill: #1976d2; } /* Blue - maybe insectivores on mature islands */
    .finch.species-2 { fill: #d32f2f; } /* Red - maybe large beak on older islands */
    .finch.species-3 { fill: #fbc02d; } /* Yellow - maybe flower eaters */
    /* Add more species colors if needed based on age brackets */
    .finch.species-4 { fill: #7b1fa2; } /* Purple */
    .finch.species-5 { fill: #0097a7; } /* Cyan */


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const svg = document.getElementById('simulation-svg');
        const timeSlider = document.getElementById('time-slider');
        const currentTimeSpan = document.getElementById('current-time');
        const playPauseBtn = document.getElementById('play-pause-btn');
        const resetBtn = document.getElementById('reset-btn');
        const explanationDiv = document.getElementById('explanation');
        const toggleExplanationBtn = document.getElementById('toggle-explanation');

        const svgWidth = 800;
        const svgHeight = 400;
        const hotspotX = svgWidth * 0.15; // Hotspot fixed closer to the left
        const hotspotY = svgHeight / 2;
        const plateSpeed = 1.5; // Pixels per time unit (slower for smoother visualization)
        const islandCreationInterval = 15; // Create a new island every 15 time units
        const maxIslandAgeToShow = 100; // Islands become very faint or disappear after this age
        const maxIslandRadius = 45; // Max size for a young island
        const minIslandRadius = 5; // Min size before 'disappearing'
        const finchInitialArrivalTime = 40; // Finches arrive after time 40 (arbitrary)
        const finchPopulationPerIsland = 30; // Max finches per island type
        const finchSpreadChance = 0.7; // Probability a new island gets populated if finches exist
        const finchJitter = 5; // Max random offset for finch position around its relative spot

        let currentTime = 0;
        let isPlaying = false;
        let animationFrameId = null;
        let islands = []; // Array to store island data { id, creationTime, element, relX, relY, currentRadius, ageBracket }
        let finches = []; // Array to store finch data { id, islandId, speciesId, element, relX, relY } // relXY is offset from island center
        let lastCreationTime = 0; // Track time of last island creation to avoid duplicates

        // Draw static elements
        function drawHotspot() {
            // Ensure only one hotspot exists
            let hotspot = svg.querySelector('.hotspot');
            if (!hotspot) {
                 hotspot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                 hotspot.classList.add('hotspot');
                 svg.appendChild(hotspot);
            }
            hotspot.setAttribute('cx', hotspotX);
            hotspot.setAttribute('cy', hotspotY);
            // Radius and animation handled by CSS
        }

        // Update simulation based on current time
        function updateSimulation(time, isScrubbing = false) {
             // Clamp time to slider bounds
             const maxTime = parseFloat(timeSlider.max);
             time = Math.max(0, Math.min(maxTime, time));

            currentTimeSpan.textContent = Math.round(time);
            timeSlider.value = time;

            // Create new islands when time hits specific intervals
            const nextCreationTime = lastCreationTime + islandCreationInterval;
             if (time >= nextCreationTime && time > lastCreationTime + 0.1) { // Use tolerance for float comparisons
                  // Ensure we don't create duplicates or before the first interval
                  const newIslandTime = Math.floor(time / islandCreationInterval) * islandCreationInterval;
                  if (newIslandTime >= islandCreationInterval && newIslandTime > lastCreationTime) {
                       createIsland(newIslandTime);
                       lastCreationTime = newIslandTime; // Update last creation time

                       // Check for finch spread to this new island
                       if (newIslandTime >= finchInitialArrivalTime) {
                           const hasExistingFinches = finches.length > 0;
                           if (hasExistingFinches && Math.random() < finchSpreadChance) {
                                const newestIsland = islands[islands.length - 1]; // The one just created
                                if (newestIsland) { // Ensure island was successfully created
                                    // Determine species based on NEW island's age bracket *at this time*
                                    const ageBracket = getIslandAgeBracket(time - newestIsland.creationTime);
                                    addFinchesToIsland(newestIsland, ageBracket);
                                }
                           } else if (!hasExistingFinches && islands.length === 1 && newestIsland.creationTime >= finchInitialArrivalTime) {
                                // Initial finch arrival on the very first island that forms after min arrival time
                                const newestIsland = islands[islands.length - 1];
                                addFinchesToIsland(newestIsland, 0); // Assign species 0 for initial population
                           }
                       }
                  }
             }


            // Update island positions and appearance, and remove old islands
            islands = islands.filter(island => {
                const age = time - island.creationTime;

                // Skip islands that are "in the future" relative to current time
                if (age < 0) return true; // Keep future islands in array

                const displacementX = age * plateSpeed;
                const islandX = hotspotX + displacementX;
                const islandY = hotspotY + (Math.sin(island.id.split('-')[1] * 0.05 + island.id.split('-')[2] * 100) * 40); // Add persistent vertical variation based on creation ID

                // Remove islands that are too old or moved off-screen
                const currentRadius = Math.max(minIslandRadius, maxIslandRadius - age * 0.3); // Radius decreases with age
                island.currentRadius = currentRadius; // Store calculated radius
                island.x = islandX; // Store calculated position
                island.y = islandY;

                if (age > maxIslandAgeToShow || islandX > svgWidth + maxIslandRadius) {
                    // Remove island element and associated finches
                    if (island.element && island.element.parentNode === svg) {
                        svg.removeChild(island.element);
                    }
                    finches = finches.filter(finch => {
                        if (finch.islandId === island.id) {
                             if (finch.element && finch.element.parentNode === svg) {
                                  svg.removeChild(finch.element);
                             }
                             return false; // Remove finch from array
                        }
                        return true; // Keep finch
                    });
                    return false; // Remove island from array
                }


                // Create element if it doesn't exist yet (e.g., after scrubbing back)
                if (!island.element) {
                     createIslandElement(island);
                }

                // Update element attributes and appearance
                island.element.setAttribute('cx', islandX);
                island.element.setAttribute('cy', islandY);
                island.element.setAttribute('r', currentRadius);
                updateIslandAppearance(island.element, age);


                return true; // Keep island in array
            });


            // Update finch positions
            finches = finches.filter(finch => {
                 const island = islands.find(iso => iso.id === finch.islandId);
                 // If island is gone, remove finch (handled in island loop, but safety check)
                 if (!island) {
                     if (finch.element && finch.element.parentNode === svg) {
                          svg.removeChild(finch.element);
                     }
                     return false;
                 }

                 // Create element if it doesn't exist
                 if (!finch.element) {
                      createFinchElement(finch);
                 }

                 // Calculate finch position relative to island center + jitter
                 const islandX = island.x; // Use stored calculated position
                 const islandY = island.y;
                 const islandRadius = island.currentRadius;

                 // Use stored relative position, add jitter
                 const finchX = islandX + finch.relX + (Math.random() - 0.5) * finchJitter;
                 const finchY = islandY + finch.relY + (Math.random() - 0.5) * finchJitter;

                 finch.element.setAttribute('cx', finchX);
                 finch.element.setAttribute('cy', finchY);

                 // Update finch appearance (based on speciesId set at creation)
                 updateFinchAppearance(finch.element, finch.speciesId);

                 return true; // Keep finch
            });

             // Ensure hotspot is always drawn and on top? No, draw once.
             drawHotspot();
        }

        // Helper to get age bracket for appearance/speciation
        function getIslandAgeBracket(age) {
             if (age < islandCreationInterval * 1.5) return 0; // Young/Volcanic
             if (age < islandCreationInterval * 3) return 1; // Mature/Lush
             if (age < islandCreationInterval * 5) return 2; // Older/Drier
             if (age < islandCreationInterval * 7) return 3; // Very Old/Eroded
             return 4; // Near disappearance
        }


        // Create an island object
        function createIsland(creationTime) {
            const id = `island-${creationTime.toFixed(2)}-${Math.random().toFixed(4)}`; // Unique ID
            // Calculate initial relative position within a plausible range around the hotspot
             const angle = Math.random() * Math.PI / 2 - Math.PI / 4; // Angle roughly forward
             const radiusOffset = Math.random() * 30 + 10; // Distance from hotspot center
            const relX = radiusOffset * Math.cos(angle); // Relative X offset from hotspot
            const relY = radiusOffset * Math.sin(angle); // Relative Y offset from hotspot (for varied starting points)

            const newIsland = {
                 id,
                 creationTime: creationTime,
                 element: null,
                 relX: relX, // Use these to calculate starting point *relative* to hotspot
                 relY: relY,
                 x: 0, y: 0, currentRadius: 0, // Will be calculated in updateSimulation
                 ageBracket: 0 // Initial bracket
             };
            islands.push(newIsland);
             // Element will be created in updateSimulation when age is >= 0
        }

        function createIslandElement(island) {
             const element = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
             element.classList.add('island');
             svg.appendChild(element);
             island.element = element; // Link element to island object
        }

        function updateIslandAppearance(element, age) {
             const ageBracket = getIslandAgeBracket(age);
             // Update class based on age bracket
             element.classList.remove('age-0', 'age-1', 'age-2', 'age-3', 'age-4');
             element.classList.add(`age-${ageBracket}`);

             // Add/remove volcanic class
             if (ageBracket === 0) {
                  element.classList.add('volcanic-island');
             } else {
                  element.classList.remove('volcanic-island');
             }

             // Update radius is handled in updateSimulation based on age
        }


        // Add finches to an island
        function addFinchesToIsland(island, speciesId) {
             if (!island || !island.element) return; // Island must exist and have an element

             const islandId = island.id;
             const islandRadius = island.currentRadius;

             // Add finchPopulationPerIsland number of finches
             for (let i = 0; i < finchPopulationPerIsland ; i++) {
                 // Random position within island bounds (relative to island center)
                 const angle = Math.random() * Math.PI * 2;
                 const radius = Math.random() * (islandRadius * 0.8); // Stay within 80% of island radius
                 const relX = radius * Math.cos(angle);
                 const relY = radius * Math.sin(angle);

                 const finch = {
                      id: `finch-${islandId}-${i}`, // Unique ID within island
                      islandId: islandId,
                      speciesId: speciesId, // Assigned species
                      element: null, // Element created in updateSimulation
                      relX: relX, // Store relative position
                      relY: relY
                 };
                  finches.push(finch);
             }
        }

         function createFinchElement(finch) {
              const element = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
              element.classList.add('finch');
              svg.appendChild(element);
              finch.element = element;
         }

         function updateFinchAppearance(element, speciesId) {
              // Update color based on assigned species ID
              element.classList.remove('species-0', 'species-1', 'species-2', 'species-3', 'species-4', 'species-5'); // Clear all species classes
              element.classList.add(`species-${speciesId}`);
         }


        // Animation loop
        let lastTimestamp = 0;
        function animate(timestamp) {
            if (!isPlaying) {
                 animationFrameId = requestAnimationFrame(animate); // Keep requesting frames even when paused to update if controls change
                 lastTimestamp = timestamp; // Reset last timestamp on pause
                 return;
            }

            const deltaTime = timestamp - lastTimestamp;
            if (deltaTime < 16) { // Cap frame rate at roughly 60fps (1000/60 ≈ 16.6)
                 animationFrameId = requestAnimationFrame(animate);
                 return;
            }
            lastTimestamp = timestamp;

            const timeStep = deltaTime / 1000 * 5; // Advance simulation time based on real time delta (adjust 5 for speed)
            const maxTime = parseFloat(timeSlider.max);

            if (currentTime < maxTime) {
                currentTime += timeStep; // Advance time
                if (currentTime > maxTime) currentTime = maxTime; // Don't exceed max
                updateSimulation(currentTime);
                animationFrameId = requestAnimationFrame(animate);
            } else {
                isPlaying = false;
                playPauseBtn.textContent = 'התחילו!';
                 updateSimulation(maxTime); // Ensure final state is rendered
            }
        }

        // Event listeners
        playPauseBtn.addEventListener('click', () => {
            isPlaying = !isPlaying;
            if (isPlaying) {
                playPauseBtn.textContent = 'עצרו';
                // Reset lastTimestamp when starting playback to prevent large initial deltaTime
                lastTimestamp = performance.now();
                animate(); // Start the animation loop
            } else {
                playPauseBtn.textContent = 'התחילו!';
                // The animate function now handles pausing by returning early
            }
        });

        resetBtn.addEventListener('click', () => {
            isPlaying = false;
            playPauseBtn.textContent = 'התחילו!';
            cancelAnimationFrame(animationFrameId); // Stop any pending animation frame
            currentTime = 0;
            lastCreationTime = 0;
            // Remove all simulation elements except hotspot
            svg.querySelectorAll('.island, .finch').forEach(el => svg.removeChild(el));
            islands = [];
            finches = [];
            updateSimulation(currentTime); // Draw initial state (just hotspot)
            drawHotspot(); // Ensure hotspot is present
        });

        timeSlider.addEventListener('input', (event) => {
            isPlaying = false; // Pause on manual slider change
            playPauseBtn.textContent = 'התחילו!';
            cancelAnimationFrame(animationFrameId); // Stop ongoing animation
            const targetTime = parseFloat(event.target.value);

            // If moving backward or jumping significantly, rebuild state
            if (targetTime < currentTime - 1 || targetTime > currentTime + 20) { // Threshold for rebuild
                 currentTime = 0; // Reset time to rebuild from start
                 lastCreationTime = 0;
                 svg.querySelectorAll('.island, .finch').forEach(el => svg.removeChild(el));
                 islands = [];
                 finches = [];

                 // Rebuild state up to target time without animation
                 // Simulate island creation intervals
                 const numIntervals = Math.floor(targetTime / islandCreationInterval);
                 for(let i = 0; i < numIntervals; i++) {
                      const islandCreationTime = (i + 1) * islandCreationInterval;
                      if (islandCreationTime <= targetTime) {
                           createIsland(islandCreationTime);
                           lastCreationTime = islandCreationTime;
                           // Simulate finch arrival/spread during scrubbing
                           if (islandCreationTime >= finchInitialArrivalTime) {
                                const hasExistingFinches = finches.length > 0;
                                if (hasExistingFinches && Math.random() < finchSpreadChance) { // Use chance even when scrubbing
                                     const targetIsland = islands.find(iso => iso.creationTime === islandCreationTime);
                                     if (targetIsland) {
                                          const ageBracket = getIslandAgeBracket(targetTime - targetIsland.creationTime); // Species based on island state *at target time*
                                          addFinchesToIsland(targetIsland, ageBracket);
                                     }
                                } else if (!hasExistingFinches && islands.length === 1 && islands[0].creationTime >= finchInitialArrivalTime) {
                                     // Initial arrival during scrubbing
                                     const targetIsland = islands.find(iso => iso.creationTime === islandCreationTime);
                                      if (targetIsland) {
                                         addFinchesToIsland(targetIsland, 0); // Species 0 for initial
                                     }
                                }
                           }
                      } else {
                           break; // Don't create islands past target time
                      }
                 }

                 // Update simulation state to the exact target time
                 updateSimulation(targetTime, true); // Pass isScrubbing flag
                 currentTime = targetTime; // Set current time after rebuilding state
            } else {
                 // For small movements, just update state
                 currentTime = targetTime;
                 updateSimulation(currentTime);
            }

            // Ensure animation loop resumes correctly if user presses play after scrubbing
             if (isPlaying) { // Should be false here, but as a safeguard
                 lastTimestamp = performance.now(); // Reset timer
                 animate();
             }
        });


        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
            toggleExplanationBtn.textContent = isHidden ? 'הסתירו הסבר' : 'מה קורה כאן? הסבירו לי!';
        });


        // Initial setup
        drawHotspot();
        updateSimulation(currentTime); // Draw initial state
        lastTimestamp = performance.now(); // Initialize timestamp for first animation frame

         // Start animation loop but keep it paused
         animationFrameId = requestAnimationFrame(animate);

    });
</script>
---