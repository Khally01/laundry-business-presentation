<!DOCTYPE html>
<html lang="mn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Угаалгын бизнес танилцуулга</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            overflow-x: hidden;
        }
        
        .presentation-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .slide {
            min-height: 100vh;
            padding: 40px;
            display: none;
            animation: slideIn 0.5s ease-in-out;
        }
        
        .slide.active {
            display: block;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .slide-header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 3px solid #667eea;
        }
        
        .slide-title {
            font-size: 2.5em;
            color: #667eea;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .slide-subtitle {
            font-size: 1.2em;
            color: #666;
            font-weight: 300;
        }
        
        .content {
            line-height: 1.8;
            font-size: 1.1em;
        }
        
        .highlight-box {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .hero-image {
            width: 100%;
            max-width: 400px;
            height: 250px;
            margin: 20px auto;
            background: url('https://images.unsplash.com/photo-1517677208171-0bc6725a3e60?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            display: block;
            background-color: #f0f0f0;
        }
        
        .business-image {
            width: 100%;
            max-width: 350px;
            height: 200px;
            margin: 15px auto;
            background: url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            display: block;
            background-color: #f0f0f0;
        }
        
        .laundromat-image {
            width: 100%;
            max-width: 500px;
            height: 300px;
            margin: 20px auto;
            background: url('https://images.unsplash.com/photo-1604335399105-a0c585fd81a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            display: block;
            background-color: #f0f0f0;
        }
        
        .money-image {
            width: 100%;
            max-width: 300px;
            height: 180px;
            margin: 15px auto;
            background: url('https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            display: block;
            background-color: #f0f0f0;
        }
        
        .growth-image {
            width: 100%;
            max-width: 400px;
            height: 220px;
            margin: 20px auto;
            background: url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            display: block;
            background-color: #f0f0f0;
        }
        
        .team-image {
            width: 100%;
            max-width: 350px;
            height: 200px;
            margin: 15px auto;
            background: url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            display: block;
            background-color: #f0f0f0;
        }
        
        .success-image {
            width: 100%;
            max-width: 400px;
            height: 230px;
            margin: 20px auto;
            background: url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover no-repeat;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            display: block;
            background-color: #f0f0f0;
        }
        
        /* Fallback content for images */
        .hero-image::after {
            content: '🌀 WASHING MACHINES';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 15px;
        }
        
        .business-image::after {
            content: '🏢 BUSINESS SPACE';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            border-radius: 15px;
        }
        
        .team-image::after {
            content: '🤝 TEAM COLLABORATION';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 15px;
        }
        
        .laundromat-image::after {
            content: '🌀 PROFESSIONAL LAUNDROMAT';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            border-radius: 15px;
        }
        
        .money-image::after {
            content: '💰 INVESTMENT PLAN';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 15px;
        }
        
        .growth-image::after {
            content: '🚀 BUSINESS GROWTH';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 15px;
        }
        
        .success-image::after {
            content: '🎉 SUCCESS PARTNERSHIP';
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            border-radius: 15px;
        }
        
        /* Make images position relative for absolute positioning of fallback */
        .hero-image, .business-image, .team-image, .laundromat-image, 
        .money-image, .growth-image, .success-image {
            position: relative;
        }
        
        .table-container {
            overflow-x: auto;
            margin: 20px 0;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }
        
        th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
        }
        
        td {
            padding: 15px;
            text-align: center;
            border-bottom: 1px solid #eee;
        }
        
        tr:hover {
            background: #f8f9ff;
        }
        
        .phase-timeline {
            display: flex;
            justify-content: space-between;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        
        .phase {
            flex: 1;
            margin: 10px;
            padding: 25px;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 15px;
            text-align: center;
            position: relative;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .phase::after {
            content: '→';
            position: absolute;
            right: -25px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 2em;
            color: #667eea;
        }
        
        .phase:last-child::after {
            display: none;
        }
        
        .phase-number {
            background: #667eea;
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px;
            font-size: 1.2em;
            font-weight: bold;
        }
        
        .navigation {
            position: fixed;
            bottom: 30px;
            right: 30px;
            display: flex;
            gap: 10px;
            z-index: 1000;
        }
        
        .nav-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 50px;
            cursor: pointer;
            font-size: 1em;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
        
        .nav-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }
        
        .nav-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        
        .slide-counter {
            position: fixed;
            top: 30px;
            right: 30px;
            background: rgba(102, 126, 234, 0.9);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: bold;
            z-index: 1000;
        }
        
        .title-slide {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .title-slide .slide-title {
            color: white;
            font-size: 3.5em;
            margin-bottom: 20px;
        }
        
        .title-slide .slide-subtitle {
            color: rgba(255,255,255,0.9);
            font-size: 1.5em;
        }
        
        .emoji {
            font-size: 1.2em;
        }
        
        .call-to-action {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            margin: 30px 0;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }
        
        .call-to-action h3 {
            font-size: 2em;
            margin-bottom: 15px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }
        
        @media (max-width: 768px) {
            .slide {
                padding: 20px;
            }
            
            .slide-title {
                font-size: 2em;
            }
            
            .phase-timeline {
                flex-direction: column;
            }
            
            .phase::after {
                display: none;
            }
            
            .navigation {
                bottom: 20px;
                right: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="presentation-container">
        <div class="slide-counter">
            <span id="current-slide">1</span> / <span id="total-slides">8</span>
        </div>

        <!-- Slide 1: Title -->
        <div class="slide active title-slide">
            <div class="slide-title">🌀 УГААЛГЫН БИЗНЕС</div>
            <div class="slide-subtitle">Найз гэр бүлүүдийн хамтарсан бизнес төсөл</div>
            <div class="hero-image"></div>
            <div style="margin-top: 20px; font-size: 1.2em;">
                Тэмүүжин • Амраа • Ганбаяр • Эрмүүн
            </div>
        </div>

        <!-- Slide 2: Goal -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">🎯 БИДНИЙ ЗОРИЛГО</div>
            </div>
            <div class="content">
                <div class="highlight-box">
                    <h2 style="text-align: center; margin-bottom: 20px;">
                        <span class="emoji">🏙️</span> Улаанбаатар хотын 21-р хорооноос эхлэн орон даяар угаалгын үйлчилгээний сүлжээ байгуулах
                    </h2>
                </div>
                
                <div class="business-image"></div>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🏢</div>
                        <h3>Анхны салбар</h3>
                        <p>21-р хороонд эхний угаалгын газар</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🌟</div>
                        <h3>Чанартай үйлчилгээ</h3>
                        <p>Орчин үеийн тоног төхөөрөмж</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Өргөжүүлэх</h3>
                        <p>21 аймагт салбар нээх</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 3: Team -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">👥 ХАМТРАГЧ ГЭР БҮЛҮҮД</div>
            </div>
            <div class="content">
                <div class="team-image"></div>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-icon">👨‍👩‍👧‍👦</div>
                        <h3>Тэмүүжин гэр бүл</h3>
                        <p>Туршлагатай ах дүүгийн мэдлэг</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🌀</div>
                        <h3>Амраа гэр бүл</h3>
                        <p>40м² байршил</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔨</div>
                        <h3>Ганбаяр гэр бүл</h3>
                        <p>Дотоод засал чиглэлээр туслах боломжтой</p>
                    </div>
                    <div class="feature-card" style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);">
                        <div class="feature-icon">⭐</div>
                        <h3>Эрмүүн гэр бүл</h3>
                        <p><strong>Урилга хүлээж байна!</strong></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 4: Business Opportunity -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">💡 БИЗНЕСИЙН БОЛОМЖ</div>
            </div>
            <div class="content">
                <div class="laundromat-image"></div>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">40м²</div>
                        <div>Байршилын талбай</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">700K-1M₮</div>
                        <div>Өдрийн орлого</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">21</div>
                        <div>Дүүрэг/Аймаг</div>
                    </div>
                </div>

                <div class="highlight-box">
                    <h3><span class="emoji">✅</span> Бидэнд байгаа давуу тал:</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin: 10px 0;"><span class="emoji">📍</span> <strong>Байршил:</strong> Амраагийн эцэг эх 40м² нэмэлт талбайтай</li>
                        <li style="margin: 10px 0;"><span class="emoji">🎓</span> <strong>Туршлага:</strong> Тэмүүжингийн ах угаалгын бизнес эхлүүлсэн</li>
                        <li style="margin: 10px 0;"><span class="emoji">💰</span> <strong>Орлого:</strong> Өдөрт 700,000-1,000,000₮</li>
                        <li style="margin: 10px 0;"><span class="emoji">🏆</span> <strong>Түлхүүр:</strong> Байршил маш чухал!</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 5: Financial Plan -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">💰 САНХҮҮГИЙН ТӨЛӨВЛӨГӨӨ</div>
            </div>
            <div class="content">
                <div class="highlight-box">
                    <h3 style="text-align: center;">6 сарын хуримтлалын төлөвлөгөө</h3>
                    <p style="text-align: center; font-size: 1.2em;">Гэр бүл тус бүр долоо хоногт $1,000</p>
                </div>

                <div class="money-image"></div>

                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Гэр бүл</th>
                                <th>Долоо хоногт</th>
                                <th>Сард</th>
                                <th>6 сард</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Тэмүүжин</strong></td>
                                <td>$1,000</td>
                                <td>$4,000</td>
                                <td>$24,000</td>
                            </tr>
                            <tr>
                                <td><strong>Амраа</strong></td>
                                <td>$1,000</td>
                                <td>$4,000</td>
                                <td>$24,000</td>
                            </tr>
                            <tr>
                                <td><strong>Ганбаяр</strong></td>
                                <td>$1,000</td>
                                <td>$4,000</td>
                                <td>$24,000</td>
                            </tr>
                            <tr>
                                <td><strong>Эрмүүн</strong></td>
                                <td>$1,000</td>
                                <td>$4,000</td>
                                <td>$24,000</td>
                            </tr>
                            <tr style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                                <td><strong>НИЙТ</strong></td>
                                <td><strong>$4,000</strong></td>
                                <td><strong>$16,000</strong></td>
                                <td><strong>$96,000</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div style="text-align: center; font-size: 1.3em; color: #667eea; font-weight: bold;">
                    ≈ 240,000,000₮ нийт хөрөнгө оруулалт
                </div>
            </div>
        </div>

        <!-- Slide 6: Development Vision -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">🚀 ХӨГЖЛИЙН АЛСЫН ХАРАА</div>
            </div>
            <div class="content">
                <div class="growth-image"></div>
                
                <div class="phase-timeline">
                    <div class="phase">
                        <div class="phase-number">1</div>
                        <h3>Улаанбаатар 21-р хороо</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li>✓ Анхны угаалгын газар нээх</li>
                            <li>✓ Зах зээлийн хэрэгцээ судлах</li>
                            <li>✓ Процесс тогтоох</li>
                        </ul>
                    </div>
                    <div class="phase">
                        <div class="phase-number">2</div>
                        <h3>Нийслэлд өргөжүүлэх</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li>✓ Амжилттай дүүргүүдэд салбар</li>
                            <li>✓ Брэнд танигдах болгох</li>
                            <li>✓ Үйлчилгээний чанар</li>
                        </ul>
                    </div>
                    <div class="phase">
                        <div class="phase-number">3</div>
                        <h3>Орон даяар өргөжүүлэх</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li>✓ 21 аймагт салбар</li>
                            <li>✓ Төрөл бүрийн үйлчилгээ</li>
                            <li>✓ Ажлын байр бий болгох</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 7: Why Now -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">🔥 ЯАГААД ОДОО?</div>
            </div>
            <div class="content">
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-icon">⚡</div>
                        <h3>Боломж</h3>
                        <p>Угаалгын үйлчилгээний хэрэгцээ өсөн нэмэгдэж байна</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📈</div>
                        <h3>Зах зээл</h3>
                        <p>Хотын хүн ам өсөж, амьдралын түвшин дээшилж байна</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">⏰</div>
                        <h3>Хэрэгцээ</h3>
                        <p>Цагийн хомсдол улмаас үйлчилгээ илүүтэй ашиглах болсон</p>
                    </div>
                </div>

                <div class="highlight-box">
                    <h3><span class="emoji">💪</span> Бидний давуу тал:</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
                        <div>
                            <p><span class="emoji">🎓</span> Туршлагатай ах дүүгийн зөвлөгөө</p>
                            <p><span class="emoji">📍</span> Тохиромжтой байршил</p>
                        </div>
                        <div>
                            <p><span class="emoji">🤝</span> Найрсаг хамтрагч нар</p>
                            <p><span class="emoji">💰</span> Хангалттай хөрөнгө босгох боломж</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 8: Call to Action -->
        <div class="slide">
            <div class="slide-header">
                <div class="slide-title">🤝 ЭРМҮҮН ГЭРБҮЛД УРИЛГА</div>
            </div>
            <div class="content">
                <div class="call-to-action">
                    <h3><span class="emoji">🎊</span> Эрмүүн гэр бүл, та нар бидэнтэй нэгдэх үү?</h3>
                    <p style="font-size: 1.2em;">Энэ бол зөвхөн бизнес биш, бидний гэр бүлүүдийн ирээдүйн баталгаа!</p>
                </div>

                <div class="success-image"></div>

                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-icon">💫</div>
                        <h3>Та нарын оролцоо чухал</h3>
                        <p>Найрсаг хамтын ажиллагаа, тэгш эрх ба үр дүн</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📝</div>
                        <h3>Хэрэв орилцохоор шийдвэл</h3>
                        <p>Өнөөдрөөс хуримтлал эхлүүлэх</p>
                    </div>
                </div>

                <div class="highlight-box">
                    <h3>Дараагийн алхамууд:</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px;">
                        <div style="text-align: center;">
                            <div style="font-size: 2em;">1️⃣</div>
                            <p>Өнөөдрөөс хуримтлал эхлүүлэх</p>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 2em;">2️⃣</div>
                            <p>Долоо хоног бүр $1,000</p>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 2em;">3️⃣</div>
                            <p>6 сарын дараа бизнес эхлүүлэх</p>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 2em;">4️⃣</div>
                            <p>Хамтдаа амжилтанд хүрэх</p>
                        </div>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 30px; font-style: italic; font-size: 1.1em;">
                    <span class="emoji">📞</span> Холбоо барих: Тэмүүжин, Амраа, Ганбаяр
                </div>
            </div>
        </div>
    </div>

    <div class="navigation">
        <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">← Өмнөх</button>
        <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Дараах →</button>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        document.getElementById('total-slides').textContent = totalSlides;
        
        function showSlide(n) {
            slides[currentSlide].classList.remove('active');
            currentSlide = (n + totalSlides) % totalSlides;
            slides[currentSlide].classList.add('active');
            
            document.getElementById('current-slide').textContent = currentSlide + 1;
            
            // Update navigation buttons
            document.getElementById('prevBtn').disabled = currentSlide === 0;
            document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
        }
        
        function changeSlide(direction) {
            if (direction === 1 && currentSlide < totalSlides - 1) {
                showSlide(currentSlide + 1);
            } else if (direction === -1 && currentSlide > 0) {
                showSlide(currentSlide - 1);
            }
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                e.preventDefault();
                changeSlide(1);
            } else if (e.key === 'ArrowLeft') {
                e.preventDefault();
                changeSlide(-1);
            }
        });
        
        // Initialize
        showSlide(0);
        
        // Touch/swipe support for mobile
        let startX = 0;
        let endX = 0;
        
        document.addEventListener('touchstart', function(e) {
            startX = e.touches[0].clientX;
        });
        
        document.addEventListener('touchend', function(e) {
            endX = e.changedTouches[0].clientX;
            handleSwipe();
        });
        
        function handleSwipe() {
            const swipeThreshold = 50;
            const swipeDistance = startX - endX;
            
            if (Math.abs(swipeDistance) > swipeThreshold) {
                if (swipeDistance > 0) {
                    // Swipe left - next slide
                    changeSlide(1);
                } else {
                    // Swipe right - previous slide
                    changeSlide(-1);
                }
            }
        }
    </script>
</body>
</html>
