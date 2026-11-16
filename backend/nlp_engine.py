
import re
from difflib import get_close_matches


class KnowledgeEngine:

    def __init__(self):
        self.knowledge = self.load_knowledge()
        self.questions = self.generate_questions()

        print("\n❤️ SANDHU AI BOT - KNOWLEDGE ENGINE READY")
        print(f"Topics loaded: {len(self.knowledge)}")
        print(f"Question patterns loaded: {len(self.questions)}")
        print("Language: English")
        print("Answer format: Paragraph + 3 Points + Example\n")

    def load_knowledge(self):

        return {




"Self Introduction": {
    "aliases": [
        "self introduction",
        "introduce yourself",
        "about yourself",
        "tell me about yourself",
        "my introduction"
    ],
    "intro": "Self-introduction is a way of presenting your identity, education, skills, interests, and career goals. It helps people understand your background and creates a positive first impression in interviews, meetings, and professional situations.",
    "points": [
        "Start with your name and educational background.",
        "Mention your technical skills, interests, and achievements.",
        "Explain your career goals and future ambitions."
    ],
    "example": "Hello, I am Anmol Singh Sandhu. I am a BCA student interested in Python, Data Analytics, and software development."
},

"Introduce Yourself in an Interview": {
    "aliases": [
        "introduce yourself in interview",
        "self introduction for interview",
        "interview introduction",
        "how to introduce yourself in interview"
    ],
    "intro": "A professional interview introduction is a short explanation of your education, skills, projects, and career interests. It helps the interviewer understand your background and suitability for the job.",
    "points": [
        "Begin with your name and qualification.",
        "Highlight relevant skills, projects, and experience.",
        "End with your career interests and willingness to learn."
    ],
    "example": "Hello, I am Anmol Singh Sandhu, pursuing BCA. I have learned Python and developed practical projects. I am interested in starting my career in the technology industry."
},

"Educational Background": {
    "aliases": [
        "educational background",
        "tell me about your education",
        "your education",
        "academic background"
    ],
    "intro": "Educational background describes your academic qualifications, institutions, subjects, and learning journey. It helps interviewers understand your knowledge and the foundation you have developed for your professional career.",
    "points": [
        "Mention your current degree and institution.",
        "Highlight relevant subjects and certifications.",
        "Connect your education with your career goals."
    ],
    "example": "I am pursuing a Bachelor of Computer Applications and learning programming, databases, and data analytics."
},

"Personal Strengths": {
    "aliases": [
        "what are your strengths",
        "your strengths",
        "tell me your strengths",
        "personal strengths"
    ],
    "intro": "Personal strengths are positive qualities and abilities that help you perform tasks effectively. Identifying your strengths allows you to explain your value and demonstrate confidence during interviews and professional interactions.",
    "points": [
        "Identify your strongest abilities.",
        "Explain how they help you complete tasks.",
        "Support your answer with a practical example."
    ],
    "example": "My strengths are problem-solving, continuous learning, and completing tasks with responsibility."
},

"Personal Weaknesses": {
    "aliases": [
        "what are your weaknesses",
        "your weaknesses",
        "tell me your weaknesses",
        "personal weaknesses"
    ],
    "intro": "Weaknesses are areas where you need improvement in your personal or professional development. A good interview answer shows honesty, self-awareness, and a genuine effort to improve those areas.",
    "points": [
        "Choose a genuine weakness.",
        "Explain the steps you are taking to improve.",
        "Show a positive attitude towards learning."
    ],
    "example": "Sometimes I spend extra time checking my work, but I am improving my time management skills."
},

"Career Goals": {
    "aliases": [
        "what are your career goals",
        "your career goals",
        "future goals",
        "what is your future plan"
    ],
    "intro": "Career goals are the professional achievements you want to accomplish in the future. They provide direction to your learning, skill development, and career decisions.",
    "points": [
        "Set clear short-term and long-term goals.",
        "Develop skills relevant to your career.",
        "Track your progress through practical experience."
    ],
    "example": "My goal is to become a skilled Data Analyst by learning Python, SQL, Excel, and Power BI."
},

"Why Should We Hire You": {
    "aliases": [
        "why should we hire you",
        "why we should hire you",
        "hire me",
        "why are you suitable for this job"
    ],
    "intro": "This interview question helps employers understand your skills, attitude, and suitability for a position. Your response should explain how your abilities and willingness to learn can contribute to the organization.",
    "points": [
        "Highlight skills relevant to the job.",
        "Mention practical projects or experience.",
        "Demonstrate confidence and willingness to learn."
    ],
    "example": "You should hire me because I have technical knowledge, practical project experience, and a strong interest in learning new technologies."
},

"Describe Yourself": {
    "aliases": [
        "describe yourself",
        "how would you describe yourself",
        "tell me about your personality",
        "describe your personality"
    ],
    "intro": "Describing yourself means explaining your personality, working style, interests, and important qualities. A good description is honest, clear, and supported by examples from your daily life.",
    "points": [
        "Choose three genuine personality qualities.",
        "Mention your learning and working habits.",
        "Explain how these qualities help you."
    ],
    "example": "I would describe myself as hardworking, curious, and a quick learner who enjoys solving problems."
},

"Hobbies and Interests": {
    "aliases": [
        "what are your hobbies",
        "your hobbies",
        "tell me about your interests",
        "hobbies and interests"
    ],
    "intro": "Hobbies and interests are activities you enjoy outside your regular responsibilities. They can reveal your personality, creativity, curiosity, and willingness to learn new things.",
    "points": [
        "Mention hobbies you genuinely enjoy.",
        "Explain what you learn from them.",
        "Connect relevant interests with personal development."
    ],
    "example": "My hobbies include learning new technologies, exploring programming, and improving my technical knowledge."
},

"Why Do You Want This Job": {
    "aliases": [
        "why do you want this job",
        "why do you want to work here",
        "why are you interested in this job",
        "why do you want to join our company"
    ],
    "intro": "Employers ask this question to understand your motivation and interest in their organization. A strong answer connects your career goals, skills, and interests with the responsibilities of the position.",
    "points": [
        "Explain your interest in the position.",
        "Connect your skills with the job requirements.",
        "Show enthusiasm for learning and contributing."
    ],
    "example": "I want this job because it matches my technical interests and provides an opportunity to develop my professional skills."
},



"General Conversation": {
    "aliases": [
        "general conversation",
        "daily conversation",
        "normal conversation",
        "casual conversation",
        "everyday conversation",
        "how to start a conversation",
        "what to say when meeting someone",
        "conversation with someone",
        "talking to people",
        "social conversation"
    ],
    "intro": "General conversation helps people communicate, build relationships, and exchange information in everyday situations. Being polite, friendly, and respectful makes conversations comfortable and enjoyable.",
    "points": [
        "Start conversations with friendly greetings.",
        "Ask simple questions and listen carefully.",
        "Respond politely and maintain a positive attitude."
    ],
    "example": "Hello! How are you? My name is Anmol. Nice to meet you."
},

"Greeting Someone": {
    "aliases": [
        "greeting someone",
        "how to greet someone",
        "how to say hello",
        "how to welcome someone",
        "what should i say when i meet someone",
        "how to greet a person",
        "formal greetings",
        "informal greetings",
        "greetings in english",
        "ways to greet people"
    ],
    "intro": "Greetings are expressions used to welcome someone or begin a conversation. The right greeting depends on the time, situation, and relationship between people. A friendly greeting creates a positive first impression.",
    "points": [
        "Use Hello or Hi in casual situations.",
        "Use Good morning or Good evening when appropriate.",
        "Speak politely and confidently."
    ],
    "example": "Good morning! How are you doing today?"
},

"Asking How Someone Is": {
    "aliases": [
        "how are you",
        "how are you doing",
        "how is everything",
        "how have you been",
        "how is life",
        "are you doing well",
        "how are things going",
        "how is your health",
        "how is everything going",
        "hope you are doing well"
    ],
    "intro": "Asking someone how they are is a common way to show care and interest. It helps begin friendly conversations and gives the other person an opportunity to share how they feel.",
    "points": [
        "Ask How are you? politely.",
        "Listen carefully to the person's response.",
        "Reply naturally and ask about their day."
    ],
    "example": "How are you doing today? I hope everything is going well."
},

"Asking Someone's Name": {
    "aliases": [
        "what is your name",
        "may i know your name",
        "could you tell me your name",
        "what should i call you",
        "can i know your name",
        "ask someone name",
        "how to ask your name",
        "tell me your name",
        "what is your good name",
        "may i ask your name"
    ],
    "intro": "Asking someone's name is a simple way to introduce yourself and become familiar with a new person. Using polite language makes the interaction more comfortable and respectful.",
    "points": [
        "Ask politely and confidently.",
        "Listen carefully to the person's name.",
        "Use their name naturally during the conversation."
    ],
    "example": "Hi! My name is Anmol. May I know your name?"
},

"Asking Where Someone Is From": {
    "aliases": [
        "where are you from",
        "where do you come from",
        "which city are you from",
        "what is your hometown",
        "where is your hometown",
        "which state are you from",
        "are you from this city",
        "where do you live",
        "which place do you belong to",
        "tell me about your hometown"
    ],
    "intro": "Asking where someone is from helps people learn about each other's hometowns, cities, and backgrounds. It is a common topic during introductions and casual conversations.",
    "points": [
        "Ask the question in a friendly way.",
        "Share your own hometown too.",
        "Show interest in the person's answer."
    ],
    "example": "Where are you from? I am from Bhilai, Chhattisgarh."
},

"Asking About Work or Studies": {
    "aliases": [
        "what do you do",
        "what are you studying",
        "where do you work",
        "what do you study",
        "are you a student",
        "which course are you doing",
        "what is your profession",
        "what is your occupation",
        "what are you working on",
        "tell me about your work"
    ],
    "intro": "Asking about someone's work or studies helps you understand their professional or educational background. It is a useful conversation topic when meeting new people and building connections.",
    "points": [
        "Ask whether they study or work.",
        "Show interest in their field.",
        "Share your own educational or professional background."
    ],
    "example": "What do you do? I am currently studying Bachelor of Computer Applications."
},

"Talking About the Weather": {
    "aliases": [
        "how is the weather",
        "weather conversation",
        "talk about weather",
        "is it raining",
        "is it hot today",
        "is it cold today",
        "how is the weather today",
        "beautiful weather",
        "weather is nice",
        "what do you think about the weather"
    ],
    "intro": "Weather is an easy and common topic for starting casual conversations. People often discuss temperature, rain, sunshine, and seasonal changes to connect with others.",
    "points": [
        "Mention the current weather.",
        "Ask whether the person likes the weather.",
        "Keep the conversation natural and friendly."
    ],
    "example": "The weather is really pleasant today. Do you enjoy this kind of weather?"
},

"Offering Help": {
    "aliases": [
        "can i help you",
        "do you need any help",
        "offer help",
        "how can i help you",
        "would you like some help",
        "need any assistance",
        "can i do something for you",
        "may i assist you",
        "do you need my help",
        "is there anything i can help with"
    ],
    "intro": "Offering help is a polite way to show kindness and support. It makes communication more positive and helps people feel comfortable asking for assistance when they need it.",
    "points": [
        "Ask politely if someone needs help.",
        "Listen carefully to what they need.",
        "Offer practical assistance when possible."
    ],
    "example": "You look busy. Can I help you with anything?"
},

"Thanking Someone": {
    "aliases": [
        "how to say thank you",
        "thank someone",
        "express gratitude",
        "thank you conversation",
        "how to thank someone",
        "how to show appreciation",
        "ways to say thanks",
        "thank you for helping me",
        "how to appreciate someone",
        "what to say when someone helps you"
    ],
    "intro": "Thanking someone is a way to express appreciation for their help, kindness, or time. It builds positive relationships and shows respect in personal and professional conversations.",
    "points": [
        "Say Thank you for help or support.",
        "Use I really appreciate it to express gratitude.",
        "Respond warmly when someone thanks you."
    ],
    "example": "Thank you so much for helping me. I really appreciate it."
},

"Apologizing": {
    "aliases": [
        "how to apologize",
        "say sorry",
        "apologize to someone",
        "how to say sorry",
        "how to ask for forgiveness",
        "i am sorry",
        "how to apologize politely",
        "sorry for my mistake",
        "how to say sorry professionally",
        "ways to apologize"
    ],
    "intro": "Apologizing means accepting responsibility and expressing regret when your actions cause inconvenience or hurt. A sincere apology can help maintain trust and improve relationships.",
    "points": [
        "Acknowledge what happened.",
        "Say sorry sincerely.",
        "Try to correct the mistake."
    ],
    "example": "I am really sorry for being late. It will not happen again."
},

"Ending a Conversation": {
    "aliases": [
        "how to end a conversation",
        "goodbye conversation",
        "leave a conversation",
        "how to say goodbye",
        "how to end talking politely",
        "ways to say goodbye",
        "how to leave politely",
        "what to say before leaving",
        "ending a meeting",
        "how to finish a conversation"
    ],
    "intro": "Ending a conversation politely shows respect for the other person's time. A friendly goodbye leaves a positive impression and keeps communication open for future interactions.",
    "points": [
        "Finish your conversation naturally.",
        "Thank the person for their time.",
        "Say goodbye politely."
    ],
    "example": "It was nice talking to you. See you again. Have a great day!"
},

"Making Friends": {
    "aliases": [
        "how to make friends",
        "making new friends",
        "become friends with someone",
        "how to start friendship",
        "how to talk to new people",
        "how to make new friends in college",
        "how to become friendly",
        "how to approach someone",
        "how to build friendships",
        "how to meet new people"
    ],
    "intro": "Making friends involves building trust, communicating openly, and showing genuine interest in other people. Friendly behavior and mutual respect help create meaningful and lasting relationships.",
    "points": [
        "Start with a friendly conversation.",
        "Find common interests and activities.",
        "Be supportive, honest, and respectful."
    ],
    "example": "Hi! I also enjoy playing cricket. Would you like to play together sometime?"
},

"Inviting Someone": {
    "aliases": [
        "how to invite someone",
        "invite someone for coffee",
        "ask someone to join",
        "invitation conversation",
        "would you like to come",
        "invite a friend",
        "how to invite someone politely",
        "ask someone to hang out",
        "invite someone to a party",
        "how to make plans with someone"
    ],
    "intro": "Inviting someone is a friendly way to spend time together or participate in an activity. A clear and polite invitation makes it easy for the other person to respond comfortably.",
    "points": [
        "Explain what you are inviting them to.",
        "Mention the time or place if known.",
        "Respect their decision."
    ],
    "example": "Would you like to join me for coffee this evening?"
},

"Complimenting Someone": {
    "aliases": [
        "how to compliment someone",
        "give a compliment",
        "compliment conversation",
        "how to appreciate someone",
        "nice words for someone",
        "praise someone",
        "how to give compliments",
        "compliment someone's work",
        "say something nice",
        "how to appreciate someone's effort"
    ],
    "intro": "A compliment is a positive statement that appreciates someone's appearance, work, behavior, or achievements. Genuine compliments can make conversations warmer and more encouraging.",
    "points": [
        "Keep your compliment genuine.",
        "Be respectful and appropriate.",
        "Appreciate effort as well as achievements."
    ],
    "example": "You explained that topic really well. Great job!"
},

"Small Talk": {
    "aliases": [
        "small talk",
        "what is small talk",
        "casual talking",
        "casual conversation",
        "how to make small talk",
        "everyday small talk",
        "how to talk casually",
        "conversation starters",
        "topics for small talk",
        "how to start chatting"
    ],
    "intro": "Small talk is a short, informal conversation about everyday topics. It helps people feel comfortable, especially when they do not know each other very well.",
    "points": [
        "Choose simple topics such as hobbies or weather.",
        "Ask open and friendly questions.",
        "Avoid overly personal topics at first."
    ],
    "example": "Have you watched any good movies recently?"
},

"Asking About the Day": {
    "aliases": [
        "how was your day",
        "how is your day going",
        "tell me about your day",
        "how did your day go",
        "how was your morning",
        "how was your evening",
        "did you have a good day",
        "how is today going",
        "what did you do today",
        "how was your day today"
    ],
    "intro": "Asking about someone's day is a friendly way to show interest in their daily experiences. It can lead to a meaningful conversation and help people connect with each other.",
    "points": [
        "Ask the question with genuine interest.",
        "Listen to their experience.",
        "Share something about your own day."
    ],
    "example": "How was your day? Mine was quite productive today."
},

"Responding to Nice to Meet You": {
    "aliases": [
        "nice to meet you reply",
        "what to reply to nice to meet you",
        "pleasure to meet you",
        "how to respond to nice to meet you",
        "nice meeting you reply",
        "reply when someone says nice to meet you",
        "what should i say after nice to meet you",
        "good to meet you reply",
        "response to pleasure to meet you",
        "nice to meet you too"
    ],
    "intro": "When someone says Nice to meet you, responding politely helps complete the introduction. A simple and friendly reply makes the first interaction comfortable and respectful.",
    "points": [
        "Say Nice to meet you too.",
        "You can also say It is a pleasure to meet you.",
        "Maintain a friendly tone."
    ],
    "example": "Person: Nice to meet you. You: Nice to meet you too!"
},

"Talking About Hobbies": {
    "aliases": [
        "what are your hobbies",
        "what do you like doing",
        "talk about hobbies",
        "what do you do in free time",
        "how do you spend your free time",
        "what do you enjoy doing",
        "tell me about your interests",
        "what are your interests",
        "what do you do for fun",
        "your favourite activities"
    ],
    "intro": "Talking about hobbies helps people discover shared interests and build friendships. It is a comfortable topic for casual conversations and getting to know someone better.",
    "points": [
        "Ask about activities they enjoy.",
        "Share your own hobbies.",
        "Look for common interests."
    ],
    "example": "What do you enjoy doing in your free time? I like learning new technologies."
},


            "HP Laptop 15s": {
                "aliases": [
                    "hp laptop 15s",
                    "hp 15s laptop",
                    "hp 15s fq5007tu",
                    "hp laptop",
                    "tell me about hp 15s",
                    "hp laptop specifications",
                    "hp laptop features",
                    "hp 15s review",
                    "hp laptop details",
                    "what is hp 15s"
                ],
                "intro": "❤️ Sandhu ji! The HP 15s is a laptop series designed for students, professionals, and everyday users. It supports activities like programming, browsing, online classes, office work, and entertainment.",
                "points": [
                    "It comes with different Intel and AMD processor options depending on the model.",
                    "It supports everyday tasks, programming, web development, and office applications.",
                    "Its performance depends on the processor, RAM, SSD, and exact laptop configuration."
                ],
                "example": "For example, an HP 15s with an Intel Core i3 processor, 8GB RAM, and 512GB SSD can be used for Python programming and college projects."
            },

            "HP Laptop Processor": {
                "aliases": [
                    "hp laptop processor",
                    "hp 15s processor",
                    "hp processor details",
                    "which processor does hp 15s have",
                    "intel core i3 hp laptop",
                    "hp laptop cpu",
                    "hp 15s intel processor",
                    "processor generation hp laptop",
                    "hp laptop processing speed",
                    "what is cpu in hp laptop"
                ],
                "intro": "❤️ Sandhu ji! A processor is the brain of a laptop. It performs calculations, executes instructions, and manages different tasks. HP 15s laptops are available with different processor configurations.",
                "points": [
                    "Intel Core i3 processors are suitable for everyday computing and basic programming.",
                    "Processor generations offer different levels of performance and efficiency.",
                    "Processor performance also depends on RAM, cooling, and workload."
                ],
                "example": "For example, an Intel Core i3 12th Generation processor can run VS Code, Python, and regular browser applications."
            },

            "HP Laptop RAM": {
                "aliases": [
                    "hp laptop ram",
                    "hp 15s ram",
                    "how much ram does hp 15s have",
                    "hp laptop memory",
                    "8gb ram hp laptop",
                    "hp ram upgrade",
                    "hp 15s ram upgrade",
                    "what is ram in hp laptop",
                    "hp laptop ram capacity",
                    "hp laptop memory upgrade"
                ],
                "intro": "❤️ Sandhu ji! RAM is temporary memory that helps a laptop run applications and perform multiple tasks. HP 15s laptops have different RAM configurations depending on the exact model.",
                "points": [
                    "8GB RAM is suitable for basic programming, browsing, and college work.",
                    "More RAM can improve multitasking and application performance.",
                    "Always check model compatibility before upgrading RAM."
                ],
                "example": "For example, 16GB RAM can provide a smoother experience when using VS Code and multiple browser tabs together."
            },

            "HP Laptop SSD": {
                "aliases": [
                    "hp laptop ssd",
                    "hp 15s storage",
                    "hp laptop storage",
                    "512gb ssd hp laptop",
                    "what is ssd in hp laptop",
                    "hp laptop ssd upgrade",
                    "hp laptop disk space",
                    "hp laptop storage capacity",
                    "upgrade hp laptop storage",
                    "hp laptop hard drive"
                ],
                "intro": "❤️ Sandhu ji! An SSD is a storage device that stores Windows, software, documents, and personal files. It helps a laptop start faster and load applications more quickly.",
                "points": [
                    "SSD storage is generally faster than traditional mechanical hard drives.",
                    "A 512GB SSD provides space for applications, projects, and documents.",
                    "Storage upgrades depend on the laptop's supported SSD specifications."
                ],
                "example": "For example, an SSD helps Windows and VS Code open faster, making everyday work more convenient."
            },

            "HP Laptop Programming": {
                "aliases": [
                    "hp laptop for programming",
                    "can hp 15s run python",
                    "hp laptop coding",
                    "hp 15s for coding",
                    "hp laptop for web development",
                    "can i use vs code on hp laptop",
                    "hp laptop for software development",
                    "hp laptop for students",
                    "programming on hp 15s",
                    "hp laptop coding performance"
                ],
                "intro": "❤️ Sandhu ji! HP 15s laptops can be useful for students learning programming and software development. They can run popular development tools depending on their hardware configuration.",
                "points": [
                    "You can use VS Code for Python, HTML, CSS, and JavaScript programming.",
                    "You can develop basic websites, Flask applications, and college projects.",
                    "Heavy development workloads may require more RAM and processing power."
                ],
                "example": "For example, you can use an HP 15s to build Python projects and develop websites using HTML, CSS, and JavaScript."
            },

            "HP Laptop Battery": {
                "aliases": [
                    "hp laptop battery",
                    "hp 15s battery",
                    "hp laptop battery backup",
                    "hp laptop battery health",
                    "hp laptop charging",
                    "hp laptop battery draining",
                    "hp laptop battery life",
                    "hp laptop not charging",
                    "hp laptop charger",
                    "hp laptop power problem"
                ],
                "intro": "❤️ Sandhu ji! A laptop battery supplies power when the device is not connected to a charger. Its backup depends on battery health, brightness, applications, and usage.",
                "points": [
                    "High screen brightness and heavy applications consume more battery.",
                    "Battery health naturally decreases with usage and charging cycles.",
                    "Battery saver mode can help extend battery usage time."
                ],
                "example": "For example, reducing screen brightness and closing unnecessary applications can help improve battery backup."
            },

            "HP Laptop Maintenance": {
                "aliases": [
                    "hp laptop maintenance",
                    "how to clean hp laptop",
                    "hp laptop care",
                    "hp laptop overheating",
                    "hp laptop fan noise",
                    "hp laptop getting slow",
                    "hp laptop performance improvement",
                    "how to maintain hp laptop",
                    "hp laptop cleaning tips",
                    "hp laptop troubleshooting"
                ],
                "intro": "❤️ Sandhu ji! Regular maintenance helps keep an HP laptop clean, reliable, and efficient. Proper hardware care and software maintenance can prevent common performance problems.",
                "points": [
                    "Keep Windows and device drivers updated using trusted sources.",
                    "Remove unnecessary temporary files and unused applications.",
                    "Keep the laptop ventilation areas clear to maintain proper airflow."
                ],
                "example": "For example, regularly cleaning temporary files and keeping the cooling vents clear can help maintain laptop performance."
            },

                        "Redmi 11 Prime 5G": {
                "aliases": [
                    "redmi 11 prime 5g",
                    "redmi 11 prime",
                    "redmi 11 prime specifications",
                    "redmi 11 prime features",
                    "redmi 11 prime review",
                    "redmi 11 prime processor",
                    "redmi 11 prime camera",
                    "redmi 11 prime battery",
                    "redmi 11 prime 5g details",
                    "tell me about redmi 11 prime"
                ],
                "intro": "❤️ Sandhu ji! The Redmi 11 Prime 5G is a budget-friendly smartphone from Xiaomi. It offers 5G connectivity, a large display, a capable processor, and a battery designed for everyday usage.",
                "points": [
                    "It features a 6.58-inch Full HD+ display with a 90Hz refresh rate.",
                    "It is powered by the MediaTek Dimensity 700 processor with up to 6GB RAM.",
                    "It includes a 50MP main camera, an 8MP front camera, and a 5000mAh battery."
                ],
                "example": "For example, you can use the Redmi 11 Prime 5G for calling, social media, online classes, photography, and everyday applications."
            },

            "Samsung Galaxy S26": {
                "aliases": [
                    "samsung galaxy s26",
                    "samsung s26",
                    "galaxy s26 specifications",
                    "samsung s26 features",
                    "samsung s26 review",
                    "samsung s26 processor",
                    "samsung s26 camera",
                    "samsung s26 battery",
                    "samsung galaxy s26 details",
                    "tell me about samsung s26"
                ],
                "intro": "❤️ Sandhu ji! The Samsung Galaxy S26 is a premium flagship smartphone launched in 2026. It offers an advanced display, powerful processing, professional camera features, and modern Galaxy AI experiences.",
                "points": [
                    "It features a 6.3-inch Dynamic AMOLED 2X display with a 120Hz refresh rate.",
                    "It comes with a 50MP main camera, 10MP telephoto camera, and 12MP ultra-wide camera.",
                    "It offers 12GB RAM, storage options of 256GB or 512GB, and a 4300mAh battery."
                ],
                "example": "For example, you can use the Samsung Galaxy S26 for high-quality photography, gaming, video recording, multitasking, and AI-powered features."
            },

            "Apple iPhone 17 Pro": {
                "aliases": [
                    "apple iphone 17 pro",
                    "iphone 17 pro",
                    "apple 17 pro",
                    "iphone 17 pro specifications",
                    "iphone 17 pro features",
                    "iphone 17 pro review",
                    "iphone 17 pro processor",
                    "iphone 17 pro camera",
                    "iphone 17 pro battery",
                    "tell me about iphone 17 pro"
                ],
                "intro": "❤️ Sandhu ji! The Apple iPhone 17 Pro is a premium smartphone introduced by Apple in September 2025. It focuses on powerful performance, advanced photography, video recording, and the iOS experience.",
                "points": [
                    "It features a 6.3-inch Super Retina XDR OLED display with ProMotion technology up to 120Hz.",
                    "It is powered by the A19 Pro chip and supports Apple Intelligence features.",
                    "It includes a 48MP Pro Fusion camera system with advanced photography and video capabilities."
                ],
                "example": "For example, you can use the iPhone 17 Pro for professional-style photography, 4K video recording, gaming, editing, and everyday productivity."
            },



                        "What Is Home": {
                "aliases": ["what is home", "define home", "meaning of home"],
                "intro": "❤️ Sandhu ji! A home is a place where a person or family lives. It provides shelter, comfort, safety, and a place to relax.",
                "points": [
                    "A home protects us from weather.",
                    "It gives us privacy and comfort.",
                    "It is a place where we create memories."
                ],
                "example": "For example, a house where parents and children live together is called their home."
            },

            "Importance of Family": {
                "aliases": ["why is family important", "importance of family", "role of family"],
                "intro": "❤️ Sandhu ji! Family is important because family members support, care for, and understand each other. They help us during difficult situations.",
                "points": [
                    "Family provides emotional support.",
                    "Members share responsibilities.",
                    "Family teaches love, respect, and good values."
                ],
                "example": "For example, parents help their children with education and important life decisions."
            },

            "Living Room": {
                "aliases": ["what is a living room", "importance of living room", "what do we do in living room"],
                "intro": "❤️ Sandhu ji! A living room is a common area where family members sit, relax, and spend time together. It is also used to welcome guests.",
                "points": [
                    "It usually contains sofas and chairs.",
                    "Family members watch television and talk there.",
                    "It should be comfortable and organized."
                ],
                "example": "For example, a family can sit together in the living room and watch a movie."
            },

            "Kitchen": {
                "aliases": ["what is a kitchen", "importance of kitchen", "what is the use of kitchen"],
                "intro": "❤️ Sandhu ji! A kitchen is a special area of a home where food is prepared and cooked. It is one of the most important parts of a house.",
                "points": [
                    "Food is prepared and cooked in the kitchen.",
                    "Utensils and cooking equipment are stored there.",
                    "Cleanliness is important for food safety."
                ],
                "example": "For example, we use a gas stove, utensils, and refrigerator to prepare and store food."
            },

            "Bedroom": {
                "aliases": ["what is a bedroom", "importance of bedroom", "what is the use of bedroom"],
                "intro": "❤️ Sandhu ji! A bedroom is a private room used for sleeping, resting, and personal activities. It provides privacy and comfort.",
                "points": [
                    "A bedroom usually contains a bed and wardrobe.",
                    "It provides a comfortable place to sleep.",
                    "Keeping it clean improves the environment."
                ],
                "example": "For example, a person sleeps in their bedroom at night to feel fresh the next morning."
            },

            "Bathroom": {
                "aliases": ["what is a bathroom", "importance of bathroom", "how to keep bathroom clean"],
                "intro": "❤️ Sandhu ji! A bathroom is a place used for personal hygiene and cleanliness. It helps people maintain their daily health and hygiene.",
                "points": [
                    "It contains facilities for bathing and washing.",
                    "It should be cleaned regularly.",
                    "Floors should be kept dry to prevent slipping."
                ],
                "example": "For example, cleaning the bathroom regularly helps prevent bad smells and germs."
            },

            "Home Cleaning": {
                "aliases": ["how to clean a home", "home cleaning tips", "how to keep house clean"],
                "intro": "❤️ Sandhu ji! Home cleaning means removing dust, dirt, and waste from different areas of the house. A clean home creates a healthy environment.",
                "points": [
                    "Sweep and mop floors regularly.",
                    "Clean kitchen surfaces and bathrooms.",
                    "Put unnecessary items and waste in their proper places."
                ],
                "example": "For example, spending 20 minutes daily cleaning rooms can help maintain a tidy home."
            },

            "Home Decoration": {
                "aliases": ["how to decorate a home", "home decoration ideas", "how to make home beautiful"],
                "intro": "❤️ Sandhu ji! Home decoration means arranging furniture, colours, lights, and decorative items to make a house attractive and comfortable.",
                "points": [
                    "Choose colours that look good together.",
                    "Use suitable curtains, lights, and furniture.",
                    "Keep decorations simple and organized."
                ],
                "example": "For example, adding indoor plants and beautiful curtains can make a living room look attractive."
            },

            "Home Security": {
                "aliases": ["how to keep home safe", "home security tips", "how to protect your house"],
                "intro": "❤️ Sandhu ji! Home security means protecting family members and belongings from possible dangers. Safety arrangements help people feel comfortable and secure.",
                "points": [
                    "Lock doors and windows when leaving home.",
                    "Use suitable security cameras or alarms if needed.",
                    "Keep emergency contact numbers available."
                ],
                "example": "For example, checking the main door lock before sleeping is a simple home safety habit."
            },

            "Electricity Saving": {
                "aliases": ["how to save electricity at home", "ways to reduce electricity bill", "how to use less electricity"],
                "intro": "❤️ Sandhu ji! Saving electricity means using electrical energy carefully and avoiding unnecessary consumption. It also helps reduce monthly electricity bills.",
                "points": [
                    "Switch off lights and fans when not needed.",
                    "Use energy-efficient LED bulbs.",
                    "Unplug chargers and unused devices."
                ],
                "example": "For example, switching off the fan and light when leaving a room helps save electricity."
            },

            "Water Saving": {
                "aliases": ["how to save water at home", "ways to conserve water", "how to reduce water wastage"],
                "intro": "❤️ Sandhu ji! Water conservation means using water carefully and avoiding unnecessary wastage. Clean water is an important resource for every living being.",
                "points": [
                    "Close taps properly after use.",
                    "Repair leaking taps and pipes.",
                    "Reuse suitable water for gardening."
                ],
                "example": "For example, using leftover water from washing vegetables to water plants can reduce water wastage."
            },

            "Home Garden": {
                "aliases": ["how to make a home garden", "importance of home garden", "how to grow plants at home"],
                "intro": "❤️ Sandhu ji! A home garden is an area where people grow plants, flowers, vegetables, or herbs. It makes the surroundings greener and more pleasant.",
                "points": [
                    "Choose plants according to available sunlight.",
                    "Water plants according to their needs.",
                    "Remove dry leaves and maintain the soil."
                ],
                "example": "For example, you can grow mint, coriander, and tomatoes in small pots on your balcony."
            },

            "Waste Management": {
                "aliases": ["how to manage household waste", "how to dispose home garbage", "what is waste management at home"],
                "intro": "❤️ Sandhu ji! Waste management means collecting, separating, and disposing of household waste properly. It helps keep our homes and surroundings clean.",
                "points": [
                    "Separate wet and dry waste.",
                    "Recycle paper, plastic, glass, and metal where possible.",
                    "Put garbage in designated dustbins."
                ],
                "example": "For example, vegetable peels can go into a wet waste bin while plastic bottles can be collected for recycling."
            },

            "Household Responsibilities": {
                "aliases": ["what are household responsibilities", "how to share home responsibilities", "who should do household work"],
                "intro": "❤️ Sandhu ji! Household responsibilities are daily tasks that help maintain a home. Every family member can contribute according to their age and ability.",
                "points": [
                    "Everyone should keep their personal space clean.",
                    "Family members can share cooking and cleaning tasks.",
                    "Children can help with simple household activities."
                ],
                "example": "For example, one person can prepare food while another cleans the dining table."
            },

            "Happy Home": {
                "aliases": ["how to make a happy home", "what makes a happy family", "how to create a peaceful home"],
                "intro": "❤️ Sandhu ji! A happy home is a place where family members feel loved, respected, and supported. Good communication and understanding make family life better.",
                "points": [
                    "Respect everyone's opinions and feelings.",
                    "Spend quality time together.",
                    "Solve disagreements calmly and peacefully."
                ],
                "example": "For example, having dinner together and discussing everyone's day can build stronger family relationships."
            },




                        "Anmol Meaning": {
                "aliases": ["what is the meaning of anmol", "anmol name meaning", "meaning of name anmol"],
                "intro": "❤️ Sandhu ji! Anmol is a beautiful Punjabi and Indian name that means priceless, precious, or extremely valuable.",
                "points": [
                    "It represents something that cannot be measured by money.",
                    "It is commonly used as a person's name.",
                    "The name symbolizes value, importance, and uniqueness."
                ],
                "example": "For example, parents may name their child Anmol because the child is priceless to them."
            },

            "Sandhu Meaning": {
                "aliases": ["what is sandhu", "sandhu surname meaning", "meaning of sandhu surname"],
                "intro": "❤️ Sandhu ji! Sandhu is a well-known Punjabi surname and clan name found mainly in Punjab and among Punjabi communities around the world.",
                "points": [
                    "Sandhu is traditionally associated with a Punjabi Jat clan.",
                    "People with this surname live in India and other countries.",
                    "A surname alone does not tell us a person's complete identity or beliefs."
                ],
                "example": "For example, a person with the surname Sandhu may have family roots in Punjab."
            },

            "Punjabi Meaning": {
                "aliases": ["what does punjabi mean", "meaning of punjabi", "who are punjabis"],
                "intro": "❤️ Sandhu ji! Punjabi refers to the people, language, and culture connected with the Punjab region of South Asia.",
                "points": [
                    "Punjabi is spoken in India and Pakistan.",
                    "Punjabi culture is known for its music, food, festivals, and traditions.",
                    "Punjabi people follow different religions and have diverse backgrounds."
                ],
                "example": "For example, someone who speaks Punjabi and follows Punjabi traditions may be described as Punjabi."
            },

            "Hindu Meaning": {
                "aliases": ["what is hindu", "meaning of hindu", "who are hindus"],
                "intro": "❤️ Sandhu ji! Hindu refers to a person who follows Hinduism, one of the world's major religions. Hinduism has a rich history, philosophy, and many spiritual traditions.",
                "points": [
                    "Hinduism includes beliefs about karma, dharma, and rebirth in many traditions.",
                    "It has sacred texts such as the Vedas and Bhagavad Gita.",
                    "Diwali, Holi, and Navratri are important Hindu festivals."
                ],
                "example": "For example, a person who follows Hindu religious traditions may identify as Hindu."
            },

            "Sikh Meaning": {
                "aliases": ["what is sikh", "meaning of sikh", "who are sikhs"],
                "intro": "❤️ Sandhu ji! A Sikh is a follower of Sikhism, a religion founded by Guru Nanak Dev Ji in Punjab. Sikhism teaches equality, honesty, service, and devotion to one God.",
                "points": [
                    "Sikhs respect the teachings of the ten Sikh Gurus.",
                    "The Guru Granth Sahib Ji is the eternal Guru of Sikhs.",
                    "Seva, equality, and honest living are important Sikh values."
                ],
                "example": "For example, a Sikh may visit a Gurdwara, participate in prayers, and serve food through langar."
            },

            "Khalsa Meaning": {
                "aliases": ["what is khalsa", "meaning of khalsa", "who is khalsa"],
                "intro": "❤️ Sandhu ji! Khalsa refers to the initiated Sikh community established by Guru Gobind Singh Ji in 1699 at Anandpur Sahib.",
                "points": [
                    "The Khalsa was established on Vaisakhi in 1699.",
                    "Initiated Sikhs follow the discipline and values of the Khalsa.",
                    "The five Ks are important articles of Sikh faith."
                ],
                "example": "For example, a Sikh who receives Amrit and follows the Khalsa discipline becomes part of the Khalsa."
            },

            "Community Meaning": {
                "aliases": ["what is community", "meaning of community", "what does community mean"],
                "intro": "❤️ Sandhu ji! A community is a group of people connected through a shared location, interest, culture, language, or purpose.",
                "points": [
                    "People in a community may help and support each other.",
                    "A community can be based on culture, profession, or location.",
                    "Communities encourage cooperation and social relationships."
                ],
                "example": "For example, people living in the same village may form a local community."
            },

            "Caste Meaning": {
                "aliases": ["what is caste", "meaning of caste", "what is the caste system"],
                "intro": "❤️ Sandhu ji! Caste is a form of social classification historically used in South Asian societies. It has influenced social identity and opportunities in different ways.",
                "points": [
                    "Caste has historically been associated with birth and family background.",
                    "The caste system has contributed to social discrimination and inequality.",
                    "Every person deserves equal dignity, rights, and respect."
                ],
                "example": "For example, judging someone as better or worse because of their caste is discrimination."
            },

            "Bobby Meaning": {
                "aliases": ["what is the meaning of bobby", "bobby name meaning", "meaning of name bobby"],
                "intro": "❤️ Sandhu ji! Bobby is a popular personal name and nickname. It is often used as a short form of Robert, although it can also be an independent name.",
                "points": [
                    "Bobby is used as a name for different genders.",
                    "Robert is traditionally associated with fame and brightness.",
                    "Bobby is also used as an affectionate nickname."
                ],
                "example": "For example, someone named Robert may be lovingly called Bobby by family and friends."
            },

            "Rajinder Kaur Meaning": {
                "aliases": ["what is rajinder kaur", "rajinder kaur name meaning", "meaning of rajinder kaur"],
                "intro": "❤️ Sandhu ji! Rajinder Kaur is a Punjabi name. Rajinder is commonly interpreted as ruler of kings, while Kaur is a traditional Sikh women's name meaning princess.",
                "points": [
                    "Rajinder is related to the Sanskrit name Rajendra.",
                    "Kaur is traditionally used by Sikh women.",
                    "Together, the name carries associations of leadership and dignity."
                ],
                "example": "For example, Rajinder Kaur can be understood as a name combining the ideas of royal leadership and a princess."
            },

            "Kaur Meaning": {
                "aliases": ["what is kaur", "meaning of kaur", "why do sikh girls use kaur"],
                "intro": "❤️ Sandhu ji! Kaur is a traditional name used by Sikh women. It is commonly translated as princess and represents dignity and equality.",
                "points": [
                    "Guru Gobind Singh Ji encouraged Sikh women to use Kaur.",
                    "It helps represent a shared Sikh identity beyond family surnames.",
                    "Kaur is widely used as a middle or last name."
                ],
                "example": "For example, a Sikh woman may use the name Harpreet Kaur."
            },

            "Honey Meaning": {
                "aliases": ["what is honey meaning", "honey word meaning", "honey name meaning"],
                "intro": "❤️ Sandhu ji! Honey is a natural sweet substance produced by honeybees. It is also used as an affectionate nickname for someone loved or cared about.",
                "points": [
                    "Honey is made by bees from flower nectar.",
                    "It is commonly used as a food sweetener.",
                    "As a nickname, it expresses affection and warmth."
                ],
                "example": "For example, someone may lovingly call their partner or child Honey."
            },

            "Villy Meaning": {
                "aliases": ["what is villy meaning", "villy name meaning", "meaning of villy"],
                "intro": "❤️ Sandhu ji! Villy may be a personal name or nickname, but its exact meaning depends on the intended spelling and language.",
                "points": [
                    "It may be a spelling variation or a family nickname.",
                    "It should not automatically be assigned a fixed meaning.",
                    "The original spelling can help identify its correct origin."
                ],
                "example": "For example, if you mean Willy or Willie, those are commonly used forms of William."
            },

            "Parmeet Meaning": {
                "aliases": ["what is parmeet", "parmeet name meaning", "meaning of name parmeet"],
                "intro": "❤️ Sandhu ji! Parmeet is a Punjabi and Indian personal name. Its interpretation can vary, but it is often associated with friendship, goodness, and spiritual connection.",
                "points": [
                    "It is used as a personal name in Punjabi families.",
                    "The name is sometimes interpreted as a supreme or special friend.",
                    "Its exact meaning can depend on its linguistic origin."
                ],
                "example": "For example, parents may choose the name Parmeet because they like its positive and meaningful sound."
            },

            "Kalu Maasi Meaning": {
                "aliases": ["what is kalu maasi", "meaning of maasi", "who is maasi in punjabi"],
                "intro": "❤️ Sandhu ji! Maasi is a Punjabi and Hindi family relationship word for a mother's sister. Kalu may be a person's name or nickname in this phrase.",
                "points": [
                    "Maasi means maternal aunt.",
                    "A maasi is the sister of someone's mother.",
                    "Kalu may refer to a particular person's nickname."
                ],
                "example": "For example, your mother's sister is your Maasi. If her nickname is Kalu, someone may call her Kalu Maasi."
            },

            "Channa Meaning": {
                "aliases": ["what is channa", "channa word meaning", "meaning of channa in punjabi"],
                "intro": "❤️ Sandhu ji! Channa is commonly used for chickpeas in Punjabi and Hindi food vocabulary. It can also appear as a personal name or affectionate nickname.",
                "points": [
                    "Channa is used in many Indian dishes.",
                    "Chole and channa masala are popular chickpea dishes.",
                    "The word may have a different meaning when used as a name."
                ],
                "example": "For example, channa masala is a popular Indian curry prepared using chickpeas."
            },

            "Navneet Meaning": {
                "aliases": ["what is navneet", "navneet name meaning", "meaning of navneet"],
                "intro": "❤️ Sandhu ji! Navneet is an Indian name derived from Sanskrit. It commonly means fresh butter and is associated with softness, sweetness, and purity.",
                "points": [
                    "The name comes from the Sanskrit word Navanita.",
                    "Navanita refers to fresh or newly churned butter.",
                    "Navneet is used as a personal name."
                ],
                "example": "For example, parents may choose Navneet as a name because of its traditional and positive meaning."
            },

            "Gurmeet Meaning": {
                "aliases": ["what is gurmeet", "gurmeet name meaning", "meaning of gurmeet"],
                "intro": "❤️ Sandhu ji! Gurmeet is a Punjabi and Sikh name formed from Guru and Meet. It is commonly interpreted as a friend or companion of the Guru.",
                "points": [
                    "Guru refers to a spiritual teacher.",
                    "Meet means friend or companion in this name.",
                    "The name is associated with spiritual connection and guidance."
                ],
                "example": "For example, someone named Gurmeet may be understood as a companion of the Guru."
            },

            "Singh Meaning": {
                "aliases": ["what is singh", "meaning of singh", "why do sikhs use singh"],
                "intro": "❤️ Sandhu ji! Singh is a name traditionally used by Sikh men. It comes from a word meaning lion and represents courage, dignity, and equality.",
                "points": [
                    "Guru Gobind Singh Ji encouraged Sikh men to use Singh.",
                    "The name symbolizes bravery and strength.",
                    "Singh is also used by people from other communities."
                ],
                "example": "For example, a Sikh man may use the name Harpreet Singh."
            },

            "Punjab Meaning": {
                "aliases": ["what is punjab", "meaning of punjab", "where is punjab"],
                "intro": "❤️ Sandhu ji! Punjab is a historical region in South Asia. The name is commonly explained as the land of five rivers.",
                "points": [
                    "Punjab is divided between India and Pakistan.",
                    "Indian Punjab has Chandigarh as its capital.",
                    "The region is known for agriculture, Punjabi language, music, and culture."
                ],
                "example": "For example, Amritsar, Ludhiana, and Jalandhar are well-known cities in Indian Punjab."
            },

            "Waheguru Meaning": {
                "aliases": ["what is waheguru", "meaning of waheguru", "who is waheguru"],
                "intro": "❤️ Sandhu ji! Waheguru is a sacred name used by Sikhs for God. It expresses wonder, praise, and devotion to the wonderful divine.",
                "points": [
                    "Waheguru represents the one supreme God in Sikhism.",
                    "Sikhs remember Waheguru through Naam Simran.",
                    "The word is used in Sikh prayers and spiritual practice."
                ],
                "example": "For example, Sikhs may repeat Waheguru during meditation and prayer."
            },

            "Guru Meaning": {
                "aliases": ["what is guru", "meaning of guru", "who is a guru"],
                "intro": "❤️ Sandhu ji! A Guru is a spiritual teacher or guide who helps people understand knowledge, truth, and the right path in life.",
                "points": [
                    "A Guru provides guidance and wisdom.",
                    "The word is used in several Indian spiritual traditions.",
                    "In Sikhism, the Guru Granth Sahib Ji is the eternal Guru."
                ],
                "example": "For example, a teacher who guides students towards knowledge can be described as a guru in a general sense."
            },

            "Seva Meaning": {
                "aliases": ["what is seva", "meaning of seva", "what is seva in sikhism"],
                "intro": "❤️ Sandhu ji! Seva means selfless service. It is an important value in Sikhism and encourages people to help others without expecting rewards.",
                "points": [
                    "Seva can include helping people in need.",
                    "It teaches humility, kindness, and equality.",
                    "It can be performed through physical work, time, or resources."
                ],
                "example": "For example, helping prepare and serve food in a Gurdwara is a form of Seva."
            },

            "Langar Meaning": {
                "aliases": ["what is langar", "meaning of langar", "why is langar served"],
                "intro": "❤️ Sandhu ji! Langar is a free community meal served in a Gurdwara. It represents equality, sharing, and service in Sikh tradition.",
                "points": [
                    "Everyone is welcome to eat langar regardless of background.",
                    "Volunteers prepare and serve the food.",
                    "People traditionally sit together to share the meal."
                ],
                "example": "For example, visitors at the Golden Temple in Amritsar can eat free langar."
            },

            "Sat Sri Akal Meaning": {
                "aliases": ["what is sat sri akal", "meaning of sat sri akal", "when do we say sat sri akal"],
                "intro": "❤️ Sandhu ji! Sat Sri Akal is a common Sikh greeting in Punjabi. It expresses the idea that God is the eternal truth.",
                "points": [
                    "Sat means truth or eternal reality.",
                    "Sri is an honorific word expressing respect.",
                    "Akal refers to the timeless one."
                ],
                "example": "For example, Punjabi speakers often greet each other by saying Sat Sri Akal."
            },




                    "Daru Meaning": {
            "aliases": ["what is daru", "daru meaning", "meaning of daru"],
            "intro": "❤️ Sandhu ji! Daru is a common Hindi and Punjabi word for alcoholic drinks. These drinks contain ethanol, which affects the brain and body.",
            "points": [
                "Daru includes drinks such as whisky, rum, vodka, and wine.",
                "Alcohol can affect judgment, memory, and coordination.",
                "Regular consumption can lead to dependence and health problems."
            ],
            "example": "For example, whisky and rum are commonly called daru in everyday conversations."
        },

        "Beer Meaning": {
            "aliases": ["what is beer", "beer meaning", "how is beer made"],
            "intro": "❤️ Sandhu ji! Beer is an alcoholic beverage generally made by fermenting grains such as barley. It contains ethanol and can cause intoxication.",
            "points": [
                "Beer is made using water, grains, hops, and yeast.",
                "Its alcohol content varies depending on the product.",
                "Regular consumption can increase health risks."
            ],
            "example": "For example, lager and ale are two common types of beer."
        },

        "Alcohol Meaning": {
            "aliases": ["what is alcohol", "alcohol meaning", "what is ethanol"],
            "intro": "❤️ Sandhu ji! Alcohol in alcoholic beverages usually refers to ethanol, a chemical substance that affects the central nervous system.",
            "points": [
                "Ethanol is found in beer, wine, and spirits.",
                "It can slow reactions and affect decision-making.",
                "Excessive consumption can damage the liver and other organs."
            ],
            "example": "For example, ethanol is responsible for the intoxicating effects of alcoholic drinks."
        },

        "Nasha Meaning": {
            "aliases": ["what is nasha", "meaning of nasha", "what is intoxication"],
            "intro": "❤️ Sandhu ji! Nasha refers to intoxication or an altered mental and physical state caused by certain substances.",
            "points": [
                "It can affect memory, balance, and thinking.",
                "Different substances produce different effects.",
                "Repeated substance use can lead to addiction."
            ],
            "example": "For example, a person may experience poor coordination after consuming alcohol."
        },

        "Feem Meaning": {
            "aliases": ["what is feem", "feem meaning", "what is opium"],
            "intro": "❤️ Sandhu ji! Feem is a Punjabi word for opium, a substance obtained from the opium poppy plant. It contains powerful opioid chemicals.",
            "points": [
                "Opium contains naturally occurring substances such as morphine.",
                "It can cause drowsiness and slow breathing.",
                "Repeated use can lead to physical dependence and addiction."
            ],
            "example": "For example, opium misuse can cause serious health problems and require professional treatment."
        },

        "Whisky Meaning": {
            "aliases": ["what is whisky", "whisky meaning", "what is whiskey"],
            "intro": "❤️ Sandhu ji! Whisky is a distilled alcoholic beverage generally produced from fermented grains. It contains ethanol and can cause intoxication.",
            "points": [
                "It is commonly made using barley, corn, or rye.",
                "Some varieties are aged in wooden barrels.",
                "It can affect the brain and nervous system."
            ],
            "example": "For example, Scotch whisky is a well-known category of whisky."
        },

        "Rum Meaning": {
            "aliases": ["what is rum", "rum meaning", "how is rum made"],
            "intro": "❤️ Sandhu ji! Rum is a distilled alcoholic beverage generally made from sugarcane products such as molasses or sugarcane juice.",
            "points": [
                "Rum is produced through fermentation and distillation.",
                "It comes in different varieties and styles.",
                "It contains alcohol and carries health risks."
            ],
            "example": "For example, white rum and dark rum are two common varieties."
        },

        "Vodka Meaning": {
            "aliases": ["what is vodka", "vodka meaning", "how is vodka made"],
            "intro": "❤️ Sandhu ji! Vodka is a distilled alcoholic beverage traditionally produced from fermented grains or potatoes.",
            "points": [
                "Vodka is generally a clear distilled spirit.",
                "Its alcohol concentration varies by product.",
                "Alcohol consumption can affect the brain and body."
            ],
            "example": "For example, vodka is produced through fermentation followed by distillation."
        },

        "Wine Meaning": {
            "aliases": ["what is wine", "wine meaning", "how is wine made"],
            "intro": "❤️ Sandhu ji! Wine is an alcoholic beverage generally made by fermenting grapes or other fruits.",
            "points": [
                "Red wine and white wine are common varieties.",
                "Wine is produced through fermentation.",
                "It contains alcohol and is not risk-free."
            ],
            "example": "For example, red wine is commonly produced using dark-coloured grapes."
        },

        "Drug Meaning": {
            "aliases": ["what are drugs", "drug meaning", "what is a drug"],
            "intro": "❤️ Sandhu ji! A drug is a substance that changes how the body or brain functions. Some drugs are medicines, while others can be harmful when misused.",
            "points": [
                "Medicines are used to prevent or treat health conditions.",
                "Some drugs affect mood, thinking, and behaviour.",
                "Misusing drugs can cause dependence and health problems."
            ],
            "example": "For example, a doctor may prescribe medicine to treat an infection."
        },

        "Addiction Meaning": {
            "aliases": ["what is addiction", "meaning of addiction", "what is substance addiction"],
            "intro": "❤️ Sandhu ji! Addiction is a condition in which a person struggles to control substance use despite harmful consequences.",
            "points": [
                "It can affect physical and mental health.",
                "It may damage relationships, education, and professional life.",
                "Professional treatment and support can help recovery."
            ],
            "example": "For example, someone who repeatedly drinks alcohol despite serious problems may have alcohol addiction."
        },

        "Alcohol Dependence": {
            "aliases": ["what is alcohol dependence", "alcohol dependency meaning", "signs of alcohol dependence"],
            "intro": "❤️ Sandhu ji! Alcohol dependence occurs when the body and brain become accustomed to regular alcohol consumption.",
            "points": [
                "A person may develop a strong urge to drink.",
                "Tolerance can increase over time.",
                "Medical supervision may be necessary when stopping alcohol."
            ],
            "example": "For example, someone experiencing shaking when alcohol is unavailable may need medical assessment."
        },

        "Smoking Meaning": {
            "aliases": ["what is smoking", "smoking meaning", "effects of smoking"],
            "intro": "❤️ Sandhu ji! Smoking means inhaling smoke produced by burning tobacco or other substances. It can seriously damage the body.",
            "points": [
                "Smoking increases the risk of lung cancer.",
                "It can damage the heart and blood vessels.",
                "Quitting smoking improves long-term health."
            ],
            "example": "For example, cigarette smoking exposes the lungs to harmful chemicals."
        },

        "Tobacco Meaning": {
            "aliases": ["what is tobacco", "tobacco meaning", "what is nicotine"],
            "intro": "❤️ Sandhu ji! Tobacco is a plant whose leaves contain nicotine, an addictive substance. Tobacco products can cause serious health problems.",
            "points": [
                "Tobacco is used in cigarettes and other products.",
                "Nicotine can cause dependence.",
                "Tobacco use increases the risk of cancer and heart disease."
            ],
            "example": "For example, cigarettes contain tobacco and nicotine."
        },

        "Cannabis Meaning": {
            "aliases": ["what is cannabis", "cannabis meaning", "what is marijuana"],
            "intro": "❤️ Sandhu ji! Cannabis is a plant containing chemical compounds called cannabinoids. Some of these compounds affect brain activity and perception.",
            "points": [
                "THC is a psychoactive compound found in cannabis.",
                "Cannabis can affect memory and attention.",
                "Frequent use can create health and dependence-related risks."
            ],
            "example": "For example, cannabis use can affect a person's ability to drive safely."
        },

        "Opioids Meaning": {
            "aliases": ["what are opioids", "opioid meaning", "what is opioid addiction"],
            "intro": "❤️ Sandhu ji! Opioids are substances that act on opioid receptors in the body. Some are prescribed for severe pain but carry risks.",
            "points": [
                "Morphine and codeine are examples of opioids.",
                "Opioids can slow breathing.",
                "They should only be used under medical supervision."
            ],
            "example": "For example, a doctor may prescribe an opioid medicine for severe pain after surgery."
        },

        "Overdose Meaning": {
            "aliases": ["what is overdose", "meaning of drug overdose", "what happens in overdose"],
            "intro": "❤️ Sandhu ji! An overdose happens when someone takes more of a substance than the body can safely handle. It can be life-threatening.",
            "points": [
                "Symptoms may include unconsciousness and difficulty breathing.",
                "An opioid overdose can cause dangerously slow breathing.",
                "Emergency medical help should be called immediately."
            ],
            "example": "For example, if someone becomes unconscious after taking drugs, call emergency services immediately."
        },

        "Hangover Meaning": {
            "aliases": ["what is hangover", "hangover meaning", "why does hangover happen"],
            "intro": "❤️ Sandhu ji! A hangover refers to unpleasant physical and mental symptoms that can occur after drinking alcohol.",
            "points": [
                "Symptoms may include headache, nausea, and tiredness.",
                "Alcohol can contribute to dehydration and poor sleep.",
                "Severe symptoms require urgent medical attention."
            ],
            "example": "For example, someone may experience a headache the morning after drinking alcohol."
        },

        "Withdrawal Meaning": {
            "aliases": ["what is withdrawal", "withdrawal symptoms meaning", "what is alcohol withdrawal"],
            "intro": "❤️ Sandhu ji! Withdrawal refers to symptoms that occur when someone reduces or stops a substance after becoming physically dependent on it.",
            "points": [
                "Symptoms can include sweating, anxiety, shaking, and nausea.",
                "Severe alcohol withdrawal can cause seizures.",
                "Medical supervision is important for significant dependence."
            ],
            "example": "For example, a person with long-term alcohol dependence may need supervised treatment when stopping."
        },

        "De Addiction Meaning": {
            "aliases": ["what is de addiction", "meaning of de addiction", "how to overcome addiction"],
            "intro": "❤️ Sandhu ji! De-addiction means receiving treatment and support to stop harmful substance use and recover from addiction.",
            "points": [
                "Treatment may include medical care and counselling.",
                "Support from family and professionals can help recovery.",
                "Long-term follow-up can reduce the risk of relapse."
            ],
            "example": "For example, someone struggling with alcohol addiction can seek help from a qualified specialist."
        },

        "Rehabilitation Meaning": {
            "aliases": ["what is rehabilitation", "meaning of rehabilitation", "what is rehab centre"],
            "intro": "❤️ Sandhu ji! Rehabilitation is a structured process that helps people recover their health, daily routines, and independence after addiction or illness.",
            "points": [
                "It may include medical treatment and counselling.",
                "It helps people develop healthier habits.",
                "Family support can improve recovery."
            ],
            "example": "For example, a person recovering from substance addiction may attend a rehabilitation programme."
        },

        "Nasha Mukti Kendra": {
            "aliases": ["what is nasha mukti kendra", "meaning of nasha mukti centre", "where to get addiction treatment"],
            "intro": "❤️ Sandhu ji! A Nasha Mukti Kendra is a centre that provides support and treatment for people experiencing substance addiction.",
            "points": [
                "Centres may provide medical assessment and counselling.",
                "Treatment depends on the person's health and needs.",
                "Choose a properly registered and qualified treatment facility."
            ],
            "example": "For example, someone struggling with drug dependence can consult a doctor and seek treatment."
        },

        "Effects of Alcohol": {
            "aliases": ["what are effects of alcohol", "how alcohol affects the body", "alcohol side effects"],
            "intro": "❤️ Sandhu ji! Alcohol affects several organs, including the brain, liver, heart, and digestive system. Risks increase with greater consumption.",
            "points": [
                "Short-term effects include poor coordination and slower reactions.",
                "Long-term use can cause liver disease and certain cancers.",
                "Alcohol can also affect mental health and relationships."
            ],
            "example": "For example, drinking alcohol before driving increases the risk of road accidents."
        },

        "Alcohol and Driving": {
            "aliases": ["can we drive after drinking alcohol", "alcohol and driving risks", "why is drunk driving dangerous"],
            "intro": "❤️ Sandhu ji! Driving after consuming alcohol is dangerous because alcohol affects concentration, judgment, and reaction time.",
            "points": [
                "Alcohol reduces the ability to judge distance and speed.",
                "It slows down reaction time.",
                "Never drive after drinking; arrange safe transport."
            ],
            "example": "For example, someone who has consumed alcohol should use a taxi instead of driving."
        },

        "Helping an Addicted Person": {
            "aliases": ["how to help an addicted person", "how to support drug addict", "how to help someone quit alcohol"],
            "intro": "❤️ Sandhu ji! Helping someone with addiction requires patience, understanding, and professional guidance.",
            "points": [
                "Talk calmly and encourage professional medical help.",
                "Support the person without judging them.",
                "Seek emergency help if overdose or severe withdrawal occurs."
            ],
            "example": "For example, a family member can help someone arrange an appointment with an addiction specialist."
        },

        "Substance Abuse Prevention": {
            "aliases": ["how to prevent substance abuse", "how to avoid nasha", "ways to stay away from drugs"],
            "intro": "❤️ Sandhu ji! Substance abuse prevention means avoiding harmful drug and alcohol use through awareness, healthy habits, and positive support.",
            "points": [
                "Learn about the health risks of addictive substances.",
                "Build healthy hobbies and supportive friendships.",
                "Seek help early when facing stress or substance-use pressure."
            ],
            "example": "For example, joining sports activities and talking to trusted people can help avoid harmful substance use."
        },




                "Punjab Meaning": {
            "aliases": ["what is punjab", "where is punjab located", "tell me about punjab"],
            "intro": "❤️ Sandhu ji! Punjab is a state in northern India known for its rich culture, agriculture, history, and Punjabi language.",
            "points": [
                "Chandigarh is the capital of Punjab.",
                "Punjabi is the main official language of the state.",
                "Punjab is famous for farming, traditional food, music, and festivals."
            ],
            "example": "For example, Punjab is famous for wheat farming, Bhangra, Giddha, and traditional Punjabi food."
        },

        "Amritsar City": {
            "aliases": ["what is amritsar", "where is amritsar", "tell me about amritsar"],
            "intro": "❤️ Sandhu ji! Amritsar is a famous city in Punjab, India. It is internationally known for the Golden Temple and its Sikh religious and historical importance.",
            "points": [
                "The Golden Temple is one of the most important Sikh religious sites.",
                "Jallianwala Bagh is an important historical memorial.",
                "Amritsar is famous for Punjabi food and tourism."
            ],
            "example": "For example, thousands of visitors travel to Amritsar to visit Sri Harmandir Sahib."
        },

        "Batala City": {
            "aliases": ["what is batala", "where is batala", "tell me about batala"],
            "intro": "❤️ Sandhu ji! Batala is a historic city in the Gurdaspur district of Punjab, India. It is known for its history, industries, and cultural heritage.",
            "points": [
                "Batala is located in the Majha region of Punjab.",
                "It has a history of metal and engineering industries.",
                "The city has several historical and religious places."
            ],
            "example": "For example, Batala is known for its traditional engineering and metalworking industries."
        },

        "India Country": {
            "aliases": ["what is india", "where is india located", "tell me about india"],
            "intro": "❤️ Sandhu ji! India is a country in South Asia with a rich history, diverse cultures, and many languages. Its capital is New Delhi.",
            "points": [
                "India is the world's largest democracy by population.",
                "It has 28 states and 8 Union Territories.",
                "Hindi and English are used for official purposes at the Union level."
            ],
            "example": "For example, India celebrates Independence Day on 15 August every year."
        },

        "State Meaning": {
            "aliases": ["what is a state", "meaning of state", "what is state in india"],
            "intro": "❤️ Sandhu ji! A state is an administrative division of a country that has its own government and defined geographical boundaries.",
            "points": [
                "States have their own elected governments.",
                "Each state has a capital city.",
                "States manage several areas of administration and public services."
            ],
            "example": "For example, Punjab, Haryana, and Rajasthan are states of India."
        },

        "City Meaning": {
            "aliases": ["what is a city", "meaning of city", "how is a city different from a village"],
            "intro": "❤️ Sandhu ji! A city is a large human settlement where people live, work, study, and access different facilities and services.",
            "points": [
                "Cities usually have schools, hospitals, offices, and markets.",
                "They provide employment and business opportunities.",
                "Cities generally have more developed infrastructure than small villages."
            ],
            "example": "For example, Amritsar, Chandigarh, and Delhi are well-known cities."
        },

        "District Meaning": {
            "aliases": ["what is a district", "meaning of district", "what is district in india"],
            "intro": "❤️ Sandhu ji! A district is an administrative area within a state. It helps the government manage local administration and public services.",
            "points": [
                "A district is generally managed by a District Magistrate or Deputy Commissioner.",
                "A state can contain several districts.",
                "Districts include towns, villages, and sometimes cities."
            ],
            "example": "For example, Gurdaspur is a district in Punjab, and Batala is a city within it."
        },

        "Punjab Culture": {
            "aliases": ["what is punjabi culture", "tell me about punjab culture", "what is famous in punjab"],
            "intro": "❤️ Sandhu ji! Punjabi culture is known for its energetic music, traditional clothing, delicious food, festivals, and welcoming social traditions.",
            "points": [
                "Bhangra and Giddha are popular traditional dances.",
                "Baisakhi and Lohri are important festivals.",
                "Makki di roti, sarson da saag, and lassi are popular foods."
            ],
            "example": "For example, people celebrate Lohri with music, dancing, and traditional gatherings."
        },

        "Majha Region": {
            "aliases": ["what is majha", "where is majha region", "is amritsar in majha"],
            "intro": "❤️ Sandhu ji! Majha is a historical and cultural region of Punjab. It includes important areas on both sides of the India-Pakistan border.",
            "points": [
                "Amritsar and Gurdaspur are associated with the Indian Majha region.",
                "Punjabi language and traditional culture are important parts of Majha.",
                "The region has significant historical and religious heritage."
            ],
            "example": "For example, Amritsar and Batala are both located in the Majha region of Punjab."
        },

        "Punjab Geography": {
            "aliases": ["where is punjab situated", "which states border punjab", "punjab geographical location"],
            "intro": "❤️ Sandhu ji! Punjab is located in northwestern India. It shares boundaries with several Indian states and the Union Territory of Chandigarh.",
            "points": [
                "Punjab borders Jammu and Kashmir, Himachal Pradesh, Haryana, and Rajasthan.",
                "It also shares an international border with Pakistan.",
                "The state has fertile agricultural land and river systems."
            ],
            "example": "For example, Amritsar is located in northwestern Punjab near the India-Pakistan border."
        },




                "India Country": {
            "aliases": ["what is india", "tell me about india", "which country is india"],
            "intro": "❤️ Sandhu ji! India is a country in South Asia. It is known for its diverse cultures, languages, traditions, history, and democratic system.",
            "points": [
                "The capital of India is New Delhi.",
                "India has 28 states and 8 Union Territories.",
                "India celebrates Independence Day on 15 August."
            ],
            "example": "For example, Punjab, Chhattisgarh, Haryana, and Maharashtra are states of India."
        },

        "Number of States in India": {
            "aliases": ["how many states are in india", "total number of states in india", "number of indian states"],
            "intro": "❤️ Sandhu ji! India currently has 28 states. Every state has its own government, administration, culture, and geographical identity.",
            "points": [
                "India has a total of 28 states.",
                "Each state has its own capital.",
                "States are responsible for many regional administrative services."
            ],
            "example": "For example, Chhattisgarh is one of the 28 states of India."
        },

        "Union Territories of India": {
            "aliases": ["how many union territories are in india", "total union territories in india", "what are union territories"],
            "intro": "❤️ Sandhu ji! India has 8 Union Territories. They are administrative regions that are governed under the Union Government, with some having their own legislatures.",
            "points": [
                "India has 8 Union Territories.",
                "Delhi, Ladakh, and Chandigarh are examples.",
                "Their administration is different from that of states."
            ],
            "example": "For example, Chandigarh is a Union Territory and also the capital of Punjab and Haryana."
        },

        "Chhattisgarh State": {
            "aliases": ["what is chhattisgarh", "tell me about chhattisgarh", "where is chhattisgarh located"],
            "intro": "❤️ Sandhu ji! Chhattisgarh is a state located in central India. It is famous for its natural resources, forests, waterfalls, culture, and mineral industries.",
            "points": [
                "Raipur is the capital of Chhattisgarh.",
                "The state was formed on 1 November 2000.",
                "Hindi and Chhattisgarhi are widely used languages."
            ],
            "example": "For example, Chitrakote Waterfall is a famous tourist attraction in Chhattisgarh."
        },

        "Chhattisgarh Formation": {
            "aliases": ["when was chhattisgarh formed", "chhattisgarh formation date", "when did chhattisgarh become a state"],
            "intro": "❤️ Sandhu ji! Chhattisgarh became a separate state on 1 November 2000 after being separated from Madhya Pradesh.",
            "points": [
                "Chhattisgarh was formed on 1 November 2000.",
                "It was previously part of Madhya Pradesh.",
                "Every year, 1 November is celebrated as Chhattisgarh Foundation Day."
            ],
            "example": "For example, Chhattisgarh celebrates its state foundation day on 1 November."
        },

        "Raipur City": {
            "aliases": ["what is raipur", "tell me about raipur", "where is raipur located"],
            "intro": "❤️ Sandhu ji! Raipur is the capital city of Chhattisgarh. It is an important centre for education, business, transportation, and administration.",
            "points": [
                "Raipur is the capital of Chhattisgarh.",
                "It is an important commercial and educational city.",
                "Swami Vivekananda Airport serves the city."
            ],
            "example": "For example, the Chhattisgarh state government operates from the capital city of Raipur."
        },

        "Bhilai City": {
            "aliases": ["what is bhilai", "tell me about bhilai", "where is bhilai located"],
            "intro": "❤️ Sandhu ji! Bhilai is an important industrial city in Chhattisgarh, located in Durg district. It is especially famous for the Bhilai Steel Plant.",
            "points": [
                "Bhilai is located in Durg district.",
                "Bhilai Steel Plant is a major industrial landmark.",
                "The city is known for steel production and industrial development."
            ],
            "example": "For example, Bhilai Steel Plant is one of the major steel-producing facilities in India."
        },

        "Durg City": {
            "aliases": ["what is durg", "tell me about durg city", "where is durg located"],
            "intro": "❤️ Sandhu ji! Durg is an important city and district headquarters in Chhattisgarh. It is part of the Durg-Bhilai urban region.",
            "points": [
                "Durg is located in Chhattisgarh.",
                "Durg district includes the Bhilai industrial area.",
                "The region is known for education, trade, and industries."
            ],
            "example": "For example, people often travel between Durg and Bhilai for work, education, and business."
        },

        "Chhattisgarh Districts": {
            "aliases": ["how many districts are in chhattisgarh", "total districts in chhattisgarh", "number of districts in cg"],
            "intro": "❤️ Sandhu ji! Chhattisgarh currently has 33 districts. These districts help manage local administration and public services across the state.",
            "points": [
                "Chhattisgarh has 33 districts.",
                "Raipur, Durg, Bilaspur, and Bastar are some of its districts.",
                "Each district has its own local administrative structure."
            ],
            "example": "For example, Raipur district and Durg district are two districts of Chhattisgarh."
        },

        "Difference Between Raipur and Bhilai": {
            "aliases": ["difference between raipur and bhilai", "is raipur same as bhilai", "compare raipur and bhilai"],
            "intro": "❤️ Sandhu ji! Raipur and Bhilai are two different cities in Chhattisgarh. Raipur is the state capital, while Bhilai is widely known for its steel industry.",
            "points": [
                "Raipur is the capital of Chhattisgarh.",
                "Bhilai is located in Durg district.",
                "Both cities are important for the state's economy and development."
            ],
            "example": "For example, Raipur is known for state administration, while Bhilai is famous for the Bhilai Steel Plant."
        },




                "Study Assistant": {
            "aliases": [
                "what is a study assistant",
                "what can a study assistant do",
                "help me with my studies",
                "how can i study effectively",
                "how can i understand difficult topics"
            ],
            "intro": "❤️ Sandhu ji! A Study Assistant helps students understand subjects, prepare for exams, and improve their learning skills.",
            "points": [
                "It explains difficult concepts in simple language.",
                "It helps students prepare notes, practice questions, and revise important topics.",
                "It supports better time management and organized learning."
            ],
            "example": "For example, a student can use a Study Assistant to understand Python, prepare BCA exam notes, and practice interview questions."
        },

        "Code Studio": {
            "aliases": [
                "what is code studio",
                "what can i do in code studio",
                "how can i improve my coding skills",
                "how can i fix programming errors",
                "how can i learn programming"
            ],
            "intro": "❤️ Sandhu ji! Code Studio is a development workspace that helps programmers write, understand, test, and improve their code.",
            "points": [
                "It helps users understand programming concepts and code logic.",
                "It can explain common programming errors and suggest possible solutions.",
                "It supports learning different programming languages and development technologies."
            ],
            "example": "For example, a beginner can use Code Studio to understand Python code, fix a syntax error, and learn how to build a website."
        },

        "Data Analysis": {
            "aliases": [
                "what is data analysis",
                "what can i do in data analysis",
                "how can i analyze data",
                "what is the purpose of data analysis",
                "how can i start learning data analytics"
            ],
            "intro": "❤️ Sandhu ji! Data Analysis is the process of collecting, cleaning, organizing, and studying data to discover useful information and make better decisions.",
            "points": [
                "Python, SQL, Excel, and Power BI are commonly used in data analysis.",
                "Data analysts create reports, dashboards, and visualizations.",
                "Data analysis helps businesses identify patterns, trends, and opportunities."
            ],
            "example": "For example, a company can analyze its sales data using Excel and Power BI to understand which products are performing best."
        },

        "Interview Preparation": {
            "aliases": [
                "what is interview preparation",
                "how can i prepare for an interview",
                "how can i improve my interview skills",
                "what questions are asked in interviews",
                "how can i become confident in interviews"
            ],
            "intro": "❤️ Sandhu ji! Interview Preparation is the process of practicing questions, improving communication skills, and building confidence before attending a job interview.",
            "points": [
                "Candidates should prepare their self-introduction and explain their educational background.",
                "They should practice technical questions related to their skills and projects.",
                "Good communication, confidence, and honest answers help create a positive impression."
            ],
            "example": "For example, a BCA student can prepare Python questions, explain their projects, and practice common HR interview questions before an interview."
        },



                "Learn Something": {
            "aliases": [
                "learn something",
                "teach me something",
                "i want to learn something new",
                "explain a new topic",
                "help me learn a subject"
            ],
            "intro": "❤️ Sandhu ji! Learning something new is a great way to improve your knowledge, develop skills, and grow personally and professionally.",
            "points": [
                "Choose a topic that interests you and start with its basic concepts.",
                "Practice regularly and try to understand concepts instead of memorizing everything.",
                "Use books, tutorials, videos, and practical exercises to improve your knowledge."
            ],
            "example": "For example, you can learn Python programming by understanding variables, practicing small programs, and building simple projects."
        },

        "Write Something": {
            "aliases": [
                "write something",
                "help me write something",
                "write an article",
                "create some content",
                "help me write a paragraph"
            ],
            "intro": "❤️ Sandhu ji! Writing is the process of expressing thoughts, information, and ideas through words in a clear and meaningful way.",
            "points": [
                "You can write emails, articles, essays, captions, stories, and professional documents.",
                "Good writing should have clear language, correct grammar, and an organized structure.",
                "Always understand the purpose and audience before creating written content."
            ],
            "example": "For example, you can write a professional LinkedIn post about completing an internship or developing a new project."
        },

        "Fix My Code": {
            "aliases": [
                "fix my code",
                "debug my code",
                "find errors in my code",
                "help me solve a coding error",
                "why is my code not working"
            ],
            "intro": "❤️ Sandhu ji! Debugging is the process of identifying, understanding, and fixing errors in a computer program.",
            "points": [
                "Read the error message carefully to understand where the problem occurred.",
                "Check syntax, indentation, variable names, and program logic.",
                "Test the corrected code to make sure it works as expected."
            ],
            "example": "For example, if Python shows a NameError, check whether the variable has been defined correctly before using it."
        },

        "Find an Idea": {
            "aliases": [
                "find an idea",
                "give me a project idea",
                "suggest a new idea",
                "i need a creative idea",
                "help me find an idea"
            ],
            "intro": "❤️ Sandhu ji! Finding an idea means discovering a useful or creative concept that can be developed into a project, business, solution, or new activity.",
            "points": [
                "Identify a problem, need, or interest that you want to explore.",
                "Research existing solutions and think about how you can make something better.",
                "Start with a small plan and test whether your idea is practical and useful."
            ],
            "example": "For example, a BCA student can develop a Student Management System, Expense Tracker, or Data Analytics Dashboard as a practical project."
        },




                "Plan My Week": {
            "aliases": [
                "plan my week",
                "help me plan my week",
                "create a weekly routine",
                "make a weekly schedule",
                "how should i organize my week"
            ],
            "intro": "❤️ Sandhu ji! Planning your week helps you organize your responsibilities, manage your time, and maintain a healthy balance between work, studies, and personal activities.",
            "points": [
                "Write down your important tasks, deadlines, and weekly goals.",
                "Divide your time between work, studies, exercise, rest, and personal activities.",
                "Keep some flexible time for unexpected tasks and take regular breaks."
            ],
            "example": "For example, a college student can plan study sessions, coding practice, gym time, assignments, and weekend revision in a weekly timetable."
        },

        "Project Ideas": {
            "aliases": [
                "project ideas",
                "suggest some project ideas",
                "give me software project ideas",
                "what project should i build",
                "i need a new project idea"
            ],
            "intro": "❤️ Sandhu ji! Project ideas are practical concepts that can be developed into useful applications, websites, software tools, or business solutions.",
            "points": [
                "Choose a project according to your interests, skills, and learning goals.",
                "Start with a simple version and gradually add useful features.",
                "Focus on solving a real problem instead of adding unnecessary features."
            ],
            "example": "For example, a BCA student can build an AI chatbot, expense tracker, student management system, or sales analytics dashboard."
        },

        "Take a Quiz": {
            "aliases": [
                "take a quiz",
                "start a quiz",
                "test my knowledge",
                "ask me some questions",
                "give me a practice test"
            ],
            "intro": "❤️ Sandhu ji! A quiz is a learning activity that tests your knowledge and helps you understand how well you remember a particular subject.",
            "points": [
                "Quizzes can include multiple-choice, true-or-false, and short-answer questions.",
                "Reviewing incorrect answers helps identify areas that need improvement.",
                "Regular practice improves knowledge, accuracy, and confidence."
            ],
            "example": "For example, you can take a Python quiz covering variables, data types, loops, functions, and basic programming concepts."
        },

        "Code Review": {
            "aliases": [
                "code review",
                "review my code",
                "check my programming code",
                "improve my code quality",
                "make my code better"
            ],
            "intro": "❤️ Sandhu ji! Code Review is the process of examining source code to improve its quality, readability, reliability, and maintainability.",
            "points": [
                "Check code for logical mistakes, bugs, and unnecessary complexity.",
                "Use meaningful variable names, proper formatting, and reusable functions.",
                "Review security, performance, and error handling where necessary."
            ],
            "example": "For example, a developer can review a Python project to remove repeated code, improve function names, and fix potential errors."
        },

        "Resume Builder": {
            "aliases": [
                "resume builder",
                "create my resume",
                "help me build a resume",
                "make a professional cv",
                "how can i improve my resume"
            ],
            "intro": "❤️ Sandhu ji! A Resume Builder helps you create a professional resume that presents your education, skills, projects, experience, and achievements clearly.",
            "points": [
                "Include your contact details, career objective, education, and technical skills.",
                "Add relevant projects, internships, certifications, and measurable achievements.",
                "Use a clean layout, clear headings, and simple professional language."
            ],
            "example": "For example, a BCA student can create a resume highlighting Python, SQL, Data Analytics projects, internships, and relevant certifications."
        },

        "Skill Builder": {
            "aliases": [
                "skill builder",
                "help me build a skill",
                "create a learning roadmap",
                "how can i improve my skills",
                "make a practical learning plan"
            ],
            "intro": "❤️ Sandhu ji! A Skill Builder helps you develop new abilities through structured learning, regular practice, and practical projects.",
            "points": [
                "Choose one skill and divide it into beginner, intermediate, and advanced topics.",
                "Follow a realistic learning roadmap with regular practice sessions.",
                "Build practical projects to apply your knowledge and track your progress."
            ],
            "example": "For example, you can learn Data Analytics through a roadmap covering Excel, SQL, Python, Pandas, NumPy, and Power BI."
        },

        "Presentation": {
            "aliases": [
                "presentation",
                "create a presentation",
                "help me make slides",
                "prepare a presentation",
                "how to make a good presentation"
            ],
            "intro": "❤️ Sandhu ji! A Presentation is an organized way of communicating information, ideas, or research to an audience using spoken explanations and visual materials.",
            "points": [
                "Start with a clear title and organize your content into meaningful sections.",
                "Use readable text, relevant images, charts, and simple slide designs.",
                "Practice your delivery and keep your explanation clear and within the available time."
            ],
            "example": "For example, a student can create a presentation about Artificial Intelligence with slides covering its introduction, applications, benefits, challenges, and conclusion."
        },

        "Compare Options": {
            "aliases": [
                "compare options",
                "compare two options",
                "help me compare choices",
                "which option is better",
                "help me make a decision"
            ],
            "intro": "❤️ Sandhu ji! Comparing options means evaluating different choices using relevant factors so you can make a clear and informed decision.",
            "points": [
                "Identify the important factors such as cost, quality, features, time, and reliability.",
                "Compare the advantages and disadvantages of each available option.",
                "Choose the option that best matches your needs, priorities, and budget."
            ],
            "example": "For example, you can compare two laptops based on processor, RAM, storage, battery life, price, and programming performance."
        },
        












                "Swift Car": {
            "aliases": [
                "what is swift car",
                "swift car price",
                "swift specifications"
            ],
            "intro": "❤️ Sandhu ji! Maruti Suzuki Swift is a popular hatchback in India known for its sporty design, fuel efficiency, and comfortable driving experience.",
            "points": [
                "Approximate starting price is ₹5.84 lakh ex-showroom.",
                "It has a 1.2-litre Z-Series petrol engine.",
                "It is available with manual and AMT transmission options."
            ],
            "example": "For example, Swift is a popular choice for daily city driving."
        },

        "Hyundai Verna": {
            "aliases": [
                "what is hyundai verna",
                "verna car price",
                "verna specifications"
            ],
            "intro": "❤️ Sandhu ji! Hyundai Verna is a premium sedan known for its stylish design, comfortable interior, and powerful petrol engines.",
            "points": [
                "Approximate starting price is ₹10.99 lakh ex-showroom.",
                "It offers 1.5-litre petrol and turbo-petrol engines.",
                "Features include ADAS, touchscreen infotainment, and automatic transmission options."
            ],
            "example": "For example, Verna is suitable for people who prefer a stylish sedan."
        },

        "Tata Safari": {
            "aliases": [
                "what is tata safari",
                "safari car price",
                "safari specifications"
            ],
            "intro": "❤️ Sandhu ji! Tata Safari is a premium family SUV known for its bold design, spacious cabin, and powerful diesel engine.",
            "points": [
                "Approximate starting price is ₹13.29 lakh ex-showroom.",
                "It comes with a 2.0-litre diesel engine.",
                "It is available in 6-seater and 7-seater configurations."
            ],
            "example": "For example, Safari is suitable for large families."
        },

        "Maruti Alto K10": {
            "aliases": [
                "what is alto k10",
                "alto car price",
                "alto specifications"
            ],
            "intro": "❤️ Sandhu ji! Maruti Alto K10 is an affordable hatchback designed for economical and convenient city driving.",
            "points": [
                "Approximate starting price is ₹3.70 lakh ex-showroom.",
                "It has a 1.0-litre petrol engine.",
                "It is available with manual and AMT transmission options."
            ],
            "example": "For example, Alto K10 is suitable for first-time car buyers."
        },

        "Toyota Fortuner": {
            "aliases": [
                "what is toyota fortuner",
                "fortuner car price",
                "fortuner specifications"
            ],
            "intro": "❤️ Sandhu ji! Toyota Fortuner is a premium full-size SUV famous for its muscular design, powerful performance, and strong road presence.",
            "points": [
                "Approximate starting price is ₹33.65 lakh ex-showroom.",
                "It offers petrol and diesel engine options.",
                "Selected variants offer four-wheel-drive capability."
            ],
            "example": "For example, Fortuner is popular among people who prefer powerful SUVs."
        },

        "Ford Endeavour": {
            "aliases": [
                "what is ford endeavour",
                "endeavour car price",
                "endeavour specifications"
            ],
            "intro": "❤️ Sandhu ji! Ford Endeavour is a premium SUV known for its muscular appearance, powerful diesel engine, and off-road capability.",
            "points": [
                "It was previously sold in India but is not currently part of Ford's regular new-car lineup.",
                "Used-car prices depend on model year and vehicle condition.",
                "It is known as Ford Everest in many international markets."
            ],
            "example": "For example, older Endeavour models are popular among SUV enthusiasts."
        },

        "Ford Company": {
            "aliases": [
                "what is ford",
                "tell me about ford company",
                "ford car brand"
            ],
            "intro": "❤️ Sandhu ji! Ford is an American automobile manufacturer known for SUVs, pickup trucks, sports cars, and performance vehicles.",
            "points": [
                "Popular models include Mustang, Endeavour, EcoSport, and Ranger.",
                "Ford has a historic presence in the Indian automobile market.",
                "Mustang is one of its most recognised performance cars."
            ],
            "example": "For example, Ford Mustang is famous for its sporty design."
        },

        "Ford Mustang": {
            "aliases": [
                "what is ford mustang",
                "mustang car price",
                "mustang specifications"
            ],
            "intro": "❤️ Sandhu ji! Ford Mustang is an iconic American sports car known for its aggressive design, powerful engines, and rear-wheel-drive performance.",
            "points": [
                "Indian availability and pricing depend on the model and import status.",
                "International versions include EcoBoost and 5.0-litre V8 GT options.",
                "It is available in coupe and convertible body styles in different markets."
            ],
            "example": "For example, Mustang GT is famous for its powerful V8 engine."
        },

        "Mercedes G Wagon": {
            "aliases": [
                "what is g wagon",
                "g wagon price",
                "mercedes g class specifications"
            ],
            "intro": "❤️ Sandhu ji! Mercedes-Benz G-Class, popularly called G-Wagon, is a luxury off-road SUV famous for its boxy design and premium interior.",
            "points": [
                "Approximate Indian starting price is around ₹2.90 crore ex-showroom.",
                "It features a powerful engine and four-wheel-drive system.",
                "It combines luxury, technology, and off-road capability."
            ],
            "example": "For example, G-Wagon is recognised by its iconic square-shaped body."
        },

        "Toyota Land Cruiser": {
            "aliases": [
                "what is land cruiser",
                "land cruiser price",
                "toyota lc specifications"
            ],
            "intro": "❤️ Sandhu ji! Toyota Land Cruiser is a premium luxury SUV known for durability, comfort, and excellent off-road performance.",
            "points": [
                "Approximate LC300 starting price is ₹2.16 crore ex-showroom.",
                "The Indian LC300 is offered with a powerful diesel engine.",
                "It features four-wheel drive and advanced off-road technology."
            ],
            "example": "For example, Land Cruiser is suitable for luxury travel and challenging terrain."
        },

        "Toyota Company": {
            "aliases": [
                "what is toyota",
                "tell me about toyota",
                "toyota car models"
            ],
            "intro": "❤️ Sandhu ji! Toyota is a Japanese automobile manufacturer known for reliable cars, SUVs, hybrid technology, and premium vehicles.",
            "points": [
                "Popular models include Fortuner, Innova HyCross, Glanza, and Hyryder.",
                "Toyota offers petrol, diesel, and hybrid vehicles.",
                "The company has a strong international automobile presence."
            ],
            "example": "For example, Toyota Fortuner is a popular premium SUV in India."
        },

        "BMW Cars": {
            "aliases": [
                "what is bmw",
                "bmw car price",
                "bmw car models"
            ],
            "intro": "❤️ Sandhu ji! BMW is a German luxury automobile brand known for sporty driving, premium interiors, and advanced technology.",
            "points": [
                "Popular models include 3 Series, 5 Series, 7 Series, X1, X5, and X7.",
                "BMW also produces high-performance M models.",
                "Its vehicles focus on luxury, performance, and driving experience."
            ],
            "example": "For example, BMW X5 is a luxury SUV and BMW M4 is a performance coupe."
        },

        "Mercedes-Benz Cars": {
            "aliases": [
                "what is mercedes benz",
                "mercedes car models",
                "mercedes car price"
            ],
            "intro": "❤️ Sandhu ji! Mercedes-Benz is a German luxury car manufacturer known for comfort, elegant styling, and premium technology.",
            "points": [
                "Popular models include C-Class, E-Class, S-Class, GLC, GLE, and G-Class.",
                "AMG represents its high-performance vehicle range.",
                "Maybach represents its ultra-luxury range."
            ],
            "example": "For example, Mercedes S-Class is famous for luxury and comfort."
        },

        "GT Cars": {
            "aliases": [
                "what is gt car",
                "meaning of gt in cars",
                "what is grand touring"
            ],
            "intro": "❤️ Sandhu ji! GT stands for Grand Touring. GT cars combine powerful performance with comfort for long-distance driving.",
            "points": [
                "GT cars generally offer powerful engines.",
                "They focus on performance and long-distance comfort.",
                "Examples include Mustang GT, Mercedes-AMG GT, and Bentley Continental GT."
            ],
            "example": "For example, Bentley Continental GT combines luxury and high performance."
        },

        "Nissan Cars": {
            "aliases": [
                "what is nissan",
                "nissan car models",
                "nissan car price"
            ],
            "intro": "❤️ Sandhu ji! Nissan is a Japanese automobile manufacturer known for SUVs, sedans, electric vehicles, and performance cars.",
            "points": [
                "Popular international models include GT-R, Patrol, Z, and X-Trail.",
                "Nissan Magnite is a well-known model in India.",
                "Nissan GT-R is famous for its powerful performance."
            ],
            "example": "For example, Nissan GT-R is a popular Japanese performance car."
        },

        "Tata Harrier": {
            "aliases": [
                "what is tata harrier",
                "harrier car price",
                "harrier specifications"
            ],
            "intro": "❤️ Sandhu ji! Tata Harrier is a premium five-seater SUV known for bold styling, a spacious cabin, and diesel performance.",
            "points": [
                "Approximate starting price is ₹12.89 lakh ex-showroom.",
                "It has a 2.0-litre diesel engine.",
                "Features include touchscreen infotainment and a panoramic sunroof on selected variants."
            ],
            "example": "For example, Harrier is suitable for families looking for a premium five-seater SUV."
        },

        "Tata Motors": {
            "aliases": [
                "what is tata motors",
                "tell me about tata cars",
                "tata car models"
            ],
            "intro": "❤️ Sandhu ji! Tata Motors is an Indian automobile manufacturer producing passenger cars, SUVs, electric vehicles, and commercial vehicles.",
            "points": [
                "Popular models include Nexon, Punch, Harrier, Safari, Tiago, and Curvv.",
                "It offers petrol, diesel, CNG, and electric vehicles.",
                "The company is known for its focus on vehicle safety."
            ],
            "example": "For example, Tata Nexon is available in petrol, diesel, and electric versions."
        },

        "Vehicle Meaning": {
            "aliases": [
                "what is a vehicle",
                "meaning of vehicle",
                "types of vehicles"
            ],
            "intro": "❤️ Sandhu ji! A vehicle is a machine used to transport people or goods from one location to another.",
            "points": [
                "Examples include cars, buses, trucks, motorcycles, and vans.",
                "Vehicles can use petrol, diesel, CNG, or electricity.",
                "They are used for personal and commercial transportation."
            ],
            "example": "For example, Swift is a passenger vehicle and a truck is a commercial vehicle."
        },

        "Sports Cars": {
            "aliases": [
                "what is a sports car",
                "sports car meaning",
                "sports car examples"
            ],
            "intro": "❤️ Sandhu ji! A sports car is designed for speed, acceleration, handling, and an exciting driving experience.",
            "points": [
                "Sports cars often have powerful engines and sporty suspension.",
                "Many sports cars have two doors and two seats.",
                "Examples include Porsche 911, Ford Mustang, and Chevrolet Corvette."
            ],
            "example": "For example, Porsche 911 is famous for its sporty performance."
        },

        "Mahindra Thar": {
            "aliases": [
                "what is mahindra thar",
                "thar car price",
                "thar specifications"
            ],
            "intro": "❤️ Sandhu ji! Mahindra Thar is a lifestyle off-road SUV known for its rugged design, high ground clearance, and adventure-focused features.",
            "points": [
                "It is available in different petrol and diesel configurations.",
                "Selected variants offer four-wheel-drive capability.",
                "It is popular for off-road adventures and road presence."
            ],
            "example": "For example, Thar is popular among people who enjoy adventure driving."
        },

        "Jeep Wrangler": {
            "aliases": [
                "what is jeep wrangler",
                "wrangler car price",
                "jeep wrangler specifications"
            ],
            "intro": "❤️ Sandhu ji! Jeep Wrangler is an iconic American off-road SUV with a rugged body, removable roof options, and advanced four-wheel-drive systems.",
            "points": [
                "Approximate Indian starting price is around ₹64 lakh ex-showroom.",
                "Indian versions use a 2.0-litre turbo-petrol engine.",
                "It is designed for challenging off-road conditions."
            ],
            "example": "For example, Wrangler is popular among adventure and off-road enthusiasts."
        },

        "Land Rover Defender": {
            "aliases": [
                "what is land rover defender",
                "defender car price",
                "defender specifications"
            ],
            "intro": "❤️ Sandhu ji! Land Rover Defender is a luxury off-road SUV combining premium interiors, modern technology, and excellent terrain capability.",
            "points": [
                "Approximate Defender 110 starting price is around ₹1.07 crore ex-showroom.",
                "Available in Defender 90, 110, and 130 body configurations.",
                "Features include four-wheel drive and terrain response systems."
            ],
            "example": "For example, Defender 110 offers luxury and off-road capability together."
        },

        "Car Models and Variants": {
            "aliases": [
                "what are car variants",
                "difference between car model and variant",
                "what is base model and top model"
            ],
            "intro": "❤️ Sandhu ji! A car model is the name of a vehicle, while variants are different versions with different features and equipment.",
            "points": [
                "Base variants generally offer essential features.",
                "Mid variants add convenience and technology.",
                "Top variants generally include more premium equipment."
            ],
            "example": "For example, a car may be available in LXi, VXi, ZXi, and ZXi+ variants."
        },

        "Top Model Cars": {
            "aliases": [
                "what is top model car",
                "what is top variant",
                "fully loaded car meaning"
            ],
            "intro": "❤️ Sandhu ji! A top model is generally the highest-equipped version of a particular car.",
            "points": [
                "It may include a sunroof, premium audio, and advanced safety features.",
                "Top variants usually cost more than base variants.",
                "Exact features depend on the manufacturer and model."
            ],
            "example": "For example, a top variant may offer ventilated seats and a 360-degree camera."
        },

        "Car Modification": {
            "aliases": [
                "what is car modification",
                "car modification types",
                "types of car modifications"
            ],
            "intro": "❤️ Sandhu ji! Car modification means changing a vehicle's appearance, performance, comfort, or functionality from its original factory setup.",
            "points": [
                "Common modifications include alloy wheels, body kits, and seat covers.",
                "Performance modifications may include suspension and exhaust upgrades.",
                "Modifications must follow applicable Indian vehicle safety and legal rules."
            ],
            "example": "For example, installing approved alloy wheels can change the appearance of a car."
        },

        "Car Body Kits": {
            "aliases": [
                "what is car body kit",
                "car body kit modification",
                "bumper modification"
            ],
            "intro": "❤️ Sandhu ji! A body kit is a collection of exterior parts used to change the appearance and sometimes the aerodynamics of a vehicle.",
            "points": [
                "It can include front bumpers, rear bumpers, side skirts, and spoilers.",
                "Body kits are available in different designs and materials.",
                "Modifications should not compromise vehicle safety."
            ],
            "example": "For example, a sporty body kit can give a sedan a more aggressive appearance."
        },

        "Car Engine Types": {
            "aliases": [
                "what are car engine types",
                "petrol vs diesel engine",
                "types of car engines"
            ],
            "intro": "❤️ Sandhu ji! A car engine or powertrain converts fuel or electrical energy into movement.",
            "points": [
                "Common types include petrol, diesel, hybrid, and electric powertrains.",
                "Petrol and diesel engines use internal combustion.",
                "Electric cars use battery-powered electric motors."
            ],
            "example": "For example, Swift uses a petrol engine while Tata Nexon EV uses an electric motor."
        },

        "Car Transmission": {
            "aliases": [
                "what is car transmission",
                "manual vs automatic car",
                "car gearbox types"
            ],
            "intro": "❤️ Sandhu ji! Transmission is the system that transfers engine power to the wheels and controls gear ratios.",
            "points": [
                "Manual transmission requires the driver to change gears.",
                "Automatic options include AMT, CVT, DCT, and torque converter.",
                "Each type offers a different driving experience."
            ],
            "example": "For example, a manual car has a clutch pedal, while an automatic car changes gears automatically."
        },

        "Car Safety Features": {
            "aliases": [
                "what are car safety features",
                "car safety systems",
                "important car safety features"
            ],
            "intro": "❤️ Sandhu ji! Car safety features are systems designed to help prevent accidents and protect passengers.",
            "points": [
                "Important features include airbags, ABS, and electronic stability control.",
                "Advanced systems may include ADAS and blind-spot monitoring.",
                "Safety equipment varies by car variant."
            ],
            "example": "For example, ABS helps prevent the wheels from locking during hard braking."
        },

        "Porsche Cars": {
            "aliases": [
                "what is porsche",
                "porsche car models",
                "porsche car price"
            ],
            "intro": "❤️ Sandhu ji! Porsche is a German luxury sports-car manufacturer famous for performance, engineering, and premium design.",
            "points": [
                "Popular models include 911, Cayenne, Macan, Panamera, and Taycan.",
                "The 911 is one of its most iconic sports cars.",
                "Porsche offers petrol and electric models."
            ],
            "example": "For example, Porsche 911 is known for its unique design and performance."
        },

        "Lamborghini Cars": {
            "aliases": [
                "what is lamborghini",
                "lamborghini car models",
                "lamborghini price"
            ],
            "intro": "❤️ Sandhu ji! Lamborghini is an Italian supercar manufacturer famous for aggressive styling, powerful engines, and exotic performance vehicles.",
            "points": [
                "Popular models include Urus, Revuelto, and Temerario.",
                "Urus is a luxury performance SUV.",
                "Lamborghini cars belong to the premium supercar segment."
            ],
            "example": "For example, Lamborghini Urus combines SUV practicality with performance."
        },

        "Ferrari Cars": {
            "aliases": [
                "what is ferrari",
                "ferrari car models",
                "ferrari car price"
            ],
            "intro": "❤️ Sandhu ji! Ferrari is an Italian luxury sports-car manufacturer known for racing heritage, high performance, and distinctive design.",
            "points": [
                "Popular models include 296 GTB, SF90, and 12Cilindri.",
                "Ferrari also participates in Formula One racing.",
                "Its vehicles are known for powerful engines and premium craftsmanship."
            ],
            "example": "For example, Ferrari 296 GTB is a high-performance hybrid sports car."
        },

        "Rolls Royce Cars": {
            "aliases": [
                "what is rolls royce",
                "rolls royce car models",
                "rolls royce price"
            ],
            "intro": "❤️ Sandhu ji! Rolls-Royce is a British ultra-luxury automobile manufacturer known for handcrafted interiors, comfort, and exclusivity.",
            "points": [
                "Popular models include Phantom, Ghost, Cullinan, and Spectre.",
                "Cullinan is its luxury SUV.",
                "The brand focuses on comfort and personalisation."
            ],
            "example": "For example, Rolls-Royce Phantom is known for exceptional luxury."
        },

        "Audi Cars": {
            "aliases": [
                "what is audi",
                "audi car models",
                "audi car price"
            ],
            "intro": "❤️ Sandhu ji! Audi is a German luxury automobile brand known for modern styling, advanced technology, and quattro all-wheel-drive systems.",
            "points": [
                "Popular models include A4, A6, Q3, Q5, Q7, and Q8.",
                "Audi RS models focus on high performance.",
                "The brand offers luxury sedans and SUVs."
            ],
            "example": "For example, Audi Q7 is a premium luxury SUV."
        },

        "Bentley Cars": {
            "aliases": [
                "what is bentley",
                "bentley car models",
                "bentley continental gt"
            ],
            "intro": "❤️ Sandhu ji! Bentley is a British luxury car manufacturer known for powerful grand touring cars and handcrafted premium interiors.",
            "points": [
                "Popular models include Continental GT, Flying Spur, and Bentayga.",
                "Bentayga is its luxury SUV.",
                "Continental GT is a famous grand touring car."
            ],
            "example": "For example, Bentley Continental GT combines performance and luxury."
        },

        "McLaren Cars": {
            "aliases": [
                "what is mclaren",
                "mclaren car models",
                "mclaren supercars"
            ],
            "intro": "❤️ Sandhu ji! McLaren is a British performance-car manufacturer with strong Formula One racing heritage.",
            "points": [
                "Popular models include 750S, Artura, and GTS.",
                "McLaren vehicles focus on lightweight engineering and performance.",
                "The brand is famous for aerodynamic supercar designs."
            ],
            "example": "For example, McLaren 750S is a high-performance supercar."
        },

        "Aston Martin Cars": {
            "aliases": [
                "what is aston martin",
                "aston martin car models",
                "aston martin price"
            ],
            "intro": "❤️ Sandhu ji! Aston Martin is a British luxury sports-car manufacturer known for elegant styling and powerful grand touring vehicles.",
            "points": [
                "Popular models include DB12, Vantage, and DBX.",
                "DBX is its luxury SUV.",
                "The brand is also associated with James Bond films."
            ],
            "example": "For example, Aston Martin DB12 is a luxury grand touring sports car."
        },

        "Car Price in India": {
            "aliases": [
                "how are car prices decided",
                "car price in india",
                "ex showroom and on road price"
            ],
            "intro": "❤️ Sandhu ji! Car prices in India depend on the model, variant, engine, features, taxes, insurance, and registration charges.",
            "points": [
                "Ex-showroom price is the listed price before registration and insurance.",
                "On-road price includes applicable registration, insurance, and other charges.",
                "Prices can vary between cities and dealerships."
            ],
            "example": "For example, a car with a ₹10 lakh ex-showroom price will generally cost more on-road."
        },

        "Luxury Cars": {
            "aliases": [
                "what are luxury cars",
                "luxury car brands",
                "luxury car examples"
            ],
            "intro": "❤️ Sandhu ji! Luxury cars are premium vehicles designed to provide high levels of comfort, technology, performance, and quality.",
            "points": [
                "Popular luxury brands include BMW, Mercedes-Benz, Audi, and Lexus.",
                "Ultra-luxury brands include Rolls-Royce and Bentley.",
                "Luxury vehicles often feature premium interiors and advanced technology."
            ],
            "example": "For example, Mercedes S-Class and BMW 7 Series are luxury sedans."
        },

        "Supercars": {
            "aliases": [
                "what is supercar",
                "supercar meaning",
                "supercar examples"
            ],
            "intro": "❤️ Sandhu ji! A supercar is a high-performance sports car designed with exceptional acceleration, speed, engineering, and exclusive styling.",
            "points": [
                "Supercars often use powerful engines and lightweight materials.",
                "Examples include Ferrari, Lamborghini, and McLaren models.",
                "They are generally more expensive than regular sports cars."
            ],
            "example": "For example, Lamborghini Revuelto is a high-performance hybrid supercar."
        },

        "Hypercars": {
            "aliases": [
                "what is hypercar",
                "hypercar meaning",
                "hypercar examples"
            ],
            "intro": "❤️ Sandhu ji! A hypercar is an extremely high-performance and exclusive vehicle that often represents the highest level of automotive engineering.",
            "points": [
                "Hypercars may feature advanced hybrid or electric technology.",
                "Examples include Bugatti Tourbillon and Koenigsegg Jesko.",
                "They are generally produced in limited numbers."
            ],
            "example": "For example, Bugatti models are known for extreme speed and advanced engineering."
        },

        "SUV Cars": {
            "aliases": [
                "what is suv",
                "suv meaning",
                "suv car examples"
            ],
            "intro": "❤️ Sandhu ji! SUV stands for Sports Utility Vehicle. SUVs generally offer a higher seating position, spacious interiors, and versatile driving capabilities.",
            "points": [
                "SUVs are available in compact, mid-size, and full-size categories.",
                "Examples include Thar, Fortuner, Safari, and Defender.",
                "Some SUVs offer four-wheel-drive capability."
            ],
            "example": "For example, Toyota Fortuner is a full-size SUV."
        },

        "Sedan Cars": {
            "aliases": [
                "what is sedan car",
                "sedan meaning",
                "sedan car examples"
            ],
            "intro": "❤️ Sandhu ji! A sedan is a passenger car generally featuring four doors, a separate boot, and a comfortable cabin.",
            "points": [
                "Sedans are designed for comfortable passenger travel.",
                "Popular examples include Hyundai Verna and Mercedes-Benz E-Class.",
                "They generally have a lower driving position than SUVs."
            ],
            "example": "For example, Hyundai Verna is a mid-size sedan."
        },

        "Hatchback Cars": {
            "aliases": [
                "what is hatchback car",
                "hatchback meaning",
                "hatchback car examples"
            ],
            "intro": "❤️ Sandhu ji! A hatchback is a compact passenger car with a rear door that opens upwards and provides access to the luggage area.",
            "points": [
                "Hatchbacks are generally easy to drive in cities.",
                "They are often more compact than sedans and SUVs.",
                "Examples include Swift, Alto K10, and Tata Tiago."
            ],
            "example": "For example, Maruti Swift is a popular hatchback in India."
        },
        






            "BCA": {
                "aliases": ["bca", "bachelor of computer applications"],
                "intro": "BCA stands for Bachelor of Computer Applications. It is an undergraduate degree focused on computer applications, programming, software development, databases, and information technology. It helps students build technical knowledge and prepare for careers in the IT industry.",
                "points": [
                    "It is generally a three-year undergraduate degree.",
                    "Students learn programming, databases, networking, and software development.",
                    "Career options include software developer, web developer, and IT support."
                ],
                "example": "A BCA student can create a website using HTML, CSS, JavaScript, and Python."
            },

            "B.Tech": {
                "aliases": ["btech", "b.tech", "b tech", "bachelor of technology"],
                "intro": "B.Tech stands for Bachelor of Technology. It is an undergraduate engineering degree that focuses on technical concepts, engineering principles, practical projects, and specialized technology fields. Students develop problem-solving skills and prepare for engineering and technology careers.",
                "points": [
                    "It is generally a four-year undergraduate degree.",
                    "Students study engineering subjects and practical technical applications.",
                    "Popular branches include Computer Science, Mechanical, Civil, and Electrical Engineering."
                ],
                "example": "A Computer Science B.Tech student can develop software applications and work on artificial intelligence projects."
            },

            "Python": {
                "aliases": ["python", "python programming", "python language"],
                "intro": "Python is a popular, high-level programming language known for its simple syntax and readability. It is widely used in web development, automation, data analytics, artificial intelligence, and machine learning. Beginners often choose Python because it is relatively easy to learn.",
                "points": [
                    "Python uses simple and readable programming syntax.",
                    "It supports libraries such as NumPy, Pandas, and Flask.",
                    "It is useful for automation, data analysis, and application development."
                ],
                "example": "A data analyst can use Python and Pandas to clean and analyze thousands of sales records."
            },

            "Data Analytics": {
                "aliases": ["data analytics", "data analysis", "data analyst"],
                "intro": "Data Analytics is the process of collecting, cleaning, organizing, and analyzing data to discover useful information. Businesses use it to understand performance, identify trends, and make better decisions. It combines technical tools, logical thinking, and communication skills.",
                "points": [
                    "It involves collecting and cleaning data.",
                    "Common tools include Excel, SQL, Python, and Power BI.",
                    "It helps organizations make data-driven decisions."
                ],
                "example": "An analyst can examine monthly sales data to identify the company's best-selling products."
            },

            "NumPy": {
                "aliases": ["numpy", "numerical python"],
                "intro": "NumPy is a Python library used for numerical computing. It provides powerful arrays and mathematical functions that make calculations faster and easier. It is especially useful in data analytics, scientific computing, statistics, and machine learning.",
                "points": [
                    "It provides powerful one-dimensional and multidimensional arrays.",
                    "It supports mathematical and statistical operations.",
                    "It works efficiently with large numerical datasets."
                ],
                "example": "A student can use NumPy to calculate the average marks of 500 students."
            },

            "Pandas": {
                "aliases": ["pandas", "python pandas library"],
                "intro": "Pandas is a Python library designed for data manipulation and analysis. It provides useful structures such as Series and DataFrames. Analysts use it to clean datasets, handle missing values, filter records, and summarize information.",
                "points": [
                    "It provides Series and DataFrame data structures.",
                    "It can clean, filter, and transform datasets.",
                    "It supports CSV, Excel, and other data formats."
                ],
                "example": "A data analyst can use Pandas to remove duplicate records from a customer dataset."
            },

            "Power BI": {
                "aliases": ["power bi", "powerbi", "microsoft power bi"],
                "intro": "Power BI is Microsoft's business intelligence and data visualization platform. It helps users transform raw data into interactive dashboards and reports. Organizations use it to monitor business performance and understand important trends through visual insights.",
                "points": [
                    "It creates interactive dashboards and reports.",
                    "It connects with Excel, databases, and other data sources.",
                    "It supports data transformation using Power Query."
                ],
                "example": "A company can use Power BI to display monthly revenue, expenses, and sales performance."
            },

            "SQL": {
                "aliases": ["sql", "structured query language"],
                "intro": "SQL stands for Structured Query Language. It is used to communicate with relational databases. Users can retrieve, insert, update, and delete information using SQL commands. It is an essential skill for database management and data analytics.",
                "points": [
                    "SELECT retrieves information from database tables.",
                    "INSERT, UPDATE, and DELETE modify stored records.",
                    "JOIN combines information from multiple tables."
                ],
                "example": "A data analyst can use SQL to find the top ten highest-selling products."
            },

            "Excel": {
                "aliases": ["excel", "microsoft excel", "ms excel"],
                "intro": "Microsoft Excel is a spreadsheet application used to organize, calculate, analyze, and visualize data. It provides formulas, functions, charts, and pivot tables. It is widely used in education, business, accounting, and data analytics.",
                "points": [
                    "It organizes information using rows and columns.",
                    "It provides formulas, charts, and PivotTables.",
                    "It helps users perform calculations and analyze data."
                ],
                "example": "A shop owner can use Excel to calculate monthly sales and expenses."
            },

            "Machine Learning": {
                "aliases": ["machine learning", "ml"],
                "intro": "Machine Learning is a branch of artificial intelligence that enables computers to learn patterns from data and make predictions. Instead of programming every rule manually, developers train models using examples and algorithms.",
                "points": [
                    "It learns patterns from historical data.",
                    "It includes supervised and unsupervised learning.",
                    "It is used for predictions, recommendations, and classification."
                ],
                "example": "An email service can use machine learning to identify and filter spam messages."
            },

            "Artificial Intelligence": {
                "aliases": ["artificial intelligence", "ai"],
                "intro": "Artificial Intelligence is a field of computer science focused on creating systems that perform tasks requiring human-like intelligence. These systems can understand information, recognize patterns, generate content, and support decision-making.",
                "points": [
                    "AI can process information and identify patterns.",
                    "It includes machine learning and natural language processing.",
                    "It is used in chatbots, healthcare, education, and automation."
                ],
                "example": "A chatbot can use AI to understand a question and generate a helpful response."
            },

            "DSA": {
                "aliases": ["dsa", "data structures and algorithms", "data structure"],
                "intro": "Data Structures and Algorithms help programmers organize information and solve computational problems efficiently. Data structures define how information is stored, while algorithms describe the steps used to process it.",
                "points": [
                    "Common structures include arrays, stacks, queues, and trees.",
                    "Algorithms include searching and sorting techniques.",
                    "Time and space complexity help measure efficiency."
                ],
                "example": "A search algorithm helps an application find a particular student record quickly."
            },

            "Java": {
                "aliases": ["java", "java programming"],
                "intro": "Java is a popular, object-oriented programming language used to build applications across different platforms. It is known for its structured programming approach, large ecosystem, and portability through the Java Virtual Machine.",
                "points": [
                    "Java supports object-oriented programming.",
                    "It runs on systems with a compatible Java Virtual Machine.",
                    "It is used in enterprise software and Android-related development."
                ],
                "example": "A developer can use Java to create a banking application."
            },

            "C Programming": {
                "aliases": ["c programming", "c language", "programming in c"],
                "intro": "C is a general-purpose programming language widely used for learning programming fundamentals and developing system software. It provides control over memory and hardware-related operations, making it important in computer science.",
                "points": [
                    "C supports functions, loops, arrays, and pointers.",
                    "It is commonly used in system-level programming.",
                    "It helps students understand programming fundamentals."
                ],
                "example": "A student can write a C program to calculate the average marks of a class."
            },

            "HTML": {
                "aliases": ["html", "hypertext markup language"],
                "intro": "HTML stands for HyperText Markup Language. It provides the basic structure of web pages using elements such as headings, paragraphs, images, links, and forms. Browsers interpret HTML to display website content.",
                "points": [
                    "HTML structures the content of web pages.",
                    "It uses elements and tags.",
                    "It works with CSS and JavaScript."
                ],
                "example": "A developer uses HTML to create the heading and contact form of a website."
            },

            "CSS": {
                "aliases": ["css", "cascading style sheets"],
                "intro": "CSS stands for Cascading Style Sheets. It controls the appearance and layout of web pages. Developers use it to manage colors, fonts, spacing, animations, and responsive designs across different screen sizes.",
                "points": [
                    "CSS controls colors, fonts, and spacing.",
                    "It supports layouts using Flexbox and Grid.",
                    "Media queries help create responsive websites."
                ],
                "example": "CSS can make a website display properly on both laptops and mobile phones."
            },

            "JavaScript": {
                "aliases": ["javascript", "js programming"],
                "intro": "JavaScript is a programming language that makes websites interactive and dynamic. It can respond to user actions, validate forms, update page content, and communicate with servers. It is also used for backend development.",
                "points": [
                    "It adds interactivity to websites.",
                    "It supports frontend and backend development.",
                    "It works with frameworks such as React and Node.js."
                ],
                "example": "JavaScript can validate a login form before sending information to a server."
            },

            "Flask": {
                "aliases": ["flask", "python flask"],
                "intro": "Flask is a lightweight Python web framework used to build websites, APIs, and backend applications. It provides routing and request handling while allowing developers to add only the features their projects require.",
                "points": [
                    "It is a lightweight Python framework.",
                    "It supports routes, templates, and APIs.",
                    "It is suitable for small and medium-sized applications."
                ],
                "example": "A student can use Flask to create a chatbot website with a Python backend."
            },

            "DBMS": {
                "aliases": ["dbms", "database management system"],
                "intro": "DBMS stands for Database Management System. It is software used to store, organize, retrieve, and manage information. It helps applications maintain structured data while supporting security, consistency, and controlled access.",
                "points": [
                    "It stores and manages organized information.",
                    "It supports operations such as insert, update, and delete.",
                    "Examples include MySQL, PostgreSQL, and Oracle Database."
                ],
                "example": "A college uses a DBMS to maintain student details, attendance, and examination records."
            },

            "Operating System": {
                "aliases": ["operating system", "os"],
                "intro": "An Operating System is system software that manages computer hardware and provides services to applications. It handles memory, processes, files, and devices, allowing users to interact with a computer efficiently.",
                "points": [
                    "It manages memory and running processes.",
                    "It controls files and hardware devices.",
                    "Examples include Windows, Linux, macOS, and Android."
                ],
                "example": "Windows allows users to open applications, manage files, and connect printers."
            },

            "Computer Networks": {
                "aliases": ["computer networks", "networking", "computer networking"],
                "intro": "Computer Networking connects computers and devices so they can communicate and share information. Networks use communication technologies and protocols to transfer data between devices over local or global connections.",
                "points": [
                    "LAN and WAN are common network types.",
                    "Protocols define how devices communicate.",
                    "Routers and switches help connect network devices."
                ],
                "example": "A college Wi-Fi network allows students to access the internet using their laptops."
            },

            "Cloud Computing": {
                "aliases": ["cloud computing", "cloud"],
                "intro": "Cloud Computing provides computing services such as storage, databases, servers, and software over the internet. It allows organizations to use resources without maintaining all their own physical infrastructure.",
                "points": [
                    "It provides computing resources over the internet.",
                    "It supports flexible scaling and remote access.",
                    "Examples include Google Cloud, AWS, and Microsoft Azure."
                ],
                "example": "A company can store application files on cloud storage instead of a local computer."
            },

            "BigQuery": {
                "aliases": ["bigquery", "google bigquery", "big query"],
                "intro": "Google BigQuery is a cloud-based data warehouse designed for analyzing large datasets using SQL. It helps analysts run queries, explore information, and generate insights without managing traditional database infrastructure.",
                "points": [
                    "It supports SQL-based data analysis.",
                    "It can process large datasets.",
                    "It integrates with Google Cloud data services."
                ],
                "example": "An analyst can query millions of sales records to calculate yearly revenue."
            },

            "Git": {
                "aliases": ["git", "version control"],
                "intro": "Git is a distributed version control system used to track changes in source code. It allows developers to save project versions, create branches, compare changes, and collaborate while maintaining a history of development.",
                "points": [
                    "It tracks changes in project files.",
                    "It supports branches and merging.",
                    "It helps developers collaborate safely."
                ],
                "example": "A developer can commit code changes before adding a new feature to a project."
            },

            "GitHub": {
                "aliases": ["github", "git hub"],
                "intro": "GitHub is an online platform for hosting Git repositories and collaborating on software projects. Developers use it to share code, manage issues, review changes, and showcase their work through public or private repositories.",
                "points": [
                    "It hosts software repositories online.",
                    "It supports collaboration through pull requests and issues.",
                    "It helps developers build a project portfolio."
                ],
                "example": "A student can upload a Python project to GitHub and share its repository link."
            },

            "Cybersecurity": {
                "aliases": ["cybersecurity", "cyber security", "information security"],
                "intro": "Cybersecurity focuses on protecting computers, networks, applications, and information from digital threats. It uses security practices and technologies to reduce unauthorized access, data theft, malware infections, and other cyber risks.",
                "points": [
                    "It protects systems and sensitive information.",
                    "It includes encryption, authentication, and security monitoring.",
                    "Strong passwords and updates improve security."
                ],
                "example": "Two-factor authentication helps protect an online account even if its password is exposed."
            },

            "Internet": {
                "aliases": ["internet", "world wide web", "www"],
                "intro": "The Internet is a global network of connected computer systems that communicate using standard protocols. It enables services such as websites, email, video calls, online learning, and digital communication across the world.",
                "points": [
                    "It connects networks and devices worldwide.",
                    "It uses protocols such as TCP/IP.",
                    "It supports communication and information sharing."
                ],
                "example": "A student can attend an online class using an internet connection."
            },

            "Website Development": {
                "aliases": ["website development", "web development", "web designing"],
                "intro": "Website Development is the process of creating and maintaining websites. It involves designing the user interface, building frontend functionality, connecting backend services, and managing data to provide useful online experiences.",
                "points": [
                    "Frontend technologies include HTML, CSS, and JavaScript.",
                    "Backend technologies include Python, Flask, and Node.js.",
                    "Testing and responsive design improve website quality."
                ],
                "example": "A developer can build an online clothing store with product pages and a shopping cart."
            },

            "API": {
                "aliases": ["api", "application programming interface"],
                "intro": "An API is a set of rules that allows different software applications to communicate. It enables one application to request data or services from another system through defined endpoints and formats.",
                "points": [
                    "APIs connect different software applications.",
                    "REST APIs commonly use HTTP methods.",
                    "JSON is a popular format for exchanging data."
                ],
                "example": "A weather application can use an API to retrieve current weather information."
            },

            "Statistics": {
                "aliases": ["statistics", "statistical analysis"],
                "intro": "Statistics is the study of collecting, organizing, analyzing, and interpreting data. It helps people understand patterns, compare results, and make decisions based on evidence rather than assumptions.",
                "points": [
                    "Mean, median, and mode describe central tendency.",
                    "Standard deviation measures data variation.",
                    "Statistics supports research and data analytics."
                ],
                "example": "A teacher can calculate the average marks of students to understand class performance."
            },

            "Data Visualization": {
                "aliases": ["data visualization", "data visualisation", "data charts"],
                "intro": "Data Visualization presents information through visual formats such as charts, graphs, and dashboards. It makes complex datasets easier to understand and helps people identify comparisons, patterns, and trends quickly.",
                "points": [
                    "Common visuals include bar charts and line charts.",
                    "Dashboards summarize important business metrics.",
                    "Good visual design improves communication."
                ],
                "example": "A line chart can show how a company's sales change every month."
            },

            "Resume": {
                "aliases": ["resume", "cv", "curriculum vitae"],
                "intro": "A resume is a professional document that summarizes a candidate's education, skills, projects, experience, and achievements. It helps recruiters understand whether an applicant is suitable for a particular job or internship.",
                "points": [
                    "Include relevant education and technical skills.",
                    "Describe projects using clear achievements.",
                    "Keep the layout readable and professional."
                ],
                "example": "A BCA student can list Python, SQL, and a data analytics project on a resume."
            },

            "Interview": {
                "aliases": ["interview", "job interview", "technical interview"],
                "intro": "An interview is a conversation in which an employer evaluates a candidate's knowledge, communication, experience, and suitability for a role. Preparation helps candidates explain their skills and answer questions confidently.",
                "points": [
                    "Understand the company and job description.",
                    "Practise technical and common HR questions.",
                    "Explain projects and skills honestly."
                ],
                "example": "A student applying for a Python internship may be asked to explain variables, loops, and a project."
            },

            "Internship": {
                "aliases": ["internship", "internships", "intern"],
                "intro": "An internship is a temporary work or learning opportunity that helps students gain practical experience in a professional environment. It allows learners to apply academic knowledge, develop workplace skills, and understand industry expectations.",
                "points": [
                    "Internships provide practical project experience.",
                    "They help develop communication and teamwork skills.",
                    "They can strengthen a fresher's resume."
                ],
                "example": "A BCA student can complete a data analytics internship and build a portfolio project."
            },

            "College": {
                "aliases": ["college", "college life", "university college"],
                "intro": "A college is an educational institution where students pursue higher education and develop academic, technical, and personal skills. College life includes classroom learning, practical assignments, projects, teamwork, and career preparation.",
                "points": [
                    "Students attend lectures and practical sessions.",
                    "Projects and activities improve practical skills.",
                    "Career services can support internships and placements."
                ],
                "example": "A computer applications student can learn programming in class and apply it through a college project."
            },

            "Laptop": {
                "aliases": ["laptop", "computer laptop"],
                "intro": "A laptop is a portable computer that combines a display, keyboard, battery, and processing hardware in one device. It is used for studying, programming, office work, communication, entertainment, and many professional tasks.",
                "points": [
                    "It contains a processor, memory, and storage.",
                    "RAM affects multitasking performance.",
                    "SSD storage generally provides faster file access than traditional HDDs."
                ],
                "example": "A student can use a laptop to write Python code in Visual Studio Code."
            },

            "Artificial Neural Network": {
                "aliases": ["artificial neural network", "neural network"],
                "intro": "An Artificial Neural Network is a machine learning model inspired by how biological neurons process information. It uses connected computational units and learned weights to identify patterns and perform tasks such as classification and prediction.",
                "points": [
                    "It contains input, hidden, and output layers.",
                    "Training adjusts weights to reduce prediction errors.",
                    "It is used in image and speech recognition."
                ],
                "example": "A neural network can learn to recognize handwritten digits from labelled images."
            },

            "React": {
                "aliases": ["react", "react js", "reactjs"],
                "intro": "React is a JavaScript library used to build interactive user interfaces. It organizes interfaces into reusable components and updates the displayed content when application data changes.",
                "points": [
                    "It uses reusable components.",
                    "It supports state and props.",
                    "It is commonly used for modern frontend applications."
                ],
                "example": "A developer can build a shopping cart interface using reusable React components."
            },

            "Node.js": {
                "aliases": ["node.js", "node js", "nodejs"],
                "intro": "Node.js is a JavaScript runtime that allows developers to execute JavaScript outside a web browser. It is widely used to create backend services, APIs, and real-time applications.",
                "points": [
                    "It runs JavaScript on the server side.",
                    "It uses an event-driven, non-blocking model.",
                    "It is often used with Express for backend development."
                ],
                "example": "A developer can create a login API using Node.js and Express."
            },

            "Google Cloud": {
                "aliases": ["google cloud", "gcp", "google cloud platform"],
                "intro": "Google Cloud is a cloud computing platform that provides infrastructure, storage, databases, analytics, and artificial intelligence services. Developers and organizations use it to build, deploy, and manage applications and data solutions.",
                "points": [
                    "It offers services such as BigQuery and Cloud Storage.",
                    "It supports scalable application deployment.",
                    "It provides tools for data analytics and AI."
                ],
                "example": "A data analyst can use BigQuery on Google Cloud to analyze a large dataset."
            },

            "Machine Learning Model": {
                "aliases": ["ml model", "machine learning model"],
                "intro": "A Machine Learning Model is a system trained on data to recognize patterns and make predictions or decisions. Its performance depends on the quality of training data, suitable algorithms, and proper evaluation.",
                "points": [
                    "Models learn from training data.",
                    "Testing data helps evaluate performance.",
                    "Models can perform classification or regression."
                ],
                "example": "A model can predict house prices using features such as location and area."
            },

            "Time Management": {
                "aliases": ["time management", "time management skills"],
                "intro": "Time Management is the practice of planning and organizing tasks to use available time effectively. It helps students and professionals balance responsibilities, reduce unnecessary delays, and make consistent progress toward goals.",
                "points": [
                    "Prioritize important tasks.",
                    "Break large goals into smaller activities.",
                    "Use schedules and regular progress reviews."
                ],
                "example": "A student can reserve one hour daily for Python practice and another hour for college assignments."
            },

            "Communication Skills": {
                "aliases": ["communication skills", "communication"],
                "intro": "Communication Skills are the abilities used to share information, ideas, and thoughts clearly. They include speaking, listening, writing, and understanding others, helping people work effectively in academic and professional environments.",
                "points": [
                    "Speak clearly and organize your ideas.",
                    "Listen carefully before responding.",
                    "Use professional and understandable language."
                ],
                "example": "A student can explain their final-year project clearly during a placement interview."
            }

        }

    def normalize(self, text):
        text = str(text).lower().strip()
        text = re.sub(r"[^a-z0-9.+# ]", " ", text)
        return re.sub(r"\s+", " ", text)

    def generate_questions(self):

        templates = [
            "what is {}",
            "explain {}",
            "tell me about {}",
            "describe {}",
            "how does {} work",
            "why is {} important",
            "what are the features of {}",
            "what are the benefits of {}",
            "what are the uses of {}",
            "how can i learn {}",
            "give me an example of {}",
            "explain {} in simple words",
            "explain {} for beginners",
            "teach me {}",
            "i want to understand {}",
            "help me learn {}",
            "give information about {}",
            "what do you mean by {}",
            "what is the importance of {}",
            "how is {} used",
            "{} kya hai",
            "{} ke baare mein batao",
            "{} kaise kaam karta hai",
            "{} kyu important hai",
            "{} ka example do"
        ]

        questions = {}

        for topic, data in self.knowledge.items():

            for alias in [topic] + data["aliases"]:

                for template in templates:
                    question = template.format(alias)
                    questions[self.normalize(question)] = topic

        return questions

    def format_answer(self, topic):

        data = self.knowledge[topic]

        answer = (
            f"❤️ Sandhu ji! **{topic}**\n\n"
            f"{data['intro']}\n\n"
            f"**📌 3 Important Points:**\n"
        )

        for index, point in enumerate(data["points"], start=1):
            answer += f"{index}. {point}\n"

        answer += (
            f"\n**💡 Real-Life Example:**\n"
            f"{data['example']}\n"
        )

        return answer

    def find_topic(self, message):

        text = self.normalize(message)

        # First priority: exact topic and alias matching.
        # Longest aliases are checked first to avoid incorrect matches.
        aliases = []

        for topic, data in self.knowledge.items():
            for alias in [topic] + data["aliases"]:
                aliases.append((self.normalize(alias), topic))

        aliases.sort(key=lambda item: len(item[0]), reverse=True)

        for alias, topic in aliases:

            pattern = r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])"

            if re.search(pattern, text):
                return topic

        # Second priority: known generated question patterns.
        if text in self.questions:
            return self.questions[text]

        return None

    def get_response(self, message, previous_user_message=None):

        if not message or not str(message).strip():
            return "❤️ Sandhu ji! Please enter a question so I can help you."

        text = self.normalize(message)

        # Greetings
        greetings = ["hi", "hello", "hey", "good morning",
                      "good afternoon", "good evening"]

        if text in greetings:
            return (
                "❤️ Sandhu ji! Hello! 😊 I am SANDHU AI BOT. "
                "I can help you with programming, Data Analytics, "
                "college subjects, technology, and many more topics. "
                "What would you like to learn today?"
            )

        if text in ["thanks", "thank you", "thankyou"]:
            return "❤️ Sandhu ji! You're welcome! 😊 Keep learning and keep growing."

        if text in ["bye", "goodbye", "see you"]:
            return "❤️ Sandhu ji! Goodbye! 👋 Have a great day and keep learning!"

        # Use the previous question for short follow-ups.
        topic = self.find_topic(message)

        if not topic and previous_user_message:
            topic = self.find_topic(previous_user_message)

        if topic:
            return self.format_answer(topic)

        # Do not guess a different topic when the question is unclear.
        return (
            "❤️ Sandhu ji! I want to give you the correct answer. 😊\n\n"
            "I could not confidently identify the topic in your question. "
            "Please mention the exact topic, such as BCA, B.Tech, Python, "
            "Data Analytics, SQL, NumPy, or Power BI.\n\n"
            "I will explain it in simple English with 3 important points "
            "and a real-life example."
        )


engine = KnowledgeEngine()
