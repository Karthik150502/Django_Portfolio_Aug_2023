const readline = require('readline');
const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const time = new Date()

// const time_diff = 330 
// const timehour = Math.floor(time_diff/60)
// const timemins = time_diff%60 
// const timrightnow = time.getTime()


const hours = time.getHours() 
const minutes = time.getMinutes() 
const seconds = time.getSeconds()




function greetings(theName){
    let text_element = document.getElementById("greeting")
    const messages = {
      morning:[
        `${theName}, Good Morning! Start your day with a smile on your face..!`,
        `${theName}, Good morning! Wishing you a day filled with positivity and joy.`,
        `${theName}, Rise and shine! Today is a brand new opportunity to make the most of.`,
        `${theName}, Hello world! It's a beautiful morning to start afresh.`,
        `${theName}, Good morning! May your day be as bright as the sun.`,
        `${theName}, Wake up and smile! It's the start of another wonderful day.`,
        `${theName}, Good morning! Let your actions today reflect your goals and aspirations.`,
        `${theName}, Rise and grind! Success comes to those who work for it.`,
        `${theName}, Hello, early bird! Embrace the day with enthusiasm.`,
        `${theName}, Good morning! Start your day with a grateful heart.`,
        `${theName}, Seize the day! Your potential is limitless.`,
        `${theName}, Rise and shine, it's coffee time!`,
        `${theName}, Good morning! Make today amazing.`,
        `${theName}, Wake up with determination, go to bed with satisfaction.`,
        `${theName}, Embrace the morning breeze and let it invigorate your spirit.`,
        `${theName}, Good morning! Each day is a new chance to be better than yesterday.`,
        `${theName}, Rise and conquer! Today is yours for the taking.`,
        `${theName}, Hello sunshine! You have the power to brighten the world.`,
        `${theName}, Good morning! Remember, you are capable of achieving greatness.`,
        `${theName}, Start your day with a smile and positive thoughts.`,
        `${theName}, Rise and shine! Life is full of possibilities waiting for you.`,
        `${theName}, Good morning! Chase your dreams with unwavering determination.`,
        `${theName}, Make today count! Your journey to success begins now.`,
        `${theName}, Wake up, it's a new day filled with opportunities and adventures.`,
        `${theName}, Good morning! Embrace the challenges, they lead to growth.`,
        `${theName}, Rise and sparkle! Your light can illuminate the darkest of days.`,
        `${theName}, Hello, world changer! Make a positive impact today.`,
        `${theName}, Good morning! Your potential knows no bounds.`,
        `${theName}, Start your day with a grateful heart and a positive mindset.`,
        `${theName}, Rise and thrive! Success is the result of persistent effort.`,
        `${theName}, Every morning is a fresh start, a chance to rewrite your story.`,
        `${theName}, Good morning! Seize the day with both hands and make it yours.`,
        `${theName}, Embrace the morning calm and let it bring you inner peace.`,
        `${theName}, Rise and shine! Your journey to success begins with a single step.`,
        `${theName}, Hello, dreamer! Your goals are within reach.`,
        `${theName}, Good morning! Believe in yourself, and you'll achieve greatness.`,
        `${theName}, Wake up, it's a brand new day to create wonderful memories.`,
        `${theName}, Start your day with gratitude, and watch your blessings multiply.`,
        `${theName}, Rise and conquer! Challenges are stepping stones to success.`,
        `${theName}, Embrace the morning with open arms and a positive attitude.`,
        `${theName}, Good morning! Your potential is limitless; don't underestimate it.`,
        `${theName}, Rise and shine! Today is a gift; make the most of it.`,
        `${theName}, Hello, world changer! You have the power to make a difference.`,
        `${theName}, Good morning! Make each moment count on your journey.`,
        `${theName}, Wake up, it's a new day filled with endless possibilities.`,
        `${theName}, Start your day with a smile, and positivity will follow.`,
        `${theName}, Rise and sparkle! Let your enthusiasm light up the day.`,
        `${theName}, Embrace the morning tranquility and find your inner strength.`,
        `${theName}, Good morning! Chase your dreams with unwavering determination.`,
        `${theName}, Rise and thrive! Success is the result of relentless effort.`,
        `${theName}, Hello, champion! Today is another opportunity to excel.`
      ],
      afternoon:[
        `${theName}, Good Afternoon, How are you doing, had your lunch...?`,
        `${theName}, Good afternoon! I hope you're having a fantastic day so far.`,
        `${theName}, Hello there! Wishing you a peaceful and productive afternoon.`,
        `${theName}, Afternoons are for refueling. Enjoy your break!`,
        `${theName}, Good afternoon! May your day continue to be filled with positivity.`,
        `${theName}, Time for a quick recharge! Have a great afternoon.`,
        `${theName}, Hello, busy bee! Keep up the good work this afternoon.`,
        `${theName}, Good afternoon! Take a moment to relax and refresh.`,
        `${theName}, Afternoons are a second chance to make your day even better.`,
        `${theName}, Hey, you! Hope your afternoon is as bright as your morning.`,
        `${theName}, Good afternoon! Keep those good vibes rolling.`,
        `${theName}, Take a deep breath, it's the afternoon! You've got this.`,
        `${theName}, Hello, sunshine! The afternoon is your canvas; paint it bright.`,
        `${theName}, Good afternoon! Stay focused and make every moment count.`,
        `${theName}, Don't forget to pause and enjoy the beauty of this afternoon.`,
        `${theName}, Afternoons are perfect for catching up and connecting.`,
        `${theName}, Hello, superstar! Continue to shine this afternoon.`,
        `${theName}, Good afternoon! Your hard work is paying off.`,
        `${theName}, Keep the momentum going! It's a productive afternoon ahead.`,
        `${theName}, Hey, champ! Conquer the afternoon with confidence.`,
        `${theName}, Good afternoon! Let's make the rest of the day amazing.`,
        `${theName}, Recharge your energy for the afternoon journey ahead.`,
        `${theName}, Hello, go-getter! Your determination shines this afternoon.`,
        `${theName}, Good afternoon! Stay positive, and the day will be a breeze.`,
        `${theName}, Take a moment to appreciate the beauty of this afternoon.`,
        `${theName}, Afternoons are for taking small steps toward big goals.`,
        `${theName}, Hello, dreamer! Keep chasing your dreams this afternoon.`,
        `${theName}, Good afternoon! May your day be as bright as the sun.`,
        `${theName}, Stay motivated and conquer the challenges of the afternoon.`,
        `${theName}, Hey, you! Your afternoon adventure awaits.`,
        `${theName}, Good afternoon! Keep smiling; it's contagious.`,
        `${theName}, Take a break, breathe, and enjoy the serenity of the afternoon.`,
        `${theName}, Hello, achiever! Afternoons are for accomplishing goals.`,
        `${theName}, Good afternoon! Stay positive, and the world will smile with you.`,
        `${theName}, Embrace the opportunities that the afternoon brings your way.`,
        `${theName}, Hey, superstar! Make every moment count this afternoon.`,
        `${theName}, Good afternoon! Continue to be awesome in everything you do.`,
        `${theName}, Find joy in the simple moments of this lovely afternoon.`,
        `${theName}, Hello, trailblazer! Lead the way this afternoon.`,
        `${theName}, Good afternoon! Keep the faith; your goals are within reach.`,
        `${theName}, Afternoons are for making progress and taking action.`,
        `${theName}, Hey, warrior! Keep fighting for your dreams this afternoon.`,
        `${theName}, Good afternoon! The world is full of possibilities; explore them.`,
        `${theName}, Take a moment to appreciate the beauty of this sunny afternoon.`,
        `${theName}, Hello, motivator! Inspire and be inspired this afternoon.`,
        `${theName}, Good afternoon! Keep your energy high and your goals higher.`,
        `${theName}, Afternoons are perfect for small wins and big smiles.`,
        `${theName}, Hey, adventurer! Explore new horizons this afternoon.`,
        `${theName}, Good afternoon! Stay determined, and success will follow.`,
        `${theName}, Keep your spirits high and your dreams alive this afternoon.`,
        `${theName}, Hello, go-getter! You're making great strides; keep it up.`,
      ],
      evening:[
        `${theName}, Good Evening, how was today, pretty tired huh...?`,
        `${theName}, Good evening! Wishing you a relaxing and peaceful night ahead.`
        ,`${theName}, Hello, night owl! May your evening be filled with joy and serenity.`
        ,`${theName}, Evenings are for unwinding and reflecting on the day's blessings.`
        ,`${theName}, Good evening! Take a moment to appreciate the beauty of twilight.`
        ,`${theName}, Time to wind down and recharge for a wonderful evening.`
        ,`${theName}, Hello, tranquility! Let the evening bring you inner peace.`
        ,`${theName}, Good evening! Your presence brightens up the night.`
        ,`${theName}, Evenings are perfect for spending quality time with loved ones.`
        ,`${theName}, Hey, you! Make the most of this beautiful evening.`
        ,`${theName}, Good evening! Relax, and let go of the day's stresses.`
        ,`${theName}, Take a deep breath; it's the evening! Enjoy the calm.`
        ,`${theName}, Hello, starlight! Make your evening shine with positivity.`
        ,`${theName}, Good evening! Make memories that warm your heart.`
        ,`${theName}, Embrace the peace and quiet of this lovely evening.`
        ,`${theName}, Evenings are for gratitude; count your blessings.`
        ,`${theName}, Hello, dreamer! Chase your dreams under the evening sky.`
        ,`${theName}, Good evening! May your night be filled with sweet dreams.`
        ,`${theName}, Keep the positivity flowing throughout this beautiful evening.`
        ,`${theName}, Hey, adventurer! Explore the night with an open heart.`
        ,`${theName}, Good evening! Let the night inspire your creativity.`
        ,`${theName}, Reflect on your accomplishments and look forward to the night.`
        ,`${theName}, Hello, magic hour! Make the most of this enchanting evening.`
        ,`${theName}, Good evening! Your presence makes every moment special.`
        ,`${theName}, Spend the evening doing what makes your soul happy.`
        ,`${theName}, Evenings are for stargazing and dreaming big dreams.`
        ,`${theName}, Hello, serenity! Let the evening calm your spirit.`
        ,`${theName}, Good evening! Find joy in the little things tonight.`
        ,`${theName}, Enjoy the company of loved ones and friends this evening.`
        ,`${theName}, Hey, night sky watcher! Discover the wonders of the universe.`
        ,`${theName}, Good evening! Let positivity guide you through the night.`
        ,`${theName}, Take a moment to relax and appreciate the beauty of evening.`
        ,`${theName}, Hello, storyteller! Share laughter and stories this evening.`
        ,`${theName}, Good evening! May your night be filled with peace and contentment.`
        ,`${theName}, End your day with a smile and a heart full of gratitude.`
        ,`${theName}, Evenings are for making memories and cherishing moments.`
        ,`${theName}, Hello, night adventurer! Explore the unknown with courage.`
        ,`${theName}, Good evening! Your kindness shines even in the dark.`
        ,`${theName}, Spend the evening surrounded by love and laughter.`
        ,`${theName}, Embrace the night's calm and let it soothe your soul.`
        ,`${theName}, Hello, night thinker! Let your dreams take flight tonight.`
        ,`${theName}, Good evening! Stay positive; the night holds endless possibilities.`
        ,`${theName}, Reflect on the beauty of life during this tranquil evening.`
        ,`${theName}, Evenings are for finding inspiration in the quiet moments.`
        ,`${theName}, Hey, night explorer! Seek the magic hidden in the night.`
        ,`${theName}, Good evening! The night is yours; make it extraordinary.`
        ,`${theName}, Wind down and relax, it's the perfect evening for it.`
        ,`${theName}, Hello, peace seeker! Let the evening bring you tranquility.`
        ,`${theName}, Good evening! May your night be filled with laughter and love.`
        ,`${theName}, End the day on a positive note and prepare for a restful night.`
        ,`${theName}, Embrace the serenity of the night and let it rejuvenate your spirit.`
      ],
      night:[
        `${theName}, Good Night, have a relaxed eye shut!`,
        `${theName}, Good night! May your dreams be as sweet as your slumber.`,
        `${theName}, Hello, night owl! It's time to rest and recharge.`,
        `${theName}, Nights are for finding comfort in the embrace of sleep.`,
        `${theName}, Good night! May your sleep be deep and your dreams be beautiful.`,
        `${theName}, Wishing you a peaceful night filled with restful sleep.`,
        `${theName}, Hello, tranquility! Let the night bring you inner peace.`,
        `${theName}, Good night! Close your eyes and let go of the day's worries.`,
        `${theName}, The night sky is a canvas of dreams; sleep under its beauty.`,
        `${theName}, Hey, you! Drift into a world of dreams and imagination.`,
        `${theName}, Good night! Let the stars above guide you to dreamland.`,
        `${theName}, Find solace in the stillness of the night; it's time to relax.`,
        `${theName}, Hello, starlight! May your night be filled with magic.`,
        `${theName}, Good night! Sleep well and wake up refreshed and renewed.`,
        `${theName}, Embrace the quiet of the night and find serenity within.`,
        `${theName}, Let the night be a gentle lullaby that soothes your soul.`,
        `${theName}, Hello, dreamer! Your night holds the key to new adventures.`,
        `${theName}, Good night! May your dreams be filled with happiness and hope.`,
        `${theName}, The night is a canvas of rest; paint it with peaceful sleep.`,
        `${theName}, Hey, adventurer! Explore the dream world with an open heart.`,
        `${theName}, Good night! May your mind find rest and your heart find calm.`,
        `${theName}, Dive into the world of dreams and let your imagination soar.`,
        `${theName}, Hello, magic hour! Let the night's beauty captivate your senses.`,
        `${theName}, Good night! Find comfort in the quietude of the night.`,
        `${theName}, Let go of the day's troubles and welcome a tranquil night.`,
        `${theName}, In the night's embrace, find comfort and renewal.`,
        `${theName}, Hello, serenity! Let the night's peace wash over you.`,
        `${theName}, Good night! May your sleep be as deep as the ocean.`,
        `${theName}, The night sky is a masterpiece; gaze upon its wonders.`,
        `${theName}, Hey, stargazer! The night holds the secrets of the universe.`,
        `${theName}, Good night! Surrender to sleep and let your worries fade.`,
        `${theName}, Find joy in the stillness of the night; it's time to rest.`,
        `${theName}, Hello, storyteller! Let your dreams weave tales of adventure.`,
        `${theName}, Good night! Embrace the darkness and the promise of dawn.`,
        `${theName}, The night is a sanctuary of rest; seek solace within.`,
        `${theName}, As the night unfolds, may your dreams take flight.`,
        `${theName}, Hello, night thinker! Your dreams hold the key to tomorrow.`,
        `${theName}, Good night! May your dreams be a tapestry of wonder.`,
        `${theName}, Let the night's calm wash away the cares of the day.`,
        `${theName}, Hey, night traveler! Explore new horizons in your dreams.`,
        `${theName}, Good night! Surrender to sleep and find peace within.`,
        `${theName}, In the night's silence, find renewal and tranquility.`,
        `${theName}, Hello, peace seeker! Let the night bring you serenity.`,
        `${theName}, Good night! May your sleep be as deep as the ocean's depths.`,
        `${theName}, As you rest, may your dreams be filled with inspiration.`,
        `${theName}, Embrace the night's serenity and let it embrace you in return.`,
        `${theName}, Hello, dream catcher! Your night holds the hopes of tomorrow.`,
        `${theName}, Good night! Let the stars above be your guiding light.`,
        `${theName}, In the night's stillness, find solace and rejuvenation.`,
        `${theName}, Hey, night wanderer! Explore the world of dreams with wonder.`,
        `${theName}, Good night! May your sleep be a journey to new horizons.`
      ]}
    
    // console.log(`Hello, {}`)
    post_meridium = (hours>12)?true:false

    if(!post_meridium){
      if (hours >= 6 && hours <= 12){
        res = messages.morning[Math.floor((Math.random() * 50) + 0)]
      }
    }
    else{
      if (hours >= 12 && hours <= 3){
        res = messages.afternoon[Math.floor((Math.random() * 50) + 0)]
      }
      else if(hours >= 3 && hours <= 8){
        res = messages.evening[Math.floor((Math.random() * 50) + 0)]
      }
      else{
        res = messages.night[Math.floor((Math.random() * 50) + 0)]
      } 
    }
    text_element.textContent = res   
}

// document.body.addEventListener("load", greetings)

