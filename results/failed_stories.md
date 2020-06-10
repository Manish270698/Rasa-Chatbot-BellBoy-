## happy path 1 (C:\Users\manis\AppData\Local\Temp\tmpyj2kgh7x\b8600596af864c07a428c38e641a0a08_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: action_default_fallback -->


## happy path 2 (C:\Users\manis\AppData\Local\Temp\tmpyj2kgh7x\b8600596af864c07a428c38e641a0a08_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: action_default_fallback -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 1 (C:\Users\manis\AppData\Local\Temp\tmpyj2kgh7x\b8600596af864c07a428c38e641a0a08_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: confirm: yes -->
    - utter_happy   <!-- predicted: action_default_fallback -->


## sad path 2 (C:\Users\manis\AppData\Local\Temp\tmpyj2kgh7x\b8600596af864c07a428c38e641a0a08_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 3 (C:\Users\manis\AppData\Local\Temp\tmpyj2kgh7x\b8600596af864c07a428c38e641a0a08_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: action_default_fallback -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: action_default_fallback -->


