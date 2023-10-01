from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from web_app.models import emailform
from web_app.forms import Email_form
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from random import randint, choice
from django.core.mail import EmailMessage
import pytz

import smtplib
 

def index(request):

    return render(request, "index.html")


def works(request):
    return render(request, "work.html")


def about(request):

    return render(request, "about.html")



def greeting_message(username = None):
    current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    messages = {
      "morning":[
        f"{username}, Good Morning! Start your day with a smile on your face..!",
        f"{username}, Good morning! Wishing you a day filled with positivity and joy.",
        f"{username}, Rise and shine! Today is a brand new opportunity to make the most of.",
        f"{username}, Hello world! It's a beautiful morning to start afresh.",
        f"{username}, Good morning! May your day be as bright as the sun.",
        f"{username}, Wake up and smile! It's the start of another wonderful day.",
        f"{username}, Good morning! Let your actions today reflect your goals and aspirations.",
        f"{username}, Rise and grind! Success comes to those who work for it.",
        f"{username}, Hello, early bird! Embrace the day with enthusiasm.",
        f"{username}, Good morning! Start your day with a grateful heart.",
        f"{username}, Seize the day! Your potential is limitless.",
        f"{username}, Rise and shine, it's coffee time!",
        f"{username}, Good morning! Make today amazing.",
        f"{username}, Wake up with determination, go to bed with satisfaction.",
        f"{username}, Embrace the morning breeze and let it invigorate your spirit.",
        f"{username}, Good morning! Each day is a new chance to be better than yesterday.",
        f"{username}, Rise and conquer! Today is yours for the taking.",
        f"{username}, Hello sunshine! You have the power to brighten the world.",
        f"{username}, Good morning! Remember, you are capable of achieving greatness.",
        f"{username}, Start your day with a smile and positive thoughts.",
        f"{username}, Rise and shine! Life is full of possibilities waiting for you.",
        f"{username}, Good morning! Chase your dreams with unwavering determination.",
        f"{username}, Make today count! Your journey to success begins now.",
        f"{username}, Wake up, it's a new day filled with opportunities and adventures.",
        f"{username}, Good morning! Embrace the challenges, they lead to growth.",
        f"{username}, Rise and sparkle! Your light can illuminate the darkest of days.",
        f"{username}, Hello, world changer! Make a positive impact today.",
        f"{username}, Good morning! Your potential knows no bounds.",
        f"{username}, Start your day with a grateful heart and a positive mindset.",
        f"{username}, Rise and thrive! Success is the result of persistent effort.",
        f"{username}, Every morning is a fresh start, a chance to rewrite your story.",
        f"{username}, Good morning! Seize the day with both hands and make it yours.",
        f"{username}, Embrace the morning calm and let it bring you inner peace.",
        f"{username}, Rise and shine! Your journey to success begins with a single step.",
        f"{username}, Hello, dreamer! Your goals are within reach.",
        f"{username}, Good morning! Believe in yourself, and you'll achieve greatness.",
        f"{username}, Wake up, it's a brand new day to create wonderful memories.",
        f"{username}, Start your day with gratitude, and watch your blessings multiply.",
        f"{username}, Rise and conquer! Challenges are stepping stones to success.",
        f"{username}, Embrace the morning with open arms and a positive attitude.",
        f"{username}, Good morning! Your potential is limitless; don't underestimate it.",
        f"{username}, Rise and shine! Today is a gift; make the most of it.",
        f"{username}, Hello, world changer! You have the power to make a difference.",
        f"{username}, Good morning! Make each moment count on your journey.",
        f"{username}, Wake up, it's a new day filled with endless possibilities.",
        f"{username}, Start your day with a smile, and positivity will follow.",
        f"{username}, Rise and sparkle! Let your enthusiasm light up the day.",
        f"{username}, Embrace the morning tranquility and find your inner strength.",
        f"{username}, Good morning! Chase your dreams with unwavering determination.",
        f"{username}, Rise and thrive! Success is the result of relentless effort.",
        f"{username}, Hello, champion! Today is another opportunity to excel."
      ],
      "afternoon":[
        f"{username}, Good Afternoon, How are you doing, had your lunch...?",
        f"{username}, Good afternoon! I hope you're having a fantastic day so far.",
        f"{username}, Hello there! Wishing you a peaceful and productive afternoon.",
        f"{username}, Afternoons are for refueling. Enjoy your break!",
        f"{username}, Good afternoon! May your day continue to be filled with positivity.",
        f"{username}, Time for a quick recharge! Have a great afternoon.",
        f"{username}, Hello, busy bee! Keep up the good work this afternoon.",
        f"{username}, Good afternoon! Take a moment to relax and refresh.",
        f"{username}, Afternoons are a second chance to make your day even better.",
        f"{username}, Hey, you! Hope your afternoon is as bright as your morning.",
        f"{username}, Good afternoon! Keep those good vibes rolling.",
        f"{username}, Take a deep breath, it's the afternoon! You've got this.",
        f"{username}, Hello, sunshine! The afternoon is your canvas; paint it bright.",
        f"{username}, Good afternoon! Stay focused and make every moment count.",
        f"{username}, Don't forget to pause and enjoy the beauty of this afternoon.",
        f"{username}, Afternoons are perfect for catching up and connecting.",
        f"{username}, Hello, superstar! Continue to shine this afternoon.",
        f"{username}, Good afternoon! Your hard work is paying off.",
        f"{username}, Keep the momentum going! It's a productive afternoon ahead.",
        f"{username}, Hey, champ! Conquer the afternoon with confidence.",
        f"{username}, Good afternoon! Let's make the rest of the day amazing.",
        f"{username}, Recharge your energy for the afternoon journey ahead.",
        f"{username}, Hello, go-getter! Your determination shines this afternoon.",
        f"{username}, Good afternoon! Stay positive, and the day will be a breeze.",
        f"{username}, Take a moment to appreciate the beauty of this afternoon.",
        f"{username}, Afternoons are for taking small steps toward big goals.",
        f"{username}, Hello, dreamer! Keep chasing your dreams this afternoon.",
        f"{username}, Good afternoon! May your day be as bright as the sun.",
        f"{username}, Stay motivated and conquer the challenges of the afternoon.",
        f"{username}, Hey, you! Your afternoon adventure awaits.",
        f"{username}, Good afternoon! Keep smiling; it's contagious.",
        f"{username}, Take a break, breathe, and enjoy the serenity of the afternoon.",
        f"{username}, Hello, achiever! Afternoons are for accomplishing goals.",
        f"{username}, Good afternoon! Stay positive, and the world will smile with you.",
        f"{username}, Embrace the opportunities that the afternoon brings your way.",
        f"{username}, Hey, superstar! Make every moment count this afternoon.",
        f"{username}, Good afternoon! Continue to be awesome in everything you do.",
        f"{username}, Find joy in the simple moments of this lovely afternoon.",
        f"{username}, Hello, trailblazer! Lead the way this afternoon.",
        f"{username}, Good afternoon! Keep the faith; your goals are within reach.",
        f"{username}, Afternoons are for making progress and taking action.",
        f"{username}, Hey, warrior! Keep fighting for your dreams this afternoon.",
        f"{username}, Good afternoon! The world is full of possibilities; explore them.",
        f"{username}, Take a moment to appreciate the beauty of this sunny afternoon.",
        f"{username}, Hello, motivator! Inspire and be inspired this afternoon.",
        f"{username}, Good afternoon! Keep your energy high and your goals higher.",
        f"{username}, Afternoons are perfect for small wins and big smiles.",
        f"{username}, Hey, adventurer! Explore new horizons this afternoon.",
        f"{username}, Good afternoon! Stay determined, and success will follow.",
        f"{username}, Keep your spirits high and your dreams alive this afternoon.",
        f"{username}, Hello, go-getter! You're making great strides; keep it up.",
      ],
      "evening":[
        f"{username}, Good Evening, how was today, pretty tired huh...?`"
        f"{username}, Good evening! Wishing you a relaxing and peaceful night ahead."
        ,f"{username}, Hello, night owl! May your evening be filled with joy and serenity."
        ,f"{username}, Evenings are for unwinding and reflecting on the day's blessings."
        ,f"{username}, Good evening! Take a moment to appreciate the beauty of twilight."
        ,f"{username}, Time to wind down and recharge for a wonderful evening."
        ,f"{username}, Hello, tranquility! Let the evening bring you inner peace."
        ,f"{username}, Good evening! Your presence brightens up the night."
        ,f"{username}, Evenings are perfect for spending quality time with loved ones."
        ,f"{username}, Hey, you! Make the most of this beautiful evening."
        ,f"{username}, Good evening! Relax, and let go of the day's stresses."
        ,f"{username}, Take a deep breath; it's the evening! Enjoy the calm."
        ,f"{username}, Hello, starlight! Make your evening shine with positivity."
        ,f"{username}, Good evening! Make memories that warm your heart."
        ,f"{username}, Embrace the peace and quiet of this lovely evening."
        ,f"{username}, Evenings are for gratitude; count your blessings."
        ,f"{username}, Hello, dreamer! Chase your dreams under the evening sky."
        ,f"{username}, Good evening! May your night be filled with sweet dreams."
        ,f"{username}, Keep the positivity flowing throughout this beautiful evening."
        ,f"{username}, Hey, adventurer! Explore the night with an open heart."
        ,f"{username}, Good evening! Let the night inspire your creativity."
        ,f"{username}, Reflect on your accomplishments and look forward to the night."
        ,f"{username}, Hello, magic hour! Make the most of this enchanting evening."
        ,f"{username}, Good evening! Your presence makes every moment special."
        ,f"{username}, Spend the evening doing what makes your soul happy."
        ,f"{username}, Evenings are for stargazing and dreaming big dreams."
        ,f"{username}, Hello, serenity! Let the evening calm your spirit."
        ,f"{username}, Good evening! Find joy in the little things tonight."
        ,f"{username}, Enjoy the company of loved ones and friends this evening."
        ,f"{username}, Hey, night sky watcher! Discover the wonders of the universe."
        ,f"{username}, Good evening! Let positivity guide you through the night."
        ,f"{username}, Take a moment to relax and appreciate the beauty of evening."
        ,f"{username}, Hello, storyteller! Share laughter and stories this evening."
        ,f"{username}, Good evening! May your night be filled with peace and contentment."
        ,f"{username}, End your day with a smile and a heart full of gratitude."
        ,f"{username}, Evenings are for making memories and cherishing moments."
        ,f"{username}, Hello, night adventurer! Explore the unknown with courage."
        ,f"{username}, Good evening! Your kindness shines even in the dark."
        ,f"{username}, Spend the evening surrounded by love and laughter."
        ,f"{username}, Embrace the night's calm and let it soothe your soul."
        ,f"{username}, Hello, night thinker! Let your dreams take flight tonight."
        ,f"{username}, Good evening! Stay positive; the night holds endless possibilities."
        ,f"{username}, Reflect on the beauty of life during this tranquil evening."
        ,f"{username}, Evenings are for finding inspiration in the quiet moments."
        ,f"{username}, Hey, night explorer! Seek the magic hidden in the night."
        ,f"{username}, Good evening! The night is yours; make it extraordinary."
        ,f"{username}, Wind down and relax, it's the perfect evening for it."
        ,f"{username}, Hello, peace seeker! Let the evening bring you tranquility."
        ,f"{username}, Good evening! May your night be filled with laughter and love."
        ,f"{username}, End the day on a positive note and prepare for a restful night."
        ,f"{username}, Embrace the serenity of the night and let it rejuvenate your spirit."
      ],
      "night":[
        f"{username}, Good Night, have a relaxed eye shut!",
        f"{username}, Good night! May your dreams be as sweet as your slumber.",
        f"{username}, Hello, night owl! It's time to rest and recharge.",
        f"{username}, Nights are for finding comfort in the embrace of sleep.",
        f"{username}, Good night! May your sleep be deep and your dreams be beautiful.",
        f"{username}, Wishing you a peaceful night filled with restful sleep.",
        f"{username}, Hello, tranquility! Let the night bring you inner peace.",
        f"{username}, Good night! Close your eyes and let go of the day's worries.",
        f"{username}, The night sky is a canvas of dreams; sleep under its beauty.",
        f"{username}, Hey, you! Drift into a world of dreams and imagination.",
        f"{username}, Good night! Let the stars above guide you to dreamland.",
        f"{username}, Find solace in the stillness of the night; it's time to relax.",
        f"{username}, Hello, starlight! May your night be filled with magic.",
        f"{username}, Good night! Sleep well and wake up refreshed and renewed.",
        f"{username}, Embrace the quiet of the night and find serenity within.",
        f"{username}, Let the night be a gentle lullaby that soothes your soul.",
        f"{username}, Hello, dreamer! Your night holds the key to new adventures.",
        f"{username}, Good night! May your dreams be filled with happiness and hope.",
        f"{username}, The night is a canvas of rest; paint it with peaceful sleep.",
        f"{username}, Hey, adventurer! Explore the dream world with an open heart.",
        f"{username}, Good night! May your mind find rest and your heart find calm.",
        f"{username}, Dive into the world of dreams and let your imagination soar.",
        f"{username}, Hello, magic hour! Let the night's beauty captivate your senses.",
        f"{username}, Good night! Find comfort in the quietude of the night.",
        f"{username}, Let go of the day's troubles and welcome a tranquil night.",
        f"{username}, In the night's embrace, find comfort and renewal.",
        f"{username}, Hello, serenity! Let the night's peace wash over you.",
        f"{username}, Good night! May your sleep be as deep as the ocean.",
        f"{username}, The night sky is a masterpiece; gaze upon its wonders.",
        f"{username}, Hey, stargazer! The night holds the secrets of the universe.",
        f"{username}, Good night! Surrender to sleep and let your worries fade.",
        f"{username}, Find joy in the stillness of the night; it's time to rest.",
        f"{username}, Hello, storyteller! Let your dreams weave tales of adventure.",
        f"{username}, Good night! Embrace the darkness and the promise of dawn.",
        f"{username}, The night is a sanctuary of rest; seek solace within.",
        f"{username}, As the night unfolds, may your dreams take flight.",
        f"{username}, Hello, night thinker! Your dreams hold the key to tomorrow.",
        f"{username}, Good night! May your dreams be a tapestry of wonder.",
        f"{username}, Let the night's calm wash away the cares of the day.",
        f"{username}, Hey, night traveler! Explore new horizons in your dreams.",
        f"{username}, Good night! Surrender to sleep and find peace within.",
        f"{username}, In the night's silence, find renewal and tranquility.",
        f"{username}, Hello, peace seeker! Let the night bring you serenity.",
        f"{username}, Good night! May your sleep be as deep as the ocean's depths.",
        f"{username}, As you rest, may your dreams be filled with inspiration.",
        f"{username}, Embrace the night's serenity and let it embrace you in return.",
        f"{username}, Hello, dream catcher! Your night holds the hopes of tomorrow.",
        f"{username}, Good night! Let the stars above be your guiding light.",
        f"{username}, In the night's stillness, find solace and rejuvenation.",
        f"{username}, Hey, night wanderer! Explore the world of dreams with wonder.",
        f"{username}, Good night! May your sleep be a journey to new horizons."
      ]}
    hour = current_time.hour
    
    if hour >= 0 and hour<=12:
        message = messages["morning"][randint(1,50)]
    elif hour >=12 and hour<=3:
        message = messages["afternoon"][randint(1,50)]
    elif hour >=15 and hour <= 20:
        message = messages["evening"][randint(1,50)]
    elif hour >= 20 and hour <=24:
        message = messages["night"][randint(1,50)]
    return message

def hireme(request):
    form = Email_form()
    if request.method == 'POST':
        form = Email_form(request.POST)
        username = request.POST.get("username", False)
        email = request.POST.get("email", False)
        # user = User.objects.create_user(
        #     username = username,
        #     password = password,
        #     email = email
        # )
        # login(request, user)

        subject = f"Hello, {username}, it's me Karthik J!"
        message = f"\nI am reverting to you since i have received your intimation through my portfolio website. And I whole heartedly am grateful to you for considering me as a worhty candidate for your esteemed organisation. We shall with your due permission continue the conversation through this medium henceforth.\nThanking you"
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [email,]
        # send_mail(subject, message, email_from, recipent_list)

        msg = EmailMessage(subject, message, email_from, recipent_list)
        msg.content_subtype = "html"  
        msg.attach_file('static/Resume_KarthikJ.pdf')
        msg.send()

        return redirect("web_app:index")
    
    return render(request, "hireme.html", {"form":form})







