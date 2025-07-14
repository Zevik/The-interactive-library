---
title: "ניהול בית הפקה: האם תהפוך לסקורסזה הדוקומנטרי הבא?"
english_slug: managing-a-production-house-will-you-become-the-next-documentary-scorsese
category: "ניהול"
tags:
  - ניהול פרויקטים
  - הפקה
  - קולנוע דוקומנטרי
  - תקצוב
  - סימולציה
---
# ניהול בית הפקה: האם תהפוך לסקורסזה הדוקומנטרי הבא?

האם אי פעם חלמתם לנהל בית הפקה מצליח ולהשפיע דרך סיפורים אמיתיים על המסך הגדול? מה קורה כשתקציב מוגבל פוגש רעיונות גדולים, והזמן הוא משאב יקר? צללו עמוק לעולם המורכב והמרתק של הפקת סרטים דוקומנטריים, ותראו אם יש לכם מה שנדרש.

<div id="production-sim" class="game-container">
    <div class="stats panel">
        <h2>סטטוס בית ההפקה</h2>
        <p>חודש: <span id="current-month" class="stat-value">1</span></p>
        <p>כסף: <span id="money" class="stat-value" data-currency="₪">100,000</span></p>
        <p>מוניטין: <span id="reputation" class="stat-value">50</span></p>
    </div>

    <div class="team panel">
        <h2>הצוות שלך (עלויות חודשיות)</h2>
        <div id="team-list" class="list-items">
            <!-- Team members populated by JS -->
        </div>
        <!-- <button id="hire-team-btn" class="btn-disabled" disabled>גייס צוות נוסף (בקרוב)</button> -->
    </div>

    <div class="projects panel grid-panel">
        <div class="project-section">
            <h3><i class="icon-clipboard"></i> הצעות פרויקטים חדשות</h3>
            <div id="project-proposals" class="project-list">
                <p class="placeholder">טוען הצעות מרתקות...</p>
            </div>
        </div>

        <div class="project-section">
            <h3><i class="icon-play"></i> פרויקטים פעילים</h3>
            <div id="active-projects" class="project-list">
                <p class="placeholder">אין פרויקטים בעבודה כרגע. זה הזמן לקחת אתגר!</p>
            </div>
        </div>

         <div class="project-section">
            <h3><i class="icon-check"></i> פרויקטים שהושלמו</h3>
            <div id="completed-projects" class="project-list">
                 <p class="placeholder">אין פרויקטים שהושלמו עדיין. בוא/י נתחיל להפיק!</p>
            </div>
        </div>
    </div>

    <div class="actions panel">
        <button id="next-month-btn" class="btn-primary">קדימה לחודש הבא!</button>
         <button id="restart-btn" class="btn-secondary">התחל סימולציה מחדש</button>
    </div>

    <div id="messages" class="messages panel">
        <h3>יומן אירועים ועדכונים</h3>
        <div id="messages-list" class="list-items">
            <p class="initial-message">ברוך/ה הבא/ה למשרד החדש שלך! הצעות הפרויקטים הראשונות בדרך...</p>
        </div>
    </div>

    <div id="game-over" class="game-over-screen">
        <div class="game-over-content">
            <h2>המסך ירד!</h2>
            <p id="game-over-message"></p>
            <button id="restart-game-over-btn" class="btn-primary">התחל סימולציה מחדש</button>
        </div>
    </div>

    <div id="project-modal" class="modal">
        <div class="modal-content">
            <span class="close-button">&times;</span>
            <h3 id="modal-project-title"></h3>
            <p><strong id="modal-project-description"></strong></p>
             <p>תקציב הפקה כולל (מוערך): <span id="modal-project-budget"></span> <span class="currency">₪</span></p>
             <p>משך הפקה מוערך: <span id="modal-project-duration"></span> חודשים</p>
             <p>פוטנציאל השפעה / הכרה: <span id="modal-project-potential"></span></p>
             <h4>צוות נדרש להפקה:</h4>
             <ul id="modal-project-team" class="list-items"></ul>
              <p class="modal-cost-estimate">עלות התחלתית (עם קבלת הפרויקט): <span id="modal-initial-cost"></span> <span class="currency">₪</span></p>
              <p class="modal-cost-estimate">עלות חודשית משוערת במהלך הפקה: <span id="modal-monthly-cost"></span> <span class="currency">₪</span></p>

            <button id="accept-project-btn" class="btn-primary">קח/י את הפרויקט לאתגר הבא!</button>
             <p id="accept-project-message" class="warning-message"></p>
        </div>
    </div>

     <div id="event-modal" class="modal">
        <div class="modal-content">
             <span class="close-button">&times;</span>
             <h3 id="event-title">אירוע מיוחד!</h3>
             <p id="event-description"></p>
             <button id="event-ok-btn" class="btn-primary">הבנתי</button>
        </div>
     </div>
</div>

<style>
    /* General Styles */
    :root {
        --primary-color: #E74C3C; /* Deep Red - Film/Production feel */
        --secondary-color: #34495E; /* Dark Blue/Grey - Professional */
        --accent-color: #F39C12; /* Orange/Gold - Highlight */
        --background-color: #ECF0F1; /* Light Grey - Clean background */
        --panel-background: #FFFFFF; /* White - Content areas */
        --border-color: #BDC3C7; /* Grey Border */
        --success-color: #2ECC71; /* Green */
        --warning-color: #F1C40F; /* Yellow */
        --danger-color: #E74C3C; /* Red */
        --text-color: #2C3E50; /* Dark Text */
        --header-color: var(--secondary-color);

        --spacing-unit: 15px;
        --border-radius: 8px;
        --panel-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    body {
        font-family: 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: var(--background-color);
        color: var(--text-color);
        line-height: 1.6;
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: var(--header-color);
        text-align: center;
        margin-bottom: var(--spacing-unit);
    }
     h1 { font-size: 2.5em; margin-bottom: 30px;}
     h2 { font-size: 1.8em; }
     h3 { font-size: 1.4em; }
     h4 { font-size: 1.2em; margin-bottom: 10px;}

    /* Game Layout */
    .game-container {
        max-width: 1000px;
        margin: var(--spacing-unit) auto;
        padding: var(--spacing-unit);
        background-color: var(--background-color); /* Match body or slightly different */
        border-radius: var(--border-radius);
        display: grid;
        grid-template-areas:
            "stats team"
            "projects projects"
            "actions actions"
            "messages messages"
            "game-over game-over"; /* Game over takes over when active */
        grid-template-columns: 1fr 1fr;
        gap: var(--spacing-unit);
        box-shadow: var(--panel-shadow);
    }

     @media (max-width: 768px) {
         .game-container {
             grid-template-areas:
                 "stats"
                 "team"
                 "projects"
                 "actions"
                 "messages"
                 "game-over";
             grid-template-columns: 1fr;
         }
          .grid-panel {
              grid-template-columns: 1fr !important; /* Override project grid for mobile */
          }
     }


    .panel {
        padding: var(--spacing-unit);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--panel-background);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .stats { grid-area: stats; }
    .team { grid-area: team; }
    .projects { grid-area: projects; }
    .actions { grid-area: actions; text-align: center; }
    .messages { grid-area: messages; }
    .game-over-screen {
         grid-area: game-over;
         display: none; /* Initially hidden */
         position: absolute; /* Cover the game area */
         top: 0; left: 0; right: 0; bottom: 0;
         background-color: rgba(var(--secondary-color), 0.95);
         color: white;
         z-index: 10;
         border-radius: var(--border-radius);
         padding: 20px;
         text-align: center;
         opacity: 0; /* Start hidden for animation */
         pointer-events: none; /* Don't block clicks when hidden */
         transition: opacity 0.5s ease-in-out;
     }

     .game-over-screen.visible {
         display: flex; /* Use flexbox to center content */
         align-items: center;
         justify-content: center;
         opacity: 1;
         pointer-events: auto;
     }

     .game-over-content {
         max-width: 500px;
         padding: 30px;
         background-color: var(--panel-background);
         color: var(--text-color);
         border-radius: var(--border-radius);
         box-shadow: var(--panel-shadow);
         animation: scaleUp 0.5s ease-in-out;
     }

     .game-over-content h2 {
         color: var(--danger-color);
         font-size: 2em;
     }


     /* Stats and Team */
     .stat-value {
         font-weight: bold;
         color: var(--primary-color);
         transition: color 0.3s ease, transform 0.3s ease; /* Animation for value changes */
     }
      .stat-value.change-up { color: var(--success-color); transform: scale(1.1); }
      .stat-value.change-down { color: var(--danger-color); transform: scale(0.9); }

     .team-member {
         padding: 8px 0;
         border-bottom: 1px dashed #eee;
         font-size: 0.95em;
     }
     .team-member:last-child { border-bottom: none; }

    /* Projects */
     .grid-panel {
         display: grid;
         grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
         gap: var(--spacing-unit);
     }

    .project-section {
        border: 1px solid var(--border-color);
        padding: var(--spacing-unit);
        border-radius: var(--border-radius);
        background-color: var(--background-color); /* Slightly darker than panel background */
        display: flex;
        flex-direction: column;
    }

     .project-section h3 {
         margin-top: 0;
         margin-bottom: var(--spacing-unit);
         padding-bottom: var(--spacing-unit);
         border-bottom: 1px solid var(--border-color);
         display: flex;
         align-items: center;
         justify-content: center;
     }
      .project-section h3 i { margin-left: 10px;} /* Add icon spacing */


    .project-list {
        min-height: 100px;
        flex-grow: 1; /* Allow list to fill section height */
    }

     .placeholder {
         text-align: center;
         color: #777;
         font-style: italic;
         margin-top: var(--spacing-unit);
     }


    .project-item, .active-project-item, .completed-project-item {
        border: 1px solid var(--border-color);
        padding: var(--spacing-unit);
        margin-bottom: 10px;
        border-radius: var(--border-radius)S;
        background-color: var(--panel-background);
        cursor: pointer;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    .project-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }

    .project-item h4, .active-project-item h4, .completed-project-item h4 {
        margin-top: 0;
        margin-bottom: 8px;
        color: var(--primary-color); /* Use primary color for titles */
        text-align: right; /* Align titles to the right */
    }
    .project-item h4 { color: var(--secondary-color);} /* Different color for proposals */

    .project-item p, .active-project-item p, .completed-project-item p {
        margin: 4px 0;
        font-size: 0.95em;
        color: #555;
    }

     .active-project-item {
        border-color: var(--success-color);
        background-color: #E8F5E9; /* Light green */
     }
      .active-project-item h4 {
         color: var(--success-color);
      }
      .active-project-item:hover {
           transform: none; /* No lift animation for active items */
           box-shadow: none;
      }
       .project-progress {
          height: 8px;
          background-color: #ddd;
          border-radius: 4px;
          margin-top: 8px;
          overflow: hidden;
      }
      .project-progress-bar {
          height: 100%;
          background-color: var(--success-color);
          width: 0%;
          transition: width 0.5s ease-in-out;
      }


     .completed-project-item {
        border-color: var(--accent-color); /* Use accent color for completed */
        background-color: #FFF8E1; /* Light yellow */
     }
      .completed-project-item h4 {
         color: var(--accent-color);
      }
       .completed-project-item:hover {
           transform: none; /* No lift animation */
           box-shadow: none;
       }
       .completed-project-item p { font-size: 0.9em; }


    /* Buttons */
    button {
        padding: 12px 20px;
        margin: 5px;
        border: none;
        border-radius: var(--border-radius); /* Match panel radius */
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

     button:active {
         transform: scale(0.98);
     }

    .btn-primary {
        background-color: var(--primary-color);
        color: white;
    }
    .btn-primary:hover:not(:disabled) {
        background-color: #C0392B; /* Darker red */
    }

    .btn-secondary {
        background-color: var(--secondary-color);
        color: white;
    }
     .btn-secondary:hover:not(:disabled) {
         background-color: #2C3E50; /* Darker blue */
     }

    button:disabled, .btn-disabled {
        background-color: #ccc;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Messages */
    .messages {
        max-height: 200px; /* Increased height for more messages */
        overflow-y: auto;
         border-top: 3px solid var(--accent-color); /* Highlight messages section */
    }

     .messages h3 { text-align: right; border-bottom: none; padding-bottom: 0;}

    .messages-list {
        padding-top: 10px;
    }

    .messages p {
        margin-bottom: 10px;
        padding-bottom: 10px;
        border-bottom: 1px dashed #eee;
        font-size: 0.9em;
        line-height: 1.5;
         color: #444;
    }
     .messages p:last-child { border-bottom: none; padding-bottom: 0; margin-bottom: 0;}
     .messages p.initial-message { color: var(--secondary-color); font-weight: bold;}
     .messages p.success { color: var(--success-color); }
     .messages p.failure { color: var(--danger-color); }
     .messages p.event { color: var(--accent-color); }


    /* Modal */
    .modal {
        display: none; /* Hidden by default */
        position: fixed; /* Stay in place */
        z-index: 100; /* Sit on top of game over screen */
        left: 0;
        top: 0;
        width: 100%; /* Full width */
        height: 100%; /* Full height */
        overflow: auto; /* Enable scroll if needed */
        background-color: rgba(0,0,0,0.7); /* Black w/ opacity */
        padding-top: 60px;
        animation: fadeIn 0.3s ease-in-out;
    }

    .modal-content {
        background-color: var(--panel-background);
        margin: 5% auto;
        padding: 30px; /* More padding */
        border: 1px solid var(--border-color);
        width: 90%;
        max-width: 600px; /* Increased max width */
        border-radius: var(--border-radius);
        position: relative;
        direction: rtl;
        text-align: right;
        box-shadow: var(--panel-shadow);
         animation: slideInFromTop 0.3s ease-in-out;
    }

    .close-button {
        color: #aaa;
        float: left; /* Position close button left for RTL */
        font-size: 30px;
        font-weight: bold;
        cursor: pointer;
        transition: color 0.2s ease;
    }

    .close-button:hover,
    .close-button:focus {
        color: var(--danger-color);
        text-decoration: none;
    }

    .modal h3 {
        margin-top: 0;
        margin-bottom: var(--spacing-unit);
        color: var(--primary-color);
        text-align: center;
    }

     .modal .list-items li {
         margin-bottom: 5px;
         font-size: 0.95em;
     }
      .modal .list-items ul { margin-bottom: var(--spacing-unit);}

     .modal-cost-estimate {
         font-weight: bold;
         margin-top: 10px;
         color: var(--secondary-color);
     }

    .modal button {
        display: block; /* Make button block for centered margin */
        margin: var(--spacing-unit) auto 10px auto;
    }

     .warning-message {
         color: var(--warning-color);
         text-align: center;
         font-weight: bold;
     }


    /* Explanation Toggle Button */
    #toggle-explanation {
        display: block;
        margin: var(--spacing-unit) auto;
         background-color: var(--secondary-color);
         color: white;
    }
     #toggle-explanation:hover {
         background-color: #2C3E50;
     }


    /* Explanation Section */
    #explanation {
        display: none; /* Initially hidden */
        margin-top: var(--spacing-unit);
        padding: var(--spacing-unit);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        background-color: var(--panel-background);
        direction: rtl;
        text-align: right;
        max-width: 1000px;
        margin-left: auto;
        margin-right: auto;
         box-shadow: var(--panel-shadow);
    }

     #explanation h2 { text-align: right; color: var(--primary-color); border-bottom: 2px solid var(--accent-color); padding-bottom: 10px; margin-bottom: 20px;}
     #explanation h3 { text-align: right; color: var(--secondary-color); margin-top: 20px; margin-bottom: 10px;}
     #explanation p { margin-bottom: 15px; color: #444;}


    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

     @keyframes slideInFromTop {
         from { transform: translateY(-50px); opacity: 0; }
         to { transform: translateY(0); opacity: 1; }
     }

     @keyframes pulse {
         0% { transform: scale(1); }
         50% { transform: scale(1.05); }
         100% { transform: scale(1); }
     }
     .pulse {
         animation: pulse 0.5s ease;
     }


     /* Basic Icons (using characters or simple shapes) */
     .icon-clipboard::before { content: '📋 '; }
     .icon-play::before { content: '▶️ '; }
     .icon-check::before { content: '✅ '; }
     .icon-alert::before { content: '⚠️ '; }
     .icon-success::before { content: '👍 '; }
     .icon-fail::before { content: '❌ '; }
     .icon-money::before { content: '💰 '; }
     .icon-reputation::before { content: '⭐ '; }
      .currency::after { content: ' ₪'; font-size: 0.8em;}


</style>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Game State
        let gameState = {}; // Initialize during resetGame

        // UI Elements
        const currentMonthEl = document.getElementById('current-month');
        const moneyEl = document.getElementById('money');
        const reputationEl = document.getElementById('reputation');
        const teamListEl = document.getElementById('team-list');
        const projectProposalsEl = document.getElementById('project-proposals');
        const activeProjectsEl = document.getElementById('active-projects');
        const completedProjectsEl = document.getElementById('completed-projects');
        const nextMonthBtn = document.getElementById('next-month-btn');
        const restartBtn = document.getElementById('restart-btn');
        const messagesListEl = document.getElementById('messages-list');
        const gameOverEl = document.getElementById('game-over');
        const gameOverMessageEl = document.getElementById('game-over-message');
        const restartGameOverBtn = document.getElementById('restart-game-over-btn');
         const gameContainer = document.getElementById('production-sim'); // For game over screen positioning

        // Modal Elements
        const projectModal = document.getElementById('project-modal');
        const closeButtons = document.querySelectorAll('.modal .close-button');
        const modalProjectTitle = document.getElementById('modal-project-title');
        const modalProjectDescription = document.getElementById('modal-project-description');
        const modalProjectBudget = document.getElementById('modal-project-budget');
        const modalProjectDuration = document.getElementById('modal-project-duration');
        const modalProjectPotential = document.getElementById('modal-project-potential');
        const modalProjectTeam = document.getElementById('modal-project-team');
        const modalInitialCost = document.getElementById('modal-initial-cost');
        const modalMonthlyCost = document.getElementById('modal-monthly-cost');
        const acceptProjectBtn = document.getElementById('accept-project-btn');
         const acceptProjectMessageEl = document.getElementById('accept-project-message');

        // Event Modal
        const eventModal = document.getElementById('event-modal');
        const eventTitleEl = document.getElementById('event-title');
        const eventDescriptionEl = document.getElementById('event-description');
        const eventOkBtn = document.getElementById('event-ok-btn');


        let selectedProjectId = null; // To keep track of the project selected in the modal

        // Project Definitions (Templates) - More varied and interesting names/descriptions
        const projectTemplates = [
             {
                id: 'template-1',
                title: 'קצר: "מפגש בוקר" - סיפורי המאפייה השכונתית',
                description: 'סרט אינטימי על משפחת אופים ותיקה, עליית השחר והפגישה עם הקהילה שנוצרת סביב לחם טרי. חום, ריחות ונוסטלגיה.',
                baseBudget: 35000, // Slightly increased
                baseDuration: 4, // months
                potential: 'מקומי, לבבי, פוטנציאל לפסטיבלים קטנים וקהילות אונליין.',
                requiredTeam: { director: 0.5, camera: 0.5, editor: 0.5, lineProducer: 0.2 }, // Add minimal line producer involvement
                initialCostFactor: 0.2,
                monthlyCostFactor: 0.15,
                completionBonusFactor: 1.5,
                completionReputation: 12, // Slightly increased
                failurePenaltyMoneyFactor: 0.5,
                failurePenaltyReputation: -5
            },
             {
                id: 'template-2',
                title: 'סדרת רשת: "חיים בדיגיטל" - המהפכה בבית',
                description: 'מסע ויזואלי ואינטלקטואלי אל תוך הבית המודרני - איך גאדג\'טים, AI וחיבוריות משנים את האופן בו אנו חיים, עובדים ומתקשרים? ראיונות עם מומחים ואנשים רגילים.',
                baseBudget: 90000, // Slightly increased
                baseDuration: 6,
                potential: 'רלוונטי, קהל רחב, פוטנציאל להכנסות מפלטפורמות סטרימינג וחסויות.',
                requiredTeam: { director: 1, camera: 1, editor: 1, lineProducer: 0.7 }, // More LP involvement
                 initialCostFactor: 0.15,
                monthlyCostFactor: 0.12, // Slightly increased monthly cost
                completionBonusFactor: 1.7, // Slightly adjusted
                completionReputation: 22, // Slightly increased
                failurePenaltyMoneyFactor: 0.6, // Lose a bit less on failure
                failurePenaltyReputation: -10
            },
             {
                id: 'template-3',
                title: 'פיצ\'ר: "צדק ארכיוני" - תיק היסטורי בלתי פתור',
                description: 'חקירה עיתונאית וקולנועית מעמיקה של פרשת היסטורית אפלה, תוך שימוש בחומרי ארכיון נדירים ועדויות חדשות. דורש נסיעות וריאיונות מורכבים.',
                baseBudget: 180000, // Significantly increased budget
                baseDuration: 10, // Longer duration
                potential: 'יוקרתי, פוטנציאל לפסטיבלים בינלאומיים, פרסים והשפעה ציבורית משמעותית.',
                requiredTeam: { director: 1.5, camera: 1.5, editor: 1.5, lineProducer: 1.5 }, // Higher team requirements
                 initialCostFactor: 0.3, // Higher initial cost
                monthlyCostFactor: 0.15, // Higher monthly cost
                completionBonusFactor: 2.5, // Higher potential reward
                completionReputation: 40, // Higher potential reputation
                failurePenaltyMoneyFactor: 0.9, // Lose most spent money
                failurePenaltyReputation: -20 // Higher reputation penalty
            },
             {
                id: 'template-4',
                title: 'קצר: "קירות מדברים" - אמנות הרחוב בעיר',
                description: 'תיעוד סוחף וצבעוני של סצנת אמנות הרחוב המקומית - גרפיטי, סטנסילים, מיצגים. מבט על הקולות שמשנים את מרקם העיר.',
                baseBudget: 28000, // Slightly increased
                baseDuration: 3,
                potential: 'אסתטי, קהל צעיר, פוטנציאל לפלטפורמות אונליין וגלריות אלטרנטיביות.',
                requiredTeam: { director: 0.7, camera: 1, editor: 0.7 }, // Slightly higher requirements
                 initialCostFactor: 0.12,
                monthlyCostFactor: 0.22, // Slightly higher monthly cost
                completionBonusFactor: 1.4,
                completionReputation: 10, // Slightly increased
                failurePenaltyMoneyFactor: 0.5,
                failurePenaltyReputation: -5
            },
             {
                 id: 'template-5',
                 title: 'קצר: "גיבורי שוליים" - מבט על מתנדבים מקומיים',
                 description: 'פרופיל של אנשים שפועלים בשקט למען הקהילה. סיפורים קטנים עם השפעה גדולה. פרויקט קהילתי.',
                 baseBudget: 20000,
                 baseDuration: 3,
                 potential: 'קהילתי, מחמם לב, פוטנציאל למענקים קטנים והכרה מקומית.',
                 requiredTeam: { director: 0.3, camera: 0.5, editor: 0.5 }, // Lower requirements
                  initialCostFactor: 0.05, // Very low initial cost
                 monthlyCostFactor: 0.18,
                 completionBonusFactor: 1.2,
                 completionReputation: 7,
                 failurePenaltyMoneyFactor: 0.3,
                 failurePenaltyReputation: -3
             }
            // Add more project templates here to increase variety
        ];

        // Random Events
        const randomEvents = [
            {
                id: 'event-1',
                title: 'ציוד התקלקל!',
                description: 'מצלמה יקרה נפלה ונשברה. עלות תיקון או החלפה.',
                type: 'bad',
                probability: 0.1, // 10% chance per month
                effect: (state) => {
                    const cost = Math.round(state.money * 0.05); // 5% of current money
                    state.money -= cost;
                    addMessage(`אירוע: ${this.title} - ${cost.toLocaleString()} ₪ ירדו מהתקציב לתיקון/החלפת ציוד.`, 'event');
                    return { title: this.title, description: `${this.description}\nהוצאה: ${cost.toLocaleString()} ₪.` };
                }
            },
             {
                 id: 'event-2',
                 title: 'קיבלתם ציון לשבח מקומי!',
                 description: 'ההתנהלות המקצועית שלכם בפרויקט קודם זכתה לשבחים בעיתונות המקומית.',
                 type: 'good',
                 probability: 0.08, // 8% chance
                 effect: (state) => {
                     const repGain = Math.round(Math.random() * 5) + 3; // Gain 3-8 reputation
                     state.reputation += repGain;
                     addMessage(`אירוע: ${this.title} - המוניטין עלה ב-${repGain}!`, 'event');
                      return { title: this.title, description: `${this.description}\nהמוניטין שלך עלה ב-${repGain}.` };
                 }
             },
             {
                 id: 'event-3',
                 title: 'הצעה מפתיעה למימון!',
                 description: 'גוף בלתי צפוי מעוניין להשקיע בפרויקט פעיל או להציע מימון לפרויקט חדש (בהנחה שיילקח).',
                 type: 'good',
                 probability: 0.05, // 5% chance
                 effect: (state) => {
                     const grant = Math.round(Math.random() * 20000) + 10000; // Gain 10k-30k
                     state.money += grant;
                     addMessage(`אירוע: ${this.title} - קיבלתם מענק של ${grant.toLocaleString()} ₪!`, 'event');
                      return { title: this.title, description: `${this.description}\nקיבלת מענק בסך ${grant.toLocaleString()} ₪.` };
                 }
             },
             {
                 id: 'event-4',
                 title: 'עיכוב בירוקרטי!',
                 description: 'אישור הכרחי לצילומים התעכב משמעותית, דוחה את התקדמות הפרויקטים הפעילים.',
                 type: 'bad',
                 probability: 0.12, // 12% chance - more common setback
                 effect: (state) => {
                     let affectedProjects = 0;
                     state.activeProjects.forEach(p => {
                         // Randomly add 1-2 months to duration, minimum 1
                         const delay = Math.max(1, Math.round(Math.random() * 2));
                         p.duration += delay;
                         addMessage(`  >> פרויקט "${p.title}" מתעכב ומשך ההפקה המעורך הוארך ב-${delay} חודשים. (סה"כ ${p.duration})`, 'event');
                         affectedProjects++;
                     });
                      if(affectedProjects === 0) {
                           addMessage(`אירוע: ${this.title} - היו עיכובים, אך הם לא השפיעו על הפרויקטים הנוכחיים (או שאין כאלה).`, 'event');
                           return { title: this.title, description: `${this.description}\n(לא היו פרויקטים פעילים שהושפעו הפעם).` };
                      }
                     return { title: this.title, description: `${this.description}\n${affectedProjects} פרויקט/ים פעיל/ים הושפעו.` };
                 }
             }
            // Add more event types
        ];


         // Helper function to generate a unique project ID
        function generateProjectId() {
            return 'project-' + Date.now() + '-' + Math.floor(Math.random() * 1000);
        }

         // Helper for number animation
         function animateNumberChange(element, start, end, duration, prefix = '', suffix = '') {
            const range = end - start;
            const startTime = performance.now();
            const isMoney = element.id === 'money'; // Special formatting for money

            function updateValue(timestamp) {
                const elapsed = timestamp - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const currentValue = start + range * progress;

                if (isMoney) {
                     element.textContent = Math.round(currentValue).toLocaleString();
                } else {
                     element.textContent = Math.round(currentValue);
                }


                if (progress < 1) {
                    requestAnimationFrame(updateValue);
                } else {
                     if (isMoney) {
                          element.textContent = end.toLocaleString();
                     } else {
                          element.textContent = end;
                     }

                     // Add/remove animation class based on change
                     if (range !== 0) {
                         element.classList.add('pulse');
                         if (range > 0) {
                             element.classList.add('change-up');
                         } else {
                             element.classList.add('change-down');
                         }
                         setTimeout(() => {
                             element.classList.remove('pulse', 'change-up', 'change-down');
                         }, duration + 100); // Remove class after animation
                     }
                }
            }

            requestAnimationFrame(updateValue);
        }


        // Game Logic Functions

        function updateUI() {
             // Animate stat changes
             animateNumberChange(currentMonthEl, parseInt(currentMonthEl.textContent.replace(/,/g, '')) || gameState.month - 1, gameState.month, 500);
             animateNumberChange(moneyEl, parseInt(moneyEl.textContent.replace(/,/g, '')) || gameState.money, gameState.money, 800);
             animateNumberChange(reputationEl, parseInt(reputationEl.textContent.replace(/,/g, '')) || gameState.reputation, gameState.reputation, 800);


            // Update team list
             let teamHtml = '';
             const teamRoleNames = {
                 producer: 'מפיק ראשי',
                 director: 'במאי',
                 camera: 'צלם',
                 editor: 'עורך',
                 lineProducer: 'מפיק בפועל'
             };
             for (const role in gameState.team) {
                 if (gameState.team[role].count > 0) {
                      const roleName = teamRoleNames[role] || role;
                     teamHtml += `<div class="team-member">${roleName} (${gameState.team[role].count}) - ${gameState.team[role].cost.toLocaleString()} ₪/חודש</div>`;
                 }
             }
             teamListEl.innerHTML = teamHtml;


            // Update project proposals
            projectProposalsEl.innerHTML = '';
            if (gameState.availableProjects.length === 0) {
                projectProposalsEl.innerHTML = '<p class="placeholder">אין הצעות חדשות החודש. אולי בחודש הבא...</p>';
            } else {
                gameState.availableProjects.forEach(project => {
                    const div = document.createElement('div');
                    div.classList.add('project-item');
                    div.dataset.projectId = project.id;
                    div.innerHTML = `
                        <h4>${project.title}</h4>
                        <p><span class="icon-money"></span> תקציב: ${project.budget.toLocaleString()} ₪ | <span class="icon-clipboard"></span> משך: ${project.duration} חודשים</p>
                         <p><span class="icon-reputation"></span> פוטנציאל: ${project.potential}</p>
                    `;
                    div.addEventListener('click', () => showProjectModal(project.id));
                    projectProposalsEl.appendChild(div);
                });
            }

            // Update active projects
            activeProjectsEl.innerHTML = '';
            if (gameState.activeProjects.length === 0) {
                activeProjectsEl.innerHTML = '<p class="placeholder">אין פרויקטים בעבודה כרגע. קבל/י הצעה!</p>';
            } else {
                gameState.activeProjects.forEach(project => {
                    const div = document.createElement('div');
                    div.classList.add('active-project-item');
                    const progressPercent = Math.min(100, (project.progress / project.duration) * 100).toFixed(0);
                    div.innerHTML = `
                        <h4>${project.title}</h4>
                         <p>חודש <span class="stat-value">${project.progress}</span> מתוך <span class="stat-value">${project.duration}</span></p>
                         <div class="project-progress"><div class="project-progress-bar" style="width: ${progressPercent}%"></div></div>
                         <p><span class="icon-money"></span> הוצאה חודשית מוערכת: ${(project.budget * project.monthlyCostFactor).toLocaleString()} ₪</p>
                    `;
                     // Optional: Add click to see details modal for active projects too
                    // div.addEventListener('click', () => showProjectModal(project.id, true)); // Pass true for active project
                    activeProjectsEl.appendChild(div);
                });
            }

             // Update completed projects
            completedProjectsEl.innerHTML = '';
            if (gameState.completedProjects.length === 0) {
                completedProjectsEl.innerHTML = '<p class="placeholder">הפרויקטים שתשלים/י יופיעו כאן.</p>';
            } else {
                gameState.completedProjects.forEach(project => {
                    const div = document.createElement('div');
                    div.classList.add('completed-project-item');
                    const result = project.success ? 'הושלם בהצלחה' : 'הופסק / כשל';
                     const earnings = project.success ? `(<span class="icon-money success"></span>+${(project.budget * project.completionBonusFactor).toLocaleString()} ₪, <span class="icon-reputation success"></span>+${project.completionReputation})`
                                                      : `(<span class="icon-money danger"></span> עלויות שקעו: ${project.spentMoney.toLocaleString()} ₪, <span class="icon-reputation danger"></span>${project.failurePenaltyReputation})`;
                     const resultClass = project.success ? 'success' : 'failure';
                    div.innerHTML = `
                        <h4>${project.title}</h4>
                        <p><span class="icon-${resultClass}"></span> סטטוס: ${result} ${earnings}</p>
                    `;
                    completedProjectsEl.appendChild(div);
                });
            }

             // Update Game Over state
             if (gameState.gameOver) {
                 gameOverEl.classList.add('visible');
                 nextMonthBtn.disabled = true;
                 restartBtn.style.display = 'none'; // Hide the inline restart button
             } else {
                 gameOverEl.classList.remove('visible');
                 nextMonthBtn.disabled = false;
                 restartBtn.style.display = 'inline-block'; // Show the inline restart button
             }

        }

        function addMessage(text, type = '') {
            const p = document.createElement('p');
             p.classList.add(type); // Add class for styling (success, failure, event)
            p.textContent = `חודש ${gameState.month}: ${text}`;
            messagesListEl.prepend(p); // Add to the top
             // Limit messages to prevent performance issues / screen clutter
             while(messagesListEl.children.length > 30) { // Increased limit
                 messagesListEl.removeChild(messagesListEl.lastChild);
             }
        }

        function generateProjectProposals() {
            // Clear previous proposals unless game just started
            if (gameState.month > 1) {
                gameState.availableProjects = [];
            }

            const numProposals = Math.floor(Math.random() * 3) + 1; // 1 to 3 new proposals

            for (let i = 0; i < numProposals; i++) {
                 const template = projectTemplates[Math.floor(Math.random() * projectTemplates.length)];
                 const variance = (Math.random() * 0.3 - 0.15); // +/- 15% variance (slightly less variance)
                 const budget = Math.round(template.baseBudget * (1 + variance));
                 const duration = Math.max(2, Math.round(template.baseDuration * (1 + variance * 0.5))); // Min duration 2 months, less duration variance

                 const newProject = {
                    id: generateProjectId(), // Unique ID for this instance
                    templateId: template.id, // Reference to template
                    title: template.title,
                    description: template.description,
                    budget: budget,
                    duration: duration,
                    potential: template.potential,
                    requiredTeam: template.requiredTeam,
                    initialCost: Math.round(budget * template.initialCostFactor),
                    monthlyCost: Math.round(budget * template.monthlyCostFactor),
                    completionBonusFactor: template.completionBonusFactor,
                    completionReputation: template.completionReputation,
                    failurePenaltyMoneyFactor: template.failurePenaltyMoneyFactor,
                    failurePenaltyReputation: template.failurePenaltyReputation,
                    progress: 0, // Months worked on the project
                    spentMoney: 0 // Money spent on this specific project
                 };
                 gameState.availableProjects.push(newProject);
            }
             if (gameState.month > 1 && numProposals > 0) {
                 addMessage(`התקבלו ${numProposals} הצעות פרויקטים חדשות!`, 'event');
             }
        }

        function checkTeamCapacity(requiredTeam) {
            let teamAvailable = { ...gameState.team }; // Copy team state
             // Subtract capacity used by active projects
             gameState.activeProjects.forEach(activeP => {
                 for (const role in activeP.requiredTeam) {
                      if (teamAvailable[role]) {
                          teamAvailable[role].count -= activeP.requiredTeam[role];
                      }
                 }
             });

             let hasEnoughTeam = true;
             let missingRoles = [];
             for (const role in requiredTeam) {
                 // Ensure the role exists in the base team structure before checking count
                 const availableCount = teamAvailable[role] ? teamAvailable[role].count : 0;
                 if (availableCount < requiredTeam[role]) {
                     hasEnoughTeam = false;
                      const roleName = { director: 'במאי', camera: 'צלם', editor: 'עורך', lineProducer: 'מפיק בפועל' }[role] || role;
                     missingRoles.push(`${roleName} (נדרש: ${requiredTeam[role]}, זמין: ${availableCount})`);
                 }
             }
             return { canAccept: hasEnoughTeam, missingRoles: missingRoles };
        }


        function canAcceptProject(project) {
            let messages = [];

            // Check if enough money for initial cost
            if (gameState.money < project.initialCost) {
                messages.push(`אין מספיק כסף (${gameState.money.toLocaleString()} ₪) לעלות התחלתית (${project.initialCost.toLocaleString()} ₪).`);
            }

            // Check team capacity
             const teamCheck = checkTeamCapacity(project.requiredTeam);
            if (!teamCheck.canAccept) {
                messages.push(`אין מספיק אנשי צוות זמינים. חסר: ${teamCheck.missingRoles.join(', ')}.`);
            }

            return { canAccept: messages.length === 0, messages: messages };
        }


        function acceptProject(projectId) {
            const projectIndex = gameState.availableProjects.findIndex(p => p.id === projectId);
            if (projectIndex === -1) return; // Project not found

            const project = gameState.availableProjects[projectIndex];
             const checkResult = canAcceptProject(project);

            if (checkResult.canAccept) {
                 // Deduct initial cost
                 gameState.money -= project.initialCost;
                 project.spentMoney += project.initialCost; // Track spent money on this project

                 // Move project from available to active
                 gameState.availableProjects.splice(projectIndex, 1);
                 gameState.activeProjects.push(project);

                 addMessage(`קיבלת את הפרויקט "${project.title}". עלות התחלתית: ${project.initialCost.toLocaleString()} ₪. בהצלחה!`, 'success');

                 // Close modal
                 closeProjectModal();
                 updateUI();
            } else {
                 // Display reason why it can't be accepted
                 acceptProjectMessageEl.innerHTML = checkResult.messages.join('<br>');
            }
        }

         function triggerRandomEvent() {
             const possibleEvents = randomEvents.filter(event => Math.random() < event.probability);
             if (possibleEvents.length > 0) {
                 // Pick one random event from the triggered ones
                 const event = possibleEvents[Math.floor(Math.random() * possibleEvents.length)];
                 const eventDetails = event.effect(gameState); // Apply effect and get details
                 showEventModal(eventDetails.title, eventDetails.description);
             }
         }

        function advanceTime() {
            if (gameState.gameOver) return;

            gameState.month++;
            addMessage('קדימה לחודש הבא...', 'event');


            // Pay monthly team salaries
            let totalSalaries = 0;
            for (const role in gameState.team) {
                totalSalaries += gameState.team[role].count * gameState.team[role].cost;
            }

             // Check if enough money for salaries + minimum active project costs
             let requiredMinimum = totalSalaries;
             gameState.activeProjects.forEach(p => {
                  // Assuming a project cannot continue without *some* monthly cost
                  // This is simplified, could be more complex check based on team availability
                  requiredMinimum += Math.round(p.budget * p.monthlyCostFactor * 0.5); // Need at least half monthly cost?
             });

             if (gameState.money < requiredMinimum) {
                 // Automatic failure due to lack of funds to even pay salaries/minimum project costs
                  endGame(false, `אזל הכסף! לא הצלחת לשלם משכורות ולהחזיק את הפרויקטים... בית ההפקה פשט רגל בחודש ${gameState.month}.`);
                  updateUI(); // Show final state before game over screen
                  return; // Stop processing
             }


            gameState.money -= totalSalaries;
            addMessage(`שולמו משכורות לצוות: ${totalSalaries.toLocaleString()} ₪.`, 'failure'); // Mark salary payment as an expense


            // Process active projects
            const completedThisMonth = [];
            const failedThisMonth = [];

            // Loop through active projects
             for (let i = gameState.activeProjects.length - 1; i >= 0; i--) {
                 const project = gameState.activeProjects[i];
                 const monthlyProjectCost = Math.round(project.budget * project.monthlyCostFactor);

                 // Check if enough money for THIS project's monthly cost
                 if (gameState.money < monthlyProjectCost) {
                     // Cannot afford monthly cost, project fails
                    addMessage(`אין מספיק כסף לקיים את הפרויקט "${project.title}" (נדרש: ${monthlyProjectCost.toLocaleString()} ₪, זמין: ${gameState.money.toLocaleString()} ₪). הפרויקט הופסק!`, 'danger');
                    failedThisMonth.push(project);
                    // Penalties: lose spent money AND reputation
                     // gameState.money -= project.spentMoney; // Option: lose all spent money
                    gameState.reputation += project.failurePenaltyReputation;
                 } else {
                    gameState.money -= monthlyProjectCost;
                    project.spentMoney += monthlyProjectCost;
                    project.progress++;
                    addMessage(`פרויקט "${project.title}" מתקדם. (התקדמות: חודש ${project.progress}/${project.duration})`, 'success');

                    // Check for completion
                    if (project.progress >= project.duration) {
                         addMessage(`פרויקט "${project.title}" הושלם בהצלחה!`, 'success');
                         completedThisMonth.push(project);

                         // Calculate earnings and reputation gain
                         const earnings = Math.round(project.budget * project.completionBonusFactor);
                         gameState.money += earnings;
                         gameState.reputation += project.completionReputation;
                         addMessage(`הפרויקט "${project.title}" הכניס ${earnings.toLocaleString()} ₪ והוסיף ${project.completionReputation} למוניטין.`, 'success');
                    }
                 }
             }


             // Move completed/failed projects from active list AFTER the loop
             completedThisMonth.forEach(project => {
                 project.success = true;
                 gameState.completedProjects.push(project);
                 gameState.activeProjects = gameState.activeProjects.filter(p => p.id !== project.id);
             });
            failedThisMonth.forEach(project => {
                 project.success = false;
                 gameState.completedProjects.push(project);
                 gameState.activeProjects = gameState.activeProjects.filter(p => p.id !== project.id);
             });


            // Generate new project proposals (less frequent after the start?)
             if (gameState.month === 1 || gameState.month % 3 === 0) { // Generate proposals on month 1 and every 3 months
                  generateProjectProposals();
             } else {
                 gameState.availableProjects = []; // No new proposals this month
             }


             // Trigger random event
             triggerRandomEvent();


             // Check for Game Over conditions
             if (gameState.money < 0) { // This check should ideally happen after all expenses and before next month
                 endGame(false, `אזל הכסף! ההוצאות הכריעו את בית ההפקה בחודש ${gameState.month}.`);
             } else if (gameState.reputation <= 0) {
                  endGame(false, `המוניטין ירד לשפל... אף אחד לא רוצה לעבוד איתך בחודש ${gameState.month}.`);
             } else if (gameState.month > 60) { // Arbitrary end condition after 5 years
                 endGame(true, `כל הכבוד! ניהלת את בית ההפקה בהצלחה במשך ${gameState.month -1} חודשים.\n בוא/י נראה כמה הצלחת...`);
             }


            updateUI(); // Update UI at the end of the month processing
        }

        function endGame(success, message) {
             gameState.gameOver = true;
             gameOverMessageEl.textContent = message;
              // Add final score calculation?
             if (success) {
                 gameOverMessageEl.textContent += `\nסיכום סופי: כסף נותר: ${gameState.money.toLocaleString()} ₪, מוניטין: ${gameState.reputation}.`;
             }
             updateUI();
             // Ensure game over screen is visible and centered
             const gameContainerRect = gameContainer.getBoundingClientRect();
              gameOverEl.style.top = `${gameContainerRect.top + window.scrollY}px`;
              gameOverEl.style.left = `${gameContainerRect.left + window.scrollX}px`;
              gameOverEl.style.width = `${gameContainerRect.width}px`;
              gameOverEl.style.height = `${gameContainerRect.height}px`;
        }


        function resetGame() {
            gameState = {
                month: 1,
                money: 100000,
                reputation: 50,
                team: {
                    producer: { count: 1, cost: 0 }, // Player
                    director: { count: 1, cost: 10000 },
                    camera: { count: 1, cost: 9000 },
                    editor: { count: 1, cost: 8000 },
                    lineProducer: { count: 1, cost: 9000 }
                },
                availableProjects: [],
                activeProjects: [],
                completedProjects: [],
                gameOver: false
            };
             messagesListEl.innerHTML = '<p class="initial-message">ברוך/ה הבא/ה למשרד החדש שלך! הצעות הפרויקטים הראשונות בדרך...</p>'; // Reset messages
            startGame(); // Restart the game flow
        }

        function startGame() {
            generateProjectProposals(); // Generate initial proposals
            updateUI();
        }

         function showProjectModal(projectId) { // Removed isActive param, simplified
            const project = gameState.availableProjects.find(p => p.id === projectId);

            if (!project) return; // Only show modal for available projects

             selectedProjectId = projectId; // Store for accept button

            modalProjectTitle.textContent = project.title;
            modalProjectDescription.textContent = project.description;
            modalProjectBudget.textContent = project.budget.toLocaleString();
            modalProjectDuration.textContent = project.duration;
            modalProjectPotential.textContent = project.potential;
             modalInitialCost.textContent = project.initialCost.toLocaleString();
             modalMonthlyCost.textContent = project.monthlyCost.toLocaleString();


             // Display required team and estimated cost contribution per role
            modalProjectTeam.innerHTML = '';
            const teamRoleNames = {
                producer: 'מפיק ראשי',
                director: 'במאי',
                camera: 'צלם',
                editor: 'עורך',
                lineProducer: 'מפיק בפועל'
            };
            for (const role in project.requiredTeam) {
                 const roleName = teamRoleNames[role] || role;
                 const requiredCount = project.requiredTeam[role];
                  // Calculate monthly cost for this specific role requirement IF we had to hire them
                  // Note: This doesn't mean you pay extra if you already have them, it's just showing the cost contribution *of* that role
                 const teamCost = gameState.team[role] ? gameState.team[role].cost : 0;
                 const monthlyCostForRole = requiredCount * teamCost; // Cost PER PERSON required
                 const listItem = document.createElement('li');
                 listItem.textContent = `${roleName}: ${requiredCount} (עלות כ"א משוערת בחודש: ${(teamCost).toLocaleString()} ₪)`; // Show cost per person
                 modalProjectTeam.appendChild(listItem);
             }

             // Check if project can be accepted and update button/message
             const checkResult = canAcceptProject(project);
             acceptProjectBtn.disabled = !checkResult.canAccept;
             acceptProjectMessageEl.innerHTML = checkResult.canAccept ? '' : checkResult.messages.join('<br>');
             acceptProjectBtn.style.display = 'block'; // Always show accept button for proposals

            projectModal.style.display = 'block';
        }

         function showEventModal(title, description) {
             eventTitleEl.textContent = title;
             eventDescriptionEl.textContent = description;
             eventModal.style.display = 'block';
         }

        function closeProjectModal() {
            projectModal.style.display = 'none';
            selectedProjectId = null;
            acceptProjectMessageEl.innerHTML = ''; // Clear previous messages
        }
         function closeEventModal() {
             eventModal.style.display = 'none';
         }


        // Event Listeners
        nextMonthBtn.addEventListener('click', advanceTime);
        restartBtn.addEventListener('click', resetGame);
        restartGameOverBtn.addEventListener('click', resetGame);

        // Close modals using close buttons or clicking outside
        closeButtons.forEach(button => button.addEventListener('click', (event) => {
             const modal = event.target.closest('.modal');
             if (modal.id === 'project-modal') closeProjectModal();
             if (modal.id === 'event-modal') closeEventModal();
        }));

        window.addEventListener('click', (event) => {
            if (event.target === projectModal) {
                closeProjectModal();
            }
             if (event.target === eventModal) {
                 closeEventModal();
             }
        });

        eventOkBtn.addEventListener('click', closeEventModal);


        acceptProjectBtn.addEventListener('click', () => {
            if (selectedProjectId && !acceptProjectBtn.disabled) {
                acceptProject(selectedProjectId);
            }
        });


         // Explanation Toggle
        const toggleExplanationBtn = document.getElementById('toggle-explanation');
        const explanationDiv = document.getElementById('explanation');

        toggleExplanationBtn.addEventListener('click', () => {
            const isHidden = explanationDiv.style.display === 'none';
            explanationDiv.style.display = isHidden ? 'block' : 'none';
             toggleExplanationBtn.textContent = isHidden ? 'הסתר הסבר' : 'הצג/הסתר הסבר';
        });


        // Initial Game Start
        resetGame(); // Use resetGame to initialize state and start
    });
</script>