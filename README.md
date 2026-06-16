# Text Scene Handler

A text scene parser and processing tool developed for Ren'Py visual novel projects.

The tool automates dialogue tagging and scene preparation, reducing manual work during content production and localization workflows.

## 🚀 Installation
- Clone the repository: git clone https://github.com/AgentCorgi008/AudioAnimationTester.git
- Paste your text into the “source” folder in .txt format and ready for use

## 🛠 Features
- Dialogue parsing
- Automatic text tagging
- Scene processing automation
- Content preparation pipeline
- Customize for your needs parsing of dialogues

## How to custom

Just create your own ```scene_nandler``` and extend or change all of any ```SceneHandler``` attributes:
```python
# modify here
class SceneHandler:
    SYMBOLS_TRIGGER = (",", "...", "!", ".", "?", "…", "*", "~")
    IGNORE_PERS = ("gg", "gg_th")
    SKIP_LINE_BASED_ON_SYMBOL = ("#", "*", "(", "-")

...

# create new a use that one
# first - directory, second - added tag
scene_handler = SceneHandler("source", "[hrtimg]")
```

## 🛠 Technologies
- Python
- Ren'Py

## ✨ Purpose
Created to automate processing of large volumes of narrative content and accelerate text production workflows during game development.
