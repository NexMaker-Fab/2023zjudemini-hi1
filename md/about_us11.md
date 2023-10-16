<!DOCTYPE html>
<style>
    body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: 'Arial', sans-serif;
}

.container {
    position: relative;
    height: 100vh; /* 使用视口单位，确保容器占据整个视口高度 */
    background-color: #000;
    display: flex;
    align-items: flex-end; /* 将内容垂直对齐到底部 */
    justify-content: flex-end; /* 将内容水平对齐到右侧 */
    padding: 20px; /* 为了确保内容不会贴在屏幕边缘，可以添加一些内边距 */
}

.image {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: auto;
    opacity: 0.2; /* 可调整这个值来改变图片的透明度 */
}

.content {
    z-index: 1;
    width: 50%; /* 调整这个值可以改变文本区域的宽度 */
    background-color: rgba(255, 255, 255, 0.7); /* 这是一个半透明的背景色 */
    padding: 40px;
    border-radius: 20px;
}

h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
    border-bottom: 2px solid #000;
    padding-bottom: 10px;
}

.woohoo {
    font-size: 1.2em;
    font-weight: bold;
}

.description {
    margin-top: 20px;
}

</style>
<html lang="en">

<body>
    <div class="container">
        <img src="../_media/group.png" alt="Image" class="image">
        <div class="content">
            <h1>About us</h1>
            <p class="woohoo">Hello!! Here is Fivevolution! Our team is a 23-grade graduate student of industrial design from Polytechnic Institute, Zhejiang University.</p>
            <p class="description">Our team consists of five people with professional backgrounds in industrial design, machinery, Computer science and technology, etc., who work hard together, learn from each other, and look forward to making the coolest things！</p>
        </div>
    </div>
</body>
</html>
