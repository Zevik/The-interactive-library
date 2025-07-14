---
title: "הקרב הגדול: וירוס פולש לתא"
english_slug: viral-host-cell-war-journey-inside-host-cell
category: "מדעי החיים / ביולוגיה"
tags:
  - וירוסים
  - שכפול ויראלי
  - מחזור ליטי
  - מחזור ליזוגני
  - תא מארח
  - ביולוגיה מולקולרית
---
# הקרב הגדול: וירוס פולש לתא

איך יצור כה פשוט כמו וירוס מצליח להשתלט על מכונות מורכבות כמו התאים שלנו? האם תמיד ההשתלטות מובילה להרס מיידי של התא, או שיש לווירוס אסטרטגיות שקטות יותר להישרדות? צללו פנימה כדי לגלות את הקרב המולקולרי הנסתר שמתרחש בכל רגע בגופנו ובעולם סביבנו.

<div id="simulation-container">
    <div id="cell">
        <div id="membrane-interaction"></div> <!-- Added for interaction animation -->
        <div id="nucleus">
            <div id="host-dna"></div>
            <div id="viral-dna-integrated" class="hidden"></div>
        </div>
        <div id="ribosomes"></div>
        <div id="viral-dna" class="hidden"></div>
         <div id="mrna" class="hidden"></div> <!-- Added for Lytic step visualization -->
         <div id="viral-proteins" class="hidden"></div> <!-- Added for Lytic step visualization -->
        <div id="new-viruses-assembly" class="hidden"></div>
         <div id="released-viruses" class="hidden"></div> <!-- Added for Lysis visualization -->
    </div>
    <div id="virus-outside"></div>
    <div id="controls">
        <button id="start-simulation" class="action-button">התחל פלישה: וירוס מתקרב</button>
        <div id="path-selection" class="controls-group hidden">
            <p>החומר הגנטי בפנים! בחר מסלול שכפול:</p>
            <button id="lytic-path" class="path-button lytic">מסלול ליטי (השמדה)</button>
            <button id="lysogenic-path" class="path-button lysogenic">מסלול ליזוגני (הסוואה)</button>
        </div>
        <button id="induce-lytic" class="action-button hidden">גרם למעבר ליטי (גירוי חיצוני)</button>
        <button id="reset-simulation" class="secondary-button hidden">התחל קרב מחדש</button>
    </div>
    <div id="status"></div>
</div>

<style>
    :root {
        --cell-color-light: #e9f7ff; /* Light blue */
        --cell-color-border: #007bff; /* Blue */
        --nucleus-color-light: #f8f9fa; /* Light grey */
        --nucleus-color-border: #6610f2; /* Purple */
        --host-dna-color: #000; /* Black */
        --viral-dna-color: #dc3545; /* Red */
        --ribosome-color: #ffc107; /* Yellow */
        --ribosome-busy-color: #e0a800; /* Darker yellow */
        --virus-color: #28a745; /* Green */
        --mrna-color: #fd7e14; /* Orange */
        --protein-color: #6f42c1; /* Indigo */
        --background-color: #f0f4f8; /* Light modern background */
        --control-bg-color: #ffffff;
        --border-radius-soft: 15px;
        --border-radius-round: 50%;
        --animation-duration-short: 0.5s;
        --animation-duration-medium: 1s;
        --animation-duration-long: 2s;
    }

    #simulation-container {
        width: 100%;
        max-width: 800px;
        margin: 30px auto;
        border: 1px solid #dcdcdc;
        border-radius: var(--border-radius-soft);
        padding: 30px;
        position: relative;
        background-color: var(--background-color);
        overflow: hidden;
        font-family: 'Arial', sans-serif; /* Modern font */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    #cell {
        width: 350px; /* Slightly larger */
        height: 250px; /* Slightly larger */
        border: 3px solid var(--cell-color-border);
        border-radius: 70px; /* More rounded */
        position: relative;
        margin: 60px auto; /* More space */
        background-color: var(--cell-color-light);
        overflow: hidden;
        transition: all var(--animation-duration-medium) ease-in-out; /* Add transition */
    }

    #nucleus {
        width: 130px; /* Slightly larger */
        height: 100px; /* Slightly larger */
        border: 3px solid var(--nucleus-color-border);
        border-radius: 40px; /* More rounded */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: var(--nucleus-color-light);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }

    #host-dna {
        width: 80px; /* Larger */
        height: 70px; /* Larger */
        background: repeating-linear-gradient(45deg, var(--host-dna-color), var(--host-dna-color) 5px, transparent 5px, transparent 10px);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        transition: all var(--animation-duration-medium) ease-in-out;
    }

    #viral-dna-integrated {
        width: 80px; /* Match host DNA size */
        height: 70px; /* Match host DNA size */
        /* Combine patterns */
        background:
            repeating-linear-gradient(-45deg, var(--viral-dna-color), var(--viral-dna-color) 5px, transparent 5px, transparent 10px),
            repeating-linear-gradient(45deg, var(--host-dna-color), var(--host-dna-color) 5px, transparent 5px, transparent 10px);
        background-blend-mode: multiply; /* Blend the patterns */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        transition: all var(--animation-duration-medium) ease-in-out;
    }

    #ribosomes {
        width: 120px; /* Larger */
        height: 60px; /* Larger */
        position: absolute;
        bottom: 20px; /* More space from bottom */
        left: 50%;
        transform: translateX(-50%);
        background-color: var(--ribosome-color);
        border-radius: 15px; /* More rounded */
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 0 10px; /* More padding */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: background-color var(--animation-duration-short) ease, box-shadow var(--animation-duration-short) ease;
    }

    #ribosomes::before, #ribosomes::after {
        content: '';
        width: 20px; /* Larger */
        height: 20px; /* Larger */
        background-color: var(--ribosome-busy-color); /* Darker part */
        border-radius: var(--border-radius-round);
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
    }
     #ribosomes.busy {
        background-color: var(--ribosome-busy-color);
        box-shadow: 0 0 12px var(--ribosome-color); /* Stronger glow */
     }

    #virus-outside {
        width: 30px; /* Larger */
        height: 35px; /* Larger */
        background-color: var(--virus-color); /* Green */
        border-radius: var(--border-radius-round);
        position: absolute;
        top: 150px; /* Adjust initial position */
        left: 100px; /* Adjust initial position */
        transition: all var(--animation-duration-medium) ease-in-out;
        z-index: 10; /* Ensure it's on top */
         box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
     #virus-outside::before {
         content: '';
         position: absolute;
         top: -8px; /* Adjust leg position */
         left: 50%;
         transform: translateX(-50%);
         width: 8px; /* Larger leg */
         height: 15px; /* Longer leg */
         background-color: var(--virus-color);
         border-radius: 3px;
     }

     #membrane-interaction { /* Visual cue for virus attachment */
        position: absolute;
        width: 40px;
        height: 40px;
        border: 4px dashed rgba(0, 123, 255, 0.5); /* Dashed blue */
        border-radius: var(--border-radius-round);
        top: calc(50% - 20px); /* Initial position near virus entry */
        left: calc(150px - 20px);
        opacity: 0;
        transition: opacity var(--animation-duration-short) ease-in-out;
     }

    #viral-dna {
        width: 20px; /* Larger */
        height: 25px; /* Larger */
        background-color: var(--viral-dna-color); /* Red */
        position: absolute;
        top: 165px; /* Initial position inside cell */
        left: 115px;
        transition: all var(--animation-duration-long) ease-in-out;
        border-radius: 5px; /* More rounded corners */
        z-index: 5; /* Below virus */
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    #mrna {
        width: 15px; /* Smaller */
        height: 5px;
        background-color: var(--mrna-color); /* Orange */
        position: absolute;
        top: 180px; /* Near ribosomes */
        left: 300px;
        opacity: 0;
        transition: all var(--animation-duration-long) ease-in-out;
        border-radius: 2px;
    }

     #viral-proteins {
         width: 10px;
         height: 10px;
         background-color: var(--protein-color); /* Indigo */
         border-radius: var(--border-radius-round);
         position: absolute;
         top: 180px; /* Near ribosomes */
         left: 300px;
         opacity: 0;
         transition: all var(--animation-duration-long) ease-in-out;
     }


     #new-viruses-assembly {
        position: absolute;
        bottom: 80px; /* More space */
        left: 50%;
        transform: translateX(-50%);
        width: 180px; /* Larger area */
        height: 100px; /* Larger area */
        border: 2px dashed rgba(0,0,0,0.3); /* Softer dashed border */
        border-radius: var(--border-radius-soft);
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 8px; /* More space between viruses */
        padding: 8px;
        background-color: rgba(255,255,255,0.5); /* Semi-transparent white */
     }
     #new-viruses-assembly .new-virus {
        width: 15px; /* Larger assembled virus */
        height: 18px; /* Larger assembled virus */
        background-color: var(--virus-color);
        border-radius: var(--border-radius-round);
        position: relative; /* Needed for ::before */
        opacity: 0; /* Start hidden */
        transform: scale(0.5); /* Start smaller */
         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
     }
      #new-viruses-assembly .new-virus::before {
         content: '';
         position: absolute;
         top: -4px; /* Adjust leg position */
         left: 50%;
         transform: translateX(-50%);
         width: 4px; /* Larger leg */
         height: 8px; /* Longer leg */
         background-color: var(--virus-color);
         border-radius: 2px;
     }

     #released-viruses {
         position: absolute;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         display: flex;
         justify-content: center;
         align-items: center;
         pointer-events: none; /* Don't block clicks */
         z-index: 20;
     }
      #released-viruses .flying-virus {
         width: 20px;
         height: 25px;
         background-color: var(--virus-color);
         border-radius: var(--border-radius-round);
         position: absolute;
         opacity: 1;
         transform: translate(-50%, -50%);
          box-shadow: 0 1px 3px rgba(0,0,0,0.2);
      }
      #released-viruses .flying-virus::before {
         content: '';
         position: absolute;
         top: -6px;
         left: 50%;
         transform: translateX(-50%);
         width: 6px;
         height: 12px;
         background-color: var(--virus-color);
         border-radius: 2px;
     }


    #controls {
        text-align: center;
        margin-top: 30px; /* More space */
        background-color: var(--control-bg-color);
        padding: 15px;
        border-radius: var(--border-radius-soft);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

     .controls-group {
         margin-bottom: 15px;
     }

    #controls button {
        margin: 8px; /* More spacing */
        padding: 12px 20px; /* Larger padding */
        cursor: pointer;
        font-size: 1.1rem; /* Larger font */
        border: none;
        border-radius: 25px; /* Pill shape */
        transition: background-color 0.2s ease, transform 0.1s ease;
        min-width: 150px; /* Minimum button width */
    }

     .action-button {
        background-color: #007bff; /* Primary blue */
        color: white;
     }
     .action-button:hover {
         background-color: #0056b3;
         transform: translateY(-1px);
     }

     .path-button {
         background-color: #6c757d; /* Secondary grey */
         color: white;
     }
      .path-button.lytic { background-color: var(--viral-dna-color); } /* Red for lytic */
      .path-button.lysogenic { background-color: var(--nucleus-color-border); } /* Purple for lysogenic */

     .path-button:hover {
         filter: brightness(1.1);
         transform: translateY(-1px);
     }

     .secondary-button {
         background-color: #f8f9fa; /* Light background */
         color: #343a40; /* Dark text */
         border: 1px solid #ced4da;
     }
     .secondary-button:hover {
         background-color: #e2e6ea;
         transform: translateY(-1px);
     }


    #status {
        text-align: center;
        margin-top: 20px; /* More space */
        font-weight: bold;
        color: #333;
        min-height: 1.2em; /* Reserve space */
    }

    .hidden {
        display: none;
    }

    /* Animations */
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }

     @keyframes entry-approach {
         to { top: 150px; left: 140px; } /* Approach cell edge */
     }

     @keyframes membrane-pulse {
         0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
         50% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
         100% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
     }

     @keyframes dna-injection {
         0% { width: 8px; height: 15px; top: calc(150px + 10px); left: calc(140px + 10px); opacity: 1; } /* Start inside virus */
         50% { top: calc(150px + 30px); left: calc(140px + 30px); opacity: 1; } /* Move into cell */
         100% { top: 165px; left: 115px; width: 20px; height: 25px; opacity: 1; } /* Settle at initial cell DNA pos */
     }


     @keyframes dna-movement {
         from { opacity: 1; }
         to { opacity: 1; } /* Just moves, stays visible */
     }

     @keyframes mrna-production {
         0% { opacity: 0; width: 0;}
         20% { opacity: 1; width: 20px;}
         80% { opacity: 1; width: 20px;}
         100% { opacity: 0; width: 0;}
     }
      @keyframes protein-production {
         0% { opacity: 0; transform: translate(-50%, -50%) scale(0.5);}
         50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1);}
         100% { opacity: 0; transform: translate(-50%, -50%) scale(0.5);}
     }

    @keyframes assemble-viruses {
        0% { transform: scale(0.5); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }

     @keyframes cell-lysis {
         0% { transform: scale(1); opacity: 1; border-color: var(--cell-color-border);}
         50% { transform: scale(1.05); opacity: 0.8; border-color: var(--viral-dna-color); /* Cell turns red */ }
         100% { transform: scale(1.2); opacity: 0; border-color: var(--viral-dna-color); }
     }

      @keyframes cell-division {
          0% { transform: scaleX(1); }
          50% { transform: scaleX(1.1) rotate(5deg); }
          100% { transform: scaleX(1); }
      }

     @keyframes flying-virus {
         0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
         100% { transform: translate(var(--dx, 0), var(--dy, 0)) scale(0.5); opacity: 0; }
     }


</style>

<button id="toggle-explanation" class="secondary-button full-width-button">הצג/הסתר הסבר מפורט</button>

<div id="explanation" class="hidden">
    <h2>הסבר מפורט: הקרב הגדול בין וירוס לתא</h2>

    <h3>מהו וירוס וכיצד הוא שונה מיצורים חיים?</h3>
    וירוסים הם "טפילים תאיים אובליגטוריים" - חלקיקים זעירים במיוחד שאין להם את היכולת לקיים תהליכי חיים בכוחות עצמם. הם אינם נושמים, אוכלים או גדלים. מבנה וירוס בסיסי כולל ליבה של חומר גנטי (DNA או RNA) העטופה במעטפת חלבון (קפסיד), ולעיתים שכבה חיצונית נוספת של שומן (מעטפת). הם חייבים לפלוש לתא חי כדי "להתעורר לחיים" ולהתרבות.

    <h3>למה וירוסים חייבים תא מארח?</h3>
    הסיבה פשוטה: לווירוסים אין את המכונות (כמו ריבוזומים) הדרושות לייצור חלבונים או לשכפול החומר הגנטי שלהם בכמויות גדולות. הם כמו תוכנת מחשב זדונית שחייבת לפעול על מערכת הפעלה קיימת. הם חודרים לתא המארח ו"משתלטים" על המנגנונים הביולוגיים שלו כדי לייצר עותקים של עצמם.

    <h3>השלבים הראשונים של הפלישה (הצמדות וחדירה)</h3>
    כל וירוס "מתמחה" בהדבקת סוגי תאים מסוימים. הפלישה מתחילה כשהווירוס מזהה ונצמד לקולטנים ספציפיים על פני ממברנת התא המארח - כמו מפתח הנכנס למנעול. לאחר ההצמדות, הווירוס חודר פנימה בדרכים שונות (למשל, הזרקת החומר הגנטי בלבד, או חדירה של כל החלקיק ולאחר מכן שחרור החומר הגנטי בתוך התא). החומר הגנטי הוויראלי משוחרר לתוך הציטופלזמה של התא.

    <h3>המחזור הליטי: אסטרטגיית ההרס המהיר</h3>
    זהו המסלול האגרסיבי והמהיר ביותר, המכונה גם "מסלול השכפול הפעיל".
    <ul>
        <li>**השתלטות:** החומר הגנטי הוויראלי מגיע לריבוזומים של התא המארח (המפעלים ליצור חלבונים) ו"מכתיב" להם לייצר אך ורק חלבונים ויראליים – גם את החלבונים המבניים שירכיבו את הווירוסים החדשים, וגם אנזימים שישכפלו את החומר הגנטי הוויראלי.</li>
        <li>**שכפול והרכבה:** החומר הגנטי הוויראלי משוכפל במהירות, והחלבונים המיוצרים מתאספים ליצירת עשרות עד אלפי חלקיקי וירוס חדשים בתוך התא.</li>
        <li>**השמדה (ליזיס):** כאשר כמות הווירוסים החדשים בתא מגיעה לשיא, הם מייצרים חלבונים שמחלישים את דופן/ממברנת התא, ולבסוף התא "מתפוצץ" (ליזיס), משחרר את כל הווירוסים החדשים לסביבה כדי שידביקו תאים נוספים.</li>
        <li>**דוגמאות:** וירוסים רבים הגורמים למחלות חריפות כמו שפעת, הצטננות, קורונה, ווירוסים שתוקפים חיידקים (בקטריופאג'ים) פועלים כך.</li>
    </ul>

    <h3>המחזור הליזוגני: אסטרטגיית ההסוואה השקטה</h3>
    מסלול זה מאפשר לווירוס להתקיים בתוך התא המארח מבלי להרוס אותו באופן מיידי, מעין "מצב המתנה".
    <ul>
        <li>**הטמעה (אינטגרציה):** במקום להשתלט מיד על הריבוזומים, החומר הגנטי הוויראלי (במקרה של וירוס DNA, או לאחר שהומר ל-DNA מווירוס RNA) נכנס לגרעין התא ו"משתלב" פיזית בתוך ה-DNA המארח. מקטע ה-DNA הוויראלי המשולב נקרא "פרופז'" (Prophage בבקטריופאג'ים) או פרו-וירוס.</li>
        <li>**שכפול תורשתי:** כשהתא המארח מתחלק (למשל לצורך גדילה או החלפת תאים פגומים), הוא משכפל את כל ה-DNA שלו, כולל מקטע הפרופז'. כך, מבלי שהווירוס פעיל, החומר הגנטי שלו מועבר אוטומטית לכל תאי הבת. זהו שכפול שקט וסמוי.</li>
        <li>**השפעות על התא:** לעיתים, נוכחות הפרופז' יכולה להקנות לתא המארח תכונות חדשות, כמו עמידות בפני הדבקה בווירוסים אחרים, או אף לייצר רעלנים (כפי שקורה בחיידקים המוּדָבּקים שמייצרים רעלנים מסוכנים לאדם).</li>
        <li>**מעבר למחזור הליטי (אינדוקציה):** הפרופז' יכול להישאר רדום בגנום המארח למשך דורות של תאים. אך בתנאים מסוימים (למשל, קרינת UV, חומרים כימיים, או כשהתא נמצא במצוקה), ה-DNA הוויראלי יכול "לקפוץ החוצה" מהגנום המארח ולהתחיל במחזור הליטי הפעיל, המוביל לייצור וירוסים חדשים ולהרס התא. תהליך זה נקרא "אינדוקציה".</li>
        <li>**דוגמאות:** בקטריופאג' למדא הוא דוגמה קלאסית. גם וירוסים אנושיים כמו וירוס ההרפס ווירוס ה-HIV יכולים לקיים מצב רדום דומה במידה מסוימת.</li>
    </ul>

    <h3>חשיבות ההבנה: כלי למלחמה במחלות</h3>
    הבנת המנגנונים המורכבים הללו חיונית מאין כמותה. ידע זה מאפשר למדענים לפתח תרופות אנטי-ויראליות החוסמות שלבים ספציפיים במחזור השכפול, ליצור חיסונים שמאלפים את מערכת החיסון לזהות וירוסים, ולתכנן אסטרטגיות טיפוליות כנגד מחלות ויראליות רבות, הן אלה שמתפרצות במהירות והן אלה שנשארות רדומות ופורצות בזמנים אחרים. זוהי מלחמה מולקולרית מתמדת, והבנת כל מהלך בה חיונית לניצחון.

    <button id="hide-explanation" class="secondary-button full-width-button">הסתר הסבר</button>
</div>

<script>
    const simulationContainer = document.getElementById('simulation-container');
    const cell = document.getElementById('cell');
    const membraneInteraction = document.getElementById('membrane-interaction');
    const nucleus = document.getElementById('nucleus');
    const hostDna = document.getElementById('host-dna');
    const viralDnaIntegrated = document.getElementById('viral-dna-integrated');
    const ribosomes = document.getElementById('ribosomes');
    const virusOutside = document.getElementById('virus-outside');
    const viralDna = document.getElementById('viral-dna');
    const mrna = document.getElementById('mrna');
    const viralProteins = document.getElementById('viral-proteins');
    const newVirusesAssembly = document.getElementById('new-viruses-assembly');
    const releasedVirusesContainer = document.getElementById('released-viruses'); // New container
    const startButton = document.getElementById('start-simulation');
    const pathSelection = document.getElementById('path-selection');
    const lyticButton = document.getElementById('lytic-path');
    const lysogenicButton = document.getElementById('lysogenic-path');
    const induceLyticButton = document.getElementById('induce-lytic');
    const resetButton = document.getElementById('reset-simulation');
    const statusDiv = document.getElementById('status');
    const explanationDiv = document.getElementById('explanation');
    const toggleExplanationButton = document.getElementById('toggle-explanation');
    const hideExplanationButton = document.getElementById('hide-explanation');

    let currentPath = null; // 'lytic' or 'lysogenic'
    let isLysogenic = false;

     const animationDurations = { // Define durations for consistency
         short: 500, // 0.5s
         medium: 1000, // 1s
         long: 2000, // 2s
         assembly: 100, // 0.1s per virus
         lysis: 1000, // 1s
         division: 2000 // 2s per division pulse
     };


    function setStatus(message) {
        statusDiv.textContent = message;
    }

    function resetSimulation() {
        // Clear existing animations and styles
        cell.style.cssText = '';
        nucleus.style.cssText = '';
        hostDna.style.cssText = '';
        viralDnaIntegrated.style.cssText = '';
        ribosomes.style.cssText = '';
        virusOutside.style.cssText = '';
        viralDna.style.cssText = '';
        mrna.style.cssText = '';
        viralProteins.style.cssText = '';
        membraneInteraction.style.cssText = '';

        // Reset element visibility and content
        cell.style.width = '350px';
        cell.style.height = '250px';
        cell.style.opacity = '1';
        cell.style.borderColor = 'var(--cell-color-border)'; // Reset border color after lysis
        virusOutside.classList.remove('hidden');
        viralDna.classList.add('hidden');
        mrna.classList.add('hidden');
        viralProteins.classList.add('hidden');
        newVirusesAssembly.classList.add('hidden');
        newVirusesAssembly.innerHTML = ''; // Clear assembled viruses
        releasedVirusesContainer.classList.add('hidden');
        releasedVirusesContainer.innerHTML = ''; // Clear released viruses
        ribosomes.classList.remove('busy');
        viralDnaIntegrated.classList.add('hidden');
        hostDna.classList.remove('hidden');
        membraneInteraction.classList.add('hidden');

        // Reset controls
        startButton.classList.remove('hidden');
        pathSelection.classList.add('hidden');
        lyticButton.classList.remove('hidden');
        lysogenicButton.classList.remove('hidden');
        induceLyticButton.classList.add('hidden');
        resetButton.classList.add('hidden');

        // Reset state variables
        setStatus('מוכן לקרב: וירוס ממתין מחוץ לתא');
        currentPath = null;
        isLysogenic = false;
    }

    function startSimulation() {
        startButton.classList.add('hidden');
        setStatus('וירוס מתקרב... מזהה את התא המארח!');

        // Animate virus approaching the cell edge
        virusOutside.style.transition = `all ${animationDurations.long}ms ease-in-out`;
        virusOutside.style.top = '150px';
        virusOutside.style.left = '140px'; /* Position near cell edge */

        setTimeout(() => {
            setStatus('וירוס נצמד לממברנה... מנסה לחדור!');
             // Show membrane interaction pulse
             membraneInteraction.classList.remove('hidden');
             membraneInteraction.style.top = '150px';
             membraneInteraction.style.left = '140px';
             membraneInteraction.style.animation = `membrane-pulse ${animationDurations.short}ms ease-in-out 3`; // Pulse a few times


            setTimeout(() => {
                setStatus('חדירה מוצלחת! החומר הגנטי שוגר פנימה!');
                virusOutside.style.opacity = '0'; // Virus "empties" or detaches
                membraneInteraction.classList.add('hidden');
                membraneInteraction.style.animation = ''; // Clear animation

                viralDna.classList.remove('hidden');
                // Animate DNA injection from virus position into the cell
                 const virusRect = virusOutside.getBoundingClientRect();
                 const containerRect = simulationContainer.getBoundingClientRect();

                // Position DNA initially inside the (now fading) virus relative to container
                 const initialDNA_top = virusRect.top - containerRect.top + virusRect.height / 2 - 8; // Approx center + slight adjustment
                 const initialDNA_left = virusRect.left - containerRect.left + virusRect.width / 2 - 4; // Approx center + slight adjustment


                 viralDna.style.width = '8px';
                 viralDna.style.height = '15px';
                 viralDna.style.top = `${initialDNA_top}px`;
                 viralDna.style.left = `${initialDNA_left}px`;
                 viralDna.style.opacity = '1';
                 viralDna.style.transition = `all ${animationDurations.medium}ms ease-in-out`; // Transition for initial size/pos


                // Calculate target position inside cell relative to container
                 const cellRect = cell.getBoundingClientRect();
                 const targetDNA_top = cellRect.top - containerRect.top + cellRect.height * 0.6; // Arbitrary point inside
                 const targetDNA_left = cellRect.left - containerRect.left + cellRect.width * 0.4; // Arbitrary point inside

                // Animate DNA moving inwards and expanding to its normal intracellular size
                viralDna.style.top = `${targetDNA_top}px`;
                viralDna.style.left = `${targetDNA_left}px`;
                 viralDna.style.width = '20px';
                 viralDna.style.height = '25px';


                setTimeout(() => {
                    setStatus('החומר הגנטי הוויראלי בפנים. מה יהיה גורל התא? בחר מסלול:');
                     // Position DNA near center after injection animation
                     const cellCenterTop = cellRect.top - containerRect.top + cellRect.height / 2;
                     const cellCenterLeft = cellRect.left - containerRect.left + cellRect.width / 2;
                     viralDna.style.transition = `all ${animationDurations.long}ms ease-in-out`; // Reset transition for next moves
                     viralDna.style.top = `${cellCenterTop}px`;
                     viralDna.style.left = `${cellCenterLeft}px`;
                     viralDna.style.transform = 'translate(-50%, -50%)'; // Center DNA

                    pathSelection.classList.remove('hidden');
                     // Maybe slightly pulse the viral DNA to draw attention
                     viralDna.style.animation = 'pulse 1s infinite';


                }, animationDurations.medium); // Wait for injection animation

            }, animationDurations.short * 3 + 200); // Wait for membrane pulse + slight delay

        }, animationDurations.long); // Wait for virus approach animation
    }

    function startLyticPath() {
        currentPath = 'lytic';
        pathSelection.classList.add('hidden');
        viralDna.style.animation = ''; // Stop pulsing
        setStatus('המסלול הליטי נבחר! החומר הגנטי הוויראלי דורש מהתא לייצר וירוסים חדשים.');

        // Animate viral DNA towards ribosomes
        const ribosomesRect = ribosomes.getBoundingClientRect();
        const containerRect = simulationContainer.getBoundingClientRect();
        const targetTop = ribosomesRect.top - containerRect.top + ribosomesRect.height / 2;
        const targetLeft = ribosomesRect.left - containerRect.left + ribosomesRect.width / 2;

        viralDna.style.transition = `all ${animationDurations.long}ms ease-in-out`;
        viralDna.style.top = `${targetTop}px`;
        viralDna.style.left = `${targetLeft}px`;
        viralDna.style.transform = 'translate(-50%, -50%)';

        setTimeout(() => {
            setStatus('החומר הגנטי משתלט על הריבוזומים... מתחיל ייצור מסיבי!');
            ribosomes.classList.add('busy');
             viralDna.classList.add('hidden'); // DNA is now "active" in the machinery

             // Simulate mRNA and protein production animations near ribosomes
             mrna.classList.remove('hidden');
             viralProteins.classList.remove('hidden');
             mrna.style.top = `${targetTop - 20}px`;
             mrna.style.left = `${targetLeft - 50}px`;
             viralProteins.style.top = `${targetTop + 20}px`;
             viralProteins.style.left = `${targetLeft + 50}px`;

             mrna.style.animation = `mrna-production ${animationDurations.medium}ms linear infinite`;
             viralProteins.style.animation = `protein-production ${animationDurations.short}ms ease-in-out infinite alternate`;


            setTimeout(() => {
                setStatus('חלקיקי וירוס חדשים מורכבים באזור ההרכבה.');
                mrna.style.animation = ''; // Stop production animations
                mrna.classList.add('hidden');
                viralProteins.style.animation = '';
                viralProteins.classList.add('hidden');

                newVirusesAssembly.classList.remove('hidden');
                 // Simulate assembly animation
                 let count = 0;
                 const totalVirusesToAssemble = 25; // More viruses for visual impact
                 const assemblyInterval = setInterval(() => {
                     if (count < totalVirusesToAssemble) {
                         const newVirus = document.createElement('div');
                         newVirus.classList.add('new-virus');
                         newVirusesAssembly.appendChild(newVirus);
                         newVirus.style.animation = `assemble-viruses ${animationDurations.short}ms ease-out forwards`;
                          // Add small delay to each animation
                         newVirus.style.animationDelay = `${count * (animationDurations.assembly / 1000)}s`; // Delay in seconds
                         count++;
                     } else {
                         clearInterval(assemblyInterval);
                         setTimeout(() => {
                             setStatus('עומס יתר! התא המארח עומד להתפוצץ (ליזיס)!');
                             ribosomes.classList.remove('busy');
                             newVirusesAssembly.classList.add('hidden'); // Hide assembly area
                             viralDna.classList.add('hidden'); // Ensure DNA is hidden

                            // Animate cell lysis
                            cell.style.transition = `all ${animationDurations.lysis}ms ease-in-out`;
                            cell.style.animation = `cell-lysis ${animationDurations.lysis}ms forwards`;

                             // Show released viruses flying out
                             releasedVirusesContainer.classList.remove('hidden');
                             const assemblyRect = newVirusesAssembly.getBoundingClientRect(); // Use assembly area center as explosion source
                             const containerRect = simulationContainer.getBoundingClientRect();
                             const explosionCenterX = assemblyRect.left - containerRect.left + assemblyRect.width / 2;
                             const explosionCenterY = assemblyRect.top - containerRect.top + assemblyRect.height / 2;

                             const virusesToRelease = Math.min(totalVirusesToAssemble, 30); // Release up to 30
                             for(let i = 0; i < virusesToRelease; i++) {
                                 const flyingVirus = document.createElement('div');
                                 flyingVirus.classList.add('flying-virus');
                                 flyingVirus.style.top = `${explosionCenterY}px`;
                                 flyingVirus.style.left = `${explosionCenterX}px`;
                                 releasedVirusesContainer.appendChild(flyingVirus);

                                 // Random destination outside container
                                 const angle = Math.random() * 360;
                                 const distance = Math.max(containerRect.width, containerRect.height) * 0.8; // Fly far out
                                 const dx = Math.cos(angle * Math.PI / 180) * distance;
                                 const dy = Math.sin(angle * Math.PI / 180) * distance;

                                 flyingVirus.style.setProperty('--dx', `${dx}px`);
                                 flyingVirus.style.setProperty('--dy', `${dy}px`);
                                 flyingVirus.style.animation = `flying-virus ${animationDurations.long + Math.random() * animationDurations.medium}ms ease-out forwards`;
                                 flyingVirus.style.animationDelay = `${Math.random() * animationDurations.short / 1000}s`; // Stagger starts
                             }


                             setTimeout(() => {
                                setStatus('הקרב הסתיים: וירוסים חדשים שוחררו להדביק תאים נוספים.');
                                resetButton.classList.remove('hidden');
                                virusOutside.classList.add('hidden'); // Ensure initial virus is hidden
                             }, animationDurations.lysis); // Matches lysis animation duration

                         }, animationDurations.medium); // Time after assembly finishes

                     }
                 }, animationDurations.assembly); // Interval between adding new viruses

            }, animationDurations.long); // Time for ribosomes to get busy and produce components

        }, animationDurations.long); // Time for DNA to reach ribosomes
    }

    function startLysogenicPath() {
        currentPath = 'lysogenic';
        isLysogenic = true;
        pathSelection.classList.add('hidden');
        viralDna.style.animation = ''; // Stop pulsing
        setStatus('המסלול הליזוגני נבחר! החומר הגנטי הוויראלי חודר לגרעין...');

         // Animate viral DNA towards nucleus
        const nucleusRect = nucleus.getBoundingClientRect();
        const containerRect = simulationContainer.getBoundingClientRect();
        const targetTop = nucleusRect.top - containerRect.top + nucleusRect.height / 2;
        const targetLeft = nucleusRect.left - containerRect.left + nucleusRect.width / 2;

        viralDna.style.transition = `all ${animationDurations.long}ms ease-in-out`;
        viralDna.style.top = `${targetTop}px`;
        viralDna.style.left = `${targetLeft}px`;
        viralDna.style.transform = 'translate(-50%, -50%)';

        setTimeout(() => {
            setStatus('הטמעה! ה-DNA הוויראלי משתלב בשקט בגנום התא המארח (פרופז\').');
            viralDna.style.transition = ''; // Disable transition for quick visual change
            viralDna.classList.add('hidden'); // DNA integrates (visually disappears as separate entity)
            hostDna.classList.add('hidden'); // Hide pure host DNA
            viralDnaIntegrated.classList.remove('hidden'); // Show combined DNA representation
             // Maybe pulse integrated DNA briefly?
             viralDnaIntegrated.style.animation = 'pulse 0.8s ease-out 2';


            setTimeout(() => {
                 setStatus('התא ממשיך בשגרתו... מתחלק ומשכפל יחד איתו את הפרופז\'.');
                 // Simulate cell division
                 cell.style.animation = `cell-division ${animationDurations.division}ms ease-in-out 2`; // Animate cell division twice
                 nucleus.style.animation = `cell-division ${animationDurations.division}ms ease-in-out 2`; // Animate nucleus too
                 viralDnaIntegrated.style.animation = `cell-division ${animationDurations.division}ms ease-in-out 2, pulse 1s infinite ${animationDurations.division * 2 / 1000}s`; // Integrated DNA divides & then pulses gently


                 setTimeout(() => {
                     setStatus('מצב שקט: הפרופז\' רדום בגנום המארח. ממתין לגירוי חיצוני למעבר למצב פעיל.');
                     cell.style.animation = ''; // Stop division animation
                      nucleus.style.animation = ''; // Stop nucleus animation
                     viralDnaIntegrated.style.animation = 'pulse 1s infinite'; // Keep integrated DNA pulsing subtly

                     induceLyticButton.classList.remove('hidden');
                     resetButton.classList.remove('hidden');
                 }, animationDurations.division * 2); // After cell division animation finishes

            }, animationDurations.medium); // Time for integration visual change
        }, animationDurations.long); // Time for DNA to reach nucleus
    }

     function induceLytic() {
         if (!isLysogenic) return; // Only allow induction from lysogenic state

         isLysogenic = false; // No longer in lysogenic state
         induceLyticButton.classList.add('hidden');
         setStatus('גירוי חיצוני התקבל! הפרופז\' נקרע החוצה מהגנום המארח.');

         viralDnaIntegrated.style.animation = ''; // Stop integrated DNA pulse
         viralDnaIntegrated.classList.add('hidden'); // Integrated DNA disappears
         hostDna.classList.remove('hidden'); // Host DNA back to normal

         // Animate viral DNA reappearing near nucleus and moving out
         viralDna.classList.remove('hidden');
         const nucleusRect = nucleus.getBoundingClientRect();
         const containerRect = simulationContainer.getBoundingClientRect();
         const initialTop = nucleusRect.top - containerRect.top + nucleusRect.height / 2;
         const initialLeft = nucleusRect.left - containerRect.left + nucleusRect.width / 2;

         viralDna.style.cssText = ''; // Clear previous styles (like pulsing)
         viralDna.style.top = `${initialTop}px`;
         viralDna.style.left = `${initialLeft}px`;
         viralDna.style.transform = 'translate(-50%, -50%)';
         viralDna.style.opacity = '1'; // Ensure visible
         viralDna.style.transition = `all ${animationDurations.medium}ms ease-in-out`; // Transition for moving out of nucleus area

         // Position DNA slightly outside nucleus before moving to ribosomes
          const cellRect = cell.getBoundingClientRect();
          const postNucleusTop = cellRect.top - containerRect.top + cellRect.height * 0.5;
          const postNucleusLeft = cellRect.left - containerRect.left + cellRect.width * 0.6;

         setTimeout(() => {
             viralDna.style.top = `${postNucleusTop}px`;
             viralDna.style.left = `${postNucleusLeft}px`;


             setTimeout(() => {
                  // Continue with lytic path steps starting from DNA release within the cell
                 setStatus('החומר הגנטי הוויראלי ממהר אל הריבוזומים למחזור ייצור פעיל!');

                 // Animate viral DNA towards ribosomes (same as initial lytic path)
                 const ribosomesRect = ribosomes.getBoundingClientRect();
                 const targetTop = ribosomesRect.top - containerRect.top + ribosomesRect.height / 2;
                 const targetLeft = ribosomesRect.left - containerRect.left + ribosomesRect.width / 2;

                 viralDna.style.transition = `all ${animationDurations.long}ms ease-in-out`;
                 viralDna.style.top = `${targetTop}px`;
                 viralDna.style.left = `${targetLeft}px`;
                 viralDna.style.transform = 'translate(-50%, -50%)';

                 setTimeout(() => {
                    setStatus('הריבוזומים תחת פקודה ויראלית... ייצור חלקיקים בעיצומו!');
                    ribosomes.classList.add('busy');
                    viralDna.classList.add('hidden');

                    // Start production animations
                    mrna.classList.remove('hidden');
                    viralProteins.classList.remove('hidden');
                     mrna.style.top = `${targetTop - 20}px`;
                     mrna.style.left = `${targetLeft - 50}px`;
                     viralProteins.style.top = `${targetTop + 20}px`;
                     viralProteins.style.left = `${targetLeft + 50}px`;
                     mrna.style.animation = `mrna-production ${animationDurations.medium}ms linear infinite`;
                     viralProteins.style.animation = `protein-production ${animationDurations.short}ms ease-in-out infinite alternate`;


                     setTimeout(() => {
                        setStatus('חלקיקי וירוס חדשים מתאגדים... ההרכבה בעיצומה!');
                        mrna.style.animation = '';
                        mrna.classList.add('hidden');
                        viralProteins.style.animation = '';
                        viralProteins.classList.add('hidden');

                        newVirusesAssembly.classList.remove('hidden');
                        let count = 0;
                        const totalVirusesToAssemble = 25;
                        const assemblyInterval = setInterval(() => {
                            if (count < totalVirusesToAssemble) {
                                const newVirus = document.createElement('div');
                                newVirus.classList.add('new-virus');
                                newVirusesAssembly.appendChild(newVirus);
                                newVirus.style.animation = `assemble-viruses ${animationDurations.short}ms ease-out forwards`;
                                newVirus.style.animationDelay = `${count * (animationDurations.assembly / 1000)}s`;
                                count++;
                            } else {
                                clearInterval(assemblyInterval);
                                setTimeout(() => {
                                    setStatus('עומס יתר! התא המארח עובר ליזיס (פיצוץ)!');
                                    ribosomes.classList.remove('busy');
                                    newVirusesAssembly.classList.add('hidden');

                                    cell.style.transition = `all ${animationDurations.lysis}ms ease-in-out`;
                                    cell.style.animation = `cell-lysis ${animationDurations.lysis}ms forwards`;

                                     // Show released viruses flying out
                                     releasedVirusesContainer.classList.remove('hidden');
                                     const assemblyRect = newVirusesAssembly.getBoundingClientRect();
                                     const containerRect = simulationContainer.getBoundingClientRect();
                                     const explosionCenterX = assemblyRect.left - containerRect.left + assemblyRect.width / 2;
                                     const explosionCenterY = assemblyRect.top - containerRect.top + assemblyRect.height / 2;

                                     const virusesToRelease = Math.min(totalVirusesToAssemble, 30);
                                     for(let i = 0; i < virusesToRelease; i++) {
                                         const flyingVirus = document.createElement('div');
                                         flyingVirus.classList.add('flying-virus');
                                         flyingVirus.style.top = `${explosionCenterY}px`;
                                         flyingVirus.style.left = `${explosionCenterX}px`;
                                         releasedVirusesContainer.appendChild(flyingVirus);

                                         const angle = Math.random() * 360;
                                         const distance = Math.max(containerRect.width, containerRect.height) * 0.8;
                                         const dx = Math.cos(angle * Math.PI / 180) * distance;
                                         const dy = Math.sin(angle * Math.PI / 180) * distance;

                                         flyingVirus.style.setProperty('--dx', `${dx}px`);
                                         flyingVirus.style.setProperty('--dy', `${dy}px`);
                                         flyingVirus.style.animation = `flying-virus ${animationDurations.long + Math.random() * animationDurations.medium}ms ease-out forwards`;
                                         flyingVirus.style.animationDelay = `${Math.random() * animationDurations.short / 1000}s`;
                                     }


                                    setTimeout(() => {
                                       setStatus('הקרב הסתיים: וירוסים חדשים שוחררו.');
                                       resetButton.classList.remove('hidden');
                                       virusOutside.classList.add('hidden');
                                    }, animationDurations.lysis);
                                }, animationDurations.medium);
                            }
                        }, animationDurations.assembly);

                     }, animationDurations.long);

                 }, animationDurations.long);


             }, animationDurations.medium); // Time for DNA to move out of nucleus area


         }, animationDurations.medium); // Time for visual change of integration
     }


    startButton.addEventListener('click', startSimulation);
    lyticButton.addEventListener('click', startLyticPath);
    lysogenicButton.addEventListener('click', startLysogenicPath);
    induceLyticButton.addEventListener('click', induceLytic);
    resetButton.addEventListener('click', resetSimulation);

    toggleExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.toggle('hidden');
         if (!explanationDiv.classList.contains('hidden')) {
            // Scroll to explanation if shown
            explanationDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

     hideExplanationButton.addEventListener('click', () => {
        explanationDiv.classList.add('hidden');
         // Scroll back to simulation if hidden
         simulationContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });


    // Initial state setup
    resetSimulation(); // Ensure correct initial state

</script>
---