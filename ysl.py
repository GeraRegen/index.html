
html_content='''

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тревога</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        
        .main-content {
            display: flex;
            flex-grow: 1;
            flex-wrap: wrap;
        }
        
        .image-block {
            width: 293px;
            height: 524px;
            flex-shrink: 0;
            background-color: #ddd;
            margin: 20px;
        }
        
        .image-block img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .content-block {
            flex-grow: 1;
            padding: 20px;
            min-width: 300px;
        }
        
        .info-container_1 {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-image: url('about2.jpg');
            background-size: cover;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #000;
            text-align: justify;
        }
        
        .info-container_1 h2 {
            color: #000;
            margin-top: 0;
            text-align: center;
        }
        
        .cloud-glava {
            width: 100%;
            background-image: url('oblako.jpg');
            background-size: cover;
            border-radius: 0 0 20px 20px;
            padding: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        
        nav {
            background-color: #333;
            padding: 10px;
            text-align: center;
        }
        
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        
        nav a:hover {
            text-decoration: underline;
        }
        
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px;
            width: 100%;
        }
        
        img {
            max-width: 100%;
            height: auto;
            margin: 10px auto;
            display: block;
        }
        
        pre {
            white-space: pre-wrap;
            font-family: Arial, sans-serif;
            margin: 10px auto;
            max-width: 800px;
        }
        
        .row {
            display: flex;
            width: 100%;
            flex-wrap: wrap;
        }
        
        @media (max-width: 768px) {
            .row {
                flex-direction: column;
            }
            
            .image-block {
                width: 100%;
                height: auto;
                max-height: 400px;
                margin: 0 0 20px 0;
            }
            
            .content-block {
                width: 100%;
                padding: 10px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="cloud-glava">
            <h1>Психологическая помощь ВЫХОД ЕСТЬ!</h1>
            <img src="page_psih2.png" alt="Логотип компании">
        </div>
    </header>

    <nav>
        <a href="index.html">Главная</a>
    </nav>
    
    <div class="main-content">
        <!-- Первый ряд: слева картинка, справа контент -->
        <div class="row">
            <div class="image-block">
                <a href='nimber.html'>
                    <img src="or_ysl.jpg" alt="Первое изображение">
                </a>
            </div>
            
            <div class="content-block">
                <div class="info-container_1" style="background-color: #ffffff;">
                    <h2>Заголовок контента</h2>
                    <p>Это основной контент вашей страницы. Здесь вы можете разместить любой текст, изображения или другие элементы.</p>
                    <p>Фон этого контейнера можно изменить, добавив CSS-свойство background-color или background-image.</p>
                </div>
            </div>
        </div>
        
        <!-- Второй ряд: слева контент, справа картинка -->
        <div class="row">
            <div class="content-block">
                <div class="info-container_1" style="background-color: #f0f0f0;">
                    <h2>Второй блок контента</h2>
                    <p>Здесь может быть дополнительная информация. Этот контейнер теперь слева, а справа будет вторая картинка.</p>
                </div>
            </div>
            
            <div class="image-block">
                <a href='nimber.html'>
                    <img src="or_ysl_2.jpg" alt="Второе изображение">
                </a>
            </div>
        </div>
    </div>
    
    <div class="row">
            <div class="image-block">
                <a href='nimber.html'>
                    <img src="or_ysl_3.jpg" alt="Первое изображение">
                </a>
            </div>
            
            <div class="content-block">
                <div class="info-container_1" style="background-color: #ffffff;">
                    <h2>Заголовок контента</h2>
                    <p>Это основной контент вашей страницы. Здесь вы можете разместить любой текст, изображения или другие элементы.</p>
                    <p>Фон этого контейнера можно изменить, добавив CSS-свойство background-color или background-image.</p>
                </div>
            </div>
    </div>

    <footer>
        <img src="page_psih2.png" alt="фото">
        <pre>
            ООО «Медико-диагностический центр «Выход Есть!» - это многопрофильное лечебно-профилактическое учреждение, которое имеет современную материально-техническую базу,
            оказывает платные медицинские услуги и осуществляет консультации высококвалифицированных специалистов.
        </pre>
        <pre>
            Обращаем ваше внимание на то, что данный интернет-сайт носит исключительно информационный характер и ни при каких условиях не является публичной офертой,
            определяемой положениями ст. 405 Гражданского кодекса Республики Беларусь.
            Для получения подробной информации о наличии и стоимости указанных услуг, пожалуйста, обращайтесь к администраторам клиники.
        </pre>
    </footer>
</body>
</html>

'''

with open("ysl.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-файл успешно создан!")