<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mass Portfolio</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
    <link rel="stylesheet" href="/style.css">
    
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    
</head>

<body>
    <header class="header">
        
        <a href="#" class="logo">Mass Portfolio</a>


        <nav class="navbar">
            <a href="#home" class="active">Home</a>
            <a href="#about">About </a>
            <a href="#services">Services </a>
            <a href="#portfolio">Portfolio</a>
            <a href="#contact">Contact </a>
        </nav>

        <div class="bx bx-moon" id="darkMode-icon"></div>
        <div class="bx bx-menu" id="menu-icon"> </div>

    </header>


   
    <section class="home" id="home">
        <div class="home-content">
            <h3>hello , I am </h3>
            <h1>Vignesh G </h1>
            <p>The mind ventures into good new temporary networks. Listing allows discovering new steps. Commonly the list of a new venture </p>


            <div class="social-media">
                <a href="#"><i class='bx bxl-facebook'></i></a>
                <a href="#"><i class='bx bxl-github'></i></a>
                <a href="#"><i class='bx bxl-linkedin-square'></i></a>
                <a href="#"><i class='bx bxl-twitter'></i></a>
            </div>
            <a href="#" class="btn">Download cv</a>

        </div>

        <div class="profession-container">
            <div class="profession-box">
                <div class="profession" style="--i:0;">
                    <i class='bx bxs-camera'></i>
                    <h3>Web Developer </h3>
                </div>
                <div class="profession" style="--i:1">
                    <i class='bx bxs-video-recording'></i>
                    <h3>Web Developer</h3>
                    
                </div>
                <div class="profession" style="--i:2">
                    <i class='bx bxs-palette'></i>
                    <h3>Web Developer</h3>
                </div>
                <div class="profession" style="--i:3">
                    <i class='bx bx-message-dots'></i>
                    <h3>Web Developer</h3>
                </div>

                <div class="circle"></div>
            </div>
            <div class="overlay"></div>
        </div>
        <div class="home-img">
            <img src="" alt="mass's ">
        </div>


    </section>


    
    <section class="about" id="about">
        <div class="about-img">
            <img src="/img/1.jpeg" alt="">


        </div>
        <div class="about-content">
            <h2 class="heading">About <span>me</span></h2>
            <h3>Who I am </h3>
            <p>I'm a I'm a Sophomore who is crazy about convention, consistency, and constraints. I am deeply passionate about competitive Programming and contributing to communities. who is crazy about convention, consistency, and constraints. I am deeply passionate about
                competitive Programming and contributing to communities.
                <br>


                - 🧠 Coding is my passion. <br>
                - ⚡ Fun fact I can touch type at 90+ wpm. <br>
                <br>
                Apart from Tech, I love to do public speaking and deliver speeches . Moreover, I am good at learning and
                always open to challenges.
            </p>
            <a href="#" class="btn">Read more</a>
        </div>
    </section>


    

    <section class="services" id="services">
        <h2 class="heading">My <span>Skills</span></h2>

        <div class="services-container">
            <div class="services-box">
                <i class='bx bxl-html5'></i>
                <h3>HTML & CSS</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="#" class="btn">Read more</a>
            </div>

            <div class="services-box">
                <i class='bx bxl-javascript'></i>
                <h3>JAVASCRIPT</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="#" class="btn">Read more</a>
            </div>
            <div class="services-box">
                <i class='bx bxl-nodejs'></i>
                <h3>NODE JS</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="#" class="btn">Read more</a>
            </div>
            <div class="services-box">
                <i class='bx bxl-react'></i>
                <h3>REACT JS</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="#" class="btn">Read more</a>
            </div>
            <div class="services-box">
                <i class='bx bxl-c-plus-plus'></i>
                <h3>C++</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="#" class="btn">Read more</a>
            </div>
            <div class="services-box">
                <i class='bx bxl-mongodb'></i>
                <h3>MONGO DB</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate cum, temporibus explicabo,
                    consectetur qui rem corporis in dicta ducimus fuga est aspernatur omnis! </p>
                <a href="" class="btn" id="btn" onclick="readtext()">Read more</a>
            </div>
        </div>
    </section>

    
    <section class="portfolio" id="portfolio">
        <h2 class="heading">Latest <span>Project</span></h2>
        <div class="portfolio-container">
            <div class="portfolio-box">
                <img src="/img/3.png " alt="">

                <div class="portfolio-layer">
                    <h4>Landing Page</h4>
                    <p>A landing page is a standalone web page designed for a specific marketing or advertising campaign, with the primary goal of driving visitor action, such as capturing leads or making sales.</p>
                    <a href="#"><i class='bx bx-plus-medical'></i></a>
                </div>
            </div>
            <div class="portfolio-box">
                <img src="/img/2.png " alt="">
                <div class="portfolio-layer">
                    <h4>Calculator</h4>
                    <p>Calculator using HTML, CSS and JAVASCRIPT</p>
                    <a href="#"><i class='bx bx-plus-medical'></i></a>
                </div>
            </div>
   
            <div class="portfolio-box">
                <img src="/img/4.png" alt="">
                <div class="portfolio-layer">
                    <h4>TIC TAE TOE WEB GAME</h4>
                    <p> where two players take turns marking spaces with X and O symbols to achieve a winning pattern.</p>
                    <a href="#"><i class='bx bx-link-external'></i></a>
                </div>

            </div>

        </div>
    </section>

    
    <div class="testimonial-container">
        <h2 class="heading">MY <span>Socials</span></h2>
        <div class="testimonial-wrapper">
            <div class="testimonial-box mySwiper">
                <div class="testimonial-content swiper-wrapper">
                    <div class="testimonial-slide swiper-slide">
                        
                        <i class='bx bxl-linkedin-square' > </i>
                        
                        <h3>LinkedIn </h3>
                       
                    </div>
                    <div class="testimonial-slide swiper-slide">

                        
                        <i class='bx bxl-twitter' ></i>
                        <h3>Twitter</h3>
                       
                    </div>
                    <div class="testimonial-slide swiper-slide">
                      
                        <i class='bx bxl-github' ></i>
                        <h3>Github</h3>
                        
                    </div>
                </div>
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
                <div class="swiper-scrollbar"></div>
                <div class="swiper-pagination"></div>

            </div>
        </div>
    </div>

   

    <section class="contact" id="contact">
        <h2 class="heading">Contact <span>Me!</span></h2>

        <form action="#">
            <div class="input-box">
                <input type="text" placeholder="Full name">
                <input type="email" placeholder="Enter E-Mail">
            </div>
            <div class="input-box">
                <input type="Number" placeholder="Mobile number">
                <input type="email" placeholder="email subject">
            </div>
            <textarea name="" id="" cols="30" rows="10">Yours Message</textarea>
            <input type="submit " value="send message " class="btn">
        </form>
    </section>

    
    <footer class="footer">
        <div class="footer-text">
            <p>Copyright &copy; 2024 by Mass Vignesh | All Rights Reserved</p>
        </div>
        <div class="footer-iconTop">
            <a href="#home"><i class='bx bx-up-arrow-alt'></i></a>
        </div>
    </footer>

   
    <script src="https://unpkg.com/scrollreveal"></script>

    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>

    <script src="/index.js">
    </script>
   
</body>

</html>
