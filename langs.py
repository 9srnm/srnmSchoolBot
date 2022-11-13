langs = {
    'en': {
        'keyboards': {
            'edit_class': {
                'name': "⚙ Edit name",
                'delete': "❌ Delete class",
                'cancel': "🔙 Cancel"
            },
            'new_class': {
                'cancel': "🔙 Cancel"
            },
            'delete_class': {
                'yes': "👍 Yes, I am!",
                'no': "😢 Nooo!"
            },
            'sure_delete_class': {
                'yes': "✅ No doubt!",
                'no': "❌ Not on your life!"
            },
            'settings': {
                'admins': "👨‍💻 Change admins",
                'lang': "💭 Language: {lang}",
                'notify': "🔔 Notifications: {notify}",
                'timezone': "✈ Timezone: UTC{timezone}",
                'time': "⏰ Notifications time",
                'cancel': "🔙 Cancel"
            },
            'timezone': {
                'back': "🔙 Back",
                '-12': "UTC−12, USA, Baker Island",
                '-11': "UTC−11, USA, Samoa",
                '-10': "UTC−10, USA, Hawaii",
                '-9': "UTC−9, France, Gambier Islands",
                '-8': "UTC−8, USA, Washington",
                '-7': "UTC−7, USA, New Mexico",
                '-6': "UTC−6, USA, Minnesota",
                '-5': "UTC−5, USA, New York",
                '-4': "UTC−4, Dominican Republic",
                '-3': "UTC−3, Argentina",
                '-2': "UTC−2, Brazil, Fernando de Noronha",
                '-1': "UTC−1, Portugal, Azores islands",
                '+0': "UTC+0, Ireland",
                '+1': "UTC+1, Germany",
                '+2': "UTC+2, Russia, Kaliningrad",
                '+3': "UTC+3, Russia, Moscow",
                '+4': "UTC+4, Russia, Samara",
                '+5': "UTC+5, Russia, Yekaterinburg",
                '+6': "UTC+6, Russia, Omsk",
                '+7': "UTC+7, Russia, Krasnoyarsk",
                '+8': "UTC+8, Russia, Irkutsk",
                '+9': "UTC+9, Russia, Amur",
                '+10': "UTC+10, Russia, Vladivostok",
                '+11': "UTC+11, Russia, Magadan",
                '+12': "UTC+12, Fiji",
                '+13': "UTC+13, Samoa",
                '+14': "UTC+14, Kitibati, Line Islands",
            },
            'time_settings': {
                'save': "✅ Save cahnges",
                'lesson': "👨‍🎓 Before lesson",
                'left': "◀",
                'before': "{mins} min.",
                'right': "▶",
                'day': "📆 Day before",
                'hours': "{hours} h.",
                'minutes': "{mins} min.",
                'back': "🔙 Back"
            },
            'groups': {
                'add': "➕ Add group",
                'cancel': "🔙 Cancel"
            },
            'add_group': {
                'back': "🔙 Back"
            },
            'group': {
                'name': "♻ Edit name",
                'delete': "❌ Delete group",
                'back': "🔙 Back"
            },
            'edit_group_name': {
                'cancel': "🔙 Cancel"
            },
            'delete_group': {
                'yes': "✅ Sure",
                'no': "❌ Not at all"
            },
            'admins': {
                'add': "➕ Add admin",
                'back': "🔙 Back"
            }
        },
        'start':
            """
Hi {name}! 👋

📅 I'm @srnmSchoolBot for scheduling your school *lessons* and reminding you about your *school tasks* 📝

📌 For more _info_ try /help
            """,
        'help':
            """
🤔 To use @srnmSchoolBot add it into *your class chat*
After that use _this commands_ in order and _follow instructions_:

📍 /class — firstly, you should create your class. Type in name of it. If it is already created, you can change its name or delete it with all data!

📍 /settings — after you have created your class, you should go to settings to choose the language and your timezone and change the notification system
            """,
        'not_group':
            """
❌ To use @srnmSchoolBot and its command you should chat with it in a group!

📍 For detailed instructions use /help
            """,
        'not_text':
            """
🤔 Make sure that what you send is a text message!
            """,
        'only_admin':
            """
❌ Only admin can do this!
            """,
        'too_fast':
            """
❌ Don't click too fast. Retry in {seconds} seconds!
            """,
        'edit_class':
            """
😍 This is your class: *{name}*

👉 Here you can change its name or *delete* it

_❗❗❗ WARNING ❗❗❗
Note that if you delete your class, all data including groups and timetables will be deleted_
            """,
        'edit_class_name':
            """
Choose a new name for your class...
            """,
        'edit_class_name_changed':
            """
♻ Class name was changed on *{name}*
            """,
        'new_class':
            """
What would be the name of your class?
            """,
        'new_class_created':
            """
🎉 Your class with name *{name}* has been successfully created!

📍 Don't forget to check out /settings before using the bot!

👨‍🎓 To use scheduling feature, create at least _one group_ via /groups
            """,
        'delete_class':
            """
❓ Are you sure you want to delete your class *{name}*? 

All your data will be deleted including your groups and timetables for this groups! ❌
            """,
        'sure_delete_class':
            """
🤔 *100% SURE???*
            """,
        'sure_delete_class_deleted':
            """
✅ Your class has been successfully deleted!

📍 You can create a new one via /class
            """,
        'no_class':
            """
📌 Class is not created yet. Use /class to do it
            """,
        'settings':
            """
⚙ Here you can change the settings for your class *{name}*:

📍 Change language the bot will chat with you
📍 Turn on/off (✅/❌) the notifications about the lessons on the next day and about the next lesson
📍 Change your timezone to get your notifications just in time
📍 Change the time you will be notified
            """,
        'timezone':
            """
🗺 Choose the timezone where your class *{name}* is located!

This is needed to make the bot usable in different countries with different timezones ⏳
            """,
        'time_settings':
            """
⏰ Here you can choose when you want to be notified about lessons in your class *{name}*...

🔜 Firstly, choose the time gap before the lesson when @srnmSchoolBot will send you a message about next lesson

🕰 Then choose the exact time of the day when you will be notified about the next day lessons
            """,
        'groups':
            """
📈 Here you can create groups to edit your lessons timetable or choose an existing one!
            """,
        'add_group':
            """
What would be the name of a new group?
            """,
        'added_group':
            """
✅ Group *{class_name} {group}* has been added successfully! Check out /timetable to schedule your lessons
            """,
        'group':
            """
⚙ This is *{class_name} {group}*. Here you can edit your group's name or delete it!
            """,
        'edit_group_name':
            """
🤔 Choose a new name for *{class_name} {group}*
            """,
        'edit_group_name_changed':
            """
✅ Group name has been changed!
            """,
        'delete_group':
            """
🤔 Are you sure you want to delete *{class_name} {group}*? _All the *timetables* for this group will be *deleted*!_
            """,
        'deleted_group':
            """
✅ Group has been successfully deleted!
            """,
        'admins':
            """
👉 Here is an admin list of *{name}*!

📌 You can delete the existing one (except for yourself) or add a new one (maximum of 5 admins) 
            """,
        'add_admin':
            """
✍ Type in an id of the user you want to be an admin

_📍 You can ask a user you want to add to look his id in @userinfobot_
            """,
        'incorrect_admin':
            """
❗ ID must be not longer than 10 symbols
            """
    }
}