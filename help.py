html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Услуги психотерапия.by</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #e38d2b;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .breadcrumbs {
            font-family: Arial, sans-serif;
            margin-bottom: 20px;
        }
        .breadcrumbs a {
            color: #007BFF;
            text-decoration: none;
        }
        .breadcrumbs a:hover {
            text-decoration: underline;
        }
        .breadcrumbs span {
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>Услуги</h1>
    </header>
    <main>
        <div class="breadcrumbs">
            <a href="index.html">Главная</a> <a>/</a> <a href="help.html">Предоставляемые услуги</a>
        </div>
        <div class="content">
            <pre> 
                бла бла бла
                блаблабла
            </pre>
        </div>
    </main>
    <footer>
        <p>Gera_Regen</p>
    </footer>

    <script>
        // Проверка, зарегистрирован ли пользователь
        const user = JSON.parse(localStorage.getItem('user'));

        if (!user) {
            // Если пользователь не зарегистрирован, перенаправляем на страницу регистрации
            window.location.href = 'reg_and_login.html';
        }
    </script>
</body>
</html>
"""

# Записываем HTML-код в файл
with open("help.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-файл успешно создан!")